# hemoglobin
# CARA PAKAI:
<P> git clone https://github.com/ArioBara/hemoglobin.git </P>

cd hemoglobin

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
