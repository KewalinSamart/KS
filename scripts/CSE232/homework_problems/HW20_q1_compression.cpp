/* We have an array of doubles that sometimes has runs of numbers that are very close to each other 
(where one number is within 1 unit of its neighbor). 
These run's aren't important to the work we are doing so we want you to write a function that will compress the array to just hold 
the values are are more than one unit away from its neighoring element. Of course, the function can't actually change the size of the array, 
so instead return the number of elements in the array post-compression.

Write a function, named "Compress", that takes an array of doubles and an int denoting the number of elements in that array. 
The function should modify the array to no longer have elements that are within 1.0 of the preceding element. 
The function should return the remaining number of elements (as an int).

You should be using the STL algorithms to achieve this, credit is only given if your solution doesn't have any looping constructs 
(no "while" or "for" keywords anywhere in the solution, nor the use of "goto" or "for_each"). If a URL you are citing has such a word, 
add an interupting space like: https://www.programiz.com/cpp-programming/fo r-loop
*/

#include <algorithm>
#include <iterator>
#include <array>
#include <vector>
#include <numeric>
#include <cmath>


int Compress(double ary[], int num){
  double old = 0;
  bool ch;
  int Num = num;
  std::remove_if(ary, ary+num, [&old,&ch,&Num] (const double& now){
    ch = false;
    if(fabs(old - now) < 1){
      ch = true;
      Num--;
    }
    old = now;
    return ch;
  });
  return Num;
}

// solution code
/*
#include <algorithm>
#include <cmath>

int Compress(double * array, int size) {
  double * end = std::unique(array, array + size, 
      [](const double & a, const double & b) {
    return std::abs(a - b) < 1.0;});
  return end - array;
}
*/
