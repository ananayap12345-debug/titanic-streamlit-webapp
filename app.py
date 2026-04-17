import streamlit as st
st.title("Titanic Prediction System")
pclass=st.number_input("Enter the Passenger Class ",1,2)
gender=st.radio("select your gender:",["male","female"])
age=st.number_input("Enter your Age",0,100)
sibsp=st.number_input("Enter your sibsp",0,10)
parch=st.number_input("Enter your parch",0,5)
fare=st.number_input("Enter your fare",0,500)
embarked=st.radio("select your boarding station",["s","c","Q"])
user_input=[[pclass,gender,age,sibsp,parch,fare,embarked]]

# import joblib
# pipe = joblib.load("pipe1.pkl")
import pickle
f=open("pipe1.pkl","rb")
pipe=pickle.load(f)
if st.button("click to predict "):
    res=pipe.predict(user_input)
    st.write(res)
    if res==0:
        print("dead")
    else:
        st.balloons()    

