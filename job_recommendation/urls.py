from django.urls import path
from . import views

urlpatterns = [
    path('job-posting/', views.job_posting_form, name='job_posting_form'),
    path('success/', views.success, name='success'),
    path('match-selection/', views.match_selection, name='match_selection'),
    path('applicant-form/', views.applicant_form, name='applicant_form'),
    path('recommend-jobs/<int:applicant_id>/', views.recommend_jobs_to_applicant, name='recommend_jobs_to_applicant'),
]
