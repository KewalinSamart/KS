/*
Write a function, named sortByCourseNumber, that takes a reference to a vector of string (like {"CSE 232", "ECE 100", "CSE 450", "CSE 232"}) and returns nothing. The function should reorder the vector so that the courses are sorted by number in ascending order. You can assume that the department code is separated from the number by a space and that all course numbers are 3 characters long.

You should be using the STL algorithms to achieve this, full credit is only possible if your solution doesn't have any looping constructs (no "while" or "for" keywords anywhere in the solution). If a URL you are citing has such a word, add an interupting space like: https://www.programiz.com/cpp-programming/fo r-loop
*/

#include <vector>
#include <string>
#include <algorithm>

//http://www.cplusplus.com/reference/string/string/substr/

void sortByCourseNumber (std::vector<std::string> &v){
  std::sort (v.begin(), v.end(), [](std::string a, std::string b) { return std::stoi(a.substr(a.find(" "))) < std::stoi(b.substr(b.find(" "))); });
}

// solution code 
/*
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

int getCourseNumber(std::string course_name) {
  std::istringstream iss(course_name);
  std::string department_code;
  int course_number;
  iss >> department_code >> course_number;
  return course_number;
}

bool isSmallerNumber(const std::string & name_left,
                     const std::string & name_right) {
  int number_left = getCourseNumber(name_left);
  int number_right = getCourseNumber(name_right);
  return number_left < number_right;
}

void sortByCourseNumber(std::vector<std::string> & course_names) {
	std::sort(course_names.begin(),
	          course_names.end(),
	          isSmallerNumber);
}
*/
