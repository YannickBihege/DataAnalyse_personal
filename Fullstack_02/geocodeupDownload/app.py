from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)

db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:xboxer89@localhost/heightcollector'
#data model

##in the console for test
# from app import db
#>>> db.create_all()
class Data(db.Model):
    __tablename__ ="data"
    id= db.Column(db.Integer, primary_key = True)
    email_= db.Column(db.String(120), unique = True)
    height_= db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods =['POST'])
def success():
    if request.method =='POST':
        email = request.form['email_name'] #grab the mail
        height = request.form['height_name'] #grab the mail
        #send_email(email, height)

        print('request: {}'.format(request))
        print('------------------------------------------')
        print('request form: {}'.format(request.form))

        #insert when the key is unique
        if db.session.query(Data).filter(Data.email_ ==email).count() == 0:
            print('---------------')
            print('Session')
            print(db.session)
            # add to database
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            print('--------average-------')

            #average function
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            print(average_height)
            print(db.session.query(func.avg(Data.height_)))
            average_height = round(average_height, 2)

            count = db.session.query(Data.height_).count()
            send_email(email, height , average_height , count)


            return render_template("success.html")

        return render_template("index.html", text='Seems like we already have your mail')


if __name__=='__main__':
    app.debug = True
    app.run()