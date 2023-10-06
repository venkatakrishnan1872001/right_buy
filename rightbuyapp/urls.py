from django.urls import path

from . import views


from rightbuyapp.views import (BikeTypeList,SpecificationList,CompanyList,BudgetList,ValidateLoginView,TargetView,ScodeList)

urlpatterns = [
    path('BikeTypeList', BikeTypeList.as_view(), name='BikeTypeList'),

    path('SpecificationList', SpecificationList.as_view(), name='SpecificationList'),

    
    path('CompanyList', CompanyList.as_view(), name='CompanyList'),


    
    path('BudgetList', BudgetList.as_view(), name='BudgetList'),

    
    path('validate_login', ValidateLoginView.as_view(), name='validate_login'),

    
    path('TargetView', TargetView.as_view(), name='TargetView'),

    path('ScodeDetail', ScodeList.as_view(), name='ScodeList'),

]

