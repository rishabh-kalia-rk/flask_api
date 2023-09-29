#  **REST APIs with Flask and Python**
This is a Flask project that demonstrates the development of a RESTful API with authentication, database integration, and interactive documentation using Swagger UI.
# Project Overview
This Flask project serves as the foundation for building a robust RESTful API. It incorporates various libraries and frameworks, including Flask, Flask-RESTful, Flask-JWT, Flask swagger ui and SQLAlchemy ans SQLite3 for database.

# Getting Started

These instructions will let you run project on your local machine for development and testing purposes. 

### **Prerequisites**

Make sure you have installed Python 3 on your device

### **Modules**
* [Flask](https://pypi.org/project/Flask/):\
&emsp;&emsp;Flask is a lightweight web framework for Python, ideal for building web applications and APIs.
* [Flask-RESTful](https://pypi.org/project/Flask-RESTful/):\
&emsp;&emsp;Flask-RESTful is an extension for Flask that simplifies the creation of RESTful APIs, making it easier to define resources and endpoints.
* [Flask-Swagger-UI](https://pypi.org/project/flask-swagger-ui/):\
&emsp;&emsp;Flask-Swagger-UI is used to generate a user-friendly Swagger UI interface for API documentation. It allows developers and users to explore and test API endpoints easily.
* [Flask-JWT](https://pypi.org/project/Flask-JWT/):\
&emsp;&emsp;Flask-JWT is a library for handling JSON Web Tokens (JWT) authentication in Flask applications. It provides secure user authentication and token-based access control.
* [SQLAlchemy](https://pypi.org/project/SQLAlchemy):\
&emsp;&emsp;SQLAlchemy is a popular SQL toolkit and Object-Relational Mapping (ORM) library used for database operations. It enables the application to interact with a relational database.
* [Flask_swagger_ui](https://pypi.org/project/flask-swagger-ui/):\
&emsp;&emsp;This is a Python library that provides integration with Swagger UI for Flask applications.

<br>

# Project structure
```
  flask_api/
  |--- .env/
  |--- modules/
  |    |    |--- __init__.py
  |    |    |--- item.py
  |    |    |--- store.py
  |    |    |--- user.py
  |--- resources/
  |    |    |--- __init__.py
  |    |    |--- item.py
  |    |    |--- store.py
  |    |    |--- user.py
 
  |--- app/
  |--- db.py/
  |--- security.py/
  

```
<br>

# Step to start flask rest api

A step by step series of examples that tell you how to get a development env running

1. Install virtual environment
```
pip install virtualenv
```
2. Create virtual environment and activate inside your flask-rest-api directory according the above structure
```
virtualenv venv
> On windows -> venv\Scripts\activate
> On linux -> . env/bin/activate
```
3. Install librares or module on your virtual environment with pip as mentioned in modules
```
pip install flask sqlalchemy flask-sqlalchemy flask-migrate
```
5. set the KEY variable in .config file. Which is the app secrete key.
   
6. Run  the `app.py` file.
```python
Access the API at http://127.0.0.1:5000
```
<br>


# Components
## **API Endpoints**
Here are some of the main API endpoints:

&emsp;**/item/\<string:name>**: CRUD operations for item.\
&emsp;**/store/\<string:name>**: CRUD operations for stores containing items.\
&emsp;**/user/\<int:user_id>**: CRUD operation for user.\
&emsp;**/register/**: To register new user.\
&emsp;**/auth**: To authenticate and this will return a JWT token.
<br>
For detailed information about available endpoints and request/response formats, refer to the Swagger Documentation section.

## **Authentication**
This project uses JWT (JSON Web Tokens) for authentication. To access protected endpoints, follow these steps:

Register a user account or obtain valid credentials.\
&emsp;**/register**: To regiester new user

Authenticate by sending a POST request to **/auth** with your credentials to receive a JWT token.

Include the JWT token in the Authorization header of your requests to access protected resources.\
&emsp;**/items**: We need JWT toke to access this request.


## **Database**
The project uses SQLAlchemy to interact with the database. Make sure to set up your database connection and models according to your requirements. Refer to the models.py file for database schema.
* **Database** : data.db
* **Tables**
  * items
    * Schema
      ```python
      | Column Name  | Data Type  |  Description                    |
      |--------------|------------|---------------------------------|
      | id           | Integer    | ID of item          |
      | name         | Text       | Name of the item                |
      | price        | Float      | Price of the item               |
      | store_id     | Integer    | ID of store to which item place |
       ```
      ```
      Primary key: id
      Foreign Key: store_id
      ```
  * stores
     * Schema
        ```python
        | Column Name  | Data Type  | Description             |
        |--------------|------------|-------------------------|
        | id           | Integer    | Id of store             |
        | name         | Text       | Name of the store       |
        ```
        
        ```
        Primary key: id
         ```

  * users
    * Schema
      ```python
      | Column Name  | Data Type  |  Description              |
      |--------------|-----------|----------------------------|
      | id           | Integer    | Unique identifier         |
      | username     | Text       | Name of the user          |
      | password     | Text       | Password of user to login |
      ```
      ```
      Primary Key: id
      ```



## **Swagger Documentation**
Interactive API documentation is available using Swagger UI. Access it at http://localhost:5000/swagger after running the application. Explore and test the API endpoints directly from the Swagger UI interface

### Online demo?
#### [Backend Flask REST API]()

## **Conclusion**
This Flask project showcases the development of a RESTful API with secure user authentication, database integration, and interactive documentation using Swagger UI. It provides a solid foundation for building web applications and services that require API functionality.
