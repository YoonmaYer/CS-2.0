#include <iostream>
using namespace std;

class Square {
public:
	int width;
	int height;

	int calcArea() {
		return width * height;
	}
};

int main() {
	Square obj;

	obj.width = 5;
	obj.height = 5;

	cout << "사각형의 면적 = " << obj.calcArea() << "\n";
		return 0;
}