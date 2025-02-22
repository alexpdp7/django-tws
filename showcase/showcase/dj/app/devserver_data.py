from django_tws import users

users.user_manager().create_superuser("admin", password="admin")

