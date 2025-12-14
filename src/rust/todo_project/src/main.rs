use std::process;
use config::Config;

mod config;
mod types;
mod functions;

fn main() {
    const FILE: &str = "data.json";

    let conf = match config::Config::build() {
        Ok(conf) => conf,
        Err(err) => {
            println!("Error: {err}");
            process::exit(1);
        },
    };

    match conf {
        Config::NewTask(task) => functions::create_task(FILE, task),
        Config::ListTasks => functions::list_tasks(FILE),
        Config::RemoveTask(ind) => {
            if let Err(err) = functions::remove_task(FILE, ind) {
                eprintln!("Error: {err}");
            };
        },
        Config::ToggleDone(ind) => {
            if let Err(err) = functions::toggle_task_done(FILE, ind) {
                eprintln!("Error: {err}");
            };
        },
        Config::Default => eprintln!("Config incorrectly setup"),
    }
}
