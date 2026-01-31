#include "getarg.h"
#include "temp_conv.h"
#include <stdio.h>

int main(int argc, char *argv[]) {
	double argument_value;
	int return_code = get_argument(argc, argv, &argument_value);

	if (return_code == 0) {
		double result = convert_to_cent(argument_value);
		printf("%.2lf degrees fahrenheit is %.2lf degrees centigrade\n", argument_value,
		       result);
	} else {
		return return_code;
	}
	return 0;
}