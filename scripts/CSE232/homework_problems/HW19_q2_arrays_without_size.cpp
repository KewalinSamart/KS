/*
One trick in C to work with arrays (and to not have to pass a size in a second argument with the array) is to have the array somehow encode 
where it ends inside the array. In C-style strings (https://www.learncpp.com/cpp-tutorial/66-c-style-strings/), the null terminator character ('\0') 
denotes the end of the string (though the character array can be longer).

Lets write a function that uses this approach. I have two arrays of doubles that will represent stock prices. 
Instead of specifying the size of the array, the first negative stock price indicates that the rest of the array doesn't contain actual data. 
Write a copy function named "copy_stock_prices" that takes two arguments: a pointer to the begining of the source array and a pointer to the beginning of 
the destination array. It should only copy over the valid data (and the terminating value).
*/

#include <algorithm>
#include <iterator>


void copy_stock_prices (double *ary1, double *ary2){
  double * &ary3 = ary2;
  int index_neg = 0;
  int i = 0;
  while (1) {
    ++i;
    if (ary1[i] < 0){
      index_neg = i;
      break;
    }
  }
  std::copy(ary1, ary1+index_neg+1,ary3);
}

// solution code
/*
void copy_stock_prices(double * source, double * dest) {
  while (true) {
    *dest = *source;
    ++dest;
    ++source;
    if (*source < 0)
      break;
  }
  // Copy terminal
  *dest = *source;
}
*/
