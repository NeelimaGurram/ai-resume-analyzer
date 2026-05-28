skills_list=[
    "Python",
    "Java",
    "JavaScript",
    "MachineLearning",
    "Git",
    "Github",
    "Node",
    "React",
    "SQL",
    "CI/CD"
]

def extract_skills(text,skills:list[str])->list[str]:
    foundskills=[]
    for skill in skills:
        if skill.lower() in text.lower():
            foundskills.append(skill)

    return foundskills

