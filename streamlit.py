import streamlit as st
import random

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

st.title("🌟 Growth Mindset Challenge Web App")
st.write("""
Welcome! Explore how adopting a growth mindset can make a difference in your learning journey.
""")

# Motivational Quotes Section
quotes = [
    "“It’s not that I’m so smart, it’s just that I stay with problems longer.” – Albert Einstein",
    "“I am always doing what I cannot do yet, in order to learn how to do it.” – Vincent Van Gogh",
    "“Mistakes are proof that you are trying.”"
]
st.subheader("💡 Today's Motivation")
st.info(random.choice(quotes))

# Interactive Quiz Section
st.subheader("📚 Growth Mindset Quiz")
score = 0
if st.button("Start Quiz"):
    q1 = st.radio("True or False: Intelligence is fixed from birth.", ["True", "False"])
    if q1 == "False":
        score += 1
    q2 = st.radio("Which is essential for growth?", ["Giving up", "Learning from mistakes", "Avoiding challenges"])
    if q2 == "Learning from mistakes":
        score += 1
    st.success(f"Your Score: {score}/2")

# Personal Reflection
st.subheader("📝 Your Growth Plan")
goal = st.text_input("What's one new skill you want to develop?")
if st.button("Submit Goal"):
    st.write(f"🌟 Great goal: '{goal}'. Keep pushing forward!")

# Resources Section
st.subheader("📖 Growth Mindset Resources")
st.markdown("""
- [Growth Mindset by Carol Dweck](https://www.mindsetworks.com/science/)
- [TED Talk: The power of believing you can improve](https://www.ted.com/talks/carol_dweck_the_power_of_believing_you_can_improve)
""")
