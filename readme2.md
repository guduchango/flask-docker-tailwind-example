# Flask Project Documentation

## Project Structure Overview
This project is a Flask-based web application with a modular structure and Docker support. Below is a detailed breakdown of the project structure:

### **1. `app/controller/`**
Contains the logic for handling API requests and rendering views.
- **`auth_controller.py`**:
  - Handles authentication for the application.
  - Supports both API-based authentication (JWT) and session-based authentication.
- **`person_controller.py`**:
  - Manages API actions related to person entities.
- **`person_controller_views.py`**:
  - Contains logic for rendering views using Jinja templates.

### **2. `app/models/`**
Defines the database models for the application.
- **`person.py`**:
  - Represents the `Person` entity.
- **`user.py`**:
  - Represents the `User` entity.

### **3. `app/routes/`**
Defines routing logic for the application.
- **`api_routes.py`**:
  - Contains API-specific routes for handling HTTP requests.
- **`views_routes.py`**:
  - Contains view-specific routes for rendering templates using Jinja.

### **4. `app/static/`**
Stores static assets such as stylesheets and other frontend resources.
- Built with **Tailwind CSS** for responsive and modern design.

### **5. `app/templates/`**
Holds the HTML templates for the application.
- **Base Templates**:
  - **`base.html`**: The base layout template used across the application.
  - **`index.html`**: The main landing page of the application.
  - **`login.html`**: The login page for user authentication.
- **Person Templates**:
  - **`create_person.html`**: Template for creating a new person entity.
  - **`edit_person.html`**: Template for editing an existing person entity.
  - **`index_person.html`**: Template for listing all person entities.

### **6. `app/auth_utils.py`**
Contains utility functions for handling authentication logic.
- Manages JWT token generation and validation.
- Handles session-based authentication mechanisms.

### **7. `tests/`**
Contains unit tests for the application.
- **`test_api_persons.py`**:
  - Tests API endpoints for person-related functionality.
- **`test_views_persons.py`**:
  - Tests view-related functionality.
- **`conftest.py`**:
  - Configuration for test setup and fixtures.

#### **Running Tests**
To execute the test suite, run the following command:
```bash
pytest -s ./tests/
```

### **8. Docker Configuration**
This project is configured to run in a Docker environment.
- **`Dockerfile`**:
  - Defines the Docker image for the application.
- **`docker-compose.yml`**:
  - Manages multi-container Docker applications.

#### **Steps to Build and Run in Docker**
1. Build the Docker image:
   ```bash
   docker-compose build
   ```
2. Start the containers:
   ```bash
   docker-compose up -d
   ```
3. Access the application at `http://127.0.0.1:5000`.

#### **Database Setup**
1. Access the app container:
   ```bash
   docker-compose exec app bash
   ```
2. Run the following commands to initialize and migrate the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

#### **Database Information**
- The application uses a SQLite database, which is stored at `instance/app.db`.

---

## Key Features
- **Authentication**:
  - JWT-based API authentication.
  - Session-based authentication for web views.
- **Dynamic Views**:
  - Uses Jinja templates for dynamic rendering of HTML pages.
- **Static Resources**:
  - Tailwind CSS for modern and responsive design.
- **Testing**:
  - Comprehensive unit tests for both API and views.
- **Docker Support**:
  - Easily deployable using Docker and Docker Compose.

---

## Getting Started

### **Prerequisites**
Ensure you have the following installed on your system:
- Python 3.7+
- pip (Python package manager)
- Docker and Docker Compose

### **Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set up a virtual environment** (optional for local development):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application locally**:
   ```bash
   flask run
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

---

## Screenshots

### Login Page
![Login Page](https://images.edgardoponce.com/flask-python-tailwind-example/login.png)

### List Persons Page
![List Persons Page](https://images.edgardoponce.com/flask-python-tailwind-example/list.png)

### Create Person Page
![Create Person Page](https://images.edgardoponce.com/flask-python-tailwind-example/create.png)

### Edit Person Page
![Edit Person Page](https://images.edgardoponce.com/flask-python-tailwind-example/edit.png)

---

## Future Improvements
- Add role-based access control for user management.
- Implement CI/CD pipelines for automated testing and deployment.
- Enhance styling with additional Tailwind components.

---

## Contributing
If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For any questions or support, please contact [your-email@example.com].

---

## Happy Coding! 😊🚀🎉

