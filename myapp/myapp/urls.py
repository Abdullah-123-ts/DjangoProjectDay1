from django.contrib import admin
from django.urls import path,include
import book.urls
import ClassBasedViewsBook.api.urls
import SerializerRelationships.api.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('books/', include(book.urls)),
    path('classBased/', include(ClassBasedViewsBook.api.urls)),
    path('hyperLinks/', include(SerializerRelationships.api.urls)),

]
