# Library Management App

This is a Django-based application for managing a library, allowing users to view, borrow, and comment on available books.

## Features

- Manage books, authors, and categories
- Borrow books with user authentication
- Add reviews and ratings for books
- Swagger-based API documentation
- **Pagination, Filtering, and Ordering support for selected endpoints**

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/dhia1599/django-library-app.git
    ```

2. Navigate into the project directory:

    ```bash
    cd django-library-app
    ```

3. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

- Access to home page at `/`.
- Access the admin panel at `/admin/`.
- API documentation is available at `/swagger/`.


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


## Custom Permissions

### IsAdminOrReadOnly
- **Description**: 
  - Cette permission permet uniquement aux utilisateurs authentifiés appartenant au groupe **admin** d'accéder aux endpoints en écriture (POST, PUT, DELETE).
  - Les utilisateurs sans cette permission ne peuvent pas modifier, créer ou supprimer des données.

### IsOwnerOrReadOnly
- **Description**:
  - Cette permission permet aux utilisateurs du groupe **lecteur** de lire des ressources (GET, HEAD, OPTIONS), mais empêche toute modification des ressources (POST, PUT, PATCH, DELETE).


