# muzeekdb

```
psql -U postgres
create database muzeekdb;
\q

python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Stack

1. Python
2. Django Rest Framework
3. Swagger
4. PostgreSQL

## Filters

### Artist
- name
- band

**Ordering**
- full_name
- created
- id (default)

**Search**
- full_name
- band__name

---

### Band
- name

---

### Track
- title
- album
- artist
- genre

### Album
- title

## TODOs

- [ ] More `SearchFilter` fields?
- [ ] UI
- [ ] Tests
- [ ] Upload/download views and media organization
- [ ] Admin

### URLs
    localhost:8000/swagger/
    localhost:8000/api/tracks/
    localhost:8000/api/albums/
    localhost:8000/api/bands/
    localhost:8000/api/artists/
