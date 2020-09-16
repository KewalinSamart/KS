/*
Write a function, named "ArrayAdd" that takes two arrays (and their sizes) and returns a new array (really a pointer) 
to an array with the elements of the first array followed by the second. The parameters are a dynamically allocated int array 
(followed by an int denoting its size) and a second dynamically allocated int array (again, followed by its size). 
Be sure to delete the argument arrays when you are done adding them.

You should be using the STL algorithms to achieve this, credit is only given if your solution doesn't have any looping constructs 
(no "while" or "for" keywords anywhere in the solution, nor the use of "goto" or "for_each"). If a URL you are citing has such a word, 
add an interupting space like: https://www.programiz.com/cpp-programming/fo r-loop
*/

#include <algorithm>
#include <array>
#include <iterator>

int * ArrayAdd (int *ary1, int size1, int *ary2, int size2){
  int *ary = new int[size1 + size2];
    std::copy(ary1, ary1 + size1, ary);
    std::copy(ary2, ary2 + size2, ary + size1);
    delete [] ary1;
    delete [] ary2;
  return ary;
}

// solution code
/*
#include <algorithm>

int * ArrayAdd(int * array_a, int size_a, int * array_b, int size_b) {
  int new_size = size_a + size_b;
  int * result = new int [new_size];
  std::copy(array_a, array_a + size_a, result);
  std::copy(array_b, array_b + size_b, result + size_a);
  delete [] array_a;
  delete [] array_b;
  return result;
}
*/
