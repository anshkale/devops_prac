import streamlit as st
from ai_service import fetch_questions


def main():

    # Check and initialize session state variables
    if "started" not in st.session_state:
        st.session_state.started = False

    # Check and initialize quiz_generated state variable
    if "quiz_generated" not in st.session_state:
        st.session_state.quiz_generated = False    


    st.title("TESTIFY - AI-Powered Quiz Generator")

    # Display animated GIF
    st.image("image1.gif.gif")
    if not st.session_state.started:
        if st.button("Start Testify"):
            st.session_state.started = True
        return 

    # Text input for user to paste content
    text_content = st.text_area("Paste your text content here:")

    #Dropdown for selecting quiz level
    quiz_level = st.selectbox("Select Quiz Level:", ["Easy", "Medium", "Hard"])

    #convert quiz level to lower casing
    quiz_level_lower = quiz_level.lower()

    #Initialize session_state for storing user answers
    session_state = st.session_state

    # check if quiz_generated is in session_state, if not initialize it
    if 'quiz_generated' not in session_state:
        session_state.quiz_generated = False

    #Track if Generate Quiz button is clicked
    if not session_state.quiz_generated:
        session_state.quiz_generated = st.button("Generate Quiz")



    if session_state.quiz_generated:
        #define questions and options
        questions = fetch_questions(text_content=text_content, quiz_level=quiz_level_lower) # call fetch_questions function

        #Display questions and radio buttons
        selected_options = []
        correct_answers = []
        for question in questions:                  # arrange questions from fetched questions 
            options = list(question["options"].values())
            selected_option = st.radio(question["mcq"], options, key=question["mcq"], index=None,)
            selected_options.append(selected_option)  
            correct_answers.append(question["options"][question["correct"]])

        # submit button
        if st.button("Submit Answers"):
            marks = 0
            #Display selected options
            st.header("Quiz Results:")
            for i, question in enumerate(questions):
                selected_option = selected_options[i]
                correct_answer = correct_answers[i]
                st.subheader(f"{question['mcq']}")
                st.write(f"Your Answer: {selected_option}")
                st.write(f"Correct Answer: {correct_answer}")

                if selected_option == correct_answer: #check answers
                    marks += 1

            st.subheader(f"Your Scored: {marks} out of {len(questions)}")    #display marks


#call main function
if __name__ == "__main__":
    main()