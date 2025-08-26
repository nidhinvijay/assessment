# poll/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # THIS IS THE NEW HOMEPAGE URL
    path('', views.index_view, name='index'),

    # The poll list is now at its own URL
    path('polls/', views.poll_list, name='poll_list'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('poll/<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('poll/<int:poll_id>/vote/', views.vote, name='vote'),
    path('poll/<int:poll_id>/results/', views.poll_results, name='poll_results'),
    path('my-votes/', views.my_votes, name='my_votes'),
    path('poll/<int:poll_id>/export/csv/', views.export_results_csv, name='export_results_csv'),
]