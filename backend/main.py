from extractor import extract_text_from_pdf
from skills import extract_skills, skills_list

pdf_path="data/resume.pdf"

resume_text=extract_text_from_pdf(pdf_path)
skills_matched=extract_skills(resume_text,skills_list)

print("Skills Matched with Job description are:")
print(skills_matched)