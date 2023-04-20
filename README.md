                                                HOME
                                         ________|_________
                                        |                  |
                                      LOGIN <---------- REGISTER 
                                ________|_________
                               |                  |
                            Superuser            User 
                                






## Requirements:
You can find the requirements to pip install virtual environment in the 'requirements.txt' file

## Site Functioning

Site starts from the home page that is present throughout unless some other page is loaded.
    
### Navigation Bar:
This bar is fundamental to the working of the site since it contains all the necessary links to navigate through the website.
Firstly, while the user is not yet authenticated by the Django authentication, the navigation bar will display 2 options, LOGIN and REGISTER.
Next, upon registration, user is redirected to login page, and after succesful login, user is taken to back to the home page.

Now, in this case, the user is authenticated. So the Nav Bar shows new 2 options, PROFILE and LOGOUT.

Clicking on profile, the user is taken to a protected area, that cannot be accessed simply by using the url. This area contains the profile of the user (for now, the profile just contains "Hi <username>")

There is a separate option for superusers, in profile section, which I will come to in the webpage section.

The LOGOUT button does the usual performance of logging the user out (through Django's authentication)

### Webpages
Following webpages are functional:
Home, Login, Register, Protected (and within protected, Biodata)

All these webpages use the base html file which does basic function of extending the template of each file so that they can function under the outer look of base. Moreover base file also styles each page, through background color and navigation bar.

Coming to Home page, this page is visible when we first start the localhost and is also visible when we log in.
Login page and Register page are default but customized pages, part of Django form. They are used for login, authentication and signup.

After logging in, when we click on the PROFILE button, we are taken to the protected page. This page contains the profile of the user.

However, in the case of a superuser, it also contains a link to view to the Biodata of the superuser.

The Biodata page is not functional but just an idea.
Biodata page has a navigation bar of itself that lets the superuser navigate to various pages
(although due to time constraints, I have not been able to make these pages, but to create them, there are the following 3 things that should be done:
1- make a url of that page in url.py, so that the user can be redirected to that page
2- make a custom view of that page in views.py, so that when the url calls the view, the view can further call the template of the page we wish the user to see
3- make the template of the page by creating an html file  )

So, these are all the pages and their functions.