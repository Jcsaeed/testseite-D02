from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def handle_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    print("New contact form submission:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    return "Message received successfully."

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
