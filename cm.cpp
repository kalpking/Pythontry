#include <iostream>

int main() {
    // Declare variables to store user input
    double num1, num2;

    // Prompt user to enter the first number
    std::cout << "Enter the first number: ";
    std::cin >> num1;

    // Prompt user to enter the second number
    std::cout << "Enter the second number: ";
    std::cin >> num2;

    // Calculate and display the sum
    double sum = num1 + num2;
    std::cout << "The sum of " << num1 << " and " << num2 << " is: " << sum << std::endl;

    return 0;
}
