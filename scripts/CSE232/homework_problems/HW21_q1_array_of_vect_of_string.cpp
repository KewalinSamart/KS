/* Write a function called "Crazy", that takes two arguments an array of vectors of strings and a size_t indicating the array's size.

This program should return an int indicating the total number of characters in all the strings. */

#include <vector>
#include <string>
#include <array>
#include <iterator>

int Crazy(std::vector<std::string> *ary, size_t size_ary ){
  int num = 0;
  for (int i = 0; i < int(size_ary); i++ ){
    for (int n = 0; n < static_cast<int>(ary[i].size()); n++){
      num += static_cast<int>(size(ary[i][n]));
    }
  }
  
  return num;
}

// solution code
/*
#include <vector>
using std::vector;
#include <string>
using std::string;

int Crazy(vector<string> ary_vec_str[], size_t size) {
  int count  = 0;
  for (int i = 0; i < size; ++i) {
    for (const auto & str : ary_vec_str[i]) {
      count += str.size();
    }
  }
  return count;
}
*/
