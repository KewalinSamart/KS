/*
Python lists have a handy feature where you can use negative indices to get at elements counting from the end of the list. x[-1] returns the last element in x and x[-2] returns the penultimate element and so on. Implement a struct named "PythonicIntVector" in the files "PythonicIntVector.h" and "PythonicIntVector.cpp" that supports the push_back and at methods of a vector of ints. However, be sure to add the functionality of negative indices.

Don't forget that the at method still should throw exceptions for invalid indices (just like in Python)!
*/

#ifndef PYTHONINTVECT_H
#define PYTHONINTVECT_H

#include <vector>

struct PythonicIntVector{
  std::vector<int> v;
  int size_vect = static_cast<int>(v.size());

  PythonicIntVector();

  void push_back(int);
  int at(int);
};

#endif

// solution code
/*
#pragma once
#include <vector>

struct PythonicIntVector {
  std::vector<int> data;
  PythonicIntVector() = default;
  void push_back(int);
  int & at(int);
};
*/
