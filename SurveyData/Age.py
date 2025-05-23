import matplotlib.pyplot as plt
from collections import Counter

# Fullständig lista med 52 röster
ages = [
    "18–29", "18–29", "18–29", "18–29", "18–29", "18–29", "18–29", "18–29", "18–29", "18–29",
    "45–59", "18–29", "18–29", "18–29", "18–29", "18–29", "18–29", "18–29", "18–29", "18–29",
    "18–29", "18–29", "Under 18", "60 or older", "45–59", "18–29", "18–29", "18–29", "45–59",
    "30–44", "45–59", "45–59", "60 or older", "18–29", "18–29", "30–44", "18–29", "18–29",
    "30–44", "18–29", "45–59", "18–29", "18–29", "30–44", "18–29", "60 or older", "18–29",
    "18–29", "18–29", "Under 18", "18–29", "18–29"
]

# Kontroll: Totalt antal röster
total_votes = len(ages)
assert total_votes == 52, f"Förväntade 52 röster, men fick {total_votes}"

# Räkna rösterna
age_counts = Counter(ages)

# Åldersgrupper i önskad ordning
age_order = ["Under 18", "18–29", "30–44", "45–59", "60 or older"]
counts_ordered = [age_counts[age] for age in age_order]
percentages = [f"{(count / total_votes) * 100:.1f}%" for count in counts_ordered]

# Skapa stapeldiagram
plt.figure(figsize=(9, 6))
bars = plt.bar(age_order, counts_ordered, color="#4A90E2")
plt.title("Antal röster per åldersgrupp")
plt.xlabel("Åldersgrupp")
plt.ylabel("Antal röster")
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Lägg till antal och procent över varje stapel
for bar, count, percent in zip(bars, counts_ordered, percentages):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
             f"{count} ({percent})", ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
