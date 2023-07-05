from django.urls import path
from .views import getroutes,Gettasks,Gettask,Createtask,getprofiles,Task_delete

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', getroutes),
    path('Tasks/',Gettasks),
    path('Task/<str:pk>/', Gettask),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/',Createtask),
    path('profiles/', getprofiles),
    path('Delete/',Task_delete),

]