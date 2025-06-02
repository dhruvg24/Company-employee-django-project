from rest_framework import serializers
from api.models import Company, Employee


# Create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields='__all__' #all fields of company model included
    
# serializer for Employee
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields='__all__' #all fields
