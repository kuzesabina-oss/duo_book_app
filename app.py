from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

TEXTBOOK_DATA = {
    "title": "Oxford Business English Coursebook",
    "total_chapters": 10,
    "current_chapter": 4,
    "progress_percent": 40,
    "language_metrics": {
        "vocabulary_mastered": 142,
        "grammar_accuracy": "76%",
        "active_retention_rate": "Good"
    },
    "weak_spots": [
        {"topic": "Present Perfect vs Past Simple", "error_count": 3},
        {"topic": "Vocabulary: 'Negotiation Terms'", "error_count": 2}
    ],
    "chapters": [
        {
            "id": 1,
            "title": "Module 1: Professional Greetings",
            "type": "Curriculum Lesson",
            "question": "Which phrase is used for formal email greetings based on Chapter 1?",
            "options": ["Dear Mr. Smith,", "Hey buddy,", "What's up!", "Cheers,"],
            "correct": "Dear Mr. Smith,"
        },
        {
            "id": 4,
            "title": "Module 4: Business Negotiations (Current Topic)",
            "type": "Curriculum Lesson",
            "question": "According to page 45 of your textbook, what does 'Counter-offer' mean?",
            "options": ["An alternative proposal", "Accepting the price", "Canceling the deal", "Signing a contract"],
            "correct": "An alternative proposal"
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=TEXTBOOK_DATA)

@app.route('/api/quiz/<int:chapter_id>')
def get_quiz(chapter_id):
    chapter = next((c for c in TEXTBOOK_DATA['chapters'] if c['id'] == chapter_id), None)
    if chapter:
        return jsonify(chapter)
    return jsonify({"error": "Chapter not found"}), 404

@app.route('/api/weak-spot-quiz')
def get_weak_spot_quiz():
    return jsonify({
        "id": 99,
        "title": "⚡ AI Weakness Drill (Targeted Practice)",
        "type": "Adaptive AI Review",
        "question": "AI Review based on your 3 past errors: Choose the correct form for completed action with present relevance:",
        "options": ["We have finalized the deal.", "We finalize the deal yesterday.", "We finalized tomorrow.", "We finalizing now."],
        "correct": "We have finalized the deal."
    })

# Вот этого блока у вас не хватало в самом низу:
if __name__ == '__main__':
    app.run(debug=True)