from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.app_context().push()

@app.route('/')
def index():
    return render_template('index.html')

class Upload(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    filename = db.Column(db.String(50))
    data = db.Column(db.String)

def allowed_file(filename):
    return True if filename[-3:]=='txt' else False

@app.route('/acetylcholinesterase/',methods = ['GET','POST'])
def acetylcho():
    if request.method == 'POST':
        file = request.files['file']
        if allowed_file(file.filename) == True:
            upload = Upload(filename = file.filename,data=file.read())
            # db.session.add(upload)
            # db.session.commit()
            return f'Uploaded'
        else:
            return 'failed'
    else:
        return render_template('acetylcho.html')



if __name__=='__main__':
    app.run(debug=True)