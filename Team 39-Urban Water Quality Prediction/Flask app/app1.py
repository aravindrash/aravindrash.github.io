from flask import Flask, request , render_template
import pickle

import numpy as np 

app = Flask(__name__)
model = pickle.load(open('wqi.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('page.html')

@app.route('/y_pred',methods=['POST'])
def y_pred():
    
    year =request.form['year']
    do=request.form['do']
    ph=request.form['ph']
    co =request.form['co']
    bod=request.form['bod']
    na=request.form['na']
    tc=request.form['tc'] 
    data=[[int(year),float(do),float(ph),float(co),float(bod),float(na),float(tc)]]
    prediction  = model.predict(data)
    print(prediction)
    output=prediction[0]
    if(output>=95 and output<=100):
        return render_template('page.html', prediction_text='Excellent The predicted WQI is:'+str(output))
    if(output>=85 and output<=94):
        return render_template('page.html', prediction_text='Good The predicted WQI is:'+str(output))
    if(output>=75 and output<=84):
        return render_template('page.html', prediction_text='Fair The predicted WQI is:'+str(output))
    if(output>=65 and output<=74):
        return render_template('page.html', prediction_text='Mariginal The predicted WQI is:'+str(output))
    if(output>=45 and output<=64):
        return render_template('page.html', prediction_text='Poor The predicted WQI is:'+str(output))
    else:
        return render_template('page.html', prediction_text='Not Fit for drinking The predicted WQI is:'+str(output))
if __name__ == "__main__":
    app.run(debug=True)
 