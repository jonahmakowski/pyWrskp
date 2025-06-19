import webbrowser


def online_search():
    author = input("What is the author of the book?")
    author = list(author)
    for i in range(len(author)):
        if author[i] == " ":
            author[i] = "+"
    author2 = ""
    for char in author:
        author2 += char
    title = input("What is the title of the book?")
    title = list(title)
    for i in range(len(title)):
        if title[i] == " ":
            title[i] = "+"
    title2 = ""
    for char in title:
        title2 += char
    # print('Click here:')
    # print('https://www.google.com/search?q={}%2C+{}'.format(author2, title2)
    webbrowser.open("https://www.google.com/search?q={}%2C+{}".format(author2, title2))


def wait():
    input("Press enter to continue")
