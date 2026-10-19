#!/usr/bin/env python3
"""Record data for the Movies and Shows database build (JAH Databases).

Four databases, 34 ladder-ordered records each (136 total):

  movies-every-film              The Movies Database            (public-harvest)
  movies-every-film-signature    The Movies Signature Database  (signature originals)
  shows-every-series             The Shows Database             (public-harvest)
  shows-every-series-signature   The Shows Signature Database   (signature originals)

Public records are real, fact-checked film/series data. Public-domain titles
carry the actual playable file reference (verified Internet Archive item,
item page hosts the in-browser player plus direct file downloads); licensed
titles carry legal watch avenues only — no infringing links anywhere.
Signature records are Manon's original Signature-line companions: an original
restoration/curation engineering plan plus an original creative treatment,
with lineage back to the public record. Clearly labeled Signature, never
presented as authentic public record.

Public-domain determinations verified 2026-10-19:
- Every public-domain title in this seed is a pre-1931 U.S. publication:
  PD by expired term (95-year term). No renewal research needed.
- Overlaps with the existing public-movies database were removed by title
  (whole-system dedupe gate); this seed complements it with different films.
- The 39 Steps (1935) was EXCLUDED as PD: after Golan v. Holder (2012) its
  copyright was restored; rights held by ITV Studios / MGM. It is not listed.
"""

# (title, year, director, cast, genre, runtime_min, story, pd_kind, archive_id, rights)
# pd_kind: expired | lapsed | defective | licensed
MOVIES = [
# ---- foundations: the silent art, simplest film grammar (ladder 1-12), all public domain
("The Great Train Robbery", 1903, "Edwin S. Porter",
 "Broncho Billy Anderson, A. C. Abadie",
 "Silent western short", 12,
 "Bandits rob a train, are pursued by a posse, and meet justice in a final shootout, closing with the famous shot of a bandit firing at the camera. "
 "Porter assembled the story from fourteen separate shots cut together for parallel action, establishing editing -- not the stage tableau -- as cinema's engine. "
 "It proved that films could tell sustained action stories and made the western a screen genre.",
 "expired", "the-great-train-robbery-1903-tmdb5698", None),
("Sherlock Holmes Baffled", 1903, "Arthur Marvin",
 "No credited cast",
 "Silent trick short", 1,
 "A burglar baffles Sherlock Holmes by vanishing in puffs of smoke in cinema's first detective film. "
 "Made by American Mutoscope and Biograph with stop-trick disappearances, it is pure screen magic in thirty seconds. "
 "It is the earliest known screen appearance of Sherlock Holmes.",
 "expired", "sherlock-holmes-baffled-1903", None),
("Broken Blossoms", 1919, "D. W. Griffith",
 "Lillian Gish, Richard Barthelmess",
 "Silent melodrama", 90,
 "A gentle Chinese shopkeeper in London shelters an abused girl from her brutal boxer father. "
 "Griffith's most tender film -- soft-focus, intimate, and humane, far from his spectacles. "
 "Gish's closet scene remains one of silent cinema's most harrowing performances.",
 "expired", "broken-blossoms", None),
("Within Our Gates", 1920, "Oscar Micheaux",
 "Evelyn Preer, Flo Clements",
 "Silent race-film drama", 79,
 "A Black schoolteacher travels north to raise money for her Southern school, confronting racism, lynching, and interracial violence along the way. "
 "Micheaux, America's first major Black feature filmmaker, made it as a direct answer to The Birth of a Nation, centering Black dignity and resistance. "
 "It is the oldest surviving feature by an African-American director.",
 "expired", "within-our-gates-1920-by-oscar-micheaux", None),
("The Mark of Zorro", 1920, "Fred Niblo",
 "Douglas Fairbanks",
 "Silent swashbuckler", 107,
 "Don Diego Vega poses as a fop by day and becomes the masked Zorro by night to fight a corrupt governor. "
 "Fairbanks invented the screen swashbuckler -- and the superhero's double identity -- in a single leap. "
 "It made him the king of adventure and set the template for masked heroes.",
 "expired", "silent-the-mark-of-zorro", None),
("Way Down East", 1920, "D. W. Griffith",
 "Lillian Gish, Richard Barthelmess",
 "Silent melodrama", 148,
 "A betrayed country girl is cast out and finds shelter with a farm family, climaxing on ice floes in a frozen river. "
 "Griffith's ice-floe rescue -- Gish drifting toward a waterfall -- is silent cinema's most famous peril sequence. "
 "Audiences wept and exhibitors grew rich; it was among the biggest hits of the silent era.",
 "expired", "way-down-east-1920-by-d.-w.-griffith", None),
("The Kid", 1921, "Charlie Chaplin",
 "Charlie Chaplin, Jackie Coogan",
 "Silent comedy-drama", 68,
 "The Tramp raises an abandoned baby as his own, and the two survive by their wits until authorities -- and the boy's mother -- intervene. "
 "Chaplin blends slapstick with genuine pathos, letting a comedy carry the weight of poverty, charity, and parenthood. "
 "It made the feature-length comedy-drama respectable and made Jackie Coogan the first great child star.",
 "expired", "turner_video_9", None),
("The Sheik", 1921, "George Melford",
 "Rudolph Valentino, Agnes Ayres",
 "Silent romance", 80,
 "An Englishwoman is abducted by an Arab sheik in the desert and falls for her captor. "
 "Valentino became the screen's great lover overnight and defined smoldering romance for the decade. "
 "Its desert fantasies now read as pure 1920s exoticism -- a time capsule of the era's desires.",
 "expired", "THESHEIKSilent1921RudolphValentino", None),
("Sherlock Holmes", 1922, "Albert Parker",
 "John Barrymore",
 "Silent mystery", 109,
 "Holmes battles Professor Moriarty across London and Switzerland in this big-budget silent adaptation. "
 "Barrymore -- the great stage Hamlet -- brought theatrical grandeur to the detective. "
 "Long thought lost, it was rediscovered and restored, returning a landmark to view.",
 "expired", "SherlockHolmessilent1922", None),
("Our Hospitality", 1923, "Buster Keaton and John G. Blystone",
 "Buster Keaton",
 "Silent comedy", 74,
 "A New Yorker inherits a Southern estate and walks into a generations-old feud -- where hospitality rules forbid killing a guest under your roof. "
 "Keaton's first great feature: a deadpan odyssey ending on a waterfall. "
 "The train and river sequences are engineering marvels of comedy construction.",
 "expired", "OurHospitality_29", None),
("Sherlock Jr.", 1924, "Buster Keaton",
 "Buster Keaton",
 "Silent comedy", 44,
 "A daydreaming projectionist imagines himself a great detective inside the movie he is showing. "
 "Keaton walks into the screen -- literally -- in cinema's most playful meditation on film itself. "
 "At 44 minutes it is the most perfect short feature ever made.",
 "expired", "sherlock-jr.-1924-by-buster-keaton", None),
("The Kid Brother", 1927, "Ted Wilde",
 "Harold Lloyd",
 "Silent comedy", 84,
 "The timid youngest son of a sheriff must prove himself when a traveling medicine show brings trouble to town. "
 "Lloyd's most character-driven comedy -- less thrill, more heart than his skyscraper pictures. "
 "The strongman finale is a masterclass in underdog triumph.",
 "expired", "harold-lloyd-the-kid-brother-1927", None),
# ---- compounded: late-silent mastery and the coming of sound (ladder 13-24), all public domain
("The Phantom of the Opera", 1925, "Rupert Julian",
 "Lon Chaney, Mary Philbin",
 "Horror", 101,
 "A disfigured musical genius haunts the Paris Opera, obsessed with a young singer. "
 "Chaney's self-designed skull-face reveal -- done without studio permission -- is horror's most famous unmasking. "
 "The chandelier crash set the template for stage horror on screen.",
 "expired", "ThePhantomOfTheOpera_364", None),
("The Thief of Bagdad", 1924, "Raoul Walsh",
 "Douglas Fairbanks",
 "Silent fantasy adventure", 155,
 "A roguish thief loves a princess and quests for treasures -- a flying carpet, an invisibility cloak -- to win her. "
 "Fairbanks's Arabian Nights epic built the most lavish fantasy sets of the silent era. "
 "Every screen fantasy since owes it a debt, from its magic to its matte paintings.",
 "expired", "sonido-ttob-1080p", None),
("The Last Laugh", 1924, "F. W. Murnau",
 "Emil Jannings",
 "German silent drama", 90,
 "An aging hotel doorman is demoted to washroom attendant and his dignity collapses. "
 "Murnau told the story almost without intertitles -- the 'unchained camera' moving through the hotel made subjectivity visual. "
 "The benchmark of German silent artistry and of the camera as narrator.",
 "expired", "silent-the-last-laugh", None),
("The Man Who Laughs", 1928, "Paul Leni",
 "Conrad Veidt",
 "Horror melodrama", 110,
 "A nobleman's son, his face carved into a permanent grin, becomes a circus clown while loving a blind girl. "
 "Veidt's grin directly inspired the Joker, drawn from this very performance. "
 "Leni's gothic visuals made it Universal's most beautiful horror film.",
 "expired", "the-man-who-laughs-1928_202404", None),
("The Cat and the Canary", 1927, "Paul Leni",
 "Laura La Plante",
 "Horror comedy", 80,
 "Heirs gather in a creepy mansion for a will reading as an escaped lunatic prowls outside. "
 "Leni invented the old-dark-house formula -- secret panels, clutching hands -- that horror-comedy still uses. "
 "The template for every haunted-house movie after it.",
 "expired", "the-cat-and-the-canary-1927", None),
("The Lodger", 1927, "Alfred Hitchcock",
 "Ivor Novello, Marie Ault",
 "Silent thriller", 91,
 "A mysterious lodger may be the serial killer terrorizing London. "
 "Hitchcock's first thriller -- and the first true 'Hitchcock film' -- with the glass-ceiling shot and the director's first cameo. "
 "The wrong-man theme that defined his career starts here.",
 "expired", "the.-lodger.-a.-story.-of.-the.-london.-fog.-1927", None),
("Steamboat Bill, Jr.", 1928, "Charles Reisner and Buster Keaton",
 "Buster Keaton, Ernest Torrence",
 "Silent comedy", 70,
 "A college-educated weakling tries to win his stern steamboat-captain father's respect, culminating in a cyclone that tears the town apart. "
 "The cyclone sequence -- including the famous falling-house-front gag -- is the most dangerous and precisely timed stunt comedy ever filmed. "
 "It is Keaton's last great independent feature and a masterclass in physical storytelling.",
 "expired", "turner_video_20", None),
("The Cameraman", 1928, "Edward Sedgwick and Buster Keaton",
 "Buster Keaton",
 "Silent comedy", 69,
 "A would-be newsreel cameraman bungles every assignment trying to impress a girl at the studio. "
 "Keaton's first MGM film still carries his full genius -- the Tong War shootout is peak Keaton. "
 "His last great silent feature, made as the silent era was ending around him.",
 "expired", "TheCameramanWBusterKeatonFULLHDVideoDailymotion", None),
("The Circus", 1928, "Charlie Chaplin",
 "Charlie Chaplin, Merna Kennedy",
 "Silent comedy", 72,
 "The Tramp stumbles into a failing circus, becomes its accidental star clown, and falls for the bareback rider. "
 "Chaplin's tightrope-walk finale -- pursued by monkeys -- is among his most physically daring sequences. "
 "Released in 1928, its U.S. copyright has expired, placing it in the public domain.",
 "expired", "the-circus-charlie-chaplin", None),
("Blackmail", 1929, "Alfred Hitchcock",
 "Anny Ondra, John Longden",
 "Thriller", 85,
 "A woman kills an attacker in self-defense, then faces blackmail -- from a detective who loves her. "
 "Hitchcock's first sound film, shot silent then reshot with dialogue, pivots on the famous knife-scream montage. "
 "The sound era's first great British thriller.",
 "expired", "blackmail-1929_202303", None),
("Man with a Movie Camera", 1929, "Dziga Vertov",
 "The people of a Soviet city (non-actors)",
 "Soviet documentary", 68,
 "A day in a Soviet city, filmed and edited as pure visual music -- no plot, no actors, no intertitles. "
 "Vertov's manifesto: the camera eye sees what the human eye cannot. "
 "The most exhilarating editing ever put on screen, and the founding work of experimental documentary.",
 "expired", "ChelovekskinoapparatomManWithAMovieCamera", None),
("The Hitch-Hiker", 1953, "Ida Lupino",
 "Edmond O'Brien, Frank Lovejoy",
 "Film noir", 71,
 "Two friends on a fishing trip pick up a hitchhiker who turns out to be a wanted killer holding them hostage. "
 "Lupino -- the only woman directing studio noirs in the 1950s -- strips the genre to sweat, headlights, and dread. "
 "Its U.S. copyright was never renewed, placing it in the public domain.",
 "lapsed", "the-hitch-hiker-1953-by-ida-lupino", None),
# ---- advanced: studio-era and modern landmarks (ladder 25-34), licensed
("Casablanca", 1942, "Michael Curtiz",
 "Humphrey Bogart, Ingrid Bergman",
 "Romantic drama", 102,
 "In wartime Morocco, a cynical cafe owner must choose between his lost love and helping her resistance-hero husband escape. "
 "Written day by day on the set, it became the most quoted film in history and the template for romantic sacrifice. "
 "It is a licensed studio work; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Warner Bros."),
("Citizen Kane", 1941, "Orson Welles",
 "Orson Welles, Joseph Cotten",
 "Drama", 119,
 "Reporters chase the meaning of a newspaper magnate's dying word, 'Rosebud,' through contradictory memories. "
 "Welles, 25, reinvented deep focus, ceilinged sets, and fractured narrative in a single debut that tops greatest-film polls to this day. "
 "It is a licensed studio work; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Warner Bros."),
("It's a Wonderful Life", 1946, "Frank Capra",
 "James Stewart, Donna Reed",
 "Fantasy drama", 130,
 "A despairing small-town banker sees, through an angel's intervention, how empty the world would be without him. "
 "A box-office disappointment in 1946, it became America's Christmas film through decades of television. "
 "Its copyright lapsed in 1974 but underlying rights were later reasserted -- treat it as a licensed work.",
 "licensed", None, "Paramount / NBCUniversal (licensed)"),
("12 Angry Men", 1957, "Sidney Lumet",
 "Henry Fonda, Lee J. Cobb",
 "Courtroom drama", 96,
 "One holdout juror forces eleven others to re-examine a seemingly open-and-shut murder case, vote by vote. "
 "Shot almost entirely in one room, it is the definitive drama of reason against prejudice. "
 "It is a licensed studio work; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "MGM / Amazon MGM Studios"),
("Psycho", 1960, "Alfred Hitchcock",
 "Anthony Perkins, Janet Leigh",
 "Horror thriller", 109,
 "A secretary on the run stops at a lonely motel managed by a shy young man and his unseen mother. "
 "Hitchcock killed his star a third of the way in and rewrote the rules of horror, suspense, and marketing with it. "
 "It is a licensed studio work; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Universal Pictures"),
("The Godfather", 1972, "Francis Ford Coppola",
 "Marlon Brando, Al Pacino",
 "Crime drama", 175,
 "The aging head of a crime family transfers power to his reluctant youngest son, who becomes colder than the father. "
 "Coppola turned a pulp bestseller into American tragedy; Brando's mumbled Don and Pacino's freezing stare defined screen acting. "
 "It is a licensed studio work; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Paramount Pictures"),
("Star Wars", 1977, "George Lucas",
 "Mark Hamill, Harrison Ford, Carrie Fisher",
 "Space opera", 121,
 "A farm boy, a princess, and a smuggler join a rebellion to destroy a planet-killing battle station. "
 "Lucas fused Kurosawa, Flash Gordon serials, and Joseph Campbell into the blockbuster template that reorganized Hollywood. "
 "It is a licensed studio work; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Lucasfilm / Disney"),
("Back to the Future", 1985, "Robert Zemeckis",
 "Michael J. Fox, Christopher Lloyd",
 "Science-fiction comedy", 116,
 "A teenager is flung thirty years into the past and must make his parents fall in love or erase himself. "
 "Its clockwork screenplay -- every setup paid off -- is taught as the perfect commercial script. "
 "It is a licensed studio work; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Universal Pictures"),
("Toy Story", 1995, "John Lasseter",
 "Tom Hanks, Tim Allen",
 "Animated family film", 81,
 "A cowboy doll's world collapses when a space-ranger toy takes his place as a boy's favorite. "
 "The first fully computer-animated feature, it proved digital animation could carry a story and launched Pixar. "
 "It is a licensed studio work; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Disney / Pixar"),
("The Matrix", 1999, "The Wachowskis",
 "Keanu Reeves, Laurence Fishburne",
 "Science-fiction action", 136,
 "A hacker learns reality is a simulation and joins the war against the machines that farm humanity. "
 "Its bullet-time, Hong Kong choreography, and simulation philosophy rewired action cinema and popular thought. "
 "It is a licensed studio work; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Warner Bros."),
]

# (title, years, network, stars, genre, ep_len_min, episodes, story, pd_kind, archive_id, rights)
SHOWS = [
# ---- foundations: early television (ladder 1-12), public-domain episodes
("Captain Video and His Video Rangers", "1949-1955", "DuMont Television Network",
 "Al Hodge", "Science-fiction serial", 30, "hundreds of episodes (few survive)",
 "Television's first space hero battled villains across the galaxy from a cardboard cockpit, live every night. "
 "Made for almost nothing on the DuMont network, it proved science fiction could live on the small screen. "
 "Surviving episodes were never renewed for copyright and are in the public domain.",
 "lapsed", "captain-video-and-his-video-rangers-episode-4-of-4-mkv", None),
("The Cisco Kid", "1950-1956", "Syndicated",
 "Duncan Renaldo, Leo Carrillo", "Western", 30, "156 episodes",
 "The Cisco Kid and his comic sidekick Pancho righted wrongs across the Old West with charm instead of cruelty. "
 "Filmed in color when almost everything aired in black and white, it was an early syndication triumph. "
 "Many episodes were never renewed for copyright and are in the public domain.",
 "lapsed", "cisco-kid-s-01-e-08-convict-story", None),
("The Gene Autry Show", "1950-1956", "CBS",
 "Gene Autry", "Western", 30, "91 episodes",
 "America's singing cowboy rode into a different town each week, solving problems with a guitar, a code of honor, and Champion the horse. "
 "Autry's Cowboy Code — never shoot first, always help the weak — shaped a generation's idea of decency. "
 "Many episodes were never renewed for copyright and are in the public domain.",
 "lapsed", "GeneAutryDoubleSwitch08271950", None),
("You Bet Your Life", "1950-1961", "NBC",
 "Groucho Marx", "Quiz and comedy", 30, "hundreds of episodes",
 "Groucho Marx interviewed ordinary contestants with ad-libbed wit, occasionally interrupted by a quiz for the secret word. "
 "It turned the game show into a comedy showcase and won television's highest honors. "
 "Many episodes were never renewed for copyright and are in the public domain.",
 "lapsed", "Wall_1950s-game-show", None),
("Tom Corbett, Space Cadet", "1950-1955", "CBS, ABC, NBC, and DuMont",
 "Frankie Thomas", "Science fiction", 30, "hundreds of episodes",
 "Cadet Tom Corbett and his crewmates trained at Space Academy and patrolled the solar system for the Solar Guard. "
 "Airing across all four networks at various times, it made space opera a children's-television staple. "
 "Surviving episodes were never renewed for copyright and are in the public domain.",
 "lapsed", "1955-tom-corbett-deep-space-project-360p", None),
("Dragnet", "1951-1959", "NBC",
 "Jack Webb", "Police procedural", 30, "276 episodes",
 "Sergeant Joe Friday worked cases 'just the facts' through Los Angeles, in television's first true police procedural. "
 "Webb's documentary flatness — real case files, no glamour — invented the cop show as a genre. "
 "Many episodes were never renewed for copyright and are in the public domain.",
 "lapsed", "dragnet_202101", None),
("The Adventures of Kit Carson", "1951-1955", "Syndicated",
 "Bill Williams", "Western", 30, "104 episodes",
 "Frontiersman Kit Carson and his partner El Toro protected settlers across the frontier. "
 "One of the first westerns made specifically for television syndication, it filled the after-school hours of the 1950s. "
 "Many episodes were never renewed for copyright and are in the public domain.",
 "lapsed", "TheAdventuresOfKitCarsonSingingWires", None),
("The Roy Rogers Show", "1951-1957", "NBC",
 "Roy Rogers, Dale Evans", "Western", 30, "101 episodes",
 "Roy Rogers, Dale Evans, and Trigger kept the peace in Mineral City with songs and straight shooting. "
 "The King of the Cowboys brought his movie stardom to Sunday television for six seasons. "
 "Many episodes were never renewed for copyright and are in the public domain.",
 "lapsed", "The_Roy_Rogers_Show_-_Ranch_War", None),
("Hopalong Cassidy", "1952-1954", "Syndicated and NBC",
 "William Boyd", "Western", 30, "52 episodes",
 "The silver-haired Hopalong Cassidy brought feature-film westerns to television, edited and repackaged for the small screen. "
 "Boyd bought his own films and became television's first western star — and its first merchandising phenomenon. "
 "Many episodes were never renewed for copyright and are in the public domain.",
 "lapsed", "HopalongCassidyColtsvilleTerritoryJanuary151950", None),
("Sherlock Holmes", "1954-1955", "Syndicated",
 "Ronald Howard", "Mystery", 30, "39 episodes",
 "Ronald Howard's Holmes and Howard Marion-Crawford's Watson solved original mysteries across Europe. "
 "The first American television Holmes, it played the detective straight in half-hour doses. "
 "The series was never renewed for copyright and is in the public domain.",
 "lapsed", "sherlock-holmes-the-complete-tv-series-1954-55-dvd-1-of-5_20221114", None),
("Annie Oakley", "1954-1957", "Syndicated",
 "Gail Davis", "Western", 30, "81 episodes",
 "Sharp-shooting Annie Oakley kept order in the town of Diablo with her brother Tagg and deputy Lofty. "
 "One of television's first female-led westerns, it gave young viewers a heroine who outshot everyone. "
 "Many episodes were never renewed for copyright and are in the public domain.",
 "lapsed", "annie-oakley-tv-series-episodes", None),
("Flash Gordon", "1936", "Universal Pictures (serial)",
 "Buster Crabbe", "Science-fiction serial", 20, "13 chapters",
 "Flash Gordon, Dale Arden, and Dr. Zarkov travel to the planet Mongo to stop Emperor Ming the Merciless. "
 "The 13-chapter serial invented screen space opera — the direct ancestor of Star Wars — with cliffhangers that filled Saturday matinees. "
 "Its copyright was never renewed and it is in the public domain.",
 "lapsed", "PhantasmagoriaTheater-FlashGordonEpisodeOneThePlanetOfPeril445-2", None),
# ---- compounded: the network golden age (ladder 13-24), licensed
("I Love Lucy", "1951-1957", "CBS",
 "Lucille Ball, Desi Arnaz", "Sitcom", 30, "180 episodes",
 "Lucy Ricardo's schemes for stardom constantly collided with her bandleader husband Ricky's patience. "
 "Ball's physical genius, the multi-camera studio audience format, and the rerun — all invented or perfected here. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Paramount / CBS"),
("The Twilight Zone", "1959-1964", "CBS",
 "Rod Serling (host and creator)", "Anthology science fiction", 30, "156 episodes",
 "Ordinary people stepped into the fifth dimension, where twist endings carried moral weight. "
 "Serling smuggled civil rights, war, and conformity past the censors inside fantasy parables. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Paramount / CBS"),
("The Andy Griffith Show", "1960-1968", "CBS",
 "Andy Griffith, Ron Howard", "Sitcom", 30, "249 episodes",
 "Sheriff Andy Taylor kept the peace in Mayberry with common sense while Deputy Barney Fife supplied the chaos. "
 "Television's gentlest comedy — decency as a weekly practice — anchored by Griffith's warmth. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Paramount / CBS"),
("Star Trek: The Original Series", "1966-1969", "NBC",
 "William Shatner, Leonard Nimoy", "Science fiction", 60, "79 episodes",
 "The crew of the starship Enterprise explored strange new worlds on a five-year mission. "
 "Cancelled after three seasons, it became the most influential science-fiction universe ever built, through reruns and fandom. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Paramount"),
("Mister Rogers' Neighborhood", "1968-2001", "PBS",
 "Fred Rogers", "Children's", 30, "912 episodes",
 "Fred Rogers spoke directly to children about feelings, fears, and kindness, one gentle episode at a time. "
 "The most humane program in television history — radical in its belief that children deserve honesty and respect. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Fred Rogers Productions"),
("Sesame Street", "1969-present", "PBS",
 "Ensemble cast and the Muppets", "Children's", 60, "over 4,500 episodes",
 "Big Bird, Oscar, and generations of Muppets taught letters, numbers, and empathy on the most famous street on television. "
 "The longest-running children's program in American history, researched like a curriculum and loved like family. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Sesame Workshop"),
("The Mary Tyler Moore Show", "1970-1977", "CBS",
 "Mary Tyler Moore", "Sitcom", 30, "168 episodes",
 "A single woman built a career and a chosen family at a Minneapolis TV newsroom. "
 "The first great workplace sitcom — and television's declaration that a woman's story needed no husband to matter. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Disney / 20th Television"),
("All in the Family", "1971-1979", "CBS",
 "Carroll O'Connor, Jean Stapleton", "Sitcom", 30, "202 episodes",
 "Bigot Archie Bunker clashed nightly with his liberal son-in-law Meathead over everything dividing America. "
 "Norman Lear proved the sitcom could hold the country's arguments — racism, war, women's rights — and still get laughs. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Sony Pictures"),
("M*A*S*H", "1972-1983", "CBS",
 "Alan Alda", "Comedy-drama", 30, "256 episodes",
 "Army surgeons used jokes as armor against the daily horror of the Korean War. "
 "Its finale remains the most-watched television episode in American history; its mix of laughter and grief set the template for dramedy. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Disney / 20th Television"),
("Cheers", "1982-1993", "NBC",
 "Ted Danson", "Sitcom", 30, "275 episodes",
 "The regulars of a Boston bar — where everybody knows your name — stumbled through love, work, and beer. "
 "The ensemble sitcom perfected: eleven seasons of character comedy that made the bar a second home for millions. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Paramount"),
("The Simpsons", "1989-present", "Fox",
 "Voice ensemble", "Animated sitcom", 30, "over 750 episodes",
 "The Simpson family of Springfield satirized everything in American life for what became the longest-running scripted series in history. "
 "It made prime-time animation viable and trained generations in irony. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Disney / 20th Television"),
("Seinfeld", "1989-1998", "NBC",
 "Jerry Seinfeld and ensemble", "Sitcom", 30, "180 episodes",
 "Four neurotic New Yorkers navigated dating, manners, and nothing in particular. "
 "The 'show about nothing' perfected the comedy of petty social rules and ended on its own uncompromising terms. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Sony Pictures"),
# ---- advanced: prestige and streaming eras (ladder 25-34), licensed
("The X-Files", "1993-2018", "Fox",
 "David Duchovny, Gillian Anderson", "Science-fiction drama", 60, "218 episodes",
 "FBI agents Mulder and Scully investigated the paranormal — he believed, she demanded proof. "
 "It made serialized mythology television mainstream and taught a generation to trust no one. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Disney / 20th Television"),
("Friends", "1994-2004", "NBC",
 "Ensemble cast", "Sitcom", 30, "236 episodes",
 "Six friends in Manhattan apartments and a coffee shop grew up together across ten seasons. "
 "The defining hangout sitcom — endlessly rewatchable, endlessly quoted, streaming's eternal comfort watch. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Warner Bros."),
("The Sopranos", "1999-2007", "HBO",
 "James Gandolfini", "Crime drama", 60, "86 episodes",
 "A New Jersey mob boss's panic attacks landed him in therapy, exposing the rot inside the American dream. "
 "The series that proved television could be art on cinema's level — and changed what the medium was allowed to be. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "HBO / Warner Bros. Discovery"),
("The Wire", "2002-2008", "HBO",
 "Dominic West", "Crime drama", 60, "60 episodes",
 "Baltimore's drug war, told season by season through the police, the dealers, the docks, the schools, and the press. "
 "A novel in five seasons about how institutions fail the people inside them — the critics' consensus greatest drama ever. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "HBO / Warner Bros. Discovery"),
("The Office", "2005-2013", "NBC",
 "Steve Carell", "Sitcom", 30, "201 episodes",
 "A documentary crew filmed the world's worst best boss and his paper-company employees. "
 "The American mockumentary found its heart — cringe comedy with genuine love for its characters. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "NBCUniversal"),
("Planet Earth", "2006", "BBC and Discovery",
 "David Attenborough (narrator)", "Nature documentary", 60, "11 episodes",
 "Eleven episodes crossed every biome on the planet in high definition for the first time. "
 "The most expensive documentary series ever made at its release — and the benchmark all nature films are judged against. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "BBC"),
("Breaking Bad", "2008-2013", "AMC",
 "Bryan Cranston, Aaron Paul", "Crime drama", 60, "62 episodes",
 "A dying chemistry teacher cooked meth to provide for his family and became a monster. "
 "The most complete character transformation in television — Mr. Chips into Scarface, measured in 62 episodes. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Sony Pictures"),
("Game of Thrones", "2011-2019", "HBO",
 "Ensemble cast", "Fantasy drama", 60, "73 episodes",
 "Noble houses warred for the Iron Throne while the dead marched from the north. "
 "The biggest television event of the 2010s — proof that fantasy could command cinema-scale spectacle weekly. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "HBO / Warner Bros. Discovery"),
("Cosmos: A Spacetime Odyssey", "2014", "Fox and National Geographic",
 "Neil deGrasse Tyson (host)", "Science documentary", 60, "13 episodes",
 "A new Ship of the Imagination carried viewers across 13.8 billion years of cosmic history. "
 "Carl Sagan's legacy rebooted for a new century — science as the greatest story ever told. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "National Geographic / Disney"),
("Stranger Things", "2016-present", "Netflix",
 "Ensemble cast", "Science-fiction horror", 60, "42 episodes across four released seasons",
 "Kids in 1980s Hawkins battled creatures from the Upside Down with bikes, walkie-talkies, and friendship. "
 "Netflix's flagship proved streaming could birth monoculture — and made a generation fall for synth scores. "
 "It is a licensed series; watch it through licensed services, rental, physical media, or the library.",
 "licensed", None, "Netflix"),
]
