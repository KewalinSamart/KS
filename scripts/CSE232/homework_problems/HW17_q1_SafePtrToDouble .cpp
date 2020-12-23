/*
 Write a struct named "SafePtrToDouble" that is used to provide a (slightly) safer way to work with pointers (you'll learn better solutions in CSE 335). One major problem with pointers is that they can be dereferenced even when they are nullptr (meaning they have an invalid address to dereference). A nullptr value for a pointer is used to indicate that the pointer isn't pointing at a valid memory location. But it is up to the programmer to confirm that a pointer is not nullptr before dereferencing it. But programmers make mistakes!

This struct should accept as a converting constructor a pointer to a double. This struct must define two methods that both have no parameters:

"Dereference": this method should act like a dereference of the pointer the struct was created with. However, if the pointer is nullptr then a std::logic_error should be thrown
"Value": this method should return the value of the pointer.
Your code should be in two files: "SafePtrToDouble.cpp" and "SafePtrToDouble.h". Also note, a knowledge of pointers and references will be needed to solve this problem.
*/

#include <stdexcept>

#include "SafePtrToDouble.h"

SafePtrToDouble::SafePtrToDouble(double *a){
  ptr = a;
}

double &SafePtrToDouble::Dereference(){
  if(ptr == nullptr){
    throw std::logic_error("invalid address\n");
  }else{
    return *ptr;
  }
}

double *SafePtrToDouble::Value(){
  return ptr;
}

// solution code
/*
#include <stdexcept>
#include "SafePtrToDouble.h"


double & SafePtrToDouble::Dereference() {
  if (ptr_to_dbl == nullptr) {
    throw std::logic_error("Attempting to dereference a null ptr");
  }
  return *ptr_to_dbl;
}

double * SafePtrToDouble::Value() {
  return ptr_to_dbl;
}
*/
