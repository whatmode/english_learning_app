from flask import Flask, render_template, request

english_learning_app = Flask(__name__)

# Expanded lessons content
lessons = {
    "grammar": {
        "title": "Grammar Basics",
        "description": "Understanding the foundational 
        rules of English grammar.",
        "content": """
        <h3>1. Subject-Verb Agreement</h3>
        <p>The subject and verb in a sentence 
        must agree in number (singular or plural).</p>
        <ul>
            <li>
            <strong>Correct:</strong> 
            She <em>runs</em> every morning.
            </li>
            <li>
            <strong>Incorrect:</strong> 
            She <em>run</em> every morning.
            </li>
        </ul>

        <h3>2. Tenses</h3>
        <p>Tenses indicate the timing 
        of actions (past, present, future).</p>
        <ul>
            <li>Present Simple: I <em>walk</em>.</li>
            <li>Past Simple: I <em>walked</em>.</li>
            <li>Future Simple: I <em>will walk</em>.</li>
        </ul>
        """
    },
    "vocabulary": {
        "title": "Vocabulary Basics",
        "description": "Learning common words, 
        synonyms, and antonyms.",
        "content": """
        <h3>1. Synonyms and Antonyms</h3>
        <p>Synonyms are words with similar meanings, 
        while antonyms are words with opposite meanings.</p>
        <ul>
            <li>Synonym of <em>happy</em>: joyful, content</li>
            <li>Antonym of <em>happy</em>: sad, unhappy</li>
        </ul>

        <h3>2. Commonly Confused Words</h3>
        <p>Words that sound similar but have different meanings.</p>
        <ul>
            <li><strong>Accept</strong> vs. <strong>Except</strong></li>
            <li><strong>Effect</strong> vs. <strong>Affect</strong></li>
        </ul>
        """
    }
}

# Sample quiz questions
quiz_questions = [
    {"id": 0, 
    "question": "What is the plural form of 'child'?", 
    "answer": "children"},
    {"id": 1, 
    "question": "What is the opposite of 'hot'?", 
    "answer": "cold"},
    {"id": 2, 
    "question": "Fill in the blank: She ___ to the store yesterday.", 
    "answer": "went"}
]

@english_learning_app.route('/')
def home():
    return render_template('index.html', lessons=lessons)

@english_learning_app.route('/lesson/<topic>')
def lesson(topic):
    # Retrieve lesson content based on the topic
    lesson_content = lessons.get(topic)
    if lesson_content:
        return render_template('lesson.html', 
        title=lesson_content["title"], 
        content=lesson_content["content"])
    else:
        return "Lesson not found.", 404

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
