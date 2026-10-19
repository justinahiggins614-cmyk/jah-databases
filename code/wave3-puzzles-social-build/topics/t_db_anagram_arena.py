# -*- coding: utf-8 -*-
"""Topic module: db-anagram-arena. Property of Justin Addam Higgins (JAH)."""
from w3lib import mkcfg, T

CFG = mkcfg({
    "slug": "db-anagram-arena", "name": "The Anagram Arena", "pfx": "JAH-ANAARE-",
    "tagline_pub": "Word rearrangement challenges with hints and full solution explanations - single-word anagrams, famous phrase anagrams, and fiendish long ones: every record carrying the scrambled letters, a real hint, the verified solution, and why the letters lock together, taught progressively along the ladder.",
    "tagline_sig": "The Signature letter-forge: every anagram a Signature recombination, the same letters reborn as new meaning. The full ladder from quick word flips through famous phrase anagrams to Signature-grade letter epics. Clearly labeled Signature-made, never presented as authentic public record.",
    "ai": "Anagram Arena",
    "role_pub": "anagram master - dealing scrambled letters with fair hints and proving every solution letter by letter",
    "role_sig": "Signature anagram master - forging Signature recombinations from the same letters",
    "record_kind": "anagram puzzle record", "record_kind_plural": "anagram puzzles",
    "demo_kind": "anagram-check", "demo_title": "Anagram Arena Study",
    "search_ph": "Search anagrams, scrambled words, hints, solutions...",
    "chat_ph": "Ask for an anagram...",
    "gen_blurb": "Generate clearly-labeled anagram studies. Seeded archive records are the authoritative entries.",
    "about_archive": "Seeded anagram puzzles, every solution letter-verified, marching toward one million records. Presented in teaching-ladder order: word anagrams, phrase anagrams, epic anagrams.",
    "reqs": "A pencil and paper (or a good memory). No dictionary needed - the hints are fair.",
    "stds": "Every solution is verified by letter count: sorted scrambled letters must exactly equal sorted solution letters.",
    "cites": ["JAH Databases puzzle verification standard v1.0"],
})


def _an(tier, scrambled, answer, hint, note):
    sc = "".join(c for c in scrambled.lower() if c.isalpha())
    an = "".join(c for c in answer.lower() if c.isalpha())
    return T(
        tier, 'Anagram: "%s"' % scrambled,
        desc_pub='UNSCRAMBLE THIS: "%s" (%d letters). Hint: %s.\n\nSOLUTION: "%s". Letter proof: the scrambled letters sorted are "%s" and the solution letters sorted are "%s" - identical, so every letter is used exactly once. %s'
        % (scrambled, len(sc), hint, answer, "".join(sorted(sc)), "".join(sorted(an)), note),
        desc_sig='Signature letter-forge: "%s" melted down and recast as "%s" - same letters, new meaning, the Signature recombination complete. The Signature edition treats every solved anagram as a small rebirth.' % (scrambled, answer),
        how_pub='Solve it: count the letters, hunt for common endings (-ING, -TION, -ED), and try the hint first. If stuck, write the letters in a circle - the eye sees patterns the line hides.',
        how_sig='The Signature way: solve it aloud, letter by letter, then say the solution like you forged it yourself.',
        keys=['Scrambled: "%s" (%d letters).' % (scrambled, len(sc)),
              'Hint: %s' % hint,
              'Solution: "%s" - letter-verified.' % answer,
              'Technique note: %s' % note],
        demo=("check", {"code": ["SC = %r" % sc, "AN = %r" % an],
                        "checks": [("letter_count", "len(SC) == %d" % len(sc)),
                                   ("valid_anagram", "sorted(SC) == sorted(AN)"),
                                   ("solution_uses_all_letters", "len(AN) == len(SC)")]}),
    )


B, C, A = "Foundations", "Compounded", "Advanced"
TOPICS = [
    _an(B, "SILENT", "LISTEN", "what you do with your ears", "The classic first anagram - the letters of silence become the act of listening."),
    _an(B, "DUSTY", "STUDY", "what you do with books", "Dust off the books: the letters agree with the hint."),
    _an(B, "NIGHT", "THING", "a general word for an object", "Five letters, one vowel moved - small anagrams teach the eye to rotate letters."),
    _an(B, "EARTH", "HEART", "what beats in your chest", "The planet and the pulse share their letters - poetry the letters wrote themselves."),
    _an(B, "ACT", "CAT", "a pet that naps all day", "Three letters, instant solve - the warm-up rep."),
    _an(B, "STRESSED", "DESSERTS", "what you crave when tense", "Stress spelled backward-ish becomes its own cure - the letters knew before you did."),
    _an(B, "CHEATER", "TEACHER", "who gives the test", "A mischievous classic: the two roles share every letter."),
    _an(B, "ANGER", "RANGE", "where you practice archery", "Rearrange the feeling, find the field - anagrams as emotional alchemy."),
    _an(B, "CIDER", "CRIED", "what you do at sad movies", "Apple drink to tears in five letters flat."),
    _an(B, "SAVE", "VASE", "it holds flowers", "Four letters, two common words - the minimal anagram."),
    _an(B, "LEMON", "MELON", "a bigger fruit", "Citrus to melon: one letter slides, the fruit grows."),
    _an(C, "THE EYES", "THEY SEE", "what eyes do", "The phrase describes itself - the letters confess their own meaning."),
    _an(C, "DORMITORY", "DIRTY ROOM", "what it becomes by Friday", "Every student's room, anagrammatically inevitable."),
    _an(C, "ASTRONOMER", "MOON STARER", "their hobby, two words", "The profession contains its own pastime - the stars wrote this one."),
    _an(C, "DESPERATION", "A ROPE ENDS IT", "grim, four words", "Dark and perfect - the letters tell a whole tiny tragedy."),
    _an(C, "SLOT MACHINES", "CASH LOST IN ME", "the gambler's lament", "The casino's business model, hidden in its own name."),
    _an(C, "THE COUNTRY SIDE", "NO CITY DUST HERE", "the air is cleaner", "Fifteen letters of fresh air - the countryside anagrammatically brags."),
    _an(C, "CONVERSATION", "VOICES RANT ON", "what happens at loud dinners", "Twelve letters that describe every family holiday."),
    _an(C, "A DECIMAL POINT", "I'M A DOT IN PLACE", "tiny punctuation", "The punctuation mark introduces itself, anagrammatically."),
    _an(C, "ELEVEN PLUS TWO", "TWELVE PLUS ONE", "both equal 13", "The math checks out AND the letters check out - a double proof."),
    _an(C, "A GENTLEMAN", "ELEGANT MAN", "well-dressed fellow", "Manners rearranged into style - the definition, anagrammatically."),
    _an(C, "CLINT EASTWOOD", "OLD WEST ACTION", "his movie genre", "The actor's name contains his entire filmography."),
    _an(C, "PRESBYTERIAN", "BEST IN PRAYER", "devout, three words", "Twelve letters of devotion, rearranged into a compliment."),
    _an(A, "WILLIAM SHAKESPEARE", "I AM A WEAKISH SPELLER", "the Bard's confession", "The greatest writer in English, anagrammatically humble."),
    _an(A, "FLORENCE NIGHTINGALE", "FLIT ON, CHEERING ANGEL", "the lady with the lamp", "Nineteen letters: the nurse's name becomes her job description."),
    _an(A, "THE MEANING OF LIFE", "THE FINE GAME OF NIL", "philosophical, sixteen letters", "The answer to everything, rearranged into a shrug."),
    _an(A, "SCHOOLMASTER", "THE CLASSROOM", "where they work", "The job title contains the workplace - twelve letters, zero coincidence."),
    _an(A, "THE DETECTIVES", "DETECT THIEVES", "their actual job", "Thirteen letters: the profession is the job description."),
    _an(A, "STATUE OF LIBERTY", "BUILT TO STAY FREE", "her promise", "Fifteen letters of freedom, forged into a mission statement."),
    _an(A, "SNOOZE ALARMS", "ALAS! NO MORE Z'S", "Monday morning", "The alarm clock's tragedy, told by its own letters."),
    _an(A, "THE MORSE CODE", "HERE COME DOTS", "what it looks like", "The code introduces itself in dots and dashes - well, letters."),
    _an(A, "TOM MARVOLO RIDDLE", "I AM LORD VOLDEMORT", "the reveal", "The most famous literary anagram ever printed - sixteen letters of villainy."),
    _an(A, "ASTRONOMERS", "NO MORE STARS", "light pollution", "Eleven letters of astronomical melancholy."),
    _an(A, "THE EARTHQUAKES", "THAT QUEER SHAKE", "seismology", "Fourteen letters that wobble exactly like their subject."),
]
