#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

class TempData {
public:
	int hour;
	double temperature;
};

int main()
{
	ifstream is{ "temp.txt" };
	if (!is) {		// ! 연산자 오버로딩
		cerr << "파일 오픈에 실패하였습니다" << endl;
		exit(1);
	}
	vector<TempData> temps;

	int hours;
	double temperature;
	while (is >> hour >> temperature) {
		temps.push_back(TempData{ hour, temperature });
	}
	for (TempData t : temps) {
		cout << t.hour << "시: 온도" << t.temperature << endl;
	}
	return 0;
}