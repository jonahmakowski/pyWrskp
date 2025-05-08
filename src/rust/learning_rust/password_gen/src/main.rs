use std::env;
use rand::Rng;

fn generate_password(length: i32) -> String {
    let mut password = String::new();
    
    for _ in 0..length {
        let letter: char = rand::rng().sample(rand::distr::Alphanumeric) as char;
        password.push(letter);
    }
    
    password
}

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(&args);

    if args.len() < 2 {
        println!("Pass the password length as an argument.");
        std::process::exit(1);
    }

    let length: &i32 = &args[1].parse().unwrap_or_else(|_| {
        println!("Please provide a valid number for the password length.");
        std::process::exit(1);
    });

    println!("Generating a password of length {}...", length);
    let password = generate_password(*length);
    println!("Generated password: {}", password);

}
