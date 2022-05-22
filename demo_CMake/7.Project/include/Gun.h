#pragma once
#include <iostream>
#include <string>

class Gun
{
public:
    Gun(std::string type, int bullet_count = 0)
        : _type(type), _bullet_count(bullet_count) {}

    ~Gun() {}

    void addBullet(const int &num);
    bool shoot();
    int getBulletCount() const;
    std::string getGunType() const;

private:
    std::string _type;
    int _bullet_count;
};