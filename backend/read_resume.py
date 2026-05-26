import pdfplumber

pdf_path = "data/resume.pdf"

text = ""

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

skills = [
    "Python",
    "Java",
    "React",
    "FastAPI",
    "SQL",
    "Docker",
    "Machine Learning",
    "TensorFlow"
]

found_skills = []

for skill in skills:
    if skill.lower() in text.lower():
        found_skills.append(skill)

print("Found Skills:")
print(found_skills)