# hemoglobin
# CARA PAKAI:
git clone https://github.com/ArioBara/hemoglobin.git

cd hemoglobin

python -m venv .venv

.venv\Scripts\activate

pip install -r requirement.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
