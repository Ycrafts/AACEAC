# AACEAC - Employee Tracking System for the Addis Ababa City Ethics and Anti-corruption Commission

> **Note:** This project is currently under active development. Only part of the planned functionality has been completed, and some features may be subject to change.

This project is a full-stack web application designed to serve as an employee tracking system for the **Addis Ababa City Ethics and Anti-corruption Commission (AACEAC)**. It provides a comprehensive system for managing employees, their roles, and their positions within the commission's hierarchical organization. The system is composed of a Django REST Framework backend and a React frontend.

## Features

- **User Authentication:** Secure login system for authorized users.
- **Hierarchical Organizational Structure:**
  - Manage Divisions (e.g., Sector Office, Subcity, College, Hospital).
  - Manage Subcities and their Woredas.
  - Define and manage organizational units with parent-child relationships.
- **Employee Management:**
  - Add, view, edit, and delete employee records.
  - Assign roles (e.g., Director, Expert) to employees.
  - Place employees within specific organizational units.
- **Data Management:**
  - Manage various data types like Sector Subdivision Types and Subcity Subdivision Types.
  - Search and filter capabilities across all major data tables.
  - Paginated lists for efficient data browsing.
- **RESTful API:** A well-documented and robust API for all backend functionalities.

## Tech Stack

### Backend
- Python
- Django
- Django REST Framework

### Frontend
- JavaScript
- React
- Vite
- Tailwind CSS

## Project Structure

The project is divided into two main parts:

- `AACEAC/`: The Django backend.
  - `accounts/`: Handles user authentication.
  - `employee_tracker/`: The core application for managing employees and organizational units.
  - `AACEAC/`: Django project settings.
- `AACEACE_frontend/`: The React frontend.
  - `src/pages/`: Contains the main pages of the application.
  - `src/api.js`: Handles communication with the backend API.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Node.js and npm

### Backend Setup

1.  Clone the repository:
    ```sh
    git clone https://github.com/your-username/AACEAC.git
    cd AACEAC/AACEAC
    ```
2.  Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4.  Apply database migrations:
    ```sh
    python manage.py migrate
    ```
5.  Create a superuser to access the admin panel:
    ```sh
    python manage.py createsuperuser
    ```
6.  Run the development server:
    ```sh
    python manage.py runserver
    ```
    The backend will be available at `http://127.0.0.1:8000`.

### Frontend Setup

1.  Navigate to the frontend directory:
    ```sh
    cd ../AACEACE_frontend
    ```
2.  Install npm packages:
    ```sh
    npm install
    ```
3.  Run the development server:
    ```sh
    npm run dev
    ```
    The frontend will be available at `http://localhost:5173` (or another port if 5173 is in use).

## API Endpoints

The backend exposes the following API endpoints under the `/api/` prefix. All endpoints require authentication.

- `/api/accounts/`: For user authentication.
- `/api/employee-tracker/`:
  - `sector-subdivision-types/`
  - `subcities/`
  - `woredas/`
  - `organizational-units/`
  - `employees/`
  - `employee-roles/`
  - `subcity-subdivision-types/`
  - `divisions/`

## Screenshots

*(Add screenshots of your application here)*

### Login Page
![Login Page](./screenshots/Screenshot%202025-06-22%20130343.png)

### Dashboard
![Dashboard](./screenshots/Screenshot%202025-06-22%20130409.png)

### Employee List
![Employee List](./screenshots/Screenshot%202025-06-22%20130536.png)

### Organizational Unit List
![Organizational Unit List](./screenshots/Screenshot%202025-06-22%20130519.png)

### Subcity List
![Subcity List](./screenshots/Screenshot%202025-06-22%20130458.png)

### Woreda List
![Woreda List](./screenshots/Screenshot%202025-06-22%20130430.png)

## Contributing



If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request
