

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_ci_example.settings.dev")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
