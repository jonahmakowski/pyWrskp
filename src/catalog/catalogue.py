# This is a simple catalog app

import json
import time
import fuction

class catalog:
    def __init__(self, books):
        self.books = books
        while True:
            new_title = input('Please write the title of your book:   ')
            new_author = input('Please write the name of the author that the book is written by:   ')
            new_book = {'title':new_title, 'author':new_author}
            if new_title == '' and new_author == '':
                break
            self.books.append(new_book)
        self.active = False
        self.start()

    def start(self):
        try:
            self.read()
        except:
            print('could not find your "data.txt" file, please make sure it is in the same folder as this file')
            print('if you have not created a "data.txt" file or, have not run this code before, ignore this message')
            self.old_books = []
            fuction.wait()
        self.show()
        s = input('Would you like to search the books? (y/n)   ')
        while s == 'y':
            self.search()
            s = input('Would you like to search the books again? (y/n)   ')
        s = input('Would you like to search the web? (y/n)   ')
        if s == 'y':
            self.online_search()
        self.login()
        self.save()
        
        
    def save(self):
        with open('data.txt', 'w') as outfile:
            json.dump(self.books, outfile)
    
    def read(self):
        with open('data.txt') as json_file:
            self.old_books = json.load(json_file)
    
    def show(self):
        print('NEW BOOKS')
        print('=========')
        for book in self.books:
            print(book['title'])
        fuction.wait()
        print('OLD BOOKS:')
        print('==========')
        for book in self.old_books:
            print(book['title'])
            
    def search(self):
        from fuzzywuzzy import process
        
        qs = self.books + self.old_books
        query_t = input('What is the title of the book you are looking for?')
        query_a = input('What author of the book you are looking for?')
        query = {'title':query_t, 'author':query_a}
        ratios = process.extract(query, qs)
        
        for item in ratios:
            print(item[0]['title'] + ', ' + item[0]['author'])
    
    def online_search(self):
        fuction.online_search()
    
    def login(self):
        import login
        
        self.root = tk.Tk()
        self.root.title('Login')

        self.root.rowconfigure(0, minsize =800, weight = 1)
        self.root.columnconfigure(1, minsize =600, weight=1)

        self.app = Application(master=root)
        self.app.mainloop()

        if self.app.active == True and self.app.pas == self.app.code:
            self.active = True
    
    def admin(self):
        if self.active:
            while True:
                do = input('what do you want to do admin')
                if do == 'change books':
                    do = input('what type?')
                    if do == 'del':
                        num = int(input('What number do you want to del?'))
                        del self.books[num]
                    if do == 'add':
                        new_book_a = input('What is the author?')
                        new_book_t = input('What is the title?')
                        new_book = {'title':new_title, 'author':new_author}
                        self.books.append(new_book)
                
                if do == 'n':
                    break
                    

cat = catalog([])
