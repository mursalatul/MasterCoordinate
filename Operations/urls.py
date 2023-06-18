from django.urls import path
from . import views

urlpatterns = [
    path("p1/operation/distance/<str:x1>$<str:y1>&<str:x2>$<str:y2>", views.distance), # using <str:> to take +- both value(<int:> take only positive values)
    path("p1/operation/dotproduct/<str:x1>$<str:y1>&<str:x2>$<str:y2>", views.dotproduct),
    path("p1/operation/crossproduct/<str:x1>$<str:y1>&<str:x2>$<str:y2>", views.crossproduct),
]