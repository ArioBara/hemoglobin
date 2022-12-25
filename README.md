# hemoglobin
git clone https://github.com/ArioBara/project_kpl.git

cd project_kpl

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
