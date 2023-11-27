# Phone Number Management CRUD

[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-green)](https://www.djangoproject.com/)

A simple CRUD application for managing phone numbers.

## Features

- Create, read, update, and delete phone numbers
- User authentication and login functionality
- Simple and intuitive user interface

## Requirements

- Python 3.9 or higher
- Django 3.2 or higher

## Installation

1. Clone the repository:
```
git clone https://github.com/gitesiek/phonenumber_crud.git
cd phone-number-management
```
2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate
```
3. Install the dependencies:
```
pip install -r requirements.txt
```
4. Apply the database migrations:
```
python manage.py migrate
```
5. Run the development server:
```
python manage.py runserver
```
6. Open your web browser and visit [http://localhost:8000](http://127.0.0.1:8000/) to access the application.


## Usage

1. Register a new account using
  ```
  python manage.py createsuperuser
  ```
2. Log into your account on `http://127.0.0.1:8000/login`
3. Add, edit, or delete phone numbers using the provided forms or by using a bash script that loads them from csv
  ```
  python manage.py shell
  from data_import import import_clinics_from_csv
  import_clinics_from_csv()
  ```
4. View the list of phone numbers on the main page.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more information.

