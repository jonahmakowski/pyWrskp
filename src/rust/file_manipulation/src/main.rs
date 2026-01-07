use std::env;
mod config;
mod search;

fn main() {
    let args = env::args();

    let conf = match config::Config::build(args) {
        Ok(c) => c,
        Err(err) => {
            eprintln!("{err}");
            return;
        }
    };

    match conf {
        config::Config::Search(for_text, in_path) => {
            match search::perform_search(&in_path, &for_text) {
                Ok(_) => (),
                Err(err) => {
                    eprintln!("{err}");
                    return;
                }
            }
        }
    }
}
