from django.urls import path

from api.views import CodeFileDetailsView, CodeFileCreateView, PingPongView


urlpatterns = [
    path("codes/<int:pk>", CodeFileDetailsView.as_view()),
    path("codes/", CodeFileCreateView.as_view()),
    path('ping/', PingPongView.as_view())
]
