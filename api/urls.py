from django.urls import path

from api.views import CodeFileDetailsView, CodeFileCreateView


urlpatterns = [
    path("codes/<int:pk>", CodeFileDetailsView.as_view()),
    path("codes/", CodeFileCreateView.as_view()),
]
