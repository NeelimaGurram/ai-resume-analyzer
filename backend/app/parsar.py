from extractor import extract_skills,skills_list,extract_education

def parse_resume(text):

    return {
        "skills": extract_skills(text,skills_list),
        "education":extract_education(text),
        "projects":[]
    }
