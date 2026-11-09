async function loadQuiz(chapterId) {
    const area = document.getElementById('quiz-area');
    area.innerHTML = "<div class='card'><p>Generating quiz from textbook content...</p></div>";

    const res = await fetch(`/api/quiz/${chapterId}`);
    const data = await res.json();
    renderQuizCard(data);
}

async function loadWeaknessDrill() {
    const area = document.getElementById('quiz-area');
    area.innerHTML = "<div class='card'><p>Generating targeted AI drill for your registered mistakes...</p></div>";

    const res = await fetch('/api/weak-spot-quiz');
    const data = await res.json();
    renderQuizCard(data);
}

function renderQuizCard(data) {
    const area = document.getElementById('quiz-area');
    area.innerHTML = `
        <div class="card" style="border: 2px solid #2563eb; background: #0f172a;">
            <span class="source-badge" style="color: #4ade80;">Active Session</span>
            <h3 style="margin-top: 6px;">${data.title}</h3>
            <p style="font-size: 16px; margin-bottom: 16px;"><b>Question:</b> ${data.question}</p>
            ${data.options.map(opt => `
                <button class="btn opt-btn" onclick="checkAnswer(this, '${opt}', '${data.correct}')">${opt}</button>
            `).join('')}
        </div>
    `;
    area.scrollIntoView({ behavior: 'smooth' });
}

function checkAnswer(btn, selected, correct) {
    const all = document.querySelectorAll('.opt-btn');
    all.forEach(b => b.disabled = true);

    if (selected === correct) {
        btn.classList.add('correct');
        alert("✅ Correct Answer! Progress recorded.");
    } else {
        btn.classList.add('wrong');
        alert(`❌ Incorrect! The system added this rule to your Weak Spots list.\nCorrect answer: ${correct}`);
    }
}