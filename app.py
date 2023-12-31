import streamlit as st

st.title('Welcome to the Streamlit!✨')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a text')
st.markdown('This is a markdown')
st.info('This is a info')
st.warning('This is a warning')
st.error('This is a error')
st.exception('This is a exception')
# st.help('This is a help')


st.sidebar.title('Welcome to the Sidebar!✨')
st.sidebar.header('This is a header in sidebar')
st.sidebar.subheader('This is a subheader in sidebar')
st.sidebar.text('This is a text in sidebar')
st.sidebar.markdown('This is a markdown in sidebar')
st.sidebar.info('This is a info in sidebar')
st.sidebar.warning('This is a warning in sidebar')
st.sidebar.error('This is a error in sidebar')
st.sidebar.exception('This is a exception in sidebar')
# st.sidebar.help('This is a help in sidebar')
st.sidebar.radio('Choose:',[1,2])