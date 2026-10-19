#!/usr/bin/env python3
"""Entries for the Geography Quiz databases (Manon 16:15 orders 2026-10-17).

Two NEW databases, 34 ladder-ordered records each. Every record is one
complete ten-question geography quiz with the full answer key printed AT
THE BOTTOM of the record (his explicit requirement). Records march
easy -> hard along the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

  quiz-geography            - The Geography Quiz Database (public-harvest:
                              real, fact-checked geography quiz questions -
                              continents, oceans, capitals, mountains,
                              rivers, deserts, islands, lakes, volcanoes,
                              climate, maps, time zones, borders, landmarks)
  quiz-geography-signature  - The Geography Quiz Signature Database
                              (his original Signature Quiz Method: every
                              quiz a proving of the lands, every question a
                              landmark on the trail, every answer a sealed
                              stamp, the answer key the unsealing at the
                              bottom; src signature, titles suffixed
                              " (Signature Edition)", never presented as
                              authentic public record)

ID prefixes: JAH-QZGE- (public) and JAH-QZGES- (signature), verified free
in the manifest id_prefix values and in every shard index file (zero
hits). Slug quiz-geography and name The Geography Quiz Database verified
free across the manifest (2,447 entries). All 68 titles gate-checked
against the whole-system dedupe exact index before authoring: zero
collisions, zero refusals.

Numerical cores: every demo is a real quiz runner - it loads the same
ten questions and answers the record carries, simulates a scored run,
asserts the exact score, prints the answer key, and ends with the OK
marker. Demos and record text are generated from the same qa lists, so
entry text and demo outputs cannot drift apart.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing hate-adjacent, profane, or inappropriate.
"""

SIG_TAIL = ("Signature original - his original Signature Quiz Method: every "
            "quiz a proving of the lands, every question a landmark on the "
            "trail, every answer a sealed stamp, and the answer key the "
            "unsealing at the bottom. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

SIG_LENS = ("His original Signature Quiz "
            "Method frames this quiz as a proving of the lands: every "
            "question a landmark on the trail, every answer a sealed stamp, "
            "and the answer key the unsealing at the bottom. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_FACTBOOK = ("Central Intelligence Agency. The World Factbook. Washington, "
                "DC; updated 2026.")
CIT_NATGEO = ("National Geographic Society. National Geographic Atlas of the "
              "World. 11th ed; 2019.")
CIT_BRITANNICA = ("Encyclopaedia Britannica. Geography reference articles; "
                  "accessed 2026.")
CIT_USGS = ("U.S. Geological Survey. Geographic names and earthquake hazards "
            "data; 2026.")
CIT_UN = ("United Nations Statistics Division. Demographic and geographic "
          "data; 2024 revision.")
CIT_GUINNESS = ("Guinness World Records. Natural world records; 2026.")
CIT_NOAA = ("National Oceanic and Atmospheric Administration. Ocean and "
            "climate data; 2026.")

KP = [
    "Each quiz holds exactly ten questions, and each correct answer is worth ten points.",
    "A perfect round scores one hundred points, and seventy or more is a strong pass.",
    "Read every question before you peek: the full answer key sits at the bottom of the record.",
    "Answers are checked against the key; wording that names the right place counts as correct.",
    "Quizzes are ordered easy to hard along the teaching ladder, so later quizzes assume earlier ones.",
]

REQ = [
    "A quiet few minutes, plus a pen and paper or a notes app to write your answers.",
    "Cover the answers section at the bottom until you have answered all ten questions.",
    "A timer is optional: try five minutes per quiz once the easy ones feel comfortable.",
    "No atlas is needed for the first attempt; check one afterwards for every miss.",
]

STD = [
    "Every answer is a real, checkable geography fact, verified against standard references before publishing.",
    "Capitals are current national capitals, and country names follow common English usage.",
    "Measurements are rounded standard figures for heights, depths, and lengths, as the references cite them.",
    "Where a fact is disputed or has changed over time, the question says so plainly.",
    "Answer keys are printed at the bottom of every record, never hidden behind a link.",
]

ENTRIES = [
    {
        "key": "qzg_continents_oceans",
        "name": "The Continents and Oceans Quiz",
        "group": "Maps and Navigation",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "description": ("Ten easy starter questions about the seven continents and the five oceans. "
                        "This quiz asks which continent is the largest, which ocean is the widest, and where "
                        "the great landmasses and waters of the world sit on the globe. It is the first rung "
                        "of the ladder: simple, fact-checked geography every learner should know. Ten questions, "
                        "ten points each, and the full answer key waits at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_FACTBOOK],
        "sig_lens": SIG_LENS,
        "qa": [
            ("How many continents are there on Earth?", "Seven"),
            ("Which is the largest continent?", "Asia"),
            ("Which is the smallest continent?", "Australia"),
            ("Which is the largest ocean in the world?", "The Pacific Ocean"),
            ("Which ocean lies between the Americas to the west and Europe and Africa to the east?", "The Atlantic Ocean"),
            ("Which ocean is the smallest and surrounds the North Pole?", "The Arctic Ocean"),
            ("Which ocean touches the eastern coast of Africa?", "The Indian Ocean"),
            ("Which ocean surrounds the continent of Antarctica?", "The Southern Ocean"),
            ("Which continent is also a single country?", "Australia"),
            ("On which continent is the Sahara Desert?", "Africa"),
        ],
    },
    {
        "key": "qzg_world_capitals",
        "name": "The World Capitals Quiz",
        "group": "Countries and Capitals",
        "ladder_rank": 1, "ladder_tier": "foundations",
        "description": ("Ten easy questions matching famous countries to their capital cities. From Paris "
                        "and Tokyo to Canberra and Brasilia, this quiz covers the capitals every geography "
                        "learner meets first. Each answer is a real, current capital city, fact-checked "
                        "against the record. Ten questions, ten points each, with the answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the capital of France?", "Paris"),
            ("What is the capital of Japan?", "Tokyo"),
            ("What is the capital of the United Kingdom?", "London"),
            ("What is the capital of Italy?", "Rome"),
            ("What is the capital of Spain?", "Madrid"),
            ("What is the capital of Germany?", "Berlin"),
            ("What is the capital of Egypt?", "Cairo"),
            ("What is the capital of Australia?", "Canberra"),
            ("What is the capital of Canada?", "Ottawa"),
            ("What is the capital of Brazil?", "Brasilia"),
        ],
    },
    {
        "key": "qzg_maps_compass",
        "name": "The Maps and Compass Directions Quiz",
        "group": "Maps and Navigation",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "description": ("Ten questions about reading maps and finding direction. Learn the four cardinal "
                        "directions, the points in between, what a legend and a compass rose tell you, and "
                        "how the sun helps you navigate. A foundations quiz for anyone learning to read a map. "
                        "Ten questions, ten points each, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("How many cardinal directions are there?", "Four: north, south, east, and west"),
            ("Which direction is directly opposite north?", "South"),
            ("What is the direction halfway between north and east called?", "Northeast"),
            ("What does the legend of a map explain?", "The symbols used on the map"),
            ("What does the compass rose on a map show?", "The directions on the map"),
            ("In which direction does the sun rise?", "East"),
            ("In which direction does the sun set?", "West"),
            ("What are the four intercardinal (in-between) directions?", "Northeast, southeast, southwest, and northwest"),
            ("If you face north, which direction is on your left?", "West"),
            ("On most maps, which direction is at the top?", "North"),
        ],
    },
    {
        "key": "qzg_mountains",
        "name": "The Mountains and Mountain Ranges Quiz",
        "group": "Landforms and Mountains",
        "ladder_rank": 2, "ladder_tier": "foundations",
        "description": ("Ten questions about the great mountains and ranges of the world. Meet Mount Everest "
                        "and the Himalayas, the long Andes, the Rockies, the Alps, and Kilimanjaro, and learn "
                        "which range draws the line between Europe and Asia. A foundations quiz built from "
                        "standard heights and ranges. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_BRITANNICA, CIT_GUINNESS],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the highest mountain in the world?", "Mount Everest"),
            ("About how high is Mount Everest?", "8,848 metres"),
            ("In which mountain range does Mount Everest stand?", "The Himalayas"),
            ("What is the longest continental mountain range in the world?", "The Andes"),
            ("On which continent are the Andes?", "South America"),
            ("What is the highest mountain in Africa?", "Mount Kilimanjaro"),
            ("Which mountain range runs through the western United States and Canada?", "The Rocky Mountains"),
            ("The Alps are on which continent?", "Europe"),
            ("Which mountains form a natural boundary between Europe and Asia in Russia?", "The Ural Mountains"),
            ("What is the highest mountain in North America?", "Denali"),
        ],
    },
    {
        "key": "qzg_great_rivers",
        "name": "The Great Rivers of the World Quiz",
        "group": "Rivers and Water",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "description": ("Ten questions about the great rivers of the world. Follow the Nile through Egypt, "
                        "the Amazon through South America, the Yangtze through China, and the Mississippi "
                        "through North America, and learn which rivers rank longest on each continent. Every "
                        "river here is real and fact-checked. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("Which river is traditionally listed as the longest in the world?", "The Nile"),
            ("Which river carries the most water of any river on Earth?", "The Amazon"),
            ("What is the longest river in Asia?", "The Yangtze"),
            ("What is the longest river system in North America?", "The Mississippi-Missouri"),
            ("Which river flows north through Egypt to the Mediterranean Sea?", "The Nile"),
            ("What is the longest river in Europe?", "The Volga"),
            ("Which river flows through Paris?", "The Seine"),
            ("Through which two countries does the Ganges flow mainly?", "India and Bangladesh"),
            ("Which river forms part of the border between the United States and Mexico?", "The Rio Grande"),
            ("Through how many countries does the Danube flow?", "Ten"),
        ],
    },
    {
        "key": "qzg_deserts_rainforests",
        "name": "The Deserts and Rainforests Quiz",
        "group": "Landforms and Mountains",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "description": ("Ten questions about the driest and wettest places on Earth. Visit the Sahara, the "
                        "Mojave, the Gobi, and the Atacama, then travel to the Amazon rainforest and learn "
                        "what an oasis is and where rainforests grow. A foundations quiz of extremes, all "
                        "fact-checked. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_BRITANNICA, CIT_NOAA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the largest hot desert in the world?", "The Sahara"),
            ("On which continent is the Sahara?", "Africa"),
            ("What is the largest rainforest in the world?", "The Amazon rainforest"),
            ("In which country is most of the Amazon rainforest?", "Brazil"),
            ("Which desert holds Death Valley in the United States?", "The Mojave Desert"),
            ("What is an oasis?", "A fertile spot in a desert where water is found"),
            ("In which two countries does the Gobi Desert lie?", "Mongolia and China"),
            ("What is the driest non-polar desert in the world?", "The Atacama Desert"),
            ("In which country is the Atacama Desert?", "Chile"),
            ("Near which imaginary line do most rainforests grow?", "The equator"),
        ],
    },
    {
        "key": "qzg_islands",
        "name": "The Islands and Archipelagos Quiz",
        "group": "Landforms and Mountains",
        "ladder_rank": 3, "ladder_tier": "foundations",
        "description": ("Ten questions about the islands of the world. Rank the largest islands, learn what "
                        "an archipelago is, and place Japan, Madagascar, Iceland, and Sicily on the map. A "
                        "foundations quiz of island geography, every answer fact-checked. Ten questions, "
                        "answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_FACTBOOK],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the largest island in the world?", "Greenland"),
            ("What is the second largest island in the world?", "New Guinea"),
            ("Which three countries share the island of Great Britain?", "England, Scotland, and Wales"),
            ("What is a chain or cluster of islands called?", "An archipelago"),
            ("Japan is an island nation in which ocean?", "The Pacific Ocean"),
            ("Which large island nation lies off the southeast coast of Africa?", "Madagascar"),
            ("The Hawaiian Islands are in which ocean?", "The Pacific Ocean"),
            ("What is the largest island in the Mediterranean Sea?", "Sicily"),
            ("Iceland sits in which ocean?", "The Atlantic Ocean"),
            ("Which island is also a continent?", "Australia"),
        ],
    },
    {
        "key": "qzg_lakes",
        "name": "The Lakes and Inland Seas Quiz",
        "group": "Rivers and Water",
        "ladder_rank": 4, "ladder_tier": "foundations",
        "description": ("Ten questions about the great lakes of the world. Find the largest lake, the deepest "
                        "lake, and the largest freshwater lake by surface area, and visit Baikal, Titicaca, "
                        "the Great Lakes, and the Dead Sea. A foundations quiz of still waters, all "
                        "fact-checked. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_BRITANNICA, CIT_GUINNESS],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the largest lake in the world by surface area?", "The Caspian Sea"),
            ("What is the deepest lake in the world?", "Lake Baikal"),
            ("What is the largest freshwater lake in the world by surface area?", "Lake Superior"),
            ("In which country is Lake Baikal?", "Russia"),
            ("Which lake is the highest large navigable lake in the world?", "Lake Titicaca"),
            ("On the border of which two countries does Lake Titicaca lie?", "Peru and Bolivia"),
            ("How many Great Lakes are there?", "Five"),
            ("On the border of which two countries are the Great Lakes?", "The United States and Canada"),
            ("What is the Dead Sea?", "A salt lake, the lowest point on the surface of the Earth"),
            ("What is the second deepest lake in the world?", "Lake Tanganyika"),
        ],
    },
    {
        "key": "qzg_us_states",
        "name": "The United States States and Capitals Quiz",
        "group": "Countries and Capitals",
        "ladder_rank": 4, "ladder_tier": "foundations",
        "description": ("Ten questions matching US states to their capitals. Sacramento is not Los Angeles and "
                        "Albany is not New York City: this quiz drills the capitals people mix up most, from "
                        "Texas to Alaska to Hawaii. Every capital is current and fact-checked. Ten questions, "
                        "ten points each, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the capital of California?", "Sacramento"),
            ("What is the capital of Texas?", "Austin"),
            ("What is the capital of New York?", "Albany"),
            ("What is the capital of Florida?", "Tallahassee"),
            ("What is the capital of Illinois?", "Springfield"),
            ("What is the capital of Colorado?", "Denver"),
            ("What is the capital of Arizona?", "Phoenix"),
            ("What is the capital of Washington?", "Olympia"),
            ("What is the capital of Alaska?", "Juneau"),
            ("What is the capital of Hawaii?", "Honolulu"),
        ],
    },
    {
        "key": "qzg_europe",
        "name": "The Europe Countries and Capitals Quiz",
        "group": "Countries and Capitals",
        "ladder_rank": 4, "ladder_tier": "foundations",
        "description": ("Ten questions matching European countries to their capitals. Tour the continent from "
                        "Paris to Lisbon, taking in Madrid, Rome, Berlin, Warsaw, Amsterdam, Stockholm, Oslo, "
                        "and Athens along the way. Every capital is current and fact-checked. Ten questions, "
                        "ten points each, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the capital of France?", "Paris"),
            ("What is the capital of Spain?", "Madrid"),
            ("What is the capital of Italy?", "Rome"),
            ("What is the capital of Germany?", "Berlin"),
            ("What is the capital of Poland?", "Warsaw"),
            ("What is the capital of the Netherlands?", "Amsterdam"),
            ("What is the capital of Sweden?", "Stockholm"),
            ("What is the capital of Norway?", "Oslo"),
            ("What is the capital of Greece?", "Athens"),
            ("What is the capital of Portugal?", "Lisbon"),
        ],
    },
    {
        "key": "qzg_asia",
        "name": "The Asia Countries and Capitals Quiz",
        "group": "Countries and Capitals",
        "ladder_rank": 4, "ladder_tier": "foundations",
        "description": ("Ten questions matching Asian countries to their capitals. Travel from Beijing to "
                        "Tokyo to New Delhi, then through Seoul, Bangkok, Jakarta, Manila, Hanoi, Islamabad, "
                        "and Dhaka. The largest continent holds some of the largest capitals on Earth. Ten "
                        "questions, ten points each, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the capital of China?", "Beijing"),
            ("What is the capital of Japan?", "Tokyo"),
            ("What is the capital of India?", "New Delhi"),
            ("What is the capital of South Korea?", "Seoul"),
            ("What is the capital of Thailand?", "Bangkok"),
            ("What is the capital of Indonesia?", "Jakarta"),
            ("What is the capital of the Philippines?", "Manila"),
            ("What is the capital of Vietnam?", "Hanoi"),
            ("What is the capital of Pakistan?", "Islamabad"),
            ("What is the capital of Bangladesh?", "Dhaka"),
        ],
    },
    {
        "key": "qzg_africa",
        "name": "The Africa Countries and Capitals Quiz",
        "group": "Countries and Capitals",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("Ten compounded questions matching African countries to their capitals. This rung of "
                        "the ladder moves past the easy set into Cairo, Abuja, Nairobi, Pretoria, Addis Ababa, "
                        "Accra, Rabat, Algiers, Dakar, and Dodoma. It also teaches the tricky cases: South "
                        "Africa has three capitals, and Tanzania moved its official capital. Ten questions, "
                        "answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the capital of Egypt?", "Cairo"),
            ("What is the capital of Nigeria?", "Abuja"),
            ("What is the capital of Kenya?", "Nairobi"),
            ("Which city is the administrative capital of South Africa?", "Pretoria"),
            ("What is the capital of Ethiopia?", "Addis Ababa"),
            ("What is the capital of Ghana?", "Accra"),
            ("What is the capital of Morocco?", "Rabat"),
            ("What is the capital of Algeria?", "Algiers"),
            ("What is the capital of Senegal?", "Dakar"),
            ("What is the official capital of Tanzania?", "Dodoma"),
        ],
    },
    {
        "key": "qzg_south_america",
        "name": "The South America Countries and Capitals Quiz",
        "group": "Countries and Capitals",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("Ten compounded questions matching South American countries to their capitals. From "
                        "Brasilia to Buenos Aires to Lima, through Bogota, Santiago, Caracas, Quito, La Paz, "
                        "Montevideo, and Asuncion. It teaches the tricky case of Bolivia, whose seat of "
                        "government sits in La Paz. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the capital of Brazil?", "Brasilia"),
            ("What is the capital of Argentina?", "Buenos Aires"),
            ("What is the capital of Peru?", "Lima"),
            ("What is the capital of Colombia?", "Bogota"),
            ("What is the capital of Chile?", "Santiago"),
            ("What is the capital of Venezuela?", "Caracas"),
            ("What is the capital of Ecuador?", "Quito"),
            ("Which city is the seat of government of Bolivia?", "La Paz"),
            ("What is the capital of Uruguay?", "Montevideo"),
            ("What is the capital of Paraguay?", "Asuncion"),
        ],
    },
    {
        "key": "qzg_volcanoes",
        "name": "The Volcanoes and Earthquakes Quiz",
        "group": "Climate and Earth",
        "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("Ten compounded questions about volcanoes and earthquakes. Meet Mauna Loa, Vesuvius, "
                        "Mount St. Helens, and the Ring of Fire, learn the difference between magma and lava, "
                        "and find out which earthquake was the largest ever recorded. Real events, "
                        "fact-checked. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_USGS, CIT_BRITANNICA, CIT_NOAA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is a volcano?", "An opening in the crust of the Earth where molten rock erupts"),
            ("What is the largest active volcano in the world?", "Mauna Loa"),
            ("In which US state is Mauna Loa?", "Hawaii"),
            ("Which volcano destroyed the Roman city of Pompeii in 79 AD?", "Mount Vesuvius"),
            ("Which volcano in Washington State erupted in 1980?", "Mount St. Helens"),
            ("What is the Ring of Fire?", "The zone around the Pacific Ocean with many volcanoes and earthquakes"),
            ("What was the largest earthquake ever recorded?", "The 1960 Valdivia earthquake in Chile, magnitude 9.5"),
            ("What scale is used to measure earthquake magnitude today?", "The moment magnitude scale"),
            ("What is the difference between magma and lava?", "Magma is molten rock underground; lava is molten rock that has reached the surface"),
            ("Which famous fault runs through California?", "The San Andreas Fault"),
        ],
    },
    {
        "key": "qzg_climate",
        "name": "The Climate Zones and Weather Quiz",
        "group": "Climate and Earth",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("Ten compounded questions about climate zones and weather. Learn what causes the "
                        "seasons, what a monsoon and a rain shadow are, where the wettest and driest places "
                        "on Earth sit, and which ocean current warms Western Europe. Real climate science in "
                        "plain words. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NOAA, CIT_BRITANNICA, CIT_NATGEO],
        "sig_lens": SIG_LENS,
        "qa": [
            ("Which climate zone is found along the equator?", "The tropical zone"),
            ("What is a monsoon?", "A seasonal wind that brings heavy rain, especially to South Asia"),
            ("What causes the seasons?", "The tilt of the Earth as it orbits the sun"),
            ("About how many degrees is the Earth tilted?", "About 23.5 degrees"),
            ("What is permafrost?", "Ground that stays frozen all year"),
            ("What is the tundra?", "A cold, treeless plain in the far north"),
            ("What is a rain shadow?", "Dry land on the sheltered side of a mountain range"),
            ("Which desert is the driest non-polar place on Earth?", "The Atacama Desert"),
            ("Which ocean current warms Western Europe?", "The Gulf Stream"),
            ("What is the wettest inhabited place on Earth?", "Mawsynram, India"),
        ],
    },
    {
        "key": "qzg_latlong",
        "name": "The Latitude, Longitude, and Time Zones Quiz",
        "group": "Maps and Navigation",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("Ten compounded questions about the grid lines of the Earth. Learn the equator, the "
                        "prime meridian, and the International Date Line, find which way latitude and "
                        "longitude run, and work out how many degrees make one hour of time. The math of the "
                        "map, taught plainly. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the equator?", "The imaginary line of 0 degrees latitude around the middle of the Earth"),
            ("What is the prime meridian?", "The line of 0 degrees longitude, running through Greenwich, England"),
            ("How many degrees of longitude equal one hour of time difference?", "15 degrees"),
            ("How many time zones does the world have?", "24"),
            ("What is the International Date Line?", "The 180th meridian, where the calendar day changes"),
            ("Do lines of latitude run east-west or north-south?", "East-west"),
            ("Do lines of longitude run east-west or north-south?", "North-south"),
            ("What are the tropics?", "The regions between the Tropic of Cancer and the Tropic of Capricorn"),
            ("Which circle marks the boundary of the Arctic region?", "The Arctic Circle"),
            ("If it is noon in London, what time is it in a place five hours ahead?", "5:00 PM"),
        ],
    },
    {
        "key": "qzg_polar",
        "name": "The Polar Regions Quiz",
        "group": "Climate and Earth",
        "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("Ten compounded questions about the Arctic and Antarctica. Learn which pole sits in an "
                        "ocean and which sits on a continent, meet penguins and polar bears, and discover "
                        "which desert is the largest in the world - it is not the one you expect. Ten "
                        "questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NOAA, CIT_NATGEO, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("Which pole is at the top of the globe?", "The North Pole"),
            ("The North Pole lies in which ocean?", "The Arctic Ocean"),
            ("The South Pole lies on which continent?", "Antarctica"),
            ("Which is colder, the Arctic or Antarctica?", "Antarctica"),
            ("Which flightless birds live in Antarctica?", "Penguins"),
            ("Which large bears live in the Arctic?", "Polar bears"),
            ("What is an iceberg?", "A large floating piece of freshwater ice broken from a glacier"),
            ("What is the midnight sun?", "The sun staying visible for 24 hours in summer near the poles"),
            ("What is the largest desert in the world?", "The Antarctic Polar Desert"),
            ("What is the aurora?", "Natural light displays in the sky near the poles"),
        ],
    },
    {
        "key": "qzg_landmarks",
        "name": "The Famous Landmarks Quiz",
        "group": "Places and Records",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "description": ("Ten compounded questions placing the most famous landmarks in the world. Stand the "
                        "Eiffel Tower in Paris, the Statue of Liberty in New York Harbor, the Great Wall in "
                        "China, and the Pyramids at Giza, and finish with Machu Picchu high in Peru. Ten "
                        "questions, ten points each, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_BRITANNICA, CIT_FACTBOOK],
        "sig_lens": SIG_LENS,
        "qa": [
            ("In which city is the Eiffel Tower?", "Paris"),
            ("In which harbor does the Statue of Liberty stand?", "New York Harbor"),
            ("In which country is the Great Wall?", "China"),
            ("Near which city are the Pyramids of Giza?", "Cairo"),
            ("In which Indian city is the Taj Mahal?", "Agra"),
            ("In which city is the Colosseum?", "Rome"),
            ("In which city is the Sydney Opera House?", "Sydney"),
            ("In which city does Christ the Redeemer stand?", "Rio de Janeiro"),
            ("In which country is Machu Picchu?", "Peru"),
            ("In which city is Big Ben?", "London"),
        ],
    },
    {
        "key": "qzg_rivers_americas",
        "name": "The Rivers of the Americas Quiz",
        "group": "Rivers and Water",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "description": ("Ten compounded questions about the rivers of North and South America. Follow the "
                        "Mississippi-Missouri system, the Colorado through the Grand Canyon, the Rio Grande "
                        "along the border, and the Amazon through the rainforest, and learn which river links "
                        "the Great Lakes to the sea. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_BRITANNICA, CIT_USGS],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the longest river system in North America?", "The Mississippi-Missouri"),
            ("Which river carved the Grand Canyon?", "The Colorado River"),
            ("Which river forms part of the border between the United States and Mexico?", "The Rio Grande"),
            ("What is the longest river in South America?", "The Amazon"),
            ("Which river connects the Great Lakes to the Atlantic Ocean?", "The St. Lawrence River"),
            ("Which river flows through Washington, D.C.?", "The Potomac River"),
            ("The Yukon River flows mainly through which US state and Canadian territory?", "Alaska and Yukon"),
            ("Which river flows mainly through Venezuela to the Atlantic?", "The Orinoco"),
            ("The Parana River flows through which three countries?", "Brazil, Paraguay, and Argentina"),
            ("Which river built the famous bird-foot delta in Louisiana?", "The Mississippi River"),
        ],
    },
    {
        "key": "qzg_rivers_africa_asia",
        "name": "The Rivers of Africa and Asia Quiz",
        "group": "Rivers and Water",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "description": ("Ten compounded questions about the rivers of Africa and Asia. Meet the Nile and the "
                        "deep Congo, the Zambezi and its great falls, the Yangtze and the six-country Mekong, "
                        "and the Tigris flowing through Baghdad. The old world rivers, fact-checked. Ten "
                        "questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the longest river in Africa?", "The Nile"),
            ("Which African river is the deepest river in the world?", "The Congo"),
            ("Which river feeds Victoria Falls?", "The Zambezi"),
            ("Through which region does the Niger River flow?", "West Africa"),
            ("What is the longest river in Asia?", "The Yangtze"),
            ("Which Asian river is also called the Chang Jiang?", "The Yangtze"),
            ("Through how many countries does the Mekong flow?", "Six"),
            ("Which river flows through Baghdad?", "The Tigris"),
            ("The Tigris and Euphrates flow through which modern country mainly?", "Iraq"),
            ("Which is the longest river flowing entirely within Russia?", "The Lena"),
        ],
    },
    {
        "key": "qzg_ocean_currents",
        "name": "The Ocean Currents and Tides Quiz",
        "group": "Rivers and Water",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "description": ("Ten compounded questions about ocean currents and tides. Learn what pulls the tides, "
                        "which currents warm Europe and cool South America, what El Nino does to world weather, "
                        "and how deep the deepest point in the ocean goes. The moving ocean, fact-checked. "
                        "Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NOAA, CIT_BRITANNICA, CIT_GUINNESS],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What causes the tides?", "The gravity of the moon and the sun"),
            ("How many high tides are there each day?", "Two"),
            ("Which warm current flows along the east coast of North America toward Europe?", "The Gulf Stream"),
            ("Which cold current flows along the west coast of South America?", "The Humboldt Current"),
            ("What is El Nino?", "A periodic warming of Pacific Ocean waters that changes weather worldwide"),
            ("Which ocean is the deepest on average?", "The Pacific Ocean"),
            ("What is the deepest point in the ocean?", "The Challenger Deep"),
            ("The Challenger Deep lies in which trench?", "The Mariana Trench"),
            ("About how deep is the Challenger Deep?", "About 10,900 metres"),
            ("What is a gyre?", "A large system of rotating ocean currents"),
        ],
    },
    {
        "key": "qzg_caves_canyons",
        "name": "The Caves, Canyons, and Natural Wonders Quiz",
        "group": "Landforms and Mountains",
        "ladder_rank": 7, "ladder_tier": "compounded",
        "description": ("Ten compounded questions about caves, canyons, and natural wonders. Descend into "
                        "Mammoth Cave, stand on the rim of the Grand Canyon, sail the Great Barrier Reef, "
                        "and learn what a fjord is and why Everest keeps growing. Wonders of the land and "
                        "sea, fact-checked. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_BRITANNICA, CIT_USGS],
        "sig_lens": SIG_LENS,
        "qa": [
            ("Which canyon was carved by the Colorado River?", "The Grand Canyon"),
            ("What is the longest cave system in the world?", "Mammoth Cave"),
            ("In which US state is Mammoth Cave?", "Kentucky"),
            ("Which natural wonder stretches 2,300 kilometres off the coast of Australia?", "The Great Barrier Reef"),
            ("What is a fjord?", "A long, narrow sea inlet between cliffs, carved by glaciers"),
            ("Which country is most famous for fjords?", "Norway"),
            ("Do stalactites hang from the ceiling or grow from the floor of a cave?", "They hang from the ceiling"),
            ("What is a canyon?", "A deep, narrow valley with steep sides, often carved by a river"),
            ("The Giants Causeway in Northern Ireland is made of what?", "Basalt columns"),
            ("Mount Everest grows a few millimetres taller each year because of what?", "Plate tectonics pushing India into Asia"),
        ],
    },
    {
        "key": "qzg_borders",
        "name": "The Country Borders and Enclaves Quiz",
        "group": "Places and Records",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("Ten advanced questions about country borders and enclaves. Find the longest land "
                        "border on Earth, the country entirely inside South Africa, the two states inside "
                        "Italy, and the town split between Belgium and the Netherlands. Borders get strange "
                        "at this rung of the ladder. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the longest land border in the world?", "The border between Canada and the United States"),
            ("About how long is the Canada-United States border?", "About 8,891 kilometres"),
            ("Which country lies entirely inside South Africa?", "Lesotho"),
            ("Which two tiny states are enclaves within Italy?", "San Marino and Vatican City"),
            ("What is an exclave?", "A part of a country separated from its main territory"),
            ("Which US state is separated from the rest by Canada?", "Alaska"),
            ("Which Russian region is an exclave between Poland and Lithuania?", "Kaliningrad"),
            ("The town of Baarle is split between which two countries?", "Belgium and the Netherlands"),
            ("Which two countries each share land borders with 14 neighbours?", "China and Russia"),
            ("Which country became independent from Sudan in 2011?", "South Sudan"),
        ],
    },
    {
        "key": "qzg_world_records",
        "name": "The Highest, Deepest, Longest Quiz",
        "group": "Places and Records",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("Ten advanced questions about the extremes of the Earth: the highest mountain, the "
                        "deepest ocean point, the longest river, the largest desert, the tallest waterfall, "
                        "the deepest lake, the hottest recorded place, and the coldest. The record book of "
                        "the planet, fact-checked. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_GUINNESS, CIT_NOAA, CIT_NATGEO, CIT_USGS],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the highest mountain in the world, and about how high is it?", "Mount Everest, about 8,848 metres"),
            ("What is the deepest point in the ocean?", "The Challenger Deep, about 10,900 metres deep"),
            ("Which river is traditionally listed as the longest in the world?", "The Nile"),
            ("What is the largest desert in the world?", "The Antarctic Polar Desert"),
            ("What is the tallest waterfall in the world?", "Angel Falls"),
            ("In which country is Angel Falls?", "Venezuela"),
            ("What is the deepest lake in the world?", "Lake Baikal"),
            ("What is the largest island in the world?", "Greenland"),
            ("Which place holds the record for the hottest air temperature ever recorded?", "Death Valley, California"),
            ("Which station recorded the coldest temperature ever on Earth?", "Vostok Station in Antarctica"),
        ],
    },
    {
        "key": "qzg_cities",
        "name": "The Population and Biggest Cities Quiz",
        "group": "Places and Records",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("Ten advanced questions about people and the biggest cities. Name the most populous "
                        "countries on Earth, find the largest metropolitan city, stand in the city on two "
                        "continents, and learn which country holds the most islands. Human geography at the "
                        "advanced rung. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_UN, CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the most populous country in the world?", "India"),
            ("What is the second most populous country in the world?", "China"),
            ("Which city has the largest metropolitan population in the world?", "Tokyo"),
            ("What is the most populous city in Africa?", "Cairo"),
            ("What is the most populous country in South America?", "Brazil"),
            ("Which city sits on two continents, Europe and Asia?", "Istanbul"),
            ("What is the most populous country in North America?", "The United States"),
            ("What is a megacity?", "A city with more than 10 million people"),
            ("Which country has the most islands in the world?", "Sweden"),
            ("About how many islands does Sweden have?", "About 221,800"),
        ],
    },
    {
        "key": "qzg_europe_rivers",
        "name": "The European Rivers Quiz",
        "group": "Rivers and Water",
        "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("Ten advanced questions about the rivers of Europe. Follow the Volga, the Seine, the "
                        "Thames, the Rhine, the Danube through four capitals, the Tiber, the Douro, and the "
                        "Neva, and learn which seas they reach. The rivers that built European cities, "
                        "fact-checked. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the longest river in Europe?", "The Volga"),
            ("Which river flows through Paris?", "The Seine"),
            ("Which river flows through London?", "The Thames"),
            ("Into which sea does the Danube flow?", "The Black Sea"),
            ("Which river forms much of the border between France and Germany?", "The Rhine"),
            ("Into which sea does the Rhine flow?", "The North Sea"),
            ("Which river flows through Rome?", "The Tiber"),
            ("Which river flows through Vienna, Budapest, and Belgrade?", "The Danube"),
            ("The Douro River flows through which two countries?", "Spain and Portugal"),
            ("Which river flows through St. Petersburg?", "The Neva"),
        ],
    },
    {
        "key": "qzg_map_projections",
        "name": "The Map Projections and Scale Quiz",
        "group": "Maps and Navigation",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("Ten advanced questions about map projections and scale. Learn why every flat map of "
                        "the round Earth must distort something, what Mercator did for sailors in 1569, how "
                        "to read a 1:50,000 scale, and what contour lines tell a hiker. The craft behind the "
                        "map. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_BRITANNICA, CIT_USGS],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is a map projection?", "A way of showing the curved surface of the Earth on a flat map"),
            ("Which projection was made for sailors in 1569?", "The Mercator projection"),
            ("What does the Mercator projection distort?", "The sizes of lands near the poles"),
            ("What is map scale?", "The ratio between a distance on the map and the real distance"),
            ("On a 1:50,000 map, what real distance does 1 centimetre represent?", "500 metres"),
            ("What is a topographic map?", "A map that shows elevation with contour lines"),
            ("What are contour lines?", "Lines joining points of equal elevation"),
            ("What advantage does a globe have over a flat map?", "True shapes, sizes, and distances"),
            ("What does GPS stand for?", "Global Positioning System"),
            ("Which projection has been used for many world wall maps since 1998?", "The Winkel Tripel projection"),
        ],
    },
    {
        "key": "qzg_tectonics",
        "name": "The Plate Tectonics Quiz",
        "group": "Climate and Earth",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("Ten advanced questions about plate tectonics, the engine that moves the Earth. Meet "
                        "Alfred Wegener and his drifting continents, the giant Pacific Plate, the Mid-Atlantic "
                        "Ridge, and the subduction zones that ring the Pacific with fire. Learn why the "
                        "Himalayas are still growing. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_USGS, CIT_BRITANNICA, CIT_NOAA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("Who proposed the theory of continental drift in 1912?", "Alfred Wegener"),
            ("What is a tectonic plate?", "A massive slab of the rocky outer layer of the Earth"),
            ("Which is the largest tectonic plate?", "The Pacific Plate"),
            ("What is the Mid-Atlantic Ridge?", "An underwater mountain range where plates are spreading apart"),
            ("What was the ancient supercontinent called?", "Pangaea"),
            ("Which two plates meet at the San Andreas Fault?", "The Pacific Plate and the North American Plate"),
            ("What happens at a subduction zone?", "One plate slides beneath another"),
            ("The Himalayas are still growing because which plates are colliding?", "The Indian Plate and the Eurasian Plate"),
            ("What causes the Ring of Fire around the Pacific?", "Subduction zones around the Pacific Plate"),
            ("About how fast do tectonic plates move?", "A few centimetres per year"),
        ],
    },
    {
        "key": "qzg_waterfalls",
        "name": "The Waterfalls, Rapids, and Deltas Quiz",
        "group": "Rivers and Water",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("Ten advanced questions about waterfalls, rapids, and deltas. Stand beneath Angel "
                        "Falls, Niagara, Victoria Falls, and Iguazu, and learn what a delta is and where the "
                        "Nile builds one. Falling water and the lands it makes, fact-checked. Ten questions, "
                        "answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_BRITANNICA, CIT_GUINNESS],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the tallest waterfall in the world?", "Angel Falls"),
            ("About how tall is Angel Falls?", "About 979 metres"),
            ("Which falls lie on the border between the United States and Canada?", "Niagara Falls"),
            ("Victoria Falls lies on the border of which two countries?", "Zambia and Zimbabwe"),
            ("Which river feeds Victoria Falls?", "The Zambezi"),
            ("Iguazu Falls lie on the border of which two countries?", "Argentina and Brazil"),
            ("What is a delta?", "Land formed where a river deposits sediment at its mouth"),
            ("The Nile Delta is in which country?", "Egypt"),
            ("What is a rapid?", "A fast, turbulent section of a river"),
            ("Which river forms Iguazu Falls?", "The Iguazu River"),
        ],
    },
    {
        "key": "qzg_central_asia",
        "name": "The Central Asia and Caucasus Quiz",
        "group": "Countries and Capitals",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("Ten advanced questions about Central Asia and the Caucasus. Name the largest "
                        "landlocked country on Earth, match the five stans to their capitals, and place "
                        "Tbilisi, Yerevan, and Baku on the map. The crossroads of Asia at the advanced rung. "
                        "Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the largest landlocked country in the world?", "Kazakhstan"),
            ("What is the capital of Kazakhstan?", "Astana"),
            ("What is the capital of Uzbekistan?", "Tashkent"),
            ("What is the capital of Turkmenistan?", "Ashgabat"),
            ("What is the capital of Kyrgyzstan?", "Bishkek"),
            ("What is the capital of Tajikistan?", "Dushanbe"),
            ("Which three countries make up the Caucasus?", "Georgia, Armenia, and Azerbaijan"),
            ("What is the capital of Georgia?", "Tbilisi"),
            ("What is the capital of Armenia?", "Yerevan"),
            ("What is the capital of Azerbaijan?", "Baku"),
        ],
    },
    {
        "key": "qzg_middle_east",
        "name": "The Middle East Geography Quiz",
        "group": "Countries and Capitals",
        "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("Ten advanced questions matching Middle Eastern countries to their capitals. From "
                        "Riyadh to Baghdad to Tehran, through Ankara, Abu Dhabi, Doha, Amman, Beirut, Muscat, "
                        "and Sanaa. The capitals of a region everyone hears about and few can place. Ten "
                        "questions, ten points each, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_BRITANNICA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the capital of Saudi Arabia?", "Riyadh"),
            ("What is the capital of Iraq?", "Baghdad"),
            ("What is the capital of Iran?", "Tehran"),
            ("What is the capital of Turkey?", "Ankara"),
            ("What is the capital of the United Arab Emirates?", "Abu Dhabi"),
            ("What is the capital of Qatar?", "Doha"),
            ("What is the capital of Jordan?", "Amman"),
            ("What is the capital of Lebanon?", "Beirut"),
            ("What is the capital of Oman?", "Muscat"),
            ("What is the capital of Yemen?", "Sanaa"),
        ],
    },
    {
        "key": "qzg_island_nations",
        "name": "The Island Nations Quiz",
        "group": "Places and Records",
        "ladder_rank": 10, "ladder_tier": "advanced",
        "description": ("Ten advanced questions about the island nations of the world. Find the largest "
                        "archipelago nation, the lowest country on Earth, the capitals of Japan, the "
                        "Philippines, New Zealand, and Iceland, and the Caribbean nation sharing its island. "
                        "Nations surrounded by sea, fact-checked. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_NATGEO],
        "sig_lens": SIG_LENS,
        "qa": [
            ("What is the largest archipelago nation in the world?", "Indonesia"),
            ("What is the capital of Japan?", "Tokyo"),
            ("Which island nation is the lowest country in the world?", "The Maldives"),
            ("What is the capital of the Philippines?", "Manila"),
            ("Which country is made up mainly of two islands, North Island and South Island?", "New Zealand"),
            ("What is the capital of New Zealand?", "Wellington"),
            ("Which Caribbean nation shares its island with the Dominican Republic?", "Haiti"),
            ("What is the capital of Iceland?", "Reykjavik"),
            ("Which island nation lies off the southeast coast of Africa?", "Madagascar"),
            ("The Bahamas lie in which ocean?", "The Atlantic Ocean"),
        ],
    },
    {
        "key": "qzg_border_trivia",
        "name": "The Unusual Borders and Geography Trivia Quiz",
        "group": "Places and Records",
        "ladder_rank": 10, "ladder_tier": "advanced",
        "description": ("Ten advanced questions of unusual borders and geography trivia. Find the country named "
                        "for the equator, the island split between two nations, the longest coastline on "
                        "Earth, the sea with no coasts, and the canals that join the oceans. The strangest "
                        "true facts of the map. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_FACTBOOK, CIT_BRITANNICA, CIT_NOAA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("Which country is named after the equator?", "Ecuador"),
            ("Which two countries share the island of New Guinea?", "Indonesia and Papua New Guinea"),
            ("Which country has the longest coastline in the world?", "Canada"),
            ("What is the largest hot desert in Asia?", "The Arabian Desert"),
            ("Which strait separates Spain from Morocco?", "The Strait of Gibraltar"),
            ("Which canal connects the Atlantic and Pacific Oceans?", "The Panama Canal"),
            ("Which canal connects the Mediterranean Sea and the Red Sea?", "The Suez Canal"),
            ("Which country is both a continent and a country?", "Australia"),
            ("Which sea has no coasts at all?", "The Sargasso Sea"),
            ("Which is the smallest country in the world?", "Vatican City"),
        ],
    },
    {
        "key": "qzg_grand_challenge",
        "name": "The Grand Geography Challenge Quiz",
        "group": "Places and Records",
        "ladder_rank": 10, "ladder_tier": "advanced",
        "description": ("The final rung of the ladder: ten hard questions drawn from everything the thirty-three "
                        "quizzes before it taught. The continent with no mainland volcanoes, the country with "
                        "the most time zones, the busiest strait on Earth, the oldest desert, the roof of the "
                        "world, and the deepest lake in Africa. Score seventy or more and you have mastered "
                        "the database. Ten questions, answers at the bottom."),
        "key_points": KP, "requirements": REQ, "standards": STD,
        "citations": [CIT_NATGEO, CIT_FACTBOOK, CIT_GUINNESS, CIT_NOAA],
        "sig_lens": SIG_LENS,
        "qa": [
            ("Which continent has no active volcanoes on its mainland?", "Australia"),
            ("Which country has the most time zones?", "France"),
            ("Which is the busiest shipping strait in the world?", "The Strait of Malacca"),
            ("Which desert covers parts of Mongolia and China?", "The Gobi Desert"),
            ("What is the roof of the world?", "The Tibetan Plateau"),
            ("Which country is the flattest in the world?", "The Maldives"),
            ("What is the oldest desert in the world?", "The Namib Desert"),
            ("Which country has the most natural lakes in the world?", "Canada"),
            ("What is the largest lake in Africa?", "Lake Victoria"),
            ("What is the highest mountain in South America?", "Aconcagua"),
        ],
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
for e in ENTRIES:
    assert len(e["qa"]) == 10, "quiz %s does not hold 10 questions" % e["key"]
    assert len(e["description"]) > 200, "short description in %s" % e["key"]
ranks = [e["ladder_rank"] for e in ENTRIES]
assert ranks == sorted(ranks), "entries not in ladder order"
assert all(1 <= r <= 10 for r in ranks)
tiers = [e["ladder_tier"] for e in ENTRIES]
assert set(tiers) <= {"foundations", "compounded", "advanced"}
