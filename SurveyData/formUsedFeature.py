import matplotlib.pyplot as plt 

# Data: AI-funktioner och antal svar
labels = ['Personalized match recommendation', 
          'AI-powered chatbot for quick support and ticket inquiries', 
          'AI-generated highlights based on your interests', 
          'AI commentator tailored to your interests', 
          'Real-time analysis of players', 
          'AI coach providing tips for training', 
          'Other',  # Namnet ändrat här
          'I don\'t know if I have come across this feature']

# Antal svar för varje funktion
responses = [8, 7, 9, 6, 14, 2, 6 + 10, 16]  # Kombinerat Other och None of the above (6 + 10)

# Antal unika respondenter (baserat på din beskrivning)
unique_respondents = 52

# Procentandelar baserat på antalet unika respondenter
percentages_unique = [(response / unique_respondents) * 100 for response in responses]

# Skapa diagrammet med en större storlek
plt.figure(figsize=(10, 8))  # Justerat till en större storlek
bars = plt.barh(labels, responses, color='skyblue')
plt.xlabel('Antal användare')

# Lägg till titel högre upp
plt.title('Which of the following AI features have you used or encountered?', pad=10)  # pad ökar avståndet från toppen

# Lägg till text om antal svar som en liten paragraf
plt.figtext(0.49, 0.93, '52 svar', ha='center', va='center', fontsize=12, color='grey')

plt.gca().invert_yaxis()  # För att ha den högsta värdet överst

# Lägg till antal och procent efter varje stapel
for bar, response, percentage in zip(bars, responses, percentages_unique):
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2, 
             f'{response} ({percentage:.1f}%)', va='center', ha='left', color='black')

# Lägg till L-formade axlar
ax = plt.gca()
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

# Ta bort de andra kanterna runt diagrammet
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Justera för att göra plats för y-axeltexten
plt.tight_layout()

# Visa diagrammet
plt.show()
