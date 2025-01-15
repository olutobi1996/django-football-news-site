# Django Blog Project



A fully-featured blog application built with Django, designed to showcase the core functionalities of a content management system (CMS). This project allows users to create, manage, and interact with blog posts, including adding and approving comments.

## Features

- 📝 Create, edit, and delete blog posts.

- 💬 Add, view, and approve comments.

- 🔍 Display a list of all blog posts.

- 📄 Detailed view for individual blog posts.

- 📅 Auto-timestamp for posts and comments.

- ⚙️ Admin interface for managing posts and comments.

Features



## Blog Posts

	•	Create, Read, Update, and Delete (CRUD) blog posts.

	•	Auto-timestamp for post creation and updates.

	•	Rich text support for blog content.



## Comments

	•	Add comments to blog posts.

	•	Admin approval workflow for comments.

	•	Approved comments are displayed publicly.



## User-Friendly Interface

	•	Minimalistic and clean design for users to navigate blog posts.

	•	Admin panel for managing posts and comments.



## Additional Features

	•	Pagination for large lists of blog posts.

	•	Filter approved/unapproved comments.

	•	Extendable architecture for adding tags, categories, or user authentication.



## Tech Stack

	•	Language: Python (>=3.8)

	•	Framework: Django (>=4.0)

	•	Database: SQLite (default, easy to switch to PostgreSQL or MySQL)

	•	Frontend: HTML5, CSS3, Bootstrap (optional)

	•	Development Server: Django’s built-in server for local development



## Prerequisites



## Make sure you have the following installed before setting up the project:

	•	Python (>= 3.8)

	•	pip (Python package manager)

	•	A virtual environment tool like venv or virtualenv



## Installation and Setup



1. Clone the Repository



git clone https://github.com/olutobi1996/django-football-news-site.git

cd your-django-blog



2. Set Up a Virtual Environment



python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate



3. Install Dependencies



pip install -r requirements.txt



4. Apply Migrations



Run the following commands to create the database schema:



python manage.py makemigrations

python manage.py migrate



5. Create a Superuser



Create an admin account to access the admin panel:



python manage.py createsuperuser



Follow the prompts to set a username, email, and password.



6. Run the Development Server



python manage.py runserver



Visit https://8000-olutobi1996-djangofootb-p47lxg23wkk.ws-eu117.gitpod.io/ in your browser to view the application.



## Usage



## Adding Blog Posts

	1.	Log in to the Django admin panel at https://8000-olutobi1996-djangofootb-p47lxg23wkk.ws-eu117.gitpod.io/admin/.

	2.	Add new blog posts via the “Post” model.



## Managing Comments

	1.	Comments submitted by users are not visible by default.

	2.	Approve comments in the admin panel under the “Comment” model.



## Viewing Blog Posts

	1.	Visit the homepage (/) to see a list of blog posts.

	2.	Click on any blog post to view its details, including approved comments.



## Project Structure



your-django-blog/

├── blog/                 # Main app for the blog

│   ├── migrations/       # Database migrations

│   ├── templates/        # HTML templates for the blog

│   │   ├── blog/         # Templates for blog-specific views

│   │       ├── base.html # Base template for the project

│   │       ├── post_list.html  # Homepage template

│   │       └── post_detail.html # Single post template

│   ├── admin.py          # Admin configurations for models

│   ├── apps.py           # App configuration

│   ├── models.py         # Database models for posts and comments

│   ├── views.py          # View functions for blog logic

│   ├── urls.py           # URL routing for the blog

│   └── forms.py          # Forms for user input

├── your_project/         # Django project folder

│   ├── settings.py       # Project settings

│   ├── urls.py           # Root URL configuration

│   ├── wsgi.py           # WSGI entry point

│   └── asgi.py           # ASGI entry point

├── manage.py             # Django management script

├── requirements.txt      # Python dependencies

└── README.md             # Project documentation



## Key Files and What They Do



blog/models.py



Defines the Post and Comment models:

	•	Post: Stores blog post data such as title, body, and timestamps.

	•	Comment: Stores user-submitted comments with an approval flag.



blog/views.py



Contains view functions:

	•	post_list: Displays a list of all blog posts.

	•	post_detail: Displays the details of a specific blog post and its approved comments.



blog/forms.py



Defines a form for adding comments:

	•	Includes fields like author and body.



blog/templates/



Contains the HTML templates:

	•	base.html: The base template extended by all other templates.

	•	post_list.html: Displays a list of all blog posts.

	•	post_detail.html: Displays a single blog post with its comments.



## Requirements



Here’s a sample requirements.txt file:

asgiref==3.8.1
cloudinary==1.36.0
crispy-bootstrap5==0.7
dj-database-url==0.5.0
dj-rest-auth==7.0.0
dj3-cloudinary-storage==0.0.6
Django==4.2.17
django-allauth==0.57.2
django-crispy-forms==2.3
django-froala-editor==4.3.1
djangorestframework==3.15.2
gunicorn==20.1.0
oauthlib==3.2.2
psycopg2==2.9.10
PyJWT==2.10.1
python3-openid==3.2.0
requests-oauthlib==2.0.0
sqlparse==0.5.2
urllib3==1.26.20
whitenoise==5.3.0


## Testing



To run tests for the application:

	1.	Test Cases ran in blog folder.



python manage.py test



## Deployment



1. Prepare for Deployment

	•	Update the ALLOWED_HOSTS setting in settings.py.

	•	Configure a production database (e.g., PostgreSQL).



2. Collect Static Files



Run the following command to collect static files:



python manage.py collectstatic



3. Use a Production Server



Deploy using a WSGI server like Gunicorn and a web server like Nginx.



## Contributing



Contributions are welcome! Please follow these steps:

	1.	Fork the repository.

For any questions or suggestions, feel free to contact me:

	•	Email: olutobi1996@icloud.com

	•	GitHub: olutobi1996

