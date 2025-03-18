# Documentation for src/voiceAssistants/voiceAssistant/helpers/removeKeyword.py

# remove_keyword

## Description

The `remove_keyword` function takes a string of text and a keyword as input. It removes the first occurrence of the keyword from the text and returns the modified text as a string. If the keyword is not found in the text, the function raises a `ValueError`.

## Parameters

*   `text` (str): The input text from which the keyword will be removed.
*   `keyword` (str): The keyword to be removed from the text.

## Returns

*   `new` (str): The modified text with the keyword removed.

## Example Usage

Usage example for `remove_keyword`:

```python
text = "This is a sample text with the keyword sample in it."
keyword = "sample"
new_text = remove_keyword(text, keyword)
print(new_text)  # Output: "This is a text with the keyword in it."
```

In this example, the keyword "sample" is removed from the input text, and the modified text is printed.