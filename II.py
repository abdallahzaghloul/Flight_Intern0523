import numpy as np #1
import pandas as pd #2
import pickle as pk
import streamlit as st

from category_encoders import BinaryEncoder #23
from sklearn.metrics import r2_score

from sklearn.ensemble import RandomForestRegressor


st.markdown(" <center>  <h1> Predicting Flight Prices </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)


AIRLINE=st.selectbox("AirLine" ,['IndiGo', 'Air India' ,'Jet Airways' ,'SpiceJet' ,'Multiple carriers' ,'GoAir','Vistara' ,'Air Asia', 'Vistara Premium economy', 'Jet Airways Business','Multiple carriers Premium economy', 'Trujet'] )

SOURCE=st.selectbox("Source Country",['Banglore' ,'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])

DESTINATION=st.selectbox("DESTINATION Country",['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi' ,'Hyderabad'])

ADDITIONAL_INFO=st.selectbox("ADDITIONAL_INFO",['No Info', 'In-flight meal not included','No check-in baggage included', '1 Short layover','1 Long layover', 'Change airports', 'Business class','Red-eye flight', '2 Long layover'])




MONTH=st.slider("Month Number" , min_value=1, max_value=12, value=0, step=1)
DAY=st.slider("Day Number" , min_value=1, max_value=31, value=0, step=1)
YEAR=st.slider("Year Number" , min_value=2019, max_value=2022, value=0, step=1)

DEP_HR = st.slider("Departure Hour" , min_value=0, max_value=24, value=0, step=1)
DEP_Min = st.slider("Departure Minute" , min_value=0, max_value=60, value=0, step=1)

ARRIVAL_HR=st.slider("Arrival Hour" , min_value=0, max_value=24, value=0, step=1)
ARRIVAL_MIN=st.slider("Arrival Minute" , min_value=0, max_value=60, value=0, step=1)

DURATION_HR=st.slider("Duration Hours" , min_value=0, max_value=30, value=0, step=1)


#def prediction(AIRLINE, SOURCE, DESTINATION, TOTAL_STOPS, ADDITIONAL_INFO, MONTH, DAY, YEAR, DEP_HR, DEP_Min, ARRIVAL_HR,ARRIVAL_MIN, DURATION_HR):
test_df = pd.DataFrame(columns=Inputs)
test_df.at[0,"AIRLINE"] = AIRLINE
test_df.at[0,"SOURCE"] = SOURCE
test_df.at[0,"DESTINATION"] = DESTINATION

test_df.at[0,"TOTAL_STOPS"] = TOTAL_STOPS
test_df.at[0,"ADDITIONAL_INFO"] = ADDITIONAL_INFO
test_df.at[0,"MONTH"] = MONTH
test_df.at[0,"DAY"] = DAY
test_df.at[0,"YEAR"] = YEAR
test_df.at[0,"DEP_HR"] = DEP_HR
test_df.at[0,"DEP_Min"] = DEP_Min
test_df.at[0,"ARRIVAL_HR"] = ARRIVAL_HR
test_df.at[0,"ARRIVAL_MIN"] = ARRIVAL_MIN
test_df.at[0,"DURATION_HR"] = DURATION_HR

RF_Model = 'Random_Forrest_Model.pkl'
encoder_filename = 'Flight_Prices_Encoder.pkl'

Model = pickle.load(open(RF_Model, 'rb'))
BE = pickle.load(open(encoder_filename, 'rb'))
    
st.dataframe(test_df)

if st.button("predict"):
        result = Model.predict(test_df)[0]
        st.text(f"The Price will {result}")
        
#st.write(result)






