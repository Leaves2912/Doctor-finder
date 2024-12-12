# Importing the necessary libraries
import re
import time
import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.parse import unquote

# Creating the user-defined function for scrapping the details
def scrape_html(url):

    # Display a spinner while searching for doctors
    with st.spinner("Searching for doctors..."):

        # Setting headers to avoid getting blocked by the website's server
        headers = {"User-agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        response = requests.get(url, headers=headers)
        page = 1
        doctors = []
    
        # Creating a loop to load the data
        while True:
            full_url = f'{url}&page={page}'  
            response = requests.get(full_url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Finding doctor names and profile sections on the current page
            doctor_name = soup.find_all('h2', class_='doctor-name')
            profile_tag = soup.find_all("div", class_='info-section')
            
            # Stopping condition to break the loop
            if not doctor_name:
                break
            
            else:
                for i, j in zip(doctor_name, profile_tag):

                    # Extracting doctor names
                    name = i.get_text(strip=True)

                    # Extracting profile link
                    profile_link = j.find('a', href=True)  
                    if profile_link:
                        href = profile_link['href']
                        link = 'www.practo.com' + href
                    else:
                        link = 'Link not available.'
                    doctors.append([name, link])  # Adding doctor name and link to the list
            page += 1
        
        # If no doctors are found, return None
        if not doctors:
            return None
        return doctors


# App title
st.markdown('<div class="title-text">Web Scraping with Streamlit Application</div>', unsafe_allow_html=True)

# Custom CSS for styling the sidebar and labels
st.sidebar.markdown(
    """
    <style>
    .title-text {
        font-family: 'Times New Roman', Times, serif;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .sidebar-header, .input-label, .message-text, .stTextInput, .stSelectbox, .stButton button {
        font-family: 'Times New Roman', Times, serif;
    }
    .sidebar-header {
        font-size: 30px;
        font-weight: bold;
        color: white;
        margin-bottom: 30px;
    }
    .input-label {
        font-size: 20px;
        color: white;
        margin-bottom: -15px;
        padding-bottom: 0px;
    }
    .stTextInput, .stSelectbox {
        margin-top: -20px; /* Reduces space between the input field and the label */
    }
    .message-text {
        font-size: 22px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar input fields
st.sidebar.markdown('<div class="sidebar-header">Please enter the details</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="input-label">Enter the city name</div>', unsafe_allow_html=True)
location = st.sidebar.text_input('', placeholder='e.g Delhi')  # Text input for city name
st.sidebar.markdown('<div class="input-label">Select the specialization</div>', unsafe_allow_html=True)
s = ['', 'Cardiologist', 'Dentist', 'Dermatologist', 'Orthopedic', 'Gynecologist', 'Pediatrician', 'Radiologist', 'Urologist', 'Psychiatrist', 'General Physician', 'Ayurveda', 'Ear-nose-throat (ENT) Specialist', 'Neurologist', 'Homeopath']
specialization = st.sidebar.selectbox('', s)

# Message box for app instructions
message = st.empty()
message.markdown(
    """
    <div class="message-text">
    This app allows you to find the number of available doctors according to your selected city and specialization. Please enter the details in the sidebar and press 'Find doctors' button to find the details.
    </div>
    """,
    unsafe_allow_html=True
)

if st.sidebar.button('Find doctors 🔍'):
    if location and specialization:
        try:
            message.empty() 
            # Constructing the custom URL
            url = f"https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22{specialization}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city={location}"
            u_url = unquote(url) 

            doctors = scrape_html(u_url)  # Call the scraping function
            
            # Display the output
            if doctors is None:
                st.markdown(f'### No doctors found for specialization "{specialization}" in "{location}".')
            elif doctors:
                st.markdown(f"### There are {len(doctors)} {specialization}s available in {location}.")
                st.subheader('Explore the profiles of these doctors by clicking on the links below.')
                doctors_df = pd.DataFrame(doctors, columns=['Doctor Name', 'Profile Link'])
                doctors_df.index = doctors_df.index + 1  
                
                # Coverting URLs to clickable profile links
                for i, (index, row) in enumerate(doctors_df.iterrows()):
                    st.write(f"{i+1}. {row['Doctor Name']}")
                    url = row['Profile Link']
                    if url.startswith('www.'):
                        q_url = quote(url, safe=":/?=&")
                        new_url = f"http://{q_url}"
                        link = f"[{new_url}]({new_url})"
                        st.markdown(link)
                    else:
                        st.write('Link not available.')
                    st.write("---")  # Separator between entries
        except Exception as e:
            st.write('Error occurred while scraping:', e)  
    else:
        st.write('Please enter both location and specialization.')

footer = """
    <style>
    .footer {
        position: fixed;
        right: 10px;
        bottom: 10px;
        font-family: 'Times New Roman', Times, serif;
        font-size: 18px;
        color: #ffffff;
    }
    </style>
    <div class="footer">
    Created by Tarun Madhwani
    </div>
    """

# Inject the footer into the app
st.markdown(footer, unsafe_allow_html=True)