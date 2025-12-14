use serde_derive::{Deserialize, Serialize};
use std::fmt::Display;

#[derive(PartialEq, Debug, Deserialize, Serialize)]
pub struct Date {
    pub year: u32,
    pub month: u32,
    pub day: u32,
}

#[derive(PartialEq, Debug, Deserialize, Serialize)]
pub struct Task {
    due_date: Date,
    task_name: String,
    done: bool,
}

impl Task {
    pub fn new(due_date: Date, task_name: &str) -> Self {
        Self {
            due_date,
            task_name: String::from(task_name),
            done: false,
        }
    }

    pub fn toggle_done(&mut self) -> bool {
        self.done = !self.done;
        self.done
    }
}

impl Display for Task {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> Result<(), std::fmt::Error> {
        writeln!(f, "\t{}", self.task_name)?;
        writeln!(
            f,
            "Due:\t{}/{}/{}",
            self.due_date.month, self.due_date.day, self.due_date.year
        )?;
        writeln!(f, "Done:\t{}", self.done)?;
        Ok(())
    }
}
