import pandas as pd
from keybert import KeyBERT

# Uppdaterad kodningsnyckel anpassad för intervju 4
abbreviations = {

    # Bakgrund och roll
    "brandbuilding": "Roll",
    "varumärkesbyggande": "Roll",
    

    # Användning av AI i praktiken
    "generativ text": "Funktion",
    "bildanalys": "Funktion",
    "personalisering": "Funktion",
    "AI-baserad": "Funktion",
    "statistik": "Funktion",
    "identifierar spelare": "Funktion",
    "realtid": "Funktion",
    "Funktionen": "Funktion",
    "skräddarsydda rekommendationer": "Funktion",
    "matchkommentarer": "Funktion",
    "AI-drivna funktioner": "Funktion",
    

    # Mätning och effekt
    

    # Dataanvändning och appstrategi
    "datainsamling": "Data",
    "GDPR": "Data",
    "information": "Data",
    "historiska data": "Data",

    # Fallstudie
    "Wimbledon": "Fall",
    "US Open": "Fall",
    "Fantasy Football": "Fall",
    "UFC": "Fall",

    # Utmaningar med AI
    "AI-washing": "Utmaning",
    "risk": "Utmaning",
   

    # Framtidsutsikter och reflektion

    "framtid": "Framtid",
    "potential": "Framtid",
}

categories = {
    "Bakgrund och roll": "Roll",
    "Användning av AI i praktiken": "Funktion",
    "Mätning och effekt": "Mätning",
    "Dataanvändning och appstrategi": "Data",
    "Fallstudie": "Fall",
    "Utmaningar med AI": "Utmaning",
    "Framtidsutsikter och reflektion": "Framtid"
}

# Intervju 4 – para ihop frågor och svar
interview_qna = [
    ("För att börja lite övergripande – hur ser du på sportpartnerskapens roll inom IBM som organisation?",
     "Sportpartnerskapen har en tydlig roll inom det vi kallar brandbuilding – alltså varumärkesbyggande. Det handlar inte främst om direkt intäktsgenerering utan snarare om att förknippa IBM med innovation, teknik och upplevelser som människor kan relatera till på ett emotionellt plan. Genom att synas i sammanhang som Wimbledon, US Open eller The Masters bygger vi associationer till kvalitet, pålitlighet och teknologisk spets, vilket på sikt stärker IBM:s position på marknaden."),
    
    ("Så det är inte direkt kopplat till försäljning?",
     "Inte i första hand. Det finns naturligtvis ett indirekt affärsvärde – vi visar upp våra teknologier i konkreta tillämpningar, vilket kan inspirera andra branscher att ta kontakt. Men jämfört med exempelvis traditionell konsultverksamhet är sportpartnerskapen betydligt mer fokuserade på kommunikation, synlighet och innovation snarare än direkt revenue."),
    
    ("Hur ser du då på användningen av AI i dessa sportpartnerskap? Är det alltid meningsfullt, eller finns det risk för AI-washing?",
     "Det finns definitivt en risk för det senare. Jag tycker det är viktigt att vara ärlig med att inte allt som kallas AI verkligen bygger på avancerade algoritmer. I vissa fall används begreppet mest som ett marknadsföringsverktyg. Funktionen i exempelvis The Masters-appen, där du kan se var en spelare befinner sig på banan eller få statistik om sannolikheten för en birdie, är i grunden baserad på historiska data och ganska enkel logik. Det kräver inte nödvändigtvis avancerad maskininlärning. Att kalla det för AI kan då vara lite missvisande – ett exempel på vad man ibland kallar AI-washing."),
    
    ("Samtidigt finns det ju funktioner som faktiskt använder AI, som generativ text, bildanalys och personalisering?",
     "Absolut. Det är viktigt att skilja mellan de funktioner där AI verkligen tillför något unikt – som generering av matchkommentarer eller skräddarsydda rekommendationer – och de där man använder begreppet mer symboliskt. Den tekniska höjden varierar. Det häftiga är när tekniken används för att förbättra fanupplevelsen i realtid, till exempel med AI-baserad bildanalys som identifierar spelare och genererar statistik direkt under matchen. Men vi måste också vara medvetna om att det ibland är marknadsföringsvärdet snarare än den tekniska innovationen som är det primära motivet."),
    
    ("Utifrån ett användarperspektiv då – vad tror du att AI skulle kunna tillföra för att verkligen göra upplevelsen bättre?",
     "Jag tror det finns stor potential i AI som personaliseringsverktyg. Tänk dig att du som användare direkt får innehåll som är skräddarsytt efter ditt favoritlag, dina tidigare interaktioner och till och med ditt humör. Det finns också stora möjligheter inom tillgänglighet – AI kan till exempel hjälpa till att transkribera, översätta eller tillhandahålla visuellt stöd i realtid, vilket gör upplevelsen mer inkluderande."),
    
    ("I vår studie har vi pratat med personer på IBM:s globala sportavdelning som nämnt att ni arbetar med många fler partnerskap än man kanske känner till i Sverige, som UFC och Fantasy Football. Är det något du har insyn i?",
     "Jag har inte insyn i alla samarbeten eftersom de flesta hanteras på global nivå. Det är sant att många av dessa partnerskap, särskilt de i USA, kanske inte är lika kända här hemma. Men det visar också på bredden i IBM:s sportstrategi – vi använder partnerskap i olika sporter och regioner för att visa hur vår teknik kan appliceras i väldigt olika sammanhang."),
    
    ("Vi undersöker också etiska aspekter i vår studie. Vad tycker du är viktigast att tänka på där?",
     "Det etiska perspektivet är jätteviktigt. Allt börjar med datainsamlingen – vad samlar vi in, varför, och vad gör vi med informationen? Det är centralt att allt sker enligt GDPR och andra regelverk, men också att det finns en tydlig kommunikation till användaren om hur deras data används. Transparens skapar förtroende, vilket är avgörande om vi vill att användare ska interagera med AI-drivna funktioner. Man måste också fundera på var gränsen går mellan hjälp och manipulation – exempelvis i hur man personaliserar innehåll för att öka användning eller engagemang."),
    
    ("Tack så mycket – det här var otroligt värdefullt!",
     "Det var så lite! Lycka till med uppsatsen.")
]

# Initiera KeyBERT
kw_model = KeyBERT()
rows = []

# Kodning
for q, a in interview_qna:
    keywords = kw_model.extract_keywords(a, top_n=5, keyphrase_ngram_range=(1, 1))
    keyphrases = [kw[0] for kw in keywords]
    keyphrases_abbr = []

    matched_category = None
    for category, code in categories.items():
        if category.lower() in a.lower():
            matched_category = code
            break

    if matched_category is None:
        for phrase in keyphrases:
            if phrase in abbreviations:
                keyphrases_abbr.append(abbreviations[phrase])
        for phrase in abbreviations:
            if phrase.lower() in a.lower():
                keyphrases_abbr.append(abbreviations[phrase])
        category_code = ", ".join(set(keyphrases_abbr)) if keyphrases_abbr else "Okodad"
    else:
        category_code = matched_category

    row = {
        "Fråga": q,
        "Svar": a,
        "Kod": category_code
    }
    rows.append(row)

# Skapa DataFrame och spara som CSV
df = pd.DataFrame(rows)
df.to_csv("interview_4_full_with_categories.csv", index=False)

# Terminalvisning med förkortat svar
print("\nFörhandsvisning av kodade intervjusvar:\n")
for row in rows:
    short_answer = row["Svar"][:100] + "..." if len(row["Svar"]) > 100 else row["Svar"]
    print(f"Fråga: {row['Fråga']}")
    print(f"Svar: {short_answer}")
    print(f"Kod: {row['Kod']}")
    print("-" * 80)

print("\nFil skapad: interview_4_full_with_categories.csv")
