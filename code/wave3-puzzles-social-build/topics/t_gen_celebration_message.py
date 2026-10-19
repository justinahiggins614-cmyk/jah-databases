# -*- coding: utf-8 -*-
"""Topic module: gen-celebration-message (GENERATOR class, first-release pick).
34 full sample celebration messages + REAL message generator (see realgen).
Property of Justin Addam Higgins (JAH)."""
from w3lib import topic

CFG = {
    "slug": "gen-celebration-message",
    "prefix_pub": "JAH-CELMES-",
    "prefix_sig": "JAH-CELMESS-",
    "name_pub": "The Celebration Message Generator Database",
    "name_sig": "The Celebration Message Signature Generator Database",
    "tagline_pub": "Celebration messages for every occasion - birthdays, graduations, new jobs, new homes, weddings, new babies, retirements, thank-yous, get-wells, and big congratulations: every record a complete ready-to-send message with personalization notes, plus a real generator that writes brand-new messages on every run, taught progressively along the ladder.",
    "tagline_sig": "The Signature way of marking moments: every milestone a Signature testimony, every message carrying lineage - the full ladder from simple warm wishes through crafted occasion messages to Signature-grade celebration prose. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai_pub": "JAH Celebration Message Archivist",
    "ai_sig": "JAH Celebration Message Signature Archivist",
    "role_pub": "celebration writer - composing complete ready-to-send messages for every occasion and showing how to personalize each one",
    "role_sig": "Signature celebration writer - composing Signature-grade occasion messages that mark moments as testimony",
    "greet_pub": "I am the JAH Celebration Message Archivist. Tell me the occasion and I will write the message - or ask how to personalize any sample.",
    "greet_sig": "I am the JAH Celebration Message Signature Archivist. Tell me the occasion for a Signature-grade message.",
    "record_kind": "celebration message record",
    "record_kind_plural": "celebration messages",
    "demo_kind": "celebration-message",
    "demo_title": "Celebration Message Study",
    "search_ph": "Search birthday, graduation, wedding, new job, thank you, occasions...",
    "chat_ph": "Ask for a celebration message...",
    "gen_blurb": "Real working generator - every run writes a brand-new, complete celebration message for the occasion you pick. Never a structural sample.",
    "about_archive": "Seeded sample celebration messages, each complete and ready to personalize, marching toward one million records. Presented in teaching-ladder order: simple warm wishes, occasion messages, crafted Signature-grade prose.",
    "reqs_default": "A name, an occasion, and one personal detail. A pen beats a keyboard for the final version.",
    "stds_default": "Every message is complete (greeting, warm body, closing), names a real-feeling recipient, and carries one personalization note.",
    "cites_default": ["JAH Databases message craft standard v1.0"],
}
CUSTOM_GEN = "celebration"


def _m(tier, occasion, msg, personalize):
    return topic(
        tier, "%s message: %s" % (occasion, msg[:48].rstrip(" ,.!") + "..."),
        desc_pub="SAMPLE MESSAGE - %s:\n\n%s\n\nThis is a complete, ready-to-personalize celebration message." % (occasion.upper(), msg),
        desc_sig="Signature occasion craft: this message marks the moment as testimony - the milestone named, the person honored, the feeling made permanent in words. The Signature edition writes every celebration as a small ceremony.",
        how_pub="Personalize it: %s Then deliver it the way that lands hardest - handwritten card first, spoken second, texted third." % personalize,
        how_sig="The Signature way: read it aloud once before sending - if it does not sound like you at your warmest, adjust one line until it does.",
        keys=["Complete message: greeting, warm body, and closing.",
              "Occasion: %s." % occasion,
              "Personalization hook: %s" % personalize,
              "Ready to send after one personal detail is added."],
        demo=("check", {"code": ["MSG = %r" % msg],
                        "checks": [("length_ok", "len(MSG) > 60"),
                                   ("no_unfilled_slots", "'{' not in MSG"),
                                   ("ends_well", "MSG.rstrip().endswith(('.', '!'))"),
                                   ("has_name", "any(w[0].isupper() for w in MSG.split() if len(w) > 2)")]}),
    )


B = "Foundations"
C = "Compounded"
A = "Advanced"
TOPICS = [
    _m(B, "Birthday", "Happy birthday, Maya! Another year of you being exactly the wonderful friend you are - I hope this one brings you everything you quietly wished for. Eat cake first, make wishes second, and know you are so loved.", "swap in the real name and add one shared memory"),
    _m(B, "Birthday", "Happy birthday, Daniel! You make getting older look like a skill. Wishing you a year with more laughter than last year and fewer candles to blow out in one breath.", "swap in the real name and their actual age joke"),
    _m(B, "Thank You", "Elena, thank you - truly. What you did meant more than you know, and I will not forget it. People like you are why the rest of us keep believing in people.", "name the specific thing they did"),
    _m(B, "Congratulations", "Congratulations, Sam! Big news deserves big cheers, and I am cheering the biggest. Savor this - you earned every bit of it.", "name the achievement"),
    _m(B, "Get Well", "Get well soon, Rosa! Rest up and let people fuss over you for once. I am sending all the healing vibes and zero chores your way.", "add one specific offer of help"),
    _m(B, "Birthday", "To the best neighbor on the block - happy birthday, Mr. Chen! Your garden puts the rest of the street to shame and your wave makes every morning better.", "use their real name and one true detail"),
    _m(B, "New Job", "Congratulations on the new job, Priya! They have no idea how lucky they are. I knew all along - now go show them what I have been telling everyone.", "name the company or role"),
    _m(B, "Birthday", "Happy birthday, Leo! Officially old enough to know better, still young enough to do it anyway. Hope your day is as fun as you are.", "match the tone to how well you know them"),
    _m(B, "Thank You", "Just a note to say thank you, Marcus. Your help came exactly when I needed it, no questions asked. I owe you dinner - and I mean that.", "name what they helped with"),
    _m(B, "Congratulations", "You did it, Aisha! I am not even slightly surprised and enormously proud. Congratulations on the promotion - the team just got a lot stronger.", "name the promotion or win"),
    _m(B, "Get Well", "Healing thoughts headed your way, Tom. Take it slow, take it easy - I have everything else covered until you are back on your feet.", "offer one concrete covered task"),
    _m(C, "Graduation", "Maya, you did it! All those late nights just turned into a diploma with your name on it. Proud does not even cover it - watching you work for this has been the honor of knowing you. Now go use that big brain on something wonderful.", "name the degree and one late-night memory"),
    _m(C, "Wedding", "Sofia and James, wishing you a marriage as joyful as this wedding day. Love chose well with you two. I promise excellent dance-floor energy and lifelong cheering from the sidelines.", "use both names and one detail from the day"),
    _m(C, "New Baby", "Welcome to the world, little Noah - and congratulations, Emma and Liam! You are going to be amazing parents; I already know it. Sleep now, all three of you - these years fly faster than anyone warns you.", "use the baby's name and the parents' names"),
    _m(C, "New Home", "Happy new home, the Rivera family! May the walls hold laughter, the kitchen hold good smells, and my visits be frequent. I am bringing snacks to the housewarming and staying for the tour.", "name the family and the neighborhood"),
    _m(C, "Retirement", "Happy retirement, Captain Alvarez! Thirty years of keeping everyone safe and on course - now the calendar is finally yours. First order of business: absolutely nothing, for as long as you like.", "name their years of service and one legendary story"),
    _m(C, "Birthday", "Happy 50th, Diane! Half a century of being the person everyone calls when it matters. You have collected friends the way other people collect stamps - carefully, and all over the world. Here is to the next fifty.", "name the milestone age and one defining trait"),
    _m(C, "Graduation", "Congratulations, graduate! Kevin, from the kid who took apart the toaster to the engineer holding the degree - what a road. Your whole family is bursting. Go build something the world needs.", "name the field of study and one childhood clue"),
    _m(C, "New Job", "First day nerves are just excitement in disguise, Ana. You earned this role the hard way - by being excellent when nobody was watching. Now everybody is watching. You have got this.", "name the role and one strength they bring"),
    _m(C, "Wedding", "To my sister Lily on her wedding day: I have watched you love fiercely your whole life, and today you married someone who loves you back exactly as hard. Welcome to the family, Noah - take good care of my favorite person.", "write from your real relationship to the couple"),
    _m(C, "New Baby", "A brand-new human! Congratulations, Zara - little Zane is lucky to land with a mom like you. Rest when the baby rests (everyone says it because it is true), and call me for the 3 a.m. shift anytime.", "use real names and offer one real night-shift"),
    _m(C, "Birthday", "Happy birthday, Grandma June! Ninety years young and still beating everyone at cards. You are the root system of this whole family - everything good in us grew from you. We love you more than words, but we will keep trying with words anyway.", "name the age and one family truth"),
    _m(C, "Retirement", "After 25 years of shaping young minds, Mrs. Okafor, you have earned every slow morning coming your way. Generations of students carry your lessons - including me. Enjoy the next chapter; it is going to be a good one.", "name their impact and one lesson you kept"),
    _m(A, "Wedding", "On this day, two histories became one story. Amara and Kwame: may your marriage be a long conversation that never runs out of things worth saying, a house where laughter is the load-bearing wall, and a partnership where each of you makes the other braver. It is the honor of my life to witness the beginning.", "keep the elevated tone only if it matches your voice"),
    _m(A, "Graduation", "They hand you the diploma in seconds, but you earned it over years - the 2 a.m. study sessions, the doubt, the stubborn return. David, a PhD is not a piece of paper; it is proof you can walk into the unknown and come back with answers. The world needs what you found. Congratulations, Doctor.", "name the doctorate field and the journey"),
    _m(A, "New Baby", "Somewhere tonight, two people are learning the particular weight of a sleeping newborn - the heaviest, lightest thing in the world. To Sofia and Marco on the arrival of Lucia: you are now members of the oldest club there is, and the dues are paid in lullabies. Welcome. She is perfect, and so are you for loving her.", "use all three names; keep it tender"),
    _m(A, "Birthday", "Sixty years, Robert. That is 21,900 days of showing up - for family, for friends, for every hard thing that asked something of you. Today we do not celebrate a number; we celebrate the man the number describes. Happy birthday to the steadiest person I know.", "do the day-count math for their age"),
    _m(A, "Retirement", "The last bell rings differently when it is yours, Ms. Delgado. Forty years of first days and last days, of shy Septembers turned into confident Junes. You did not just teach subjects; you taught children they were capable. That work does not retire - it graduates, thousands of times over. Enjoy everything.", "name the school and the legacy"),
    _m(A, "Congratulations", "There are wins, and then there are the ones that change the shape of a life. Winning the regional championship after three losing seasons, team - that is the second kind. You learned the hard lesson sports exist to teach: that losing together teaches you how to win together. Champions, all of you. Savor it.", "name the specific long-awaited win"),
    _m(A, "Thank You", "I have been trying to write this for a week, because some thanks are too big for a card. Dr. Patel: you did not just treat the illness, you treated the fear. Every appointment, you looked me in the eye and told me the truth kindly. I am well today because you were excellent every day. Thank you is not enough, but it is what I have, given with everything I have.", "for life-sized gratitude, be specific and unhurried"),
    _m(A, "New Home", "A house is lumber and paint until a family moves in - then it starts collecting the only currency that matters: mornings. To the Nguyen family in your beautiful new home on Willow Lane: may these walls learn your laughter quickly, may the kitchen become command central, and may every guest leave feeling like family. Housewarming is Saturday; I am bringing the good dessert.", "name the street and the first gathering"),
    _m(A, "Birthday", "Eighteen years ago you arrived and immediately started rearranging everything - the furniture, the schedule, and eventually my entire understanding of what matters. Happy 18th, Jayden. Childhood is officially complete; the main quest begins now. Whatever you choose, choose it boldly. I will be right here, proud either way.", "for milestone birthdays, mark the passage honestly"),
    _m(A, "Get Well", "The hospital room is quiet at 3 a.m., and I know, because I have been thinking of you there. Maria, bodies heal on their own stubborn schedule, and yours has always been tougher than it looks. Rest. Let the machines beep. Let people bring the bad pudding. I will be there Thursday with the good pudding and all the time in the world.", "for serious illness, be present more than poetic"),
    _m(A, "Wedding", "Fifty years from now, someone will ask how you knew. You will not remember the flowers or the seating chart - you will remember this exact feeling, right now, looking at each other like the rest of the room faded out. Hold onto that. Congratulations, Elena and David: the adventure everyone warned you about is the best one there is.", "speak to the couple's future selves"),
]
