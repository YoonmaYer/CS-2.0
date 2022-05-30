#include <iostream>
#include <time.h>
using namespace std;

int main()
{
	int* ptr;	// 동적 메모리를 가리키는 포인터

	srand(time(NULL));
	ptr = new int[10]; // 동적 메모리 할당

	for (int i = 0; i<10; i++)
		ptr[i] = rand();

	for (int i = 0; i<10; i++)
		cout << ptr[i] << "";

	delete[] ptr; // 동적 메모리 반납
	cout << endl;
	return 0;
}