from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerialier, BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerialier

class SingleMenuItemView(
    generics.RetrieveUpdateAPIView, 
    generics.DestroyAPIView
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerialier


def index(request):
    return render(request, 'index.html', {})