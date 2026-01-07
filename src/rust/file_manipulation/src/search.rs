use colored::*;
use std::{fs, io};

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn search_text_test() {}
}

pub fn perform_search(path: &str, for_text: &str) -> Result<(), &'static str> {
    let files = match get_file_info(path) {
        Ok(obj) => obj,
        Err(_) => return Err("Failed to get file info"),
    };

    for file in &files {
        let mut printed = false;
        if file.to_lowercase().contains(&for_text.to_lowercase()) {
            print_section_bold(file, for_text);
            printed = true;
        }

        if file.ends_with("/") {
            continue;
        }

        let file_contents = match fs::read_to_string(file) {
            Ok(contents) => contents,
            Err(_) => {
                //eprintln!("Failed to open file {file}");
                continue;
            }
        };

        let (internal_results, lines) = search_text(&for_text, &file_contents);

        if internal_results.len() != 0 && !printed {
            println!("{file}");
            printed = true;
        }

        for (index, m) in internal_results.iter().enumerate() {
            print!("{}\t", lines[index]);
            print_section_bold(m, &for_text);
        }

        if printed {
            println!("\n");
        }
    }

    Ok(())
}

fn get_file_info(path: &str) -> Result<Vec<String>, io::Error> {
    if fs::read(path).is_ok() {
        return Ok(vec![path.to_string()]);
    }

    let mut data = vec![];

    for entry in fs::read_dir(path)? {
        let entry = entry?;
        let path = entry.path();
        let mut path_str = entry.path().to_string_lossy().to_string();

        if path.is_dir() {
            data.append(&mut get_file_info(&path_str)?);
            path_str.push('/');
        }

        data.push(path_str);
    }

    return Ok(data);
}

/// Prints all occurrences of `section` within `text` in bold and red
fn print_section_bold(text: &str, section: &str) {
    let mut start = 0;
    let lower_text = text.to_lowercase();
    let lower_section = section.to_lowercase();

    while let Some(pos) = lower_text[start..].find(&lower_section) {
        let actual_start = start + pos;
        let actual_end = actual_start + section.len();

        print!("{}", &text[start..actual_start]);

        print!("{}", &text[actual_start..actual_end].bold().red());

        start = actual_end;
    }

    print!("{}", &text[start..]);
    println!();
}

fn search_text<'a>(query: &str, contents: &'a str) -> (Vec<&'a str>, Vec<i32>) {
    let mut lines = vec![];
    let mut current_line = 1;
    let mut results = vec![];

    for line in contents.lines() {
        if line.to_lowercase().contains(&query.to_lowercase()) {
            lines.push(current_line);
            results.push(line);
        }
        current_line += 1;
    }

    (results, lines)
}
