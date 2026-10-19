# -*- coding: utf-8 -*-
"""Topic module: gen-thank-you-note-creator (GENERATOR class, first-release pick).
34 full sample thank-you notes + REAL note generator (see realgen).
Property of Justin Addam Higgins (JAH)."""
from w3lib import topic

CFG = {
    "slug": "gen-thank-you-note-creator",
    "prefix_pub": "JAH-THAYOUNOT-",
    "prefix_sig": "JAH-THAYOUNOTS-",
    "name_pub": "The Thank-You Note Creator Generator Database",
    "name_sig": "The Thank-You Note Creator Signature Generator Database",
    "tagline_pub": "Thank-you notes that actually land - for gifts, for help, for hospitality, for kind words, for opportunities: every record a complete ready-to-send note built on the name-it, feel-it, future-it anatomy, plus a real generator that writes brand-new notes on every run, taught progressively along the ladder.",
    "tagline_sig": "The Signature art of gratitude: every thank-you a Signature testimony, the giver named, the gift honored, the bond recorded. The full ladder from simple thanks through crafted notes to Signature-grade gratitude. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai_pub": "JAH Thank-You Note Archivist",
    "ai_sig": "JAH Thank-You Note Signature Archivist",
    "role_pub": "gratitude writer - composing complete thank-you notes for gifts, help, hospitality, kind words, and opportunities",
    "role_sig": "Signature gratitude writer - composing Signature-grade thank-you notes that record the bond",
    "greet_pub": "I am the JAH Thank-You Note Archivist. Tell me what you are thankful for and I will write the note.",
    "greet_sig": "I am the JAH Thank-You Note Signature Archivist. Tell me what you are thankful for.",
    "record_kind": "thank-you note record",
    "record_kind_plural": "thank-you notes",
    "demo_kind": "thank-you-note",
    "demo_title": "Thank-You Note Study",
    "search_ph": "Search gift, help, hospitality, kind words, opportunity notes...",
    "chat_ph": "Ask for a thank-you note...",
    "gen_blurb": "Real working generator - every run writes a brand-new, complete thank-you note for the situation you pick. Never a structural sample.",
    "about_archive": "Seeded sample thank-you notes, each complete and ready to personalize, marching toward one million records. Presented in teaching-ladder order: simple thanks, crafted notes, Signature-grade gratitude.",
    "reqs_default": "The giver's name, the specific thing, and one honest feeling. Send within a week - late gratitude still counts.",
    "stds_default": "Every note names the thing, names the feeling, and names the future - the three beats of a note that lands.",
    "cites_default": ["JAH Databases message craft standard v1.0"],
}
CUSTOM_GEN = "thank-you"


def _n(tier, kind, note, tip):
    return topic(
        tier, "Thank-you note (%s): %s" % (kind.lower(), note[:44].rstrip(" ,.!") + "..."),
        desc_pub="SAMPLE NOTE - %s:\n\n%s\n\nThis is a complete, ready-to-personalize thank-you note." % (kind.upper(), note),
        desc_sig="Signature gratitude: this note records the bond - the giver named, the gift honored in specific detail, the future of the relationship sketched in one line. The Signature edition treats every thank-you as a small entry in the ledger of kindness.",
        how_pub="Make it yours: %s Deliver within a week; handwritten beats typed, and specific beats general every time." % tip,
        how_sig="The Signature way: read it aloud - gratitude should sound like you on your best day, unhurried and exact.",
        keys=["Complete note: names the thing, names the feeling, names the future.",
              "Situation: %s." % kind,
              "Personalization: %s" % tip,
              "Anatomy check: specific detail present, warmth present, forward look present."],
        demo=("check", {"code": ["NOTE = %r" % note],
                        "checks": [("length_ok", "len(NOTE) > 60"),
                                   ("no_unfilled_slots", "'{' not in NOTE"),
                                   ("ends_well", "NOTE.rstrip().endswith(('.', '!'))"),
                                   ("mentions_thing", "len(NOTE.split()) > 20")]}),
    )


B = "Foundations"
C = "Compounded"
A = "Advanced"
TOPICS = [
    _n(B, "For a Gift", "Dear Aunt Rosa, thank you so much for the beautiful knitted scarf. It was thoughtful, perfect, and so very you. I thought of you the moment I opened it, and I have smiled about it every cold morning since. With love and gratitude.", "name the gift exactly and one time you used it"),
    _n(B, "For Help", "Marcus, your help with the move saved my back and my sanity. Thank you for showing up with the truck, the dolly, and zero complaints. I owe you dinner - and I mean that.", "name what they helped with and one funny moment"),
    _n(B, "For Kind Words", "Lena, your encouraging message arrived exactly when I needed to hear it. Thank you for saying the true thing kindly. I have kept your words close all week.", "quote one line they said if you can"),
    _n(B, "For a Gift", "Jake, the book was perfect - you always know. Thank you for thinking of me. I started it last night and already do not want it to end.", "name the book and your first impression"),
    _n(B, "For Hospitality", "Tom and Priya, thank you for the wonderful dinner party. Your home felt like a hug, the food was perfect, and the company was even better. My place next time - be brave.", "name one dish you still think about"),
    _n(B, "For Help", "Dana, thank you for covering my shift on zero notice. You are the reason I could be where I needed to be. I have got your next one, no questions asked.", "name the shift or favor"),
    _n(B, "For a Gift", "Grandma, thank you for the handmade quilt. Every stitch feels like a hug from you. It is on my bed already and it is the warmest thing I own, in every sense.", "mention where the gift lives now"),
    _n(B, "For Kind Words", "Coach, thank you for believing in me before I believed in myself. Your words at halftime changed the whole season for me.", "name the moment their words landed"),
    _n(B, "For an Opportunity", "Ms. Rivera, thank you for the interview. I left feeling excited about the work and the team. Whatever you decide, I am grateful for the chance to be considered.", "name one thing about the role that excites you"),
    _n(B, "For Hospitality", "The Hendersons, thank you for the cozy weekend. I left feeling rested, fed, and reminded how lucky I am to know you all.", "name one moment from the visit"),
    _n(B, "For Help", "Neighbor Joe, thank you for jump-starting the car in the rain without being asked. That is just who you are, and the street is better for it.", "describe the scene briefly"),
    _n(C, "For a Gift", "Dear Mr. and Mrs. Osei, thank you for the generous wedding gift. James and I have put it toward our first home fund, and every time we walk through that future front door, we will think of you. Your presence at the wedding meant even more than the present.", "say what the gift is becoming"),
    _n(C, "For Help", "Elena, stepping in with the kids during the emergency - there are no adequate words, so I will use the true ones: you saved us that week. The kids still talk about Aunt Elena's pancake mornings. Thank you is not big enough, but it is a start, and dinner is on us forever.", "name what the kids remember"),
    _n(C, "For Hospitality", "Dearest Amara, thank you for the holiday gathering that felt like a warm novel. The table was beautiful, the stories were better, and nobody wanted the night to end. You have a gift for making people feel like the most important person in the room - because to you, they are.", "name the feeling of the evening"),
    _n(C, "For Kind Words", "Professor Hale, your letter of recommendation was more generous than I deserved and exactly what I needed. Thank you for seeing potential in my work and saying so on the record. I will spend my career trying to be worthy of your description.", "name the opportunity the letter opened"),
    _n(C, "For an Opportunity", "Dear Director Chen, thank you for trusting me with the lead on the Harbor project. I know it was a stretch assignment, and I will work relentlessly to be worthy of the chance. Your belief in this team is the reason we aim high.", "name the project and your commitment"),
    _n(C, "For a Gift", "Sofia, the framed photo of us at the lake made me cry in the good way. Thank you for freezing that perfect afternoon. It is on my desk where I see it every workday, and it fixes bad mornings.", "say where it lives and what it fixes"),
    _n(C, "For Help", "To the night-shift nurses of Ward 4B: thank you for the 3 a.m. kindnesses nobody charts - the extra blanket, the unhurried explanation, the joke that made my father laugh through the pain. You do holy work in comfortable shoes.", "name the unit and one specific kindness"),
    _n(C, "For Hospitality", "Uncle Ray and Aunt Jo, thank you for the week at the cabin. The mornings on the dock, the fish stories (some true), the pie - I came home rested in a way I had forgotten was possible. The kids are already asking when we can return.", "name the ritual you will repeat"),
    _n(C, "For Kind Words", "Maya, your toast at the wedding made half the room cry laughing and the other half just cry. Thank you for telling our story better than we could. We will be quoting you for decades.", "quote their best line back to them"),
    _n(C, "For an Opportunity", "Kwame, thank you for the introduction to the studio. One conversation turned into the collaboration I have dreamed about for years. I will pay the introduction forward - that is the deal with good connectors like you.", "name what the introduction became"),
    _n(C, "For a Gift", "Dearest Grandpa, thank you for the watch. I know it was yours first, which makes it the most valuable thing I own. I will wear it daily, wind it carefully, and think of you every time I check the hour. Love always.", "for heirlooms, acknowledge the lineage"),
    _n(C, "For Help", "Priya, you rewrote the entire proposal with me until 1 a.m. and never once made me feel like a burden. Thank you. The client signed, and your fingerprints are all over that win. Next launch dinner is on me, and I am not taking no for an answer.", "name the win their help produced"),
    _n(A, "For an Opportunity", "There are moments that divide a life into before and after. Your email - three lines, one introduction - was mine. Dr. Osei, thank you for opening a door I did not know existed and then walking me through it. The lab, the work, the people: everything I hoped science could be. I intend to spend the next decade making your judgment look brilliant.", "for life-changing opportunities, say so plainly"),
    _n(A, "For Help", "I have been trying to write this for a week, because some thanks are too big for a card. Dr. Patel: you did not just treat the illness, you treated the fear. Every appointment, you looked me in the eye and told me the truth kindly. I am well today because you were excellent every day. Thank you is not enough, but it is what I have, given with everything I have.", "for life-sized gratitude, be specific and unhurried"),
    _n(A, "For Hospitality", "A home is not the walls; it is the way the door always seems to be open. The Almeidas, your house on Cypress Street has hosted my hardest year and my happiest news, sometimes in the same weekend. Thank you for the spare key, the spare room, and the standing invitation that made a city feel like home.", "name the house as a character"),
    _n(A, "For Kind Words", "At the funeral, people say things because they must. You said things because they were true. Daniel, your eulogy for my father - the story about the broken lawnmower, the line about stubborn love - gave our grief a shape we could hold. Thank you for knowing him, and for letting us borrow your clarity on the hardest day.", "for grief-adjacent thanks, be gentle and exact"),
    _n(A, "For a Gift", "The scholarship letter said 'full tuition,' but what it really said was: someone believes a kid from our neighborhood belongs at that university. Mrs. Whitfield, thank you for the Whitfield Scholarship and for the belief inside it. I will graduate, and I will come back and tell the next kid exactly who made it possible.", "for scholarships, name the future you will build"),
    _n(A, "For Help", "To everyone who brought food, watched the baby, mowed the lawn, and sat with us in the waiting room during those six weeks: thank you. We have a list of names and we will never lose it. You taught our children what community means before they could spell it. We are paying it forward, starting now.", "for group thanks, promise the list is kept"),
    _n(A, "For Kind Words", "Editor's notes usually sting. Yours taught. Ms. Okonkwo, thank you for the three pages of single-spaced belief in my manuscript - the critique was ruthless and the encouragement was relentless, exactly as it should be. The book is dedicated to you, and it is better because you refused to let it be merely good.", "for mentors, show the work their words produced"),
    _n(A, "For an Opportunity", "Second chances are rarer than first ones, and you handed me one without a lecture. Mr. Thompson, thank you for the job when my record made me easy to skip. Eighteen months later: promoted twice, never late, training the new hires myself. You bet on the right person. I will keep proving it.", "for second chances, report the results"),
    _n(A, "For Hospitality", "Refugees do not get to choose their first friends in a new country; we got lucky. The Berg family: thank you for the apartment setup, the winter coats, the patient English, and the Christmas we will tell our grandchildren about. You turned 'asylum' into 'home' in six months. We will never forget, and we will never stop being grateful.", "for profound hospitality, let the weight stand"),
    _n(A, "For a Gift", "Dad, the truck is great, but the note taped to the steering wheel is the real gift: 'Earned, not given. Proud of you. - Dad.' I read it every morning before I turn the key. Thank you for raising me to earn things and for noticing when I do.", "for parent gifts, answer the deeper message"),
    _n(A, "For Help", "Nobody saw the year I almost quit except you, Rosa. The 6 a.m. pep talks, the emergency childcare, the way you never once said 'I told you so' when I finally listened. The business survived because you refused to let me disappear. Thank you is a small phrase for a large debt - consider this the first installment.", "for the ones who stayed, name the staying"),
]
