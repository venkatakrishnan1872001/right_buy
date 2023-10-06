from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
import ast
import copy
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import (Budget,Company,Specification,BikeType,Login,Vehicle,Scodedetail
)


from .serializers import (
    BikeTypeSerializer,SpecificationSerializer,CompanySerializer,BudgetSerializer,VehicleSerializer,ScodedetailSerializer
)


class BikeTypeList(generics.ListAPIView):
    queryset = BikeType.objects.all()
    serializer_class = BikeTypeSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        response_data = {
            "success": "true",
            "message": "BikeTypeList retrieved successfully",
            "BikeTypeList": serializer.data,
        }
        return Response(response_data)
    


class SpecificationList(generics.ListAPIView):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        response_data = {
            "success": "true",
            "message": "SpecificationList retrieved successfully",
            "SpecificationList": serializer.data,
        }
        return Response(response_data)
    


class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        response_data = {
            "success": "true",
            "message": "CompanyList retrieved successfully",
            "CompanyList": serializer.data,
        }
        return Response(response_data)
    


class BudgetList(generics.ListAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        response_data = {
            "success": "true",
            "message": "BudgetList retrieved successfully",
            "BikeTypeList": serializer.data,
        }
        return Response(response_data)
    

    # views.py

    
from django.http import JsonResponse
from django.views import View
from .models import Login

class ValidateLoginView(View):
    def get(self, request):
        phno = request.GET.get('phno')
        name = request.GET.get('name')

        try:
            login_obj = Login.objects.get(phno=phno, name=name)
            response_data = {
                'status': 'success',
                'message': 'Login successful!',
                # 'user_id': login_obj.id,
            }
            return JsonResponse(response_data)
        except Login.DoesNotExist:
            response_data = {
                'status': 'error',
                'message': 'Login failed.',
            }
            return JsonResponse(response_data, status=200)




class TargetView(generics.RetrieveAPIView):
    serializer_class = VehicleSerializer

    def retrieve(self, request, *args, **kwargs):
         
        specification = request.query_params.get("specification")
        company = request.query_params.get("company")
        budget = request.query_params.get("budget")
        
        if not specification:
            return Response({"success": "false", "message": "specification is required"})
        
        if not company:
            return Response({"success": "false", "message": "company is required"})
        
        if not budget:
            return Response({"success": "false", "message": "budget is required"})
        
        specification=specification.lower()
        
        company=company.lower()

        
        budget=budget.lower()
        

        try:
            vehicle_instance = Vehicle.objects.get(specification=specification,company=company,budget=budget)
            print("vehicle_instance",vehicle_instance)

            vehicle_serializer = self.serializer_class(vehicle_instance)
            
            print("pallet_form_serializer",vehicle_serializer)


            response_data = {
                        "success": "true",
                        "message": "Bike details retrieved successfully.",
                        # 'master': master_data,
                        "response": [
                            {
                               "bikename": vehicle_serializer.data["bikename"],
                               "bikeimage": vehicle_serializer.data["bikeimage"]
                               
                            }
                        ],
                    }
            return Response(response_data)

        except Vehicle.DoesNotExist:
            return Response({"success": "false", "message": "Invalid credential data"})
        
####################################  working code ##########################################

class ScodeList(generics.ListAPIView):
    queryset = Scodedetail.objects.all()
    serializer_class = ScodedetailSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        response_data = {
            "success": "true",
            "message": "Scode details retrieved successfully",
            "ScodeDetail": serializer.data,
        }
        return Response(response_data)
    

###########################################################   end code  ####################################


####################################   calculating response bite 
# import sys
# import json
# from rest_framework.response import Response
# from rest_framework import generics
# from .models import Scodedetail
# from .serializers import ScodedetailSerializer

# class ScodeList(generics.ListAPIView):
#     queryset = Scodedetail.objects.all()
#     serializer_class = ScodedetailSerializer

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(queryset, many=True)
#         response_data = {
#             "success": "true",
#             "message": "Scode details retrieved successfully",
#             "BikeTypeList": serializer.data,
#         }
        
#         # Serialize the response_data to JSON and encode it as bytes
#         response_json = json.dumps(response_data)
#         response_bytes = response_json.encode('utf-8')
        
#         # Calculate the size of the response in bytes
#         response_size_bytes = sys.getsizeof(response_bytes)

#         print("response_size_bytes",response_size_bytes)
        
#         # Create a Response object with the serialized data
#         response = Response(response_data)
        
#         # Add a custom HTTP header to indicate the response size
#         response['X-Response-Size-Bytes'] = str(response_size_bytes)

#         print("after response['X-Response-Size-Bytes']",response['X-Response-Size-Bytes'])
        
#         return response



