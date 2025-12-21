use std::fs::File;
use std::io::Read;

fn main() {
    let mut file = File::open("input.txt").expect("Failed to open the file");

    let mut file_contents = String::new();
    file.read_to_string(&mut file_contents).expect("Failed to get data out of file");

    let lines = file_contents.lines();

    let mut current_position = 50;
    let mut result = 0;

    for line in lines {
        let line_number: i32 = line.replace("R", "").replace("L", "").trim().parse().expect("Failed to parse num");
        let mut direction = 1;

        if line.contains("L") {
            direction = -1;
        }

        for _ in 0..line_number {
            current_position += 1 * direction;
            current_position %= 100;

            if current_position == 0 {
                result += 1;
            }
        }
    }

    println!("Result: {result}")
}
