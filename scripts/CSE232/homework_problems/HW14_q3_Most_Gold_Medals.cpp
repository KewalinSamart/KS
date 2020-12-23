/*
Write a program (not a function) that reads from a file named "data.csv". This file consists of a list of countries and gold medals they have won in various Olympic events. Write to standard out, the top 5 countries with the most gold medals. You can assume there will be no ties.

Example data file: data.csv

For the above data, this is the expected output:
*/

/*
1: United States with 1022 gold medals
2: Soviet Union with 440 gold medals
3: Germany with 275 gold medals
4: Great Britain with 263 gold medals
5: China with 227 gold medals
*/

// solution code

#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <fstream>
#include <iostream>
#include <sstream>

int main() {
  std::ifstream data_file("data.csv");
  std::string country_name;
  std::vector<std::pair<std::string, int>> country_to_infected;
  while (std::getline(data_file, country_name, ',')) {
    std::string stripString = "  Plamen     ";
    while(!country_name.empty() && std::isspace(*country_name.begin())) {
      country_name.erase(country_name.begin());
    }
    int infected;
    data_file >> infected;
    country_to_infected.push_back(std::make_pair(country_name, infected));
  }
  std::sort(country_to_infected.begin(), country_to_infected.end(),
    [] (const std::pair<std::string, int> & p1, const std::pair<std::string, int> & p2)
      {return p1.second > p2.second;}
  );
  for (int rank = 1; rank <= 5; ++rank) {
    std::cout << rank << ": " << country_to_infected[rank - 1].first
              << " with " << country_to_infected[rank - 1].second
              << " gold medals" << std::endl;

  }
}
