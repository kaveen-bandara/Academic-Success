ReadMe*

This application provides a simple interface for predicting the academic success of a student based on input features. The prediction model is exported and imported using the Python pickle library.

Files Included:

01. server.py: This file contains the Flask application code or the backend. It includes routes for the home page and prediction endpoint.
02. model.pkl: This is the trained machine learning model serialized using pickle. It is loaded into memory when the Flask app starts.
03. application.html: This HTML file is used for rendering the home page of the Flask application or in other words the frontend. It contains a form for user input, where here it strictly takes .csv files. Three CSV files have been included for testing.
04. Dockerfile: Contains the requirements for the Docker container.
05. requirements.txt: This file lists all the dependencies required to run the Flask application. You can install them using pip install -r requirements.txt.

Instructions manual:

01. Setting up Environment:

* Ensure you have Python installed on your system.
* Install the required dependencies by running: "pip install -r requirements.txt"
* Make sure you have Docker or any other app that handle containers.

02. Running the API:

* Execute the following command in your terminal: "docker build -t academic_model ."
* Then execute this command next: "docker run --name container_ML -p 8000:8000 academic_model"
* This will start the Flask development server, and you can access the application in your web browser at 'http://127.0.0.1:8000/'


03. Using the Application:

* Upon accessing the home page, you will see a form where you can input the CSV file relevant to predicting the academic success of a student.
* Once the CSV file is chosen submit the form by pressing "Submit".
* The application will process the input data, make a prediction using the trained model, and display the prediction.
