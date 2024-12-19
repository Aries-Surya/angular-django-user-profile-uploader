# Vishvena Techno Solutions - My Angular Django App

This project is a full-stack web application built with Angular for the frontend and Django for the backend. It allows users to upload profile photos, which are then stored and managed by the backend.

## Project Structure

- **backend/**: Contains the Django backend application.
  - **manage.py**: Command-line utility for managing the Django project.
  - **mysite/**: Main Django project directory.
    - **settings.py**: Configuration settings for the Django project.
    - **urls.py**: URL routing for the Django application.
    - **wsgi.py**: Entry point for WSGI-compatible web servers.
  - **users/**: Django app for user management.
    - **models.py**: Defines the User model with fields: id, name, mobile, and profile photo.
    - **views.py**: Handles requests related to users, including uploading profile photos.
  - **media/**: Directory for storing uploaded profile photos.
  - **db.sqlite3**: SQLite database file for the Django project.

- **frontend/**: Contains the Angular frontend application.
  - **src/**: Source files for the Angular application.
    - **app/**: Main application components and modules.
      - **upload/**: Component for uploading zip files containing profile photos.
    - **assets/**: Static assets like images and styles.
    - **environments/**: Environment-specific configuration files.
    - **index.html**: Main HTML file that loads the Angular application.
    - **main.ts**: Entry point for the Angular application.
  - **angular.json**: Configuration settings for the Angular project.
  - **package.json**: Lists dependencies and scripts for the Angular project.
  - **tsconfig.json**: TypeScript configuration file.

- **docker-compose.yml**: Defines services, networks, and volumes for Docker containers used in the project.

## Features

- User profile management
- Profile photo upload
- Integration between Angular frontend and Django backend

## Getting Started

### Prerequisites

- Node.js and npm (for the Angular frontend)
- Python and pip (for the Django backend)
- Git

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/aries-surya/angular-django-app.git
    cd my-angular-django-app
    ```

2. **Set up the backend (Django)**

    ```bash
    cd backend
    ```

    - Create a virtual environment

        ```bash
        python -m venv venv
        ```

    - Activate the virtual environment

        ```bash
        # On Windows
        .\venv\Scripts\activate

        # On macOS/Linux
        source venv/bin/activate
        ```

    - Install the required packages

        ```bash
        pip install -r requirements.txt
        ```

    - Apply migrations

        ```bash
        python manage.py migrate
        ```

    - Create a superuser (optional, for accessing the Django admin interface)

        ```bash
        python manage.py createsuperuser
        ```

    - Start the Django development server

        ```bash
        python manage.py runserver
        ```

3. **Set up the frontend (Angular)**

    ```bash
    cd ../frontend
    ```

    - Install the required packages

        ```bash
        npm install
        ```

    - Start the Angular development server

        ```bash
        ng serve --project frontend
        ```

4. **Access the application**

    - The Angular frontend will be running at `http://localhost:4200`
    - The Django backend will be running at `http://localhost:8000`