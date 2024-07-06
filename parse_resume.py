import fitz  # PyMuPDF
import re

def extract_resume_data(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    text = ""
    
    # Extract text from each page
    for page in doc:
        text += page.get_text()

    # Extracting the relevant sections using regex
    name_re = re.search(r"Name: (.*)", text)
    contact_re = re.search(r"Contact: (.*)", text)
    summary_re = re.search(r"Summary\n(.*?)\nEducation", text, re.DOTALL)
    education_re = re.search(r"Education\n(.*?)\nExperience", text, re.DOTALL)
    experience_re = re.search(r"Experience\n(.*?)\nProjects", text, re.DOTALL)
    projects_re = re.search(r"Projects\n(.*?)\nCertifications", text, re.DOTALL)
    certifications_re = re.search(r"Certifications\n(.*?)\nSkills", text, re.DOTALL)
    skills_re = re.search(r"Skills\n(.*?)\nLanguages", text, re.DOTALL)
    languages_re = re.search(r"Languages\n(.*?)\nLinks", text, re.DOTALL)
    links_re = re.search(r"Links\n(.*?)\nPersonal Details", text, re.DOTALL)
    personal_re = re.search(r"Personal Details\n(.*?)\n", text, re.DOTALL)

    # Constructing the JSON object
    resume_data = {
        "name": name_re.group(1).strip() if name_re else "",
        "contact": contact_re.group(1).strip() if contact_re else "",
        "summary": summary_re.group(1).strip() if summary_re else "",
        "education": education_re.group(1).strip() if education_re else "",
        "experience": experience_re.group(1).strip() if experience_re else "",
        "projects": projects_re.group(1).strip() if projects_re else "",
        "certifications": certifications_re.group(1).strip() if certifications_re else "",
        "skills": skills_re.group(1).strip() if skills_re else "",
        "languages": languages_re.group(1).strip() if languages_re else "",
        "links": links_re.group(1).strip() if links_re else "",
        "personal_details": personal_re.group(1).strip() if personal_re else ""
    }

    return resume_data

if __name__ == "__main__":
    pdf_path = "resumehaveloc.pdf"  # Path to your resume PDF
    resume_data = extract_resume_data(pdf_path)
    print(resume_data)
