#  Learning Path Recommender

## 🔗 Live Demo
https://learning-path-recommender-xelqpubfhcpytdp3atbwjm.streamlit.app/

---

##  Project Overview
The **Learning Path Recommender** is a web-based educational application that helps learners plan their studies by generating a personalized learning roadmap.  
The system recommends a structured sequence of topics based on the learner’s current skill level, target career goal, and available study time per week.

This project is designed as a **functional prototype** to demonstrate how learning paths can be optimized using rule-based logic and simple user inputs.

---

##  Problem Statement
Learners often face confusion about:
- What skills to learn next
- The correct order of learning topics
- How much time is required to reach a specific career goal

Due to the lack of clear guidance, learners waste time on unstructured learning.  
This project aims to solve that problem by providing **clear, goal-oriented, and time-aware learning paths**.

---

##  Solution Approach
The application collects user inputs and applies predefined learning rules to:
- Identify the required skills for a chosen career goal
- Arrange learning topics in a logical order
- Estimate total learning time and completion duration
- Allow users to track progress visually

The system focuses on **simplicity, clarity, and usability**.

---

##  How the System Works
1. The user selects:
   - Current skill level (Beginner / Intermediate / Advanced)
   - Target role (Python Developer / Data Analyst / Data Scientist)
   - Available study hours per week
2. The system:
   - Selects a predefined learning path for the chosen role
   - Calculates total required learning hours
   - Estimates the number of weeks needed to complete the path
3. The user can:
   - View the recommended learning sequence
   - Track progress using a progress slider

---

##  Key Features
- Personalized learning path generation
- Skill-based topic sequencing
- Time estimation (total hours and weeks)
- Visual progress tracking
- Simple and interactive user interface
- Web-based deployment using Streamlit

---

## 🛠 Tech Stack
- **Programming Language:** Python  
- **Framework:** Streamlit  
- **Deployment Platform:** Streamlit Community Cloud  

---

##  How to Run the Project Locally

### 1. Clone the repository
```bash
git clone https://github.com/Biswasrita/learning-path-recommender.git
