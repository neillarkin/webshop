# Milestone Project 4 – Full Stack Development
# Online Record Store with Python and Django

## Overview
The application is a mock online record store that allows vinyl collecting enthusiasts the ability to browse and purchase contemporary and vintage vinyl records for sale. The application gives uses the ability to easily find what they are looking for by providing a search function as well as a menu that filters records per genre or per artist. Records that are not in stock can be added to a users personal wishlist and purchased at a later date.

A live version of the app is hosted here: https://neils-webshop.herokuapp.com/ 

Project code is is available here: https://github.com/neillarkin/atari-app 

[![Build Status](https://travis-ci.org/neillarkin/webshop.svg?branch=master)](https://travis-ci.org/neillarkin/webshop)

## WireFrames

* [Mobile](https://neils-webshop.s3-eu-west-1.amazonaws.com/documentation/01.mobile.jpg)
* [Tablet](https://neils-webshop.s3-eu-west-1.amazonaws.com/documentation/02.tablet.jpg)
* [Desktop](https://neils-webshop.s3-eu-west-1.amazonaws.com/documentation/01.desktop.jpg)


## UX
The primary target audience of the application is a potential employer who may be seeking out more information on my capabilities as a developer. The employer may only spend a short time using the application and so it is vital that is no major functional bug, is fully responsive and has a clean and professional interface that gives a positive user experience. The user should be able to quickly get an idea of my competency with modern front and back-end web technologies.
 

The secondary mock target audience for the application is that of the vinyl record collector. The app provides an online service where record collectors can find and purchase vintage and modern vinyl recordings.

### Use case scenarios
Below are some stories that a typical user can follow:

* A new user should be able to:
– Visualize the home page and view all the records currently on sale
– Visualize the artists in the store
– Visualize an artists records
– Visualize genres in the store
– Visualize a genres records
– Visualize the navigation bar and links to all sections of the site
– Visualize a search bar for finding records.
– Return to a previous page with using a device or browsers back button
– Register and create an account

* An active user should be able to purchase a record
– Visualize and browse all the records on sale
– Visualize records by genre
– Filter categories from the navigation bar
– Perform searches from the navigation bar
– Register or log in to an account
– Edit a profile
– Add, remove or amend records in a cart
– Add contact and payment details
– Pay for a record(s) 

* When a registered user wants to add a record to their wishlist
– Add a record to their wishlist
– Edit and Save wishlist item
– Delete a wishlist item

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

### Features to implement
* Improve search results to display both records and artists on the same page
* Improve the send email functionality when resetting a password
* Functionality to display how many items are currently in stock
* Notify users when their wishlist item comes back in stock


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

## Database Schema
![](https://neils-webshop.s3-eu-west-1.amazonaws.com/documentation/relationship-db.png)

## Testing
Test driven development methods were used during development. Django in-built unit-test features were used to perform basic test on various views and classes of the application. Defensive design was incorporated on pages where no results were found, prompting an error message for empty result sets.

### Automated tests were performed on various models, views and forms of the project.
Results of the tests can be seen here: 
[![Build Status](https://travis-ci.org/neillarkin/webshop.svg?branch=master)](https://travis-ci.org/neillarkin/webshop)


1) Classes can be instantiated with local data stored in its attributes. Examples of these tests are in the test_models.py scripts throughout the various apps.

2) View functions were tested to see if they act correctly by returning a template with a status code 200 or in some cases a status 404 if incorrect parameter data was passed.

3) Forms valid data and respond appropriately when correct or incorrect data is passed.

Below is a list of the apps and automated tests that were performed:
* accounts – Login view tested for status 200. Login and Registration forms tested for validation.
* artists – Model tested for instantiation. Views tested for status 200 on all-artists and artists-records templates. Views tests for 404 codes.
* checkout – Order model tested for instantiation.
* genres – Model tested for instantiation. Views tested for status 200 on all-genres and genre-records templates. Views tests for 404 codes.
* home –  Views tested for status 200 and 404 codes
* records – Model tested for instantiation. View templates tested for status 200 on all-records and 404 for no data returned.

### Manual testing was performed on areas of the project that were not tested by automation. 

1) Launch and browse all views of the app on both Chrome and Firefox and Safari desktop browsers.
* Verify app views are accessible and not items are significantly misaligned or truncated.

2) Launch and browse all views of the app on both Chrome and Firefox and Safari mobile browsers.
* Verify app views are accessible and not items are significantly misaligned or truncated.

#### Navbar
1) Click the sore icon at the top-left of the home page. Verify the a list of records appears. Verify there is not back-button visible at the top-left of the page.
1) Click the Records link: Verify a list of records appears. Verify the back button is now visible.
2) Click the Artists link: Verify a list of artists appears. Click the back button. Verify the previous page appears.
3) Click and artist with not records. Verify a message appears.
3) Click an artist with no records. Verify a message appears.
4) Click the Genre link: Verify a drop-down menu of genres appears.
5) Click the genre menu item called All. Verify: a page of genres appears. Verify a genre with 0 records displays a message.

#### Search
1) Enter an artist name in to the search field and click the search button. Verify the artist appear in the results. 
2) Enter a record name in to the search field and click the search button. Verify the artist appear in the results.
3) Enter no data in to the search field and click the search button Verify a message appears of no results found.

#### Profile
1) Register an account. Verify: the home page is visible after login.
2) Browse to the profile page:  Verify: the profile page is visible
3) Browse to the profile page:  Edit the users details and save. Verify: the details have been updated.
4) Browse to the profile page: Click the Reset Password link. Verify an email form appears. Enter an email and click submit. Verify reset link appears in your inbox.
4) Logout. Verify: the home page is visible after logout.

#### Wishlist: 
1) Browse to the Profile page. Verify: a wishlist form is visible.
2) Click the Add a record link. Verify: a form appears with arts and name labels and a button.
3) Enter information in to the wishlist form and click Submit. Verify: the item appears in the list.
4) Delete and item from the wishlist. Verify: A prompt message appears and the item can be deleted.

#### Cart:
1) Add an item to cart: Verify: the item appears in the cart.
2) Navigate to the cart. Verify: the cart view is visible with the added item.
3) Navigate to the cart. Adjust the item quantity. Verify the quantity updates.

#### Checkout:
1) Add an item to cart. Click the checkout button. Verify: a user information form appears.
2) Add details in to the cart checkout form and click Submit payment. Verify the user is redirected to the home page with a message promoting on successful payment.

#### Bugs/Issues
Reset password email is not working. The email is not being sent.

### Deployment
The project has been deployed to both Github and Heroku with media and static files on AWS S3. The version on Heroku is what was used for testing and is considered to be at a production level. The primary differences between both versions is in the Settings config file where the Debug mode has been disabled for security and the env variable has been commented out. 
On occasion the Github base.html may contain differences between the CSS and JS file references where they were being switched from S3 to local (Cloud9) during editing. 

#### Credits and Sources
- Most of the code concepts and logic was taken from Niels and Aarons course work in the ‘Full Stack Frameworks with Django’ modules.
- Bootstrap 4 played a significant role in making adjustments to UI compared to previous projects where adjustments were done in CSS3
- Some forms such as Registration, Login, Checkout, Password Reset forms are taken from the Boostrap 4 library

