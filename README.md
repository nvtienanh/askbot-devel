
# Install
```console
source pyvenv/Scripts/activate

python -m pip install --upgrade pip
pip install -r askbot_requirements.txt
pip install psycopg2
python setup.py develop
askbot-setup 
python manage.py migrate
python manage.py runserver 0.0.0.0:8000  --insecure
SECRET_KEY=whatever DJANGO_SETTINGS_MODULE=askbot_app.settings python manage.py collectstatic --noinput
```

export DB_TYPE=postgres
export DB_USER=askbot
export DB_PASS=askB0T
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=askbotfortox
export DATABASE_URL="postgres://askbot:askB0T@localhost:5432/askbotfortox"
askbot-setup -r ./askbot_app -e 1 -d askbotfortox -u askbot -p askB0T --db-host=localhost --db-port=5432 --logfile-name=stdout --no-secret-key --create-project container-uwsgi
SECRET_KEY=whatever DJANGO_SETTINGS_MODULE=askbot_site.settings python manage.py collectstatic --noinput
SECRET_KEY=whatever DJANGO_SETTINGS_MODULE=askbot_site.settings DEBUG_MODE=True python manage.py runserver 0.0.0.0:8000  --insecure

# Mapping

| Q & A       | Boom          |
| ----------- | ------------- |
| question    | phone-number  |
| questions   | phone-numbers |
| ask         | report        |
| asks        | reports       |
| answer      | feedback      |
| answers     | feedbacks     |

