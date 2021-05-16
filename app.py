from flask import Flask,request , render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class blog(db.Model):
    SNo = db.Column(db.Integer,primary_key = True)
    Name = db.Column(db.String(200),nullable = False)
    Msg = db.Column(db.String(1000), nullable = False)
    Phone = db.Column(db.String(10), nullable = False)
    Date = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Name}"




@app.route('/')
def home():
    return render_template ("index.html")

@app.route("/contact.html",methods=["POST","GET"])
def contact():
    return render_template ("contact.html")

@app.route('/submit.html',methods=["POST","GET"])
def submit():
    if request.method=='POST':
        nm=request.form["Name"]
        phn=request.form["Phone"]
        msg=request.form["Message"]
        admin= blog(Name=nm,Msg=msg,Phone=phn)
        db.session.add(admin)
        db.session.commit()
    return render_template("submit.html")

@app.route("/search.html")
def search():
    return render_template ("search.html")

@app.route("/index.html",methods=["POST","GET"])
def indext():
    return render_template ("index.html")

@app.route("/about.html")
def about():
    return render_template ("about.html")

if __name__=="__main__":
    app.run(debug=True,port=8000)


