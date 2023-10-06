from django.forms.models import model_to_dict
import pytz
from rest_framework import serializers


from django.utils import timezone

from django.db.models import Max
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import permissions, generics, status
from rest_framework import serializers
from rest_framework import serializers, status
from rest_framework.response import Response

from .models import (Budget, Company, Specification, BikeType, Login, Vehicle,Scodedetail)




class ScodedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scodedetail
        fields ='__all__'


class BikeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeType
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
