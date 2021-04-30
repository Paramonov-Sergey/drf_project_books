
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from store.views import UserBookRelationView, BookViewSet

urlpatterns=[

]
router=SimpleRouter()
router.register(r'book',BookViewSet)
router.register(r'book_relation',UserBookRelationView)
urlpatterns+=router.urls