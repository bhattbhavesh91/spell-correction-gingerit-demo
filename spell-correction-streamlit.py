from gingerit.gingerit import GingerIt
import streamlit as st

st.title('Grammar & Spell Checker In Python')
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
parser = GingerIt()
if st.button('Correct Sentence'):
    if text == '':
        st.write('Please enter text for checking') 
    else: 
        result_dict = parser.parse(text)
        st.markdown('**Corrected Sentence - **' + str(result_dict["result"]))
else: pass