from django.db.models import Count, Case, When, Avg, Value, CharField
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, renderers, permissions, status, mixins
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

from store.models import *
from store.permissions import IsOwnerOrReadOnly
from store.serializers import *


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().annotate(annotated_likes=Count(Case(
        When(userbookrelation__like=True, then=1)))).select_related('owner').prefetch_related('readers')



    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        """Второй способ"""
        # serializer.cleaned_data['owner']=self.request.user
        # serializer.save()


def auth(request):
    return render(request, 'oauth.html')


class UserBookRelationView(GenericViewSet, mixins.UpdateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserBookRelationSerializer
    queryset = UserBookRelation.objects.all()
    lookup_field = 'book'

    def get_object(self):
        obj, created = UserBookRelation.objects.get_or_create(user=self.request.user, book_id=self.kwargs['book'])
        print('created', created)

        return obj
