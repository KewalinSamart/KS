#ifndef SECRETKEEPER_H
#define SECRETKEEPER_H

#include<string>
using std::string;
#include<vector>

struct SecretKeeper{
  string password;
  string secret;
  string get_secret(string);

};

#endif

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
