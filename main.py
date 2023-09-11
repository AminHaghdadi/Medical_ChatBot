import streamlit as st
from model import qa_bot



#Streamlit code
st.title('Medical ChatBot 👨🏼‍⚕️🏥')
st.sidebar.subheader(("This ChatBot reference is Gale Encyclopedia of Medicine book."),divider='rainbow')
st.sidebar.image('91GcaWaZrXL.jpg')
st.sidebar.subheader(("This ChatBot is powerd by llama2-7b 🦙"),divider='rainbow')

qu = st.text_area('ask your question here:')
button=st.button('Submit')
if button :
    response=qa_bot(qu)
    st.write(response['result'])
    source=response['source_documents'][0]
    st.caption('\nText and source are from:')
    st.write(source)
    