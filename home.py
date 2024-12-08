import streamlit as st
from PIL import Image 


def home_page():

    image = Image.open(r"C:\Users\Akinremi Timothy\Desktop\NEST 360 Phase 2\Teleco Churn.png")
    st.image(image)
    
    st.title("Embedded a ML model in GUI's -- Using Streamlit")

    st.markdown("""This uses machine learning for classification of customer churning""")
    st.subheader("Instructions")

    st.markdown("""
                - Upload a csv file
                - Select the features for classification
                - Choose a machine learning model from the dropdown
                - Click on 'classify' to get the predicted results
                - The app gives you a report on the performance of the model
                - Expect it to give matrics like F1 score,recall, precision and accuracy
                """)
    st.header("App Features")
    st.markdown("""
                - **Data View**: Access the customer data.
                - **Predict view**: Shows the various models and predictions
                - **Dashboard**: Shows data visualization for insights
                """)
    st.subheader("User Benefits")
    st.markdown("""
                - **Data Driven Decision**: You make an informed decision backed by data
                - **Access Machine Learning**: Utilize machine learning algorithms.
                """)
    st.write("#### How to Run an application")
    with st.container(border=True): 
        st.code("""
                # Activate the virtual environment
                env/scripts/activate

                # Run the App
                streamlit run app.py
                """)
    # adding the embeded link
    st.video("https://www.youtube.com/watch?v=IOdW3jompYw",autoplay=True)

    
    # install pillow -- from PIL import Image

    st.divider()

    st.write("=====" * 20)
    
    st.write("Need help?")
    st.write("Contact me on:    [LinkedIn](https://www.linkedin.com/in/timothyakinremi/)")
    


if __name__ == "__main__":
    home_page()