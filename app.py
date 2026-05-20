from flask import Flask, render_template, request

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Academics Route
@app.route('/academics')
def academics():
    return render_template('academics.html')

# Contact Us Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Handle the contact form submission (save to database, send email, etc.)
        return render_template('contact.html', success=True)
    return render_template('contact.html')

# Gallery Route
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Teachers Pillars Route
@app.route('/teachers')
def teachers():
    return render_template('teachers.html')

if __name__ == '__main__':
    app.run(debug=True)
