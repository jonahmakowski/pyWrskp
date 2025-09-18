/***************************************************************************
 *  Name: Jonah Makowski         Subway Program       Date: Sep 18, 2025   *
 *                                                                         *
 *   Program to calculate cost and calories of a subway order              *
 *   Incomplete solution to help get you started                           *
 ***************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main() {
    //DO NOT CHANGE ANYTHING IN THE INPUT SECTION!!
    //bool veggie;
    char order[21] = "";
    char strSandwich[21];
    char strSnack[21] = "";
    char strDrink[21] = "";
    bool bVeggie = false;
    bool bChips = false;
    bool bCookies = false;
    bool bDrink = false;
    bool bBottle = false;
    bool bTooManySnacks = false;
    float fCost = 0.0;
    int iCalories = 0;
    
    // Input Section
    printf("Welcome to the Sandwich Shop\n");
    printf("Would you like a veggie or roast chicken Sub? (v/c) ");
    scanf("%s", order);
    if (tolower(order[0]) == 'v') {
        bVeggie = true;
        strcpy(strSandwich, "veggie");
    }    
    else {
        bVeggie = false; 
        strcpy(strSandwich, "roast chicken");
    }
    
    printf("Would you like chips? (y/n) ");
    scanf("%s", order);
    if (tolower(order[0]) == 'y') {
        bChips = true;
        strcpy(strSnack, "and chips");
    }    
    else {
        bChips = false;   
    }
    
    printf("Would you like cookies? (y/n) ");
    scanf("%s", order);
    if (tolower(order[0]) == 'y') {
        bCookies = true;
        strcpy(strSnack, "and cookies");
    }    
    else {
        bCookies = false;   
    }    
    
    printf("Would you like a drink? (y/n) ");
    scanf("%s", order);
    if (tolower(order[0]) == 'y') {
        bDrink =  true;
        printf("Would you like a bottle or a fountain drink? (b/f) ");
        scanf("%s", order);
        if (tolower(order[0]) == 'b') {
            bBottle = true;
            strcpy(strDrink, "and bottle drink");
        }    
        else {
            bBottle = false; 
            strcpy(strDrink, "and fountain drink");
        }    
    }        
    else {
        bDrink = false;
    }
    
    // Process Section
    
    /*************************************************************
    You will be coding the process section of the code.
    
    You need to calculate:
        1.  the cost of the order
        2.  the number of calories in the order.
    
    Please use the following information:
        1.	The user is not allowed to purchase both a bag of chips and cookies. 
        2.	Veggie subs are 460 calories, and cost $5.50. 
        3.	Roast chicken subs are 620 calories, and cost $6.75. 
        4.	Chips are 222 calories, and cost $1.10.
        5.	Cookies are 440 calories, and cost $1.60.
        6.	Bottle drinks are 187 calories, and cost $1.80.
        7.	Fountain drinks are 260 calories, and cost $1.30.
        8.	If you buy a combo, you get $1.00 off. 
            (A combo consists of a sub, a bag of chips OR cookies, and a drink.)
   
    Note: As this is an assignment about if statements, you should be implementing
    the requirements using if statements.
   
    ENTER YOUR CODE HERE
    **************************************************************/ 
    
    const int daily_calorie_count = 2000;

    if (bChips && bCookies) {
        // Too many snacks (having cookies and chips)
        bTooManySnacks = true;
    } else {
        // Sandwich
        if (bVeggie) {
            fCost += 5.5;
            iCalories += 460;
        } else {
            fCost += 6.75;
            iCalories += 620;
        }

        // Chips
        if (bChips) {
            fCost += 1.1;
            iCalories += 222;
        }

        // Cookies
        if (bCookies) {
            fCost += 1.6;
            iCalories += 440;
        }

        // Drinks
        if (bDrink && bBottle) {
            fCost += 1.8;
            iCalories += 187;
        } else if (bDrink && !bBottle) {
            fCost += 1.3;
            iCalories += 260;
        }

        // Combo discount
        if ((bChips || bCookies) && bDrink) {
            fCost -= 1.0;
        }
    }

    printf("Total Calories is %.2f%% of daily intake\n", (iCalories / (float)daily_calorie_count) * 100);

   /******************************************************************/     
    //DO NOT CHANGE ANYTHING IN THE OUTPUT SECTION!
    // Output
    if (bTooManySnacks){ 
        printf("You can't order both cookies and chips, get out of the line\n");
    }
    else {
        printf("\n\nYour order of %s sandwich %s %s is\n ",
            strSandwich, strSnack, strDrink);
        printf("\t$%.2f and %d calories\n\n",
             fCost, iCalories);  
    }
    
    return 0;
}
