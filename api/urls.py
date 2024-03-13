from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customers', CustomerViewset)
router.register('customer-interaction', CustomerInteractionViewset)
router.register('employees', EmployeeViewset)
router.register('roleset', RoleViewset)

urlpatterns = [
    path('api/register/', Register.as_view(),name='register'),
    path('api/login/', Login.as_view(),name='login'),
    path('api/logout/', Logout.as_view(),name='logout'),
    path('api/', include(router.urls))
]
