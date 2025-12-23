use std::fs::File;
use std::io::Read;
use std::thread;
use std::sync::mpsc;

fn main() {
    let mut file = File::open("input.txt").expect("Failed to open the file");

    let mut file_contents = String::new();
    file.read_to_string(&mut file_contents)
        .expect("Failed to get data out of file");

    let lines = file_contents.lines();

    let mut sum = 0;
    let mut handles = vec![];

    let lines: Vec<String> = lines.map(|line| line.to_string()).collect();

    let (tx, rx) = mpsc::channel();

    for (index, line) in lines.iter().enumerate() {
        let tx_clone = tx.clone();
        let line_clone = line.clone();
        handles.push(thread::spawn(move || {
            tx_clone.send(do_line(&line_clone)).unwrap();
        }));

        if index % 5 == 0 && index != 0 {
            for handle in handles {
                handle.join().unwrap();
            }
            handles = vec![];
        }
    }

    for _ in 0..handles.len() {
        sum += rx.recv().unwrap();
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("{sum}");
}

fn do_line(line: &str) -> i32 {
    println!("Started Line");
    let mut options = vec![];
    let chars: Vec<char> = line.chars().collect();
    recursive_search(12, &chars, &mut String::new(), &mut options);
    println!("Finished line");

    let mut max = options[0];

    for option in options {
        if option > max {
            max = option;
        }
    }

    return max;
}

fn recursive_search(depth: i32, chars: &[char], current: &mut String, results: &mut Vec<i32>) {
    if depth == 0 {
        if let Ok(number) = current.trim().parse() {
            results.push(number);
        }
        return;
    }

    for (index, &ch) in chars.iter().enumerate() {
        current.push(ch);

        recursive_search(depth - 1, &chars[index + 1..], current, results);

        current.pop(); // Backtrack
    }
}
