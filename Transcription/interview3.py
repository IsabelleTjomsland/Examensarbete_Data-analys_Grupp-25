import pandas as pd
from keybert import KeyBERT

# Anpassad kodningsnyckel för intervju 3 och kategorier
abbreviations = {

    # Bakgrund och roll

    "R3": "Roll",
    "IBM Sports and Live Events": "Roll",
    "digital and technical delivery": "Roll",
    "responsible for": "Roll",
    

    #Användning av AI i praktiken

    "AI features": "Funktion",
    "AI commentary": "Funktion",
    "computer vision": "Funktion",
    "WatsonX": "Funktion",
    "generative AI": "Funktion",
    "metadata": "Funktion",
    "innovation features": "Funktion",
    "AI innovations": "Funktion",
    "IBM technologies": "Funktion",
    "delivery": "Funktion",
    "creative": "Funktion",
    "build": "Funktion",

    # Mätning och effekt

    "productivity": "Mätning",
    "efficient": "Mätning",
    "measured": "Mätning",


    # Dataanvändning och appstrategi

    "data": "Data",
    "metadata": "Data",
    "data migration": "Data",
    "guardrails": "Data",
    "source of truth": "Data",
    "Hawkeye": "Data",
    "limb tracking": "Data",
   

    # Fallstudie

    "Wimbledon": "Fall",
    "US Open": "Fall",
    "Masters": "Fall",
    "Grammys": "Fall",
    "ESPN Fantasy Football": "Fall",
    "Ferrari": "Fall",
    "UFC": "Fall",
    


    # Utmaningar med AI

    "challenges": "Utmaning",
    "data quality": "Utmaning",
    "coordination": "Utmaning",
    "align": "Utmaning",
    "mistakes": "Utmaning",
    


    # Framtidsutsikter och reflektion

    "North Star": "Framtid",
    "generative content": "Framtid",
    "future": "Framtid",
    "personalized": "Framtid",
    "player posture": "Framtid",
    "latest and greatest": "Framtid",
    "up and coming": "Framtid",
    "new technology": "Framtid",
    "stay ahead": "Framtid",
    "vision": "Framtid",
    "we want to create": "Framtid",
}

# Kategorier och förkortade koder
categories = {
    "Bakgrund och roll": "Roll",
    "Användning av AI i praktiken": "Funktion",
    "Mätning och effekt": "Mätning",
    "Dataanvändning och appstrategi": "Data",
    "Fallstudie": "Fall",
    "Utmaningar med AI": "Utmaning",
    "Framtidsutsikter och reflektion": "Framtid"
}

# Intervjudata: para ihop frågor och svar
interview_qna = [
    ("Are you guys there?", "Okay, there we go. Oh, I think it's working."),
    ("Do you want to ask the question again?", "Yeah. Yeah, can you just quickly and briefly tell us a little bit about what's your role and what you do?"),
    ("Yeah, can you just quickly and briefly tell us a little bit about what's your role and what you do?", "Sure. So my name is R3, and I work on the IBM Sports and Live Events. And we are responsible for the digital and technical delivery across our sports entertainment portfolio. So that includes delivering all the different digital platforms, data analytics, video work, as well as our innovation and AI features. And the innovation and AI features are the projects that I'm focused on across the portfolio. "),
    ("And that includes all of the events that you're partnering with?", "Correct. So we work on the Masters, US Open Tennis, Wimbledon. We do work with ESPN Fantasy Football, the Grammys, and then we have two new partnerships with Ferrari, part of F1, and then UFC."),
    ("How does IBM strategically decide which AI innovations to prioritize for enhancing digital fan experience?", "Yeah, so we go through an innovation process across the portfolio where we come together with different stakeholders. So you have the IBM marketing and partnership stakeholders. You have the stakeholders on my team who are responsible for the build and the creative and the delivery. And then we also have the client stakeholders. So based on the different priorities and requirements and goals and needs of each of these different parties, we come together to decide and prioritize what are the best possible innovations for the fan, so the end-user. A lot of times with these projects, we are using these AI and innovation features as a way to showcase the best of the best, the newest, latest and greatest of IBM technologies.So a lot of times, some of the work that we do, we work with IBM Research. To make sure that we're staying ahead of any of the public announcements to make sure that we do have the latest and greatest technologies within the projects and features that we build.So it's definitely a collaborative effort amongst all of the stakeholders. What's up and coming? What's the new technology? Then also, most importantly, how can we help better the fan experience? "),
    ("All right. In terms of AI, could you give us an example of like one of your latest technologies in any of the apps that you do? ", "Yeah, so I think one of the goals of these AI and innovation features is that we want it to feel like a seamless experience. So we don't want it to, you know, we want it to be part of the overall digital platform. So I think one of the reasons why maybe you didn't see some of those flashing AI features is because it's very much integrated into the core work, um, so it's like driving driving the whole uh operation behind like the back end, it's really, I mean that's exactly right. So if you think about um, one of my favorite AI features that that we've built over the years for golf and tennis um, would be something called AI commentary. So if you think about all yeah, if you think about all the different um video clips and points and shots for golf, and generation Correct. So we're basically using AI to analyze the metadata in the video clips and then produce that output of what's going on in the video based on the metadata stats, as well as, you know, visually we can use computer vision as well. And we have in the past in certain instances to create this output that is paired with the video clips. And that could be only really possible with AI because there are so many different points. There are so many different shots. I think for the Masters, there's like over 200,000 different clips or shots analyzed. So, that certainly would not be possible without some of these super powerful tools. And I think one of the goals would be: is right now, you might have seen it's more based on the stats and it's a little bit more; there's more parameters to keep it accurate. And as the generative technology improves, you're going to see more color and maybe some of those personas shine through a bit more. But as we're starting off, the goal is: we can't be wrong. The output has to be right. So, we put those parameters and those safeguards in to make sure that the model produces the accurate results. And then over time, we'll be able to dial up those levers a bit more to add some more of that color and personality that you'll see in other AI applications that you use."),
    ("Are there any unexplored areas within digital fan engagement where you believe AI could make a difference?", "I mean, I think there's lots. One of the things that I'm really excited about for the future, at least from a tennis is my background and that's my favorite sport. But if you think about Wimbledon, for example, there's obviously the ladies' and gentlemen's events where we know all of those players, Alcaraz, Coco Gauff, people like that. There's also like many other events taking place for juniors, for wheelchairs, for doubles, for mixed doubles, all sorts of other events. And there's so many different players from all over the world who speak many different languages. And there's a lot of players who are up and coming and don't have the type of publicity or the content written about them yet. So, I think that the dream scenario for AI is to essentially create content for every single player and ever in any potential language over the course of the tournament. It would be physically impossible for a human to create that much content for all the different players and all the different events and all the different languages. So again, using our Using generative AI to create that content about every player, which is only going to help the players make a name for themselves and get more known. So that's what I'm really excited about. And you can take that one step further. It can be text-based. It can be audio-based. It can be video-based. So it could all be all the different mediums, again, with the generative AI at the center. So that's something that we're like, you know, North Star working on. I see from a. more focused maybe on the computer vision and inputting that data into these generative AI models, looking at video to understand player body movements. We work with a partner called Hawkeye, and they're working on limb tracking data. So the player posture, if a player slams the racket, like we do some of that right now, you know, using those technologies to get even more detailed in terms of how a player is acting. on the court and using that as another source of data to create all sorts of cool output. So it's all about what other data sources can we add to input into the models and then create this generative content."),
    ("Do you observe cultural differences in how fans respond to different AI technologies?", "I mean, I think that no matter where you live, the expectation for AI to be accurate and that it doesn't make mistakes is very high. And I think that as someone who works in this space that we know, you guys know that it's not always accurate. And yes, ChatGPT can look perfect right in the response because it's formatted right but if you actually dive into the actual content and then you know do this at scale it breaks it makes mistakes it times out whatever it may be um so I think that just the expectation of what a user thinks AI can do and what it can actually do, I think there are some discrepancies. But I think over time, hello, I think over time that will improve. I think the other thing is that finding use cases that make sense for the fan. So, again, we don't want to be like same AI, AI down a fan's throat, because that's not people don't like that. And they don't want to think that humans are taking jobs or AI is taking jobs and all that stuff. So I think going back to the point of how do we seamlessly integrate it? How do we help, right, the content team at these different events? So like, you know, creating content for every player, that's really helping the Wimbledon content team, for example. So it's how do you use AI to help what these teams are already doing and then create that on the fan experience side in a seamless way. "),
    ("Where does IBM itself see the biggest challenges when it comes to AI for fan engagement?", "I think one of the biggest challenges is probably just around the data , and working with these different properties and events, and making sure that they have the data organized with the proper guardrails and safeguards in place, to then create the output that is desired. Because whatever goes into the model comes out of the model. So I think that's kind of, it's less on, I mean. I mean, this is my experience. I don't know what IBM thinks, but in my experience, the hardest part is getting access to the source of truth of the data and making sure that it's good and quality, to then influence any of the features. "),
    ("Like the data migration from the sport organizations to your models.", "Yeah. And there's so many different sources of truth of data, especially in sports, there's so many different sources of truth of data. So like how one governing body tracks a win might not be how another governing body tracks a win because a withdrawal could be counted on one site, but not on the other. So it's like that source of truth of data, I think is really important."),
    ("What do you do for the UFC?", "Yeah, it's new. I don't work on that project, but I think what we're doing, I can send you an article, we're providing insights. So we're helping them create more insights about the fights. I can send you an article about it. Corey would have been that person to ask about that."),
    ("How much of this is marketing and how much is about producing a good product?", "I mean you're not necessarily completely like it's a good way to think, I mean, that is an accurate way to think about it because at the end of the day, a lot of the work is based on a partnership and it's a marketing play. I mean, I wouldn't put that in your thesis, but it is an important part of it. But the good news on the other side of that is that we still are, you know, we're creating these technologies on our client—on these sport properties' digital platforms. So as much as we want to just put a name, a brand placement and a name on it, the technology and the features still need to work for the fan and in real time. So just because we want to create this cool new AI commentary feature and put our name on it—well, if it doesn't work by the millions of fans who are logging on to the app and the website, like it's going to end up being bad press, right? So it still has to work and be successful. Even though both things can exist, in my opinion. "),
    ("Can you send a recording?", "We'll figure out how to get it to you guys."),
    ("All right. Thank you so much, R3, for this interview. We're really thankful.", "Thank you. It took your time, even though you didn't know what you were getting into."),
    ("Can you send a recording to, or does Henrik have access?", "Probably, but, I'll figure between him and me, we'll figure out how to get that to you guys.")
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
df.to_csv("interview_3_full_with_categories.csv", index=False)

# Terminalvisning med förkortat svar
print("\nFörhandsvisning av kodade intervjusvar:\n")
for row in rows:
    short_answer = row["Svar"][:100] + "..." if len(row["Svar"]) > 100 else row["Svar"]
    print(f"Fråga: {row['Fråga']}")
    print(f"Svar: {short_answer}")
    print(f"Kod: {row['Kod']}")
    print("-" * 80)

print("\nFil skapad: interview_3.csv")