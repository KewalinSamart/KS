#ifndef app_h
#define app_h

#include <algorithm>
#include <map>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

#include "recipe.h"
#include "utility.h"

class RecipeApp {

private:
  std::vector<Recipe> vect_recipe_;
  std::vector<std::pair<std::string, std::pair<std::string, std::string>>>
      vect_pantry_;

public:
  // default constructor
  RecipeApp() = default;

  // getters
  std::vector<Recipe> vect_recipe() { return vect_recipe_; }
  std::vector<std::pair<std::string, std::pair<std::string, std::string>>>
  vect_pantry() {
    return vect_pantry_;
  }

  // member functions
  void AddRecipe(Recipe);
  void AddIngredientToPantry(std::string);
  Recipe UseUpIngredient(std::string);

  // friends
  friend std::ostream &operator<<(std::ostream &, RecipeApp &);
};

// overloaded operator<< function
std::ostream &operator<<(std::ostream &oss, RecipeApp &object) {
  oss << "Recipes in the app (ordered by name):" << '\n';
  for (int i = 0; i < static_cast<int>(object.vect_recipe().size()); i++) {
    oss << "Recipe for: " << object.vect_recipe()[i].recipe_name() << '\n'
        << "Serves " << object.vect_recipe()[i].num_serving() << '\n'
        << "Ingredients:" << '\n';
    for (int n = 0; n < static_cast<int>(
                            object.vect_recipe()[i].vect_ingredients().size());
         n++) {
      oss << object.vect_recipe()[i].vect_ingredients()[n].second.first << ' '
          << object.vect_recipe()[i].vect_ingredients()[n].second.second << ' '
          << object.vect_recipe()[i].vect_ingredients()[n].first << '\n';
    }
    oss << '\n'
        << "Instructions:" << '\n'
        << object.vect_recipe()[i].instruction() << '\n';
  }
  oss << "Ingredients in pantry (ordered by name):" << '\n';
  for (int m = 0; m < static_cast<int>(object.vect_pantry().size()); m++) {
    oss << object.vect_pantry()[m].second.first << ' '
        << object.vect_pantry()[m].second.second << ' '
        << object.vect_pantry()[m].first << '\n';
  }
  return oss;
}

// member function definitions

void RecipeApp::AddRecipe(Recipe recipe) {
  vect_recipe_.push_back(recipe);
  std::sort(vect_recipe_.begin(), vect_recipe_.end(), [](Recipe a, Recipe b) {
    return a.ingredient_name() < b.ingredient_name();
  });
}

void RecipeApp::AddIngredientToPantry(std::string ingredient) {
  remove_whitespace(ingredient);
  std::istringstream iss(ingredient);
  std::string ratio;
  std::string unit;
  std::string ingredient_name;
  iss >> ratio >> unit;
  std::getline(iss >> std::ws, ingredient_name);
  std::string modified_ratio = modify_ratio(ratio);
  std::pair<std::string, std::string> pair_unit_ingredient_name_ = {
      modified_ratio, unit};
  vect_pantry_.push_back(
      make_pair(ingredient_name, pair_unit_ingredient_name_));
  std::sort(vect_pantry_.begin(), vect_pantry_.end(), sortbyfisrt);
}

Recipe RecipeApp::UseUpIngredient(std::string looked_up_ingredient) {
  remove_whitespace(looked_up_ingredient);
  std::istringstream iss(looked_up_ingredient);
  std::string ratio;
  std::string unit;
  std::string ingredient_name;
  iss >> ratio >> unit;
  std::getline(iss >> std::ws, ingredient_name);

  double pantry_ratio = make_ratio_number(ratio);
  Recipe recipe_name;
  double number = 0.0;
  bool found = 0;

  for (auto recipe : vect_recipe_) {
    for (auto ele : recipe.vect_ingredients()) {
      if (ele.first == ingredient_name) {
        number = make_ratio_number(recipe.ratio_one_serving(ele.second.first));
        recipe_name = recipe;
        found = 1;
        double greatest_num_serving = pantry_ratio / number;
        recipe_name.ChangeServings(int(greatest_num_serving));
        break;
      }
    }
    if (found == 1) {
      break;
    }
  }
  if (found == 1) {
    return recipe_name;
  } else {
    throw std::invalid_argument("invalid_argument");
  }
}

#endif /* app_h */
