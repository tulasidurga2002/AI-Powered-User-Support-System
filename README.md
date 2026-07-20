# AI Powered User Support System

## Project Overview

The AI Powered User Support System is a web-based application that provides instant customer support using Artificial Intelligence. It helps users get quick answers to their queries and allows them to create support tickets when their issues are not resolved by the AI chatbot.

## Problem Statement

Users often face delays and confusion while getting support because responses are slow and problems are not handled properly. This project aims to provide fast, accurate, and organized assistance through an AI-powered chatbot and support ticket system.

## Features

* AI-powered chatbot for instant user support
* Gemini AI integration for intelligent responses
* Real-time chat interface
* Typing animation while generating responses
* Support ticket generation for unresolved issues
* Professional light green user interface
* Responsive and user-friendly design

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Google Gemini AI API
* Python Dotenv

## Project Structure

AI-Powered-User-Support-System/

├── static/

│   ├── css/

│   │   └── style.css

│   ├── js/

│   │   └── script.js

│   └── images/

├── templates/

│   └── index.html

├── app.py

├── .env

├── requirements.txt

├── README.md

└── tickets.txt

## Installation and Setup

1. Clone or download the project.
2. Open the project folder in VS Code.
3. Create a virtual environment:
   py -m venv venv
4. Activate the virtual environment:
   venv\Scripts\activate
5. Install the required packages:
   py -m pip install flask google-generativeai python-dotenv
6. Add your Gemini API key in the .env file:
   GEMINI_API_KEY=your_api_key_here
7. Run the Flask application:
   py app.py
8. Open your browser and visit:
   http://127.0.0.1:5000

## How It Works

1. The user enters a support query in the chatbot.
2. The query is sent to the Flask backend.
3. Gemini AI generates an intelligent response.
4. The response is displayed in the chat interface.
5. If the issue is not resolved, the user can create a support ticket.
6. The ticket details are stored in a text file for future reference.

## Expected Output

* Users receive instant AI-generated responses.
* Common support queries are resolved quickly.
* Unresolved issues are converted into support tickets.
* The system provides a professional and organized support experience.

## Future Enhancements

* Store tickets in a database
* Add user authentication
* Implement ticket status tracking
* Add admin dashboard for managing tickets
* Improve AI response accuracy with a custom knowledge base

## Author
BY TEAM 2 
1. V.NEHA
2. R.ANANTHA
3. G.TULASI 
4. M.LALITHA
5. D.PRAHARSHITHA

B.Tech AIML Student, Kakinada Institute of Engineering and Technology for Women

---

This project was developed as a college mini-project to demonstrate the use of Artificial Intelligence in customer support systems.
