```bash
python -m pip install --upgrade pip \
pip install -r /askbot_requirements.txt \
pip install psycopg2
python setup.py develop
askbot-setup
pip uninstall 'django-appconf' && pip install 'django-appconf==1.0.3'
SECRET_KEY=whatever DJANGO_SETTINGS_MODULE=askbot_app.settings python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000 --insecure
```