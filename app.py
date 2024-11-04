from flask import Flask, render_template, request, redirect, url_for


english_learning_app = Flask(__name__)

lessons = {
    "grammar": "Grammar Basics: Subject-Verb Agreement, Tenses, etc.",
    "vocabulary": "Vocabulary Basics: Common Words, Synonyms, Antonyms, etc."
}

quiz_questions = [
    {"question": "What is the plural form of 'child'", "answer": "children"},
    {"question": "What is the opposite of 'hot'?", "answer": "cold"}
]

@english_learning_app.route("/")
def home():
    print("Home page accessed")
    return render_template("index.html", lessons=lessons)

@english_learning_app.route("/lessons/<topic>")
def lesson(topic):
    content = lessons.get(topic, "Lesson not found")
    return render_template("lesson.html", topic=topic.capitalize(), content=content)

if __name__ == "__main__":
    english_learning_app.run()
