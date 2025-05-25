import matplotlib.pyplot as plt
from collections import Counter

# Fördefinierad ordning på AI-funktionerna
ai_features_ordered = [
    "Personalized match recommendations",
    "AI-generated highlights based on your interests",
    "AI commentator tailored to your knowledge level (beginner/expert)",
    "Real-time analysis of players and teams",
    "AI coach providing tips for training or fantasy leagues",
    "AI-powered chatbot for quick support and ticket inquiries",
    "Other"
]

# Råa fritextsvar från enkäten
responses_raw = [
    "Personalized match recommendations",
    "AI-generated highlights based on your interests, Real-time analysis of players and teams",
    "Real-time analysis of players and teams",
    "AI-generated highlights based on your interests",
    "AI-generated highlights based on your interests",
    "AI-generated highlights based on your interests",
    "Other",
    "Real-time analysis of players and teams",
    "Personalized match recommendations, AI commentator tailored to your knowledge level (beginner/expert), AI-powered chatbot for quick support and ticket inquiries",
    "AI-generated highlights based on your interests, Real-time analysis of players and teams, Other",
    "Real-time analysis of players and teams",
    "Personalized match recommendations, AI-generated highlights based on your interests, AI commentator tailored to your knowledge level (beginner/expert)",
    "Real-time analysis of players and teams",
    "Real-time analysis of players and teams, AI coach providing tips for training or fantasy leagues",
    "Other",
    "Personalized match recommendations",
    "AI-generated highlights based on your interests",
    "AI commentator tailored to your knowledge level (beginner/expert)",
    "Personalized match recommendations, AI-generated highlights based on your interests, Real-time analysis of players and teams",
    "Personalized match recommendations",
    "Other",
    "Real-time analysis of players and teams, AI coach providing tips for training or fantasy leagues",
    "Other",
    "Other",
    "Other",
    "AI-generated highlights based on your interests",
    "Other",
    "AI-powered chatbot for quick support and ticket inquiries",
    "Real-time analysis of players and teams",
    "Other",
    "AI-generated highlights based on your interests",
    "AI commentator tailored to your knowledge level (beginner/expert)",
    "Other",
    "AI-generated highlights based on your interests, Real-time analysis of players and teams",
    "Personalized match recommendations, AI-generated highlights based on your interests, Real-time analysis of players and teams",
    "Personalized match recommendations",
    "Personalized match recommendations, AI-generated highlights based on your interests, Real-time analysis of players and teams, AI-powered chatbot for quick support and ticket inquiries",
    "AI-generated highlights based on your interests",
    "Other",
    "Other",
    "AI-generated highlights based on your interests, AI coach providing tips for training or fantasy leagues",
    "Real-time analysis of players and teams",
    "Real-time analysis of players and teams, Other",
    "AI-generated highlights based on your interests",
    "AI-generated highlights based on your interests, AI commentator tailored to your knowledge level (beginner/expert)",
    "AI-generated highlights based on your interests, AI commentator tailored to your knowledge level (beginner/expert)",
    "AI-generated highlights based on your interests",
    "AI-generated highlights based on your interests, Real-time analysis of players and teams",
    "AI-generated highlights based on your interests, AI commentator tailored to your knowledge level (beginner/expert)"
]

# Räkna hur ofta varje funktion nämns
counter = Counter()
for response in responses_raw:
    for feature in ai_features_ordered:
        if feature in response:
            counter[feature] += 1

# Skapa listor i rätt ordning
responses_count = [counter[feature] for feature in ai_features_ordered]
unique_respondents = 49
percentages = [(count / unique_respondents) * 100 for count in responses_count]

# Rita diagrammet
plt.figure(figsize=(10, 8))
bars = plt.barh(ai_features_ordered, responses_count, color='#87CEEB')  # ljusblå färg

# Etiketter och titel
plt.xlabel('Antal användare')
plt.title('Which AI feature is your favourite or the most useful to you?', pad=10)
plt.figtext(0.545, 0.93, f'{unique_respondents} svar', ha='center', va='center', fontsize=12, color='grey')

# Vänd y-axeln så den mest populära hamnar högst upp
plt.gca().invert_yaxis()

# Lägg till siffror till höger om varje stapel
for bar, count, percent in zip(bars, responses_count, percentages):
    plt.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
             f'{count} ({percent:.1f}%)', va='center', ha='left')

# Visa endast vänster och nedre axellinje
ax = plt.gca()
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
