# Project Management App

This is a project management tool that allows teams to collaborate on projects.

## Prerequisites

- Python 3.x installed on your system.
- Django framework installed (`pip install django`).

## Getting Started

Follow these steps to get the Django project up and running on your local machine.

1. Clone the repository:

    ```bash
    git clone https://github.com/AhteshamUddowla/Project-Management-App.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Perform database migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the project in your web browser at `http://localhost:8000`.

# Authentication
All endpoints in this API require authentication using JWT (JSON Web Token). Include the access token in the Authorization header of your HTTP request as follows:
```bash
Authorization: Bearer youraccesstoken
```

# API Endpoints

## User Endpoints
### Register User 
- **URL:** http://localhost:8000/api/users/register/
- **Method:** `POST`
- **Description:** Create a new user.
- **Request Body:**
    ```bash
    {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword",
        "first_name": "Test",
        "last_name": "User"
    }
    ```
- **Response:**
  ```bash
  {
    "id": 1,
    "username": "testuser",
    "email": "testuser@example.com",
    "first_name": "Test",
    "last_name": "User",
    "date_joined": "2024-06-28T18:14:40.706020Z"
  }
  ```

### Login User 
- **URL:** http://localhost:8000/api/users/token/
- **Method:** `POST`
- **Description:** Authenticate a user and return a JWT token.
- **Request Body:**
    ```bash
    {
        "username": "testuser",
        "password": "testpassword"
    }
    ```
- **Response:**
  ```bash
    {
        "refresh": "yourrefreshtoken",
        "access": "youraccesstoken"
    }
  ```

### Get User Details
- **URL:** http://localhost:8000/api/users/{id}/
- **Method:** `GET`
- **Description:** Retrieve details of a specific user.
- **Response:**
  ```bash
    {
        "id": 1,
        "username": "testuser",
        "email": "testuser@example.com",
        "first_name": "Test",
        "last_name": "User",
        "date_joined": "2024-06-28T18:14:40.706020Z"
    }
  ```

### Update User
- **URL:** http://localhost:8000/api/users/{id}/
- **Method:** `PUT`, `PATCH`
- **Description:** Update user details.
- **Request Body (example for PATCH):**
    ```bash
    {
        "first_name": "UpdatedName"
    }
    ```
- **Response:**
  ```bash
    {
        "id": 1,
        "username": "testuser",
        "email": "testuser@example.com",
        "first_name": "UpdatedName",
        "last_name": "User",
        "date_joined": "2024-06-28T18:14:40.706020Z"
    }
  ```

### Delete User
- **URL:** http://localhost:8000/api/users/{id}/
- **Method:** `DELETE`
- **Description:** Delete a user account.
- **Response:** `204 No Content`

## Project Endpoints
### List Project 
- **URL:** http://localhost:8000/api/projects/
- **Method:** `GET`
- **Description:** Retrieve a list of all projects.
- **Response:**
  ```bash
  [
    {
        "id": 1,
        "name": "Project 1",
        "description": "Project 1 description",
        "owner": 1,
        "created_at": "2024-06-28T18:20:40.706020Z"
    },
    ...
  ]
  ```

### Create Project
- **URL:** http://localhost:8000/api/projects/
- **Method:** `POST`
- **Description:** Create a new project.
- **Request Body:**
  ```bash
  {
    "name": "New Project",
    "description": "New Project Description"
  }
  ```
- **Response:**
  ```bash
  {
    "id": 2,
    "name": "New Project",
    "description": "New Project Description",
    "owner": 1,
    "created_at": "2024-06-28T18:24:40.798356Z"
  }
  ```

### Retrieve Project
- **URL:** http://localhost:8000/api/projects/{id}/
- **Method:** `GET`
- **Description:** Retrive a project.
- **Response:**
  ```bash
  {
    "id": 2,
    "name": "New Project",
    "description": "New Project Description",
    "owner": 1,
    "created_at": "2024-06-28T18:57:18.798356Z"
  }
  ```
  
### Update Project
- **URL:** http://localhost:8000/api/projects/{id}/
- **Method:** `PUT`, `PATCH`
- **Description:** Update project details.
- **Request Body (example for PATCH):**
    ```bash
    {
        "name": "New Project (Updated)"
    }
    ```
- **Response:**
  ```bash
    {
        "id": 2,
        "name": "New Project (Updated)",
        "description": "New Project Description",
        "owner": 1,
        "created_at": "2024-06-28T18:57:18.798356Z"
    }
  ```

### Delete Project
- **URL:** http://localhost:8000/api/project/{id}/
- **Method:** `DELETE`
- **Description:** Delete a project.
- **Response:** `204 No Content`

## Task Endpoints
### Task List
- **URL:** http://localhost:8000/api/projects/{project_id}/tasks/
- **Method:** `GET`
- **Description:** Retrieve a list of all tasks in a project.
- **Response:**
  ```bash
  [
    {
        "id": 1,
        "title": "Task 1",
        "description": "Task 1 Description",
        "status": "To Do",
        "priority": "High",
        "assigned_to": 1,
        "project": 1,
        "created_at": "2024-06-29T05:02:33.513437Z",
        "due_date": "2024-06-29T00:00:00Z"
    },
    ...
  ]
  ```

### Create Task
- **URL:** http://localhost:8000/api/projects/{project_id}/tasks/
- **Method:** `POST`
- **Description:** Create a new task in a project.
- **Request Body:**
  ```bash
  {
    "title": "Task 2",
    "description": "Task 2 description",
    "status": "To Do",
    "priority": "High",
    "assigned_to": "1",
    "due_date": "2024-06-29T00:00:00Z"
  }
  ```
- **Response:**
  ```bash
  {
    "id": 2,
    "title": "Task 2",
    "description": "Task 2 description",
    "status": "To Do",
    "priority": "High",
    "assigned_to": 1,
    "project": 1,
    "created_at": "2024-06-29T05:42:34.729806Z",
    "due_date": "2024-06-29T00:00:00Z"
  }
  ```

### Retrieve Task
- **URL:** http://localhost:8000/api/tasks/{id}/
- **Method:** `GET`
- **Description:** Retrieve details of a specific task.
- **Response:**
  ```bash
  {
    "id": 2,
    "title": "Task 2",
    "description": "Task 2 description",
    "status": "To Do",
    "priority": "High",
    "assigned_to": 1,
    "project": 1,
    "created_at": "2024-06-29T05:42:34.729806Z",
    "due_date": "2024-06-29T00:00:00Z"
  }
  ```
  
### Update Task
- **URL:** http://localhost:8000/api/tasks/{id}/
- **Method:** `PUT`, `PATCH`
- **Description:** Update task details.
- **Request Body (example for PATCH):**
    ```bash
    {
        "status": "In Progress"
    }
    ```
- **Response:**
  ```bash
    {
        "id": 2,
        "title": "Task 2",
        "description": "Task 2 description",
        "status": "In Progress",
        "priority": "High",
        "assigned_to": 1,
        "project": 1,
        "created_at": "2024-06-29T05:42:34.729806Z",
        "due_date": "2024-06-29T00:00:00Z"
    }
  ```

### Delete Project
- **URL:** http://localhost:8000/api/tasks/{id}/
- **Method:** `DELETE`
- **Description:** Delete a task.
- **Response:** `204 No Content`

## Comment Endpoints
### Comment List
- **URL:** http://localhost:8000/api/tasks/{task_id}/comments/
- **Method:** `GET`
- **Description:** Retrieve a list of all comments on a task.
- **Response:**
  ```bash
  [
    {
        "id": 1,
        "content": "This is a comment",
        "user": 1,
        "task": 1,
        "created_at": "2024-06-29T00:00:00Z"
    },
    ...
  ]
  ```

### Create Comment
- **URL:** http://localhost:8000/api/tasks/{task_id}/comments/
- **Method:** `POST`
- **Description:** Create a new comment on a task.
- **Request Body:**
  ```bash
  {
    "content": "This is a comment"
  }
  ```
- **Response:**
  ```bash
  {
    "id": 1,
    "content": "This is a comment",
    "user": 1,
    "task": 1,
    "created_at": "2024-06-29T00:00:00Z"
  }
  ```

### Retrieve Comment
- **URL:** http://localhost:8000/api/comments/{id}/
- **Method:** `GET`
- **Description:** Retrieve details of a specific comment.
- **Response:**
  ```bash
     {
        "id": 1,
        "content": "This is a comment",
        "user": 1,
        "task": 1,
        "created_at": "2024-06-29T00:00:00Z"
    }
  ```
  
### Update Comment
- **URL:** http://localhost:8000/api/comments/{id}/
- **Method:** `PUT`, `PATCH`
- **Description:** Update comment details.
- **Request Body (example for PATCH):**
    ```bash
    {
        "content": "Updated comment"
    }
    ```
- **Response:**
  ```bash
    {
        "id": 1,
        "content": "Updated comment",
        "user": 1,
        "task": 1,
        "created_at": "2024-06-29T00:00:00Z"
    }
  ```

### Delete Comment
- **URL:** http://localhost:8000/api/comments/{id}/
- **Method:** `DELETE`
- **Description:** Delete a comment.
- **Response:** `204 No Content`
  
