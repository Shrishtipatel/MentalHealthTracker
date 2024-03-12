import numpy as np
import flask
from flask import Flask,request,jsonify,render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

app=Flask(__name__)

#import Random Forest Classifier model 
app.config['SECRET_KEY']='projectisrunning'
RF_model=pickle.load(open('RF_model.pkl','rb'))

#route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        # Name=object(request.form.get('Name'))
        Gender=object(request.form.get('Gender'))
        if Gender=='Male':
            Gender=1
        else:
            Gender=0
        Age=float(request.form.get('Age'))
        Course=object(request.form.get('Course'))
        if Course=='Engineering':
            Course=0
        elif Course=='Islamic Education':
            Course=1
        elif Course=='Computer Science Engineering':
            Course=2
        elif Course=='Law':
            Course=3
        elif Course=='Mathemathics':
            Course=4
        elif Course=='Pendidikan Islam':
            Course=5
        elif Course=='BCS':
            Course=6
        elif Course=='Human Resources':
            Course=7
        elif Course=='Irkhs':
            Course=8
        elif Course=='Psychology':
            Course=9
        elif Course=='KENMS':
            Course=10
        elif Course=='Accounting':
            Course=11
        elif Course=='ENM':
            Course=12
        elif Course=='Marine science':
            Course=13
        elif Course=='KOE':
            Course=14
        elif Course=='Banking Studies':
            Course=15
        elif Course=='Business Administration':
            Course=16
            
        elif Course=='Usuluddin':
            Course=17
        elif Course=='TAASL':
            Course=18
        elif Course=='ALA':
            Course=19
        elif Course=='Biomedical science':
            Course=20
        elif Course=='Koe':
            Course=21
        elif Course=='BENL':
            Course=22
        elif Course=='CTS':
            Course=23
        elif Course=='Econs':
            Course=24
        elif Course=='MHSC':
            Course=25
        elif Course=='Malcom':
            Course=26
        elif Course=='Kop':
            Course=27
        elif Course=='Human Sciences':
            Course=28
        elif Course=='Biotechnology':
            Course=29
        elif Course=='Communication':
            Course=30
        elif Course=='Diploma Nursing':
            Course=31
        elif Course=='Radiography':
            Course=32
        
        elif Course=='Fiqh':
            Course=33
        elif Course=='DIPLOMA TESL':
            Course=34
        else:
            Course=35
        
        
        Year=int(request.form.get('Year'))
        CGPA=object(request.form.get('CGPA'))
        if CGPA=='3.00 - 3.49':
            CGPA=3
        elif CGPA=='3.50 - 4.00':
            CGPA=4
        elif CGPA=='2.50 - 2.99':
            CGPA=2
        elif CGPA=='2.00 - 2.49':
            CGPA=1
        else:
            CGPA=0
        Marital_status=object(request.form.get('Marital_status'))
        if Marital_status=='Yes':
            Marital_status=1
        else:
            Marital_status=0
        Depression=object(request.form.get('Depression'))
        if Depression=='Yes':
            Depression=1
        else:
            Depression=0
        Anxiety=object(request.form.get('Anxiety'))
        if Anxiety=='Yes':
            Anxiety=1
        else:
            Anxiety=0
        Panic_Attack=object(request.form.get('Panic_Attack'))
        if Panic_Attack=='Yes':
            Panic_Attack=1
        else:
            Panic_Attack=0
        
        new_data=[[Gender,Age,Course,Year,Marital_status,Depression,Anxiety,Panic_Attack]]
        result=RF_model.predict(new_data)
        
        return render_template('templates/question.html',result=result[0])
        
    else:
        return render_template('templates/question.html')
    


if __name__=="__main__":
    app.run(port=8000,debug=True)