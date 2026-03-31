# Chatbot for Student Queries

A web-based AI chatbot built with Python Flask, NLTK, HTML, CSS, and JavaScript. The bot answers common student queries like course details, college timings, fees, hostel facilities, and contact information.

## Prerequisites
- Python 3.8 or above installed on your computer.

## Installation and Running Steps

1. **Open a Terminal or Command Prompt**.
2. **Navigate to the project folder**:
   ```bash
   cd student_chatbot
   ```
3. **Install the required dependencies**:
   Run the following command to install Flask and NLTK:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask application**:
   ```bash
   python app.py
   ```
   *(Note: The first time you run the app, it will download necessary NLTK datasets in the terminal output. This will only happen once.)*
   
5. **Open the Chatbot in Browser**:
   Open a web browser such as Chrome, Firefox, or Edge and go to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Sample Chatbot Conversation Output

**Bot**: Hello! Welcome to the college inquiry bot. How can I help you today? Try asking about courses, fees, or timings.
**User**: What are the available courses?
**Bot**: We offer B.Tech in Computer Science (CSE), Electronics and Communication (ECE), Mechanical Engineering (ME), and Civil Engineering (CE). We also offer MBA and MCA programs.
**User**: What are the college timings?
**Bot**: The college timings are from 9:00 AM to 4:00 PM, Monday to Friday. The campus is closed for classes on weekends, but the library remains open.
**User**: Thanks!
**Bot**: You're welcome!

## Screenshots Required for Project Submission

Make sure to take screenshots of the following for your documentation/viva presentation:
1. **Command Prompt / Terminal**: Showing the Flask server running (`* Running on http://127.0.0.1:5000`).
2. **Web Interface**: The clean UI right when you open the page in the browser (with the default greeting).
3. **Conversation Flow**: A screenshot demonstrating the user asking a question (e.g., "Tell me about the fees") and the bot replying.
4. **Error Handling (Optional)**: If you type unstructured gibberish, show the bot's default fallback response ("I'm sorry, I don't quite understand...").
