# Documentation for src/rust/simple_lib/src/input.rs

# AI Summary
This file contains two functions for reading input from standard input. The first function reads a line as a String, while the second function reads a line and parses it into a number of a generic type T. Both functions handle potential errors during the read and parse operations.

The AI gave it a general rating of 9/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code is well-structured and adheres to Rust conventions. The functions are concise and handle errors appropriately.
# Functions

## get_string_input
### Explanation
This function reads a line from standard input and returns it as a String. It handles potential errors during the read operation.
### Code
```rust
pub fn get_string_input() -> Result<String, &'static str> {
    let mut result = String::new();

    match io::stdin().read_line(&mut result) {
        Ok(_) => (),
        Err(_) => return Err("Failed to get input"),
    }

    Ok(result)
}
```

## get_num_input
### Explanation
This function reads a line from standard input, parses it into a number of type T, and returns the number. It handles potential errors during the read and parse operations.
### Code
```rust
pub fn get_num_input<T: FromStr>() -> Result<T, &'static str> {
    let mut result = String::new();

    match io::stdin().read_line(&mut result) {
        Ok(_) => (),
        Err(_) => return Err("Failed to get input"),
    }

    match result.trim().parse::<T>() {
        Ok(num) => Ok(num),
        Err(_) => Err("Failed to parse input"),
    }
}
```
# Overall File Contents
```rust
use std::io;
use std::str::FromStr;

/// Gets string input from stdin
pub fn get_string_input() -> Result<String, &'static str> {
    let mut result = String::new();

    match io::stdin().read_line(&mut result) {
        Ok(_) => (),
        Err(_) => return Err("Failed to get input"),
    }

    Ok(result)
}

/// Gets number input from stdin
/// Reads it in, and then uses parse to convert it to a number
pub fn get_num_input<T: FromStr>() -> Result<T, &'static str> {
    let mut result = String::new();

    match io::stdin().read_line(&mut result) {
        Ok(_) => (),
        Err(_) => return Err("Failed to get input"),
    }

    match result.trim().parse::<T>() {
        Ok(num) => Ok(num),
        Err(_) => Err("Failed to parse input"),
    }
}

```
