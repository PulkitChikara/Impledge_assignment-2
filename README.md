# Impledge_assignment-2

These are the 3 tasks given and their respective files.

# 1)Automated Test Cases Execution using Selenium WebDriver

# Overview:
This project automates the execution of two test cases on the KloudShip application using Selenium WebDriver in Python. The test cases include adding a package (Test Case 01) and deleting a package (Test Case 02). The goal is to verify the functionality of adding and deleting packages on the KloudShip platform.

# Design Decisions and Approach:
Selenium WebDriver: Selenium WebDriver is chosen for its compatibility with web browsers and its ability to automate web interactions.<br/>
Python: Python is selected as the programming language due to its simplicity, readability, and extensive support for Selenium WebDriver.</br>
Test Case Structure: Each test case is encapsulated within its function to promote modularity and readability.</br>
Error Handling: Exception handling is implemented to catch and print any errors that occur during test execution, providing visibility into potential issues.</br>

# Setup
Setup Python Environment: Ensure Python is installed on your system.</br>
Install Selenium: Use pip to install the Selenium package (pip install selenium).</br>
WebDriver Installation: Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome) and ensure it is added to your system's PATH.</br>
Clone Repository: Clone or download the repository containing the automation code.</br>
Update Credentials: Replace the provided email and password with your KloudShip test account credentials in the Python script.</br>
Execute Code: Run the Python script (automated_tests.py) using a Python interpreter (e.g., python automated_tests.py).</br>
View Results: Check the console output for any error messages and verify the test results by logging into the KloudShip application.</br>
This automation project streamlines the execution of test cases, enhancing efficiency and reliability in validating the KloudShip platform's package management functionality.</br>

# 2)Automated API Testing using Postman
This project automates API testing using Postman for the EasyPost API. The exercises include fixing failing test cases, adding a new request to fetch shipment details, and adding test cases to verify specific responses. The goal is to ensure the accuracy and reliability of the EasyPost API.

# Steps to Execute:

Download and Install Postman: Download and install the Postman application from the official website (https://www.postman.com/downloads/).</br>
Import Collection: Import the provided Postman collection file (Impledge_QA_Exercise.postman_collection.json) into Postman.</br>
Rename Collection: Rename the imported collection from Impledge_QA_Exercise to Impledge_QA_YourFullName by editing the collection settings in Postman.</br>
Fix Failing Test Cases (POSTMAN Test 01): Review the failing test cases in the imported collection and make necessary corrections according to the EasyPost API documentation (https://www.easypost.com/docs/api).</br>
Add New Request (POSTMAN Test 02): Add a new request to the collection to fetch details of the shipment with ID shp_e0b570fd1d7d4b62bd206917eae5881a. Use the appropriate endpoint and parameters based on the EasyPost API documentation.</br>
Add Test Cases (POSTMAN Test 03): For the newly added request in step 5, add test cases to verify the following:</br>
Ensure that the value of selected_rate.retail_rate is equal to 12.</br>
Confirm that retail_rate is greater than list_rate.</br>
Execute Collection: Execute the modified collection in Postman to run the test cases against the EasyPost API.</br>
Review Results: Review the test results in the Postman Runner to validate the API responses and ensure that all test cases pass successfully.</br>
This automation project streamlines API testing for the EasyPost API, ensuring its functionality and reliability. By leveraging Postman's capabilities, testers can efficiently execute and validate API endpoints, enhancing the overall quality of the EasyPost API integration.</br>

# 3)SQL Practice on SQL-Practice.com

Overview:
This project automates SQL queries execution and practice on the SQL-Practice.com website. It aims to enhance SQL skills by performing various queries related to patient, doctor, and admission tables. The tasks include navigating to the website, understanding table relationships, executing UPDATE queries, and solving specific problems using SQL SELECT queries.

# Steps to Execute:

Open Chrome Browser: Launch the Google Chrome web browser on your computer.</br>
Navigate to SQL-Practice.com: Enter the URL https://www.sql-practice.com/ in the address bar and press Enter to access the SQL-Practice.com website.</br>
View Schema: Click on "SQL Database" on the left-hand side of the page, and then click on "View Schema" to understand the relationship between the patients, doctors, and admissions tables.</br>
Execute UPDATE Queries: Before preparing SELECT queries, execute the given UPDATE queries to update the admissions table:</br>
Update [Admissions] Set attending_doctor_id = 29 where attending_doctor_id = 3;</br>
Update [Admissions] Set patient_id = 4 where patient_id = 35;</br>
Execute SELECT Queries: Execute the SELECT queries along with the UPDATE queries to ensure proper data manipulation and retrieval.</br>
SQL Test 1: Problem Solving:
Problem 1: SELECT the details of doctor(s) who have admissions.</br>
Problem 2: SELECT the details of doctor(s) for whom there are no admissions.</br>
Problem 3: SELECT the details of patient(s) whose admission can't be completed due to missing doctor details.</br>
Ensure to execute the SELECT queries after executing the UPDATE queries to reflect the changes made to the database.</br>

These are the steps to complete the 3 tasks.
Thankyou :)


