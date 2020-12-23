/*
Write a function, named "smallerThanPredecessor", that takes a reference to a vector of ints.
It should return an iterator pointing at the first element that is strictly smaller than the element
before it. You can assume that the vector has at least two elements. If no element qualifies,
return an iterator to one past the end of the vector.
*/

#include <vector>
#include <algorithm>
std::vector<int>::iterator smallerThanPredecessor(std::vector<int> &v){
  std::vector<int>::iterator smaller_ele = v.end();
  for (int i = 1; i < static_cast<int>(v.size()); ++i){
    if (v.at(i) < v.at(i-1)){
       smaller_ele = v.begin() + i;
       break;
    }
  }
return smaller_ele;
}

// solution code
/*
#include <vector>

std::vector<int>::iterator smallerThanPredecessor(std::vector<int> & vec) {
  std::vector<int>::iterator pred = vec.begin();
  std::vector<int>::iterator curr = pred + 1;
  while (curr != vec.end()) {
    if (*curr < *pred) {
      return curr;
    }
    ++curr;
    ++pred;
  }
  return vec.end();
}
*/
