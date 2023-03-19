# urls.py 
from django.contrib import admin
from django.urls import include, path
from register import views as v

urlpatterns = [
    path('', include('user1.urls')),
    path("register/", v.register, name="register"),  # <-- added
    path('accounts/', include("django.contrib.auth.urls")), # <-- added

    path('admin/', admin.site.urls),

]