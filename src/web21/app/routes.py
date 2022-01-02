from flask import request, render_template, redirect
from app import app
import sys
import os

try:
    pyWrkspLoc = os.environ["PYWRKSP"]
   
except KeyError:
    pyWrkspLoc = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                            '\nPlease enter the pwd for the pyWrskp repo not including the '
                                            '"home" section')
    # pyWrskpLoc = '/Users/jonahmakowski/Desktop/Github/pyWrskp'  #for debug, so you don't have to enter info
User = ''

blogPosts_list = [
    {
        'creator': {'username': 'Jonah', 'user': 'Jonah'},
        'content': 'Why this website is better then the other',
        'info': 'It is home made by me! It also has many pages, unlike the first website I made!',
        'link': '/post/Jonah'
    },
    {
        'creator': {'username': "Mr. Payne's 4/5 class 2020-21", 'user': "Mr.Payne's+45+class+2020-21"},
        'content': 'Why in-person school is better then the online version',
        'info': "In-person school is so much better than online school "
                "because when we are in person we can chat, and eat together "
                "(note this was not written by Mr.Payne's class, it was written by Jonah)",
        'link': "/post/Mr.Payne's+45+class"
        },
    {
        'creator': {'username': 'Jonah', 'user': 'Jonah1'},
        'content': 'What does www stand for?',
        'info': 'What does www (like https://www...) mean? www means World Wide Web!',
        'link': '/post/Jonah1'
        },
    {
        'creator': {'username': 'Jonah', 'user': 'Jonah2'},
        'content': 'How to show the CEO info',
        'info': 'in your web address bar, remove "/link/Jonah2", and put "/ceo+info" '
                'instead, then press enter, and bingo, you got the CEO info!',
        'link': '/post/Jonah2'
        }]

CEO = {'name': 'Jonah Makowski',
       'emails': {
        '1': 'jonah.kmjn@gmail.com',
        '2': 'jonah@makowski.ca',
        '3': 'jonah@makowski.at'},
       'link': 'https://www.youtube.com/channel/UC1ti62i-uMnBVAh9b_Pp3UA/'}


@app.route('/', methods=['POST', 'GET'])
@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    return render_template('index.html', title='Welcome', User=User)


@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html', title='Home', User=User)


@app.route('/home/blogposts', methods=['POST', 'GET'])
@app.route('/home/blogposts/', methods=['POST', 'GET'])
@app.route('/blogposts', methods=['POST', 'GET'])
def blog_posts():
    return render_template('posts.html', title='blog posts', posts=blogPosts_list)


@app.route('/post/<creator>', methods=['POST', 'GET'])
def post(creator):
    usr = False
    for item in blogPosts_list:
        if item['creator']['user'] == creator:
            usr = True
            break
    if not usr:
        error_code = '404'
        error = '{} error'.format(str(error_code))
        title = error
        return render_template('error.html', title=title, error=error)
    else:
        return render_template('Blog_outline.html', title=post['creator']['username'] + "'s blog post", post=post)


@app.route('/home/blogposts/small', methods=['POST', 'GET'])
@app.route('/home/blogposts/small/', methods=['POST', 'GET'])
@app.route('/blogposts/small', methods=['POST', 'GET'])
@app.route('/blogposts+small', methods=['POST', 'GET'])
@app.route('/home/blogposts+small', methods=['POST', 'GET'])
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
    if request.method == "POST":
        return redirect(CEO['link'])
    elif request.method == 'GET':
        name = 'Name:         ' + CEO['name']
        email = 'Emails:       {}, {}, {}'.format(CEO['emails']['1'], CEO['emails']['2'], CEO['emails']['3'])
        link = 'Youtube channel: ' + CEO['link']
        print(name + '\n' + email + '\n' + link)
        return render_template('CEO_info.html', title='CEO info', name=name, email=email, link=link)
    else:
        print('request.method is not get or post it is {}'.format(request.method))
        exit(5)


@app.route('/youtube', methods=['POST', 'GET'])
def youtube():
    return render_template('youtube.html', title='youtube')


@app.route('/page', methods=['POST', 'GET'])
def page():
    return render_template('page.html', title='List of Pages | This is a list of pages on this website')


@app.route('/cac', methods=['POST', 'GET'])
def calculator():
    if request.method == "POST":
        global pyWrkspLoc
        try:
            num2 = int(request.form.get("num2"))
        except ValueError:
            num2 = None
        num1 = int(request.form.get('num1'))
        t = request.form.get('type')
        try:
            num1 = float(num1)
            num2 = float(num2)
            if t == '+':
                a = num1 + num2
                q = '{} + {}'.format(num1, num2)
            elif t == '-':
                a = num1 - num2
                q = '{} - {}'.format(num1, num2)
            elif t == '*':
                a = num1 * num2
                q = '{} * {}'.format(num1, num2)
            elif t == '/':
                a = num1 / num2
                q = '{} / {}'.format(num1, num2)
            elif t == '**':
                a = num1 ** num2
                q = '{} ** {}'.format(num1, num2)
            elif t == '^':
                from math import sqrt
                a = sqrt(num1)
                q = '√{}'.format(num1)
            else:
                a = "ISSUE CODE CAN NOT FIND NUMBERS NECESSARY, TALK TO THE OWNER OF THIS WEBSITE"
                q = a
        except AssertionError as error:
            q = error
            a = 'The linux_interaction() function was not executed'
        except ValueError as error:
            q = error
            a = 'The first or other string is not a int or float'
        return render_template('calculator.html', title='Calculator', a=a, q=q)
    elif request.method == 'GET':
        return render_template('calculator_redirect.html', title='Calculator Sender')
    else:
        print('request.method is not get or post it is {}'.format(request.method))
        exit(5)


@app.route('/passwords', methods=['GET', 'POST'])
def passwords():
    if request.method == "POST":
        global pyWrkspLoc
        
        sys.path.append(pyWrkspLoc + '/src/password_maker')

        from Creater import create
        
        password = create(request.form.get("letters"),
                          request.form.get("numbers"),
                          request.form.get("sc"),
                          request.form.get("super_c"),
                          int(request.form.get("length")),
                          'n',
                          False)
        return render_template('password_show.html', title='Passwords', password=password)
    elif request.method == 'GET':
        return render_template('passwords.html', title='Passwords')
    else:
        print('request.method is not get or post it is {}'.format(request.method))
        exit(5)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global User
    if request.method == "POST":
        global pyWrkspLoc
        password = request.form.get("password")
        User = request.form.get("username")
        if User == 'WhiteSwine' and password == 'LOLA IS THE BEST':
            return render_template('logged_in.html', title='logged in!', user=User)
        else:
            return '<h1>INCORRECT</h1>'
    elif request.method == 'GET':
        return render_template('login.html', title='login')
    else:
        print('request.method is not get or post it is {}'.format(request.method))
        exit(5)


@app.route('/noah')
@app.route('/turtle', methods=['GET', 'POST'])
def turtle():
    if request.method == "POST":
        global pyWrkspLoc
        
        sys.path.append(pyWrkspLoc + '/src/other/home')
        
        try:
            from noah_and_me_turtle import run
            run()
        except:  # I know there is a warning here, but I am not sure how to fix it, if you know how please do
            return redirect('/')
        return '<h1>Done</h1> <p>if nothing is happening, you have an error</p> <a href="/">return to home page</a>'
    elif request.method == 'GET':
        return render_template('turtle.html', title='Noah and me turtle')
    else:
        print('request.method is not get or post it is {}'.format(request.method))
        exit(5)


@app.route('/pygame/draw', methods=['GET', 'POST'])
def draw():
    if request.method == "POST":
        global pyWrkspLoc
        sys.path.append(pyWrkspLoc + '/src/other/classes')
        
        from Class_one import draw
        
        draw()
        return '<h1>Done</h1> <p>if nothing is happening, you have an error</p> <a href="/">return to home page</a>'
    elif request.method == 'GET':
        return render_template('pygame_draw.html', title='DRAW!')
    else:
        print('request.method is not get or post it is {}'.format(request.method))
        exit(5)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    return render_template('feedback.html', title='Feedback')


@app.route('/fire', methods=['GET', 'POST'])
def fire():
    return render_template('fire.html', title='Fire')


@app.route('/alarm', methods=['GET', 'POST'])
def alarm():
    if request.method == 'POST':
        global pyWrkspLoc
        sys.path.append(pyWrkspLoc + '/src/alarm')
        
        from time_only import work
        
        work(request.form.get('hour'), request.form.get('min'), print_info=False)
        
        return '<h1>DING-DONG</h1> <a href="/">return to home page</a>'
    elif request.method == 'GET':
        return render_template('alarm.html', title='Alarm clock!')
    else:
        print('request.method is not get or post it is {}'.format(request.method))
        exit(5)


@app.route('/lola', methods=['GET', 'POST'])
def lola():
    return render_template('lola.html', title='Lola Image')


@app.route('/code', methods=['GET', 'POST'])
def code():
    if request.method == 'POST':
        sys.path.append(pyWrkspLoc + '/src/coder-decoder')
        
        from coder import coderDecoder
        key = int(request.form.get('key'))
        coder_decoder = request.form.get('type')
        
        coder = coderDecoder(print_info=False)
        coder.add_vars(message=request.form.get('message'), key=key, )
        if coder_decoder == 'code':
            message = coder.code()
        elif coder_decoder == 'decode':
            message = coder.decode()
        else:
            print('error within code')
            print('coder_decoder did not equal code or decode, exiting')
            message = 'error within code\ncoder_decoder did not equal code or decode, exiting'
        return render_template('coder_show.html', title='coder decoder show', message=message, key=key)
    elif request.method == 'GET':
        return render_template('coder.html', title='coder decoder')
    else:
        print('request.method is not get or post it is {}'.format(request.method))
        exit(5)


@app.route('/fun', methods=['GET', 'POST'])
def fun():
    return render_template('fun.html', title='Fun')


@app.route('/translater', methods=['GET', 'POST'])
def translater():
    if request.method == 'POST':
        language = request.form.get('language')
        text = request.form.get('text')
        from translate import Translator
        translator = Translator(to_lang=language)
        trans = translator.translate(text)
        if text != trans:
            return trans
        elif text == trans:
            return '<h1>Language not supported</h1> ' \
                   '<p>This language you used is not one of the languages supported on this translater</p>'
    elif request.method == 'GET':
        return render_template('translate.html', title='translater')
    else:
        print('request.method is not get or post it is {}'.format(request.method))
        exit(5)


@app.route('/christmas', methods=['GET', 'POST'])
def christmas_tree():
    return render_template('christmas_tree.html', title='Christmas')


@app.route('/notes/write', methods=['GET', 'POST'])
def notes_write():
    if request.method == 'POST':
        import json
        sys.path.append(pyWrkspLoc + '/src/notes')
        from notes import Notes
        n = Notes(name=pyWrkspLoc + '/docs/txt-files/data4.txt')
        n.add_note(request.form.get('note'))
        n.save_notes()
        return 'Your note {} was saved'.format(request.form.get('note'))
    elif request.method == 'GET':
        return render_template('notes.html', title='Notes writer')
    else:
        print('request.method is not get or post it is {}'.format(request.method))
        exit(5)


@app.route('/notes/read', methods=['GET', 'POST'])
def notes_read():
    import json
    try:
        with open(pyWrkspLoc + '/docs/txt-files/data4.txt') as json_file:
            notes = json.load(json_file)
    except:
        notes = ['You have 0 notes']
    print(notes)
    return render_template('notes_read.html', title='Notes reader', notes=notes)


'''
# This code is not working, not sure why, this is the same code as in the orginal page.
@app.route('/txt', methods=['GET', 'POST'])
def txt():
    if request.method == 'POST':
        sys.path.append(pyWrkspLoc + '/src/other/classes')
        import class_4_pt_1
        import tkinter as tk
        df_save_loc = '/home/jonah/Thonny files/TXT_files/' # change to folder name where you want auto saves as def
        df_name = 'testing' # you can change def save name
        root = tk.Tk()
        root.title('Text Editer')
        root.rowconfigure(0, minsize=800, weight=1)
        root.columnconfigure(1, minsize=600, weight=1)
        app = class_4_pt_1.Application(df_name, df_save_loc, master=root)
        app.mainloop()
        return redirect('/')
    return render_template('txt.html', title='text editer')
'''
