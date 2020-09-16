/*
Write a class, named "TwoOrLess" with a header file (two_or_less.hpp) and an implementation file (two_or_less.cpp).

This is a class that acts much like a set, except it can hold 0, 1, or 2 duplicates of an int. 
You need to support the insert, count, and size methods with the same parameters and return types as the set<int> class (see test cases).
*/

#include<string>
#include<sstream>
#include<set>
#include<utility> 

#include "two_or_less.hpp"


int TwoOrLess::count(int n){
  return s.count(n);
}

std::pair<std::multiset<int>::iterator,bool> TwoOrLess::insert( const int& ele){
  if (s.count(ele) < 2){
    s.insert(ele);
    return std::make_pair(s.find(ele),true);
  }else{
    return std::make_pair(s.end(),false);
  }
}

int TwoOrLess::size(){
  return s.size();
}

/*
#include <set>
using std::set;
#include <utility>
using std::pair;

#include "two_or_less.hpp"

pair<typename set<int>::iterator, bool> TwoOrLess::insert(const int & element) {
  //  pair<set<T>::iterator, bool> p = set_1.insert(element);
  pair<typename set<int>::iterator, bool> p = set_1.insert(element);
  if (p.second) {
    return p;
  }
  pair<typename set<int>::iterator, bool> p2 = set_2.insert(element);
  return p2;
}

int TwoOrLess::count(const int & element) {
  return set_1.count(element) + set_2.count(element);
}

int TwoOrLess::size() {
  return set_1.size() + set_2.size();
}
*/





