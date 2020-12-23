#ifndef ZILLOW_H
#define ZILLOW_H

#include<string>
using std::string;
#include<vector>

struct HousePrice{
  string address;
  double price;

};

double get_average_price(const std::vector<HousePrice> &c);

#endif

// solution code
/*
#pragma once

#include <string>
#include <vector>

struct HousePrice {
  std::string address;
  double price;
};

double get_average_score(std::vector<HousePrice> ratings);
*/
