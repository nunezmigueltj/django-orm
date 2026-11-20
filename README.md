# Django ORM Practice

## Overview

This project focuses on learning and practicing Django through a practical inventory management application.

The main goal is to strengthen Python backend development skills by working with Django models, database relationships, ORM queries, and query optimization.

The project uses a simple inventory system to simulate real-world database operations.

## Technologies

- Python
- Django
- SQLite
- Django ORM
- Git and GitHub

## Project Structure

```text
django-orm/
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── inventory/
│   ├── migrations/
│   ├── models.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── views.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## Database Structure

The application currently contains two main models:

### Categoria

Stores product categories.

- nombre

### Producto

Stores inventory products.

- nombre
- precio
- stock
- categoria (ForeignKey)

### Relationships

- One category can have multiple products.
- Each product belongs to one category.
- The relationship is implemented using Django's ForeignKey field.

## Topics Covered

- Django project and application structure.
- Virtual environments and dependency management.
- Django models.
- Database migrations.
- ForeignKey relationships.
- Django ORM fundamentals.
- QuerySets.
- Filtering and excluding records.
- Ordering query results.
- Related object lookups.
- `filter()`, `exclude()`, `get()` and `exists()`.
- `select_related()` for query optimization.
- Understanding the N+1 query problem.

## ORM Practice

The project includes practical exercises involving:

- Retrieving all products.
- Filtering products by price and stock.
- Searching products using `icontains`.
- Ordering products by price.
- Excluding products based on category.
- Accessing related objects.
- Checking for existing records.
- Optimizing queries using `select_related()`.

## Project Setup

1. Clone the repository:

```bash
git clone https://github.com/nunezmigueltj/django-orm.git
```

2. Navigate to the project directory:

```bash
cd django-orm
```

3. Create and activate a virtual environment:

```bash
py -m venv .venv
.venv\Scripts\activate
```

4. Install dependencies:

```bash
py -m pip install -r requirements.txt
```

5. Apply database migrations:

```bash
py manage.py migrate
```

6. Start the development server:

```bash
py manage.py runserver
```

## Progress

**Status: In Progress**

Currently completed:

- Django project setup.
- Inventory application creation.
- Category and Product models.
- Database migrations.
- Sample data insertion.
- ForeignKey relationships.
- Basic Django ORM queries.
- Related object lookups.
- Query optimization with `select_related()`.

## Purpose

This project is part of my continuous learning process to strengthen my Python backend development skills and gain practical experience building database-driven applications with Django.