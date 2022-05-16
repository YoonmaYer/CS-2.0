#include <iostream>
#include <string>
using namespace std;
// 객체 생성을 위해 클래스가 필요
class Circle { // 클래스의 이름은 대문자로 시작하는것이 관례
public: // 접근 지정자
	int radius; // 멤버 변수
	string color;

	double calcArea() { // 멤버 함수 = 메서드, 카멜케이스
		return 3.14 * radius * radius;
	}
	string pizzaColor() {
		return color;
	}
};

int main() {
	Circle pizza1, pizza2, pizza3, pizza4; // 객체 생성

	pizza1.radius = 10;
	pizza1.color = "red";
	cout << "피자의 면적 및 색깔 = " << pizza1.calcArea() << ", " << pizza1.pizzaColor() << "\n";

	pizza2.radius = 100;
	pizza2.color = "green";
	cout << "피자의 면적 및 색깔 = " << pizza2.calcArea() << ", " << pizza2.pizzaColor() << "\n";

	pizza3.radius = 50;
	pizza3.color = "blue";
	cout << "피자의 면적 및 색깔 = " << pizza3.calcArea() << ", " << pizza3.pizzaColor() << endl;

	pizza4.radius = 5;
	pizza4.color = "olive";
	cout << "피자의 면적 및 색깔 = " << pizza4.calcArea() << ", " << pizza4.pizzaColor() << "\n";

	return 0;

}