from django.shortcuts import render
from .serializer import BooksSerializer
from rest_framework import viewsets, permissions, mixins
from books.models import Books

# permission
class isSubscribed(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.subscribed == True:
            return True

        else:
            return False


# Create your views here.
class BooksViewset(viewsets.ModelViewSet):
    
    queryset = Books.objects.all()[:2]
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllBooksViewset(viewsets.ModelViewSet):
    
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated, isSubscribed]
