import pdfplumber

def extract_text_from_pdf(pdf_path):
    text=""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text=page.extract_text()

            if page_text:
                text+=page_text
    
    return text

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

def extract_education(text):
    Education_keywords=[
        "Bachelor",
        "Master",
        "University"
    ]
    found=[]
    for keyword in Education_keywords:
        if keyword.lower() in text.lower():
            found.append(keyword)
    return found