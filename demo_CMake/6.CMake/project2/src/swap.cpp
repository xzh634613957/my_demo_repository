#include "Swap.h"

Swap::Swap(int a = 0, int b = 0)
    : _a(a), _b(b)
{
}

void Swap::RunSwap()
{
    int temp = 0;
    temp = _a;
    _a = _b;
    _b = temp;
}

void Swap::Print()
{
    std::cout << "a = " << _a << ", b = " << _b << std::endl;
}