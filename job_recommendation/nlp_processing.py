import re

def extract_keywords(text):
    """
    Extracts keywords from a given text by removing common words (stop words)
    and splitting the text into words.
    """
    # Simple word extraction and conversion to lowercase
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)

    # You can add more sophisticated filtering for stop words if necessary
    stop_words = {'the', 'and', 'for', 'is', 'of', 'to', 'a', 'in', 'on', 'with', 'an', 'at'}  # Example stop words
    keywords = set(word for word in words if word not in stop_words)

    return keywords

def match_skills_with_job(applicant_skills, job_skills_required):
    """
    Match the applicant's skills with the job's required skills.
    """
    # Split applicant skills (separated by commas or spaces) and clean up extra spaces
    applicant_skills = set([skill.lower().strip() for skill in re.split(r',|\s+', applicant_skills)])

    # Split job skills (separated by commas or spaces) and clean up extra spaces
    job_skills_required = set([skill.lower().strip() for skill in re.split(r',|\s+', job_skills_required)])

    # Find the intersection of the applicant's skills and job's required skills
    common_skills = applicant_skills.intersection(job_skills_required)

    return common_skills


def recommend_jobs(applicant_skills, job_list):
    """
    Recommends jobs based on the applicant's skills.
    """
    recommended_jobs = []

    for job in job_list:
        job_skills_required = job.get('skills_required', '')
        common_skills = match_skills_with_job(applicant_skills, job_skills_required)
        
        # If there are matching skills, recommend the job
        if common_skills:
            recommended_jobs.append(job)

    return recommended_jobs
