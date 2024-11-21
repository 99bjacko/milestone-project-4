from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_faqs, name='faqs'),
    path('add/', views.add_faq, name='add_faq'),
    path('edit/<int:faq_id>/', views.edit_faq, name='edit_faq'),
]
