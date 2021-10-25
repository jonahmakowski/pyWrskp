from flask import render_template, redirect, url_for
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
    {'creator':{'username':'Jonah', 'user':'Jonah1'},
     'content':'What does www stand for?',
     'info':'What does www (like https://www...) mean? www means World Wide Web!',
     'link':'/post/Jonah1'}]

CEO = {'name':'Jonah',
       'email':'jonah.kmjn@gmail.com'}

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
    email = 'Email:   ' + CEO['email']
    print(name + '\n' + email)
    return '<head> <title>CEO info</title> </head> <h1>DONE</h1> <p>info printed in shell</p> <a href="/">return to home page</a>'

@app.route('/youtube', methods=['POST', 'GET'])
def youtube():
    return render_template('youtube.html', title='youtube')

@app.route('/home/cac/n1=<num_1>/t=<type>/n2=<num2>')
def caculator(num_1, type, num_2):
    if type == '+':
        a = num_1 + num_2
    elif type == '-':
        a = num_1 - num_2
    elif type == '*':
        a = num_1 * num_2
    elif type == '/':
        a = num_1 / num_2
    return render_template('caculator.html', title='cacylator a', a = a)