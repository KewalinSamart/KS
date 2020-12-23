/*
Python lists have a handy feature where you can use negative indices to get at elements counting from the end of the list. x[-1] returns the last element in x and x[-2] returns the penultimate element and so on. Implement a struct named "PythonicIntVector" in the files "PythonicIntVector.h" and "PythonicIntVector.cpp" that supports the push_back and at methods of a vector of ints. However, be sure to add the functionality of negative indices.

Don't forget that the at method still should throw exceptions for invalid indices (just like in Python)!
*/

#include <vector>
#include "PythonicIntVector.h"

PythonicIntVector::PythonicIntVector(){
  v = {};
  size_vect = static_cast<int>(v.size());
}

void PythonicIntVector::push_back(int n){
  v.push_back(n);
  size_vect = static_cast<int>(v.size());
}

int PythonicIntVector::at(int m){
  if (m < 0){
    if (m < -size_vect){
      throw std::out_of_range("\n");
    }
    return v[m+size_vect];
  }else{
    if (m > (size_vect-1)){
      throw std::out_of_range("\n");
    }
    return v[m];
  }
}

// solution code
/*
#include "PythonicIntVector.h"

void PythonicIntVector::push_back(int value) {
  data.push_back(value);
}

int & PythonicIntVector::at(int index) {
  if (index < 0) {
    index = static_cast<int>(data.size()) + index;
  }
  return data.at(index);
}
*/
