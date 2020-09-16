/* We spent a lot of time implementing a stack in various ways, but if you actually need a stack for some purpose, the STL has you covered. See: https://en.cppreference.com/w/cpp/container/stack

Write a function called "reverse_stack" that takes a std::stack and returns a new stack with the reversed order of elements within (meaning what was on the top of the parameter stack is on the bottom of the returned stack).

Put your code in a file named "code.h". */

#pragma once

#include <stack>

template <typename T>
std::stack<T> reverse_stack(std::stack<T> original) {
  std::stack<T> result;
  while (!original.empty()) {
    result.push(original.top());
    original.pop();
  }
  return result;
}
