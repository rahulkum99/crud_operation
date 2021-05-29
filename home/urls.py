from django.urls import path
from home import views


urlpatterns = [
    path('',views.add_show, name="addandshow"),
    path('update/<int:id>/',views.update_data, name="updatedata"),
    path('delete/<int:id>/', views.delete_data , name='deletedata'),
]