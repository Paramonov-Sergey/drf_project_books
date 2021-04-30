from django.contrib import admin

from store.models import *


class BookAdmin(admin.ModelAdmin):
    pass

class UserBookRelationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(UserBookRelation, UserBookRelationAdmin)
