pub fn search<'a>(query: &str, contents: &'a str) -> impl Iterator<Item = &'a str> {
    contents.lines().filter(move |line| line.contains(query))
}

pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> impl Iterator<Item = &'a str> {
    contents
        .lines()
        .filter(move |line| line.to_lowercase().contains(&query.to_lowercase()))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_sensitive() {
        let query = "duct";
        let contents = "Rust:\nsafe, fast, productive\nPick three.\nDuct Tape.";

        let result: Vec<&str> = search(query, contents).collect();

        assert_eq!(vec!["safe, fast, productive"], result);
    }

    #[test]
    fn case_insensitive() {
        let query = "RuST";
        let contents = "Rust:\nsafe, fast, productive\nPick three\nTrust Me";

        let result: Vec<&str> = search_case_insensitive(query, contents).collect();

        assert_eq!(vec!["Rust:", "Trust Me"], result)
    }
}
