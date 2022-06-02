#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ofstream os{ "numbers.txt" };
	if (!os) {
		cerr << "파일 오픈에 실패하였습니다" << endl;
		exit(1);
	}
	for (int i = 0; i < 100; i++)
		os << i << "";
	return 0;

// 객체 os가 범위를 벗어나면 ofstream 소멸자가 파일을 닫는다
}