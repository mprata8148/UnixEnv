#include "temp_conv.h"

/**
 * @brief Convert a temperature in Celsius to Fahrenheit
 * @param cent The temperature in Celsius to convert
 * @return The temperature in Fahrenheit
 */
double convert_to_fahr(double cent) {
	return (1.8 * cent) + 32;
}

/**
 * @brief Convert a temperature in Fahrenheit to Celsius
 * @param fahr The temperature in Fahrenheit to convert
 * @return The temperature in Celsius
 */
double convert_to_cent(double fahr) {
	return (fahr - 32) * 5 / 9;
}