# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 00:10:08 2026

@author: lmang
"""

import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Researcher Profile | CSS 2026",
    page_icon="🔬",
    layout="wide"
)

# ------------------ Sidebar ------------------
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Profile", "Research Interests", "Projects", "Publications", "Skills", "Contact"]
)

st.sidebar.markdown("---")
st.sidebar.caption("CSS 2026 • Streamlit Cloud")

# ------------------ Header ------------------
st.title("🔬 Researcher Profile")
st.subheader("Livhuwani Ramavhuya")
st.caption("BSc Honours Student | Mathematics | Physical Sciences")

st.markdown("---")

# ------------------ Profile ------------------
if section == "Profile":
    st.header("About Me")
    st.write(
        """
        I am a BSc Honours (Mathematics) student at Sefako Makgatho Health Sciences University with a strong interest in **data science, physics,
        mathematics, and computational research**.  
        I enjoy working with data, building analytical tools, and applying scientific
        principles to real-world problems.
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Field", "Physical Sciences")
    with col2:
        st.metric("Focus", "Data & Research")

# ------------------ Research Interests ------------------
elif section == "Research Interests":
    st.header("Research Interests")
    st.markdown(
        """
        - Data Science & Analytics  
        - Scientific Computing  
        - Physics Experiments & Simulations  
        - Chemistry Data Analysis  
        - Machine Learning for Scientific Research  
        """
    )

#--------------------------Projects-----------------
elif section == "Projects":
    st.header("🛠️ Projects & Work")

    st.subheader("📊 Coursework & Academic Projects")
    st.markdown("""
    - Analyzed weather vs bike rentals using Python
    - Performed data cleaning and visualization for lab datasets
    - Built scripts to automate CSV data processing
    """)

    st.subheader("🧪 Laboratory & Experimental Work")
    st.markdown("""
    - Measured atomic spectra of Hydrogen, Helium, and Mercury
    - Conducted thermodynamic measurements of ice
    - Learned error analysis and scientific reporting techniques
    """)



# ------------------ Publications ------------------
elif section == "Publications":
    st.header("📄 Publications")
    st.info("No formal publications yet.")
    st.markdown("Currently building a strong research and project portfolio.")


# ------------------ Skills ------------------
elif section == "Skills":
    st.header("Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Programming")
        st.markdown(
            """
            - Python  
            - Pandas  
            - NumPy  
            - Streamlit  
            """
        )

    with col2:
        st.subheader("Data & Analysis")
        st.markdown(
            """
            - Data Cleaning  
            - Visualization  
            - Statistical Analysis  
            - CSV & Database Handling  
            """
        )

    with col3:
        st.subheader("Scientific Skills")
        st.markdown(
            """
            - Experimental Design  
            - Error Analysis  
            - Scientific Reporting  
            """
        )

# ------------------ Contact ------------------
elif section == "Contact":
    st.header("Contact")

    st.write("Feel free to reach out for collaboration or academic discussions.")

    st.markdown(
        """
        **Email:** 202304496@swave.smu.ac.za.com  
        **GitHub:** https://css2026-ramavhuya-research-profile-h9f5cgzrwdrcakx3n87fhy.streamlit.app/
        """
    )

# ------------------ Footer ------------------
st.markdown("---")
st.caption("© 2026 • CSS Streamlit Research Profile")





