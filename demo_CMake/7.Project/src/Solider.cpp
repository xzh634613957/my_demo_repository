#include "Solider.h"

void Solider::addGun(Gun *ptr_gun)
{
    _ptr_gun = ptr_gun;
}

void Solider::addBulletToGun(const int &num)
{
    _ptr_gun->addBullet(num);

    std::cout << "Add bullet successfully.";
    std::cout << " Now the " << _ptr_gun->getGunType() << " have "
              << _ptr_gun->getBulletCount() << " bullets." << std::endl;
}

bool Solider::fire() const
{
    if (!_ptr_gun->shoot())
    {
        std::cout << "There is no bullet! Please add bullets." << std::endl;
        return false;
    }

    std::cout << _name << " fire!";
    std::cout << " Now the " << _ptr_gun->getGunType() << " have "
                << _ptr_gun->getBulletCount() << " bullets." << std::endl;
    return true;
}

Solider::~Solider()
{
    if (_ptr_gun)
    {
        delete _ptr_gun;
        _ptr_gun = nullptr;
    }
}