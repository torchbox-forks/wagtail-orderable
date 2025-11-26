# Sandbox

This directory contains a sandbox Wagtail project for testing and development purposes. It includes basic configurations and apps to facilitate testing of the `wagtail-orderable` package.

- Last tested with Wagtail 7.2 and Django 5.2

## Run the sandbox

Set up you virtual environment and install the requirements:

```bash
pip install -e ".[dev]"
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then, you can access the Wagtail admin interface at `http://localhost:8000/admin/`.

## Testing the Orderable Feature

Goto the "Books" section in the admin to test the orderable feature.

Add some book entries and use the drag-and-drop interface to reorder them. The order should be preserved and reflected in the listing.

## Formatting and Linting the Sandbox App

If you make changes to the sandbox app, you can use the following commands to format and lint the code:

```bash
black sandbox/
isort sandbox/
flake8 sandbox/
```
