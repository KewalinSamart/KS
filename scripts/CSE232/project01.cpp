#include <cmath>
#include <iostream>
#include <string>

int convert_other_base_to_decimal(int input, int base) {
  int sum = 0;
  // convert int to string: http://www.cplusplus.com/reference/string/to_string/
  std::string number = std::to_string(input);
  int power = static_cast<int>(number.size() - 1);
  for (auto c : number) {
    int num = c - 48;
    sum += num * pow(base, power);
    power--;
  }
  return sum;
}

int convert_decimal_to_other_base(int input, int base) {
  int new_input = input / base;
  int remainder = input % base;
  char str_remainder = remainder + 48;
  std::string output;
  output += str_remainder;
  int new_remainder;
  while (new_input != 0) {
    new_remainder = new_input % base;
    new_input = new_input / base;
    char str_new_remainder = new_remainder + 48;
    std::string str_output = str_new_remainder + output;
    output = str_output;
  }
  // convert string to int:
  // https://www.systutorials.com/131/convert-string-to-int-and-reverse/
  int output_int = std::stoi(output);
  return output_int;
}

int math_in_other_base(int number1, int number2, int base, char operation) {
  int num1 = convert_other_base_to_decimal(number1, base);
  int num2 = convert_other_base_to_decimal(number2, base);
  int result_decimal = 0;
  if (operation == '+') {
    result_decimal = num1 + num2;
  } else if (operation == '-') {
    result_decimal = num1 - num2;
  } else if (operation == '*') {
    result_decimal = num1 * num2;
  } else if (operation == '/') {
    result_decimal = num1 / num2;
  } else if (operation == '%') {
    result_decimal = num1 % num2;
  }
  int result_base = convert_decimal_to_other_base(result_decimal, base);
  return result_base;
}

int main() {
  int number1, number2, base;
  char operation;
  std::cin >> number1 >> number2 >> base >> operation;
  int output = math_in_other_base(number1, number2, base, operation);
  std::cout << output;
}
