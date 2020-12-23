/*
Write a function, named seriesOfLetters, that takes a reference to a vector of chars and returns nothing.
The function should modify the vector to contain a series of letters increasing from the smallest letter
(by ASCII value) in the vector. Note, the vector should not change in size, and the initial contents of
the vector (excepting the smallest letter) do not matter.

You should be using the STL algorithms to achieve this, full credit is only possible if your solution
doesn't have any looping constructs (no "while" or "for" keywords anywhere in the solution).
If a URL you are citing has such a word, add an interupting space like: https://www.programiz.com/cpp-programming/fo r-loop
*/

#include <algorithm>
#include <functional>
#include <vector>
#include <numeric>


void seriesOfLetters(std::vector<char> &v) {
  int min_ele = *min_element(v.begin(), v.end());
  std::vector<char> &p = v;
  p.resize(static_cast<int>(v.size()));
  std::iota(std::begin(p), std::end(p), min_ele);
}

//https://stackoverflow.com/questions/17694579/use-stdfill-to-populate-vector-with-increasing-numbers

// solution code
/*
#include <vector>
#include <numeric>
#include <algorithm>

void seriesOfLetters(std::vector<char> & vec) {
  char smallest = *std::min_element(vec.begin(), vec.end());
  std::iota(vec.begin(), vec.end(), smallest);
}
*/
