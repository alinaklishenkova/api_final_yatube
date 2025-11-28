#!/c/Dev/api_final_yatube/venv311/Scripts/python.exe
# When the django-admin.py script is run, it automatically finds
# the 'django' package in the virtual environment
import sys
import os

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "yatube_api.settings"
    )
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
