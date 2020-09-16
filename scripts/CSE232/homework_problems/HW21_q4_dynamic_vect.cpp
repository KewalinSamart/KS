/* Write a class named "DynamicVector" in a header only library (DynamicVector.h).

This class is very similar to std::vector<int>. It needs to support push_back, at, reserve, capacity, size, and data methods 
(just like vector does). It also needs to support the Rule of three member functions as well as one additional member function: 
a constructor that takes a pointer to a dynamically allocated array and an int (denoting the size of that array). 
The class should use this array for its internal data structure (similar to the Stack example from the lecture). 
However, if the reserve method is called with a larger capacity than the array has, a new dynamically allocated array should be created. */

#ifndef DYNAMICVECTOR_H
#define DYNAMICVECTOR_H

#include <vector>
#include <array>
#include <iterator>
#include <stdexcept>
#include <algorithm>

class DynamicVector {
  private:
    int * ary_;
    int size_ = 0;
    int capacity_ = 0;
  
  public:
  DynamicVector() = default;
  DynamicVector(int * ary, int size) : ary_(ary), size_(size), capacity_(size) {};
  
  DynamicVector(const DynamicVector &s);   // copy
  ~DynamicVector();                // destructor
  DynamicVector& operator=(DynamicVector);
  
  
  void push_back(int);
  int &at(int);
  int* data();
  void reserve(int);
  int size();
  int capacity();
  
};

int &DynamicVector::at(int i) {
    if (i >= size_) {
        throw std::out_of_range("out_of_range");
    }
    return ary_[i];
}

int DynamicVector::size(){
  return size_;
}

int* DynamicVector::data(){
  return ary_;
}

//https://www.cse.msu.edu/~cse232/Weekly/week13/examples/19.7-stackDynamicTemplate/stack.h
void DynamicVector::reserve(int i){
  int *new_ary;
  if (i > capacity_){
    capacity_ = i;
    new_ary = new int[i];
    std::copy(ary_, ary_+size_, new_ary);
    std::swap (new_ary, ary_);
    delete [] new_ary;
  }else{
    capacity_ = size_;
  }
}

int DynamicVector::capacity(){
  return capacity_;
}

void DynamicVector::push_back(int num){
  int *new_ary;
  if (size_ == capacity_){
    size_ += 1;
    capacity_ = size_;
    new_ary = new int[size_];
    std::copy(ary_, ary_+size_, new_ary);
    // stl swap, not Stack swap
    std::swap (new_ary, ary_);
    delete [] new_ary;
    ary_[size_-1] = num;
  } else if (size_ < capacity_) {
    size_ += 1;
    ary_[size_-1] = num;
  }
}

DynamicVector::DynamicVector(const DynamicVector &s){
  ary_ = new int[s.size_];
  std::copy(s.ary_, s.ary_ + s.size_, ary_);
  size_ = s.size_;
  capacity_ = s.capacity_;
}

DynamicVector::~DynamicVector(){
  delete [] ary_;
}

DynamicVector& DynamicVector::operator=(DynamicVector s){
  if (this != &s){
    delete [] ary_;
    size_ = s.size_;
    capacity_ = s.capacity_;
    ary_ = new int[s.size_];
    std::copy(s.ary_, s.ary_ + s.size_, ary_);
  }
  return *this;
}

#endif


// solution code
/*
#pragma once
#include <algorithm>
#include <stdexcept>
	

class DynamicVector {
 private:
  int * array_ = nullptr;
  int size_ = 0;
  int capacity_ = 0;
 public:
  DynamicVector(int * array, const int & size);
  DynamicVector(const DynamicVector & x);
  DynamicVector& operator=(DynamicVector x);
  ~DynamicVector();
  int & at(int index);
  void reserve(int capacity);
  int * data();
  int capacity();
  int size();
  void push_back(const int & x);
};
void DynamicVector::push_back(const int & x) {
  if (capacity_ == size_) {
    throw std::out_of_range("no room in vector for push_back");
  }
  array_[size_++] = x;
}
int & DynamicVector::at(int index) {
  if (index >= size_) {
    throw std::out_of_range("index is too large");
  }
  return array_[index];
}

DynamicVector::DynamicVector(int * array, const int & size) {
  array_ = array;
  size_ = size;
  capacity_ = size;
}

void DynamicVector::reserve(int capacity) {
  if (capacity <= capacity_) {
    return;
  }
  int * new_array = new int[capacity];
  std::copy(array_, array_ + size_, new_array);
  capacity_ = capacity;
  delete [] array_;
  array_ = new_array;
}

int * DynamicVector::data() {
  return array_;
}

int DynamicVector::capacity() {
  return capacity_;
}

int DynamicVector::size() {
  return size_;
}

DynamicVector::DynamicVector(const DynamicVector & x) {
  size_ = x.size_;
  capacity_ = x.capacity_;
  array_ = new int[capacity_];
  std::copy(x.array_, x.array_ + size_, array_);
}

DynamicVector& DynamicVector::operator=(DynamicVector x) {
  *this = x;
  return *this;
}

DynamicVector::~DynamicVector() {
  delete [] array_;
}
*/
