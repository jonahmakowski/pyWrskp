use std::fs::File;
use std::io::Read;

fn main() {
    let mut file = File::open("input.txt").expect("Failed to open the file");

    let mut file_contents = String::new();
    file.read_to_string(&mut file_contents)
        .expect("Failed to get data out of file");

    let ids: Vec<&str> = file_contents.split(",").collect();

    let ids: Vec<Vec<i64>> = ids
        .into_iter()
        .map(|data| {
            let ids: Vec<&str> = data.split("-").collect();

            let start: i64 = ids[0].trim().parse().expect("Couldn't convert number");
            let end: i64 = ids[1].trim().parse().expect("Couldn't convert number");

            let mut part = vec![];

            for i in start..end + 1 {
                part.push(i);
            }

            part
        })
        .collect();

    let mut sum = 0;

    for id_range in ids {
        for id in id_range {
            let id_str: String = id.to_string();

            for i in 1..id_str.len() {
                let mut invalid = false;

                let split = id_str.split_at(i);

                if id_str.split(split.0).filter(|data| !data.is_empty()).collect::<Vec<&str>>().is_empty() {
                    invalid = true;
                }

                if invalid {
                    sum += id;
                    println!("Invalid number {id} -- segments {} {}", split.0, split.1);
                    break;
                }
            }
        }
    }

    println!("Sum: {sum}");
}
