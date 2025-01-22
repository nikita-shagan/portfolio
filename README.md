# Portfolio

A modern portfolio website featuring an admin panel for web developers to showcase their experience, projects, and skills. Built with Django and Docker.

---

## Features

- **Admin Panel**: Easily manage content, projects, and skills.
- **Responsive Design**: Optimized for desktop and mobile devices.
- **Dockerized Setup**: Streamlined development and production environments.

---

## Development Setup

Follow these steps to set up the development environment:

```bash
docker-compose down -v
docker-compose up -d --build
docker-compose exec web python manage.py createsuperuser
```

---

## Production Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/nikita-shagan/portfolio.git
cd portfolio
```

### Step 2: Configure Environment Variables

Edit the environment files:

```bash
nano .env.prod
nano .env.prod.db
```

Set the appropriate permissions:

```bash
sudo chmod -R 777 .
```

### Step 3: Install Docker

Remove existing Docker packages:

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Update and install Docker:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Step 4: Deploy the Application

Bring down any existing containers and deploy:

```bash
sudo docker compose down -v
sudo docker compose -f docker-compose.prod.yml up -d --build
```

Run migrations and collect static files:

```bash
sudo docker compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
sudo docker compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
sudo docker compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

### Step 5: Configure Nginx

Install and set up Nginx:

```bash
sudo apt update
sudo apt install -y nginx
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
```

Edit the Nginx configuration:

```bash
sudo nano /etc/nginx/sites-available/default
```

Example configuration:

```nginx
server {
    listen 80;
    server_name shagan.pro;

    location / {
        proxy_pass http://localhost:1337;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Test and reload Nginx:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

### Step 6: Set Up SSL

Install and configure Certbot:

```bash
sudo apt update
sudo apt install -y certbot python3-certbot-nginx
sudo systemctl reload nginx
```
