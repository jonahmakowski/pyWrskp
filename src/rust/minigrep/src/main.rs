use std::{env, fs, process, error::Error};
use minigrep::{search, search_case_insensitive};

fn main() {
    let conf = Config::build(env::args()).unwrap_or_else(|err| {
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
    fn build(mut args: impl Iterator<Item = String>) -> Result<Self, &'static str> {
        args.next();
        
        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Failed to get query string"),
        };

        let file = match args.next() {
            Some(arg) => arg,
            None => return Err("Failed to get file path string"),
        };
        
        let conf = Config {
            query,
            file,
            ignore_case: env::var("IGNORE_CASE").is_ok(),
        };

        Ok(conf)
    }
}

fn run(conf: Config) -> Result<(), Box<dyn Error>> {
    let file_contents = fs::read_to_string(&conf.file)?;

    let results: Box<dyn Iterator<Item = &str>> = match conf.ignore_case {
        true => Box::new(search_case_insensitive(&conf.query, &file_contents)),
        false => Box::new(search(&conf.query, &file_contents)),
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
