from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml 
from wishlist.views import show_json
from wishlist.views import return_json_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', return_json_id, name='return_json_id'),
]