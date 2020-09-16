#include <algorithm>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <locale>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

struct Items {
  std::string item_name;
  int num_items;
  long price;

  bool operator<(const Items &other) { return (item_name < other.item_name); }
};

struct Store {
  std::string store_name;
  std::string location;
  std::vector<Items> items;
};

struct Shopping_list {
  int quantity;
  std::string name;
};

// This function define whether the given string is an int or a string
// or a mix of both
// return 1 if the given string is string/ 2 if integer/ 3 if mix

int check_string_or_int(std::string str) {
  int count_digit = 0, count_alpha = 0;
  for (auto c : str) {
    if (std::isdigit(c)) {
      count_digit++;
    } else if ((std::isalpha(c)) || (c == ' ')) {
      count_alpha++;
    }
  }
  if (count_alpha == static_cast<int>(str.size())) {
    return 1;
  } else if (count_digit == static_cast<int>(str.size())) {
    return 2;
  } else {
    return 3;
  }
}

// modified split function from example 16.2-clock.cpp
// This function separates istringstream by comma
// converts each info to its appropriate type
// return struct Items

Items separated_by_comma(std::istringstream &iss) {
  std::string stuffs, item_name;
  char dollar_sign;
  int num = 0;
  double cost = 0.0;
  long long_cost = 0;
  std::vector<Items> stuffs_vect;
  while (std::getline(iss, stuffs, ',')) {
    if (stuffs.empty())
      break;
    if (check_string_or_int(stuffs) == 1) {
      item_name = stuffs;
    } else if (check_string_or_int(stuffs) == 2) {
      num = stoi(stuffs);
    } else if (check_string_or_int(stuffs) == 3) {
      std::istringstream iss_cost(stuffs);
      iss_cost >> dollar_sign >> cost;
    }
    long_cost = cost * 100;
  }
  return Items{item_name, num, long_cost};
}

int main() {

  std::vector<Store> store;
  std::vector<Items> items;
  std::vector<Shopping_list> shopping_list;
  std::map<std::string, std::string> map_store_location;
  std::map<std::string, int> map_items_quantity;
  std::map<std::string,
           std::vector<std::pair<std::pair<std::string, int>, long>>>
      map_items_store_instock_price;
  std::vector<std::pair<std::pair<std::string, int>, long>>
      vect_store_instock_price;

  std::string num_str_stores;
  std::string store_name;
  std::string location;
  std::string items_info;
  std::string first_line_shopping;
  int num_stores, num_shopping;

  // create vector of Stores' information
  std::getline(std::cin, num_str_stores);
  std::istringstream iss(num_str_stores);
  // get number of stores
  iss >> num_stores;
  int count = 0;
  while (count < num_stores) {
    std::getline(std::cin, store_name);
    std::getline(std::cin, location);
    map_store_location.insert(make_pair(store_name, location));
    while (std::getline(std::cin, items_info)) {
      std::istringstream items_list(items_info);

      if (items_list.str().empty()) {
        // items.clear();
        break;
      }
      // function to seperate each info by comma
      Items vect_of_stuffs = separated_by_comma(items_list);

      // aiming for creating struct Store at the end of this loop
      items.push_back(vect_of_stuffs);
      std::sort(items.begin(), items.end(),
                [](Items a, Items b) { return a < b; });

      // aiming for outputting summary info
      // insert item and quantity to the map & update its value if the key
      // already exists
      std::map<std::string, int>::iterator it;
      it = map_items_quantity.find(vect_of_stuffs.item_name);
      if (it == map_items_quantity.end()) {
        map_items_quantity.insert(
            make_pair(vect_of_stuffs.item_name, vect_of_stuffs.num_items));
      } else {
        it->second += vect_of_stuffs.num_items;
      }

      // build a map containing key: item_name and
      // value: vector of pair<pair<store_name, instock>, price>

      std::pair<std::string, int> pair_store_instock{store_name,
                                                     vect_of_stuffs.num_items};
      std::pair<std::pair<std::string, int>, long> pair_store_instock_price{
          pair_store_instock, vect_of_stuffs.price};

      std::map<std::string, std::vector<std::pair<std::pair<std::string, int>,
                                                  long>>>::iterator itr;

      itr = map_items_store_instock_price.find(vect_of_stuffs.item_name);
      // not found
      if (itr == map_items_store_instock_price.end()) {
        vect_store_instock_price.clear();
        vect_store_instock_price.push_back(pair_store_instock_price);
        map_items_store_instock_price.insert(
            make_pair(vect_of_stuffs.item_name, vect_store_instock_price));

        // found (the key we want to add already exists)
        // access value by key then we will update the value by using push_back
      } else {
        itr->second.push_back(pair_store_instock_price);
      }
    }
    store.push_back(Store{store_name, location, items});
    items.clear();
    count++;
  }

  // sort map_items_store_instock_price by price
  for (auto itr = map_items_store_instock_price.begin();
       itr != map_items_store_instock_price.end(); itr++) {
    auto &instock = itr->second;
    sort(instock.begin(), instock.end(),
         [](auto a, auto b) { return a.second < b.second; });
  }

  // deal with shopping list
  std::getline(std::cin, first_line_shopping);
  std::istringstream iss1(first_line_shopping);
  iss1 >> num_shopping;
  int count_shopping = 0;
  int quantity = 0;
  std::string info_shopping, stuff_name;
  std::string temp;
  while (count_shopping < num_shopping) {
    std::getline(std::cin, info_shopping);
    std::istringstream list_shopping(info_shopping);
    list_shopping >> quantity >> stuff_name;
    while (list_shopping >> temp) {
      stuff_name += " " + temp;
    }
    Shopping_list stuffs_list = Shopping_list{quantity, stuff_name};
    shopping_list.push_back(stuffs_list);
    count_shopping++;
  }
  // output summary infomation of the stores
  std::cout << "Store Related Information (ordered by in-file order):"
            << std::endl;
  std::cout << "There are " << num_stores << " store(s)." << std::endl;

  for_each(store.begin(), store.end(), [](Store each_store) {
    std::cout << each_store.store_name << " has " << each_store.items.size()
              << " distinct items." << std::endl;
  });
  std::cout << std::endl;
  std::set<std::string> store_items_set;
  for (Store ele : store) {
    for (auto c : ele.items) {
      store_items_set.insert(c.item_name);
    }
  }
  std::vector<std::string> store_items_vect(store_items_set.begin(),
                                            store_items_set.end());
  std::sort(store_items_vect.begin(), store_items_vect.end());

  std::cout << "Item Related Information (ordered alphabetically):"
            << std::endl;
  // get number of distinct items
  std::cout << "There are " << store_items_vect.size()
            << " distinct item(s) available for purchase." << std::endl;
  for (auto ele : map_items_quantity) {
    std::cout << "There are " << ele.second << ' ' << ele.first << "(s)."
              << std::endl;
  }

  std::string wanted_stuff, cheapest_store;
  int wanted_num = 0, num_instock = 0, num_taken = 0;
  long long_cost_item = 0, long_total_cost = 0, cheapest_price = 0;
  double cost_item = 0.0, total_cost = 0.0;

  std::map<std::string,
           std::vector<std::pair<std::pair<std::string, int>, long>>>::iterator
      it_item;
  std::vector<std::pair<std::string, int>> vect_item_store_bought;

  std::cout << std::endl << "Shopping:" << std::endl;

  for (auto ele : shopping_list) {
    wanted_stuff = ele.name;
    wanted_num = ele.quantity;
    long_cost_item = 0;

    it_item = map_items_store_instock_price.find(wanted_stuff);
    vect_item_store_bought.clear();

    if (it_item == map_items_store_instock_price.end())
      continue;

    for (auto &each_store : it_item->second) {
      cheapest_store = each_store.first.first;
      cheapest_price = each_store.second;
      num_instock = each_store.first.second;

      if (num_instock >= wanted_num) {
        num_taken = wanted_num;
        vect_item_store_bought.push_back(make_pair(cheapest_store, num_taken));
        long_cost_item += (cheapest_price * num_taken);
        long_total_cost += (cheapest_price * num_taken);
        each_store.first.second -= num_taken;
        break;

      } else {
        num_taken = num_instock;
        vect_item_store_bought.push_back(make_pair(cheapest_store, num_taken));
        long_cost_item += (cheapest_price * num_taken);
        long_total_cost += (cheapest_price * num_taken);
        wanted_num = wanted_num - num_taken;
        each_store.first.second -= num_taken;
        continue;
      }
    }

    cost_item = long_cost_item / 100.00;
    std::cout << "Trying to order " << ele.quantity << " " << wanted_stuff
              << "(s)." << std::endl;

    // go through map_item_store_bought to get num_taken from each store for a
    // wanted_stuff
    std::map<
        std::string,
        std::vector<std::pair<std::pair<std::string, int>, long>>>::iterator it;
    it = map_items_store_instock_price.find(wanted_stuff);
    if (it != map_items_store_instock_price.end()) {
      std::cout << it->second.size() << " store(s) sell " << wanted_stuff << '.'
                << std::endl;
    }
    std::cout << std::fixed << std::setprecision(2) << "Total price: $"
              << cost_item << std::endl;

    // get location from map of pair<store, location>: map_store_location
    for (std::pair<std::string, int> ele : vect_item_store_bought) {
      std::cout << "Order " << ele.second << " from " << ele.first << " in "
                << map_store_location[ele.first] << std::endl;
    }
  }
  total_cost = long_total_cost / 100.00;
  std::cout << "Be sure to bring $" << std::fixed << std::setprecision(2)
            << total_cost << " when you leave for the stores." << std::endl;
}
