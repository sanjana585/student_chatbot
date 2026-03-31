# MINI PROJECT REPORT

## 1. Title Page
**Project Title**: Chatbot for Student Queries  
**Domain**: Web Application, Artificial Intelligence (NLP)  
**Submitted By**: [Your Name/Team Names]  
**Course**: B.Tech  
**Department**: [Your Department Name]  

---

## 2. Abstract
The "Chatbot for Student Queries" is a web-based artificial intelligence application designed to automate responses to frequently asked student inquiries. Educational institutions deal with a massive influx of repetitive questions regarding admissions, fee structures, courses, timings, and facilities. This project implements an NLP-powered chatbot using Python, Flask, and the NLTK library to parse user inputs, recognize intents, and fetch appropriate answers from a predefined knowledge base. The frontend provides an intuitive chat interface constructed using HTML, CSS, and JavaScript, creating a seamless user experience similar to modern messaging applications.

---

## 3. Introduction
In today's fast-paced digital era, instant access to information is crucial. Prospective and current students often require quick answers to queries without wanting to navigate through exhaustive college websites or wait for administrative office hours. This project addresses this need by developing an AI-driven chatbot capable of handling text-based conversations. It bridges the communication gap between the institution and the student body.

---

## 4. Problem Statement
College administration offices are frequently overwhelmed by routine queries from students and parents. This manual handling of identical questions consumes valuable human resources and time. Furthermore, students face delays in receiving critical information outside of regular office hours. There is a clear need for an automated, 24/7 accessible system to address these queries efficiently.

---

## 5. Objectives
- To develop an intuitive web-based chat interface for user interaction.
- To build a backend system that can process natural language questions.
- To implement intent recognition using NLP concepts like tokenization and lemmatization.
- To provide instant, accurate responses to common college-related queries.
- To create a scalable knowledge base (JSON format) that can be easily updated without changing code.

---

## 6. Tools and Technologies
- **Backend**: Python 3, Flask framework
- **NLP Library**: NLTK (Natural Language Toolkit)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data Storage**: JSON (JavaScript Object Notation)
- **Environment**: Local web server (Werkzeug)

---

## 7. System Architecture
The system follows a typical Client-Server architecture:
1. **Client (Browser)**: Contains the UI and handles taking input and rendering message bubbles. Sends AJAX/Fetch POST requests to the server.
2. **Web Server (Flask)**: Receives the user's message via a REST API endpoint (`/get_response`).
3. **NLP Engine**: The backend tokenizes the text, lemmatizes the words, and computes scores against known patterns.
4. **Knowledge Base**: The `qa_pairs.json` file which acts as the database for intents, patterns (sample questions), and corresponding responses.

---

## 8. Implementation Details
- **Frontend**: The chat UI is styled using modern CSS variables with flexbox. JavaScript handles DOM manipulation, creating new message divs for the user and bot, and showing a "typing..." indicator before responses.
- **Backend API**: The Flask app hosts a single route (`/`) serving `index.html`, and one API endpoint (`/get_response`) which receives JSON payloads.
- **NLP Logic**: The user's sentence is split into words (tokenization) and reduced to base forms (lemmatization using `WordNetLemmatizer`). A pattern matching algorithm uses set overlap to count matching words with each predefined intent. The intent with the highest overlap score is selected, and a randomly selected response from that tag is returned.

---

## 9. Algorithm / Flowchart
**Algorithm:**
1. **Start**.
2. Load knowledge base from JSON file into memory.
3. Wait for HTTP request on `/get_response`.
4. Extract user message string from request payload.
5. Apply NLP formatting: Tokenize string, Lemmatize tokens.
6. Initialize score for each possible intent category to 0.
7. Iterate through all patterns of each intent class:
   - Find common words between user input and pattern.
   - Increment intent score by the number of matches.
8. Find the intent with the Maximum Score.
9. If Maximum Score > 0, pick a random response from that intent. Else, pick default fallback response.
10. Return response as JSON to frontend.
11. **End**.

---

## 10. Sample Output
- **User**: "What are the library timings?"
- **Bot**: "The central library is open from 8:00 AM to 8:00 PM on weekdays, and from 10:00 AM to 4:00 PM on weekends."
- **User**: "Tell me about tuition fees"
- **Bot**: "B.Tech fees are $5000/year. Scholarships are available for meritorious students."

---

## 11. Advantages
- **24/7 Availability**: Can assist students anytime relative to office hours.
- **Cost-Effective**: Reduces the administrative workload drastically.
- **Instantaneous**: Responds in milliseconds.
- **Easily Extensible**: Adding new Q&A pairs only requires editing the JSON file.

---

## 12. Future Enhancements
- Integrating Machine Learning models (like Neural Networks or Transformers) for more accurate intent classification than simple keyword matching.
- Integrating a database (like MySQL or MongoDB) to store chat histories and analyze frequently asked questions.
- Adding Voice Recognition so students can speak their questions instead of typing.
- Connecting the chatbot directly to the student portal to provide personalized data (e.g., student's attendance or grades).

---

## 13. Conclusion
The "Chatbot for Student Queries" successfully demonstrates the practical application of Natural Language Processing and web development to solve a real-world administrative problem. By combining a lightweight Flask backend with a responsive frontend design, the project provides a highly interactive and user-friendly automated assistant capable of managing routine inquiries efficiently.

---

## 14. References
1. NLTK Documentation: https://www.nltk.org/
2. Flask Framework Documentation: https://flask.palletsprojects.com/
3. MDN Web Docs (JavaScript, Fetch API, Flexbox): https://developer.mozilla.org/
