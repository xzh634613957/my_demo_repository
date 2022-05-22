#include "Swap.h"

int main(int argc, char **argv)
{
    Swap mySwap(5, 2);

    std::cout << "交换前：";
    mySwap.Print();

    std::cout << "交换后：";
    mySwap.RunSwap();
    mySwap.Print();

    return 0;
}