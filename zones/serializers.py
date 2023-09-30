from rest_framework import serializers
from zones.models import Supplier, Service, Zone

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    zones = serializers.HyperlinkedRelatedField(many=True, queryset=Zone.objects.all(), view_name='zone-detail')
    #zones = serializers.PrimaryKeyRelatedField(many=True, queryset=Zone.objects.all())
    class Meta:
        model = Supplier
        fields = ['url', 'id', 'title', 'email', 'phone_number', 'address', 'zones']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['url', 'id', 'name']

class ZoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zone
        fields = ['url', 'id', 'name', 'price', 'supplier', 'services', 'zone']