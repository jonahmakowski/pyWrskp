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
