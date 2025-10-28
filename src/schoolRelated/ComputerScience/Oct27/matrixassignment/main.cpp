#include <stdio.h>
#include <math.h>

// Maximum size of the matrices
#define MAX_SIZE 5

// Coloring the text
#define REGULAR "\e[0m"
#define RED "\e[31m"
#define GREEN "\e[32m"
#define BOLD "\e[1m"

// File names
#define OUTFILE_NAME "matrix_output.txt"
#define INFILE_NAME "matrix.txt"

// Function to print a provided matrix
void printMatrix(int matrix[MAX_SIZE][MAX_SIZE], int width, int height) {
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            printf("%-5d ", matrix[i][j]);
        }
        printf("\n");
    }
}

// Function to write a provided matrix to a file
void writeMatrixToFile(FILE *file, int matrix[MAX_SIZE][MAX_SIZE], int width, int height) {
    // Write the dimensions of the matrix
    fprintf(file, "%d %d\n", height, width);

    // Write the matrix elements
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (j < width - 1) {
                fprintf(file, "%d ", matrix[i][j]);
            } else {
                fprintf(file, "%d", matrix[i][j]);
            }
        }
        if (i < height - 1) {
            fprintf(file, "\n");
        }
    }

    printf("%sMatrix written to %s successfully.%s\n", GREEN, OUTFILE_NAME, REGULAR);
}

int main() {
    // Defining file pointer and opening file
    FILE *fptr = fopen(INFILE_NAME, "r");
    if (fptr == NULL) {
        printf("%sError opening file%s", RED, REGULAR);
        return 1;
    }

    // Defining Variables
    int matrix1_width, matrix1_height;
    int matrix2_width, matrix2_height;
    int matrix_result_width, matrix_result_height;
    int matrix1[MAX_SIZE][MAX_SIZE], matrix2[MAX_SIZE][MAX_SIZE], matrix_result[MAX_SIZE][MAX_SIZE];
    char mode;

    // Get the first matrix dimensions
    fscanf(fptr, "%d %d", &matrix1_height, &matrix1_width);
    
    // Check if matrix dimensions are within MAX_SIZE
    if (matrix1_height > MAX_SIZE || matrix1_width > MAX_SIZE) {
        printf("%sError: Matrix dimensions exceed maximum size of %d.%s\n", RED, MAX_SIZE, REGULAR);
        fclose(fptr);
        return 1;
    }

    // Read the first matrix
    for (int i = 0; i < matrix1_height; i++) {
        for (int j = 0; j < matrix1_width; j++) {
            fscanf(fptr, "%d", &matrix1[i][j]);
        }
    }

    // Get the second matrix dimensions
    fscanf(fptr, "%d %d", &matrix2_height, &matrix2_width);
    
    // Check if matrix dimensions are within MAX_SIZE
    if (matrix2_height > MAX_SIZE || matrix2_width > MAX_SIZE) {
        printf("%sError: Matrix dimensions exceed maximum size of %d.%s\n", RED, MAX_SIZE, REGULAR);
        fclose(fptr);
        return 1;
    }

    // Read the second matrix
    for (int i = 0; i < matrix2_height; i++) {
        for (int j = 0; j < matrix2_width; j++) {
            fscanf(fptr, "%d", &matrix2[i][j]);
        }
    }

    // Reading the operation mode
    fscanf(fptr, " %c", &mode);

    // Closing file
    fclose(fptr);

    // Get operation if not in file
    if (mode == '\0') {
        printf("No mode defined in file, input mode multiplication/addition/subtraction (m/a/s): ");
        scanf(" %c", &mode);
    }

    printf("%sOperation mode: %c%s\n", BOLD, mode, REGULAR);

    // Printing the first two matrices
    printf("Matrix 1:\n");
    printMatrix(matrix1, matrix1_width, matrix1_height);
    
    printf("\n\nMatrix 2:\n");
    printMatrix(matrix2, matrix2_width, matrix2_height);

    // Checking if allowed to add or subtract
    if ((mode == 'a' || mode == 's') && (matrix1_width != matrix2_width || matrix1_height != matrix2_height)) {
        printf("%sError: Matrices must have the same dimensions to add or subtract.%s\n", RED, REGULAR);
        return 1;
    }

    // Checking if allowed to multiply
    else if (mode == 'm' && matrix1_width != matrix2_height) {
        printf("%sError: Incompatible matrix dimensions for multiplication.\n", RED);
        printf("Matrix 1 width must equal Matrix 2 height.%s\n", REGULAR);
        return 1;
    }

    // Adding the two matrices
    if (mode == 'a') {
        for (int i = 0; i < matrix1_height; i++) {
            for (int j = 0; j < matrix1_width; j++) {
                matrix_result[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }
        matrix_result_width = matrix1_width;
        matrix_result_height = matrix1_height;
    }

    // Subtracting the two matrices
    else if (mode == 's') {
        for (int i = 0; i < matrix1_height; i++) {
            for (int j = 0; j < matrix1_width; j++) {
                matrix_result[i][j] = matrix1[i][j] - matrix2[i][j];
            }
        }
        
        matrix_result_width = matrix1_width;
        matrix_result_height = matrix1_height;
    }

    // Multiplication the two matrices
    else if (mode == 'm') {
        int sum;
        for (int i = 0; i < matrix1_height; i++) {
            for (int j = 0; j < matrix2_width; j++) {
                sum = 0;
                for (int k = 0; k < matrix1_width; k++) {
                    sum += matrix1[i][k] * matrix2[k][j];
                }
                matrix_result[i][j] = sum;
            }
        }

        matrix_result_width = matrix2_width;
        matrix_result_height = matrix1_height;
    }


    printf("\n\nResulting Matrix after operation %c:\n", mode);
    printMatrix(matrix_result, matrix_result_width, matrix_result_height);

    // Writing to output file
    FILE *outptr = fopen(OUTFILE_NAME, "w");
    if (outptr == NULL) {
        printf("%sError opening output file%s", RED, REGULAR);
        return 1;
    }

    writeMatrixToFile(outptr, matrix_result, matrix_result_width, matrix_result_height);

    fclose(outptr);

    return 0;
}
