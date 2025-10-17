use std::fs::File;
use std::io::prelude::*;

// C version at src/schoolRelated/ComputerScience/Oct16/arrayquestions/main.cpp

fn main() {
    // Question 1
    println!("Question 1:");
    let x = [1, 2, 3, 4, 5];

    for i in (0..x.len()).rev() {
        println!("{}", x[i]);
    }

    // Question 2
    println!("\nQuestion 2:");

    // Reading from the file
    let mut file_contents = String::new();
    let mut file = File::open("data.txt").expect("Unable to open file");
    file.read_to_string(&mut file_contents).expect("Unable to read file");

    // Processing each line
    let mut sum = 0;
    let lines = file_contents.split('\n');
    for line in lines {
        sum += line.parse::<i32>().unwrap_or(0);
    }
    println!("Sum: {}", sum);

    // Question 3
    println!("\nQuestion 3:");

    let mut array = Vec::new();
    let mut num = 1;
    for _i in 1..100 {
        array.push(num);
        num += 2;
    }
    println!("{:?}", array);

    // Question 5
    println!("\nQuestion 5:");
    const Q5_SIZE: usize = 10;
    let mut array: Vec<_> = (0..Q5_SIZE).collect();
    let mut temp;

    for i in 0..(Q5_SIZE / 2) {
        temp = array[i];
        array[i] = array[Q5_SIZE - i - 1];
        array[Q5_SIZE - i - 1] = temp;
    }

    println!("{:?}", array);

    // Question 7
    println!("\nQuestion 7:");
    let array = [3, 5, 7, 2, 8, 6, 4, 1];
    let mut max = array[0];
    let mut min = array[0];

    let mut max_index = 0;
    let mut min_index = 0;

    for (i, &value) in array.iter().enumerate() {
        if value > max {
            max = value;
            max_index = i;
        }
        if value < min {
            min = value;
            min_index = i;
        }
    }

    println!("Max: {} at index {}", max, max_index);
    println!("Min: {} at index {}", min, min_index);
}
