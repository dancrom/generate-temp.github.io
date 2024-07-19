import json
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///templates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Template model
class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_urls = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Template {self.title}>"
    
    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image_urls': json.loads(self.image_urls)  # Convert JSON string back to list
        }

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to save a new template
@app.route('/save_template', methods=['POST'])
def save_template():
    data = request.json
    new_template = Template(
        title=data['title'],
        description=data['description'],
        image_urls=json.dumps(data['image_urls'])  # Convert list to JSON string
    )
    db.session.add(new_template)
    db.session.commit()
    return jsonify({"message": "Template saved successfully!"}), 201

# Route to retrieve saved templates
@app.route('/get_templates', methods=['GET'])
def get_templates():
    templates = Template.query.all()
    return jsonify([template.as_dict() for template in templates]), 200

# Route to serve the form to create a template
@app.route('/')
def create_template_form():
    username = request.form['username']
    password = request.form['password']

    if username != 'pbtc' or password != 'PbTc150224!':
        return render_template('index.html')
    else:
        return render_template('generate.html')

# Route to view saved templates
@app.route('/view_templates')
def view_templates():
    return render_template('view_templates.html')

if __name__ == '__main__':
    app.run(debug=True)

