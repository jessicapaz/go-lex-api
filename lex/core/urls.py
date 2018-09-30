from django.urls import path
from .views import CodeApiView


urlpatterns = [
    path('', CodeApiView.as_view())
]