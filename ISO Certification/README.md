# ACS-GP ISO Certification Website

A modern, responsive Django website for ISO certification services with professional design and custom CSS styling.

## Features

- **Modern Design**: Professional, responsive layout with custom CSS animations
- **ISO Certifications**: Comprehensive certification information and details
- **Contact System**: Full contact page with form and FAQ
- **About Us**: Detailed company information and team profiles
- **Responsive**: Mobile-first design that works on all devices
- **Custom Styling**: Beautiful animations and transitions

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or Download the Project**
   ```bash
   # If using Git
   git clone <repository-url>
   cd ISO-Certification
   
   # Or simply download and extract the folder
   ```

2. **Create Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```bash
   # Run migrations
   python manage.py migrate
   
   # Create superuser (optional)
   python manage.py createsuperuser
   
   # Populate certificate data
   python manage.py populate_certificates
   ```

5. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Website**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
ISO-Certification/
├── certificates/          # Certificate app
│   ├── management/        # Custom management commands
│   ├── migrations/        # Database migrations
│   ├── models.py         # Certificate models
│   └── views.py          # Certificate views
|
├── main/                 # Main app
│   ├── migrations/       # Database migrations
│   ├── models.py        # Main models
│   └── views.py         # Main views
|
├── iso_website/         # Django project settings
│   ├── settings.py      # Project settings
│   └── urls.py         # Main URL configuration
|
├── static/              # Static files
│   ├── css/            # Custom CSS files
│   ├── images/         # Images
│   └── js/             # JavaScript files
|
├── templates/           # HTML templates
│   ├── components/     # Reusable components
│   ├── main/          # Main page templates
│   └── certificates/  # Certificate templates
|
├── requirements.txt    # Python dependencies
└── manage.py          # Django management script
```

## Dependencies

- **Django 5.2.6**: Web framework
- **Pillow 10.4.0**: Image processing
- **django-tailwind 3.6.0**: Tailwind CSS integration
- **whitenoise 6.8.2**: Static file serving
- **django-crispy-forms 2.3**: Form styling

## Customization

### Adding New Certificates

1. Go to Django Admin: `http://127.0.0.1:8000/admin/`
2. Navigate to "Certificates" section
3. Add new certificate with all required fields
4. The certificate will automatically appear on the website

### Styling Changes

- Main CSS file: `static/css/animations.css`
- All custom styles are in this file
- No Tailwind classes are used - everything is custom CSS

### Content Updates

- **Home Page**: Edit templates in `templates/components/`
- **About Page**: Edit `templates/main/about.html`
- **Contact Page**: Edit `templates/main/contact.html`
- **Certificate Pages**: Edit `templates/certificates/`

## Production Deployment

For production deployment, you'll need to:

1. Set `DEBUG = False` in `settings.py`
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving
4. Configure domain and SSL
5. Set up proper logging

## Support

For technical support or questions about this project, please contact the development team.

## License

This project is proprietary software. All rights reserved.