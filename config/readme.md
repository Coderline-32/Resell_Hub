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


