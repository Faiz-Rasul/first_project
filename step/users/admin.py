from django.contrib import admin
from .models import OtherRequests, UserInfo, AvailableCourses, Enrollment, Fees, Voting,  UserVotes

# Register your models here.


admin.site.register(OtherRequests)
admin.site.register(UserInfo)
admin.site.register(AvailableCourses)
admin.site.register(Enrollment)
admin.site.register(Fees)
admin.site.register(Voting)
admin.site.register(UserVotes)


