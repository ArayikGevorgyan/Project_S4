# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librarymanagement.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librarymanagement.settings')

    # 🚨 Force logout by deleting all session data
    try:
        import django
        django.setup()  # Required before using ORM in manage.py
        from django.contrib.sessions.models import Session
        Session.objects.all().delete()
        print("✅ All sessions deleted. All users will be logged out.")
    except Exception as e:
        print("⚠️ Could not delete sessions:", type(e).__name__, e)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
