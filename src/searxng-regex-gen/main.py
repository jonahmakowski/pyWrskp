import re
from urllib.parse import urlparse

def generate_website_regex(website_input):
    """
    Generates a regular expression to match any URL from a given website.

    The regex covers:
    - Both HTTP and HTTPS protocols.
    - Optional 'www.' and other subdomains.
    - The core domain provided by the user.
    - Any path, query parameters, or fragments following the domain.

    Args:
        website_input (str): The URL or domain of the website (e.g., 'google.com',
                             'https://www.example.org/path', 'blog.mydomain.co.uk').

    Returns:
        str: A regex string, or an error message if the domain cannot be extracted.
    """
    # 1. Normalize and extract the core domain from the input
    parsed_url = urlparse(website_input)
    domain = parsed_url.netloc # This will be 'www.example.com', 'example.com', 'sub.example.co.uk', or empty

    # If netloc is empty, it means the input was likely just a domain (e.g., "example.com")
    # without a scheme (http://) or a full path.
    if not domain:
        # Assume the input itself is the domain, but strip leading/trailing slashes
        domain = website_input.strip().rstrip('/')
        # A very basic check: if it looks like a path starting with /, it's probably not a domain directly
        if domain.startswith('/'):
            return "Error: Input appears to be a path, not a domain or full URL."

    # Remove port if present (e.g., "example.com:8080" -> "example.com")
    if ':' in domain:
        domain = domain.split(':')[0]

    # Remove common "www." prefix if present.
    # Our regex allows for any subdomain, so we want the most fundamental part here.
    if domain.startswith('www.'):
        domain = domain[4:] # Remove 'www.'

    # Handle potential empty domain after processing
    if not domain:
        return "Error: Could not extract a valid domain from the input."

    # 2. Escape the domain for use in a regex (e.g., 'example.com' -> 'example\.com')
    escaped_domain = re.escape(domain)

    # 3. Construct the full regex pattern
    # - https?:\/\/ : Matches http:// or https://
    # - (?:[a-zA-Z0-9-]+\.)* : Matches zero or more subdomains (e.g., 'www.', 'blog.', 'sub.sub.')
    # - {escaped_domain} : The core domain (e.g., 'example\.com', 'my\.co\.uk')
    # - (?:\/[^\s]*)? : Optionally matches a path, query parameters, and fragments until a whitespace character
    regex_pattern = rf"https?:\/\/(?:[a-zA-Z0-9-]+\.)*{escaped_domain}(?:\/[^\s]*)?"

    return regex_pattern

# --- Main Script for User Interaction and Testing ---
if __name__ == "__main__":
    print("--- Regex Generator for Websites ---")
    print("This script generates a regex to match URLs from a specified domain,")
    print("including subdomains, paths, queries, and fragments.")
    print("It handles 'http://', 'https://', and 'www.' prefixes automatically.")
    print("-" * 35)

    while True:
        user_input = input("\nEnter a website URL or domain (e.g., 'google.com', 'https://example.org/path'): ").strip()
        if not user_input:
            print("No input provided. Exiting.")
            break

        generated_regex = generate_website_regex(user_input)

        if generated_regex.startswith("Error:"):
            print(generated_regex)
        else:
            print(f"\nGenerated Regex (use with re.IGNORECASE flag):")
            print(generated_regex)

            print("\n--- Example Usage (Python re module) ---")
            # Generate a few example URLs to test the generated regex
            try:
                # Use the same domain extraction logic for robust example URLs
                parsed_for_example = urlparse(user_input)
                example_domain_base = parsed_for_example.netloc if parsed_for_example.netloc else user_input
                if ':' in example_domain_base:
                    example_domain_base = example_domain_base.split(':')[0]
                if example_domain_base.startswith('www.'):
                    example_domain_base = example_domain_base[4:]
                example_domain_base = example_domain_base.strip('/')

                if example_domain_base:
                    sample_text = f"""
                    This should match: https://{example_domain_base}/some/page?id=123
                    This should also match: http://blog.{example_domain_base}/latest/article
                    And the main site: https://www.{example_domain_base}/
                    Even just the base: http://{example_domain_base}
                    This should NOT match: http://other.com/
                    This should NOT match: https://{example_domain_base}.evil.com/
                    """
                else:
                    sample_text = "Cannot create dynamic test cases for this input."

            except Exception:
                sample_text = "Error generating sample text for this input."
        
        print(sample_text)

        print("\n" + "=" * 40 + "\n")