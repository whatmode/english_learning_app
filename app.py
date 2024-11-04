from flask import Flask, render_template, request

english_learning_app = Flask(__name__)

lessons = {
    "grammar": "Grammar Basics: Subject-Verb Agreement, Tenses, etc.",
    "vocabulary": "Vocabulary Basics: Common Words, Synonyms, Antonyms, etc."
}


# Sample quiz questions
quiz_questions = [
    {"id": 0, "question": "What is the plural form of 'child'?", "answer": "children"},
    {"id": 1, "question": "What is the opposite of 'hot'?", "answer": "cold"},
    {"id": 2, "question": "Fill in the blank: She ___ to the store yesterday.", "answer": "went"}
]


@english_learning_app.route('/')
def home():
    return render_template('index.html', lessons=lessons)

@english_learning_app.route('/lesson/<topic>')
def lesson(topic):
    # Retrieve lesson content based on the topic
    content = lessons.get(topic, "Lesson not found.")
    return render_template('lesson.html',
                           topic=topic.capitalize(),
                           content=content)


@english_learning_app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Handle quiz submission
    if request.method == 'POST':
        score = 0
        user_answers = {}

        # Collect user answers and calculate the score
        for question in quiz_questions:
            user_answer = request.form.get(f"q{question['id']}", "").strip().lower()
            correct_answer = question["answer"].lower()
            user_answers[question['id']] = user_answer

            # Check if the answer is correct
            if user_answer == correct_answer:
                score += 1

        # Render results with score and user answers
        return render_template('quiz.html',
                               questions=quiz_questions,
                               user_answers=user_answers,
                               score=score,
                               submitted=True)

    # Render the quiz form initially
    return render_template('quiz.html',
                           questions=quiz_questions,
                           submitted=False)

if __name__ == '__main__':
    english_learning_app.run()
