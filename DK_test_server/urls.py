from django.urls import path

from . import views

urlpatterns = [
    path('list', views.DK_list),
    path('form', views.DK_form, name='form'),
    path('', views.index, name='index'),
    path('DK/<int:id>/', views.DK_test),
    path('ID/<str:name>', views.DK_user),
    path('test', views.test),
    path('table', views.TablePageView.as_view(), name='table'),
]