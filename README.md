# Django ORM & Backend Development

## Overview

This project implements a Django-based inventory application focused on backend development, relational data modeling, and database operations through Django ORM.

It covers model design, database relationships, data retrieval, query filtering, and query optimization using practical inventory management scenarios.

## Technologies

- Python
- Django
- SQLite
- Django ORM
- Git and GitHub

## Application Structure

The application currently contains an inventory module with two main models:

### Categoria

Stores product category information.

- nombre

### Producto

Stores inventory product information.

- nombre
- precio
- stock
- categoria (ForeignKey)

### Database Relationships

- One category can have multiple products.
- Each product belongs to one category.
- The relationship is implemented using Django's ForeignKey field.

## Technical Implementation

The project covers the following areas:

- Django project and application architecture.
- Virtual environments and dependency management.
- Django models and database migrations.
- Relational data modeling.
- ForeignKey relationships.
- Django ORM and QuerySets.
- Data filtering and exclusion.
- Object retrieval and existence checks.
- Query ordering.
- Related object lookups.
- Query optimization using `select_related()`.
- N+1 query problem and performance considerations.

## ORM Operations

The application includes implementations involving:

- Retrieving records using `all()`.
- Filtering records using `filter()`.
- Excluding records using `exclude()`.
- Retrieving individual objects using `get()`.
- Checking record existence using `exists()`.
- Searching text using `icontains`.
- Filtering related models.
- Accessing reverse relationships using `related_name`.
- Optimizing ForeignKey queries using `select_related()`.

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

## Project Status

**Status: In Progress**

Currently implemented:

- Django project configuration.
- Inventory application.
- Category and Product models.
- Database migrations.
- ForeignKey relationships.
- Sample data management.
- Django ORM queries.
- Related object lookups.
- Query optimization with `select_related()`.

## Purpose

This project demonstrates practical backend development concepts using Django, with an emphasis on database-driven application development, ORM operations, and query performance.

It provides a foundation for implementing more advanced backend features and expanding the application's functionality.