# Library Management App

This is a Django-based application for managing a library, allowing users to view, borrow, and comment on available books.

## Features

- Manage books, authors, and categories
- Borrow books with user authentication
- Add reviews and ratings for books
- Swagger-based API documentation
- **Pagination, Filtering, and Ordering support for selected endpoints**
- JWT-based authentication for securing API endpoints
- Permissions and role management for access control
- Object-level permissions for enhanced security
- Password policy enforcement for user accounts
- Throttling to prevent brute-force attacks
- One Time Password (OTP) for two-factor authentication

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/dhia1599/django-library-app.git
    ```

2. Navigate into the project directory:

    ```bash
    cd django-library-app
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

- Access to home page at `/`.
- Access the admin panel at `/admin/`.
- API documentation is available at `/swagger/`.
- JWT Authentication is required for accessing most API endpoints.


## API Features

### Pagination

The API supports pagination on the following endpoints:
- **Evaluations (`/api/evaluations/`)**: Returns 5 evaluations per page.

You can navigate through pages by adding the `?page` parameter to the URL. Example:

```plaintext
GET /api/livres/?page=2
```

### Filtering

You can filter the results on some endpoints using query parameters.

#### Books Endpoint (`/api/livres/`):
You can filter books by:
- **Category** (`categorie`)
- **Language** (`langue`)

Examples:
- Filter by category (category ID = 1):  
  ```plaintext
  GET /api/livres/?categorie=1
  ```

### Ordering

You can order results on the **Evaluations** endpoint (`/api/evaluations/`) by:
- **Evaluation Date** (`date_evaluation`)
- **Rating** (`note`)

**Examples:**
- Order by evaluation date (ascending):
  ```plaintext
  GET /api/evaluations/?ordering=date_evaluation
  ```


## Security Features

### 1. JWT Authentication

The application uses **JWT (JSON Web Tokens)** for user authentication. All API endpoints are secured and require a valid JWT token to be accessed.

### 2. Password Policy

Password policy has been enforced to enhance security:

### 3. Throttling

Throttling is implemented to prevent brute-force attacks on the authentication endpoint:

- A user is limited to **5 requests every 5 seconds** on the authentication endpoint.
- If the limit is exceeded, the user will be temporarily blocked from making further requests.

### 4. One Time Password (OTP)

The application also supports **One Time Password (OTP)** for an additional layer of security during user authentication.

### 5. Role-Based

- **Role-Based Permissions**: Different roles (e.g., admin, reader) are assigned different permissions for accessing specific API endpoints.
