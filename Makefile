setup:
	pip install -r requirements.txt
	yarn install --modules-folder frontend/
	python manage.py migrate
