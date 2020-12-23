/*
 Write a struct named "SafePtrToDouble" that is used to provide a (slightly) safer way to work with pointers (you'll learn better solutions in CSE 335). One major problem with pointers is that they can be dereferenced even when they are nullptr (meaning they have an invalid address to dereference). A nullptr value for a pointer is used to indicate that the pointer isn't pointing at a valid memory location. But it is up to the programmer to confirm that a pointer is not nullptr before dereferencing it. But programmers make mistakes!

This struct should accept as a converting constructor a pointer to a double. This struct must define two methods that both have no parameters:

"Dereference": this method should act like a dereference of the pointer the struct was created with. However, if the pointer is nullptr then a std::logic_error should be thrown
"Value": this method should return the value of the pointer.
Your code should be in two files: "SafePtrToDouble.cpp" and "SafePtrToDouble.h". Also note, a knowledge of pointers and references will be needed to solve this problem.
*/

#ifndef SAFEPTRTODOUBLE_H
#define SAFEPTRTODOUBLE_H

struct SafePtrToDouble{
  double *ptr;

  SafePtrToDouble(double *); // constructor

  double &Dereference();
  double *Value();

};

#endif

// solution code
/*
#pragma once

struct SafePtrToDouble {
  double * ptr_to_dbl;
  SafePtrToDouble(double * p_to_d) : ptr_to_dbl(p_to_d) {};
  double & Dereference();
  double * Value();
};
*/
