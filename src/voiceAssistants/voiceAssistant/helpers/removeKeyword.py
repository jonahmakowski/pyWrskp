def remove_keyword(text, keyword):
    text_list = text.split()
    text_list.remove(keyword)

    new = ""
    for word in text_list:
        new += word + " "

    new = new[:-1]

    return new
