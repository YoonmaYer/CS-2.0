#include <string>
#include <iostream>
using namespace std;

int main() {
	string address;
	cout << "주소를 입력하시오";
	getline(cin, address);
	cout << "안녕! " << address << "에 사시는 분" << endl;

	return 0;
}