/*
Write a function, named onlyNumbers, that takes a const reference to a string and
returns a string composed only of the characters from the original string that are digits.

You should be using the STL algorithms to achieve this, full credit is only possible
if your solution doesn't have any looping constructs (no "while" or "for" keywords anywhere in the solution).
If a URL you are citing has such a word, add an interupting space like: https://www.programiz.com/cpp-programming/fo r-loop
*/

#include <algorithm>
#include <string>
#include <iterator>
#include <locale>
std::string onlyNumbers(std::string source ) {
  source.erase(std::remove_if(source.begin(), source.end(),
                            [](char c) { return !std::isdigit(c); }),
             source.end());
  return source;
}

//http://forums.codeguru.com/showthread.php?559457-RESOLVED-Leave-only-numeric-characters-in-std-string

// solution code
/*
#include <string>
#include <algorithm>
#include <iterator>
#include <cctype>

std::string onlyNumbers(const std::string & input) {
  std::string result;
  std::copy_if(input.begin(), input.end(), std::back_inserter(result), isdigit);
  return result;
}
*/
