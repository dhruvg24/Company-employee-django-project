from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
# Create your views here.

# through below method we get default options
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class=CompanySerializer

    # lets say we need to get all employees of a particular company {by id}
    # {{BASE_URL}}/companies/{companyID}/employees
    @action(detail=True, methods=['get']) #this is a decorator for custom api
    def employees(self, request, pk=None):
        try:
            # pk - primary key of company
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            # need to send serialized data
            emps_serializer = EmployeeSerializer(emps,many=True, context={'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Company might not exist!! Error!!'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer