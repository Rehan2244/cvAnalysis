# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
import os
from flask import Flask,session
import PyPDF2
# from django.views.generic import TemplateView

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request,'login.html')

def signuptoLogin(request):
    username=request.GET['enteredUsername']
    pwd=request.GET['enteredPassword']
    emails=request.GET['enteredEmail']
    number=request.GET['enteredMobile']
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="test",
    )
    
    mycursor = conn.cursor()
    sql = "INSERT INTO userlogin (username,password,email,mobile_no) VALUES (%s, %s, %s, %s)"
    val = (username, pwd, emails, number)
    mycursor.execute(sql, val)
    conn.commit()
    return render(request,'login.html')

def signUp(request):
    return render(request,'usersignup.html')
    
def recLogin(request):
    return render(request,'recruiterloginpage.html')

def uploadResume(request):
    usernam=request.POST['userInfo']
    pwd=request.POST['pwInfo']
    sql = """select `id`,`username`,`password` from userlogin"""
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="test",
    )    
    mycursor = conn.cursor()
    mycursor.execute(sql)
    resultSet=mycursor.fetchall()
    print(resultSet)
    for row in resultSet:
        if(row[1]==usernam and row[2]==pwd):
            return render(request,"uploadfile.html")
            session['username']=usernam
            session['id']=row[0]
            print(session.values)
    else:
        return HttpResponse('<script>window.alert("Password or username is incorrect Try Again");window.location="login"</script>')


def thanksUploadResume(request):
    filepath=""
    conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="test",
        )
    selectsql="""select * from userlogin"""
    selectcursor=conn.cursor()
    selectcursor.execute(selectsql)
    selectSet=selectcursor.fetchall()
    if request.method=="POST":
        un=request.POST['username']
        file=request.FILES['fileupload']
        openFile=open(os.path.realpath(file.name),'rb')
# creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(openFile) 
# # printing number of pages in pdf file 
        print(pdfReader.numPages) 
# # creating a page object 
        pageObj = pdfReader.getPage(0) 
        words=[]
        word=""
        spaces=[]
# # extracting text from page 
        textinpdf=pageObj.extractText()
        for i in textinpdf:
            if i!=" ":
                word+=i
            elif i==" ":
                words.append(word)
                word=""
                spaces.append(i)
        print(words)
        mycursor = conn.cursor()
        for i in words:
            i=i.lstrip()
            i=i.rstrip()
            i=i.replace(",","")
            for row in selectSet:
                if i.upper =="JAVA":
                    sql = """UPDATE `userlogin` SET `JAVA`=true where `username`='{}' """ .format(un)
                    mycursor.execute(sql)
                    conn.commit()
                if i.upper() =="PYTHON" :
                    sql = """UPDATE `userlogin` SET `PYTHON`=true where `username`='{}' """ .format(un)
                    mycursor.execute(sql)
                    conn.commit()
                if i.upper() =="CSS" :
                    sql = """UPDATE `userlogin` SET `CSS`=true where `username`='{}' """ .format(un)
                    mycursor.execute(sql)
                    conn.commit()
                if i.upper() =="HTML" :
                    sql = """UPDATE `userlogin` SET `HTML`=true where `username`='{}' """ .format(un)
                    mycursor.execute(sql)
                    conn.commit()
                if i.upper() =="C" :
                    sql = """UPDATE `userlogin` SET `C`=true where `username`='{}' """ .format(un)
                    mycursor.execute(sql)
                    conn.commit()
                if i.upper() =="C++" :
                    sql = """UPDATE `userlogin` SET `C++`=true where `username`='{}' """ .format(un)
                    mycursor.execute(sql)
                    conn.commit()
                if i.upper() =="NODEJS" :
                    sql = """UPDATE `userlogin` SET `NODEJS`=true where `username`='{}' """ .format(un)
                    mycursor.execute(sql)
                    conn.commit()
                if i.upper() =="AJAX" :
                    sql = """UPDATE `userlogin` SET `AJAX`=true where `username`='{}' """ .format(un)
                    mycursor.execute(sql)
                    conn.commit()
                
# closing the pdf file object 
        openFile.close() 

        fileOpened=open(os.path.abspath(file.name),"rb").read()
        fileStringValue=str(fileOpened)
        fileStringValue=fileStringValue.lstrip('b')
        sql = """UPDATE `userlogin` SET `resume`={} WHERE `username`='{}'""".format(fileStringValue,un)  
        mycursor = conn.cursor()
        mycursor.execute(sql)
        conn.commit()
    return render(request,"login.html")

def listResume(request):
    usernam=request.POST['username'];
    found="";
    pwd=request.POST['password'];
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        db="test"
    )
    mycursor = conn.cursor()
    mycursor.execute("select * from recruiterlogin")
    found="";
    result=mycursor.fetchall()
    for i in result:
        print(i)
        if(usernam==i[1] and pwd==i[2]):
            found=usernam
            return render(request,'analysis.html',{"username":usernam,"found":""})
    else:
        return render(request,'recruiterloginpage.html',{"found":"Username or password is incorrect please try again"})

def filteredResult(request):
    percentage=0
    totalCount=0
    availableCount=0
    if request.method=="GET":
        selected=request.GET["menu"]
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="test"
    )
    sql="select * from userlogin"
    mycurs=conn.cursor()
    mycurs.execute(sql)
    recordCount=mycurs.fetchall()
    totalCount=len(recordCount)
    if selected!="1":
        selectSql="select username from userlogin where `{}`=true".format(selected)
        mycurs.execute(selectSql)
        selectSet=mycurs.fetchall()
        availableCount=len(selectSet)
        percentage=(len(selectSet)/len(recordCount))*100
        if len(selectSet)<1:
            nofoundmsg="No record Found"
            return render(request,"analysis.html",{"selectedValue":nofoundmsg,"found":False,"precent":percentage,"totalCount":totalCount,"foundCount":availableCount,"selected":selected})
        else:
            return render(request,"analysis.html",{"selectedValue":selectSet,"found":True,"precent":percentage,"totalCount":totalCount,"foundCount":availableCount,"selected":selected})
    else:
        nofoundmsg="Please Select Any Value"
        return render(request,"analysis.html",{"selectedValue":nofoundmsg,"found":False,"precent":percentage,"totalCount":totalCount,"foundCount":availableCount, "selected":selected})
    
    
