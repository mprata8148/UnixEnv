#include "getarg.h"
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * @brief Parse a command line argument and convert it to a double
 * @param argc The number of arguments passed to the program
 * @param argv[] An array of strings containing the arguments passed to the program
 * @param return_value A pointer to a double where the parsed value will be stored
 * @return 0 for Okay, -1 for Error
 */
int get_argument(int argc, char *argv[], double *return_value) {
	// Return 0 for Okay -1 for Error
	char *endptr;
	errno = 0;

	if (argc < 1) {
		return -1;
	}

	double val = strtod(argv[1], &endptr);

	if (endptr == argv[1] || *endptr != '\0') {
		printf("strtod: Invalid input\n");
		return -1;
	}

	if (errno == ERANGE) {
		printf("strtod: Input number too large\n");
		return -1;
	}
	*return_value = val;
	return 0;
}