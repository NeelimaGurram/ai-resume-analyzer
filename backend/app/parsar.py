from skills import extract_skills, skills_list

def parse_resume(text):

    return {
        "skills": extract_skills(text,skills_list),
        "education":[],
        "projects":[]
    }
