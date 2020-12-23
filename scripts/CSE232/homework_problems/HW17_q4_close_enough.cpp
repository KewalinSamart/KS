/*
I'm interested in knowing if there are two adjacent strings in a list that are very similar to each other. For instance, "Zach" and "Zack" are only one character apart.

Write a function, named "CloseEnough" that takes a const reference to a vector of strings and an int. The vector is a list of strings (each of the same length). The int represents how many characters can be different between any two strings next to each other. This function should return the index (an int) of the string that is within the second arguments distance to the next string in the vector. If no index fulfills this criteria, it should return -1.
*/
/*
Example:

const std::vector<std::string> more_words {
  "this is a sentence.",
  "this is also words ",
  "another line in one",
  "stuff words in open",
  "stuff words in OPEN",
  "whitespace\n\tagain  ",
};
*/
/*
ASSERT_EQ(CloseEnough(more_words, 5), 3);

Index 3: "stuff words in open"
is only distance 4 fron the next string
Index 4: "stuff words in OPEN",
so the function returns 3
*/
/*
ASSERT_EQ(CloseEnough(more_words, 0), -1);
// No index is within 0 distance of the next string.
You should be using the STL algorithms to achieve this, credit is only possible if your solution doesn't have any looping constructs (no "while" or "for" keywords anywhere in the solution). You also can't use the "for_each" or "for_each_n" algorithms. If a URL you are citing has such a word, add an interupting space like: https://www.programiz.com/cpp-programming/fo r-loop
*/

#include <stdexcept>
#include <iostream>
//#include "SafePtrToDouble.h"
//#include "PythonintVector.hpp"
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool best(std::string now, std::vector<std::string>::iterator& next, int maximum)
{
    std::string next_str = *next;
    std::string::iterator ch_com = next_str.begin();
    auto COUNT = std::count_if(now.begin(), now.end(), [&ch_com](char ch){ return ch != *ch_com++ ;});
    if(COUNT <= maximum)
        return true;
    next++;
    return false;
}
int CloseEnough(std::vector<std::string> sentences, int maximum)
{
    std::vector<std::string>::iterator next = sentences.begin();
    next++;
    auto FIND = std::find_if(sentences.begin(), sentences.end() - 1, [&next,maximum](string now) { return best(now,next,maximum); });
    if(FIND == sentences.end()-1)
        return -1;
    return (int) ( FIND - sentences.begin() );
}

// solution code
/*
#include <vector>
#include <algorithm>
#include <string>
#include <iterator>
#include <numeric>


int NumLettersDiff(const std::string & s1, const std::string & s2) {
  return std::inner_product(s1.begin(),
    s1.end(),
    s2.begin(),
    0,
    std::plus<int>(),
    [](char a, char b){
      return static_cast<int>(a != b);
  });
}

int CloseEnough(const std::vector<std::string> & words, int distance) {
  auto iter = std::adjacent_find(
    words.begin(),
    words.end(),
    [distance] (const std::string & a, const std::string & b) {
      return NumLettersDiff(a, b) <= distance;
  });
  if (iter == words.end()) {
    return -1;
  }
  return std::distance(words.begin(), iter);
}
*/
