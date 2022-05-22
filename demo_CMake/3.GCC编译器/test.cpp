#include <iostream>
#include <eigen3/Eigen/Core>
#include <eigen3/Eigen/LU>
#include <Eigen/Dense>
using namespace std;

int main()
{
	cout << "This is my first cpp program in Linux C++" << endl;
	int a = 2;
	int i = a + 2;

	Eigen::MatrixXd A = Eigen::MatrixXd::Zero(5, 2);
	A << 2, 3,
		3, 7,
		2, 8,
		6, 6,
		0, 9;

	cout << A.block(0, 0, 4, 1) << endl
		 << endl;

	return 0;
}
