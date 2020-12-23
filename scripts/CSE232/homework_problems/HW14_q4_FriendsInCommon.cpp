/*
Write a function, named "FriendsInCommon", that takes two constant references to a set of strings (where each string is a name of a friend). This function should return a set of names consisting of the names that are in both arguments.



You should be using the STL algorithms to achieve this, credit is only given if your solution doesn't have any looping constructs (no "while" or "for" keywords anywhere in the solution). If a URL you are citing has such a word, add an interupting space like: https://www.programiz.com/cpp-programming/fo r-loop
*/

// solution code

#include <string>
#include <set>
#include <algorithm>
#include <iterator>

std::set<std::string> FriendsInCommon(const std::set<std::string> & friends_a,
                                      const std::set<std::string> & friends_b) {
  std::set<std::string> common;
  std::set_intersection(friends_a.begin(), friends_a.end(),
		   friends_b.begin(), friends_b.end(),
		   std::inserter(common, common.begin()));
	return common;
}
