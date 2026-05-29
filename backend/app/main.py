from extractor import extract_text_from_pdf
from parsar import parse_resume
import json

pdf_path="data/resume.pdf"

resume_text=extract_text_from_pdf(pdf_path)

resume_data=parse_resume(resume_text)

print(json.dumps(resume_data, indent=4))
