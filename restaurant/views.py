from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import MenuItem, Booking
from .serializers import MenuItemSerialier, BookingSerializer
from rest_framework.permissions import IsAuthenticated


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerialier

class SingleMenuItemView(
    generics.RetrieveUpdateAPIView, 
    generics.DestroyAPIView
):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerialier


def index(request):
    return render(request, 'index.html', {})