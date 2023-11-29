from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "Foto_Rostro_Esposito.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Lucas Esposito Tejerina Resume"
PAGE_ICON = "🧑‍💻"
NAME = "Lucas Esposito Tejerina"
DESCRIPTION = """
Systems Information Engineering Student from Buenos Aires, Argentina
"""
EMAIL = "espositolucas2002@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/lucas-esposito-tejerina/",
    "GitHub": "https://github.com/EspositoLucas"
}
PROJECTS = {
    "🏆 DATA ANALYST PORTFOLIO BLOG - Personal Website about Data Analytics ": "https://espositolucas.github.io/DataWeb.github.io/"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("✉️", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# # --- EXPERIENCE & QUALIFICATIONS ---
# st.write('\n')
# st.subheader("Experience & Qulifications")
# st.write(
#     """
# - ✔️ 7 Years expereince extracting actionable insights from data
# - ✔️ Strong hands on experience and knowledge in Python and Excel
# - ✔️ Good understanding of statistical principles and their respective applications
# - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
# """
# )


# --- SKILLS ---
st.write('\n')
st.subheader(" Skills")
st.write("---")
st.write(
    """
- 👨‍💻 Programming: Python (Pandas, NumPy, SciPy, MatPlotLib)
- 📊 Data Visulization: PowerBi, MS Excel (VLOOKUP, Conditional Formatting, Pivot Tables), Tableau
- 🗄️ Databases: MS SQL Server
"""
)


# # --- WORK HISTORY ---
# st.write('\n')
# st.subheader("Work History")
# st.write("---")

# # --- JOB 1
# st.write("🚧", "**Senior Data Analyst | Ross Industries**")
# st.write("02/2020 - Present")
# st.write(
#     """
# - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
# - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
# - ► Redesigned data model through iterations that improved predictions by 12%
# """
# )

# # --- JOB 2
# st.write('\n')
# st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
# st.write("01/2018 - 02/2022")
# st.write(
#     """
# - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
# - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
# - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
# """
# )

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
    
    
# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write(
    """
- 🎓 SYSTEMS INFORMATION ENGINEERING (4º YEAR) –  Universidad Tecnológica Nacional (UTN)       2020 - 2023
- 🏫 BACHELOR OF SOCIAL SCIENCE AND HUMANITIES –  Colegio La Salle Centro  December 2019
"""
)

# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
st.write(
    """
- 📄 PROGRAMA DEL DIPLOMA –  Bachillerato Internacional        2019
- 📄 FIRST CERTIFICATE IN ENGLISH EXAM – University of Cambridge     2019
- 📄 GRADED EXAMINATION IN SPOKEN ENLGISH  – Trinity College London     2018
"""
)
