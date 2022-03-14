# FAQ PortaL - Displays FAQ people have and when user clicks on the question in WEBUI the answer for it is displayed


Django based web app, show question and it's answer. The project currently supports:

- Enable user registration with a simple registration form ✅
    * Fields:
        * ✅    email
        * ✅    password
    * ❌ Send activation email
    * ❌ Password reset/Change password pages are optional
- Admin panel in which admin can input Questions and Answers ✅
    * ✅ Do not allow adding duplicate Questions
- User interface which:
    * ✅ Lists all questions
        * ✅ User must login before proceeding
        * ✅ questions list must be sorted by date on which the question is published in descending order
        * ✅ Hide questions older than 1 week
        * ✅ When a question is clicked user is redirected to other page which displays Question and Answer for it
- Shows simple form for currency conversion US dollars to Euro✅
    * Fields:
        * ✅    Amount
    * ✅ Exchange ratio must be dynamic(the exchange rate for the current day). 
- Management command ✅
    * ✅add CLI command in the form of "python3 manage.py delete_old_questions", which when executed will delete all questions older than 1 week
- Write tests ✅

## Tech

Application is using following libraries:

* **Django** - high-level Python web framework.
* **django-crispy-forms** - control the rendering behavior of Django forms in a very elegant and DRY way.
* **money.js** - Simple JavaScript currency conversion library with no dependencies, in just over 1 kb.
* **jQuery** - JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax. 

## Installation

Once cloned on your local machine. Use to following commands to run the application.
```sh
$ cd faq_portal
$ python3 -m venv venv
```
Now the virtual env is all set. All you have to do is activate it.
Windows activation:

```sh
$ . venv/Scripts/activate
```
Linux:

```sh
$  source venv/bin/activate
```

Once activated navigate back to root directory and install all dependencies.

```sh
(venv) $ pip install -r requirements.txt
```


## Running the Web App

Step by step commands:

1. `python ./manage.py collectstatic` - collects the static files into STATIC_ROOT.

2. `python ./manage.py makemigrations`- packaging up your model changes into individual migration files.

3. `python ./manage.py migrate` - propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

4. `python ./manage.py createsuperuser` - create a "superuser" account that has full access to the site and all needed permissions.

5. `python ./manage.py runserver` - run a emulated server on your local computer. By default you can access the portal through http://localhost:8000/

6. `python ./manage.py test apps.questions.tests` - run test to validate Question-Answer integrity in database.


## Endpoints

>### Login
>```sh
>http://localhost:8000/login
>```
>If user access root web address and haven't login, server will redirect to login page. You may use your `superuser` account or register a new one using create account link in login page.

>### Register
>```sh
>http://localhost:8000/register
>```
>Register new user into portal.

>### Home
>```sh
>http://localhost:8000/
>```
>Show list of question sort in descending order by created time.

>### Question Details
>```sh
>http://localhost:8000/details/{question_id}/
>```
>Displays Question and Answer by `question_id` in the new web page.

>### Currency Converter
>```sh
>http://localhost:8000/currency
>```
>Currency conversion US dollars to Euro. Using exchange rates from [Open Exchange Rates](https://openexchangerates.org/).

>### Logout
>```sh
>http://localhost:8000/logout
>```
>Logged out existing user from portal.