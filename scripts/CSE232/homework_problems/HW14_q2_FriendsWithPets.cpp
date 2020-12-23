/*
Write a function named "FriendsWithPets" that takes a const reference to a std::map of my friends names (std::string) to the number of pets they own (int) and returns the number of friends (int) that have at least one pet.



You should be using the STL algorithms to achieve this, credit is only given if your solution doesn't have any looping constructs (no "while" or "for" keywords anywhere in the solution). If a URL you are citing has such a word, add an interupting space like: https://www.programiz.com/cpp-programming/fo r-loop
*/

// solution code

#include <map>
#include <string>
#include <algorithm>
#include <utility>

int FriendsWithPets(const std::map<std::string, int> & friend_to_pets) {
  return std::count_if(friend_to_pets.begin(), friend_to_pets.end(),
    [] (const std::pair<std::string, int> & entry) {return entry.second > 0;});
}
