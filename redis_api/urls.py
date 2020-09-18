from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_items, manage_item, getItems

urlpatterns = {
    path('', manage_items, name="items"),
    path('test/', getItems.as_view(), name='test'),
    path('<slug:key>', manage_item, name="single_item")
}
urlpatterns = format_suffix_patterns(urlpatterns)