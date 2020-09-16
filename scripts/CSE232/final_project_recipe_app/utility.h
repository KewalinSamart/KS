#ifndef utility_h
#define utility_h

#include <algorithm>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

// function declarations
int distinguish_type_of_num(std::string const &);
std::string modify_ratio(std::string const &);
std::string ratio_scale_func(std::string const &, int const &);
void remove_whitespace(std::string &);
bool sortbyfisrt(
    const std::pair<std::string, std::pair<std::string, std::string>> &,
    const std::pair<std::string, std::pair<std::string, std::string>> &);
double make_ratio_number(std::string const &);
std::string modify_ratio_type2(std::istringstream &);
std::string modify_ratio_type3(std::istringstream &);

// function definitions
int distinguish_type_of_num(std::string const &input_ratio) {
  int count_digit = 0;
  for (auto c : input_ratio) {
    if (std::isdigit(c)) {
      count_digit++;
    }
  }
  if (count_digit == static_cast<int>(input_ratio.size())) {
    // ratio = whole number
    return 1;
  } else if ((input_ratio.find('/') != std::string::npos) &&
             (input_ratio.find('-') == std::string::npos)) {
    // ratio = fraction
    return 2;
  } else if ((input_ratio.find('/') != std::string::npos) &&
             (input_ratio.find('-') != std::string::npos)) {
    // ratio is in reduced-mixed form
    return 3;
  } else {
    // unknown type of ratio // prevent reaching end of non-return function
    // error
    return 0;
  }
}

std::string modify_ratio(std::string const &input_ratio) {
  std::string proper_ratio;
  std::istringstream iss(input_ratio);
  // whole number -> no change
  if (distinguish_type_of_num(input_ratio) == 1) {
    proper_ratio = input_ratio;
  } else if (distinguish_type_of_num(input_ratio) == 2) {
    // fraction -> check bottom and top
    proper_ratio = modify_ratio_type2(iss);
  } else if (distinguish_type_of_num(input_ratio) == 3) {
    // reduced-mixed form -> check and modify
    proper_ratio = modify_ratio_type3(iss);
  }
  return proper_ratio;
}

// std::gcd :
// https://stackoverflow.com/questions/53251638/c-says-gcd-is-not-a-member-of-std
std::string modify_ratio_type2(std::istringstream &iss) {
  std::string proper_ratio;
  char syntax2;
  int top = 0;
  int bottom = 0;
  int front = 0;
  int remainder = 0;
  int d = 0;
  iss >> top >> syntax2 >> bottom;
  if (top > bottom) {
    // modify
    front = top / bottom;
    remainder = top % bottom;
    remainder = top % bottom;
    d = std::gcd(remainder, bottom);
    remainder = remainder / d;
    bottom = bottom / d;
    if (remainder == 0) {
      proper_ratio = std::to_string(front);
    } else {
      proper_ratio = std::to_string(front) + '-' + std::to_string(remainder) +
                     '/' + std::to_string(bottom);
    }
  } else if (top == bottom) {
    proper_ratio = std::to_string(1);
  } else {
    d = std::gcd(top, bottom);
    top = top / d;
    bottom = bottom / d;
    if (top == bottom) {
      proper_ratio = std::to_string(1);
    } else {
      proper_ratio = std::to_string(top) + '/' + std::to_string(bottom);
    }
  }
  return proper_ratio;
}

std::string modify_ratio_type3(std::istringstream &iss) {
  std::string proper_ratio;
  char syntax1;
  char syntax2;
  int top = 0;
  int bottom = 0;
  int front = 0;
  int remainder = 0;
  int d = 0;
  iss >> front >> syntax1 >> top >> syntax2 >> bottom;
  if (top > bottom) {
    front += top / bottom;
    remainder = top % bottom;
    d = std::gcd(remainder, bottom);
    remainder = remainder / d;
    bottom = bottom / d;
    if (remainder == 0) {
      proper_ratio = std::to_string(front);
    } else {
      proper_ratio = std::to_string(front) + '-' + std::to_string(remainder) +
                     '/' + std::to_string(bottom);
    }
  } else if (top == bottom) {
    front += 1;
    proper_ratio = std::to_string(front);
  } else {
    d = std::gcd(top, bottom);
    top = top / d;
    bottom = bottom / d;
    proper_ratio = std::to_string(front) + '-' + std::to_string(top) + '/' +
                   std::to_string(bottom);
  }
  return proper_ratio;
}

std::string ratio_scale_func(std::string const &input_ratio, int const &scale) {
  std::string scale_serving;
  char syntax1;
  char syntax2;
  std::istringstream iss(input_ratio);
  int top = 0;
  int bottom = 0;
  int front = 0;
  int whole_num = 0;
  if (distinguish_type_of_num(input_ratio) == 1) {
    iss >> whole_num;
    int scale_up = whole_num * scale;
    scale_serving = std::to_string(scale_up);
    scale_serving = modify_ratio(scale_serving);
  } else if (distinguish_type_of_num(input_ratio) == 2) {
    iss >> top >> syntax2 >> bottom;
    scale_serving = std::to_string(top * scale) + '/' + std::to_string(bottom);
    scale_serving = modify_ratio(scale_serving);
  } else if (distinguish_type_of_num(input_ratio) == 3) {
    iss >> front >> syntax1 >> top >> syntax2 >> bottom;
    front = front * scale;
    top = top * scale;
    scale_serving = std::to_string(front) + '-' + std::to_string(top) + '/' +
                    std::to_string(bottom);
    scale_serving = modify_ratio(scale_serving);
  }
  return scale_serving;
}

// find_last_not_of:
// http://www.cplusplus.com/reference/string/string/find_last_not_of/
void remove_whitespace(std::string &str) {
  std::string whitespaces(" \t\f\v\r");
  std::size_t found_leading = str.find_last_not_of(whitespaces);
  std::size_t found_trailing = str.find_last_not_of(whitespaces);
  if (found_leading != std::string::npos) {
    str.erase(found_leading + 1);
  }
  if (found_trailing != std::string::npos) {
    str.erase(found_trailing + 1);
  }
}

bool sortbyfisrt(
    const std::pair<std::string, std::pair<std::string, std::string>> &a,
    const std::pair<std::string, std::pair<std::string, std::string>> &b) {
  return (a.first[0] < b.first[0]);
}

double make_ratio_number(std::string const &ratio) {
  double amount = 0;
  char syntax1;
  char syntax2;
  std::istringstream iss(ratio);
  double top = 0;
  double bottom = 0;
  double front = 0;
  if (distinguish_type_of_num(ratio) == 1) {
    iss >> front;
    amount = front;
  } else if (distinguish_type_of_num(ratio) == 2) {
    iss >> top >> syntax1 >> bottom;
    amount = top / bottom;
  } else if (distinguish_type_of_num(ratio) == 3) {
    iss >> front >> syntax1 >> top >> syntax2 >> bottom;
    top = (front * bottom) + top;
    amount = top / bottom;
  }
  return amount;
}

#endif /* utility_h */
