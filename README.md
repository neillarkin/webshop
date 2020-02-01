# Milestone Project 4 – Full Stack Development
# Online Record Store with Python and Django

## Overview
The application is a mock online record store that allows vinyl collecting enthusiasts the ability to browse and purchase contemporary and vintage vinyl records for sale. The application gives uses the ability to easily find what they are looking for by providing a search function as well as a menu that filters records per genre or per artist. Records that are not in stock can be added to a users personal wishlist and purchased at a later date.

A live version of the app is hosted here: https://neils-webshop.herokuapp.com/ 

Project code is is available here: https://github.com/neillarkin/atari-app 

## WireFrame
#### Mobile


#### Desktop


#### Relational Database


## UX
The primary target audience of the application is a potential employer who may be seeking out more information on my capabilities as a developer. The employer may only spend a short time using the application and so it is vital that is no major functional bug, is fully responsive and has a clean and professional interface that gives a positive user experience. The user should be able to quickly get an idea of my competency with modern front and back-end web technologies.
 

The secondary mock target audience for the application is that of the vinyl record collector. The app provides an online service where record collectors can find and purchase vintage and modern vinyl recordings.

### Use case scenarios
Below are some stories that a typical user can follow:

*A new user should be able to:
** Visualize the home page and view all the records currently on sale
** Visualize the artists in the store
** Visualize an artists records
** Visualize genres in the store
** Visualize a genres records
** Visualize the navigation bar and links to all sections of the site
** Visualize a search bar for finding records.
** Return to a previous page with using a device or browsers back button
** Register and create an account

* An active user should be able to purchase a record
** Visualize and browse all the records on sale
** Visualize records by genre
** Filter categories from the navigation bar
** Perform searches from the navigation bar
** Register or log in to an account
** Edit a profile
** Add, remove or amend records in a cart
** Add contact and payment details
** Pay for a record(s) 

* When a registered user wants to add a record to their wishlist
** Add a record to their wishlist
** Edit and Save wishlist item
** Delete a wishlist item

## Features
* Browse all records by artist or genre.
* Browse all artists
* Browse all genres
* View the records of a specific artist
* View the records of a specific genre
* Search for either a record or and artists and browse the results
* Visualise the genres of each record item
* Add a record to the cart and perform a purchase
* Browse a user personal wishlist.
* Add, edit or delete records from a wishlist
* Fully responsive
* Loads quickly
* Easy to navigate on any device

## Features to implement
* Improve search results to display both records and artists on the same page
* Improve the send email functionality when resetting a password
* Functionality to display how many items are currently in stock
* Notify users when their wishlist item comes back in stock

## Relational database
The app uses MongoDB to store three collections called games, developers and years. GridFS is used to create two more collections (fs.files & fs.chunks) are used to store image files.
The app uses a one-to-many relationship between games and artists(developers). One game can have many artists. Each artists’ Object ID is intended to be used as a foreign key in each game document.

## Technologies
The application was built using collection of modern technologies:
* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)  -– to define the elements of on the DOM
* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3) – Enhance the applications user interface
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) – to manipulate elements on the DOM that other technologies cannot do
* [Jquery](https://jquery.com/) – Used to make JavaScript functions easier to implement
* [Bootstrap](https://getbootstrap.com/) – Easily and quickly manipulate DOM elements and make a program responsive 
* [Django](https://www.djangoproject.com/) – Python framework that allows large complex web applications to be quickly built and easily maintained by translating SQL CRUD operations.
* [PostgresSQL](https://www.postgresql.org/) – Secure relational database system used for storing DB schema
* [GitHub](https://github.com/) – Used for version control and backup during development
* [Heroku](https://www.heroku.com/) – Cloud platform used for hosting production level web applications
* [AWS E3](https://aws.amazon.com/s3/) – Used for storage of static and media files for fast access
* [Travis-CI](https://travis-ci.org/) – Used for run test scripts after builds were pushed to Github

A complete list of technologies and versions is listed in the Requirements.txt file on Github

##Database Schema


## Testing
Test driven development methods were used during development. Django in-built unit-test features were used to perform basic test on various views and classes of the application. 

###Automated tests were performed on various models, views and forms of the project.
Results of the tests can be seen here: 
[![Build Status](https://travis-ci.org/neillarkin/webshop.svg?branch=master)](https://travis-ci.org/neillarkin/webshop)


1)  Classes can be instantiated with local data stored in its attributes. Examples of these tests are in the test_models.py scripts throughout the various apps.

2) View functions were tested to see if they act correctly by returning a template with a status code 200 or in some cases a status 404 if incorrect parameter data was passed.

3) Forms valid data and respond appropriately when correct or incorrect data is passed.

Below is a list of the apps and automated tests that were performed:
* accounts – Login view tested for status 200. Login and Registration forms tested for validation.
* artists – Model tested for instantiation. Views tested for status 200 on all-artists and artists-records templates. Views tests for 404 codes.
* checkout – Order model tested for instantiation.
* genres – Model tested for instantiation. Views tested for status 200 on all-genres and genre-records templates. Views tests for 404 codes.
* home –  Views tested for status 200 and 404 codes
* records – Model tested for instantiation. View templates tested for status 200 on all-records and 404 for no data returned.