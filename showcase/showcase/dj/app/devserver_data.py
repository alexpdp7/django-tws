from django.contrib.auth import models as auth_models
from django_tws import users
from showcase.dj.app import models

admin = users.user_manager().create_superuser("admin", password="admin")
staff1 = users.user_manager().create_user("staff1", password="staff1", is_staff=True)
staff2 = users.user_manager().create_user("staff2", password="staff2", is_staff=True)
user1 = users.user_manager().create_user("user1", password="user1")
user2 = users.user_manager().create_user("user2", password="user2")

group1 = auth_models.Group(name="group1")
group1.save()

for permission in ['add_userrestrictedmodel', 'change_userrestrictedmodel', 'delete_userrestrictedmodel', 'view_userrestrictedmodel']:
    permission = auth_models.Permission.objects.get(codename=permission)
    group1.permissions.add(permission)

group1.user_set.add(staff1)
group1.user_set.add(staff2)

models.UserRestrictedModel(field="only viewable by admin or superusers", user=admin).save()
models.UserRestrictedModel(field="only viewable by staff1 or superusers", user=staff1).save()
models.UserRestrictedModel(field="only viewable by staff2 or superusers", user=staff2).save()
