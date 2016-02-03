"""
WSGI config for write project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/

http://www.cnblogs.com/haozi0804/p/4729199.html
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "write.settings")

application = get_wsgi_application()
