# Portfolio

Website with an admin panel for web developers to showcase their experience, projects, and skills. Built with Django and Docker.

### Dev setup

```
docker-compose down -v
docker-compose up -d --build
docker-compose exec web python manage.py createsuperuser
```

### Prod setup

```
sudo docker compose down -v
sudo docker compose -f docker-compose.prod.yml up -d --build
sudo docker compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
sudo docker compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
sudo docker compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```
