
from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
# {{BASE_URL}}/api/v1/companies
router.register(r'employees',EmployeeViewSet)
# {{BASE_URL}}/api/v1/employees

urlpatterns = [
    path('', include(router.urls))
]
