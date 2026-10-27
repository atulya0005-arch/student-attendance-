# student-attendance-

Attendance Tracker (Django)
A simple web application built with Django to manage student attendance. You can add students, mark them Present or Absent for any date, and view an attendance report with each student's percentage.

Features
Add new students (name and unique roll number)
Delete students
Mark attendance (Present/Absent) for any date
Re-marking the same date updates the old record instead of duplicating it
Attendance report showing total days, present days and percentage
Admin panel to view and edit all data
Tech Stack
Python 3
Django
SQLite (default database)
HTML and CSS (Django templates)
Project Structure
attendance_tracker/
├── manage.py
├── attendance_project/      # project settings and main urls
│   ├── settings.py
│   └── urls.py
└── tracker/                 # main app
    ├── models.py            # Student and Attendance tables
    ├── views.py             # logic for each page
    ├── forms.py             # student form
    ├── urls.py              # app routes
    ├── admin.py
    └── templates/tracker/   # HTML pages
        ├── base.html
        ├── student_list.html
        ├── add_student.html
        ├── mark_attendance.html
        └── report.html
Database Models
Student: name, roll_no (unique)
Attendance: student (ForeignKey), date, status (P/A), unique per student per date
How to Run Locally
Clone the repository
git clone (https://github.com/atulya0005-arch/student-attendance-)
cd attendance-tracker
Create and activate a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate
Install Django
pip install django
Create the database tables
python manage.py makemigrations
python manage.py migrate
(Optional) Create an admin user
python manage.py createsuperuser
Start the server
python manage.py runserver
Pages
URL	Page
/	List of students
/add/	Add a student
/mark/	Mark attendance for a date
/report/	Attendance report with percentages
/admin/	Django admin panel
How It Works (MVT)
Model: defines the database tables
View: contains the logic and fetches data
Template: HTML pages shown to the user
URLs: connect each address to a view
Author

