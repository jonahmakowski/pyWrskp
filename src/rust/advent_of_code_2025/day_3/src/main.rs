use std::fs::File;
use std::io::Read;

fn main() {
    let mut file = File::open("input.txt").expect("Failed to open the file");

    let mut file_contents = String::new();
    file.read_to_string(&mut file_contents)
        .expect("Failed to get data out of file");

    let lines = file_contents.lines();

    let mut sum = 0;

    for line in lines {
        let mut options = vec![];
        for (index, char) in line.chars().enumerate() {
            for (second_index, second_char) in line.chars().enumerate() {
                if index >= second_index {
                    continue;
                }

                let option: i32 = format!("{char}{second_char}")
                    .trim()
                    .parse()
                    .expect("Failed to convert number");
                options.push(option);
            }
        }

        let mut max = options[0];

        for option in options {
            if option > max {
                max = option;
            }
        }

        sum += max;
    }

    println!("{sum}");
}
