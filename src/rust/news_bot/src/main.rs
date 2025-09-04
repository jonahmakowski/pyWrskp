use dotenv;
use select::document::Document;
use select::predicate::Name;
use std::error::Error;
use std::io::Cursor;

fn main() {
    dotenv::dotenv().ok();
    let newsdata_api_key =
        std::env::var("NEWSDATA_API_KEY").expect("NEWSDATA_API_KEY must be set.");
    let guardian_api_key =
        std::env::var("GUARDIAN_API_KEY").expect("GUARDIAN_API_KEY must be set.");
    let gnews_api_key = std::env::var("GNEWS_API_KEY").expect("GNEWS_API_KEY must be set.");
    let articles = get_articles(&newsdata_api_key, &guardian_api_key, &gnews_api_key);
    let articles = scrape_articles(articles);
}

fn scrape_articles(articles: Vec<serde_json::Value>) -> Vec<serde_json::Value> {
    let mut articles_with_content = Vec::new();
    for article in &articles {
        if let Some(link) = article["link"].as_str() {
            let mut current_content = String::new();
            match trpl::run(async { scrape_webpage(link).await }) {
                Ok(content) => {
                    println!("Content for {}:\n{}", article["title"], content);
                    current_content = content;
                }
                Err(e) => {
                    eprintln!("Error scraping {}: {}", link, e);
                    current_content = "Error scraping content".to_string();
                }
            }

            articles_with_content.push(serde_json::json!({
                "title": article["title"],
                "link": link,
                "content": current_content,
            }));
        } else {
            eprintln!("No link found for article: {}", article["title"]);
        }
    }
    articles_with_content
}

fn get_articles(
    newsdata_api_key: &str,
    guardian_api_key: &str,
    gnews_api_key: &str,
) -> Vec<serde_json::Value> {
    let newsdata_call = trpl::run(async {
        let url = "https://newsdata.io/api/1/latest";
        let content = call_api(url, &newsdata_api_key, "newsdata", "&language=en")
            .await
            .unwrap();
        content
    });

    let guardian_call = trpl::run(async {
        let url = "https://content.guardianapis.com/search";
        let content = call_api(url, &guardian_api_key, "guardian", "?page=1")
            .await
            .unwrap();
        content
    });
    let guardian_call2 = trpl::run(async {
        let url = "https://content.guardianapis.com/search";
        let content = call_api(url, &guardian_api_key, "guardian", "?page=2")
            .await
            .unwrap();
        content
    });
    let guardian_call3 = trpl::run(async {
        let url = "https://content.guardianapis.com/search";
        let content = call_api(url, &guardian_api_key, "guardian", "?page=3")
            .await
            .unwrap();
        content
    });
    let guardian_call4 = trpl::run(async {
        let url = "https://content.guardianapis.com/search";
        let content = call_api(url, &guardian_api_key, "guardian", "?page=4")
            .await
            .unwrap();
        content
    });

    let gnews_call = trpl::run(async {
        let url = "https://gnews.io/api/v4/top-headlines";
        let content = call_api(
            url,
            &gnews_api_key,
            "gnews",
            "?category=general&lang=en&country=ca",
        )
        .await
        .unwrap();
        content
    });

    let mut articles = Vec::new();

    for item in newsdata_call["results"].as_array().unwrap() {
        articles.push(serde_json::json!({
            "title": item["title"].as_str().unwrap(),
            "link": item["link"].as_str().unwrap(),
        }));
    }

    for item in guardian_call["response"]["results"].as_array().unwrap() {
        articles.push(serde_json::json!({
            "title": item["webTitle"].as_str().unwrap(),
            "link": item["webUrl"].as_str().unwrap(),
        }));
    }

    for item in guardian_call2["response"]["results"].as_array().unwrap() {
        articles.push(serde_json::json!({
            "title": item["webTitle"].as_str().unwrap(),
            "link": item["webUrl"].as_str().unwrap(),
        }));
    }

    for item in guardian_call3["response"]["results"].as_array().unwrap() {
        articles.push(serde_json::json!({
            "title": item["webTitle"].as_str().unwrap(),
            "link": item["webUrl"].as_str().unwrap(),
        }));
    }

    for item in guardian_call4["response"]["results"].as_array().unwrap() {
        articles.push(serde_json::json!({
            "title": item["webTitle"].as_str().unwrap(),
            "link": item["webUrl"].as_str().unwrap(),
        }));
    }

    for item in gnews_call["articles"].as_array().unwrap() {
        articles.push(serde_json::json!({
            "title": item["title"].as_str().unwrap(),
            "link": item["url"].as_str().unwrap(),
        }));
    }

    for article in &articles {
        println!("Title: {}\nLink: {}\n", article["title"], article["link"]);
    }

    println!("Total articles fetched: {}", articles.len());

    articles
}

async fn call_api(
    url: &str,
    api_key: &str,
    t: &str,
    arguments: &str,
) -> Result<serde_json::Value, Box<dyn Error>> {
    // Build the client and request with query parameters if provided
    let client = reqwest::Client::new();
    let mut url_with_params = url.to_string();

    // Add API key to headers if provided
    if t == "newsdata" {
        url_with_params.push_str(&format!("?apikey={}", api_key));
        url_with_params.push_str(&arguments);
    } else if t == "guardian" {
        url_with_params.push_str(&arguments);
        url_with_params.push_str(&format!("&api-key={}", api_key));
    } else if t == "gnews" {
        url_with_params.push_str(&arguments);
        url_with_params.push_str(&format!("&apikey={}", api_key));
    }

    let request_builder = client.get(&url_with_params);

    println!("Request URL: {}", url_with_params);

    // Send the request
    let response = request_builder.send().await?;

    // Check if the response was successful
    if !response.status().is_success() {
        return Err(Box::new(std::io::Error::new(
            std::io::ErrorKind::Other,
            format!("API request failed with status: {}", response.status()),
        )));
    }

    // Parse the JSON response
    let json_response = response.json::<serde_json::Value>().await?;

    Ok(json_response)
}

async fn scrape_webpage(url: &str) -> Result<String, Box<dyn Error>> {
    // Create a client with a custom user agent
    let client = reqwest::Client::builder()
        .user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        .build()?;

    // Send an HTTP GET request with the custom client
    let response = client.get(url).send().await?;

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
