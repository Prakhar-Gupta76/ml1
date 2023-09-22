from flask import Flask, render_template,request
import pickle

app = Flask(__name__, template_folder='template', static_folder='static')

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        sat_score = float(request.form['sat_score'])
        attendance = float(request.form['attendance'])
        prediction = model.predict([1, sat_score, attendance])
        return render_template('index.html', prediction=prediction[0])

    return render_template('index.html')
 
if __name__=='__main__':
    app.run(debug = True)