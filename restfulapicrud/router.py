from rest_framework import routers
from employeeapi.viewsets import EmployeeViewset

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)