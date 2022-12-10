from django.urls import path
from .views import  *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', mainPage, name='main'),
# path('create/', create, name='create'),
path('brand/<str:id>/', brand, name='brand' ),
path('model/<str:id>/', model, name='model'),
path('oem/<str:id>/', oem, name='oem'),
path('test', test_func , name='test'),
# path('delete/<int:id>/',delete  ),
# path('model/', model, name='model' )
# path( 'search_oem/', search_oem , name='search_oem'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
