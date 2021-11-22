from flask import Flask, request, render_template, redirect
from app import app

currentUser = {'username': input('What is your name?\n')}
blogPosts_list = [
    {
        'creator':{'username':'Jonah', 'user':'Jonah'},
        'content':'Why this website is better then the other',
        'info':'It is home made by me! It also has many pages, unlike the first website I made!',
        'link':'/post/Jonah'
    },
    {
        'creator':{'username':"Mr. Payne's 4/5 class 2020-21", 'user':"Mr.Payne's+45+class+2020-21"},
        'content':'Why in-person school is better then the online version',
        'info':"In-person school is sooooooooooo much better than online school becuase when we are in person we can chat, and eat together (note this was not written by Mr.Payne's class, it was written by Jonah)",
        'link':"/post/Mr.Payne's+45+class"
        },
    {
        'creator':{'username':'Jonah', 'user':'Jonah1'},
     'content':'What does www stand for?',
     'info':'What does www (like https://www...) mean? www means World Wide Web!',
     'link':'/post/Jonah1'
        }]

CEO = {'name':'Jonah',
       'email':'jonah.kmjn@gmail.com',
       'email2':'jonah@makowski.ca',
       'email3':'jonah@makowski.at'}

@app.route('/', methods=['POST', 'GET'])
@app.route('/welcome', methods=['POST', 'GET'])
def Welcome():
    return render_template('index.html', title='Welcome', user=currentUser)

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html', title='Home', user=currentUser)

@app.route('/home/blogposts', methods=['POST', 'GET'])
@app.route('/home/blogposts/', methods=['POST', 'GET'])
@app.route('/blogposts', methods=['POST', 'GET'])
def blog_posts():
    return render_template('posts.html', title='blog posts', posts=blogPosts_list)

@app.route('/post/<creator>', methods=['POST', 'GET'])
def post(creator):
    usr = False
    for post in blogPosts_list:
        if post['creator']['user'] == creator:
            usr = True
            break
    if usr == False:
        error_code = '404'
        error='{} error'.format(str(error_code))
        title = error
        return render_template('error.html', title=title, error=error)
    else:
        return render_template('Blog_outline.html', title=post['creator']['username'] + "'s blog post", post=post)

@app.route('/home/blogposts/small', methods=['POST', 'GET'])
def blog_post_small():
    return render_template('posts_small.html', title='blog posts', posts=blogPosts_list)

@app.route('/music', methods=['POST', 'GET'])
def music():
    return render_template('music.html', title='Music')

@app.route('/calendar', methods=['POST', 'GET'])
def calendar():
    return render_template('calendar.html', title='calendar')

@app.route('/ceo+info', methods=['POST', 'GET'])
def ceo_info():
    name = 'Name:    ' + CEO ['name']
    email = 'Email:   {}, {}, {}'.format(CEO['email'], CEO['email2'], CEO['email3'])
    print(name + '\n' + email)
    return '<head> <title>CEO info</title> </head> <h1>DONE</h1> <p>info printed in shell</p> <a href="/">return to home page</a>'

@app.route('/youtube', methods=['POST', 'GET'])
def youtube():
    return render_template('youtube.html', title='youtube')

@app.route('/page', methods=['POST', 'GET'])
def page():
    return render_template('page.html', title='List of Pages | This is a list of pages on this website')

@app.route('/cac', methods=['POST', 'GET'])
def caculator_sender():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        num1 = float(request.form.get("num1"))
        try:
            num2 = float(request.form.get("num2"))
        except:
            pass
        type = request.form.get("type")
        try:
            if type == '+':
                a = num1 + num2
                q = '{} + {}'.format(num1, num2)
            elif type == '-':
                a = num1 - num2
                q = '{} - {}'.format(num1, num2)
            elif type == '*':
                a = num1 * num2
                q = '{} * {}'.format(num1, num2)
            elif type == '/':
                a = num1 / num2
                q = '{} / {}'.format(num1, num2)
            elif type == '**':
                a = num1 ** num2
                q = '{} ** {}'.format(num1, num2)
            elif type == '^':
                from math import sqrt
                a = sqrt(num1)
                q = '{}^'.format(num1)
            else:
                a = "ISSUE CODE CAN NOT FIND NUMBERS NESSARY, TALK TO THE OWNER OF THIS WEBSITE"
        except:
            q = "ISSUE"
            a = "ISSUE"
        return render_template('caculator.html', title='Caculator', a = a, q = q)
    return render_template('caculator_redirect.html', title='Caculator Sender')

@app.route('/passwords', methods=['GET', 'POST'])
def passwords():
    if request.method == "POST":
        from random import randint

        letter = request.form.get("letters")
        num = request.form.get("numbers")
        sc = request.form.get("sc")
        super_c = request.form.get("super_c")
        length = int(request.form.get("length"))

        chars = []
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        scs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '~', '`', '{', '}', '[', ']', ';', ':', '"', "'", '<', '>', '?', ',',
               '.', '/', '|']
        super_s_c = ['←', '↑', '→', '↓', '·', '•', '●', '–', '‽', '‖', '«', '»', '‘', '„', '✅', '❤️', '⌘', '', '⌥', '⌫', '∞', '™', '¼', '½', '¾', 'À', 'Á', 'Â', 'Ã',
                     'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'æ', 'Ħ',
                     'ĳ', 'Œ', 'œ', '☚', '☛', '★', '☆', '♠', '♣', '♥', '♦', '♪', '♫', '♀']
        
        create = True
        if letter == 'y':
            chars += letters
        if num == 'y':
            chars += nums
        if sc == 'y':
            chars += scs
        if super_c == 'y':
            chars += super_s_c
        if (letter == 'n' and num == 'n') and (sc == 'n' and super_c == 'n'):
            create = False

        password = ''
        if create:
            for i in range(length):
                loc = randint(0, len(chars) - 1)
                password += chars[loc]
        elif create == False:
            password = 'Sorry, you have put no in all the questions, so there are no options'
        return render_template('password_show.html', title='Passwords', password=password)
    '''
    else:
        print('ERROR')
        print('not supported method {}'.format(request.method))
    '''
    return render_template('passwords.html', title='Passwords')