import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(
    page_title="Sandip Shaw",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


with st.sidebar:
    st.image("sandip.jpeg")
    st.title("Sandip Shaw")
    selected = option_menu(menu_title=None,
                           options=["About Me","Projects"])
if selected == "About Me":
    st.subheader("Summary")
    st.write("Versatile Data Scientist with 1.5 years of experience, equally adept in machine learning, deep learning, data analysis, and computer vision. Proficient in developing robust models for complex problem-solving, utilizing cutting-edge techniques. Skilled in transforming data into actionable insights, and leveraging computer vision to extract meaning from visual data. A dedicated learner, continuously expanding skills to stay at the forefront of technological advancements. A collaborative team player passionate about making meaningful contributions to diverse projects.")

    st.subheader("Skills")
    columns = st.columns(5)
    columns[0].button('Machine Learning')
    columns[1].button('Deep Learning')
    columns[2].button('NLP')
    columns[3].button('Data Analysis')
    columns[4].button('Python')
    columns = st.columns(5)
    columns[0].button('Tableau')
    columns[1].button('MS-EXCEL')
    columns[2].button('Computer Vision')
    columns[3].button('YOLO')
    columns[4].button('SQL')


if selected == "Projects":
    st.subheader("My Projects")

    with st.expander("MOVIE RECOMMENDER SYSTEM"):
        if st.button("Link to the app"):
            st.markdown(f'<a href="{"https://iizsandu-movie-recomendation-system-app-8hfd2d.streamlit.app/"}" target="_blank">Click here</a>', unsafe_allow_html=True)

        st.write("Click on the link above and you will be redirected to page like this")
        img = Image.open("pic.png")
        imag = img.resize((1000,300))
        st.image(imag)

    with st.expander("APPLE DETECTION - YOLO"):
        if st.button("Click here"):
            st.markdown(f'<a href="{"https://apple-detection-using-yolo-jtputdt38fmw7zsjxgwwgx.streamlit.app/"}" target="_blank">Click here</a>', unsafe_allow_html=True)

        st.write("Click on the link above and you will be redirected to page like this")
        img = Image.open("apple.png")
        imag = img.resize((800,300))
        st.image(imag)

    with st.expander("DIABETES PREDICTION"):
        if st.button("Click here to open the app"):
            st.markdown(f'<a href="{"https://iizsandu-diabetes-main-ai5hh0.streamlit.app/"}" target="_blank">Click here</a>', unsafe_allow_html=True)

        st.write("Click on the link above and you will be redirected to page like this")
        img = Image.open("diabetes.png")
        imag = img.resize((628,350))
        st.image(imag)

