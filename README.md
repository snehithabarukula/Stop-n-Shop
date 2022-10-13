# Shop-n-stop
# Introduction 

Fashion chipps is a e-commerce website built using html,css,javascript and bootstrap for frotend and django as backend. Fashion chipps sells high-end, eco-conscious fashion and accessories for men and women. Their product descriptions match their style: sassy, yet classy.

# Table of Contents
1) Technologies Used
2) System Requirements
3) Set-up
4) Project Flow 

# Technologies Used 
1) Front-end: In ecommerce, the technology usually refers to the programming languages that are used to develop the platform. Fashion Chipps is an ecommerce website built using html,css,javascript and bootstrap and Python Django
2) Back-end : The Primary database is used to collect the details from the webpages and it's responsible for the data that are shown on UI (front-end). We used Mysql database software.
3) Fashion Chipps uses Python Django as backend.

# System Requirements

Django web applications can be run on almost any machine that can run the Python 3 programming language: Windows, macOS, Linux/Unix, Solaris, to name just a few. Almost any computer should have the necessary performance to run Django during development.
- FOR WINDOWS- Windows 7 version OS, 800MHz Intel Pentium III or equivalent processor, 512MB memory and an additional 250 MB of free disk space.
- FOR UBUNTU- 9.10 version, 800MHz Intel Pentium III or equivalent processor, 512 MB memory and an additional 150 MB of free disk space.
- FOR MAC OS- 10.7 Intel version, Dual-Core Intel processor, 512 memory and additional 150 MB of free disk space.
- Latest version of python. Python 2.7 cannot be used with the current releases of Django (The Django 1.11.x series is the last to support Python 2.7).


# Set Up
you’ll need to know how to setup the following to run the project:

- Set up a virtual environment
- Install Django
- Pin your project dependencies
- Set up a Django project
- Start a Django app


## Installing Python 
[Python](https://www.python.org/downloads/)

### UBUNTU
Ubuntu Linux 20.04 LTS includes Python 3.8.5 by default. You can confirm this by running the following command in the bash terminal:
 

      python3 -V
      Python 3.8.5
You can install pip3 in the bash terminal using:
 
      
      sudo apt install python3-pip
### MAC
macOS "El Capitan" and other more recent versions do not include Python 3. You can confirm this by running the following commands in the zsh or bash terminal to check upon installation:
 
      
      python3 -V
      Python 3.9.0
      
You can similarly check that pip3 is installed by listing the available packages:
 
 
      pip3 list
      
### Windows 
You can then verify that Python 3 was installed by entering the following text into the command prompt:


      py -3 -V
      Python 3.8.6
    
The Windows installer incorporates pip3 (the Python package manager) by default. You can list installed packages as shown:

  
      pip3 list

    

## Project Set Up 
1) The system should have a python setup before setting up django. Installing a latest version of python ide is must.

3) In the next step you need to install a virtualwrapper which is a virtual environment specifically to run this project. 
In cmd create: 


       pip install virtualenwrapper -win
       
Once you've created a virtual environment, and called workon to enter it, you can use pip3 to install Django :
  
  
  
       pip3 install django~=3.1
  

4) Create the virtual environment:
  
  
       mkvirtualenv environment_name
       
6) Install Django :
  
  
       pip install django
       
8) mkdir projects -> cd projects -> django-admin startproject projectname (Here projects is the name of the folder I created on my desktop)
9) To run  the server :
  
  
       python manage.py runserver
       
       
## Project Flow 
Fashion Chipps involves two logical entities - The frontend,Backend (Payment mechanism and database). The frontend involves a series of HTML and CSS web pages that displays products and basic design of the website. The backend involves the database management system software where all the data of the product and users is stored. The database is responsible for the structure of data. The main purpose of the database is to digitally store information that can be captured, retrieved, and distributed easily at a later time. Through this system, information such as transactional or systems oriented data can be organized and tracked based on chosen settings. This also gives businesses the ability to analyze and track information about the products, sales, and customers that have been input into the database.

## References
- Building the Design of e-commerce.(n.d), Retrieved from
https://www.researchgate.net/publication/327897515_Building_the_Design_of_E- Commerce

- Design and Implementation of E-Commerce Website for Shopping.(n.d), Retrieved from 
https://www.researchgate.net/publication/335126262_Design_and_Implementation _of_E-Commerce_Website_for_Shopping
