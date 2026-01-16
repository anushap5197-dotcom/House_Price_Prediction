#connect the model with the app
import pickle
import streamlit as st
import pandas as pd

#setup
st.set_page_config(page_icon="image.jpg",page_title="HOUSE PRICE PREDICTION",layout="wide")

#load RF model

with open("RF_model.pkl",'rb') as file:
    model=pickle.load(file)

# model.predict(input)

# load the dataset
df=pd.read_csv("cleaned_df.csv")

coll1,coll2,coll3=st.columns([1,2,1])
with coll2:
    st.header("HOUSE PRICE PREDICTION")

co1,co2,co3=st.columns([1.3,2,1])
with co2:
    st.image("image.jpg",width=300)

with st.sidebar:
    st.title("HOUSE PRICE PREDICTION")
    st.image("image.jpg",width=300)


#get encoded location
def get_encoded_loc(location):
    for loc,encoded in zip(df["location"],df["encoded_loc"]):
        if location==loc:
            return encoded


st.write("    ") 
st.write("    ")   
st.write("    ")   

#input fields:  location,sqft,bath,bhk
with st.container(border=True):
    col1,col2=st.columns(2)
    with col1:
        location=st.selectbox("📌Location",options=df['location'].unique())
        st.write("    ")   
        sqft=st.number_input("📐Sq.ft:  ",min_value=300)
        st.write("    ")   

    with col2:
        bath=st.selectbox("🛁No. of baths: ",options=sorted(df['bath'].unique()))
        st.write("    ")   

        bhk=st.selectbox("🏡BHK's :",options=sorted(df['bhk'].unique()))
        st.write("    ")   
        st.write("    ")   


   
    
with st.container(border=True):
    encoded_loc=get_encoded_loc(location)
    c1,c2=st.columns([1,8])

    if c1.button("💰Predict",width=300):
        # model prediction
        inp_data=[[sqft,bath,bhk,encoded_loc]]
        pred=model.predict(inp_data)
        pred=float(f"{pred[0]:.2f}")
        st.write("    ")
        c2.title(f"Predicted Price: Rs.{pred*100000}")




