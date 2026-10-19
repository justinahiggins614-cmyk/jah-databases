# -*- coding: utf-8 -*-
"""Topic module: gen-palindrome-playground (GENERATOR class, first-release pick).
34 full sample records + REAL palindrome generator (see realgen).
Property of Justin Addam Higgins (JAH)."""
from w3lib import topic

CFG = {
    "slug": "gen-palindrome-playground",
    "prefix_pub": "JAH-PALPLA-",
    "prefix_sig": "JAH-PALPLAS-",
    "name_pub": "The Palindrome Playground Generator Database",
    "name_sig": "The Palindrome Playground Signature Generator Database",
    "tagline_pub": "Words and phrases that read the same backward and forward, every one machine-verified: single-word palindromes, classic phrase palindromes, palindrome names, and the mirror construction that builds brand-new palindromes from any two words - every record carrying the palindrome, its letter proof, and how to build your own, taught progressively along the ladder.",
    "tagline_sig": "The Signature mirror method: every palindrome a Signature reflection, the word meeting itself coming back. The full ladder from single-word mirrors through phrase palindromes and palindrome names to the mirror construction that builds new palindromes from any two words, reframed as Signature science. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai_pub": "JAH Palindrome Playground Archivist",
    "ai_sig": "JAH Palindrome Playground Signature Archivist",
    "role_pub": "palindrome archivist - teaching words and phrases that read the same backward, verifying every mirror by letter, and showing how to build brand-new palindromes from any two words",
    "role_sig": "Signature palindrome archivist - teaching the Signature mirror method across words, phrases, names, and fresh mirror-built constructions",
    "greet_pub": "I am the JAH Palindrome Playground Archivist. Ask me for palindromes - words, phrases, names - or how to build your own with the mirror trick.",
    "greet_sig": "I am the JAH Palindrome Playground Signature Archivist. Ask me about the Signature mirror method and fresh-built palindromes.",
    "record_kind": "palindrome playground record",
    "record_kind_plural": "palindrome playground records",
    "demo_kind": "palindrome-verified",
    "demo_title": "Palindrome Playground Study",
    "search_ph": "Search palindromes, words, phrases, names, mirror building...",
    "chat_ph": "Ask about palindromes...",
    "gen_blurb": "Real working generator - every run builds a genuine, machine-verified palindrome: a word, a classic phrase, a name, or a brand-new mirror-built construction. Never a structural sample.",
    "about_archive": "Seeded sample palindromes, each machine-verified letter by letter, marching toward one million records. Presented in teaching-ladder order: word mirrors, phrase mirrors, names, then the mirror construction.",
    "reqs_default": "No equipment needed - eyes, a voice to read aloud, and curiosity. A pencil helps for building your own.",
    "stds_default": "Every palindrome in this database is verified by letter: stripped to lowercase letters, the string must equal its own reverse, minimum 3 letters.",
    "cites_default": ["JAH Databases puzzle verification standard v1.0", "Palindrome Playground mirror-construction rule"],
}
CUSTOM_GEN = "palindrome"


def _w(word, fact):
    low = word.lower()
    return topic(
        "Foundations", 'Palindrome word: "%s"' % word,
        desc_pub='The word "%s" is a palindrome: read it backward and it is unchanged. Letter proof: "%s" reversed is "%s" - identical, all %d letters. %s Say it aloud forward, then backward, and feel the symmetry lock in.'
        % (word, low, low[::-1], len(word), fact),
        desc_sig='Signature mirror reading: "%s" meets itself coming back, the Signature reflection holding steady in both directions. The Signature edition treats every palindrome as a closed loop - a word that needs no other word to be complete.'
        % word,
        how_pub='Verify it yourself: write "%s", then write it backward underneath, letter by letter, and compare. Then hunt for the palindrome inside longer words you know - the mirror hides everywhere once you start looking.'
        % word,
        how_sig='The Signature way to hold a palindrome: speak it forward once, backward once, then forward again without pausing - the loop closes and the word feels inevitable.',
        keys=["Reads identically forward and backward - verified by letter, not by impression.",
              "%d letters, every one mirrored around the center." % len(word),
              "Single-word palindromes are the atoms of the playground.",
              "Collect them: each one you memorize makes phrase-building easier."],
        demo=("check", {"code": ["W = %r" % low, "L = ''.join(c for c in W if c.isalpha())"],
                        "checks": [("word", "W"), ("reversed", "L[::-1]"),
                                   ("is_palindrome", "L == L[::-1]"),
                                   ("letter_count", "len(L) == %d" % len(low))]}),
    )


def _p(phrase, note):
    letters = "".join(c for c in phrase.lower() if c.isalpha())
    return topic(
        "Compounded", 'Palindrome phrase: "%s"' % phrase,
        desc_pub='The phrase "%s" is a genuine phrase palindrome. Letter proof: stripped to lowercase letters it becomes "%s" (%d letters), and reversed it is "%s" - identical. %s Phrase palindromes ignore spaces, punctuation, and capitalization; only the letter order matters.'
        % (phrase, letters, len(letters), letters[::-1], note),
        desc_sig='Signature mirror reading: the whole phrase folds onto itself like a Signature seal pressed twice - the second impression landing exactly on the first. The Signature edition reads phrase palindromes as sentences that argue with themselves and agree.',
        how_pub='Verify it: cross out every space and punctuation mark, write the bare letters, then read them backward. Then try composing your own short one - three or four words - before attempting the classics.',
        how_sig='The Signature way: read the phrase forward at normal speed, then backward slowly, letting each mirrored pair click - the phrase teaches patience in both directions.',
        keys=["True phrase palindrome - verified across all %d letters." % len(letters),
              "Spaces, punctuation, and case are ignored; letter order is everything.",
              "Classic-grade construction: memorable, not just mechanical.",
              "Use it as a memory anchor: palindromes are almost impossible to misremember."],
        demo=("check", {"code": ["P = %r" % phrase.lower(), "L = ''.join(c for c in P if c.isalpha())"],
                        "checks": [("letters_only", "L"), ("reversed", "L[::-1]"),
                                   ("is_palindrome", "L == L[::-1]"),
                                   ("letter_count", "len(L) == %d" % len(letters))]}),
    )


def _b(a, b, title_note):
    phrase = "%s %s %s %s" % (a, b, b[::-1], a[::-1])
    letters = "".join(c for c in phrase.lower() if c.isalpha())
    return topic(
        "Advanced", 'Built palindrome: "%s"' % phrase,
        desc_pub='Fresh-built palindrome: "%s". Construction: "%s" + "%s" + reverse("%s")="%s" + reverse("%s")="%s". Letter proof: "%s" reversed is identical - guaranteed by the mirror construction, because reversing A+B+reverse(B)+reverse(A) returns exactly A+B+reverse(B)+reverse(A). %s This is the master trick of the playground: ANY two words build a valid palindrome this way.'
        % (phrase, a, b, b, b[::-1], a, a[::-1], letters, title_note),
        desc_sig='Signature mirror method, formal: the builder takes two words and returns them to themselves through the mirror - nothing added, nothing lost, the Signature reflection complete. The Signature edition treats every built palindrome as proof that symmetry is a choice you can make.',
        how_pub='Build your own: pick any two words A and B, then write A, B, reverse(B), reverse(A). Check it by the letter test. Then try to make the result MEAN something - sense is the hard part, symmetry is free.',
        how_sig='The Signature way to build: choose words that already want to meet - opposites, pairs, echoes - then mirror them and read the result aloud like an incantation.',
        keys=["Mirror construction: A + B + reverse(B) + reverse(A) is ALWAYS a palindrome.",
              "Proof by reversal: reversing the construction returns the construction.",
              "Works with any two words - symmetry is free, meaning is the craft.",
              "Master move: choose A and B so the mirrored phrase tells a tiny story."],
        demo=("check", {"code": ["A = %r" % a, "B = %r" % b,
                                 "PH = A + ' ' + B + ' ' + B[::-1] + ' ' + A[::-1]",
                                 "L = ''.join(c for c in PH if c.isalpha())"],
                        "checks": [("built_phrase", "PH"), ("is_palindrome", "L == L[::-1]"),
                                   ("construction_holds", "L == (A + B + B[::-1] + A[::-1])")]}),
    )


TOPICS = [
    _w("racecar", "The classic first palindrome - seven letters, the one every mirror starts with."),
    _w("level", "Five letters, and also a word about balance - fitting, since it balances perfectly."),
    _w("kayak", "The boat that goes both ways, named with a word that reads both ways."),
    _w("rotator", "Seven letters describing exactly what the word does: it rotates onto itself."),
    _w("deified", "Seven letters meaning made divine - the palindrome canon's showpiece."),
    _w("repaper", "Seven letters: to paper again, and to read again backward."),
    _w("reviver", "One who revives - and the word revives itself every time you reverse it."),
    _w("stats", "Five letters, the plural of stat - short, common, and perfectly mirrored."),
    _w("solos", "Musical solos, mirrored - one performer, two directions."),
    _w("tenet", "A principle held true - and the word holds true in reverse."),
    _w("redder", "The comparative of red, six letters, mirrored around its double-d heart."),
    _p("A man, a plan, a canal: Panama",
       "The most famous phrase palindrome in English - 21 letters telling a whole tiny history."),
    _p("Was it a car or a cat I saw",
       "A question that answers itself - the doubt reads the same in both directions."),
    _p("Never odd or even",
       "Fourteen letters of pure logic: the phrase about parity is itself perfectly even-handed."),
    _p("Do geese see God",
       "The philosophical palindrome - asked by geese, answered by mirrors."),
    _p("Madam, in Eden, I'm Adam",
       "The biblical garden in mirror form - the first palindrome joke ever told."),
    _p("No lemon, no melon",
       "Fourteen letters of citrus wisdom: sour or sweet, the mirror does not care."),
    _p("Step on no pets",
       "Twelve letters and a household rule - the friendliest palindrome ever built."),
    _p("Live on time, emit no evil",
       "Eighteen letters of life advice that reads the same as its own warning."),
    _p("Mr. Owl ate my metal worm",
       "Nineteen letters of nocturnal nonsense - the owl's dinner, mirrored."),
    _p("Pull up if I pull up",
       "Sixteen letters, a driving instruction that works in reverse too."),
    _p("Rise to vote, sir",
       "Thirteen letters of civic duty - democracy, mirrored."),
    _p("Taco cat",
       "Seven letters, the internet's favorite palindrome - lunch that reads both ways."),
    _b("step", "on", "The 'step on no pets' family - the friendliest mirror ever built."),
    _b("live", "on", "The 'live on no evil' family - advice that warns itself."),
    _b("star", "at", "Try it: any two words work, but pairs with meaning sing."),
    _b("draw", "it", "Short words build fast - then hunt for ones that tell stories."),
    _b("loop", "up", "The loop closes on itself, as loops do."),
    _b("dennis", "it", "Longer A-words build longer mirrors - the math never breaks."),
    _b("part", "so", "Opposites and pairs make the best mirrors - 'part so os trap' tells a tiny tale."),
    _b("reward", "it", "Six-letter A, two-letter B: the construction scales to any size."),
    _b("straw", "in", "Say it aloud: the mirror clicks when the halves meet."),
    _b("diaper", "up", "Silly inputs, perfect outputs - the mirror has no taste, only symmetry."),
    _b("tenet", "so", "A palindrome A-word doubled through the mirror - symmetry squared."),
]
