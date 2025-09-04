use text_io::read; // Library for input

fn main() {
    println!("Welcome to the multiplication calculator!");
    println!("Set the value for the first number:");
    let x: f64 = read!("{}\n"); // Gets input for the first number
    println!("Set the value for the second number:");
    let y: f64 = read!("{}\n"); // Gets input for the second number
    let result = x * y; // calculates the result
    println!("The result of {} * {} is: {}", x, y, result); // Displays the result
}
