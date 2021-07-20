# setup

---

If docker is available run `docker-compose up`

If docker is unavailable run:

- `pip3 install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py generate_data`
- `python manage.py runserver`

After all is initiated the app can be opened on [localhost:8000](localhost:8000)
