from django.urls import path

from exam_prep_library.web import views

urlpatterns = [
    path('', views.show_homepage, name='show homepage'),

    path('add/', views.add_book, name='add book'),
    path('edit/<int:pk>', views.edit_book, name='edit book'),
    path('details/<int:pk>', views.show_book, name='show book'),

    path('profile/', views.show_profile, name='show profile'),
    #path('profile/create', views.create_profile, name='create profile'),
    path('profile/edit/', views.edit_profile, name='edit profile'),
    path('profile/delete/', views.delete_profile, name='delete profile'),
]