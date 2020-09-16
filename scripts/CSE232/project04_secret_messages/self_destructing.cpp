#include <algorithm>
#include <ios>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

#include "redact.h"
#include "self_destructing.h"

// copy constructor
// std::fill : http://www.cplusplus.com/reference/algorithm/fill/
SelfDestructingMessage::SelfDestructingMessage(SelfDestructingMessage &sdm) {
  messages_ = sdm.messages_;
  number_of_allowed_views_ = sdm.number_of_allowed_views_;
  vect_view_ = sdm.vect_view_;
  std::fill(sdm.vect_view_.begin(), sdm.vect_view_.end(), 0);
}

// assignment operator
SelfDestructingMessage &
SelfDestructingMessage::operator=(SelfDestructingMessage &sdm) {
  messages_ = sdm.messages_;
  number_of_allowed_views_ = sdm.number_of_allowed_views_;
  vect_view_ = sdm.vect_view_;
  std::fill(sdm.vect_view_.begin(), sdm.vect_view_.end(), 0);
  return *this;
}

// methods
long SelfDestructingMessage::size() { return messages_.size(); }

std::vector<std::string> SelfDestructingMessage::get_redacted() {
  std::transform(messages_.begin(), messages_.end(), messages_.begin(),
                 [](std::string str) { return redact_alphabet_digits(str); });
  return messages_;
}

long SelfDestructingMessage::number_of_views_remaining(int index) {
  return vect_view_[index];
}

std::string &SelfDestructingMessage::operator[](size_t index) {
  if ((index >= messages_.size()) || (index < 0)) {
    throw std::out_of_range("out_of_range");
  } else if (vect_view_[index] == 0) {
    throw std::invalid_argument("invalid_argument");
  } else {
    vect_view_[index] -= 1;
    return messages_[index];
  }
}

void SelfDestructingMessage::add_array_of_lines(std::string *ary,
                                                long size_ary) {
  for (int i = 0; i < int(size_ary); i++) {
    messages_.push_back(ary[i]);
    vect_view_.push_back(number_of_allowed_views_);
  }
}

// overloaded operators
std::ostream &operator<<(std::ostream &oss, SelfDestructingMessage &sdm) {
  for (auto i = 0; i < static_cast<int>(sdm.messages().size()); i++) {
    oss << '0' << std::to_string(int(sdm.vect_view()[i])) << ": "
        << redact_alphabet_digits(sdm.messages()[i]) << "\n";
  }
  return oss;
}

// I learnt how to do getline with ws from
// https://stackoverflow.com/questions/16935026/stringstream-doesnt-accept-white-space
std::istream &operator>>(std::istream &input, SelfDestructingMessage &sdm) {
  std::string str;
  std::getline(input >> std::ws, str);
  sdm.messages().push_back(str);
  sdm.vect_view().push_back(sdm.number_of_allowed_views());
  return input;
}
