from django.contrib import admin
from showcase.dj.app import models


class UserRestrictedModelAdmin(admin.ModelAdmin):
    raw_id_fields = ["user"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    list_display = ["field", "user"]

    # TODO: has_change_permission


admin.site.register(models.UserRestrictedModel, UserRestrictedModelAdmin)
