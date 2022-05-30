#include <iostream>
#include <string>
using namespace std;

int main() {
	string s1 = "Rogue One: ";
	string s2 = "A Star Wars Story";

	string s3;
	s3 = s1 + s2;

	cout << "s1= " << s1 << endl;
	cout << "s2= " << s2 << endl;
	cout << "s1+s2= " << s3 << endl;
	cout << "s1==s2 " << boolalpha << (s1 == s2) << endl;
	return 0;
}