# -*- coding: utf-8 -*-
"""
WSGI config for iTechSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/


"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iTechSite.settings")
from django.contrib.auth.handlers.modwsgi import check_password, groups_for_user
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

