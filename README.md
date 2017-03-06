# Validate Credit Card #

Web application to validate credit card numbers.


## Instructions

### Requirements

- Linux/MacOS
- Git
- Python 3.5.2

### Instalation

Run the following commands on your terminal:

```bash
$ git clone git@github.com:mazulo/validate_credit_card.git
$ cd validate_credit_card
$ pip install -r requirements.txt
$ python manage.py migrate
```

and then...

### Run the server

```bash
$ ./manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
March 06, 2017 - 13:10:27
Django version 1.10.5, using settings 'settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### How to use

You can use it by access `http://127.0.0.1:8000/` or accessing the online version: https://validate-credit-card.herokuapp.com/

### Tests

To run the tests:

```bash
python manage.py test backend
```
