use minigrep::{search, search_case_insensitive};
use std::{env, error::Error, fs, process};

fn main() {
    let conf = Config::build().unwrap_or_else(|err| {
        eprintln!("{err}");
        process::exit(1);
    });

    if let Err(e) = run(conf) {
        eprintln!("Error: {e}");
        process::exit(1);
    }
}

struct Config {
    query: String,
    file: String,
    ignore_case: bool,
}

impl Config {
    fn build() -> Result<Self, &'static str> {
        let args: Vec<String> = env::args().collect();

        if args.len() < 3 {
            return Err("Not enough arguments, be sure to include a file and a search string");
        }

        let conf = Config {
            query: args[1].clone(),
            file: args[2].clone(),
            ignore_case: env::var("IGNORE_CASE").is_ok(),
        };

        Ok(conf)
    }
}

fn run(conf: Config) -> Result<(), Box<dyn Error>> {
    let file_contents = fs::read_to_string(&conf.file)?;

    let results = if conf.ignore_case {
        search_case_insensitive(&conf.query, &file_contents)
    } else {
        search(&conf.query, &file_contents)
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
