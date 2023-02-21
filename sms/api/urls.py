from rest_framework import routers
from api.views import *
from django.urls import path,include

router = routers.DefaultRouter()
router.register('subjects', Subject_detail),
router.register('staff',Staff_add),
router.register('course',Course_add),
router.register('admin',Admin_add),
router.register('session',Session_add),
#router.register('staffs', Staff_add),
router.register('custom',Custom_add),

urlpatterns = [
    path('api/', include(router.urls)),
]
