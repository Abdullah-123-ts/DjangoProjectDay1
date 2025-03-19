
from django.contrib import admin
from django.urls import path,include
import book.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('books/', include(book.urls)),

]
