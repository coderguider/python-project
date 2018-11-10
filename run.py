import os
from flask import Flask, render_template, session, redirect, url_for, escape, request

app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        '<h1>Are you ready to begin %s?</h1>''   <input type="submit" value="Encrypt" name="Encrypt"/>>' % escape(session['username'])
        if request.form.get('Encrypt') == 'Encrypt':
            # pass
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))
    
 
def ganelogic(input):
    load json 
    save  json 
    x = 0
    count = 0
    while  x !=1:
        answser = input()
        write image teplete 
        
        you make call to load image,
        you listen for input ,
        if (filename && input in answser )
        {
                count+=1
            
        }
        else:
            print 'wrong'
            return redirect(url_for)


#OG python
# @app.route('/game/<name>')
# def game(name):
#     return render_template("game.html", name=name)

def imageChanger:
        print ''
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)