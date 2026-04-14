# Testify 
#### Video Demo: <https://youtu.be/AIlXnk47448>
#### Description
TESTIFY is an AI-powered quiz generation application designed to automatically create multiple-choice questions (MCQs) from user-provided text content. The project aims to simplify and enhance the learning and assessment process by transforming study material, notes, or documents into interactive quizzes. By leveraging modern generative AI models and an intuitive user interface, TESTIFY enables learners, educators, and students to assess understanding efficiently without manually creating questions.

In traditional learning environments, preparing quizzes is a time-consuming task that requires careful question framing, option design, and answer validation. TESTIFY addresses this challenge by automating quiz creation using a Large Language Model (LLM). Users simply paste their content, select a difficulty level, and the application generates a structured quiz along with scoring functionality. This makes the application particularly useful for self-study, exam preparation, and quick knowledge evaluation.

Objectives
The primary objectives of the TESTIFY project are:
To automate MCQ generation from textual content using artificial intelligence.
To provide an interactive and user-friendly quiz experience.
To allow users to assess their knowledge instantly through automated scoring.
To demonstrate practical integration of generative AI with a Python-based frontend.
To ensure modular, reusable, and scalable code architecture.


System Overview
TESTIFY is developed using Python as the core programming language. The user interface is built using Streamlit, a lightweight framework for creating interactive web applications. The AI-powered question generation is handled by Google Gemini, a generative AI model capable of understanding context and producing structured outputs.
The application workflow is divided into multiple stages:
Start Screen – Displays a welcome interface with a start button.
Input Stage – Users provide text content and select a quiz difficulty level (Easy, Medium, or Hard).
Quiz Generation – The AI model processes the input text and generates MCQs in a predefined JSON format.
Quiz Interaction – Users answer questions through radio buttons.
Evaluation – The system compares user answers with correct options and displays the final score.


Key Features
AI-Driven MCQ Generation:
TESTIFY uses generative AI to produce meaningful, non-repetitive multiple-choice questions based on the provided content.
Difficulty Level Selection:
Users can choose between Easy, Medium, and Hard difficulty levels, allowing adaptive assessment.
Interactive User Interface:
Streamlit provides real-time interactivity, enabling smooth navigation between screens without page reloads.
Automated Scoring System:
The application evaluates user responses instantly and displays the score along with correct answers.
Session State Management:
Streamlit’s session state ensures that user progress (start state, quiz generation, and answers) is preserved across reruns.
Modular Code Structure:
The AI logic is separated into an independent module (ai_service.py), making the application easier to maintain and extend.


Technologies Used
Python 3 – Core programming language.
Streamlit – Frontend framework for building interactive web apps.
Google Gemini API – Generative AI model for quiz creation.
JSON – Structured data format for MCQ representation.
dotenv – Secure management of API keys using environment variables.


Implementation Details
The quiz generation process is guided by a strict prompt template that instructs the AI model to return only valid JSON output. This ensures reliable parsing and prevents formatting issues. Error handling mechanisms are implemented to detect invalid AI responses and prompt the user to regenerate the quiz if necessary.
The application makes use of Streamlit’s session_state to manage navigation between the start screen and quiz screen. This prevents unintended resets caused by Streamlit’s rerun behavior and provides a seamless user experience.
Radio buttons are configured without preselection to ensure fair assessment. Once the user submits the quiz, the system compares the selected options with the correct answers and calculates the final score.

Use Cases
Students generating practice quizzes from lecture notes.
Teachers creating quick assessments from study material.
Self-learners evaluating understanding of technical topics.
AI demonstration projects showcasing real-world LLM integration.


Future Enhancements
Future improvements to TESTIFY may include:
User authentication and personalized quiz history.
Exporting quiz results as PDF or CSV files.
Timed quizzes and progress tracking.
Question randomization and answer shuffling.
Support for additional question types such as true/false or short answers.
Deployment as a fully hosted web application.

Conclusion
TESTIFY successfully demonstrates how generative AI can be applied to solve real-world educational challenges. By combining AI-driven content generation with an intuitive interface, the project provides a practical, scalable, and user-friendly solution for automated quiz creation. The modular architecture and clean design make it suitable for academic evaluation as well as future expansion into a full-fledged learning platform.

TODO
#run these commands to install the packages
# pip install -r requirements.txt

#if want to cerete environment(optional)
#run these command to install environment 
# python3 -m venv testify_env
# "testify_env\Scripts\Activate "  to Activate (windows)

#to run the app use this command
# "python -m streamlit run testify.py"