from rest_framework import serializers
from .models import Barrios, Personas, Localcomida, Localrepuestos

class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barrios
        fields = "__all__"
class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personas
        fields = "__all__"
class LocalesComidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Localcomida
        fields = "__all__"
class LocalesRepuestosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Localrepuestos
        fields = "__all__"

