/*
You need to make a custom type called a "HousePrice". This type represents an address and its estimated Zillow price. It has two data members, a string with the house's address (named "address") and a double representing the price Zillow estimates for the house (named "price").

Additionally, you need to write a function (not a member function, a regular one) that takes a const reference to a vector of HousePrice and returns the average of the price in that vector as a double. This function is called "get_average_price".

Use "zillow.h" as your header file and "zillow.cpp" as your implementation file.
*/

#include<string>
#include<vector>

#include "zillow.h"


double get_average_price(std::vector<HousePrice> &vec)
{
double sum = 0;
int size = static_cast<int>(vec.size());
for(auto i =0; i < size ; i++) {
sum+=vec[i].price;
}

double avg_price = sum/size;
return avg_price;
}

// solution code
/*
#include "zillow.h"

#include <string>
#include <vector>
#include <numeric>

double get_average_price(std::vector<HousePrice> house_prices) {
  double sum = std::accumulate(house_prices.begin(), house_prices.end(), 0.0,
    [](double tally, HousePrice hp) {return tally + hp.price;});
  return sum / static_cast<double>(house_prices.size());
}
*/
