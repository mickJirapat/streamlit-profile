from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"


# Variables
PAGE_TITLE = "Jirapat's Digital CV"
PAGE_ICON = ":wave:"
NAME = "Jirapat (Mick) Jirasevijinda"
EMAIL = "mickjirapat@gmail.com"
DESCRIPTION = """
Fresh Computing graduate from NUS
"""
SOCIAL_MEDIA = {
    "Youtube": "https://youtube.com",
    "LinkedIn": "https://www.linkedin.com/in/jirapat-mick",
}
PROJECTS = {
    "Title": "Project Link",
    "Title1": "Project Link 1"
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

st.title("Hello there!")

# Load CSS, PDF, Profile Pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero Section
col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(profile_pic, width = 250)

with col2:
    # Name
    st.title(NAME)

    # Description
    st.write(DESCRIPTION)

    # Resume
    st.download_button(
        label = "📄 Download Jirapat's Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream"
    )

    # Email
    st.write("✉", EMAIL)
    st.write("🌐", SOCIAL_MEDIA["LinkedIn"])
    

# Experience and Qualifications
st.write("#")
st.subheader("Internship Experiences")
st.write(
    """
- ➜ Technical Sales Engineer Intern @ Cisco Systems
- ➜ Cloud Engineer Intern @ Merck Sharpe & Dohme
- ➜ Product Manger Intern @ Ola Chat
"""
)