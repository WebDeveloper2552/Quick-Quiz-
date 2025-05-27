AUTH_USER_MODEL = 'your_app.User'

LOGIN_URL = 'login.html'
LOGIN_REDIRECT_URL = 'dashboard.html'  # Will be overridden in views
LOGOUT_REDIRECT_URL = 'index.html'

# Add to middleware:
MIDDLEWARE = [
    # ...
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # ...
]
