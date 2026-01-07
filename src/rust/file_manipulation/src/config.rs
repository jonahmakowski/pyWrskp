#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn build_search_config() {
        let mock_args = vec!["Path to executable", "search", "for_this", "in_this"].into_iter().map(|x| x.to_string());
            
        let conf = Config::build(mock_args).expect("Failed to build config");

        match conf {
            Config::Search(arg, path) => {
                assert_eq!(arg, "for_this");
                assert_eq!(path, "in_this");
            }
            _ => assert!(false),
        }
    }
}

/// # Config System
/// ## Build system
/// ### Search:
/// <executable> search <search argument> <file/folder path>
/// 
/// ## Enum Structure
/// ### Search:
/// First argument is search argument, second is the path.
pub enum Config {
    Search(String, String),
}

impl Config {
    pub fn build(mut args: impl Iterator<Item = String>) -> Result<Self, &'static str> {
        args.next();

        // Search
        if args.next().is_some_and(|x| x == "search") {
            let search_arg = match args.next() {
                Some(obj) => obj,
                None => return Err("Missing search argument"),
            };

            let path_arg = match args.next() {
                Some(obj) => obj,
                None => return Err("Missing path argument"),
            };

            return Ok(Self::Search(search_arg, path_arg));
        }

        panic!("hi there");
    }
}
