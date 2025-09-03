# Project name
Freelance Marketplace for second hand products

# Overview
A functional web platform where users in a local community can list, browse, and contact sellers of second-hand goods (e.g. furniture, electronics, books). The goal is to support campus students who are finishing sell their products easily and those continuing get array of quality second hand goods at a comrade price.

# Planned Features
User Authentication(login, logout, register)
Admin dashboard
Seller dashboard
Customers/users dashboard
Landing page
Email Linking
Messaging btn seller and buyer
API for mobile app intergration

# Tech stack
Python 
Django 
Django Rest Framework
Bootstrap

# Installation
clone repo
`` bash 
git clone https://github.com/Coderline-32/Resell_Hub
cd Resell_Hub
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
cd config
python manage.py migrate
python manage.py runserver

# Usage for new user
Copy runserver url and paste in browser
This will take you to home
click sign up button to create account in signup page
After signing up you will be redirected to homepage but as user with profile
Open Profile and register as seller 
After seller registration you will be able to start creating products
Create Products in create products page, manage and customize them




# Created:
# Login:
For user to log into their accounts
Used Django athentication sytem

# Sign up
User to create accounts
Used Django authentication system

# Log out
To switch out of their accounts

# home page
Page to list products for buyers, with option of signing in for first time users

# Profile page
Contain profile info with button to register as seller

# Register seller page
For seller registration

# Seller_dashboard page
Allow sellers to list, manage and delete products

# Create Product page
Allow sellers to create products


# Product detail page
Shows product details including name of seler and contact details

# Seller Profile page
Show all seller products listings

# API endpoints
Base URL: http://127.0.0.1:8000/api/
Authentication
POST: /token/
Request Body:

    {
        "username": "Ke",
        "password" : "1234"
    }

Response:

    {
        "refresh": "<refresh token>",
        "access": "<acces token>"
    }

LOGOUT
POST: /user/logout/
Request Body:

    {
        "refresh_token": "<refresh token>"
    }

Headers:

    Authorization: Bearer <access_token>
    Content-Type: application/json

 Response:

    {
        "message" : "Logout Successful"
    }

REGISTER  
POST: /user/register/  
Request Body:

    {
        "username": "col",
        "email": "c@gmail.com",
        "password": "Q1234567890p,",
        "password2": "Q1234567890p,"
    }

Response:

    {
        "id": 1,
        "username": "col",
        "email": "c@gmail.com"
    }

GET USER INFO
GET: /use/profile/
Headers:

    Authorization: Bearer <access_token>

Response:

    {
        "username":"col",
        "email":"c@gmail.com"
        "id":"1"
        "date_joined":"2025-09-01"
        "full_name":"collo collo"
        "location": "Ruiru"
        "image":"https..."
    }
GET SELLER INFO
GET: /seller/profile/
Headers:

    Authorization: Bearer <access_token>

Response:

    {
        "shopname":"co",
        "id_number":"12364757757"
        "phone_number":"07128288373"
        "location": "Ruiru"
       
    }

GET USERS DETAILS(ADMIN_ONLY)
GET: /users/details/
Headers:

    Authorization: Bearer <access_token>

Response:

     {
        "username": "Sam",
        "id": 1,
        "email": "sam@gmail.com",
        "date_joined": "2025-08-16T04:44:50.291956Z",
        "full_name": null,
        "location": null,
        "image": null
    },
    {
        "username": "Ke",
        "id": 3,
        "email": "k@gmail.com",
        "date_joined": "2025-08-16T07:24:22.192266Z",
        "full_name": "Keygan Dougllas",
        "location": "Juja",
        "image": "http://127.0.0.1:8000/media/profile/pexels-steve-923192.jpg"
    },
    
    

GET SELLERS DETAILS(ADMIN_ONLY)
GET: /sellers/details/
Headers:

    Authorization: Bearer <access_token>

Response:

    {
        "shop_name": "Kenuwn",
        "phone_number": "0714567987",
        "id_number": "37269644",
        "location": "Nairobi,Kenya"
    }
    {
        "shopname":"co",
        "id_number":"12364757757",
        "phone_number":"07128288373",
        "location": "Ruiru"
       
    }

GENERAL PRODUCTS ACCESS
GET: /products/
Headers:

    Authorization: Bearer <access_token>

Response:

    {
        "id": 14,
        "title": "Drone",
        "description": "Note that if deploying to Apache using mod_wsgi, the authorization header is not passed through to a WSGI application by default, as it is assumed that authentication will be handled by Apache, rather than at an application level.\r\n\r\nIf you are deploying to Apache, and using any non-session based authentication, you will need to explicitly configure mod_wsgi to pass the required headers through to the application. This can be done by specifying the WSGIPassAuthorization directive in the appropriate context and setting it to 'On'.",
        "price": 100,
        "image": "http://127.0.0.1:8000/media/products/pexels-k15-photos-233269-744366_O79gWFl.jpg",
        "location": "Thika",
        "category_name": "Electronics",
        "seller": 1,
        "created_at": "2025-09-01T19:58:23.947256Z"
    },
    {
        "id": 13,
        "title": "Camera",
        "description": "The URL api/detail/ without a pk is a different endpoint. To fix this, simply ensure the more specific URL patterns are listed before the more general ones.",
        "price": 120,
        "image": "http://127.0.0.1:8000/media/products/pexels-gabriel-freytez-110599-341523.jpg",
        "location": "Weitethie",
        "category_name": "Electronics",
        "seller": 1,
        "created_at": "2025-08-31T19:09:14.174706Z"
    },
    {
        "id": 7,
        "title": "bed",
        "description": "Great question 👌. For a Minimum Viable Product (MVP) in e-commerce for second-hand items, the goal is to keep it lean but functional — just enough to validate your idea with real users, while avoiding feature bloat. Here’s what it should contain:",
        "price": 60,
        "image": "http://127.0.0.1:8000/media/products/pexels-laurix-2375033.jpg",
        "location": "Juja",
        "category_name": "Furnitures",
        "seller": 1,
        "created_at": "2025-08-31T11:53:41.441863Z"
    }


SPECIFIC PRODUCT ACCESS
GET: /product/detail/<int:7>/
Headers:

    Authorization: Bearer <access_token>

Response:

    {
        "id": 7,
        "title": "bed",
        "description": "Great question 👌. For a Minimum Viable Product (MVP) in e-commerce for second-hand items, the goal is to keep it lean but functional — just enough to validate your idea with real users, while avoiding feature bloat. Here’s what it should contain:",
        "price": 60,
        "image": "http://127.0.0.1:8000/media/products/pexels-laurix-2375033.jpg",
        "location": "Juja",
        "category_name": "Furnitures",
        "seller": 1,
        "created_at": "2025-08-31T11:53:41.441863Z"
    }

SELLER PRODUCTS ACCESS
GET/POST: /seller/products/
Headers:

    Authorization: Bearer <access_token>

Request Body:

     {
        "id": 7,
        "title": "bed",
        "description": "Great question 👌. For a Minimum Viable Product (MVP) in e-commerce for second-hand items, the goal is to keep it lean but functional — just enough to validate your idea with real users, while avoiding feature bloat. Here’s what it should contain:",
        "price": 60,
        "image": "http://127.0.0.1:8000/media/products/pexels-laurix-2375033.jpg",
        "location": "Juja",
        "category": "3",
        
    },
    {
        "id": 8,
        "title": "Camera",
        "description": "Great question 👌. For a Minimum Viable Product (MVP) in e-commerce for second-hand items, the goal is to keep it lean but functional — just enough to validate your idea with real users, while avoiding feature bloat. Here’s what it should contain:",
        "price": 150,
        "image": "http://127.0.0.1:8000/media/products/pexels-k15-photos-233269-744366.jpg",
        "location": "Ruiru",
        "category": "2",
        
    }

Response:
    
    {
        "id": 7,
        "title": "bed",
        "description": "Great question 👌. For a Minimum Viable Product (MVP) in e-commerce for second-hand items, the goal is to keep it lean but functional — just enough to validate your idea with real users, while avoiding feature bloat. Here’s what it should contain:",
        "price": 60,
        "image": "http://127.0.0.1:8000/media/products/pexels-laurix-2375033.jpg",
        "location": "Juja",
        "category_name": "Furnitures",
        "created_at": "2025-08-31T11:53:41.441863Z"
    },
    {
        "id": 8,
        "title": "Camera",
        "description": "Great question 👌. For a Minimum Viable Product (MVP) in e-commerce for second-hand items, the goal is to keep it lean but functional — just enough to validate your idea with real users, while avoiding feature bloat. Here’s what it should contain:",
        "price": 150,
        "image": "http://127.0.0.1:8000/media/products/pexels-k15-photos-233269-744366.jpg",
        "location": "Ruiru",
        "category_name": "Electronics",
        "created_at": "2025-08-31T11:53:41.441863Z"
    }
   