/* Write a templated class named "EveryOther" that behaves much like std::vector (in the file named "everyother.h"). It has a member function called "push_back", but only every other call to the member function actually does anything (actually pushed the element to the end of the structure). The class should have a default constructor and a constructor that takes an initializer list (be sure that you only add every other element). The other function that EveryOther needs to support is the operator<<, see the test cases for formating.

This class is templated so that instances like EveryOther<char> and EveryOther<vector<int>> are supported.*/

#pragma once

#include <initializer_list>
#include <vector>
#include <iostream>
#include <iterator>
#include <algorithm>

template <typename ElementType>
class EveryOther {
 private:
  std::vector<ElementType> vec_;
  bool works_ = true;
  
 public:
  EveryOther()=default;
  EveryOther(std::initializer_list<ElementType> lst) {
    works_ = true;
    for (auto & e : lst) {
      if (works_) 
        vec_.push_back(e);
      works_ = !works_;
    }
  }
  void push_back(ElementType e) {
    if (works_) 
      vec_.push_back(e);
    works_ = !works_;
  }
  int size() {
    return static_cast<int>(vec_.size());
  }
  friend std::ostream& operator<<(std::ostream &out, const EveryOther<ElementType> &eo){
    out << "EveryOther(";
    std::copy(eo.vec_.begin(), eo.vec_.end(),
	    std::ostream_iterator<ElementType>(out, ", "));
    out << ")";
    return out;
  }
};
