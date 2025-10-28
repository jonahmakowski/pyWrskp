#include <stdio.h>

// Storing strings in an array.
// We can use a single two-dimensional array to store several strings.

int main() {
	char stars[6][30] = {	
				"Britney Spears",
				"Mickey Mouse",
				"Justin Timberlake",
				"Albus Dumbledore",
				"Serena Williams",
				"Bilbo Baggins"
		};
	int dice = 0;
    char again;
    
    for (int i = 0; i < 6; i++) {
        printf("Star %d: %s\n", i + 1, stars[i]);
    }

    while (true) {
        do {
            printf("Pick a lucky star!\n");
            printf("Enter a number between 1 and 6: ");
            scanf("%d", &dice);
        } while (dice < 1 || dice > 6);
        
        printf("Your lucky star is %s \n", stars[dice - 1]);

        printf("Would you like to go again (y/n)? ");
        scanf(" %c", &again);
        if (again != 'y') {
            break;
        }
    }

	return 0;
}
