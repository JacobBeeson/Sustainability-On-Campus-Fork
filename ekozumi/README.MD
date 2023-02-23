### Django README
This README contains general information for our django application, covering important backend information.


## Starting the server
1. Open the terminal in the ekozumi directory
2. Run the command:
    - For Linux/Mac: `python3 manage.py runserver`
    - For Windows: `py manage.py runserver`
3. Once the command has run the server will start
4. Within the terminal website requests will be displayed, when users access the website
5. To access the webpage navigate to the URL: `127.0.0.1:8000/[PATH]`
6. Below lists the possible replacements for the placeholder [PATH]

### Ekozumi
Our ekozumi web app can be accessed by searching `127.0.0.1:8000/ekozumi`. This URL will lead you to the login page for ekozumi, if you already have a login you may access the rest of the application using this form, or if you want to register an account locate the 'Sign Up Now' link and input your information

### Admin
If you are a developer on the ekozumi app you may access the admin panel by searching `127.0.0.1:8000/admin` once the server has started.
This will give you a login prompt, which once logged in you may view and modify models for our application


## Important Backend Directories and Files

### ekozumi_app

- `admin.py` - Where you should declare models if you want them displayed on the admin page. Displaying them on the admin page will allow you to modify models in a simpler way than using terminal
- `apps.py` - General backend configuration
- `forms.py` - Templates for forms used on the website, used to proccess the information entered in a post request by a user
- `models.py` - Declares database models, when creating a model make sure to open terminal in the ekozumi directory, and run the commands `python3 manage.py makemigrations` and `python3 manage.py migrate`. This will declare the models and create tables for them in the database
- `tests.py` - Contains django test cases, to check everything is functioning correctly
- `urls.py` - Declares the url that should be typed into the search bar to access certain webpages, all wepages must follow `127.0.0.1:8000/ekozumi/[PATH]`, where [PATH] is the page you want to access
- `views.py` - Used to render templates, and carry out any logic needed for things like post requests


### ekozumi_app/static
This contains static files such as images and css files.

### ekozumi_app/templates
This contains template html files, which are access by the django backend and displayed on webpages
