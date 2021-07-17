from django.urls import path

from api.views import CodeFileDetailsView, UpsertView


urlpatterns = [
    path("codes/<pk>", CodeFileDetailsView.as_view()),
    path("upsert/", UpsertView.as_view()),
]
