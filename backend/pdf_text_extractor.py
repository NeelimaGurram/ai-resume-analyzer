import json
import pdfplumber
import re
from typing import Optional


pdf_path="data/resume.pdf"

def extract_text_with_pdfplumber(pdf_path: str)-> dict:
    result={"file":pdf_path,
            "full_text":"",
            "pages":[]}
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            page_text=page.extract_text()

            result["pages"].append({
                "page_number":i+1,
                "text": page_text
            })

            if page_text:
                result["full_text"]+=page_text+"\n"
        result["full_text"]=result["full_text"].strip()
    
    return result

def extract_name(text:str)->Optional[str]:
    lines=[line.strip() for line in text.split("\n") if line.strip()]
    return lines[0] if lines else None

def extract_email(text: str)->Optional[str]:
    pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match=re.search(pattern, text)
    return match.group() if match else None

def extract_phone(text: str)-> Optional[str]:
    pattern=r"""
        (\+\d{1,3}[\s-])?
        \(?\d{3}\)?
        [\s.\-]?
        \d{3}
        [\s.\-]?
        \d{4}
     """
    match=re.search(pattern, text,re.VERBOSE)
    return match.group().strip() if match else None

def extract_linkedin(text:str)->Optional[str]:
    pattern=r"(https?://)?(www\.)?linkedin\.com/in/[a-zA-Z0-9_-]+/?"
    match=re.search(pattern, text,re.IGNORECASE)
    return match.group() if match else None

def extract_contact_info(text:str)->dict:
    return {
        "name":extract_name(text),
        "email":extract_email(text),
        "phone":extract_phone(text),
        "linkedin":extract_linkedin(text)
    }


def main():
    extracted=extract_text_with_pdfplumber(pdf_path)
    full_text=extracted["full_text"]

    extracted["contact_info"]=extract_contact_info(full_text)

    print(json.dumps(extracted, indent=2))

    with open("resume_output.json","w") as f:
        json.dump(extracted,f, indent=2)
    print("\n saved: resume_output.json")

if __name__ =="__main__":
    main()
