from EmployeeModel import *
from flask_sqlalchemy import *
from crypt import methods
from flask import *


app=Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))        #To get current path of project folder
database_file = "sqlite:///{}".format(os.path.join(project_dir,"NewEmployeedatabase1.db")) 

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db=SQLAlchemy(app)

class EmployeeService:
    
    def addEmp(self,empid,empname,empsal,emploginid,emppassword):
        emp=Employee(empid,empname,empsal,emploginid,emppassword)
        db.session.add(emp)
        db.session.commit()
        return render_template("DiplayEmployees.html",emp=emp)
    
    def displayEmp(self):
        emp=Employee.query.all()
        return render_template("DiplayEmployees.html",emp=emp)
     
     
    def adminLogin(self,adminid,adminpassword):
        if(adminid=='shubham' and adminpassword=='1234'):
            return render_template("AdminHome.html")
        
        else:
            return render_template("home.html",adminlogininvalid="Invalid id password")
         
         
         
    def empLogin(self,empid,emppass):
        if (empid=='shubham' and emppass=='1234'):
            return render_template("EmployeeHome.html")
        
        else:
            return render_template("home.html",emplogininvalid="Invalid id password")
        
    def searchEmp(self,sid):  
        emp=Employee.query.filter_by(empid=sid).first()
  
        return render_template("AdminHome.html",searchmsg="Search found",emp1=emp)
    
    
    def updateEmp(self,sid,newempname,newempsal):
        emp1 =Employee.query.filter_by(empid=sid).first()
        emp1.empname=newempname
        emp1.empsal=newempsal
        db.session.commit()
        return render_template("AdminHome.html",updatemsg="employee updated")
    
    def deleteEmp(self,sid):
        emp =Employee.query.filter_by(empid=sid).first()
        db.session.delete(emp)
        db.session.commit()
        return render_template("AdminHome.html",deletemsg="employee deleted")
    
    
    