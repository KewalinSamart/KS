/*
You're going to write a vector class called "FunnyVector", because it's kind of like a vector, but a funny one. For starters, it can only contain numbers (ints, to be precise). Also, unlike std::vector, FunnyVector keeps all its ints in sorted order. Even worse, when you call size() on it, it gives the sum of its elements, not the number of elements. And to top it all off, if you put in numbers so that the sum goes over a threshold, all the numbers are erased. Fortunately, this threshold can be set when a FunnyVector is created. And for the pruposes of testing, you can get() a std::vector<int> from a FunnyVector to see its contents.

Provide the interface to your FunnyVector in funny_vector.hpp. You should write the implementation of FunnyVector in funny_vector.cpp

See the sample test case for how a FunnyVector should behave.
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
#include "funny_vector.hpp"

// default constructor
FunnyVector::FunnyVector(){
  threadhold = 0;
}

FunnyVector::FunnyVector(int val){
  threadhold = val;
}

int FunnyVector::size(){
   int sum = std::accumulate(v.begin(), v.end(), 0);
   return sum;
}

std::vector<int> FunnyVector::push_back(int num){
  v.push_back(num);
  int sum1 = std::accumulate(v.begin(), v.end(), 0);
  if ( sum1 > threadhold) {
    v.clear();
  }
  return v;
}

std::vector<int> FunnyVector::get(){
  std::sort(v.begin(), v.end());
  return v;

}

// solution code
/*
#include "funny_vector.hpp"
void FunnyVector::push_back(int i) {
  sum_ += i;
  if (sum_ < size_)
    v_.insert(std::lower_bound(std::begin(v_), std::end(v_), i), i);
  else {
    v_.clear();
    sum_ = 0;
  }
}

auto FunnyVector::get() { return v_; }
auto FunnyVector::size() { return std::accumulate(std::begin(v_), std::end(v_), 0); }
*/
