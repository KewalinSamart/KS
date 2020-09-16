/* 
I've made a map<string, int> that represents the number of times a word appears in a particular text.
I need you to transform the data in this data structure to some related data structure. Do not copy this map, using const references.

only_once: takes a map<string, int> and returns a set<string> of words that only appeared once in the text.
count_to_words: takes a map<string, int> and returns a multimap<int, string> of the counts to the words with that count.
count_to_set: takes a map<string, int> and returns a map<int, set<string>> of the counts to the set of words with that count.
*/

#include <map>
#include <set>
#include <string>

//only_once: takes a map<string, int> and returns a set<string> of words that only appeared once in the text.
std::set<std::string> only_once (const std::map<std::string,int> &map){
  std::set<std::string> set_string;
  std::map<std::string,int>::iterator it;
  for (auto it = map.begin();
       it != map.end(); it++) {
         if (it -> second == 1){
           set_string.insert(it -> first);
         }
       }
  return set_string;
}

//count_to_words: takes a map<string, int> and 
//returns a multimap<int, string> of the counts to the words with that count.

std::multimap<int,std::string> count_to_words (const std::map<std::string,int> &map){
  std::multimap<int,std::string> multimap_string;
  std::map<std::string,int>::iterator it;
  for (auto it = map.begin();
       it != map.end(); it++) {
           multimap_string.insert(std::make_pair(it -> second, it -> first));
       }
  return multimap_string;
}

// count_to_set: takes a map<string, int> and returns a map<int, set<string>> 
//of the counts to the set of words with that count.

std::map<int, std::set<std::string>> count_to_set (const std::map<std::string,int> &map){
std::map<int,std::set<std::string>> map_result;
std::set<std::string> setstring;
std::map<std::string,int>::iterator it;
std::map<std::string,int>::iterator it_;
std::map<int, std::set<std::string>>::iterator it2;
std::set<int> set_int;

int num = 0;
for (auto it = map.begin();it != map.end(); it++){
  num = it -> second;
  set_int.insert(num);
}
 
for (auto ele:set_int){
    setstring.clear();
    for (auto it_ = map.begin();it_ != map.end(); it_++){
        if (it_ -> second == ele){
            setstring.insert(it_ -> first);
            it2 = map_result.find(ele);
            if (it2 == map_result.end()){
                map_result.insert(std::make_pair(ele, setstring));
            }else{
                map_result.erase(ele);
                map_result.insert(std::make_pair(ele, setstring));
            }
            
        }

    }
}
    

  return map_result;
}

// solution code
/* 
#include <map>
using std::map;
using std::multimap;
#include <set>
using std::set;
#include <string>
using std::string;

set<string> only_once(const map<string, int> & word_counts) {
  set<string> result;
  for (const std::pair<const string, int> & p : word_counts) {
    if (p.second == 1)
      result.insert(p.first);
  }
  return result;
}

multimap<int, string> count_to_words(const map<string, int> & word_counts) {
  multimap<int, string> result;
  for (const std::pair<const string, int> & p : word_counts) {
    result.insert({p.second, p.first});
  }
  return result;
}

map<int, set<string>> count_to_set(const map<string, int> & word_counts) {
  map<int, set<string>> result;
  for (const std::pair<const string, int> & p : word_counts) {
    result[p.second].insert(p.first);
  }
  return result;
}
*/
