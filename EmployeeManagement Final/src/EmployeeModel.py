
from flask import *
from flask_sqlalchemy import *
from crypt import methods



app=Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))        #To get current path of project folder
database_file = "sqlite:///{}".format(os.path.join(project_dir,"NewEmployeedatabase1.db")) 

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db=SQLAlchemy(app)



class Employee(db.Model):
    empid=db.Column(db.String(23), unique=True, nullable=False, primary_key=True)
    empname = db.Column(db.String(80))
    empsal=db.Column(db.String(20))
    emploginid=db.Column(db.String(20))
    emppassword=db.Column(db.String(20))
    def __init__(self,empid,empname,empsal,emploginid,emppassword):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
        self.emploginid=emploginid
        self.emppassword=emppassword
db.create_all()         
        