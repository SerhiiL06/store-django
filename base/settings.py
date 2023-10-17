from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-t*p^^0a79)8*o#x$8^wa-!y64(krcn22rk&k#e!$u8l6ad5cq$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_email_verification",
    "crispy_forms",
    "crispy_bootstrap5",
    "shop.apps.ShopConfig",
    "account",
    "cart.apps.CartConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "base.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "shop.context_processors.categories",
                "cart.context_processors.cart",
            ],
        },
    },
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


WSGI_APPLICATION = "base.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILESDIRS = [BASE_DIR / "static"]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Users

LOGIN_URL = "account:login"
LOGOUT_REDIRECT_URL = "/"


# Email verification


def email_verified_callback(user):
    user.is_active = True


# def password_change_callback(user, password):
#     user.set_password(password)


# Global Package Settings
EMAIL_FROM_ADDRESS = "noreply@aliasaddress.com"  # mandatory
EMAIL_PAGE_DOMAIN = "http://127.0.0.1:8000/"  # mandatory (unless you use a custom link)
EMAIL_MULTI_USER = False  # optional (defaults to False)

# Email Verification Settings (mandatory for email sending)
EMAIL_MAIL_SUBJECT = "Confirm your email {{ user.username }}"
EMAIL_MAIL_HTML = "account/email/mail_body.html"
EMAIL_MAIL_PLAIN = "account/email/mail_body.txt"
EMAIL_MAIL_TOKEN_LIFE = 60 * 60  # one hour

# Email Verification Settings (mandatory for builtin view)
EMAIL_MAIL_PAGE_TEMPLATE = "account/email/email_success_template.html"
EMAIL_MAIL_CALLBACK = email_verified_callback

# # Password Recovery Settings (mandatory for email sending)
# EMAIL_PASSWORD_SUBJECT = "Change your password {{ user.username }}"
# EMAIL_PASSWORD_HTML = "password_body.html"
# EMAIL_PASSWORD_PLAIN = "password_body.txt"
# EMAIL_PASSWORD_TOKEN_LIFE = 60 * 10  # 10 minutes

# # Password Recovery Settings (mandatory for builtin view)
# EMAIL_PASSWORD_PAGE_TEMPLATE = "password_changed_template.html"
# EMAIL_PASSWORD_CHANGE_PAGE_TEMPLATE = "password_change_template.html"
# EMAIL_PASSWORD_CALLBACK = password_change_callback

# For Django Email Backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "sergiy06061997@gmail.com"
EMAIL_HOST_PASSWORD = "xwnv qxxe jlkx slmq"  # os.environ['password_key'] suggested
EMAIL_USE_TLS = True
