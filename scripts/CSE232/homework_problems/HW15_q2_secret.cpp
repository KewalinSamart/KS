/*
Write a struct that has only two data members, a string named "password" and another string named "secret". This struct is called "SecretKeeper". The purpose of this type is too only share its secret with users that know the password. The struct isn't too secure yet, but we'll learn more ways to control information later in the course.

The SecretKeeper type also has a function member named "get_secret" that takes a single argument, a string that represents a user providing a password. If the user's password matches the struct's password, return the secret, otherwise, return a empty string.

Be sure to separate your code into a header file (secret.h) and an implementation file (secret.cpp).
*/

#include<string>
using std::string;
#include<sstream>
using std::ostringstream;
#include<string>
using std::string;

#include "secret.h"


string SecretKeeper::get_secret(string str){
  string invalid_pass;
  if (str == password){
    return secret;
  }
  return invalid_pass;
}

// solution code
/*
#include "secret.h"

#include <string>

std::string SecretKeeper::get_secret(std::string provided_password) {
  if (provided_password == password)
    return secret;
  return "";
}
*/
