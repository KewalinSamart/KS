#ifndef FUNNYVECTOR_H
#define FUNNYVECTOR_H

struct FunnyVector{

	std::vector<int> v;
	int threadhold = 0;

	FunnyVector();
	FunnyVector(int);

	int size();
	std::vector<int> push_back(int);
	std::vector<int> get();
};

#endif

// solution code
/*
#pragma once
#include <algorithm>
#include <numeric>
#include <utility>
#include <vector>

struct FunnyVector {
private:
  int size_;
  int sum_ = 0;
  std::vector<int> v_;

public:
  FunnyVector(int size) : size_(size) {};
  void push_back(int i);
  auto get();
  auto size();
};
*/
