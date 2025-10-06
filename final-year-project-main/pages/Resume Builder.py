from fpdf import FPDF
import streamlit as st

# Function to create a styled PDF resume
def create_resume_pdf(first_name, last_name, phone, address, github, college_name, degree, school_name, branch, skills, certificates, projects, achievements, description):
    pdf = FPDF()
    pdf.add_page()

    # Set font and colors
    pdf.set_font("Arial", style='B', size=20)
    pdf.set_fill_color(100, 149, 237)  # Cornflower Blue
    pdf.set_text_color(255, 255, 255)  # White

    # Header with user description
    pdf.cell(200, 10, txt=f"{first_name} {last_name}", ln=True, align='C', fill=True)
    
    # Set font for address and phone to match the description font
    pdf.set_font("Arial", size=10)
    
    pdf.cell(200, 7, txt=f"{phone} | {address} | {github}", ln=True, align='C', fill=True)
    
    # Description in smaller font
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.ln(3)  # Add a bit of space before the description
    pdf.multi_cell(0, 7, txt=description)
   
    # Reset colors for the rest of the resume
    pdf.set_fill_color(255, 255, 255)  # White
    pdf.set_text_color(0, 0, 0)  # Black
    
    # Qualifications
    pdf.ln(1)  # Add spacing before the Qualifications section
    pdf.set_font("Arial", style='B', size=14)
    pdf.set_text_color(100, 149, 237)  # Cornflower Blue
    pdf.cell(200, 10, txt="Qualifications", ln=True)
    # Line separator after Personal Details
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.set_font("Arial", size=12, style = 'B')
    pdf.ln(2)
    pdf.cell(200, 7, txt=f"{college_name}", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 7, txt=f"{degree}", ln=True)
    pdf.set_font("Arial", size=12, style = 'B')
    pdf.cell(200, 7, txt=f"{school_name}", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 7, txt=f"{branch}", ln=True)

    # Skills
    # pdf.ln(2)  # Add spacing before the Skills section
    pdf.set_font("Arial", style='B', size=14)
    pdf.set_text_color(100, 149, 237)  # Cornflower Blue
    pdf.cell(200, 10, txt="Skills", ln=True)
    # Line separator after Personal Details
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line
    pdf.ln(2)
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 7, txt=skills)

    #  Certification
    pdf.ln(5)  # Add spacing before the Work Experience section
    pdf.set_font("Arial", style='B', size=14)
    pdf.set_text_color(100, 149, 237)  # Cornflower Blue
    pdf.cell(200, 10, txt="Certifications", ln=True)
    # Line separator after Personal Details
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line
    pdf.ln(2)
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 7, txt=certificates)

    
    

    # Projects
    pdf.ln(5)  # Add spacing before the Projects section
    pdf.set_font("Arial", style='B', size=14)
    pdf.set_text_color(100, 149, 237)  # Cornflower Blue
    pdf.cell(200, 10, txt="Projects", ln=True)
    # Line separator after Personal Details
    pdf.set_draw_color(0, 0, 139)  # Dark Blue
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line
    pdf.ln(2)
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 7, txt=projects)

    # Academic and Extracurricular Achievements
    pdf.ln(5)  # Add spacing before the Achievements section
    pdf.set_font("Arial", style='B', size=14)
    pdf.set_text_color(100, 149, 237)  # Cornflower Blue
    pdf.cell(200, 10, txt="Achievements", ln=True)
    # Line separator after Personal Details
    pdf.set_draw_color(0, 0, 139)  # Dark Blue
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line
    pdf.ln(2)
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 7, txt=achievements)

    return pdf

# Streamlit App
st.image('logo2.png')
st.title("Resume Builder")


# Gather personal information
first_name = st.text_input("First name")
last_name = st.text_input("Last name")
phone = st.text_input("Phone")
address = st.text_input("Email Address")
github = st.text_input("Github")

# Qualifications
st.markdown("<h2 style='color: #87CEFA;'>Qualifications</h2>", unsafe_allow_html=True)
college_name = st.text_input("College name")
degree = st.text_input("Degree")
school_name = st.text_input("School name")
branch = st.text_input("Branch")

# Skills
st.markdown("<h2 style='color: #87CEFA;'>Skills</h2>", unsafe_allow_html=True)
skills = st.text_area("List your skills, separated by |.")

# Certifications, Projects, and Achievements
st.markdown("<h2 style='color: #87CEFA;'>Certifications</h2>", unsafe_allow_html=True)

# Gather certifications
certificates = st.text_area("Certification (Enter each certificate on a new line)")


st.markdown("<h2 style='color: #87CEFA;'>Projects</h2>", unsafe_allow_html=True)
projects = st.text_area("Projects (Enter each project on a new line)")

st.markdown("<h2 style='color: #87CEFA;'>Academic and Extracurricular Achievements</h2>", unsafe_allow_html=True)
achievements = st.text_area("Academic and Extracurricular Achievements (Enter each achievement on a new line)")

# User description input
user_description = st.text_area("Enter a brief description about yourself (this will appear in the header of the PDF)")

# Create and Download PDF
if st.button("Download Resume"):
   
    pdf = create_resume_pdf(first_name, last_name, phone, address, github, college_name, degree, school_name, branch, skills, certificates, projects, achievements, user_description)
    pdf_output = bytes(pdf.output(dest="S"))

    st.download_button(label="Download Resume", data=pdf_output, file_name="resume.pdf", mime="application/pdf")
