#ifndef THERMOSTAT_H
#define THERMOSTAT_H

#include<string>
#include<vector>

struct Thermostat{
	int High = 30;
	int Low = 15;
	int Hysteresis = 2;
	std::string previous_out;

	Thermostat() = default;
	Thermostat(int a, int b, int c): High(a), Low(b), Hysteresis(c) {};
	Thermostat(int d, int e): High(d), Low(e) {};
	explicit Thermostat(std::string s);

	std::string GetStateAfterReading (int);

};

std::string ThermostatToString(const Thermostat &);
void split(const std::string &, std::vector<std::string> &);


#endif

// solution code
/*
#pragma once

#include <string>

struct Thermostat {
  // int months_till_filter_clean = 6;
  int high_setting = 30;
  int low_setting = 15;
  int hysteresis = 2;
  std::string state = "Off";
  Thermostat() = default;
  Thermostat(int h, int l, int hyst = 2) :
    high_setting(h), low_setting(l), hysteresis(hyst) {};
  explicit Thermostat(std::string s);

  std::string GetStateAfterReading(int temperature);
};

std::string ThermostatToString(Thermostat t);
*/
