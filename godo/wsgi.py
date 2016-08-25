"""
WSGI config for godo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import os
import sys

root_path = os.path.abspath(os.path.split(__file__)[0])
sys.path.insert(0, os.path.join(root_path, 'godo'))
sys.path.insert(0, root_path)


from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
application = get_wsgi_application()
