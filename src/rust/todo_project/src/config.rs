use crate::types::*;
use std::{env, num::ParseIntError};

/// # Config for what the executable should do
/// Has four modes:
/// 1. Make a new task
/// 2. List all the tasks
/// 3. Remove a task from the list
/// 4. Mark a task as done
#[derive(Debug)]
pub enum Config {
    NewTask(Task),
    ListTasks,
    RemoveTask(isize),
    ToggleDone(isize),
    Default,
}

impl Config {
    /// # Config Building Function
    /// The options look like this:
    /// 1. new <task-name> <due-month> <due-day> <due-year>
    /// 2. list
    /// 3. remove
    /// 4. done
    ///
    /// Numbers 3-4 will display a list, and then mark a task as done or remove it.
    pub fn build() -> Result<Self, &'static str> {
        let mut result = Config::Default;
        let mut args = env::args();

        // Skip where it shows the path to the executable
        args.next();

        match args.next() {
            Some(arg) => {
                if arg == "new" {
                    let task_name = match args.next() {
                        Some(arg) => arg,
                        None => return Err("No task name"),
                    };

                    let due_month: Result<u32, ParseIntError> = match args.next() {
                        Some(arg) => arg,
                        None => return Err("No due month"),
                    }
                    .trim()
                    .parse();

                    let due_day: Result<u32, ParseIntError> = match args.next() {
                        Some(arg) => arg,
                        None => return Err("No due day"),
                    }
                    .trim()
                    .parse();

                    let due_year: Result<u32, ParseIntError> = match args.next() {
                        Some(arg) => arg,
                        None => return Err("No due year"),
                    }
                    .trim()
                    .parse();

                    let due_month = match due_month {
                        Ok(month) => month,
                        Err(_) => return Err("Can not parse month"),
                    };

                    let due_day = match due_day {
                        Ok(month) => month,
                        Err(_) => return Err("Can not parse month"),
                    };

                    let due_year = match due_year {
                        Ok(month) => month,
                        Err(_) => return Err("Can not parse month"),
                    };

                    result = Config::NewTask(Task::new(
                        Date {
                            year: due_year,
                            month: due_month,
                            day: due_day,
                        },
                        &task_name,
                    ));
                } else if arg == "list" {
                    result = Config::ListTasks;
                } else if arg == "remove" {
                    let index = args.next().unwrap_or("-1".to_string());

                    let index = match index.trim().parse() {
                        Ok(ind) => ind,
                        Err(_) => return Err("Failed to parse index"),
                    };

                    result = Config::RemoveTask(index);
                } else if arg == "done" {
                    let index = args.next().unwrap_or("-1".to_string());

                    let index = match index.trim().parse() {
                        Ok(ind) => ind,
                        Err(_) => return Err("Failed to parse index"),
                    };

                    result = Config::ToggleDone(index);
                }
            }
            None => return Err("Lacking first argument"),
        }

        Ok(result)
    }
}
