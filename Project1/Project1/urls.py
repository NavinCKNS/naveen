
from django.contrib import admin
from django.urls import include,path
from app1 import views
from app1.views import delete1, values,insert,update1
from app1 import urls
from app2 import urls





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.report),
    path('s/',views.details),
    #  path('update/<int:id>',views.update),
    # path('delete/<int:id>',views.delete),
    path('accounts/',include('django.contrib.auth.urls')),
    path('del/',values.as_view(),name="list1"),
    path('ins/',insert.as_view()),
    path('delete1/<int:pk>/',delete1.as_view()),
    path('update1/<int:pk>/',update1.as_view()),
    path('log1/',views.log),
    path('in/',views.ind)


    # path('report/',include('app1.urls')),
    # path('app2/',include('app2.urls'))

]
