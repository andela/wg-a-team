#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line
from tasks import (
    setup_django_environment
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":

    # If user passed the settings flag ignore the default wger settings
    if not any('--settings' in s for s in sys.argv):
        setup_django_environment(
            os.path.join(BASE_DIR, "settings.py"))

    # Alternative to above
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    execute_from_command_line(sys.argv)
