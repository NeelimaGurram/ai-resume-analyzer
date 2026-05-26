import pdfplumber

def extract_text_fromPdf(pdf_path):
    text=""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text=page.extract_text()

            if page_text:
                text+=page_text

    return text

def extract_skills(text,skills):
    found_skills=[]
    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    
    return found_skills

skills=[
    "Python",
    "Java",
    "SQL",
    "React",
    "FastAPI",
    "Docker",
    "MachineLearning"
]

pdf_path="data/resume.pdf"

resume_text=extract_text_fromPdf(pdf_path)
found_skills=extract_skills(resume_text,skills)

print("Found Skills:")
print(found_skills)