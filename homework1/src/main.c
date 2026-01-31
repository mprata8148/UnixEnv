#include <stdio.h>

int main(int argc, char *argv[]) {
	printf("You have entered %d arguments (including program name):\n", argc);

	// Loop through each argument from argv[0] to argv[argc - 1]
	for (int i = 0; i < argc; i++) {
		printf("Argument %d: %s\n", i, argv[i]);
	}

	return 0;
}
