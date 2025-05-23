import pandas as pd
import matplotlib.pyplot as plt

# Data: (AI_improves_fan_experience, Age)
data = [
    ("Yes", "18–29"), ("Yes", "18–29"), ("No", "18–29"), ("Yes", "18–29"),
    ("Yes", "18–29"), ("Yes", "18–29"), ("Yes", "18–29"), ("No", "18–29"),
    ("Yes", "18–29"), ("Yes", "18–29"), ("Yes", "45–59"), ("Yes", "18–29"),
    ("Yes", "18–29"), ("No", "18–29"), ("Yes", "18–29"), ("No", "18–29"),
    ("Yes", "18–29"), ("Yes", "18–29"), ("No", "18–29"), ("Yes", "18–29"),
    ("Yes", "18–29"), ("No", "18–29"), ("Yes", "Under 18"), ("No", "60 or older"),
    ("No", "45–59"), ("No", "18–29"), ("Yes", "18–29"), ("Yes", "18–29"),
    ("Yes", "45–59"), ("No", "30–44"), ("No", "45–59"), ("No", "45–59"),
    ("No", "60 or older"), ("No", "18–29"), ("Yes", "18–29"), ("No", "30–44"),
    ("Yes", "18–29"), ("No", "18–29"), ("Yes", "30–44"), ("No", "18–29"),
    ("Yes", "45–59"), ("Yes", "18–29"), ("No", "18–29"), ("Yes", "30–44"),
    ("Yes", "18–29"), ("Yes", "60 or older"), ("Yes", "18–29"), ("Yes", "18–29"),
    ("No", "18–29"), ("No", "Under 18"), ("No", "18–29"), ("Yes", "18–29")
]

# Skapa DataFrame
df = pd.DataFrame(data, columns=["AI_Fan_Experience", "Age"])

# Rensa specialtecken och mellanslag
df['Age'] = df['Age'].str.replace('–', '-', regex=False)
df['Age'] = df['Age'].str.strip()

# Ta bort eventuella rader med saknade värden
df_clean = df.dropna(subset=['AI_Fan_Experience', 'Age'])

# Räkna Yes/No per åldersgrupp
age_counts = df_clean.groupby('Age')['AI_Fan_Experience'].value_counts().unstack(fill_value=0)

# Sortera åldersgrupper i rätt ordning
age_order = ['Under 18', '18-29', '30-44', '45-59', '60 or older']
age_counts = age_counts.reindex(age_order)

# Rita stapeldiagram
ax = age_counts.plot(kind='bar', stacked=True, figsize=(10, 6), color=['lightcoral', 'skyblue'])
plt.title('Do you feel like AI features improve the fan experience for your favourite sports?')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(['No', 'Yes'], title='AI Fan Experience')

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
print("Totalt antal svar:", len(df_clean))
print(df_clean['Age'].value_counts().sort_index())
