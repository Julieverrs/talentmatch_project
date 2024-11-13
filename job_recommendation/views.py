import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobPostForm, ApplicantProfileForm
from .models import JobPost, ApplicantProfile
from .nlp_processing import extract_keywords, recommend_jobs, match_skills_with_job

# Job posting form view
def job_posting_form(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = JobPostForm()
    return render(request, 'job_posting_form.html', {'form': form})

# Applicant profile form view
def applicant_form(request):
    if request.method == 'POST':
        form = ApplicantProfileForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save()  # Save the form and get the applicant object
            
            # After saving, redirect to the recommend_jobs_to_applicant view
            return redirect('recommend_jobs_to_applicant', applicant_id=applicant.id)
        
    else:
        form = ApplicantProfileForm()

    return render(request, 'applicant_form.html', {'form': form})

# Success page view after form submission
def success(request):
    return render(request, 'success.html')

# Match selection view for analyzing job fit based on keywords
def match_selection(request):
    job_posts = JobPost.objects.all()
    applicants = ApplicantProfile.objects.all()
    result = None  # Initialize result variable
    
    if request.method == 'POST':
        job_post_id = request.POST.get('job_post')
        applicant_id = request.POST.get('applicant')

        if job_post_id and applicant_id:
            job_post = JobPost.objects.get(id=job_post_id)
            applicant = ApplicantProfile.objects.get(id=applicant_id)

            # Analyze the selected job post and applicant
            job_keywords = extract_keywords(job_post.description)
            applicant_keywords = extract_keywords(applicant.skills)
            common_keywords = job_keywords.intersection(applicant_keywords)
            fit_score = len(common_keywords)

            result = {
                'job_title': job_post.title,
                'applicant_name': applicant.name,
                'fit_score': fit_score,
                'common_keywords': ', '.join(common_keywords),
                'applicant_id': applicant.id,  # Add the applicant ID here
            }

    return render(request, 'match_selection.html', {'job_posts': job_posts, 'applicants': applicants, 'result': result})

# Recommend jobs based on applicant skills using dataset
def recommend_jobs_to_applicant(request, applicant_id):
    # Retrieve the applicant profile using the applicant_id
    applicant = get_object_or_404(ApplicantProfile, id=applicant_id)

    # Extract the applicant's skills from the form
    applicant_skills = applicant.skills  # Assuming 'skills' field contains comma-separated skills

    # Load the job dataset (assuming it's a CSV file in the job_recommendation app directory)
    job_data = pd.read_csv('job_recommendation/job_dataset.csv')

    # Create an empty list to store the recommended jobs
    recommended_jobs = []

    # Loop through the job dataset and check if the job description contains skills from the applicant
    for _, job in job_data.iterrows():
        job_title = job['title']
        job_description = job['description']
        job_skills_required = job['skills_required']

        # Match the applicant's skills with the job's required skills
        common_skills = match_skills_with_job(applicant_skills, job_skills_required)

        # If there are common skills, this job is a match and should be recommended
        if common_skills:
            recommended_jobs.append({
                'job_title': job_title,
                'job_description': job_description,
                'common_skills': ', '.join(common_skills)  # List of common skills
            })

    # Pass the applicant and the list of recommended jobs to the template
    return render(request, 'job_recommendations.html', {
        'applicant': applicant,
        'recommended_jobs': recommended_jobs
    })
