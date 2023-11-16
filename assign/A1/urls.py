

from django.urls import path

from A1.views import detail,show,delete,update


urlpatterns = [
    path('',detail.as_view()),
    path('list/',show.as_view(),name='list'),
    path('delete/<int:pk>/',delete.as_view()),
    path('update/<int:pk>/',update.as_view())
]
