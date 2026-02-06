import streamlit as st

st.set_page_config(page_title="Learning Path Recommender", layout="centered")

st.title("🎓 Learning Path Recommender")
st.write("Personalized learning path based on your skills and goals.")

# User inputs
current_skill = st.selectbox(
    "Your current skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

goal = st.selectbox(
    "Your target role",
    ["Python Developer", "Data Analyst", "Data Scientist"]
)

hours_per_week = st.slider("Hours you can study per week", 1, 40, 10)

st.divider()

# Logic
learning_paths = {
    "Python Developer": [
        ("Python Basics", 10),
        ("Object Oriented Programming", 8),
        ("Data Structures", 12),
        ("Mini Project", 10)
    ],
    "Data Analyst": [
        ("Python Basics", 10),
        ("Statistics", 8),
        ("SQL", 10),
        ("Data Visualization", 8)
    ],
    "Data Scientist": [
        ("Python Basics", 10),
        ("Statistics", 10),
        ("Machine Learning", 15),
        ("ML Project", 15)
    ]
}

path = learning_paths[goal]

total_hours = sum(course[1] for course in path)
weeks_needed = max(1, total_hours // hours_per_week)

# Output
st.subheader("📌 Recommended Learning Path")

for i, (course, duration) in enumerate(path, start=1):
    st.write(f"{i}. **{course}** – {duration} hours")

st.divider()

st.success(f"⏱ Total Learning Time: {total_hours} hours")
st.info(f"📆 Estimated Duration: ~ {weeks_needed} weeks")

progress = st.slider("Track your progress (%)", 0, 100, 0)
st.progress(progress / 100)

if progress == 100:
    st.balloons()
    st.success("🎉 Congratulations! Learning path completed.")
