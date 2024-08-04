from django.urls import path
from . import views

# urlpatterns = [
#     path("create/",views.create,name="create"),
#     path("insert/",views.insert,name="insert"),
#     path('',views.index,name="index"),
# ]

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("womens/", views.womens, name="womens"),
    path("mens/", views.mens, name="mens"),
    path("kids/", views.kids, name="kids"),
    path("create/", views.create, name="create"),
    path("signin/", views.signin, name="signin"),
    path("submit/", views.submit, name="submit"),
    path("", views.index, name="index"),
]