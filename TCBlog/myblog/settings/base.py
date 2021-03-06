"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'blog.apps.BlogConfig',  # 将自己创建的app添加到设置中
    'read_statistics.apps.ReadStatisticsConfig',  # 注册阅读统计app
    'comment.apps.CommentConfig',  # 注册评论
    'likes.apps.LikesConfig',  # 注册点赞
    'user.apps.UserConfig',  # 用户相关
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blog.middleware.mymiddleware.My404',  # 添加自己的中间件
]

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'user.context_processors.login_model_form',  # 自定义模板变量，直接用模板语言调用
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# 语言
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
# 时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 不考虑时区
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 配置ckeditor
CKEDITOR_UPLOAD_PATH = 'upload/'

# 自定义参数
EACH_PAGE_BLOGS_NUMBER = 7

# 设置数据库缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_read_num_cache_table',
    }
}

# ckeditor 代码高亮,以及公式
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'tabSpaces': 4,
        'mathJaxLib': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML',
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print',
             'SpellChecker', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat',
             '-', 'Maximize', 'ShowBlocks', '-', "CodeSnippet", 'Mathjax', 'Subscript',
             'Superscript'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button',
             'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar',
             'PageBreak'], ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],),
        'extraPlugins': ','.join([
            'codesnippet',
            'mathjax',
            'dialog',
            'dialogui',
            'lineutils',
        ]),
    },
    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['TextColor', 'BGColor', 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ['Smiley', 'SpecialChar', 'Blockquote'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpace': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    }
}
