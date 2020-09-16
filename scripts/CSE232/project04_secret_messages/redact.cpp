#include <algorithm>
#include <iostream>
#include <locale>
#include <string>
#include <vector>

#include "redact.h"

// replace all chars with '#'
// https://stackoverflow.com/questions/33559456/replace-all-characters-in-a-string-except-for-spaces-with-underscores

std::string redact_all_chars(const std::string &str_input) {
  std::string str = str_input;
  std::replace_if(
      str.begin(), str.end(), [](char ch) { return ch; }, '#');
  return str;
}

// replace a-z, A-Z, and 0-9 with '#'
std::string redact_alphabet_digits(const std::string &str_input) {
  std::string str = str_input;
  std::replace_if(
      str.begin(), str.end(),
      [](char ch) { return ((std::isdigit(ch)) || (std::isalpha(ch))); }, '#');
  return str;
}

// replce all chars that appear to be in the vector of string (words_to_react)
// https://www.quora.com/How-do-I-replace-all-occurrences-of-a-string-in-C

std::string redact_words(const std::string &str_input,
                         const std::vector<std::string> &words_to_redact) {
  std::string str = str_input;
  std::string word_to_find;
  for (auto i = words_to_redact.begin(); i != words_to_redact.end(); ++i) {
    word_to_find = *i;
    std::string replaced_word = redact_all_chars(word_to_find);
    size_t pos = str.find(word_to_find);
    while (pos != std::string::npos) {
      str.replace(pos, word_to_find.size(), replaced_word);
      pos = str.find(word_to_find, pos + replaced_word.size());
    }
  }

  return str;
}
