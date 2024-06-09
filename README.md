# CSV Data Visualization Web Application Backend API

This repository contains the code for a simple Flask RESTful API backend used in a web application for visualizing CSV data. The backend interacts with a SQLite database to perform CRUD operations on the data.
> Used this Frontend: [CSV Data Visualization Web Application](https://github.com/Rakibul73/csv-data-visualization)

## Features

- **Data Management**: Provides endpoints for fetching, adding, updating, and deleting telecommunications data.
- **Pagination**: Supports pagination of data to efficiently handle large datasets.
- **Serialization**: Converts database objects to JSON format for communication with the frontend.

## Technologies Used

- **Python**:
  - Flask: Web framework for building RESTful APIs
  - SQLAlchemy: ORM library for database interaction
  - Flask-CORS: Extension for handling Cross-Origin Resource Sharing (CORS)

- **Database**:
  - SQLite: Lightweight and portable SQL database engine

## Endpoints

1. **GET /data_without_pagination**: Retrieves all telecommunications data without pagination.
2. **POST /data_without_pagination**: Adds new telecommunications data to the database.
3. **GET /data**: Retrieves paginated telecommunications data.
4. **POST /data**: Adds new paginated telecommunications data to the database.
5. **PUT /data/{id}**: Updates existing telecommunications data based on the provided ID.
6. **DELETE /data/{id}**: Deletes existing telecommunications data based on the provided ID.

## Setup

1. Clone the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask application by executing:
    ```bash
    python app.py
    ```
5. The backend API will be accessible at `http://localhost:5000`.

## Challenges Faced

1. **ORM Integration**: Integrating SQLAlchemy with Flask and understanding how to define database models and perform CRUD operations using ORM concepts.
2. **Pagination**: Implementing pagination logic to efficiently handle large datasets and optimizing queries for performance.
3. **Error Handling**: Handling errors and exceptions gracefully, ensuring proper error responses are sent to the client in case of failures.
4. **CORS Configuration**: Configuring CORS to allow requests from the frontend hosted on a different domain, enabling cross-origin communication.

## Lessons Learned

- **RESTful API Development**: Gained experience in building RESTful APIs using Flask, including handling different HTTP methods, request parsing, and response formatting.
- **Database Interaction**: Learned how to interact with a SQLite database using SQLAlchemy ORM, including querying, inserting, updating, and deleting data.
- **Pagination Techniques**: Explored various pagination techniques to efficiently retrieve and display data, improving the user experience for handling large datasets.
