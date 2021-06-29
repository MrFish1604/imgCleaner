#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

#define DEFAULT_EPS 150

using namespace cv;
using namespace std;

int moyPixel(Vec3b pixel)
{
    return (pixel[0] + pixel[1] + pixel[2])/3;
}

int main(int argc, char const *argv[])
{
	string filename;
	if(argc>1)
		filename = argv[1];
	else
	{
		cout << "Usage : imgCleaner FILENAME [sensitivity]" << endl;
		return 0;
	}

	Mat mat = imread(filename);
	if(mat.empty())
	{
		cout << "Can't open the image" << endl;
		return 1;
	}

	int epsilon = argc>2 ? atoi(argv[2]) : DEFAULT_EPS;

	Size size = mat.size();
    for(int r=0; r<size.height; r++)
    {
        for(int c=0; c<size.width; c++)
        {
            Vec3b &pixel = mat.at<Vec3b>(r,c);
            if(moyPixel(pixel) < epsilon)
            {
                pixel = Vec3b(0, 0, 0);
            }
            else
            {
                pixel = Vec3b(255, 255, 255);
            }
        }
    }

	namedWindow(filename, WINDOW_NORMAL);
	imshow(filename, mat);
	int k = waitKey(0);
	while(!(k=='q' || k=='s'))
		k = waitKey(0);
	destroyWindow(filename);
	if(k=='s')
	{
		string newFile;
		cout << "New file's name : ";
		cin >> newFile;
		imwrite(newFile, mat);
	}
	return 0;
}