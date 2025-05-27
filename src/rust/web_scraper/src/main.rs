use select::document::Document;
use select::predicate::Name;
use std::error::Error;
use std::io::Cursor;

async fn scrape_webpage(url: &str) -> Result<String, Box<dyn Error>> {
    // Send an HTTP GET request
    let response = reqwest::get(url).await?;
    
    // Check if the response was successful
    if !response.status().is_success() {
        return Err(Box::new(std::io::Error::new(
            std::io::ErrorKind::Other,
            format!("Request failed with status: {}", response.status()),
        )));
    }

    // Parse the HTML document using Cursor to satisfy Read trait
    let html = response.text().await?;
    let document = Document::from_read(Cursor::new(html))?;

    // Extract all text from the document
    let text = document
        .find(Name("p")) // Find all paragraphs (you can change this selector)
        .into_iter()
        .map(|node| node.text())
        .collect::<Vec<_>>()
        .join("\n");

    Ok(text)
}

fn main() {
    trpl::run(async {
        let url = "https://www.cbc.ca/radio/quirks/lunar-dust-could-pose-serious-threat-to-future-moon-bases-and-astronauts-study-1.7227922";
        let content = scrape_webpage(url).await.unwrap();
        println!("Content:\n{}", content);
    });
}
