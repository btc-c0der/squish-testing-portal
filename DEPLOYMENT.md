# Deployment Guide

## Development Server (Current Setup)

The current setup runs a development server suitable for learning and testing.

### Quick Start
```bash
# Make scripts executable (first time only)
chmod +x setup.sh run.sh

# Setup (first time only)
./setup.sh

# Run the application
./run.sh
```

## Production Deployment

For production deployment, consider these options:

### Option 1: Using Gunicorn (Recommended)

1. **Install Gunicorn:**
   ```bash
   pip install gunicorn
   ```

2. **Create a WSGI entry point (`wsgi.py`):**
   ```python
   from app import app
   
   if __name__ == "__main__":
       app.run()
   ```

3. **Run with Gunicorn:**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
   ```

### Option 2: Using uWSGI

1. **Install uWSGI:**
   ```bash
   pip install uwsgi
   ```

2. **Create uWSGI configuration (`uwsgi.ini`):**
   ```ini
   [uwsgi]
   module = wsgi:app
   master = true
   processes = 4
   socket = squish-portal.sock
   chmod-socket = 660
   vacuum = true
   die-on-term = true
   ```

3. **Run with uWSGI:**
   ```bash
   uwsgi --ini uwsgi.ini
   ```

### Option 3: Docker Deployment

1. **Create Dockerfile:**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   RUN python3 -c "from app import app, db; app.app_context().push(); db.create_all()"
   
   EXPOSE 5000
   
   CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app"]
   ```

2. **Build and run:**
   ```bash
   docker build -t squish-portal .
   docker run -p 5000:5000 squish-portal
   ```

### Nginx Configuration (Optional)

For better performance, you can use Nginx as a reverse proxy:

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /static/ {
        alias /path/to/your/app/static/;
    }
}
```

## Environment Variables

For production, set these environment variables:

```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key-here
export DATABASE_URL=sqlite:///production.db
```

## Security Considerations

1. **Change the secret key** in `app.py`
2. **Use HTTPS** in production
3. **Set up proper database** (PostgreSQL recommended)
4. **Enable logging** for monitoring
5. **Set up regular backups**

## Monitoring

Consider adding:
- Application monitoring (e.g., Sentry)
- Performance monitoring (e.g., New Relic)
- Log aggregation (e.g., ELK stack)
- Health checks and uptime monitoring
