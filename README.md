
# Install
source py38/Scripts/activate

pip install -r askbot_requirements.txt

export DB_TYPE=postgres
export DB_USER=askbot
export DB_PASS=askB0T
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=askbotfortox
export DATABASE_URL="postgres://askbot:askB0T@localhost:5432/askbotfortox"
askbot-setup -n ./askbot-site -e 1 -d askbotfortox -u askbot -p askbotPW --db-host=localhost --db-port=5432 --logfile-name=stdout --no-secret-key --create-project container-uwsgi
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

