#ifndef SELF_DESTRUCTING_H
#define SELF_DESTRUCTING_H

#include <ios>
#include <sstream>
#include <string>
#include <vector>

class SelfDestructingMessage {

private:
  std::vector<std::string> messages_ = {};
  long number_of_allowed_views_ = 0;
  std::vector<long> vect_view_;

public:
  // constructors
  SelfDestructingMessage() = default;
  SelfDestructingMessage(std::vector<std::string> v_str, long num)
      : messages_(v_str), number_of_allowed_views_(num),
        vect_view_(messages_.size(), number_of_allowed_views_){};

  // rule of three
  SelfDestructingMessage(SelfDestructingMessage &); // copy constructor
  ~SelfDestructingMessage(){};                      // destructor
  SelfDestructingMessage &
  operator=(SelfDestructingMessage &); // assignment operator

  // getters
  std::vector<std::string> &messages() { return messages_; }
  long number_of_allowed_views() const { return number_of_allowed_views_; }
  std::vector<long> &vect_view() { return vect_view_; }

  // methods
  long size();
  std::vector<std::string> get_redacted();
  long number_of_views_remaining(int);
  std::string &operator[](size_t);
  void add_array_of_lines(std::string *, long);

  // friends
  friend std::ostream &operator<<(std::ostream &, SelfDestructingMessage &);
  friend std::istream &operator>>(std::istream &, SelfDestructingMessage &);
};

// overloaded operator<< function
std::ostream &operator<<(std::ostream &, SelfDestructingMessage &);

// overloaded operator>> function
std::istream &operator>>(std::istream &, SelfDestructingMessage &);

#endif
