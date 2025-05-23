import pandas as pd
import matplotlib.pyplot as plt

# Uppdaterad data: 52 med ålder, 48 med AI_Knowledge
data = [
    ("18–29", "No"), ("18–29", "Yes"), ("18–29", "Yes"), ("18–29", "Yes"),
    ("18–29", "No"), ("18–29", "Yes"), ("45–59", "Yes"), ("18–29", "Yes"),
    ("18–29", "Yes"), ("18–29", "No"), ("18–29", "Yes"), ("18–29", "No"),
    ("18–29", "No"), ("18–29", "No"), ("18–29", "No"), ("18–29", "No"),
    ("18–29", "Yes"), ("18–29", "No"), ("18–29", "No"), ("Under 18", "No"),
    ("60 or older", "No"), ("45–59", "No"), ("18–29", "No"), ("18–29", "Yes"),
    ("18–29", "No"), ("45–59", "Yes"), ("30–44", "No"), ("45–59", "No"),
    ("45–59", "No"), ("60 or older", "No"), ("18–29", "No"), ("18–29", "No"),
    ("30–44", "No"), ("18–29", "Yes"), ("18–29", "Yes"), ("30–44", "No"),
    ("18–29", "No"), ("45–59", "Yes"), ("18–29", "Yes"), ("18–29", "No"),
    ("30–44", "No"), ("18–29", "No"), ("60 or older", "No"), ("18–29", "Yes"),
    ("18–29", "Yes"), ("18–29", "No"), ("Under 18", "No"), ("18–29", "No"),
    
    # 4 personer med ålder men inget AI-svar
    ("18–29", None), ("30–44", None), ("45–59", None), ("60 or older", None)
]

# Skapa DataFrame
df = pd.DataFrame(data, columns=["Age", "AI_Knowledge"])

# Rensa specialtecken och mellanslag
df['Age'] = df['Age'].str.replace('–', '-', regex=False)
df['Age'] = df['Age'].str.strip()

# Visa rader med saknad AI_Knowledge
missing_data = df[df['AI_Knowledge'].isnull()]
print(f"Antal rader med saknad AI_Knowledge: {len(missing_data)}")
print("Rader med saknad AI_Knowledge:")
print(missing_data)

# Filtrera bort rader utan AI_Knowledge
df_clean = df.dropna(subset=['AI_Knowledge'])

# Räkna Yes/No per åldersgrupp
age_counts = df_clean.groupby('Age')['AI_Knowledge'].value_counts().unstack(fill_value=0)

# Sortera åldersgrupper i rätt ordning
age_order = ['Under 18', '18-29', '30-44', '45-59', '60 or older']
age_counts = age_counts.reindex(age_order)

# Rita stapeldiagram
ax = age_counts.plot(kind='bar', stacked=True, figsize=(10, 6), color=['lightcoral', 'skyblue'])
plt.title('Do you know that AI is used for fan interaction in sports?')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(['No', 'Yes'], title='AI Knowledge')

# Lägg till etiketter på staplarna
for p in ax.patches:
    height = p.get_height()
    if height > 0:
        x = p.get_x() + p.get_width() / 2
        y = p.get_y() + height / 2
        ax.annotate(f'{int(height)}', (x, y), ha='center', va='center', color='black')

plt.tight_layout()
plt.show()

# Sammanfattning
print("Totalt antal svar med både ålder och AI knowledge:", len(df_clean))  # 48
print("Totalt antal personer som angav ålder:", len(df))  # 52
