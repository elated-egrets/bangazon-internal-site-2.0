# Welcome to Bangazon

This web application is the source code for the Bangazon e-commerce web site. It is powered by Python and Django.

Students, you are inheriting a basic implementation that provides the following features:

1. User registration 
1. User login 
1. User logout 
1. Adding a product 
1. Listing products

Please consult the backlog of issues and work with your product owner to implement the top priority tickets for your sprints.

## To begin work

1. The team lead should clone this repository, then push it to your team's Github repo.
1. Alert your manager when this is complete and all backlog issues will be imported into your project.
1. Each teammate should clone the repository.
1. In the `djangazon` directory that gets created, run the migrations with `python manage.py migrate`

## Helpful Resources

### Django Models and Migrations

Using the requirements above create a [model](https://docs.djangoproject.com/en/1.10/topics/db/models/) for each resource, and use [migrations](https://docs.djangoproject.com/en/1.10/topics/migrations/) to ensure your database structure is up to date.

### Templates

[Django template language](https://docs.djangoproject.com/en/1.10/ref/templates/language/)

### Form Helpers

Django, like Angular, has many built-in [helper tags and filters](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/) when building the site templates. We strongly recommend reading this documentation while building your templates.

## virtual environment
When you pull down this repo setup a virtual environment elsewere in your directory not in this repo. 
`virtualenv [name]`

Then activate it with 
`source [name]/bin/activate`

Then cd back into the root of this repo and run 
`pip install -r requirements.txt`


## style guide

### naming conventions

File, directory, function, and variable names should all follow snake case lower case rules. 

Class names should follow pascal case rules.

### file structure
Files that will serve a similar purpose (views, models, etc...) will live in a subdirectory of that name. Classes created within that directory will need to be imported into the __init__.py file of that directory.


## ERD
https://www.lucidchart.com/documents/edit/92257110-34ad-4d80-9c33-629ca9384027/0?shared=true&


## available models

## order
fields available
user: reference to user object
payment_type: reference to paymenttype object
products: many to many reference to products
date_created: date field, date the order was opened
date_closed: date field, date the order was closed