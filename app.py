from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_mail import Mail
import json
import os
import math
from datetime import datetime


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']

#contact sms from Mail=================================================================================================

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = 'True',
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password']
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

#contact page connect from Server=====================================================================================

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone_num = db.Column(db.String(13), nullable=False)
    msg = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(12), nullable=False)


#Post page connect from Server====================================================================================

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(13), nullable=False)
    tagline = db.Column(db.String(13), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    img_file = db.Column(db.String(25), nullable=False)
    img_path = db.Column(db.String(25), nullable=False)
    contents = db.Column(db.String(25), nullable=False)


#home page=====================================================================================

@app.route('/')
def home():
    flash("Welcome To Our Website. Hope you will enjoy it.", "primary")
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_post']))
    #[0: params['no_of_post']]
    #posts = posts[]
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)

    posts = posts[(page-1)*int(params['no_of_post']): (page-1)*int(params['no_of_post'])+ int(params['no_of_post'])]
    #Pagination Logic
    #First
    if(page==1):
        prev = "#"
        next = "/?page="+ str(page+1)
    elif(page==last):
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)




    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)


#about page=====================================================================================
@app.route('/about')
def about():
    return render_template('about.html', params=params)


#Dashboard login=====================================================================================
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if ('user' in session and session['user'] == params['admin_username']):
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts = posts)


    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_username'] and userpass == params['admin_password']):
            #set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts = posts)

    return render_template('login.html', params=params)

#post page=====================================================================================
@app.route('/post/<string:post_slug>', methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)




#edit page=========================================================================================================
@app.route('/edit/<string:sno>', methods = ['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_username']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            img_file = request.form.get('img_file')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_path = request.form.get('img_path')
            contents = request.form.get('contents')

            date = datetime.now()

            if sno =='0':
                post = Posts(title=box_title, slug=slug, content=content, tagline=tline, img_file=img_file, img_path=img_path, contents=contents,date=date)
                db.session.add(post)
                db.session.commit()

            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.slug = slug
                post.content = content
                post.tagline = tline
                post.img_file = img_file
                post.img_path = img_path
                post.contents = contents
                post.date = date
                db.session.commit()
                return redirect('/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno)


#File uploader=========================================================================================================
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_username']):
        if(request.method=='POST'):
            f= request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded Sucessfully"



#logout page=========================================================================================================
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')


#Post delete=========================================================================================================
@app.route('/delete/<string:sno>', methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_username']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')


#contact page=========================================================================================================
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, email = email, phone_num = phone, msg = message, date = datetime.now() )
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients = [params['gmail_user']],
                          body = phone + "\n" + message
        )
        flash("Your message has been send successfully. we will get back to you soon", "success")
    return render_template('contact.html', params=params)



app.run(debug=True)