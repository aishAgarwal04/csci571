
# A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'

from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('hw.html')

@app.route('/', methods=['POST'])
def index():
    # model = pickle.load(open('model.pkl','rb'))
    # data1 = age+weight
    clf = joblib.load("/home/Aish04/mysite/templates/regr.pkl")
    age = request.form['age']
    weight = request.form['weight']
    # age = 40
    # weight = 60
    x = pd.DataFrame([[age, weight]], columns=["Age", "Weight"])
    prediction = clf.predict(x)[0]
    # prediction = request.form['age'] + request.form['weight']
    return render_template('hw.html', data=prediction)

# if __name__ == '__main__':
#   app.run()