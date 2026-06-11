import json
import pdfplumber


pdf_path="../data/resume.pdf"

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

            result["full_text"]+=page_text+"\n"
        result["full_text"]=result["full_text"].strip()
    
    return result

def main():
    text=extract_text_with_pdfplumber(pdf_path)

    print(json.dumps(text, indent=2))

    with open("resume_output.json","w") as f:
        json.dump(text,f, indent=2)
    print("\n saved: resume_output.json")

if __name__ =="__main__":
    main()
