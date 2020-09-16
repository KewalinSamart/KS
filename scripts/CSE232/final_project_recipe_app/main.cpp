#include <cassert>
#include <exception>
#include <iostream>
#include <sstream>
#include <string>

#include "app.h"
#include "recipe.h"
#include "utility.h"

int WhichLineDifferent(const std::string &expected, const std::string &result) {
  std::istringstream iss_expected(expected);
  std::istringstream iss_result(result);

  for (int i = 0;; ++i) {
    std::string line_expected;
    std::string line_result;
    std::getline(iss_expected, line_expected, '\n');
    std::getline(iss_result, line_result, '\n');
    if (!iss_expected.good() || !iss_result.good()) {
      if (iss_expected.good() || iss_result.good()) {
        std::cout << "One of the texts has less lines than the other."
                  << std::endl;
        if (iss_expected.good()) {
          std::cout << "Expected is longer" << std::endl;
          std::cout << "With this line: \"" << line_expected << "\""
                    << std::endl;
        } else {
          std::cout << "Result is longer" << std::endl;
          std::cout << "With this line: \"" << line_result << "\"" << std::endl;
        }
        return i;
      }
      break;
    }
    if (line_expected != line_result) {
      std::cout << "This line from expected: \"" << line_expected << "\""
                << std::endl;
      std::cout << "Doesn't match this line from result: \"" << line_result
                << "\"" << std::endl;
      return i;
    }
  }
  return -1;
}

// int main() {
// std::cout << "Hello World!" << std::endl;
//}

int main() {
  RecipeApp ra;
  Recipe simple_pop("Simple Popcorn", 8);
  simple_pop.AddIngredient("1/4 cup unpopped popcorn");
  simple_pop.AddIngredient("1/4 teaspoon vegetable oil");
  simple_pop.AddIngredient("1/4 teaspoon salt");
  simple_pop.SetInstructions(R"***(Pop it!)***");
  Recipe apples("An Apple", 3);
  apples.AddIngredient("2-1/16 unit apple");
  apples.SetInstructions(R"***(Grab it!)***");
  Recipe apple_pie("Apple Pie", 7);
  apple_pie.AddIngredient("1 pound flour");
  apple_pie.AddIngredient("3-1/2 teaspoon salt");
  apple_pie.AddIngredient("3 unit apple");
  apple_pie.SetInstructions(R"***(Bake it!)***");
  ra.AddRecipe(simple_pop);
  ra.AddRecipe(apples);
  ra.AddRecipe(apple_pie);

  /*// check vect_recipe
    for (auto recipe: ra.vect_recipe()){
        std::cout << recipe.recipe_name() << std::endl;
    }*/

  ra.AddIngredientToPantry("2 cup unpopped popcorn");
  ra.AddIngredientToPantry("2 teaspoon salt");
  ra.AddIngredientToPantry("4-7/8 unit apple");
  std::ostringstream oss;
  Recipe consume_apples = ra.UseUpIngredient("4 unit apple");
  std::cout << consume_apples;
  oss << consume_apples;
  Recipe consume_salt = ra.UseUpIngredient("2 teaspoon salt");
  std::cout << consume_salt;
  oss << consume_salt;
  Recipe consume_popcorn = ra.UseUpIngredient("1/8 cup unpopped popcorn");
  std::cout << consume_popcorn;
  oss << consume_popcorn;
  std::string expected = R"***(Recipe for: An Apple
  Serves 5
  Ingredients:
  3-7/16 unit apple
  Instructions:
  Grab it!
  Recipe for: Apple Pie
  Serves 4
  Ingredients:
  4/7 pound flour
  2 teaspoon salt
  1-5/7 unit apple
  Instructions:
  Bake it!
  Recipe for: Simple Popcorn
  Serves 4
  Ingredients:
  1/8 cup unpopped popcorn
  1/8 teaspoon vegetable oil
  1/8 teaspoon salt
  Instructions:
  Pop it!
  )***";
}
/*
int main() {
  std::cout << "Start" << std::endl;
  Recipe r("Microwave Popcorn", 3);
  r.AddIngredient("1/2 cup unpopped popcorn");
  r.AddIngredient("1 teaspoon vegetable oil");
  r.AddIngredient("1/2 teaspoon salt");
    for (auto ele : r.vect_ingredients()){   ///// works!
        std::cout << ele.second.first << ' ' << ele.second.second << ' ' <<
ele.first << std::endl;
    }

  r.SetInstructions(
      R"***(In a cup or small bowl, mix together the unpopped popcorn and oil.
  Pour the coated corn into a brown paper lunch sack, and sprinkle in the salt.
    Fold the top of the bag over twice to seal in the ingredients.

  Cook in the microwave at full power for 2 1/2 to 3 minutes,
   or until you hear pauses of about 2 seconds between pops.

  Carefully open the bag to avoid steam, and pour into a serving bowl.
  From: https://www.allrecipes.com/recipe/87305/microwave-popcorn/
  )***");
    //std::cout << r.instruction();

  std::cout << r << std::endl;

  std::ostringstream oss;
  oss << r;
  std::string expected = R"***(Recipe for: Microwave Popcorn
Serves 3
Ingredients:
1/2 cup unpopped popcorn
1 teaspoon vegetable oil
1/2 teaspoon salt

Instructions:
In a cup or small bowl, mix together the unpopped popcorn and oil.
Pour the coated corn into a brown paper lunch sack, and sprinkle in the salt.
Fold the top of the bag over twice to seal in the ingredients.
Cook in the microwave at full power for 2 1/2 to 3 minutes,
or until you hear pauses of about 2 seconds between pops.
Carefully open the bag to avoid steam, and pour into a serving bowl.
From: https://www.allrecipes.com/recipe/87305/microwave-popcorn/

)***";

  std::cout << expected << std::endl;

  //WhichLineDifferent(oss.str(), expected);
  //assert(oss.str() == expected);

  std::cout << r.IngredientInOneServing("unpopped popcorn") << std::endl;

  std::cout << "Changing servings to 6" << std::endl;
  r.ChangeServings(10);

  std::cout << r << std::endl;

  std::cout << "End" << std::endl;

    std::istringstream iss("10/2");
    int n = 0;
    iss >> n;
    std::cout << n << std::endl;
  return 0;
}
*/
//}
