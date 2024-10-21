from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('admin/staff', views.StaffViewSet)

urlpatterns = [] + router.urls
