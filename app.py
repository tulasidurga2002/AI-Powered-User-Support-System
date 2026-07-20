from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
from dotenv import load_dotenv

try:
    import google.generativeai as genai
except ImportError:
    genai = None

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')

users = {}
tickets = []
ticket_counter = 1

if genai is not None:
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    model = None

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        if users.get(username) == password or (username == 'admin' and password == 'admin123'):
            session['user'] = username
            return redirect(url_for('dashboard'))
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html', error=None)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        if not username or not password:
            return render_template('signup.html', message='Please enter both username and password')
        if username in users:
            return render_template('signup.html', message='Username already exists')
        users[username] = password
        session['user'] = username
        return redirect(url_for('dashboard'))
    return render_template('signup.html', message=None)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/chatbot')
def chatbot():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/tickets')
def tickets_page():
    if 'user' not in session:
        return redirect(url_for('login'))
    user_tickets = [ticket for ticket in tickets if ticket['username'] == session['user']]
    return render_template('tickets.html', tickets=user_tickets)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get('message', '')
    if not user_message:
        return jsonify({'reply': 'Please enter a message.'})
    if model is None:
        return jsonify({'reply': 'AI service is unavailable in this environment.'})
    try:
        response = model.generate_content(user_message)
        return jsonify({'reply': response.text})
    except Exception:
        return jsonify({'reply': 'AI service unavailable'})

@app.route('/create-ticket', methods=['POST'])
def create_ticket():
    if 'user' not in session:
        return jsonify({'status': 'error', 'message': 'Please login to create a ticket.'}), 401
    data = request.get_json(silent=True) or {}
    name = data.get('name', '').strip()
    issue = data.get('issue', '').strip()
    if not name or not issue:
        return jsonify({'status': 'error', 'message': 'Name and issue are both required.'}), 400
    global ticket_counter
    ticket_id = ticket_counter
    ticket_counter += 1
    ticket = {'id': ticket_id, 'username': session['user'], 'name': name, 'issue': issue, 'status': 'Open'}
    tickets.append(ticket)
    print('Ticket Created')
    print('Ticket ID:', ticket_id)
    print('Username:', session['user'])
    print('Name:', name)
    print('Issue:', issue)
    return jsonify({'status': 'success', 'message': 'Support ticket created successfully!', 'ticket_id': ticket_id})

if __name__ == '__main__':
    app.run(debug=True)
