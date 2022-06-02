#include <iostream>
#include <fstream>

int main()
{
	using namespace std;

	ofstream os("sample.txt", ios::app);
	if (!os)
	{
		cerr << "파일 오픈에 실패하였습니다" << endl;
		exit(1);
	}

	os << "추가되는 줄#1" << endl;
	os << "추가되는 줄#2" << endl;

	return 0;
}