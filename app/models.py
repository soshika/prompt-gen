import openai
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class GPT(db.Model):

    API_KEY = str()

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), unique=False, nullable=False)
    answer = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.question}>'

    def __init__(self, question, API_KEY):
        self.API_KEY = API_KEY
        self.question = question
        self.answer = self.generate_qa(question)


    @staticmethod
    def generate_qa(prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the most suitable engine
            prompt=f"{prompt}\n\nGenerate questions:",
            temperature=0.5,
            max_tokens=256
        )
        
        return response.choices[0].text.strip()
        