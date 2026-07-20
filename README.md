AI-Powered User Support System
=================================

A simple Flask-based AI-powered user support system with signup/login, AI chat, and ticketing.

Quick Start
-----------

1. Create a virtual environment and install dependencies:

```powershell
python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt
```

2. (Optional) Set environment variables in a `.env` file or your shell:

```
SECRET_KEY=your-secret-key
GEMINI_API_KEY=your-gemini-api-key  # optional, for AI features
```

3. Run the app:

```powershell
# Windows
py app.py
# or
set FLASK_APP=app.py
py -m flask run
```

How to Use
----------

- Open `http://127.0.0.1:5000/` in your browser.
- Create an account via `/signup`, then login at `/login`.
- Dashboard links:
	- AI Chat: `/chatbot` — interactive chat UI.
	- Create/View Tickets: `/tickets` and `/create-ticket` (API POST).
	- Logout: `/logout`.

API Endpoints
-------------
- `POST /chat` — JSON { "message": "..." } → returns `{ reply: "..." }`.
- `POST /create-ticket` — JSON { "name": "...", "issue": "..." } → returns ticket id and status.

Notes
-----
- The app uses an in-memory store for `users` and `tickets` by default. For production, replace with a persistent database.
- If `google.generativeai` is not installed or `GEMINI_API_KEY` is not set, the AI replies will return a service-unavailable message.

Want changes?
-------------
Tell me if you want the README expanded (Docker, CI, tests) or adjusted wording.
 