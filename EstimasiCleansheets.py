import pickle
import streamlit as st

model = pickle.load(open('estimasi_cleansheets.sav', 'rb'))

st.title('Estimasi Jumlah Cleansheet Goalkeeper')
st.write('---')

match_played = st.number_input('Input Total Bermain')
conceded = st.number_input('Input Total Kebobolan')
saved_penalties = st.number_input('Input Total Penyelamatan Penalti')
saved = st.number_input('Input Total Penyelamatan')
punchesmade = st.number_input('Input Total Penyelamatan Melalui Pukulan')

predict = ''

if st.button('Estimasi Cleansheets'):
    predict = model.predict(
        [[match_played,conceded,saved_penalties,saved,punchesmade]]
    )
    st.write ('Estimasi jumlah Cleansheet adalah : ', predict)