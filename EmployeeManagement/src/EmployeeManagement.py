from flask import *
from flask_sqlalchemy import *
from crypt import methods


app=Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))        #To get current path of project folder
database_file = "sqlite:///{}".format(os.path.join(project_dir,"NewEmployeedatabase.db")) 

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db=SQLAlchemy(app)

class Employee(db.Model):
    empid=db.Column(db.String(23), unique=True, nullable=False, primary_key=True)
    empname = db.Column(db.String(80))
    empsal=db.Column(db.String(20))
    def __init__(self,empid,empname,empsal):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/addemployee",methods=['GET','POST'])
def addEmp():
    emp=None
    if request.form:
        empid=request.form.get("empid")
        name=request.form.get("empname")
        sal=request.form.get("empsal")
        emp=Employee(empid,name,sal)
        db.session.add(emp)
        db.session.commit()
    print("hello in add")  
    print(emp.empid,emp.empname,emp.empsal)
    emp1=Employee.query.all()
    for e in emp1:
        print(e.empid,e.empname,e.empsal)
    return render_template("DiplayEmployees.html",emp=emp1)
    
@app.route("/searchemployee",methods=['POST'])
def searchEmp():
    if request.form:
        sid=request.form.get("empid")
    emp=Employee.query.filter_by(empid=sid).first()
    print(emp)
    return ""
@app.route("/updateemployee",methods=['POST'])
def updateEmp():
    if request.form:
        sid=request.form.get("empid")
        newempname=request.form.get("empname") 
        newempsal=request.form.get("empsal") 
    emp1 =Employee.query.filter_by(empid=sid).first()
    emp1.empname=newempname
    emp1.empsal=newempsal
    db.session.commit()
    return render_template("AdminHome.html",msg="employee updated")
    

@app.route("/deleteemployee",methods=['POST','GET'])
def deleteemp():
    if request.form:
        sid=request.form.get("empid")
    emp =Employee.query.filter_by(empid=sid).first()
    db.session.delete(emp)
    db.session.commit()
    return "Employee deleted"

def displayEmp():
    emp=Employee.query.all()
    return render_template("DiplayEmployees.html")

    

@app.route("/adminlogin",methods=['GET','POST'])
def adminLogin():
    if request.form:
        adminid=request.form.get("adminid")
        adminpass=request.form.get("adminpass")
    print("hello in admin")
    print(adminid,adminpass)
    if(adminid=='shubham' and adminpass=='1234'):
        return render_template("AdminHome.html")
         
    else:
        return "Invalid id password"

db.create_all()  
app.run(debug=True)