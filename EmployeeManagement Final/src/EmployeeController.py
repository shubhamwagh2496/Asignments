import EmployeeModel
from flask import *
from flask_sqlalchemy import *
from crypt import methods
from EmployeeService import *

app=Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))        #To get current path of project folder
database_file = "sqlite:///{}".format(os.path.join(project_dir,"NewEmployeedatabase1.db")) 

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db=SQLAlchemy(app)


es=EmployeeService()
@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/addemployee",methods=['GET','POST'])
def addEmpc():
    if request.form:
        print("in form")
        empid=request.form.get("empid")
        empname=request.form.get("empname")
        empsal=request.form.get("empsal")
        emploginid=request.form.get("emploginid")
        emppassword=request.form.get("emppassword")
        es.addEmp(empid,empname,empsal,emploginid,emppassword)
       
@app.route("/displayemployee",methods=['POST','GET'])
def displayEmp():
    return es.displayEmp()

@app.route("/adminlogin",methods=['GET','POST'])
def adminLogin():
    if request.form:
        adminid=request.form.get("adminid")
        adminpass=request.form.get("adminpass")
    return es.adminLogin(adminid,adminpass)
    
@app.route("/employeelogin",methods=['GET','POST'])
def empLogin():
    if request.form:
        empid=request.form.get("empid")
        emppass=request.form.get("emppass")
    return es.empLogin(empid,emppass)
    
@app.route("/searchemployee",methods=['POST'])
def searchEmp():
    if request.form:
        sid=request.form.get("empid")
    return es.searchEmp(sid)
    
    
@app.route("/updateemployee",methods=['POST'])
def updateEmp():
    if request.form:
        sid=request.form.get("empid")
        newempname=request.form.get("empname") 
        newempsal=request.form.get("empsal") 
    return es.updateEmp(sid,newempname,newempsal)
    
    
@app.route("/deleteemployee",methods=['POST','GET'])
def deleteemp():
    if request.form:
        sid=request.form.get("empid")
    return es.deleteEmp(sid)
    
    
app.run(debug=True)