import pandas as pd
from keybert import KeyBERT

# förkortningslista
abbreviations = {

    #Användning av AI i praktiken
   
    "AI-narration": "Funktion",
    "Funktion": "Funktion",

    "Generativ AI": "Funktion",
    "Funktion": "Funktion",

    "Keys to the Match": "Funktion",
    "Funktion": "Funktion",

    "Personalisering": "Funktion",
    "Funktion": "Funktion",

    "Power Index": "Funktion",
    "Funktion": "Funktion",

    #Mätning och effekt

    "mätning": "Mätning",
    "Mätning": "Mätning",
    "mätetal": "Mätning",
    "Mätetal": "Mätning",
    "Key Performance Indicator": "Mätning",
    
    #Dataanvändning och appstrategi

    "CRM": "Data",
    "Data": "Data",

    "Racingdata": "Data",
    "Data": "Data",

    "Real-Time Analytics": "Data",
    "Data": "Data",

    "realtidsdata": "Data",
    "Data": "Data",


    #Fallstudie
    "Ferrari": "Fall",
    "Fall": "Fall",
    "projekt": "Fall",

    #Utmaningar med AI
    "utmaningar": "Utmaning",
    "Utmaning": "Utmaning",
    "hallucination": "Utmaning",
    "risk": "Utmaning",
    "felaktighet": "Utmaning",
    "konkurrent": "Utmaning",
    "osystematiserad": "Utmaning",


    
}

# Intervjudata
data = [
    {"Fråga": "Hur är mätning av AI:s påverkan på fan engagement?", "Svar": "Fokus ligger inte på AI i sig, utan på hur väl specifika funktioner presterar. Mätetal: nya registreringar, Dwell Time, klickdjup, försäljning. Vi mäter hur djupt en användare går in i något… och beslutar om det var värt den extra månaden av utveckling för att möjliggöra det."},
    {"Fråga": "Har du exempel på AI-drivna funktioner?", "Svar": "Keys to the Match: Identifierar tre nyckelpunkter inför varje match. Tydlig, lättförståelig och anpassad för både nybörjare och experter. Power Index: Rankar spelare i realtid utifrån form. Syftet är bl.a. att sprida publiken över olika arenor, vilket ledde till ökad försäljning på Wimbledon. Generativ AI-innehåll: Möjliggör skräddarsydda racerapporter beroende på om mottagaren är ett barn, nybörjare eller expert.AI-narration: Kommentarer skapade med hjälp av kända röster (t.ex. Jim Nance) används för att skapa igenkänning och förhöjd upplevelse."},
    {"Fråga": "Appstrategi och datadrivna lösningar?", "Svar": "Fokus: driva trafik till appar, inte bort. Verktyg: CRM, personalisering, sömlös inloggning."},
    {"Fråga": "Kan du förklara Ferrari-samarbetet?", "Svar": "Ny app med racingdata för fans. Utmaning: Ferrari äger inte all data."},
    {"Fråga": "Finns det några utmaningar med AI i sport?", "Svar": "Sportdata är ofta osystematiserad och svår att använda, till skillnad från branscher som finans.Många sportorganisationer saknar vana att använda data för att skapa fanupplevelser.Rädsla för att “hallucinationer” i AI-modeller (felaktigheter) ska slå tillbaka hårt i sociala medier.I motorsport finns även oro kring att realtidsdata ska utnyttjas av konkurrenter, vilket försvårar öppenhet. In sports, getting something wrong with AI doesn’t change the world… but everyone sees it — and the backlash can be huge."},
    {"Fråga": "Vad är IBM:s arbetsmetod?", "Svar": "Allt arbete börjar med att definiera ett konkret mål – t.ex. att attrahera nya fans, öka lojalitet eller samla in data. Funktionerna byggs utifrån detta mål, och AI används som ett verktyg för att effektivisera, förstärka och accelerera processen. Mätning sker utifrån det specifika målet snarare än generella engagemangsdata."}
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
df.to_csv("interview_1.csv", index=False)

# Visa resultatet
print(df)
