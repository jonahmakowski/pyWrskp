use std::collections::HashMap;

fn main() {
    let mut numbers = vec![2, 3, 100, 5, 5, 6, 1, 1, 3, 3, 5, 6, 7, 30045, 103, 1028, 1028, 12164, 1274];
    let mut numbers_hash= HashMap::new();

    let mut sum = 0;

    numbers.sort();

    for &num in numbers.iter() {
        let count = numbers_hash.entry(num).or_insert(0);
        *count += 1;
        sum += num;
    }

    let mean = sum / numbers.len();
    let median;
    let mut assigned_mode = false;
    let mut mode = 0;

    for (key, value) in numbers_hash.iter() {
        if !assigned_mode || numbers_hash[&mode] < *value {
            mode = *key;
            assigned_mode = true;
        }
    }

    if numbers.len() % 2 == 0 {
        median = (numbers[numbers.len() / 2 - 1] + numbers[numbers.len() / 2]) / 2
    } else {
        median = numbers[numbers.len() / 2]
    }

    println!("Mean is {mean}");
    println!("Median is {median}");
    println!("Mode is {mode}");
}
