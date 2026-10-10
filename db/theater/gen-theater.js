/* JAH Theater Database generator — jahdb-theater-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: seed -> full theater entry. 1,000,000 address space (seed % 1M).
   Records are either sourced (real, verifiable theater facts) or Signature-generated
   (homegrown fictional entries), labeled in `origin`. Never fabricates real-world facts. */
(function () {
'use strict';
function prng(seed) { var a = (seed >>> 0) || 1; return function () { a |= 0; a = (a + 0x6D2B79F5) | 0; var t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function pick(a, r) { return a[(r() * a.length) | 0]; }
function ri(r, a, b) { return a + ((r() * (b - a + 1)) | 0); }
function shuffle(a, r) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = (r() * (i + 1)) | 0; var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function interleave(lists) { var out = [], i = 0, more = true; while (more) { more = false; for (var k = 0; k < lists.length; k++) { if (i < lists[k].length) { out.push(lists[k][i]); more = true; } } i++; } return out; }

var SLUG = 'theater';
var PREFIX = 'JAH-THT-';
var VERSION = 'jahdb-theater-1.0';
var RECORD_KIND = 'theater entry';
var CATS = ['play', 'playwright', 'theatrical-form', 'stagecraft'];

/* ================= REAL (sourced) data — verifiable theater facts ================= */
/* Plays: [title, playwright, year, acts, genre, setting, logline, themes, note] */
var REAL_PLAYS = [
['Hamlet', 'William Shakespeare', 'c. 1600', 5, 'tragedy', 'Elsinore Castle, Denmark', 'A Danish prince feigns madness to investigate and avenge his father\u2019s murder by his uncle Claudius.', 'revenge; madness; mortality; appearance vs reality', 'Famous for the \u201cTo be, or not to be\u201d soliloquy; Shakespeare\u2019s longest play.'],
['Macbeth', 'William Shakespeare', '1606', 5, 'tragedy', 'Scotland', 'A Scottish general, urged by prophecy and his wife, murders the king and seizes the throne, then falls to guilt and ruin.', 'ambition; guilt; fate vs free will', 'Features the three witches and Lady Macbeth\u2019s sleepwalking scene.'],
['Othello', 'William Shakespeare', '1603', 5, 'tragedy', 'Venice and Cyprus', 'The ensign Iago poisons the mind of the Moorish general Othello against his wife Desdemona with lies of infidelity.', 'jealousy; manipulation; race; trust', 'Iago is one of literature\u2019s most studied villains.'],
['Romeo and Juliet', 'William Shakespeare', 'c. 1595', 5, 'tragedy', 'Verona, Italy', 'Two young lovers from feuding families marry in secret; miscommunication leads to their double suicide.', 'love; fate; family feud', 'The balcony scene is among the most quoted in theater.'],
['King Lear', 'William Shakespeare', '1606', 5, 'tragedy', 'Ancient Britain', 'An aging king divides his kingdom among his daughters by flattery, and is destroyed by the two who flattered him.', 'power; blindness; loyalty; nature', 'The storm scenes and the blinding of Gloucester are landmark stage moments.'],
['A Midsummer Night\u2019s Dream', 'William Shakespeare', 'c. 1595', 5, 'comedy', 'Athens and a nearby forest', 'Lovers flee into a fairy-haunted forest where Puck\u2019s mischief scrambles every romance before dawn sets things right.', 'love; illusion; dreams', 'Ends with Puck\u2019s famous apology epilogue to the audience.'],
['The Tempest', 'William Shakespeare', '1611', 5, 'romance', 'A remote island', 'The exiled Duke Prospero conjures a storm to shipwreck his enemies on his island and engineers forgiveness.', 'forgiveness; power; colonialism', 'Often read as Shakespeare\u2019s farewell to the stage.'],
['Much Ado About Nothing', 'William Shakespeare', 'c. 1598', 5, 'comedy', 'Messina, Sicily', 'Benedick and Beatrice trade witty insults while friends scheme to pair them off; a slander plot nearly ruins Hero\u2019s wedding.', 'wit; honor; deception', 'The \u201cmerry war\u201d between Beatrice and Benedick is a comic high point.'],
['The Merchant of Venice', 'William Shakespeare', 'c. 1596', 5, 'comedy', 'Venice and Belmont', 'Antonio borrows from the moneylender Shylock, who demands a pound of flesh when the loan defaults.', 'justice; mercy; prejudice', 'Portia\u2019s \u201cquality of mercy\u201d speech is a centerpiece.'],
['Twelfth Night', 'William Shakespeare', 'c. 1601', 5, 'comedy', 'Illyria', 'Shipwrecked Viola disguises herself as a boy and serves Duke Orsino, tangling three hearts in mistaken identity.', 'identity; love; disguise', 'Features the clown Feste and Malvolio\u2019s humiliation.'],
['Julius Caesar', 'William Shakespeare', '1599', 5, 'tragedy', 'Ancient Rome', 'Brutus joins the conspiracy against Caesar, then faces Mark Antony\u2019s rhetoric and civil war.', 'power; betrayal; rhetoric', 'Antony\u2019s \u201cFriends, Romans, countrymen\u201d funeral oration.'],
['Henry V', 'William Shakespeare', '1599', 5, 'history', 'England and France', 'The young English king leads his outnumbered army to victory at Agincourt.', 'leadership; honor; war', 'Contains the St. Crispin\u2019s Day speech.'],
['Richard III', 'William Shakespeare', 'c. 1592', 5, 'history/tragedy', 'England, Wars of the Roses', 'The deformed Duke of Gloucester murders his way to the throne and is slain at Bosworth Field.', 'ambition; villainy', 'Opens with the \u201cNow is the winter of our discontent\u201d soliloquy.'],
['The Taming of the Shrew', 'William Shakespeare', 'c. 1593', 5, 'comedy', 'Padua, Italy', 'Petruchio sets out to \u201ctame\u201d the sharp-tongued Katherina through a campaign of outrageous behavior.', 'marriage; gender roles', 'Often staged today with a critical eye on its gender politics.'],
['As You Like It', 'William Shakespeare', 'c. 1599', 5, 'comedy', 'The Forest of Arden', 'Exiled nobles find love and philosophy in the forest; Rosalind, disguised as a boy, tutors her own suitor.', 'love; nature; identity', 'Source of the \u201cAll the world\u2019s a stage\u201d monologue.'],
['A Streetcar Named Desire', 'Tennessee Williams', '1947', 11, 'drama', 'New Orleans', 'The fragile Blanche DuBois moves in with her sister Stella and clashes catastrophically with brother-in-law Stanley Kowalski.', 'illusion; desire; class', 'Won the Pulitzer Prize for Drama in 1948.'],
['Death of a Salesman', 'Arthur Miller', '1949', 2, 'tragedy', 'Brooklyn, New York', 'Willy Loman, a failing traveling salesman, collapses under the gap between the American Dream and his reality.', 'the American Dream; family; identity', 'Won the Pulitzer Prize for Drama in 1949.'],
['The Crucible', 'Arthur Miller', '1953', 4, 'drama', 'Salem, Massachusetts, 1692', 'The Salem witch trials become an allegory for McCarthy-era hysteria as John Proctor refuses to sign a false confession.', 'hysteria; integrity; reputation', 'Written during the anti-communist investigations of the 1950s.'],
['Waiting for Godot', 'Samuel Beckett', '1953', 2, 'tragicomedy', 'A country road, by a tree', 'Vladimir and Estragon wait for the arrival of the never-seen Godot, filling the time with routines and talk.', 'existentialism; time; habit', 'A landmark of the Theatre of the Absurd.'],
['Our Town', 'Thornton Wilder', '1938', 3, 'drama', 'Grover\u2019s Corners, New Hampshire', 'The Stage Manager narrates the ordinary lives, loves, and deaths of two small-town families.', 'everyday life; time; mortality', 'Won the Pulitzer Prize for Drama in 1938; famously bare stage.'],
['Long Day\u2019s Journey Into Night', 'Eugene O\u2019Neill', '1956', 4, 'tragedy', 'A Connecticut summer home, 1912', 'The Tyrone family tears itself open over one long day of addiction, illness, and blame.', 'family; addiction; memory', 'Won the Pulitzer Prize for Drama in 1957; written in 1941.'],
['A Raisin in the Sun', 'Lorraine Hansberry', '1959', 3, 'drama', 'Chicago\u2019s South Side', 'The Younger family debates how to spend a life-insurance check while facing racist housing barriers.', 'race; dreams; family', 'The first Broadway play by a Black woman.'],
['The Glass Menagerie', 'Tennessee Williams', '1944', 7, 'memory play', 'St. Louis', 'Tom Wingfield recalls his fragile sister Laura, her glass animals, and the gentleman caller who changes everything.', 'memory; escape; fragility', 'Williams called it a \u201cmemory play\u201d narrated by Tom.'],
['Who\u2019s Afraid of Virginia Woolf?', 'Edward Albee', '1962', 3, 'drama', 'A New England college town', 'George and Martha drag a younger couple into a night of brutal marital games.', 'marriage; illusion; truth', 'A landmark of American realism; famously profane for its time.'],
['Fences', 'August Wilson', '1985', 2, 'drama', 'Pittsburgh, 1950s', 'Troy Maxson, a former ballplayer, builds literal and figurative fences around his family.', 'race; fatherhood; responsibility', 'Won the Pulitzer Prize for Drama in 1987; part of Wilson\u2019s Century Cycle.'],
['The Importance of Being Earnest', 'Oscar Wilde', '1895', 3, 'comedy of manners', 'London and the country', 'Two bachelors invent alter egos named Ernest to escape social duties, and the lies tangle.', 'identity; satire; social convention', 'Wilde\u2019s most performed comedy; famed for its epigrams.'],
['Pygmalion', 'George Bernard Shaw', '1913', 5, 'comedy', 'London', 'Professor Higgins bets he can pass flower girl Eliza Doolittle off as a duchess by teaching her to speak.', 'class; language; identity', 'Basis for the musical My Fair Lady.'],
['A Doll\u2019s House', 'Henrik Ibsen', '1879', 3, 'drama', 'Norway', 'Nora Helmer walks out on her marriage, slamming the door on a life of being treated as a doll.', 'independence; marriage', 'The door slam was called \u201cthe shot heard round the world\u201d of modern drama.'],
['Hedda Gabler', 'Henrik Ibsen', '1891', 4, 'tragedy', 'Norway', 'The newly married Hedda, bored and trapped, destroys the people around her with cold precision.', 'freedom; boredom; power', 'One of the great complex roles for actresses.'],
['The Cherry Orchard', 'Anton Chekhov', '1904', 4, 'comedy/drama', 'Russia', 'An aristocratic family loses its beloved cherry orchard to debt as the old order fades.', 'change; loss; class', 'Chekhov\u2019s last play; premiered the year he died.'],
['Three Sisters', 'Anton Chekhov', '1901', 4, 'drama', 'A provincial Russian town', 'Three sisters dream of returning to Moscow while life quietly passes them by.', 'longing; time; unfulfilled dreams', 'Famous for its atmosphere of stalled hope.'],
['Uncle Vanya', 'Anton Chekhov', '1899', 4, 'drama', 'A Russian country estate', 'Vanya\u2019s lifetime of wasted labor for a pompous professor erupts in despair and a failed shooting.', 'wasted life; regret', 'Ends with Sonya\u2019s consoling vision of rest after death.'],
['The Seagull', 'Anton Chekhov', '1896', 4, 'drama', 'A Russian country estate', 'Young playwright Treplev loves Nina, who loves the famous writer Trigorin; art and love destroy them.', 'art; love; ambition', 'Its 1898 Moscow Art Theatre revival made Chekhov\u2019s reputation.'],
['Antigone', 'Sophocles', 'c. 441 BC', 1, 'tragedy', 'Thebes', 'Antigone defies King Creon\u2019s edict to bury her brother, choosing divine law over human law.', 'duty; civil disobedience', 'One of the most revived Greek tragedies.'],
['Oedipus Rex', 'Sophocles', 'c. 429 BC', 1, 'tragedy', 'Thebes', 'Oedipus hunts the killer of Laius and discovers the killer is himself.', 'fate; knowledge; blindness', 'Aristotle\u2019s model of perfect tragic structure.'],
['Medea', 'Euripides', '431 BC', 1, 'tragedy', 'Corinth', 'Abandoned by Jason, Medea takes revenge by murdering his new bride and her own children.', 'betrayal; revenge; gender', 'A searing study of a wronged woman\u2019s fury.'],
['Lysistrata', 'Aristophanes', '411 BC', 1, 'comedy', 'Athens and Sparta', 'The women of Greece withhold sex to force their husbands to end the Peloponnesian War.', 'war; peace; gender', 'An ancient anti-war sex comedy.'],
['Tartuffe', 'Moli\u00e8re', '1664', 5, 'comedy', 'Paris', 'A household falls under the spell of the pious fraud Tartuffe until his hypocrisy is exposed.', 'hypocrisy; religious fraud', 'Banned for years for offending the church.'],
['The Misanthrope', 'Moli\u00e8re', '1666', 5, 'comedy of manners', 'Paris', 'Alceste\u2019s brutal honesty collides with a society built on polite flattery.', 'honesty; society', 'Considered Moli\u00e8re\u2019s most psychologically complex comedy.'],
['Cyrano de Bergerac', 'Edmond Rostand', '1897', 5, 'romantic drama', '17th-century France', 'The brilliant, large-nosed Cyrano ghost-writes love letters for a rival to win Roxane.', 'love; wit; self-image', 'Famous for the balcony scene and Cyrano\u2019s panache.'],
['The Phantom of the Opera', 'Andrew Lloyd Webber', '1986', 2, 'musical', 'The Paris Opera House', 'A masked musical genius haunts the opera house and obsesses over the singer Christine.', 'obsession; art; beauty', 'The longest-running show in Broadway history.'],
['Les Mis\u00e9rables', 'Claude-Michel Sch\u00f6nberg', '1985', 2, 'musical', '19th-century France', 'Ex-convict Jean Valjean\u2019s quest for redemption unfolds against revolution, adapted from Victor Hugo\u2019s novel.', 'redemption; justice; revolution', 'Music by Sch\u00f6nberg, lyrics by Alain Boublil and Jean-Marc Natel.'],
['Hamilton', 'Lin-Manuel Miranda', '2015', 2, 'musical', 'Revolutionary America', 'The life of Alexander Hamilton told through hip-hop, R\&B, and traditional show tunes.', 'ambition; legacy; immigration', 'Won the Pulitzer Prize for Drama in 2016.'],
['West Side Story', 'Leonard Bernstein', '1957', 2, 'musical', 'New York City', 'A modern Romeo and Juliet between a Jet and a Shark in gang-divided Manhattan.', 'love; prejudice; gang conflict', 'Lyrics by Stephen Sondheim; book by Arthur Laurents.'],
['Oklahoma!', 'Richard Rodgers', '1943', 2, 'musical', 'Oklahoma Territory, 1906', 'Cowboy Curly courts Laurey while farmhand Jud menaces them; a territory becomes a state.', 'community; love; frontier', 'The first Rodgers and Hammerstein collaboration; lyrics by Oscar Hammerstein II.'],
['The Sound of Music', 'Richard Rodgers', '1959', 2, 'musical', 'Austria, 1938', 'Maria, a novice nun, becomes governess to the von Trapp children and leads them from Nazi Austria.', 'family; courage; music', 'The last Rodgers and Hammerstein musical.'],
['My Fair Lady', 'Frederick Loewe', '1956', 2, 'musical', 'London', 'Henry Higgins transforms cockney Eliza Doolittle into a lady of society.', 'class; language', 'Book and lyrics by Alan Jay Lerner; adapted from Shaw\u2019s Pygmalion.'],
['Guys and Dolls', 'Frank Loesser', '1950', 2, 'musical', 'New York City', 'Gamblers and mission dolls collide over a bet about wooing a Salvation Army sergeant.', 'love; luck; redemption', 'Based on Damon Runyon\u2019s stories.'],
['Chicago', 'John Kander', '1975', 2, 'musical', '1920s Chicago', 'Murderesses Roxie Hart and Velma Kelly turn their trials into vaudeville fame.', 'celebrity; corruption; jazz', 'Lyrics by Fred Ebb; book by Ebb and Bob Fosse.'],
['Rent', 'Jonathan Larson', '1996', 2, 'musical', 'New York\u2019s East Village', 'Struggling artists love and grieve through a year shadowed by AIDS, after Puccini\u2019s La Boh\u00e8me.', 'community; art; mortality', 'Won the Pulitzer Prize for Drama in 1996.'],
['Wicked', 'Stephen Schwartz', '2003', 2, 'musical', 'The Land of Oz', 'The untold story of the witches of Oz: Elphaba and Glinda\u2019s friendship before good and evil split them.', 'friendship; prejudice; power', 'Adapted from Gregory Maguire\u2019s novel.'],
['The Lion King', 'Elton John', '1997', 2, 'musical', 'The African savanna', 'Simba flees after his father\u2019s death and must return to claim his place as king.', 'responsibility; family', 'Julie Taymor\u2019s puppetry won wide acclaim.'],
['Cabaret', 'John Kander', '1966', 2, 'musical', 'Berlin, 1931', 'Singer Sally Bowles and writer Cliff Bradshaw drift toward doom as the Nazis rise.', 'decadence; complicity', 'Lyrics by Fred Ebb; book by Joe Masteroff.'],
['Sweeney Todd', 'Stephen Sondheim', '1979', 2, 'musical', 'Victorian London', 'A vengeful barber murders his customers while Mrs. Lovett bakes them into pies.', 'revenge; greed', 'The Demon Barber of Fleet Street; a dark masterpiece.'],
['Into the Woods', 'Stephen Sondheim', '1987', 2, 'musical', 'A fairy-tale forest', 'Fairy-tale characters\u2019 wishes come true in Act One; Act Two shows the consequences.', 'wishes; responsibility; community', 'Book by James Lapine.'],
['A Chorus Line', 'Marvin Hamlisch', '1975', 1, 'musical', 'A Broadway audition', 'Seventeen dancers audition and reveal their lives to an unseen director.', 'ambition; identity; art', 'Won the Pulitzer Prize for Drama in 1976.'],
['Fiddler on the Roof', 'Jerry Bock', '1964', 2, 'musical', 'Anatevka, Russia, 1905', 'Tevye the milkman tries to hold tradition as his daughters marry and pogroms loom.', 'tradition; change; family', 'Lyrics by Sheldon Harnick; book by Joseph Stein.'],
['Cat on a Hot Tin Roof', 'Tennessee Williams', '1955', 3, 'drama', 'A Mississippi plantation', 'Brick\u2019s drinking and Big Daddy\u2019s lies explode over one birthday evening.', 'truth; family; mendacity', 'Won the Pulitzer Prize for Drama in 1955.'],
['The Iceman Cometh', 'Eugene O\u2019Neill', '1946', 4, 'drama', 'A New York bar, 1912', 'Barflys\u2019 pipe dreams collapse when the salesman Hickey arrives preaching honesty.', 'illusion; despair', 'A four-and-a-half-hour monument of American theater.'],
['The Zoo Story', 'Edward Albee', '1958', 1, 'drama', 'Central Park', 'The volatile Jerry forces the complacent Peter into a confrontation that ends in death.', 'alienation; communication', 'Albee\u2019s breakthrough one-act.'],
['The Bald Soprano', 'Eug\u00e8ne Ionesco', '1950', 1, 'absurdist comedy', 'A London suburb', 'Two couples exchange meaningless platitudes until language itself collapses.', 'language; absurdity', 'A founding work of the Theatre of the Absurd.'],
['Rhinoceros', 'Eug\u00e8ne Ionesco', '1959', 3, 'absurdist drama', 'A French town', 'One by one the townspeople turn into rhinoceroses; Berenger resists conformity.', 'conformity; fascism', 'Written as an allegory of totalitarian conformity.'],
['Endgame', 'Samuel Beckett', '1957', 1, 'tragicomedy', 'A bare room', 'The blind Hamm and his servant Clov enact the end of everything, again.', 'endings; dependency', 'Beckett\u2019s bleak companion to Godot.'],
['Krapp\u2019s Last Tape', 'Samuel Beckett', '1958', 1, 'drama', 'Krapp\u2019s den', 'An old man listens to tapes of his younger self and confronts a wasted life.', 'memory; regret', 'A one-man tour de force.'],
['The Birthday Party', 'Harold Pinter', '1958', 3, 'drama', 'A seaside boarding house', 'Two sinister visitors interrogate and break the lodger Stanley during his birthday party.', 'menace; identity', 'Pinter\u2019s breakthrough \u201ccomedy of menace.\u201d'],
['Betrayal', 'Harold Pinter', '1978', 2, 'drama', 'London and Venice', 'An affair is told backwards, from its end to its beginning.', 'memory; betrayal', 'Famous for its reverse chronology.'],
['Glengarry Glen Ross', 'David Mamet', '1984', 2, 'drama', 'A Chicago real-estate office', 'Desperate salesmen compete for leads in a brutal sales contest; a burglary follows.', 'capitalism; masculinity', 'Won the Pulitzer Prize for Drama in 1984.'],
['True West', 'Sam Shepard', '1980', 2, 'drama', 'Southern California', 'Two brothers \u2014 a screenwriter and a drifter \u2014 swap roles over one long visit.', 'brotherhood; identity', 'A landmark of American family drama.'],
['Buried Child', 'Sam Shepard', '1978', 3, 'drama', 'An Illinois farm', 'A family\u2019s buried secret surfaces with the return of a grandson.', 'family secrets; decay', 'Won the Pulitzer Prize for Drama in 1979.'],
['Angels in America', 'Tony Kushner', '1991', 2, 'epic drama', 'New York, 1980s', 'Gay men, Mormons, and angels collide during the AIDS crisis; subtitled \u201cA Gay Fantasia on National Themes.\u201d', 'AIDS; politics; spirituality', 'Won the Pulitzer Prize for Drama in 1993.'],
['The Piano Lesson', 'August Wilson', '1987', 2, 'drama', 'Pittsburgh, 1936', 'Siblings fight over selling the family piano carved with their enslaved ancestors\u2019 faces.', 'heritage; family', 'Won the Pulitzer Prize for Drama in 1990.'],
['Ma Rainey\u2019s Black Bottom', 'August Wilson', '1984', 2, 'drama', 'Chicago, 1927', 'A blues recording session exposes exploitation and rage.', 'race; exploitation; art', 'The first-produced play of Wilson\u2019s Century Cycle.'],
['Topdog/Underdog', 'Suzan-Lori Parks', '2001', 2, 'drama', 'A rooming house', 'Two brothers named Lincoln and Booth hustle three-card monte toward tragedy.', 'brotherhood; history; fate', 'Won the Pulitzer Prize for Drama in 2002.'],
['Doubt: A Parable', 'John Patrick Shanley', '2004', 1, 'drama', 'A Bronx Catholic school, 1964', 'A nun accuses a priest of misconduct with no proof but her certainty.', 'certainty; morality', 'Won the Pulitzer Prize for Drama in 2005.'],
['Proof', 'David Auburn', '2000', 2, 'drama', 'Chicago', 'A mathematician\u2019s daughter must prove she \u2014 not her father \u2014 wrote a brilliant proof.', 'genius; trust; mental illness', 'Won the Pulitzer Prize for Drama in 2001.'],
['Rabbit Hole', 'David Lindsay-Abaire', '2006', 5, 'drama', 'Suburban New York', 'A couple grieves the accidental death of their young son.', 'grief; healing', 'Won the Pulitzer Prize for Drama in 2007.'],
['Clybourne Park', 'Bruce Norris', '2010', 2, 'comedy/drama', 'Chicago, 1959 and 2009', 'A response to A Raisin in the Sun: the same house, fifty years apart, race and gentrification reversed.', 'race; gentrification', 'Won the Pulitzer Prize for Drama in 2011.'],
['Sweat', 'Lynn Nottage', '2015', 2, 'drama', 'Reading, Pennsylvania', 'Factory friends fracture along racial lines as the plant closes.', 'labor; race; deindustrialization', 'Won the Pulitzer Prize for Drama in 2017.'],
['Fairview', 'Jackie Sibblies Drury', '2018', 3, 'drama', 'A middle-class home', 'A Black family\u2019s sitcom is watched \u2014 and invaded \u2014 by white spectators.', 'race; spectatorship', 'Won the Pulitzer Prize for Drama in 2019.'],
['A Strange Loop', 'Michael R. Jackson', '2019', 2, 'musical', 'New York', 'A Black queer musical-theater writer writes a musical about writing this musical.', 'identity; art; self', 'Won the Pulitzer Prize for Drama in 2020.'],
['Fat Ham', 'James Ijames', '2022', 2, 'comedy', 'A Southern backyard barbecue', 'A queer Black Hamlet reimagined at a cookout.', 'family; identity; joy', 'Won the Pulitzer Prize for Drama in 2022.'],
['English', 'Sanaz Toossi', '2022', 3, 'drama', 'An English classroom in Iran', 'Adult students in Karaj, Iran, prepare for an English-proficiency exam.', 'language; identity', 'Won the Pulitzer Prize for Drama in 2023.'],
['Primary Trust', 'Eboni Booth', '2023', 2, 'drama', 'A small town', 'A gentle bank teller\u2019s quiet life is upended when he loses his job.', 'kindness; community', 'Won the Pulitzer Prize for Drama in 2024.'],
['Driving Miss Daisy', 'Alfred Uhry', '1987', 3, 'drama', 'Atlanta, 1948\u20131973', 'A Jewish widow and her Black chauffeur build a 25-year friendship.', 'race; friendship; aging', 'Won the Pulitzer Prize for Drama in 1988.'],
['The Heidi Chronicles', 'Wendy Wasserstein', '1988', 2, 'comedy/drama', '1960s\u20131980s America', 'Art historian Heidi Holland navigates feminism from protest to professional life.', 'feminism; friendship', 'Won the Pulitzer Prize for Drama in 1989.'],
['Lost in Yonkers', 'Neil Simon', '1991', 2, 'comedy/drama', 'Yonkers, 1942', 'Two boys left with their harsh grandmother and gentle aunt survive a wartime year.', 'family; resilience', 'Won the Pulitzer Prize for Drama in 1991.'],
['Three Tall Women', 'Edward Albee', '1991', 2, 'drama', 'A bedroom', 'Three women \u2014 one woman at three ages \u2014 confront a life.', 'aging; memory', 'Won the Pulitzer Prize for Drama in 1994.'],
['Dinner with Friends', 'Donald Margulies', '1998', 2, 'drama', 'Connecticut', 'Two couples\u2019 friendship cracks when one pair divorces.', 'marriage; friendship', 'Won the Pulitzer Prize for Drama in 2000.'],
['Wit', 'Margaret Edson', '1995', 1, 'drama', 'A hospital', 'A Donne scholar dying of ovarian cancer examines her life with wit.', 'mortality; intellect; compassion', 'Won the Pulitzer Prize for Drama in 1999.'],
['Anna in the Tropics', 'Nilo Cruz', '2002', 2, 'drama', 'A Tampa cigar factory, 1929', 'A lector reads Anna Karenina to cigar rollers; passion ignites.', 'desire; tradition', 'Won the Pulitzer Prize for Drama in 2003.'],
['I Am My Own Wife', 'Doug Wright', '2003', 1, 'drama', 'East Berlin', 'One actor plays Charlotte von Mahlsdorf and thirty others in her true story of survival.', 'identity; survival', 'Won the Pulitzer Prize for Drama in 2004.'],
['Disgraced', 'Ayad Akhtar', '2012', 1, 'drama', 'New York', 'A Muslim-American lawyer\u2019s dinner party explodes into confrontation about identity.', 'identity; Islamophobia', 'Won the Pulitzer Prize for Drama in 2013.'],
['The Flick', 'Annie Baker', '2013', 3, 'drama', 'A run-down Massachusetts cinema', 'Three underpaid ushers mop floors and dream through long silences.', 'work; longing; attention', 'Won the Pulitzer Prize for Drama in 2014.'],
['The Humans', 'Stephen Karam', '2014', 2, 'drama', 'A Chinatown apartment', 'A family Thanksgiving curdles with money fears, illness, and strange noises.', 'family; anxiety', 'Won the Pulitzer Prize for Drama in 2016.'],
['A Moon for the Misbegotten', 'Eugene O\u2019Neill', '1957', 4, 'drama', 'A Connecticut farm, 1923', 'A boozy farmer and a farm girl confess their shames in one moonlit night.', 'forgiveness; love', 'A sequel in spirit to A Touch of the Poet.'],
['The Diary of Anne Frank', 'Frances Goodrich', '1955', 2, 'drama', 'Amsterdam, 1942\u20131944', 'Anne Frank\u2019s diary dramatized: a family hides from the Nazis in a secret annex.', 'hope; persecution', 'Won the Pulitzer Prize for Drama in 1956; book by Goodrich and Albert Hackett.'],
['Inherit the Wind', 'Jerome Lawrence', '1955', 3, 'drama', 'A Southern town', 'A teacher is tried for teaching evolution in a fictionalized Scopes trial.', 'science; freedom of thought', 'Book by Lawrence and Robert E. Lee.']
];

/* Playwrights: [name, born, nationality, era, style, notable_works, note] */
var REAL_PLAYWRIGHTS = [
['William Shakespeare', '1564', 'English', 'Elizabethan/Jacobean', 'Blank verse, soliloquy, vast character range across tragedy, comedy, and history', 'Hamlet; Macbeth; A Midsummer Night\u2019s Dream; The Tempest', 'Born in Stratford-upon-Avon; died 1616; 37 plays attributed.'],
['Tennessee Williams', '1911', 'American', '20th century', 'Poetic Southern realism, memory plays, fragile outsiders', 'A Streetcar Named Desire; The Glass Menagerie; Cat on a Hot Tin Roof', 'Born Thomas Lanier Williams; died 1983; two Pulitzer Prizes.'],
['Arthur Miller', '1915', 'American', '20th century', 'Moral realism, the common man as tragic hero, social conscience', 'Death of a Salesman; The Crucible; All My Sons', 'Died 2005; testified before the House Un-American Activities Committee.'],
['Samuel Beckett', '1906', 'Irish', '20th century', 'Minimalism, absurdism, silence and repetition as meaning', 'Waiting for Godot; Endgame; Krapp\u2019s Last Tape', 'Died 1989; Nobel Prize in Literature 1969.'],
['Eugene O\u2019Neill', '1888', 'American', '20th century', 'Autobiographical naturalism and expressionism; long, confessional dramas', 'Long Day\u2019s Journey Into Night; The Iceman Cometh; A Moon for the Misbegotten', 'Died 1953; four Pulitzer Prizes; Nobel Prize in Literature 1936.'],
['Lorraine Hansberry', '1930', 'American', '20th century', 'Social realism centered on Black family life and dignity', 'A Raisin in the Sun; The Sign in Sidney Brustein\u2019s Window', 'Died 1965 at 34; first Black woman with a play on Broadway.'],
['Edward Albee', '1928', 'American', '20th century', 'Brutal domestic realism mixed with absurdism', 'Who\u2019s Afraid of Virginia Woolf?; The Zoo Story; Three Tall Women', 'Died 2016; three Pulitzer Prizes for Drama.'],
['August Wilson', '1945', 'American', '20th century', 'Epic realism; the Century Cycle of ten plays on Black life', 'Fences; The Piano Lesson; Ma Rainey\u2019s Black Bottom', 'Died 2005; two Pulitzer Prizes; ten-play Century Cycle, one per decade of the 1900s.'],
['Oscar Wilde', '1854', 'Irish', 'Victorian', 'Epigrammatic comedy of manners; wit as weapon', 'The Importance of Being Earnest; An Ideal Husband; Lady Windermere\u2019s Fan', 'Died 1900; also famed for The Picture of Dorian Gray.'],
['Henrik Ibsen', '1828', 'Norwegian', '19th century', 'Realism and social-problem drama; the \u201cfather of modern drama\u201d', 'A Doll\u2019s House; Hedda Gabler; Ghosts; An Enemy of the People', 'Died 1906; his plays scandalized Europe with frank social critique.'],
['Anton Chekhov', '1860', 'Russian', '19th/20th century', 'Subtext, atmosphere, and inaction; comedy of wasted lives', 'The Cherry Orchard; Three Sisters; Uncle Vanya; The Seagull', 'Died 1904; also a master of the short story and a physician.'],
['Sophocles', 'c. 497 BC', 'Greek', 'Classical Athens', 'Tragic irony; added the third actor to Greek tragedy', 'Oedipus Rex; Antigone; Electra', 'Died c. 406 BC; won at least 18 Dionysia festivals.'],
['Euripides', 'c. 480 BC', 'Greek', 'Classical Athens', 'Psychological realism; sympathetic, complex women', 'Medea; The Bacchae; Electra; Hippolytus', 'Died c. 406 BC; the most modern-seeming of the Greek tragedians.'],
['Aristophanes', 'c. 446 BC', 'Greek', 'Classical Athens', 'Old Comedy: political satire, fantasy, bawdy choruses', 'Lysistrata; The Clouds; The Frogs', 'Died c. 386 BC; the only Old Comedy playwright with surviving complete plays.'],
['Moli\u00e8re', '1622', 'French', '17th century', 'Verse comedy of manners exposing hypocrisy', 'Tartuffe; The Misanthrope; The Miser', 'Born Jean-Baptiste Poquelin; died 1673, collapsing on stage during The Imaginary Invalid.'],
['Edmond Rostand', '1868', 'French', '19th/20th century', 'Romantic verse drama; panache and heroism', 'Cyrano de Bergerac; L\u2019Aiglon', 'Died 1918; Cyrano\u2019s 1897 premiere was a legendary triumph.'],
['Bertolt Brecht', '1898', 'German', '20th century', 'Epic theatre; the alienation effect (Verfremdungseffekt)', 'Mother Courage; The Good Person of Szechwan; The Threepenny Opera', 'Died 1956; co-founded the Berliner Ensemble.'],
['Tom Stoppard', '1937', 'British', '20th/21st century', 'Witty, philosophical comedy; wordplay as ideas', 'Rosencrantz and Guildenstern Are Dead; Arcadia; The Coast of Utopia', 'Born in Czechoslovakia; master of the intellectual comedy.'],
['Harold Pinter', '1930', 'British', '20th century', '\u201cComedy of menace\u201d; pauses and subtext as threat', 'The Birthday Party; Betrayal; The Homecoming', 'Died 2008; Nobel Prize in Literature 2005.'],
['David Mamet', '1947', 'American', '20th/21st century', 'Staccato, profane dialogue; con games and power', 'Glengarry Glen Ross; American Buffalo; Oleanna', 'Also a noted film director and screenwriter.'],
['Sam Shepard', '1943', 'American', '20th century', 'Mythic American West; fractured families', 'True West; Buried Child; Fool for Love', 'Died 2017; also a celebrated film actor.'],
['Tony Kushner', '1956', 'American', '20th/21st century', 'Epic, politically charged fantasia', 'Angels in America; Caroline, or Change', 'Pulitzer Prize for Drama 1993.'],
['Suzan-Lori Parks', '1963', 'American', '20th/21st century', 'Lyrical, musical language; history remixed', 'Topdog/Underdog; The America Play', 'First Black woman to win the Pulitzer for Drama (2002).'],
['Thornton Wilder', '1897', 'American', '20th century', 'Minimal staging; universal human themes', 'Our Town; The Skin of Our Teeth', 'Died 1975; three Pulitzer Prizes across categories.'],
['Neil Simon', '1927', 'American', '20th century', 'Joke-dense commercial comedy with heart', 'Lost in Yonkers; The Odd Couple; Brighton Beach Memoirs', 'Died 2018; one of Broadway\u2019s most produced playwrights.'],
['Wendy Wasserstein', '1950', 'American', '20th century', 'Feminist comedy of manners', 'The Heidi Chronicles; The Sisters Rosensweig', 'Died 2006; first solo woman to win the Tony for Best Play.'],
['Stephen Sondheim', '1930', 'American', '20th/21st century', 'Composer-lyricist of complex, literate musicals', 'Sweeney Todd; Into the Woods; Sunday in the Park with George', 'Died 2021; the dominant figure of the modern musical.'],
['Lin-Manuel Miranda', '1980', 'American', '21st century', 'Hip-hop and musical-theater fusion; American history retold', 'Hamilton; In the Heights', 'Pulitzer Prize for Drama 2016; MacArthur Fellow.'],
['Andrew Lloyd Webber', '1948', 'British', '20th/21st century', 'Melodic mega-musicals; sung-through scores', 'The Phantom of the Opera; Cats; Jesus Christ Superstar', 'The Phantom of the Opera is Broadway\u2019s longest-running show.'],
['Eug\u00e8ne Ionesco', '1909', 'Romanian-French', '20th century', 'Theatre of the Absurd; language breaking down', 'The Bald Soprano; Rhinoceros; The Chairs', 'Died 1994; a founder of absurdist theater.'],
['George Bernard Shaw', '1856', 'Irish', '19th/20th century', 'Comedy of ideas; long debate-driven plays', 'Pygmalion; Saint Joan; Major Barbara', 'Died 1950; Nobel Prize in Literature 1925.'],
['Lynn Nottage', '1964', 'American', '21st century', 'Research-driven social realism', 'Sweat; Ruined; Intimate Apparel', 'First woman to win two Pulitzer Prizes for Drama.'],
['Annie Baker', '1981', 'American', '21st century', 'Hyper-naturalism; long silences; ordinary life in close-up', 'The Flick; The Antipodes', 'Pulitzer Prize for Drama 2014.'],
['Branden Jacobs-Jenkins', '1984', 'American', '21st century', 'Adaptations that interrogate classics and race', 'An Octoroon; Appropriate; Purpose', 'Pulitzer Prize for Drama 2025 for Purpose.'],
['Eboni Booth', 'living', 'American', '21st century', 'Tender, humane character drama', 'Primary Trust', 'Pulitzer Prize for Drama 2024.']
];
/* Theatrical forms: [name, origin, characteristics, description] */
var REAL_FORMS = [
['Tragedy', 'Ancient Greece (5th century BC)', 'Serious tone; a noble protagonist undone by flaw or fate; catharsis', 'Tragedy grew from Athenian religious festivals honoring Dionysus. Aristotle defined it as the imitation of a serious action evoking pity and fear, purged through catharsis. Its arc runs from Shakespeare to Miller\u2019s insistence that the common man can be tragic.'],
['Comedy', 'Ancient Greece; Old Comedy of Aristophanes', 'Humor, happy endings, satire of folly; recognition and reunion', 'Comedy began as ribald civic satire and evolved through Roman farce, commedia dell\u2019art\u0435, Moli\u00e8re\u2019s manners, and modern sitcom structure. Its engine is incongruity: the gap between expectation and result, resolved in laughter.'],
['Farce', 'Ancient Rome; popularized in 19th-century France', 'Slapstick, mistaken identity, slamming doors, breakneck pace', 'Farce is comedy pushed to physical extremes: Georges Feydeau\u2019s bedroom farces set the template of escalating misunderstandings timed like music. The rule is momentum \u2014 never let the audience think.'],
['Melodrama', '19th-century Europe', 'Clear heroes and villains, sensational plot, music underscoring emotion', 'Melodrama \u2014 literally \u201cmusic drama\u201d \u2014 gave the 1800s its cliffhangers, orphans, and mustache-twirling villains. Its moral clarity and spectacle fed directly into film and television serials.'],
['Musical theater', 'United States, 19th\u201320th century', 'Story told through song, dance, and book scenes', 'From minstrelsy and operetta through Show Boat (1927), Oklahoma! (1943), and the rock and hip-hop musicals, the musical fuses popular music with narrative. Its golden rule: characters sing when words alone can no longer carry feeling.'],
['Opera', 'Italy, c. 1600', 'Fully sung drama with orchestra; arias, recitative, chorus', 'Born in Florentine salons around 1600, opera became the grandest stage form: Monteverdi, Mozart, Verdi, Wagner, and Puccini built a repertoire still performed worldwide. Subforms include opera buffa, grand opera, and music drama.'],
['Kabuki', 'Japan, early 17th century', 'Stylized dance-drama; elaborate makeup (kumadori), revolving stages, onnagata', 'Kabuki began with the dancer Okuni and grew into spectacular popular theater with mie poses, hanamichi runways, and stage tricks. It is UNESCO-recognized intangible heritage.'],
['Noh theater', 'Japan, 14th century', 'Masked, slow, poetic dance-drama; chorus and minimal staging', 'Perfected by Zeami, Noh compresses legend into dreamlike ritual: masked shite actors, a pine-painted backdrop, and flute-and-drum music. It values suggestion over depiction.'],
['Commedia dell\u2019arte', 'Italy, 16th century', 'Masked stock characters; improvisation around scenarios; lazzi', 'Traveling troupes improvised comic plots from outline scenarios using fixed masks \u2014 Harlequin, Pantalone, Columbine. Its physical comedy and timing shaped Moli\u00e8re, vaudeville, and sitcom.'],
['Epic theatre', 'Germany, 1920s (Brecht)', 'Narration, placards, songs that interrupt; the alienation effect', 'Brecht\u2019s epic theatre refuses emotional hypnosis: actors demonstrate characters, placards announce scenes, and songs comment on action, so audiences think critically instead of merely feeling.'],
['Theatre of the Absurd', 'France, 1950s', 'Illogical plots, circular dialogue, meaning through meaninglessness', 'Named by Martin Esslin, the Absurd \u2014 Beckett, Ionesco, Genet \u2014 stages a universe without inherent purpose. Waiting becomes the plot; language misfires; laughter curdles into dread.'],
['Realism', 'Europe, late 19th century', 'Fourth wall, everyday speech, psychologically consistent characters', 'Ibsen, Chekhov, and Stanislavski\u2019s Moscow Art Theatre made the stage a slice of life: box sets, subtext, and behavior observed like science. It remains the default grammar of film and TV acting.'],
['Naturalism', 'France, late 19th century (Zola; Antoine)', 'Extreme realism; environment determines character; slice-of-life detail', 'Zola\u2019s naturalism pushed realism further: heredity and environment as fate, staged with documentary detail. Antoine\u2019s Th\u00e9\u00e2tre-Libre hung real carcasses in a butcher-shop set.'],
['Expressionism', 'Germany, 1910s\u201320s', 'Distorted sets, heightened emotion, dream logic', 'Expressionist theater externalizes inner states: tilted staircases, harsh light, masked crowds. Strindberg\u2019s dream plays and early O\u2019Neill carry its DNA into film noir lighting.'],
['Improvisational theater', 'Modern; roots in commedia and Viola Spolin\u2019s games', 'Unscripted scenes built from audience suggestions', 'Spolin\u2019s theater games trained actors to build scenes on the spot; Chicago\u2019s Compass and Second City turned improv into comedy institutions and the training ground of American comedy.'],
['Immersive theater', 'Contemporary', 'Audience moves through the performance space; no fixed seats', 'Immersive work \u2014 from Punchdrunk\u2019s Sleep No More onward \u2014 turns spectators into explorers of a staged world, choosing their own path through simultaneous scenes.'],
['Verbatim theater', 'Contemporary documentary theater', 'Scripts built word-for-word from interviews and records', 'Verbatim (documentary) theater stages real testimony \u2014 trials, inquiries, oral histories \u2014 edited but not rewritten, as in The Laramie Project tradition.'],
['Puppetry', 'Worldwide; ancient', 'Stories told through manipulated figures: hand, rod, shadow, bunraku', 'From Indonesian wayang shadow plays to Japanese bunraku (three puppeteers per figure) to Handspring\u2019s War Horse, puppetry makes the inanimate breathe and is among the oldest stage arts.'],
['Mime', 'Ancient Greece and Rome; revived in 19th\u201320th-century France', 'Story told without words through gesture and illusion', '\u00c9tienne Decroux and Marcel Marceau refined mime into corporeal art: invisible walls, walks against wind, whole worlds drawn in air. It trains every actor\u2019s body.'],
['Vaudeville', 'United States, late 19th\u2013early 20th century', 'Variety bills: songs, comedy, magic, acrobatics', 'Vaudeville\u2019s circuits carried thousands of acts across America; its timing, heckler-handling, and bill structure became the DNA of radio, TV variety, and stand-up.'],
['Pantomime', 'Britain (holiday tradition)', 'Family musical comedy with cross-dressing dame, audience call-and-response', 'British panto turns fairy tales into Christmas-season romps: the dame, the principal boy, \u201che\u2019s behind you!\u201d Its audience participation is ritual.'],
['Bunraku', 'Japan, 17th century', 'Large puppets (half to two-thirds life-size), chanter and shamisen', 'Bunraku\u2019s near-life-size puppets need three black-clad operators each, while a chanter voices all roles beside a shamisen player. Chikamatsu wrote its greatest plays.'],
['Shadow play', 'Asia; ancient (China, Indonesia, Turkey)', 'Silhouettes cast on a screen tell myths and epics', 'Wayang kulit shadow puppetry can run all night, one dalang voicing dozens of characters behind a lit screen \u2014 cinema before cinema.'],
['Physical theater', '20th century (Grotowski, Lecoq, Complicite)', 'The actor\u2019s body as the primary storytelling instrument', 'Physical theater strips away sets and text to what bodies can do: Grotowski\u2019s poor theater, Lecoq\u2019s movement pedagogy, and companies like Complicite build worlds from ensemble motion.'],
['Forum theater', 'Brazil, 1970s (Augusto Boal)', 'Spect-actors stop oppression scenes and replay them with solutions', 'Boal\u2019s Theatre of the Oppressed turns audiences into rehearsers of revolution: anyone may shout \u201cstop,\u201d take a role, and try a different outcome.'],
['Site-specific theater', 'Contemporary', 'Performed in non-theater locations that shape the story', 'Warehouses, forests, moving buses: site-specific work lets architecture co-author the play, as audiences encounter story where life actually happens.'],
['Reader\u2019s theater', 'Mid-20th century', 'Scripts read aloud with minimal staging; voice and text carry all', 'Actors with scripts in hand, no blocking, no costumes \u2014 reader\u2019s theater proves story lives in voice and language, and doubles as a literacy tool.'],
['Radio drama / audio theater', '1920s onward', 'Plays written for sound only; foley and voice build the world', 'From Orson Welles\u2019s 1938 War of the Worlds broadcast to modern fiction podcasts, audio drama paints sets in the listener\u2019s mind with voice, music, and effects.'],
['Devised theater', 'Contemporary ensemble practice', 'The company creates the play collaboratively, without a starting script', 'Devising builds productions from improvisation, research, and image: the ensemble is the author. It dominates experimental and youth theater.'],
['Burlesque (stage)', '19th century; American revival', 'Parody, variety, and striptease as theatrical art', 'Stage burlesque mixed satire, song, and striptease; its modern neo-burlesque revival reclaims it as body-positive performance art.'],
['Operetta', '19th-century France and Vienna', 'Light opera: spoken dialogue plus songs, romance and comedy', 'Offenbach\u2019s Parisian spoofs and Leh\u00e1r\u2019s Viennese waltz romances made operetta the champagne of 19th-century theater, bridging opera and musical.'],
['Morality play', 'Medieval Europe', 'Allegorical characters teach moral lessons', 'Everyman\u2019s journey to death with Good Deeds alone beside him: morality plays allegorized the soul\u2019s choices for medieval audiences.'],
['Miracle/mystery plays', 'Medieval Europe', 'Biblical stories staged by guilds on pageant wagons', 'Craft guilds staged the Bible from Creation to Doomsday on rolling wagons \u2014 the shipwrights built the Ark \u2014 turning whole towns into theaters.']
];
/* Stagecraft: [topic, area, key_points, procedure] */
var REAL_STAGECRAFT = [
['Stage lighting basics', 'lighting', 'Visibility, mood, focus, and composition are light\u2019s four jobs; instruments include ellipsoidals, Fresnels, PARs, and followspots; color comes from gels and LEDs', 'Hang and focus: position instruments on battens and front-of-house bars, then shape each beam with shutters and focus so edges land where the plot demands. Gel and balance: choose color, check skin tones under the mix, and balance intensities so faces read at the back row. Cue the show: program fades and bumps into the board, then the operator or stage manager calls every change.'],
['The lighting design process', 'lighting', 'Script analysis, research images, the light plot, and cueing build a design', 'Read for light: mark every time-of-day, weather, and emotional shift the script implies. Research and palette: collect images and choose a color world. Draft the plot: place each instrument on the groundplan with channel, color, and purpose. Tech and refine: focus, write cues with the director, and shape the show across technical rehearsals.'],
['Sound design for theater', 'sound', 'Reinforcement, effects, and music; speakers placed for coverage without feedback', 'Script the sound: list every cue \u2014 doorbell, storm, underscoring \u2014 with timing. Build or source: record, license, or synthesize each effect. Place the system: aim speakers for even coverage and ring out feedback. Mix live: ride levels through rehearsal until effects sit inside the acting.'],
['Scenic (set) design', 'scenery', 'The groundplan, elevations, and models translate story into space', 'Analyze the action: list every location, entrance, and furniture need. Sketch and model: develop thumbnails into a scale white model. Draft: produce groundplans and elevations the shop can build from. Dress and paint: add props, textures, and scenic painting, then tech the transitions.'],
['Costume design', 'costumes', 'Character, period, and movement; pulled, built, or rented stock', 'Read for character: chart each role\u2019s arc, status, and changes. Research the world: period silhouettes, fabrics, and social codes. Render and source: sketch designs, then pull, rent, or build each piece. Fit and tech: alter through fittings and organize quick changes backstage.'],
['Stage management and the prompt book', 'management', 'The stage manager runs rehearsals and calls every cue in performance', 'Prep the book: build the prompt script with blocking, cues, and contact sheets. Run the room: schedule rehearsals, take blocking notes, and keep the company informed. Call the show: from tech onward, call every light, sound, and fly cue over headset. Hold the standard: maintain the director\u2019s intent and write the nightly report.'],
['Calling cues', 'management', 'Standby, warning, and \u201cgo\u201d keep operators synchronized', 'Standby the sequence: warn each operator a page before their cue. Call warnings: give a heads-up as the moment approaches. Call the go: speak each cue crisply on the exact beat. Confirm execution: watch that every cue lands, and log misses for notes.'],
['The fly system and rigging', 'rigging', 'Counterweight arbors balance battens; safety is the whole job', 'Inspect before use: check ropes, arbors, and locks every load-in. Load the arbor: balance pipe weight with counterweight so the batten floats. Brief the crew: assign rails, confirm spike marks and cue order. Fly the show: move battens only on cue, with a spotter watching the deck.'],
['Stage directions', 'fundamentals', 'Upstage, downstage, stage left and right are named from the actor\u2019s view facing the audience', 'Face the house: stand as the actor does, facing the audience. Name the zones: upstage is away from the audience, downstage toward it; stage left and right are the actor\u2019s own. Block with them: give every cross and position in these terms so the whole company shares one map.'],
['Types of stages', 'fundamentals', 'Proscenium, thrust, arena, black box, and traverse shape actor-audience contact', 'Read the room: note where the audience sits relative to the playing space. Choose the relationship: proscenium frames like a picture, thrust and arena surround, black box adapts. Block for sightlines: keep key action open to the most seats. Design accordingly: scenery and lighting follow the architecture.'],
['Blocking a scene', 'directing', 'Movement must be motivated, visible, and repeatable', 'Find the beats: break the scene into units of changing intention. Motivate the moves: every cross needs a reason \u2014 to confront, to escape, to reveal. Fix the traffic: set crosses so sightlines stay clean and actors never collide. Lock and record: the stage manager notes every move in the prompt book.'],
['The rehearsal process', 'management', 'Table work, blocking, runs, tech, and dress build a production in order', 'Table work: read and analyze the script together before standing. Block: set movement scene by scene. Run and refine: run acts, then full runs, polishing pace. Tech and dress: add lights, sound, costumes, and orchestra; open only when the machine runs clean.'],
['Cue-to-cue (tech rehearsal)', 'management', 'Tech skips dialogue to set every light, sound, and fly cue', 'Walk the cues: play only the moments around each technical change. Set levels: the designers adjust intensity, timing, and balance. Mark trouble: note every late or wrong cue. Run clean: finish with a full run once cues are set.'],
['The fourth wall', 'fundamentals', 'The imaginary barrier between actors and audience in realism', 'Build the room: stage the world as if the audience were not there. Keep the wall: actors do not acknowledge the house except in asides or direct address. Break it deliberately: when the play demands, breaking the wall shocks precisely because it was whole.'],
['Theater masking', 'scenery', 'Legs, borders, and teasers hide the mechanics backstage', 'Mask the wings: hang legs to hide entrances and waiting actors. Mask the top: borders hide battens and borders of light. Keep the illusion: no hardware the audience should not see stays visible.'],
['Color in stage lighting', 'lighting', 'Gels and LEDs mix color; warm vs cool shapes mood and skin tone', 'Choose the palette: assign warm and cool systems per the design. Check faces: test every mix on skin under stage conditions. Layer the color: build depth by crossing warm and cool from different angles.'],
['Followspot operation', 'lighting', 'The operator tracks performers with a manual spotlight', 'Learn the pickup: know exactly where and when each performer enters the beam. Track smoothly: follow with the whole body, keeping the head framed. Size and color: adjust iris and drop color frames on cue. Douse cleanly: fade or snap out exactly on the call.'],
['Props: hand, set, and personal', 'props', 'Every object an actor touches is tracked, preset, and maintained', 'List every prop: break the script into hand, set, and personal props. Source or build: find, rent, or construct each item. Preset nightly: place every prop before half-hour and check it. Strike and reset: collect, repair, and re-preset after each show.'],
['Scenic painting', 'scenery', 'Paint turns lumber and muslin into marble, wood, and sky', 'Prime the surface: seal flats and drops for even paint. Lay the base: roll the ground color. Add texture: sponge, rag, and dry-brush grain, stone, or foliage. Detail and seal: paint trim and shadows, then protect high-touch areas.'],
['Stage makeup basics', 'costumes', 'Makeup restores the face that distance and light wash away', 'Prep the skin: clean and moisturize. Build the base: match and blend foundation to the neck. Define features: strengthen brows, eyes, and lips for distance. Set it: powder and seal so it survives sweat and lights.'],
['Wigs and hair for the stage', 'costumes', 'Wigs change age, period, and character at a stroke', 'Choose the style: match period and character to the design. Fit and pin: secure the wig so it survives quick changes and fights. Style for distance: build shape that reads from the back row. Maintain: wash, reset, and repair on schedule.'],
['The green room and backstage etiquette', 'management', 'Quiet, courtesy, and readiness keep a company working', 'Keep it quiet: the green room rests voices and nerves \u2014 no drama offstage. Respect the space: clean up, share mirrors, guard others\u2019 presets. Stay ready: listen for calls and be in place before your cue.'],
['Front of house', 'management', 'Ushers, box office, and house management shape the audience\u2019s night', 'Open the house: check seats, programs, and sightlines before doors. Seat with care: usher latecomers at safe moments. Mind the house: handle emergencies, disruptions, and accessibility needs. Close out: count, report, and reset for tomorrow.'],
['Theater safety: weapons and fights', 'safety', 'Every blade is dull, every fight choreographed and rehearsed', 'Choreograph with a fight director: no actor invents combat. Rehearse at speed gradually: slow, then half, then full \u2014 never cold. Check weapons: inspect every blade and firearm before each show. Call the hold: anyone may stop a fight that feels wrong.'],
['Stage combat basics', 'safety', 'Illusion of violence with zero contact: distance, angles, and sound', 'Learn the techniques: slaps, punches, and falls built on distance and angle. Sell the reaction: the victim\u2019s timing makes the hit. Add the knap: a handclap hidden in the move supplies the crack. Rehearse every performance: fights are called before each show.'],
['The grid and catwalks', 'rigging', 'The grid above the stage holds the whole hanging plot', 'Know the load paths: every batten, electric, and scenic piece hangs from rated points. Respect limits: never exceed a batten\u2019s or point\u2019s rating. Move safely: catwalks demand harnesses where required and three points of contact. Inspect: check motors, cables, and shackles on schedule.'],
['Dimmers and control', 'lighting', 'Dimmers vary voltage to instruments; the console runs the show', 'Patch the rig: assign every dimmer to a channel on the console. Build the cues: set levels, fade times, and follows. Back up the show: save to multiple media and print the magic sheet. Run with a spare: keep a backup plan for board failure.'],
['The house: seating and sightlines', 'fundamentals', 'Every seat should see and hear; the house shapes the design', 'Map the sightlines: check the stage from the worst seats. Rake and stagger: slope the floor or offset rows so heads do not block. Mind the sound: balance the system for the back row without blasting the front. Keep egress clear: aisles and exits stay open always.'],
['Quick changes', 'costumes', 'Costumes engineered to change in seconds in the wings', 'Design for speed: magnets, Velcro, and breakaway seams replace buttons. Rehearse the change: dressers and actors drill it like choreography. Preset in order: lay each layer in reverse so the next piece is on top. Cover the actor: screens and robes preserve modesty in the wings.'],
['The tech table', 'management', 'Directors and designers watch tech from mid-house with scripts and scores', 'Set the table: place it center-house with headsets, scripts, and the prompt book. Communicate: the stage manager relays notes to every department. Track the fixes: each note gets an owner and a deadline. Clear before opening: strike the table for audiences.']
];

/* ================= Signature-generation pools ================= */
var FN = ['Aldous','Maren','Caspian','Ilsa','Dorian','Sable','Emrys','Vesper','Corvin','Liora','Jasper','Odette','Rurik','Sanne','Theron','Isolde','Bram','Celia','Dain','Elowen','Fenwick','Greta','Halloran','Imogen','Joren','Kestrel','Lavinia','Merrick','Nadia','Orson','Petra','Quill','Rowan','Sorrel','Tamsin','Ulric','Veda','Wren','Xavier','Ysolde','Zephyr','Ansel','Briony','Cato','Delphine','Evander','Fiona','Gideon','Hazel','Ivan','Juniper','Klaus','Lena','Milo','Nessa','Otto','Pippa','Ramon','Suki','Tilda','Vera'];
var LN = ['Blackwood','Fairlight','Grimaldi','Holloway','Ironhart','Kestrel','Larkspur','Marlowe','Nightingale','Osric','Pemberton','Quillfeather','Ravenscar','Stonebridge','Thistledown','Underbough','Vane','Winterbourne','Ashcroft','Bellamy','Corvane','Duskfall','Elmsworth','Frostwick','Galloway','Harlowe','Inkwell','Juniper','Kingsolver','Lockhart','Moonfall','Northgate','Oakenshield','Pryce','Redfern','Sallow','Torrance','Umber','Vexley','Whitlock','Yardley','Zephyr'];
var NATIONALITIES = ['American','British','Irish','French','German','Nigerian','Indian','Japanese','Brazilian','Canadian','Australian','South African','Mexican','Spanish','Italian','Polish','Swedish','Kenyan','Egyptian','Argentinian'];
var PLAY_ADJ = ['Silent','Broken','Velvet','Iron','Paper','Midnight','Hollow','Crimson','Golden','Glass','Winter','Burning','Paper','Last','Forgotten','Hidden','Electric','Ashen','Ivory','Copper','Lonely','Radiant','Sable','Thundering','Wandering','Patient','Reckless','Gentle','Fierce','Hollow'];
var PLAY_NOUN = ['Lantern','Hour','Garden','River','Crown','Mirror','Door','Song','Harbor','Theater','Letter','Storm','Window','Bridge','Forest','Key','Bell','Compass','Anchor','Flame','Map','Clock','Mask','Star','Ship','House','Field','Moon','Road','Apple'];
var PLAY_NOUN2 = ['Kings','Sailors','Dreamers','Thieves','Widows','Cartographers','Beekeepers','Astronomers','Smugglers','Gardeners','Watchmakers','Orphans','Revolutionaries','Musicians','Archivists'];
var GENRES = ['tragedy','comedy','drama','tragicomedy','farce','melodrama','history play','musical drama'];
var SETTINGS = ['a lighthouse on a crumbling cliff','a 24-hour diner in 1987','a flooded subway station','a mountaintop observatory','a traveling circus in winter','a lighthouse keeper\u2019s cottage','an orbital relay station','a small-town courthouse','a night market in the rain','a decommissioned theater','a lighthouse','a border checkpoint','a lighthouse','a lighthouse'];
var SETTINGS2 = ['a lighthouse on a crumbling cliff','a 24-hour diner in 1987','a flooded subway station','a mountaintop observatory','a traveling circus in winter','a lighthouse keeper\u2019s cottage','an orbital relay station','a small-town courthouse','a night market in the rain','a decommissioned theater','a border checkpoint at dawn','a lighthouse','a deep-sea research vessel','a rooftop greenhouse','a lighthouse','an abandoned amusement park','a monastery library','a lighthouse','a lighthouse'];
var ROLES = ['the reluctant heir','a retired smuggler','the town archivist','a lighthouse keeper','a disgraced astronomer','the mayor\u2019s daughter','a traveling musician','the night-shift nurse','a cartographer with no map','the last lighthouse keeper','a retired detective','the beekeeper\u2019s apprentice','a radio operator','the lighthouse','a lighthouse'];
var ROLES2 = ['the reluctant heir','a retired smuggler','the town archivist','a lighthouse keeper','a disgraced astronomer','the mayor\u2019s daughter','a traveling musician','the night-shift nurse','a cartographer with no map','a retired detective','the beekeeper\u2019s apprentice','a radio operator','a lighthouse engineer','a lighthouse'];
var THEMES = ['memory and forgetting','the price of ambition','forgiveness','home and exile','truth vs comfort','generational debt','the sea as fate','machines and souls','what we owe the dead','the courage to start over','silence as resistance','maps vs territory','inheritance','second chances','the cost of secrets'];
var VENUES = ['the Meridian Playhouse','the Gaslight Theater','the Old Foundry Stage','the Harborlight Theater','the Copper Lantern','the Ivory Tower Playhouse','the Blackbird Theater','the Starling Stage','the Ember House','the Foxglove Theater','the Wren\u2019s Nest','the Tidal Hall'];
var CITIES = ['Portland','Chicago','London','Dublin','Toronto','Melbourne','Lagos','Mumbai','New Orleans','Seattle','Glasgow','Cape Town'];
var ERAS = ['contemporary','mid-20th century','Victorian','post-war','the near future','the 1920s','the 1970s'];
var FORM_CONCEPTS = [
['Holographic theater','Experimental stages project volumetric performers alongside live actors','Volumetric capture; live compositing; latency under 40ms; the audience wears no headsets \u2014 the holograms share the air','A form for impossible casts: the dead, the distant, and the imaginary perform beside the living.'],
['Drone ballet','Choreographed drone swarms as an aerial corps de ballet','Swarm programming; failsafe geofencing; music-synchronized flight; outdoor night venues','Dozens of lit drones trace formations above dancers, extending choreography into the sky.'],
['Submerged theater','Performances staged in shallow pools with the audience wading','Waterproof costuming; underwater speakers; safety divers; heated pools','Actors and audience share the water; movement slows, sound thickens, and every gesture costs effort.'],
['One-room marathon','A full season of plays performed in a single room over 24 hours','Rotating casts; sleep-shift audiences; modular set; durational dramaturgy','Endurance as aesthetic: the room accumulates the ghosts of every play performed in it.'],
['Algorithmic improv','An AI feeds prompts, twists, and blackouts to improvisers live','Prompt engine; human veto; latency-tuned delivery; the cast trains with the system','The machine proposes, the humans dispose: improv with a tireless, strange scene partner.'],
['Silent-film stage','Plays performed as living silent films with intertitles and a pit pianist','Intertitle projection; exaggerated gesture; live score; tinted lighting','Melodrama returns to its roots: no spoken words, only bodies, cards, and music.'],
['Climate theater','Outdoor plays that proceed in all weather; the forecast is the dramaturg','Weather contingency as text; audience provisioned; the storm may rewrite the ending','The sky is a cast member with top billing and no rehearsal.'],
['Micro-theater','Plays for audiences of one to six in closets, cars, and elevators','Intimate staging; the audience is a character; 15-minute arcs','Theater at whisper distance, where a glance is a special effect.'],
['Archive theater','Performances built entirely from a community\u2019s donated letters and recordings','Consent protocols; verbatim editing; the donors attend opening','A town performs its own memory back to itself.'],
['Sleep theater','Audiences doze through overnight performances designed for half-dreams','Reclined seating; hypnagogic sound design; gentle waking rituals','The play meets the audience at the edge of sleep, where images do the acting.'],
['Vertical theater','Staged on building facades with climbing performers and rigging','Industrial rigging; facade choreography; street-level audience','The city wall becomes a stage; gravity becomes the antagonist.'],
['Seed theater','A play planted like a garden: scenes grow across a season in a real plot','Horticultural dramaturgy; the set is alive; performances follow the growing season','The audience returns monthly to watch both the story and the set grow.']
];
var STAGE_TOPICS = [
['Designing a lighting plot for a thrust stage','lighting','Thrust stages surround the actor on three sides, so front light must come from multiple angles to avoid shadowing faces away from any section.','Survey the hang: map every batten and boom position around the thrust. Assign systems: build warm and cool washes that cross from opposing sides so faces read everywhere. Fill the gaps: add specials for key moments and shutter spill off the audience. Focus and cue: focus each unit to its area, then write cues that keep the whole room balanced.'],
['Sound for a musical in a small house','sound','Small rooms punish loud reinforcement; the design favors clarity over volume.','Measure the room: find its natural reverb and problem frequencies. Choose the rig: a compact PA with careful aiming beats raw power. Ring it out: notch feedback frequencies before the band arrives. Mix for the room: keep vocals above the band without drowning the space.'],
['Building a unit set on a budget','scenery','One flexible set serves every location when money is short.','Design the unit: a platform, a wall, and a door that redress into anywhere. Source cheap: pallets, paint, and borrowed furniture. Build modular: every piece must move, stack, and store. Dress with light: let lighting and props do the location work paint cannot.'],
['Costuming a period play from thrift stores','costumes','Period silhouette matters more than period fabric.','Research the silhouette: learn the shape of the era first. Hunt in layers: thrift for base garments, then alter. Cheat the details: collars, hats, and hems sell the period. Fit everyone: schedule fittings early and often.'],
['Running a backstage crew of volunteers','management','Volunteers need clarity, gratitude, and short shifts.','Recruit with specifics: name the exact jobs and hours. Train once: a single thorough walkthrough beats repeated corrections. Assign ownership: each volunteer owns one track. Thank loudly: recognition is the paycheck.'],
['Stage-managing a show with 200 cues','management','Dense cue shows demand a flawless prompt book and calm calling.','Build the book: every cue numbered, every standby marked. Rehearse the call: dry-run the densest sequences. Simplify the language: short, consistent calls under pressure. Trust the operators: clear roles, no micromanaging on headset.'],
['Rigging a chandelier practical','rigging','A flown practical must be wired, balanced, and cabled safely.','Rate the point: confirm the batten and motor can carry the load. Wire safely: cable the practical through proper strain relief. Balance the arbor: counterweight precisely. Rehearse the fly: move it at cue speed in tech.'],
['Painting a forced-perspective street','scenery','Painted perspective fakes depth on a flat drop.','Set the vanishing point: draw the geometry before touching paint. Lay the base: roll the sky and ground. Build the street: paint buildings shrinking toward the point. Add life: windows, signs, and grime sell the scale.'],
['Wig quick-change in under 90 seconds','costumes','Speed comes from preparation, not hurrying.','Prep the wig: pin and style it fully before the show. Preset the station: stand, pins, and cap in order. Drill the change: time every rehearsal. Assign a dresser: four hands beat two.'],
['Foley effects performed live','sound','Live foley puts the sound effects artist on stage with the actors.','List the effects: every footstep, door, and storm. Build the kit: coconut shells, thunder sheets, and gravel trays. Rehearse with actors: timing is choreography. Perform nightly: the foley table never misses.'],
['Masking a black-box theater','scenery','Black boxes need total flexibility in masking.','Hang the blacks: legs and borders on travelers. Create the wings: leave generous crossover space. Mask the grid: hide instruments that spill. Adapt per show: rehang the box for each production.'],
['Programming intelligent lights for a dance piece','lighting','Moving lights follow dancers if programmed musically.','Choose the fixtures: washes for color, spots for beams. Build palettes: color, position, and gobo presets. Program to the score: cues land on musical beats. Busk the rest: leave manual control for solos.']
];
function playTitle(r) {
  var k = (r() * 4) | 0;
  if (k === 0) return 'The ' + pick(PLAY_ADJ, r) + ' ' + pick(PLAY_NOUN, r);
  if (k === 1) return pick(PLAY_NOUN, r) + ' of ' + pick(PLAY_NOUN2, r);
  if (k === 2) return 'A ' + pick(PLAY_NOUN, r) + ' for ' + pick(PLAY_ADJ, r) + ' ' + pick(PLAY_NOUN2, r);
  return 'The ' + pick(PLAY_NOUN2, r) + '\u2019 ' + pick(PLAY_NOUN, r);
}
function realPlayRecord(e, id, seed) {
  var details = { playwright: e[1], premiere_year: e[2], acts: e[3], genre: e[4], setting: e[5], themes: e[7].split('; ') };
  var secs = [
    { heading: 'The play', body: e[0] + ' by ' + e[1] + ' premiered in ' + e[2] + '. ' + e[6] },
    { heading: 'Staging', body: 'Written as a ' + e[4] + ' in ' + e[3] + (e[3] === 1 ? ' act' : ' acts') + ', the play is set in ' + e[5] + '.' },
    { heading: 'Why it endures', body: e[8] + ' Its themes \u2014 ' + e[7] + ' \u2014 keep it in constant revival.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'play', record_kind: RECORD_KIND, origin: 'sourced', summary: e[6], details: details, sections: secs, record_text: text, source_note: 'Sourced: widely documented theater history; verify production details against published editions.', related: [e[1]], _seed: seed };
}
function realPlaywrightRecord(e, id, seed) {
  var secs = [
    { heading: 'Life and era', body: e[0] + ' (born ' + e[1] + '), ' + e[2] + ' playwright of the ' + e[3] + '.' },
    { heading: 'Style', body: e[4] + '.' },
    { heading: 'Key works', body: 'Notable works include ' + e[5] + '. ' + e[6] }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'playwright', record_kind: RECORD_KIND, origin: 'sourced', summary: e[2] + ' playwright (' + e[3] + '); ' + e[5] + '.', details: { born: e[1], nationality: e[2], era: e[3], style: e[4], notable_works: e[5].split('; ') }, sections: secs, record_text: text, source_note: 'Sourced: widely documented theater history.', related: e[5].split('; '), _seed: seed };
}
function realFormRecord(e, id, seed) {
  var secs = [
    { heading: 'The form', body: e[0] + ' \u2014 ' + e[1] + '. Defining traits: ' + e[2] + '.' },
    { heading: 'In practice', body: e[3] }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'theatrical-form', record_kind: RECORD_KIND, origin: 'sourced', summary: e[2] + '.', details: { origin: e[1], characteristics: e[2] }, sections: secs, record_text: text, source_note: 'Sourced: standard theater-history references.', related: [], _seed: seed };
}
function realStageRecord(e, id, seed) {
  var secs = [
    { heading: 'Overview', body: e[0] + ' (' + e[1] + '). Key points: ' + e[2] + '.' },
    { heading: 'Procedure', body: e[3] }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: 'stagecraft', record_kind: RECORD_KIND, origin: 'sourced', summary: e[2] + '.', details: { area: e[1], key_points: e[2].split('; ') }, sections: secs, record_text: text, source_note: 'Sourced: standard stagecraft practice; always follow local safety codes.', related: [], _seed: seed };
}
var REAL = interleave([
  REAL_PLAYS.map(function (e) { return { k: 'p', e: e }; }),
  REAL_PLAYWRIGHTS.map(function (e) { return { k: 'w', e: e }; }),
  REAL_FORMS.map(function (e) { return { k: 'f', e: e }; }),
  REAL_STAGECRAFT.map(function (e) { return { k: 's', e: e }; })
]);
var SYN_A = ['At its heart the play asks what happens when', 'The story turns on the moment', 'Everything changes when', 'The drama deepens as', 'The final act confronts'];
var SYN_B = ['a long-buried letter resurfaces', 'the tide fails to turn', 'a stranger arrives with the missing ledger', 'the lights go out mid-ceremony', 'an old promise comes due', 'the river rises past the mark', 'a confession is overheard', 'the map proves to be wrong'];
var SYN_C = ['forcing each character to choose between loyalty and survival.', 'and no one leaves the room unchanged.', 'which sets the second act racing toward dawn.', 'leaving the audience to decide who was right.', 'in a climax staged around a single unbroken silence.'];
function sigPlay(r, id, seed) {
  var title = playTitle(r), by = pick(FN, r) + ' ' + pick(LN, r), yr = ri(r, 1960, 2026);
  var acts = ri(r, 1, 5), genre = pick(GENRES, r), setting = pick(SETTINGS2, r);
  var nch = ri(r, 3, 6), chars = [], used = {};
  var names = shuffle(FN, r);
  for (var i = 0; i < nch; i++) { var nm = names[i % names.length] + ' ' + pick(LN, r); if (used[nm]) continue; used[nm] = 1; chars.push({ name: nm, role: pick(ROLES2, r) }); }
  var themes = shuffle(THEMES, r).slice(0, ri(r, 2, 4));
  var syn = pick(SYN_A, r) + ' ' + pick(SYN_B, r) + ', ' + pick(SYN_C, r);
  var venue = pick(VENUES, r) + ', ' + pick(CITIES, r);
  var secs = [
    { heading: 'The play', body: title + ' is a ' + genre + ' in ' + acts + (acts === 1 ? ' act' : ' acts') + ' by ' + by + ', premiered in ' + yr + ' at ' + venue + '. Set in ' + setting + ', ' + syn.charAt(0).toLowerCase() + syn.slice(1) },
    { heading: 'Characters', body: 'The company includes ' + chars.map(function (c) { return c.name + ' (' + c.role + ')'; }).join('; ') + '.' },
    { heading: 'Themes and staging', body: 'The play explores ' + themes.join(', ') + '. The ' + pick(ERAS, r) + ' staging favors ' + (r() < 0.5 ? 'a spare, suggestive set that lets language carry the weight.' : 'a rich, detailed world built from layered scenic elements.') }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: title, category: 'play', record_kind: RECORD_KIND, origin: 'signature-generated', summary: 'A ' + genre + ' by ' + by + ' (' + yr + '), set in ' + setting + '.', details: { playwright: by, premiere_year: String(yr), acts: acts, genre: genre, setting: setting, characters: chars, themes: themes, premiere_venue: venue }, sections: secs, record_text: text, source_note: 'Signature-generated: an original homegrown play entry, not a real-world production.', related: [by], _seed: seed };
}
function sigPlaywright(r, id, seed) {
  var name = pick(FN, r) + ' ' + pick(LN, r), nat = pick(NATIONALITIES, r), born = ri(r, 1940, 2000);
  var works = []; for (var i = 0; i < 3; i++) works.push(playTitle(r));
  var style = pick(['lyrical realism braided with folk myth', 'brutalist minimalism and long silences', 'verse comedy with a satirist\u2019s bite', 'documentary theater built from interviews', 'magical realism staged with puppetry', 'kitchen-sink naturalism with poetic monologues'], r);
  var secs = [
    { heading: 'Life and era', body: name + ' (born ' + born + ') is a ' + nat + ' playwright working in ' + style + '.' },
    { heading: 'Style', body: 'Critics note the plays\u2019 ' + pick(['patient accumulation of domestic detail', 'sudden eruptions of the uncanny', 'musical, rhythmic dialogue', 'fearless structural experiments'], r) + ', always in service of characters fighting for ' + pick(THEMES, r) + '.' },
    { heading: 'Key works', body: 'Notable works include ' + works.join('; ') + '.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: name, category: 'playwright', record_kind: RECORD_KIND, origin: 'signature-generated', summary: nat + ' playwright (born ' + born + '); ' + style + '.', details: { born: String(born), nationality: nat, era: 'contemporary', style: style, notable_works: works }, sections: secs, record_text: text, source_note: 'Signature-generated: an original homegrown playwright entry.', related: works, _seed: seed };
}
function sigForm(r, id, seed) {
  var c = pick(FORM_CONCEPTS, r);
  var secs = [
    { heading: 'The form', body: c[0] + ' \u2014 ' + c[1] + '.' },
    { heading: 'In practice', body: c[3] + ' Signature staging notes: ' + c[2] + '.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: c[0], category: 'theatrical-form', record_kind: RECORD_KIND, origin: 'signature-generated', summary: c[1] + '.', details: { origin: 'Signature experimental practice', characteristics: c[2] }, sections: secs, record_text: text, source_note: 'Signature-generated: a conceptual experimental form.', related: [], _seed: seed };
}
function sigStage(r, id, seed) {
  var t = pick(STAGE_TOPICS, r);
  var secs = [
    { heading: 'Overview', body: t[0] + ' (' + t[1] + '). ' + t[2] },
    { heading: 'Procedure', body: t[3] }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature guide', category: 'stagecraft', record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[2], details: { area: t[1], key_points: t[2].split('. ') }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown stagecraft guide; always follow local safety codes.', related: [], _seed: seed };
}
function generate(seed, opts, rnd) {
  opts = opts || {}; rnd = rnd || prng(seed);
  var idx = ((seed % 1000000) + 1000000) % 1000000;
  var id = PREFIX + String(idx + 1).padStart(7, '0');
  if (idx < REAL.length) {
    var re = REAL[idx];
    if (opts.category && ({ p: 'play', w: 'playwright', f: 'theatrical-form', s: 'stagecraft' })[re.k] !== opts.category) { /* fall through to signature */ }
    else {
      if (re.k === 'p') return realPlayRecord(re.e, id, seed);
      if (re.k === 'w') return realPlaywrightRecord(re.e, id, seed);
      if (re.k === 'f') return realFormRecord(re.e, id, seed);
      return realStageRecord(re.e, id, seed);
    }
  }
  var cat = opts.category || pick(CATS, rnd);
  if (cat === 'play') return sigPlay(rnd, id, seed);
  if (cat === 'playwright') return sigPlaywright(rnd, id, seed);
  if (cat === 'theatrical-form') return sigForm(rnd, id, seed);
  return sigStage(rnd, id, seed);
}
var REQUIRED = ['id', 'title', 'category', 'record_kind', 'origin', 'summary', 'details', 'sections', 'record_text', 'source_note'];
function validate(rec) {
  var errors = [];
  if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
  REQUIRED.forEach(function (k) { if (rec[k] === undefined || rec[k] === null || rec[k] === '') errors.push('missing ' + k); });
  if (rec.id && !/^JAH-THT-\d{7}$/.test(rec.id)) errors.push('bad id format');
  if (rec.category && CATS.indexOf(rec.category) < 0) errors.push('bad category');
  if (rec.origin && ['sourced', 'signature-generated'].indexOf(rec.origin) < 0) errors.push('bad origin');
  if (rec.sections && (!Array.isArray(rec.sections) || !rec.sections.length)) errors.push('sections empty');
  if (rec.record_text && rec.record_text.length < 120) errors.push('record_text too short');
  return { ok: errors.length === 0, errors: errors };
}
function driftCheck(rec, sample) {
  var errors = [];
  for (var i = 0; i < sample.length; i++) {
    if (sample[i] && sample[i].t === rec.title && sample[i].id !== rec.id) { errors.push('duplicate title in archive sample'); break; }
  }
  return { ok: errors.length === 0, errors: errors };
}
var GEN = { version: VERSION, generate: generate, validate: validate, driftCheck: driftCheck, slug: SLUG, prefix: PREFIX, categories: CATS, record_kind: RECORD_KIND, realCount: REAL.length };
if (typeof JAHDB !== 'undefined' && JAHDB.registerGenerator) JAHDB.registerGenerator(SLUG, GEN);
if (typeof module !== 'undefined' && module.exports) module.exports = GEN;
})();
