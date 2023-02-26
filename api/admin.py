from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.PostTable)
admin.site.register(models.post_Likes)
admin.site.register(models.post_Comments)
admin.site.register(models.Lost_Found)
admin.site.register(models.LST_Comments)
admin.site.register(models.Events)
admin.site.register(models.Event_likes)
admin.site.register(models.Alerts)
#admin.site.register(models.Alerts_Comments)
admin.site.register(models.Clubs_Sports)
#admin.site.register(models.Clubs_Sports_files)
admin.site.register(models.Mess_table)
admin.site.register(models.Academic_table)
admin.site.register(models.Time_table)



