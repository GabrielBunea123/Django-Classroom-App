from django.contrib import admin
from .models import Room,Joined,Upload_Task,UploadFiles,Comments,Topic,UploadTaskFiles,Profile
# Register your models here.
admin.site.register(Room)
admin.site.register(Joined)
admin.site.register(Upload_Task)
admin.site.register(UploadFiles)
admin.site.register(Comments)
admin.site.register(Topic)
admin.site.register(UploadTaskFiles)
admin.site.register(Profile)
