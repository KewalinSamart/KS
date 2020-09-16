/* Another common technique to avoid having to pass a separate argument for the array's size is to make the first element of the array 
hold its size. Of course this only works for numeric arrays, but arrays of numbers are the most common kind.

Write the "copy_stock_prices" like before, but the first element contains the number of prices in the array, only copy those. */

#include <algorithm>
#include <iterator>


void copy_stock_prices (double *ary1, double *ary2){
  double * &ary3 = ary2;
  int index = 0;
  int i = 0;
  int n = ary1[0];
  std::copy(ary1, ary1+n+1,ary3);
}

// solution code
/*
#include <algorithm>
#include <iterator>


void copy_stock_prices (double *ary1, double *ary2){
  double * &ary3 = ary2;
  int index = 0;
  int i = 0;
  int n = ary1[0];
  std::copy(ary1, ary1+n+1,ary3);
}
*/
