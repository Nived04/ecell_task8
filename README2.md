## User Authentication and authorization system
    This website helps to perform 3 main operations:
    Login, Registration and Logout.

## Framework
    Django

## Requirements:
    Requirements for installation are mentioned in 'requirements.txt' file

## Features
    * Home (pre-login page)----(a)
        1. Login-----(b)
        2. Register--(c)
    * Post-login page --> Home
        1. Profile --(d)
            * Biodata (if user is superuser)
                * Main -------(e)
                    1. Education --(f)
                    2. Places -----(g)
                    3. Extra ------(h)
        2. Logout

## How to use:

The site is equipped with one main navigation bar, through which all the requisite places can be navigated to.
It has 2 components, pre-login options and post-login options which are:
Login and Register, and Logout and Profile respectively.

a) Home Page- 
    This is the fundamental page, before and after login.
    It is un-protected page meaning it can be directly accessed via its url.

b) Login Page-
    Using django auth system, login page enables user to log in to the site.

c) Register Page-
    Again using Django, user can sign up to log in to the site. After signing up and submitting, user is redirect to log in page.

d) Profile Page-
    This page can be accessed through the navigation bar only after the user has logged in. It is a protected page which cannot be accessed directly via url if the user is not logged in.

e) Main biodata page-
    If the user is the superuser then there is an option to view to the biodata of the creator in the profile   page. This page comes with a navigation bar of its own, and from here, user can access some other details of the creator (education, places and extra).
    The main biodata page contains basic information about the creator.

f) Education page-
    Here we can see the education overview of the creator.

g) Places page-
    Here we can see the places that the creator has lived in.

h) Extra page-
    Here we can see the some extra informal information about the creator.