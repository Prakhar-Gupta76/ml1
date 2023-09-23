import streamlit as st
import pickle

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict_gpa(sat_score,attendance):
        sat_score=int(sat_score)
        attendance =int(attendance)
        prediction = model.predict([[1, sat_score, attendance]])
        return float(prediction)

def main():
     st.title('GPA Predictor')
     html_temp="""
     <div style="text-align:center;">
        <h1>Welcome to our Website!</h1>
        <p>Get to know your GPA score with just your SAT score and class attendance</p>
        <p>Enter 1 if attendance(in %) is 75 or greater else Enter 0.</p>
    </div>
    """
     st.markdown(html_temp)
    sat_score=st.text_input("sat_score","Type here")
    attendance=st.text_input("attendance","Type here")
    if st.button('Predict'):
     output=predict_gpa(sat_score,attendance)
     st.success(f'Predicted GPA is: {output}')

 
if __name__=='__main__':
    main()