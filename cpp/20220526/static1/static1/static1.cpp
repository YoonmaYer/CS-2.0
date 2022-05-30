#include <iostream>
#include <string>
using namespace std;

class Circle {
	int x, y;
	int radius;

public:
	static int count;
	Circle() : x { 0 }, y{ 0 }, radius{ 0 } {
		count++;
	}
	Circle(int x, int y, int r) : x{ x }, y{ y }, radius{ r } {
		count++;
	}
	~Circle() {
		count--;
	}
};

int Circle::count = 0;

int main()
{
	Circle c1;
	cout << "지금까지 생성된 원의 개수 = " << Circle::count << endl;

	Circle c2(100, 100, 30);
	cout << "지금까지 생성된 원의 개수 = " << Circle::count << endl;

	return 0;

}