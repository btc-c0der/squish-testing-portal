# Railway Deployment Guide

## Deploy Squish Testing Portal to Railway

### Prerequisites
- GitHub repository with your code
- Railway account (https://railway.app)

### Deployment Steps

1. **Connect to Railway:**
   - Go to https://railway.app
   - Sign in with your GitHub account
   - Click "New Project"

2. **Deploy from GitHub:**
   - Select "Deploy from GitHub repo"
   - Choose your repository: `btc-c0der/squish-testing-portal`
   - Railway will automatically detect the Flask app

3. **Environment Variables (Optional):**
   - In Railway dashboard, go to Variables tab
   - Add `SECRET_KEY` with a secure random string
   - Add `DATABASE_URL` if you want to use PostgreSQL (Railway provides free PostgreSQL)

4. **Deploy:**
   - Railway will automatically build and deploy your app
   - The deployment will use the `Procfile` and `requirements.txt`

### Configuration Files

- `Procfile`: Tells Railway how to run your app (`web: gunicorn app:app`)
- `requirements.txt`: Lists all Python dependencies including gunicorn
- `app.py`: Configured to read PORT from environment variables

### Features for Railway Deployment

- **Automatic Scaling**: Railway handles scaling based on traffic
- **Custom Domain**: You can add your own domain
- **SSL/HTTPS**: Automatic SSL certificates
- **Database**: Free PostgreSQL database available
- **Logs**: Real-time application logs
- **GitHub Integration**: Auto-deploy on push to main branch

### Post-Deployment

1. Your app will be available at: `https://your-app-name.railway.app`
2. Test all features to ensure they work correctly
3. Monitor logs for any issues
4. Set up custom domain if needed

### Troubleshooting

- Check Railway logs if deployment fails
- Ensure all dependencies are in requirements.txt
- Verify PORT environment variable is used correctly
- Check that gunicorn is installed and working

### Database Notes

- The app uses SQLite by default (file-based)
- For production, consider using Railway's PostgreSQL
- Database will be initialized automatically on first run
- Sample data will be populated if tables are empty
