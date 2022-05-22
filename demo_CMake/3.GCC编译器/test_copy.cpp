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

	// Eigen::MatrixXd A = Eigen::MatrixXd::Zero(3, 3);
	// A << 0.5, 0.1, 0,
	// 	1, 0, 0.1,
	// 	0.11, 0, 0.1;

	// cout << A.block(0, 0, 3, 2) << endl;

	// cout << A.transpose() << endl;
	Eigen::VectorXd Ureal = Eigen::VectorXd::Zero(2);
	Ureal(0) = 2;
	Ureal(1) = 2;
	cout << Ureal << endl;

	return 0;
}
