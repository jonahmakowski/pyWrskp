use std::fs::File;
use std::io::Read;

use crate::types::*;

fn read_from_tasks(file_path: &str) -> Vec<Task> {
    let mut return_early = false;

    let mut file = File::open(&file_path).unwrap_or_else(|err| {
        if err.kind() == std::io::ErrorKind::NotFound {
            return_early = true;
            File::create(&file_path).expect("Failed to create file")
        } else {
            panic!("Problem opening the file: {:?}", err)
        }
    });

    if return_early {
        return vec![];
    }

    let mut file_contents = String::new();
    file.read_to_string(&mut file_contents)
        .expect("Failed to read file");

    if file_contents.trim().is_empty() {
        vec![]
    } else {
        serde_json::from_str(&file_contents).unwrap_or_else(|err| {
            eprintln!("Couldn't load file to json: {err}");
            std::process::exit(1);
        })
    }
}

fn write_to_tasks(file_path: &str, data: Vec<Task>) {
    let file_contents = serde_json::to_string(&data).expect("Failed to serialize tasks to JSON");

    std::fs::write(file_path, file_contents).expect("Failed to write to file");
}

pub fn list_tasks(file_path: &str) {
    let tasks = read_from_tasks(file_path);

    if tasks.len() == 0 {
        println!("There aren't any tasks right now");
        return;
    }

    for (index, task) in tasks.iter().enumerate() {
        print!("#{}\t", index + 1);
        println!("{}\n\n", format!("{task}").replace("\n", "\n\t"));
    }
}

pub fn create_task(file_path: &str, task: Task) {
    let mut tasks = read_from_tasks(file_path);

    tasks.push(task);

    write_to_tasks(file_path, tasks);
}

pub fn toggle_task_done(file_path: &str, ind: isize) -> Result<(), &str> {
    let mut tasks = read_from_tasks(file_path);
    let mut ind = ind;

    if tasks.len() == 0 {
        return Err("There aren't any notes right now.");
    }

    if ind == -1 {
        list_tasks(file_path);

        println!("Choose an task number to mark as done:");
        ind = match simple_lib::input::get_num_input() {
            Ok(ind) => ind,
            Err(err) => return Err(err),
        };
    }

    ind -= 1;

    if !(ind >= 0 && ind < tasks.len() as isize) {
        return Err("Task # outside of range.");
    }

    tasks[ind as usize].toggle_done();

    write_to_tasks(file_path, tasks);

    println!("Updated Task list:");
    list_tasks(file_path);

    Ok(())
}

pub fn remove_task(file_path: &str, ind: isize) -> Result<(), &str> {
    let mut tasks = read_from_tasks(file_path);
    let mut ind = ind;

    if tasks.len() == 0 {
        return Err("There aren't any notes right now.");
    }

    if ind == -1 {
        list_tasks(file_path);

        println!("Choose an task number to delete:");
        ind = match simple_lib::input::get_num_input() {
            Ok(ind) => ind,
            Err(err) => return Err(err),
        };
    }

    ind -= 1;

    if !(ind >= 0 && ind < tasks.len() as isize) {
        return Err("Task # outside of range.");
    }

    tasks.swap_remove(ind as usize);

    write_to_tasks(file_path, tasks);

    println!("Updated Task list:");
    list_tasks(file_path);

    Ok(())
}
