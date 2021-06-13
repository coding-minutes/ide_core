from django.urls import path

from api.views import PingPongView, SaveCode, GetCode


urlpatterns = [
	path("ping/", PingPongView.as_view()),
	path("code/", SaveCode.as_view()),
	path('code/<int:code_id>/',  GetCode.as_view())
]
