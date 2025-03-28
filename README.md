# Django Blog Project

# Overview

![Image](https://github.com/user-attachments/assets/2e6f8434-a944-46a3-97b4-5abe53060b8a)
My Django football blog offers substantial value by delivering curated, insightful content tailored to football enthusiasts. The clean and organized layout, combined with intuitive navigation, ensures users can effortlessly access information and engage with the community. Features like the search bar and categorized posts enhance usability, while interactive elements such as commenting and user authentication promote a sense of community. By leveraging Django’s robust framework, the blog provides a seamless, responsive, and enjoyable experience for all users.

# Key Features

# Navbar

![Image](https://github.com/user-attachments/assets/913234d8-2de2-4988-99af-5a11fbe796ab)

The primary navigation tool provides quick access to essential pages such as Home, About, Contact, and Categories. It ensures users can effortlessly explore different sections of the blog.

# Blog Posts

![Image](https://github.com/user-attachments/assets/d099a2b3-6672-41e0-8a54-e8222470a9a0)

Each post offers insightful content related to football, complete with titles, publication dates, and author information. This structure allows readers to stay informed and engaged with the latest discussions.

# “Read More” Links

![Image](https://github.com/user-attachments/assets/70f455aa-e0bb-42b4-bfb6-04a0efd27c79)

These links accompany brief excerpts of each blog post, inviting users to delve deeper into topics of interest by accessing the full articles.

# Search Bar

![Image](https://github.com/user-attachments/assets/d0eec2c2-07c6-4004-b020-838255f32e84)

Positioned prominently, the search functionality enables users to quickly find specific articles or topics, enhancing the overall accessibility of the blog’s content.

# Information Page

![Image](https://github.com/user-attachments/assets/44334780-23d7-4dca-9da7-99e36a19ea94)

This section provides background about the blog, its mission, and the team behind it, fostering a connection between the readers and the creators.

# User Authentication

# Sign-In and Sign-Out Pages

![Image](https://github.com/user-attachments/assets/ea877dec-5658-445e-a375-ef8473351799)

![Image](https://github.com/user-attachments/assets/ba9e0f6e-4c21-444e-a68f-1d3c62ca4100)

These pages facilitate user authentication, allowing readers to log in to access personalized features or log out when they finish their session, ensuring a secure and tailored experience.

# Registration Page

![Image](https://github.com/user-attachments/assets/8947bc77-996b-417e-9a34-0f2de7c6a108)

New users can create accounts here, enabling them to participate in discussions, leave comments, and engage more deeply with the community.

# Commenting Features

# Leave a Comment

![Image](https://github.com/user-attachments/assets/2afec92f-ecfe-4bd6-bae6-f3bfecc9e9ea)

Authenticated users can leave comments on blog posts, encouraging interaction and discussion. The comment form is straightforward, requiring only the comment text.

# Save Changes Comment

![Image](https://github.com/user-attachments/assets/bfcadc83-04bd-469b-9400-557b8d32f879)

Authenticated users can contribute to conversations by submitting comments on blog posts, fostering an interactive and dynamic community.

# Edit Comment

![Image](https://github.com/user-attachments/assets/2dc7a479-54a4-4d93-8310-1748a3dcf648)

This feature allows users to modify their previously submitted comments, ensuring their contributions remain accurate and reflective of their current views.

# Delete Comment

![Image](https://github.com/user-attachments/assets/89c4a71a-2699-4a48-a38f-9926f4fd7e1a)

Users have the autonomy to remove their comments if they choose, maintaining control over their participation and the content they share.

# Approval for Comments

![Image](https://github.com/user-attachments/assets/e9c854cb-405d-4b35-8417-04ba1c82bd7a)

To maintain content quality, new comments may require approval before becoming publicly visible. This moderation ensures a respectful and relevant discussion environment.

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

![ERD Relatiopnship](https://github.com/user-attachments/assets/431ab098-89e9-4fcb-8cda-f48cbd215103)

![Wireframe](https://github.com/user-attachments/assets/d950a365-94c3-470c-b511-a4840b893013)
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



Visit https://django-football-news-site-5fad26e895d2.herokuapp.com/ in your browser to view the application.



## Usage



## Adding Blog Posts

	1.	Log in to the Django admin panel.

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
            
			├── search_results.html  # Search template

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

	•	search_results.html: Search a single blog post for user.



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

How to Run Tests
To run the test suite, execute the following command in your project directory:

bash
Copy
Edit
python manage.py test
Test Details
Setup
The setUp method initializes test data to be used across all tests:

Posts:
A published post (self.post).
A draft post (self.draft_post).
Comments:
A comment (self.comment) linked to the published post.
User:
A test user (self.user) and an alternate user for unauthorized access tests.
Tests
1. test_post_list_view
Purpose: Verifies the functionality of the PostList view (home).
Assertions:
HTTP status code is 200.
Correct template (blog/index.html) is used.
Only published posts are displayed in the post list.

2. test_post_detail_view
Purpose: Verifies the post_detail view for a published post.
Assertions:
HTTP status code is 200.
Correct template (blog/post_detail.html) is used.
The view includes post details and associated comments.

3. test_post_detail_unauthenticated
Purpose: Ensures unauthenticated users are redirected to the login page when attempting to access the post_detail view.
Assertions:
Redirect to /accounts/login/.

4. test_comment_edit_view
Purpose: Validates that the owner of a comment can edit it.
Assertions:
The comment is updated successfully.
Redirects to the post_detail view after editing.

5. test_comment_edit_unauthorized
Purpose: Prevents unauthorized users from editing someone else’s comments.
Assertions:
The comment remains unchanged.
Redirects to the post_detail view.

6. test_comment_delete_without_slug
Purpose: Validates that an authenticated user can delete their own comment.
Assertions:
Comment is successfully deleted.
Redirects to the home page after deletion.

7. test_comment_delete_unauthorized
Purpose: Prevents unauthorized users from deleting comments.
Assertions:
The comment remains in the database.
Redirects to the home page.

8. test_post_search
Purpose: Tests the functionality of the search feature for posts.
Assertions:
HTTP status code is 200.
Correct template (blog/search_results.html) is used.
Returns results that match the query.
Excludes draft posts from the results.

9. test_post_search_no_query
Purpose: Ensures that no results are returned if the search query is empty.
Assertions:
HTTP status code is 200.
Correct template (blog/search_results.html) is used.
No results are returned.
Customization
Update the slug, username, or password values in the test data to match your application’s requirements.
Add more tests if new features are introduced, such as category filtering or pagination.

When the tests are executed, the expected output is as follows:
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.543s

OK


Test Data:

The comment field is populated with a non-empty string ('This is a valid comment').
Assertions:

Ensures the form is valid using assertTrue(comment_form.is_valid()).
If the form is invalid, debug information (form errors) is printed to help identify issues.

data = {
    'comment': 'This is a valid comment',
}
comment_form = CommentForm(data=data)
self.assertTrue(comment_form.is_valid())

2. test_form_is_invalid
Purpose: Verifies that the CommentForm is invalid when required fields are missing or contain invalid data.

Test Data:

The comment field is empty (''), which is invalid because the field is required.
Assertions:

Ensures the form is invalid using assertFalse(comment_form.is_valid()).
If the form is invalid, debug information (form errors) is printed to help identify issues.

data = {
    'comment': '',  # Invalid because the comment is empty
}
comment_form = CommentForm(data=data)
self.assertFalse(comment_form.is_valid())

When the tests are executed, the expected output is as follows:

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.123s

OK

## Deployment



1. Prepare for Deployment

	•	Update the ALLOWED_HOSTS setting in settings.py.

	•	Configure a production database (e.g., PostgreSQL).



2. Collect Static Files



Run the following command to collect static files:



python manage.py collectstatic



3. Use a Production Server



Deploy using a WSGI server like Gunicorn and a web server like Nginx.

## Validator Testing
• HTML
No errors were returned when passing through the official [W3C validator] https://validator.w3.org/nu/?doc=https%3A%2F%2F8000-olutobi1996-djangofootb-p47lxg23wkk.ws-eu117.gitpod.io%2F 

• CSS
No errors were found when passing through the official [(Jigsaw)] https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2F8000-olutobi1996-djangofootb-p47lxg23wkk.ws-eu117.gitpod.io%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en 

JavaScript No errors were found when passing through the official Jshint validator The following metrics were returned:
![jshint](https://github.com/user-attachments/assets/876b3676-b8b9-4e2a-8220-be7b0393af2a)

## Contributing



Contributions are welcome! Please follow these steps:

	1.	Fork the repository.

For any questions or suggestions, feel free to contact me:

	•	Email: olutobi1996@icloud.com

	•	GitHub: olutobi1996

