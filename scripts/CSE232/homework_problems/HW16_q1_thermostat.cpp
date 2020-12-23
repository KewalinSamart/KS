/*
Thermostats are interesting devices that are used to control the temperature of most homes. In my house, it controls both the furnace (for heating) and the air conditioner (for cooling). My Thermostat reads the current temperature, and decides whether to start the "heating" device, or the "Cooling" device. The thermostat has a maximum setting and a minimum setting. However, having the thermostat constantly cycled on and off is a bad idea. One solution to this is adding Hysteresis. The way this works is the following

The thermostat starts in the off position
If if the temperature goes too high, the "Cooling" device is turned on
if the temperature goes too low, the "Heating" device is turned on
if the temperature is near the minimum, and the Thermostat is "Heating", then it keeps "Heating"
if the temperature is near the maximum, and the Thermostat is "Cooling", then it keeps "Cooling"
if the temperature is not too hot for cooling, and not too cold for heating, then the thermostat is turned "Off"
See the example and the visible test cases for how your Thermostat should behave

You should make a struct (named "Thermostat") in the files "thermostat.h" and "thermostat.cpp". It should support 4 constructors:

A default constructor that has a high setting of 30C, a low setting of 15C, and a hysteresis value of 2C.
There should be a 2-parameter constructor that accepts a high and low setting, and has a hysteresis value of 2C.
A 3-parameter constructor that accepts all three settings.
And lastly, a explicit std::string constructor that accepts a string formatted like: "High=30C, Low=15C, Hysteresis=2C".
You also need to define a function named "ThermostatToString" that takes a Thermostat object and returns a string in the same form as the string construction accepts.

Lastly, (and most importantly) you need to have a member function named "GetStateAfterReading" that accepts a temperature and returns the state of the thermostat ("Heating", "Cooling", or "Off"). Note: all temperatures in this problem are ints.

Example:
*/
/*
Thermostat t_2 = Thermostat(35, 16, 3);
ASSERT_EQ(t_2.GetStateAfterReading(30), "Off");
ASSERT_EQ(t_2.GetStateAfterReading(32), "Off");
ASSERT_EQ(t_2.GetStateAfterReading(35), "Off"); // Even though the temp is at the high setting, hysteresis keeps it unchanged
ASSERT_EQ(t_2.GetStateAfterReading(37), "Off");
ASSERT_EQ(t_2.GetStateAfterReading(38), "Off");
ASSERT_EQ(t_2.GetStateAfterReading(39), "Cooling"); // 39 is outside the hysteresis zone, so the thermostat can turn the AC on
ASSERT_EQ(t_2.GetStateAfterReading(40), "Cooling");
ASSERT_EQ(t_2.GetStateAfterReading(39), "Cooling");
ASSERT_EQ(t_2.GetStateAfterReading(35), "Cooling");
ASSERT_EQ(t_2.GetStateAfterReading(33), "Cooling");
ASSERT_EQ(t_2.GetStateAfterReading(32), "Cooling"); // Cooling only stops once the temperature is again outside of the hystersis zone.
ASSERT_EQ(t_2.GetStateAfterReading(31), "Off");
ASSERT_EQ(t_2.GetStateAfterReading(30), "Off");
ASSERT_EQ(t_2.GetStateAfterReading(30), "Off");
ASSERT_EQ(t_2.GetStateAfterReading(36), "Off");
ASSERT_EQ(t_2.GetStateAfterReading(50), "Cooling");
ASSERT_EQ(t_2.GetStateAfterReading(33), "Cooling");
ASSERT_EQ(t_2.GetStateAfterReading(20), "Off");
*/

#include<string>
#include<vector>
#include<sstream>
using std::ostringstream; using std::istringstream;

#include "thermostat.h"
// string constructor
Thermostat::Thermostat(std::string s){
  // format is "High=30C, Low=15C, Hysteresis=2C".
  std::vector<std::string> v;
  split(s,v);
  High = stoi(v[0]);
  Low = stoi(v[1]);
  Hysteresis = stoi(v[2]);
}
std::string Thermostat::GetStateAfterReading (int temp){
  std::string output;
  if ((previous_out == "Off") || (previous_out == "")){
    if (temp > (High + Hysteresis)){
      output = "Cooling";
    }else if (temp < (Low - Hysteresis)){
      output = "Heating";
    }else{
      output = "Off";
    }
  }else if (previous_out == "Cooling"){
    if (temp < (Low - Hysteresis)){
      output = "Heating";
    }else if (temp < (High - Hysteresis)) {
      output = "Off";
    }else{
      output = "Cooling";
    }
  }else if (previous_out == "Heating"){
    if (temp > (High + Hysteresis)){
      output = "Cooling";
    }else if (temp > (Low + Hysteresis)){
      output = "Off";
    }else{
      output = "Heating";
    }
  }
  previous_out = output;
  return output;
}

std::string ThermostatToString(const Thermostat &c){
  ostringstream oss;
  oss << "High="<<c.High<<"C"<<", Low="
      <<c.Low<<"C"<<", Hysteresis="<<c.Hysteresis<<"C";
  return oss.str();
}

void split( const std::string &str, std::vector<std::string> &v) {
  istringstream iss(str);
  std::string a, b, c;
  iss >> a;
  int startindex = a.find('=');
  int Endindex = a.find('C');
  std::string high = a.substr(startindex + 1, Endindex - startindex - 1);
  v.push_back(high);
  iss >> b;
  startindex = b.find('=');
  Endindex = b.find('C');
  std::string low = b.substr(startindex + 1, Endindex - startindex - 1);
  v.push_back(low);
  iss >> c;
  startindex = c.find('=');
  Endindex = c.find('C');
  std::string hysteresis = c.substr(startindex + 1, Endindex - startindex - 1);
  v.push_back(hysteresis);
}

// solution code
/*
#include <string>
#include <sstream>
#include <stdexcept>
#include "thermostat.h"

Thermostat::Thermostat(std::string s){
  std::istringstream iss(s);
  std::string junk;
  std::getline(iss, junk, '=');
  if (junk != "High") {
    throw std::invalid_argument(junk);
  }
  iss >> high_setting;
  std::getline(iss, junk, '=');
  if (junk != "C, Low") {
    throw std::invalid_argument(junk);
  }
  iss >> low_setting;
  std::getline(iss, junk, '=');
  if (junk != "C, Hysteresis") {
    throw std::invalid_argument(junk);
  }
  iss >> hysteresis;
  std::getline(iss, junk);
  if (junk != "C") {
    throw std::invalid_argument(junk);
  }
}

std::string Thermostat::GetStateAfterReading(int temperature) {
  int must_cool = high_setting + hysteresis;
  int can_cool = high_setting - hysteresis - 1;
  int can_heat = low_setting + hysteresis;
  int must_heat = low_setting - hysteresis - 1;

  if (temperature > must_cool) { // Too Hot
    state = "Cooling";
    return state;
  } else if (temperature > can_cool) { // Cooling Hysteresis
    if (state == "Heating") {
      state = "Off";
    }
    return state;
  } else if (temperature > can_heat) { // Must Be Off
    state = "Off";
    return state;
  } else if (temperature > must_heat) { // Heating Hysteresis
    if (state == "Cooling") {
      state = "Off";
    }
    return state;
  }
  // Too Cold
  state = "Heating";
  return state;
}

std::string ThermostatToString(Thermostat t) {
  std::ostringstream oss;
  oss << "High=" << t.high_setting << "C, Low=" << t.low_setting
      << "C, Hysteresis=" << t.hysteresis << "C";
  return oss.str();
}
*/
