#include "Gun.h"

void Gun::addBullet(const int &num)
{
    _bullet_count += num;
}

bool Gun::shoot()
{
    if (_bullet_count <= 0)
    {
        return false;
    }

    --_bullet_count;
    return true;
}

int Gun::getBulletCount() const
{
    return _bullet_count;
}

std::string Gun::getGunType() const
{
    return _type;
}