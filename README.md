# Portfolio Website

A personal portfolio website built with Django to showcase projects, skills, services, and experiences. It includes a fully functional contact form that stores messages in the database and sends email notifications.

## Features

- **Home Page**: Introduction and overview.
- **About**: Personal background and information.
- **Skills**: Showcase of technical skills and proficiencies.
- **Projects**: Display of past and current projects.
- **Internships/Experience**: Details about internships and work experience.
- **Services**: Services offered to clients.
- **Contact Form**: A dynamic contact form that:
  - Saves submitted messages to the database.
  - Sends email notifications to the site owner.

## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (default, can be configured to use PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, JavaScript (Templates)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd portfolio
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install django
   # If there is a requirements.txt file, run: pip install -r requirements.txt
   ```

5. **Apply database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (optional, to access the Django admin panel):
   ```bash
   python manage.py createsuperuser
   ```

7. **Configure Email Settings**:
   To enable the contact form email notifications, make sure to set up your email credentials in `.env` (or directly in `settings.py` if not using environment variables):
   ```env
   EMAIL_HOST_USER='your_email@example.com'
   EMAIL_HOST_PASSWORD='your_email_app_password'
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

9. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

- `core/`: The main Django project configuration directory containing `settings.py`, `urls.py`, etc.
- `portfolio_app/`: The main Django app containing views, models, and logic for the portfolio pages.
- `static/`: Contains static files like CSS, JavaScript, and images.
- `templates/`: Contains HTML templates for the website pages.
- `manage.py`: Django's command-line utility for administrative tasks.

## License

This project is open-source and available under the MIT License.
