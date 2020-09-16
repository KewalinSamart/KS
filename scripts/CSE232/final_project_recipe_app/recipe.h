#ifndef recipe_h
#define recipe_h

#include <algorithm>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

#include "utility.h"

class Recipe {

private:
  std::string recipe_name_;
  int num_serving_ = 0;
  std::string ratio_;
  std::string unit_;
  std::string ingredient_name_;
  std::string instruction_;
  std::vector<std::pair<std::string, std::pair<std::string, std::string>>>
      vect_ingredients_;

public:
  // constructors
  Recipe() = default;
  Recipe(std::string name, int num) : recipe_name_(name), num_serving_(num){};

  // getters
  std::string recipe_name() { return recipe_name_; }
  int num_serving() const { return num_serving_; }
  std::string ratio() { return ratio_; }
  std::string unit() { return unit_; }
  std::string ingredient_name() { return ingredient_name_; }
  std::vector<std::pair<std::string, std::pair<std::string, std::string>>>
  vect_ingredients() {
    return vect_ingredients_;
  }
  std::string instruction() { return instruction_; }

  // member functions
  void AddIngredient(std::string);
  void SetInstructions(std::string);
  std::string IngredientInOneServing(std::string);
  void ChangeServings(int);
  void fill_vect_ingredients(std::string);    // add info into vect_ingredients_
  std::string ratio_one_serving(std::string); // modify ratio to one serving

  // friends
  friend std::ostream &operator<<(std::ostream &, Recipe &);
  friend int distinguish_type_of_num(std::string);
};

// overloaded operator<< function
std::ostream &operator<<(std::ostream &oss, Recipe &recipe) {
  oss << "Recipe for: " << recipe.recipe_name() << '\n'
      << "Serves " << recipe.num_serving() << '\n'
      << "Ingredients:" << '\n';
  for (int i = 0; i < static_cast<int>(recipe.vect_ingredients().size()); i++) {
    oss << recipe.vect_ingredients()[i].second.first << ' '
        << recipe.vect_ingredients()[i].second.second << ' '
        << recipe.vect_ingredients()[i].first << '\n';
  }
  oss << '\n' << "Instructions:" << '\n' << recipe.instruction() << '\n';
  return oss;
}

// member functions' definitions

void Recipe::fill_vect_ingredients(std::string str) {
  std::string modified_ratio = modify_ratio(ratio_);
  std::pair<std::string, std::string> pair_unit_ingredient_name_ = {
      modified_ratio, unit_};
  vect_ingredients_.push_back(
      make_pair(ingredient_name_, pair_unit_ingredient_name_));
}

void Recipe::AddIngredient(std::string input_ingredient) {
  remove_whitespace(input_ingredient);
  std::istringstream iss(input_ingredient);
  ratio_.clear();
  unit_.clear();
  ingredient_name_.clear();
  iss >> ratio_ >> unit_;
  std::getline(iss >> std::ws, ingredient_name_);
  ratio_ = modify_ratio(ratio_);
  fill_vect_ingredients(input_ingredient);
}

void Recipe::SetInstructions(std::string str) {
  std::istringstream iss(str);
  std::string str_output;
  std::string outout;
  while (std::getline(iss >> std::ws, str_output)) {
    remove_whitespace(str_output);
    outout += str_output + '\n';
  }
  instruction_ = outout;
}

std::string Recipe::ratio_one_serving(std::string input_ratio) {
  std::string one_serving;
  char syntax1;
  char syntax2;
  std::istringstream iss(input_ratio);
  int top = 0;
  int bottom = 0;
  int front = 0;
  if (distinguish_type_of_num(input_ratio) == 1) {
    one_serving = input_ratio + '/' + std::to_string(num_serving_);
    one_serving = modify_ratio(one_serving);
  } else if (distinguish_type_of_num(input_ratio) == 2) {
    iss >> top >> syntax2 >> bottom;
    bottom = bottom * num_serving_;
    one_serving = std::to_string(top) + '/' + std::to_string(bottom);
    one_serving = modify_ratio(one_serving);
  } else if (distinguish_type_of_num(input_ratio) == 3) {
    iss >> front >> syntax1 >> top >> syntax2 >> bottom;
    if (front % num_serving_ == 0) {
      front = front / num_serving_;
      bottom = bottom * num_serving_;
      one_serving = std::to_string(front) + '-' + std::to_string(top) + '/' +
                    std::to_string(bottom);
    } else {
      top = (front * bottom) + top;
      bottom = bottom * num_serving_;
      one_serving = std::to_string(top) + '/' + std::to_string(bottom);
    }
    one_serving = modify_ratio(one_serving);
  }
  return one_serving;
}

std::string Recipe::IngredientInOneServing(std::string possible_ingredient) {
  std::ostringstream ratio_;
  std::string str;
  bool found = 0;
  int index = 0;
  for (int i = 0; i < static_cast<int>(vect_ingredients_.size()); i++) {
    if (vect_ingredients_[i].first == possible_ingredient) {
      ratio_ << vect_ingredients_[i].second.first;
      found = 1; // found!
      index = i;
      break;
    }
  }
  if (found == 1) {
    if (num_serving_ == 1) {
      str = ratio_.str() + ' ' + vect_ingredients_[index].second.second + ' ' +
            vect_ingredients_[index].first;
      return str;
    } else {
      str = ratio_one_serving(ratio_.str()) + ' ' +
            vect_ingredients_[index].second.second + ' ' +
            vect_ingredients_[index].first;
      return str;
    }
  } else {
    throw std::invalid_argument("ingredient_not_found"); // not found
  }
}

void Recipe::ChangeServings(int num_scale) {
  for (int i = 0; i < static_cast<int>(vect_ingredients_.size()); i++) {
    std::string ratio_for_one =
        ratio_one_serving(vect_ingredients_[i].second.first);
    std::string ratio_scale = ratio_scale_func(ratio_for_one, num_scale);
    vect_ingredients_[i].second.first = ratio_scale;
  }
  num_serving_ = num_scale;
}

#endif /* recipe_h */
