from collections import Counter
import matplotlib.pyplot as plt

# Råa svar (förenklade exempel)
responses_raw = [
    "TV",
    "TV, Streaming platforms (e.g. YouTube, DAZN, etc.), Social media (e.g. Instagram, X/Twitter, TikTok), Sports apps (e.g. ESPN, Bleacher Report)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "TV, Social media (e.g. Instagram, X/Twitter, TikTok), At live events/stadiums",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.), Sports apps (e.g. ESPN, Bleacher Report)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok), Sports apps (e.g. ESPN, Bleacher Report)",
    "Social media (e.g. Instagram, X/Twitter, TikTok)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Sports apps (e.g. ESPN, Bleacher Report)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok), At live events/stadiums",
    "Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV, Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV, Sports apps (e.g. ESPN, Bleacher Report)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV, Social media (e.g. Instagram, X/Twitter, TikTok)",
    "At live events/stadiums",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok), Sports apps (e.g. ESPN, Bleacher Report)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok), Sports apps (e.g. ESPN, Bleacher Report)",
    "TV, Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV",
    "TV, At live events/stadiums",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), At live events/stadiums",
    "TV",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok), At live events/stadiums",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "TV",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV, Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok)",
    "TV, Streaming platforms (e.g. YouTube, Viaplay, etc.), Social media (e.g. Instagram, X/Twitter, TikTok), Sports apps (e.g. ESPN, Bleacher Report), At live events/stadiums",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
]

# Definiera kategorier
categories = [
    "TV",
    "Streaming platforms (e.g. YouTube, Viaplay, etc.)",
    "Social media (e.g. Instagram, X/Twitter, TikTok)",
    "Sports apps (e.g. ESPN, Bleacher Report)",
    "At live events/stadiums"
]

# Räkna varje förekomst per kategori
counter = Counter()
for response in responses_raw:
    for category in categories:
        if category in response:
            counter[category] += 1

# Sortera data i fördefinierad ordning
responses = [counter[category] for category in categories]
unique_respondents = len(responses_raw)
percentages = [(r / unique_respondents) * 100 for r in responses]

# Rita diagram
plt.figure(figsize=(10, 8))
bars = plt.barh(categories, responses, color='skyblue')
plt.xlabel('Antal användare')
plt.title('Where do you usually follow sports? (You can select more than one)', pad=10)

# Text ovanför
plt.figtext(0.545, 0.93, f'{unique_respondents} svar', ha='center', va='center', fontsize=12, color='grey')

# Vänd y-axeln
plt.gca().invert_yaxis()

# Lägg till text till höger om staplarna
for bar, count, percent in zip(bars, responses, percentages):
    plt.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
             f'{count} ({percent:.1f}%)', va='center', ha='left')

# L-formade axlar
ax = plt.gca()
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
