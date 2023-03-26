import streamlit as st
import requests
from backend.models import UserProfile, GenerateRequest
# Replace the URL with the address where your FastAPI server is running
API_URL = "https://osh-ai.onrender.com"
st.title(":robot_face: OSH.AI")
# st.set_page_config(page_title="OSH.AI", page_icon=":construction:")
st.header("Making OSHA Compliance Easy")
st.write(":wave: This is a demo of an OSHA compliance expert chatbot for small businesses.")
st.write(":brain: The chatbot is built with FastAPI and GPT-4.")
st.sidebar.title("User Profile")
​
state = st.sidebar.selectbox(
    "State",
    ('AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'))
business_type = st.sidebar.selectbox(
    "Business type",
    ("Restaurant", "Laundromat", "Clothing Store"))
​
# st.write('You selected:', option)
# state = st.sidebar.text_input("State")
# business_type = st.sidebar.text_input("Business type")
num_employees = st.sidebar.number_input("Number of employees", min_value=1)
user_profile = UserProfile(state=state, business_type=business_type, num_employees=num_employees)
# topic = st.text_input("Topic")
​
Area_of_Concern = st.sidebar.radio(
    "Area of Concern",
    ('Sanitation', 'Safety'))
​
option = ""
if st.sidebar.button("Help me"):
#     if user_profile == {
# "state": "OH",
# "business_type":  "Laundromat",
# "num_employees": 25}:
#         st.write(["How many restrooms do I need to provide?", "What are all the sanitation regulations I need to know about?",
# "What amenities do I need to provide in my restroom?"])
    if Area_of_Concern == "Sanitation":
        option = st.sidebar.selectbox(
        'Generated Questions',
         ("How many restrooms do I need to provide?", "What are all the sanitation regulations I need to know about?", "What amenities do I need to provide in my restroom?"))
    st.session_state.selected_option = option
    input_value = st.text_input("Question", st.session_state.selected_option)
    # Update the session state when the input changes
    if input_value != st.session_state.selected_option:
        st.session_state.selected_option = input_value
        input_value = st.text_input("Question", st.session_state.selected_option)
     # question = st.text(option)
        # question = st.text_input('Question', option)
# st.write("How many restrooms do I need to provide?")
        # st.write("What are all the sanitation regulations I need to know about?")
        # st.write("What amenities do I need to provide in my restroom?")
        # st.write("You are in Ohio and you own a laundromat with 25 employees. You need to know about sanitation.")
    elif Area_of_Concern == "Safety":
        option = st.sidebar.selectbox(
        'Generated Questions',
            ("Do I need to have an emergency plan?", "Under what circumstances do I need to do employee safety training?", "What are all the regulations required for employee safety?"))
        st.session_state.selected_option = option
        input_value = st.text_input("Question", st.session_state.selected_option)
        # Update the session state when the input changes
        if input_value != st.session_state.selected_option:
            st.session_state.selected_option = input_value # question = st.text(option)
            input_value = st.text_input("Question", st.session_state.selected_option)
        # question = st.text_input('Question', option)
​
        # st.write("Do I need to have an emergency plan?")
        # st.write("Under what circumstances do I need to do employee safety training?")
        # st.write("What are all the regulations required for employee safety?")
        # st.write("You are in Ohio and you own a laundromat with 25 employees. You need to know about safety.")   
        
​
    # question = st.text_input('Question', option)
    # selected_option = st.info(option)
    # selected_option = st.warning(option)
    # selected_option = st.success(option)
​
​
​
    if st.button("Submit"):
        generate_request = GenerateRequest(query=input_value, user_profile=user_profile, topic=topic)
        response = requests.post(f"{API_URL}/generate", json=generate_request.dict())
        answer = response.json()
        st.write(answer)
        st.info(answer, icon="ℹ️")
# ```
# Now, modify your `main.py` file to run the FastAPI app:
# ```python
# New
# 12:55
# HERE IS THE FEEDBACK FRON THE WORKING APP:
# 12:55
# To adapt the provided Streamlit application to work with your osh.ai repo, you can follow these steps:
# 1. Remove the unnecessary imports and code blocks that are not needed for your application.
# 2. Add the imports needed for your application, such as `UserProfile` and `GenerateRequest`.
# 3. Replace the existing user input fields and API calls with the ones needed for your application.
# Here's the modified code for your `app.py` file:
# ```python
​
​
# import streamlit as st
# import requests
# from backend.models import UserProfile, GenerateRequest
# # Replace the URL with the address where your FastAPI server is running
# API_URL = "http://localhost:8000"
# st.set_page_config(page_title="OSH.AI", page_icon=":construction:")
# st.header("OSH.AI")
# st.write(":wave: This is a demo of an OSHA compliance expert chatbot for small businesses.")
# st.write(":robot_face: The chatbot is built with FastAPI and GPT-4.")
# st.sidebar.title("User Profile")
# state = st.sidebar.text_input("State")
# business_type = st.sidebar.text_input("Business type")
# num_employees = st.sidebar.number_input("Number of employees", min_value=1)
# user_profile = UserProfile(state=state, business_profile=business_type, num_employees=num_employees)
# topic = st.text_input("Topic")
# query = st.text_input("Your question")
# if st.button("Submit"):
#     generate_request = GenerateRequest(query=query, user_profile=user_profile, topic=topic)
#     response = requests.post(f"{API_URL}/generate", json=generate_request.dict())
#     answer = response.json()
#     st.write(answer)
# if "generated" not in st.session_state:
#     st.session_state["generated"] = []
# if "past" not in st.session_state:
#     st.session_state["past"] = []
# user_input = query
# if user_input:
#     output = answer
#     st.session_state["past"].append(user_input)
#     st.session_state["generated"].append(output)
# if st.session_state["generated"]:
#     for i in range(len(st.session_state["generated"]) - 1, -1, -1):
#         message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
#         message(st.session_state["generated"][i], key=str(i))
# def refresh_chain():
#     st.session_state["generated"] = []
#     st
