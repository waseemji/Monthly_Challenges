from django.urls import path
from . import views


urlpatterns = [
    # path("january/", views.january),
    # path("february",views.february),
    path("<int:month>", views.monthly_number_challenge),
    path('<str:month>/',views.monthly_challenge)

]