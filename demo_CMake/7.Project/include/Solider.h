#pragma once
#include <iostream>
#include "Gun.h"

class Solider
{
public:
    Solider(std::string name)
        : _name(name), _ptr_gun(nullptr) {}

    ~Solider();

    void addGun(Gun *ptr_gun);
    void addBulletToGun(const int &num);
    bool fire() const;

private:
    std::string _name;
    Gun *_ptr_gun;
};