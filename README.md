This file contains the required instructions for running the app successfully.

PROJECT TITLE - Web Scraping with Streamlit Application

PROJECT DESCRIPTION - 
This project is a Streamlit-based web application designed to scrape and display information about doctors available in a user-specified city and specialization. 
The application interacts with a medical website 'Practo.com', extracting data such as doctor names and profile links based on user inputs. 
The app interface allows users to enter a city name and select a specialization from a predefined list, making it easy to find relevant medical professionals in the desired location.

INSTALLATION INSTRUCTIONS -

Step - 1 : Clone the repository:
           git clone https://github.com/Leaves2912/PaidIntern-Data-Science-Project.git
           cd PaidIntern-Data-Science-Project
          
Step - 2 : Create a virtual environment (optional but recommended):
           python -m venv env
           source env/bin/activate  # On Windows use `env\Scripts\activate`

Step - 3 : Install the required packages:
          pip install -r requirements.txt

Step - 4 : Run the application:
           streamlit run Qualification_project.py

USAGE INSRUCTIONS -

1. Input the details:
Enter the name of the city where you want to find doctors.
Select a medical specialization from the dropdown menu.

2. Find doctors:
Click the 'Find doctors 🔍' button to initiate the scraping process.
The application will display the number of available doctors along with their names and profile links.

3. Explore profiles:
Click on the provided links to view the profiles of the doctors directly on the Practo.com.

EXPECTED OUTPUT -

The application will return the total number of doctors found for the selected specialization in the specified city.
The output will include the doctors' names and clickable profile links, allowing users to explore their profiles in detail.
If no doctors are found, the application will notify the user accordingly.
