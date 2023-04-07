from django.urls import path

from api.views import ProductListApiView

app_name = 'api'

urlpatterns = [
    path('product-list/', ProductListApiView.as_view(), name='product_list'),
]
