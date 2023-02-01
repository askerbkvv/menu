
git clone “https…..” 

cd “имя проекта, заходите до папки где находиться manage.py”

python -m venv venv

venv\Scripts\activate.bat

---------------------------------------------------------------

-pip install -r requirements.txt

-python manage.py makemigrations

-python manage.py migrate

-python manage.py createsuperuser

-python manage.py runserver