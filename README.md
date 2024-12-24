# Django Blog Application

![Blog Screenshot](Screenshot_25-12-2024_11926_127.0.0.1.jpeg)

## Overview

This project is a Django-based blog application. It includes typical Django components such as models, views, templates, and static files. Additionally, there are scripts for generating blog posts and random posts, as well as user management features.

## Directory Structure

- **blog**: Contains the main blog application with Django components like `models.py`, `views.py`, and templates.
- **django_project**: Contains the Django project settings and configuration files.
- **users**: Manages user-related functionality, including forms, models, and views.
- **generate_blog_posts.py**: Script for generating blog content.
- **generate_random_posts.py**: Script for generating random blog posts.
- **manage.py**: Django's command-line utility for administrative tasks.
- **virtual_env**: The project's virtual environment.
- **media**: Directory for media files.
- **profile_pics**: Directory for user profile pictures.

## Features

- User authentication and management
- Blog post creation and management
- Random blog post generation
- Media file handling

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Virtual environment setup

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/django-blog.git
    ```
2. Navigate to the project directory:
    ```bash
    cd django-blog
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv virtual_env
    source virtual_env/bin/activate  # On Windows use `virtual_env\Scripts\activate`
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Apply migrations:
    ```bash
    python manage.py migrate
    ```
2. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
3. Run the development server:
    ```bash
    python manage.py runserver
    ```

### Usage

- Access the application at `http://127.0.0.1:8000/`
- Admin interface at `http://127.0.0.1:8000/admin/`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.