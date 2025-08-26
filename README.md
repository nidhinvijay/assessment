# Django Poll System with Interactive UI

This is a full-featured web application for creating, managing, and voting on polls. Built with Python and Django, it features a modern, interactive UI with a particle background and a light/dark theme switcher. The app is robust, secure, and user-friendly.

Users can register, vote once per poll, and view detailed results with charts and percentages. An admin panel is included for easy management of polls, questions, and choices.

## Features

- **User Authentication:** Secure registration, login, and logout.
- **Poll Management:** Admin panel for creating, updating, and deleting polls with multiple questions and choices.
- **Voting System:** Logged-in users can vote on active polls (one vote per user per poll).
- **Results Visualization:** Dynamic results page with total votes and percentage share for each option, displayed with numbers and animated doughnut charts (Chart.js).
- **Modern Interactive UI:**
  - Animated particle background (Particles.js)
  - Glassmorphism design for cards and navigation
  - Theme switcher (light/dark mode)
- **Bonus Features:**
  - "My Votes" section for users to see their voting history
  - Export poll results as CSV
  - Support for poll expiry dates

## Technologies Used

- **Backend:** Python, Django
- **Database:** SQLite 3 (local development)
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Bootstrap 5
- **JavaScript Libraries:** Chart.js, Particles.js

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-folder-name>
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

## Running the Application

### 1. Start the Server

```bash
python manage.py runserver
```

### 2. Access the Application

Open your browser and go to:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Admin Access and Poll Creation

### 1. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

### 2. Log in to the Admin Panel

- Go to: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Log in with your superuser credentials.

### 3. How to Create a Poll

1. In the admin panel, click on **"Polls"** and then **"Add poll"**.
2. Fill in the poll's title and description.
3. In the "Questions" section, add your questions.
4. Click **"Save and continue editing"**.
5. Click on a question link to edit it.
6. On the "Change question" page, add multiple choices for that question.
7. Click **"Save"**.

Your poll is now live and ready for registered users to vote!

---

Enjoy using the Django Poll System!
