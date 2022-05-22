#include "Solider.h"
#include "Gun.h"

void test()
{
    Gun *gun = new Gun("AK47");
    Solider solider("James");
    solider.addGun(gun);
    solider.addBulletToGun(10);
    solider.fire();
}

int main(int argc, char **argv)
{
    std::cout << "This is a test" << std::endl;
    test();
    return 0;
}