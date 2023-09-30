from zones.models import Supplier, Service, Zone
from zones.serializers import SupplierSerializer, ServiceSerializer, ZoneSerializer
from rest_framework import viewsets
from django.contrib.gis.geos import GEOSGeometry

def get_model_queryset(request, model):
    lat = request.GET.get('lat') 
    lng = request.GET.get('lng')
    if lat and lng:
        pnt = GEOSGeometry('POINT({} {})'.format(lat, lng))
        if model == Zone:
            return model.objects.filter(zone__contains=pnt)
        else:
            return model.objects.filter(zones__zone__contains=pnt).distinct()
    return model.objects.all()

class SupplierViewSet(viewsets.ModelViewSet):
    #queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
    def get_queryset(self):
        # lat = self.request.GET.get('lat') 
        # lng = self.request.GET.get('lng')
        # if lat and lng:
        #     pnt = GEOSGeometry('POINT({} {})'.format(lat, lng))
        #     return Supplier.objects.filter(zone__zone__contains=pnt).distinct()
        # return Supplier.objects.all()
        return get_model_queryset(self.request, Supplier)


class ServiceViewSet(viewsets.ModelViewSet):
    #queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        # lat = self.request.GET.get('lat') 
        # lng = self.request.GET.get('lng')
        # if lat and lng:
        #     pnt = GEOSGeometry('POINT({} {})'.format(lat, lng))
        #     return Service.objects.filter(zone__zone__contains=pnt).distinct()
        # return Service.objects.all()
        return get_model_queryset(self.request, Service)


class ZoneViewSet(viewsets.ModelViewSet):
    #queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

    def get_queryset(self):
        # lat = self.request.GET.get('lat') 
        # lng = self.request.GET.get('lng')
        # if lat and lng:
        #     pnt = GEOSGeometry('POINT({} {})'.format(lat, lng))
        #     return Zone.objects.filter(zone__contains=pnt)
        # return Zone.objects.all()
        return get_model_queryset(self.request, Zone)


