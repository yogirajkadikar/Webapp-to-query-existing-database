# Webapp-to-query-existing-database
getting-trending-hashtags-on-twitter

A web app to perform queries on existing database

#Usage

It is used for getting data from existing database for a keyword provided by user and displaying the result on webpage.

#Steps to copy excel sheet to database
  1. Convert excel sheet to CSV file
  2. Create a table with same headers as in CSV file
  3. Copy the CSV file to the table
     Command: COPY <table_name> FROM '/file-path/.csv' DELIMITER ',' CSV HEADER;

#development



    Need to install flask: $ pip install flask

    Need to install sql alchecmy: $ pip install FlaskSQLAlchemy

    Create a virtual environment: $ python3 -m venv virtual

    Run the code app.py in venv
