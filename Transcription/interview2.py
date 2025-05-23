import pandas as pd
from keybert import KeyBERT

# Förkortningslista
abbreviations = {
    # Bakgrund och roll
    "IBM": "Roll",
    "Sports and Entertainment Partnerships": "Roll",
    "Fred Baker": "Roll",
    "Consulting": "Roll",

    # Användning av AI i praktiken
    "AI-narration": "Funktion",
    "Hole Insights": "Funktion",
    "AutoAI": "Funktion",
    "Watson Studio": "Funktion",
    "AI features": "Funktion",
    "AI tools": "Funktion",
    "Personalized content": "Funktion",
    "Personalization": "Funktion",
    "personalized": "Funktion",
    "AI voices": "Funktion",
    "Live commentary": "Funktion",
    "AI assistant": "Funktion",

    # Mätning och effekt
    "cost efficiency": "Mätning",
    "financial motivation": "Mätning",

    # Dataanvändning och appstrategi
    "user behavior": "Data",
    "anonymized data": "Data",
    "registration": "Data",
    "GDPR": "Data",
    "privacy policies": "Data",
     "Masters app": "Data",
     "app": "Data",
    "content team": "Data",  
    "data collection": "Data",
    "user interaction": "Data",
    "personalized social content": "Data",

    # Fallstudie
    "Wimbledon": "Fall",
    "The Masters": "Fall",
    "the Masters": "Fall",
    "Ferrari": "Fall",
    "US Open": "Fall",
    "Grammy Awards": "Fall",
    "UFC": "Fall",
    "partnership": "Fall",

    # Utmaningar med AI
    "brand guidelines": "Utmaning",
    "broadcasting rights": "Utmaning",
    "creative limits": "Utmaning",
    "tradition-heavy": "Utmaning",
    "risk": "Utmaning",
    "rights": "Utmaning",

    # Framtidsutsikter och reflektion
    "smart glasses": "Framtid",
    "real-time concierge": "Framtid",
    "personalized experience": "Framtid",
    "virtual signage": "Framtid",
    "ball tracking": "Framtid",
    "opportunity" : "Framtid",
    
}

# Intervjudata
data = [
    {"Fråga": "Can you tell us a little about your position and your work at IBM?", 
     "Svar": "I lead the technology program within IBM’s Sports and Entertainment Partnerships group, which sits under Marketing and Communications. Our portfolio includes partnerships with the Masters Tournament, Wimbledon, the US Open, ESPN Fantasy Football, the Grammy Awards, UFC, and Ferrari. My team manages and leads these partnerships with a goal to tell IBM’s technology story in the context of each event. For example, at the Masters, we help solve digital experience and digital operations problems using IBM technology."},
    
    {"Fråga": "We recently interviewed Fred Baker. Do you know him?", 
     "Svar": "Yes, Fred is part of IBM Consulting and is one of our partners on the delivery side. While I work in Marketing and Communications, Fred leads the delivery, design, and development of the programs from the consulting side. Once we establish a relationship with a partner, teams like Fred’s are brought in to build and deliver the experience. We then use that work to tell the broader IBM technology story. It’s a collaborative relationship between groups within IBM."},
    
    {"Fråga": "Is there a particular partnership you’ve worked more closely with than others?", 
     "Svar": "Yes. I’ve been in this role for about three years, but before that, I spent 17 years on the consulting side—doing exactly what Fred does. I’ve led delivery for most of the programs in our portfolio—designing and building websites, mobile apps, AI features, and delivering them on site at events. Now, on the partnership side, I focus on defining use cases that are meaningful to the partner’s actual business challenges. For example, with Wimbledon, we don't just bring IBM tools—we consult to identify their true challenges and see where we can apply the right solutions, whether IBM’s or not."},
    
    {"Fråga": "What do you think is AI's most important role in fan engagement—say, for the Masters?", 
     "Svar": "AI enables personalized and scaled content in a way human teams alone can't. Take the Masters: imagine trying to create personalized social content for 100 golfers daily—hundreds of assets in different languages, tones, and formats. That’s where AI shines: generating customized content efficiently. It empowers a five-person content team to perform like fifty—or five hundred. It’s about productivity, scale, and personalized fan experiences."},
    
    {"Fråga": "So there’s a financial motivation behind that too?", 
     "Svar": "Absolutely. It’s about expanding your audience without scaling your team proportionally. Hiring 300 people to cover an event is possible—but expensive and logistically complex. Instead, AI tools allow a smaller, trusted team to produce at a massive scale, multiplying productivity and impact."},
    
    {"Fråga": "When I used the Masters app, I saw those AI-generated stats, like probability to make par. Is AI really necessary for something like that?", 
     "Svar": "That feature is called 'Hole Insights' and it has three components: Historical performance from the ball’s current location—this is statistical and doesn't need AI. Current tournament context—also empirical. Projections for the rest of the day/tournament—that’s where AI comes in. We use AutoAI in Watson Studio to simulate outcomes and choose the best-performing models for projections. Also, the descriptive sentences you saw were generated by a large language model, constrained by Augusta National's requirements to keep them factual and not overly creative. The technology can be more creative, but we follow the partner’s brand guidelines—especially for a tradition-heavy event like the Masters."},
    
    {"Fråga": "Are there areas within fan interaction where you feel AI is currently underutilized?", 
     "Svar": "Yes, definitely. One area is live commentary. At tournaments like Wimbledon or the US Open, only top matches get commentary. But there are hundreds of matches—junior, wheelchair, exhibition—that get none. We have the data, AI voices, and technology to provide live audio commentary across the board. It’s possible, and I’ve been pushing for it for years. We're actively exploring it, but it's not there yet."},
    
    {"Fråga": "Would that be delivered through the official app?", 
     "Svar": "Yes, ideally. We’re working on it. It's a long-standing goal of mine. Broadcasting rights can be tricky, but when events like Girls Junior matches aren’t covered at all, there’s an opportunity to fill that gap without conflicting with broadcaster rights."},
    
    {"Fråga": "What about AI in on-site fan experience?", 
     "Svar": "Great question. AI could enable real-time, context-aware concierge experiences. For example, with smart glasses or earbuds, an AI assistant could tell you, 'You’re in Section 3B, hot dogs are around the corner,' or, 'Your friend just arrived in Section F3.' It could even offer seat upgrades or event highlights based on your interests. There’s huge untapped potential for AI in physical fan experiences."},
    
    {"Fråga": "What upcoming technologies do you think will have the biggest impact on fan engagement?", 
     "Svar": "Rather than one big innovation, I think we’ll see smaller, highly impactful enhancements—like the first down line in American football. It seems small now, but if it were removed, fans would immediately notice. Innovations like ball tracking in golf, puck tracking in hockey, or virtual signage in horse racing all improve engagement. The next big leap might be delivering personalized, exclusive experiences, even in a crowd of 50,000. Making each fan feel like the experience was crafted just for them—that's where we're headed."},
    
    {"Fråga": "And finally, what are IBM’s guiding principles when it comes to using fan data responsibly?", 
     "Svar": "We collect very little fan data in our portfolio. For example, at Wimbledon, you need to register to buy tickets, which involves standard data collection, governed by GDPR and privacy policies. Outside that, we avoid collecting personal data. When we do personalize experiences—like at the Masters—it’s based on anonymized data and behavior. If someone watches lots of Tiger Woods videos, we might show them more, even if they haven’t selected him as a favorite. It’s all based on user interaction with the site or app, under transparent terms and conditions. We strive for a fair exchange: the user gets value, and we respect their privacy."},
]

# Initiera KeyBERT
kw_model = KeyBERT()

# Spara data i lista
rows = []

for item in data:
    question = item["Fråga"]
    answer = item["Svar"]

    # Extrahera nyckelord (enstaka ord)
    keywords = kw_model.extract_keywords(answer, top_n=5, keyphrase_ngram_range=(1, 1))
    keyphrases = [kw[0] for kw in keywords]

    # Hitta förkortningar i svaret
    keyphrases_abbr = []
    for phrase in keyphrases:
        if phrase in abbreviations:
            keyphrases_abbr.append(abbreviations[phrase])

    # Kontrollera om några nyckelord i texten matchar begreppen
    for phrase in abbreviations:
        if phrase in answer:
            keyphrases_abbr.append(abbreviations[phrase])

    # Lägg till raden i resultatet
    row = {
        "Fråga": question,
        "Svar": answer,
        "Kod": ", ".join(set(keyphrases_abbr))  # Använd set för att ta bort dubbletter
    }
    rows.append(row)

# Skapa DataFrame och spara till CSV
df = pd.DataFrame(rows)
df.to_csv("interview_with_ibm_keywords.csv", index=False)

# Visa resultatet
print(df)
