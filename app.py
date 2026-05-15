import streamlit as st
import pandas as pd
import joblib

#Load Model
model = joblib.load("model/employability_model.pkl")

#page config
st.set_page_config(
  page_title="AI Employability Predictor",
  page_icon="🎓",
  layout="centered"
)

#title
st.title("🎓 AI Employability Prediction System")

st.markdown("""
Predict whether a student is employable based on:
- Academic Performance
- Technical Skills
- Internships
- Communication
- Certifications
- Career readiness
""")

st.divider()

#input fields

st.subheader("📚 Academic Profile")

gpa = st.slider("GPA", 0.0, 10.0, 7.5)
core_subject_score = st.slider("Core Subject Score", 0, 100, 60)
academic_consistency = st.slider("Academic Consistency (CGPA variance)", 0.0, 5.0, 2.5)
research_participation = st.slider("Research Participation", 0, 10, 0)

st.subheader("💼 Experience")

internship_count = st.slider("Internship Count", 0, 10, 0)
internship_duration = st.slider("Internship Duration (months)", 0, 24, 0)
project_experience = st.slider("Project Experience Score", 0, 100, 50)
workshop_participation = st.slider("Workshop Participation", 0, 20, 0)
online_course_hours = st.slider("Online Course Hours", 0, 500, 0)

st.subheader("🛠️ Skills")

programming_skill = st.slider("Programming Skill", 0, 100, 50)
domain_knowledge = st.slider("Domain Knowledge", 0, 100, 50)
tool_proficiency = st.slider("Tool Proficiency", 0, 100, 50)
communication_skill = st.slider("Communication Skill", 0, 100, 50)
teamwork_ability = st.slider("Teamwork Ability", 0, 100, 50)
leadership_potential = st.slider("Leadership Potential", 0, 100, 50)
adaptability = st.slider("Adaptability", 0, 100, 50)

st.subheader("🎯 Career Readiness")

career_clarity = st.slider("Career Clarity", 0, 100, 50)
market_awareness = st.slider("Market Awareness", 0, 100, 50)
learning_motivation = st.slider("Learning Motivation", 0, 100, 50)
networking_activity = st.slider("Networking Activity", 0, 100, 50)
industry_relevance = st.slider("Industry Relevance", 0, 100, 50)
certification_count = st.slider("Certification Count", 0, 20, 0)

higher_study = st.checkbox("Interested in Higher Studies?")
higher_study_int = 1 if higher_study else 0

industry_map = {
    "IT/Software": 1, "Finance": 2, "Healthcare": 3,
    "Manufacturing": 4, "Consulting": 5, "Other": 6
}
target_industry = st.selectbox("Target Industry", list(industry_map.keys()))
target_industry_code = industry_map[target_industry]


#fill remaining features (input data)

input_data = pd.DataFrame({
    'GPA': [gpa],
    'Core_Subject_Score': [core_subject_score],
    'Academic_Consistency': [academic_consistency],
    'Research_Participation': [research_participation],
    'Programming_Skill': [programming_skill],
    'Domain_Knowledge': [domain_knowledge],
    'Tool_Proficiency': [tool_proficiency],
    'Certification_Count': [certification_count],
    'Internship_Count': [internship_count],
    'Internship_Duration': [internship_duration],
    'Industry_Relevance': [industry_relevance],
    'Project_Experience': [project_experience],
    'Communication_Skill': [communication_skill],
    'Teamwork_Ability': [teamwork_ability],
    'Leadership_Potential': [leadership_potential],
    'Adaptability': [adaptability],
    'Learning_Motivation': [learning_motivation],
    'Career_Clarity': [career_clarity],
    'Market_Awareness': [market_awareness],
    'Higher_Study_Interest': [higher_study_int],        
    'Target_Industry_Code': [target_industry_code],
    'Workshop_Participation': [workshop_participation],
    'Online_Course_Hours': [online_course_hours],
    'Networking_Activity': [networking_activity],
    'Learning_Path_Generation_Time': [5]

})

#predict button
probability = 0.0

if st.button("Predict Employability"):
  prediction = model.predict(input_data)[0]

  probability = model.predict_proba(
    input_data
  )[0][1]

  st.divider()

  if prediction == 1:
    st.success(
      f"✅ Employable "
      f"({probability*100:.2f}% confidence)"
    )

  else:
    st.error(
      f"❌ Need Improvement "
      f"({(1-probability)*100:.2f}% confidence)"
    )

  #progress bar
  st.progress(float(probability))


#feedback
st.subheader("📌 Suggestions")

if programming_skill < 70:
  st.write("- Improve programming skills")

if internship_count < 2:
  st.write("- Gain more internship experience")

if communication_skill < 60:
  st.write("- Improve communication skills")

if domain_knowledge < 60:
  st.write("- improve your domain knowledge concept")

if certification_count < 2:
  st.write("- Earn industry certifications")

if career_clarity < 60:
  st.write("- improve career planning")

st.divider()

#footer
st.markdown(
   
    "<div style='text-align: center; color: grey; font-size: 13px;'>"
        "Made with ❤️ by <b>Alok Ranjan</b> &nbsp;|&nbsp;"
        "<a href='https://github.com/alokrj01' target='_blank'>GitHub</a> &nbsp;|&nbsp;"
        "<a href='https://linkedin.com/in/alok-ranjan978' target='_blank'>LinkedIn</a> &nbsp;|&nbsp;"
        "<a href='https://alok-portfolio-devhub.netlify.app' target='_blank'>Portfolio</a>"
    "</div>",
    unsafe_allow_html=True
)