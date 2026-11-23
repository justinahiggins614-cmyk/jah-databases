// Demo runner: node demo.js prints the generated record for seed 1.
// Seeded boundless generator for the Search engines — Top Websites Directory
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-similarweb-top100-directory.js [seed]  (prints one
// JSON record) or: node gen-similarweb-top100-directory.js --test (runTests).
// Live; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "similarweb-top100-directory";
const RECORD_KIND = "similarweb top100 directory record";
const ID_PREFIX = "JAH-SWTD-";
const AI_NAME = "JAH Top Websites Directory Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \\u2014 not stored files.";

const TOPICS = [
  {
    "title": "Search engines — Top Websites Directory",
    "subject": "search engines directory entry",
    "description": "A search engine is a service that takes words a person types and returns a list of pages, pictures, videos, or answers that match those words. The person types a question or a few words, the engine looks through an index, which is a giant list of pages it has already read, and shows the best matches first, usually ten to a page, with a short piece of each page so the person can judge before clicking. Modern search engines also answer simple questions directly, show maps, pictures, news, and shopping results, correct spelling, and work in many languages. The ranked sites in this category are: r",
    "label": "search-engines-directory-entry",
    "figures": {
      "category_index": 1,
      "sites": 8,
      "top_rank": 1,
      "last_rank": 73,
      "rank_sum": 229,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "AI assistants — Top Websites Directory",
    "subject": "ai assistants directory entry",
    "description": "An AI assistant is a program a person talks to in plain words, by typing or speaking, which answers questions, writes drafts, explains ideas, works through problems step by step, and follows a conversation across many turns, remembering what was said earlier in the same talk. It does not fetch a page and stop; it writes a fresh answer for each question, using patterns learned from a very large amount of text, and it can be asked to try again, to be shorter, or to explain like a teacher. The ranked sites in this category are: rank 5 — ChatGPT (AI assistant); rank 15 — Google Gemini (AI assistan",
    "label": "ai-assistants-directory-entry",
    "figures": {
      "category_index": 2,
      "sites": 5,
      "top_rank": 5,
      "last_rank": 93,
      "rank_sum": 223,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Social networks — Top Websites Directory",
    "subject": "social networks directory entry",
    "description": "A social network is a service where a person keeps a profile, which is a page about themselves, follows other people, groups, and pages, and sees a feed, which is a running list of posts, pictures, short videos, and links chosen for them. People post their own updates, comment on others, share links, join groups about a shared interest, and send private messages. The feed is the centre of the service: it decides what each person sees, in what order, and how often. The ranked sites in this category are: rank 3 — Facebook (Social networking); rank 4 — Instagram (Photos and social media); rank 6 ",
    "label": "social-networks-directory-entry",
    "figures": {
      "category_index": 3,
      "sites": 11,
      "top_rank": 3,
      "last_rank": 89,
      "rank_sum": 366,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Video and entertainment — Top Websites Directory",
    "subject": "video and entertainment directory entry",
    "description": "Video and entertainment services let a person watch moving pictures with sound: long videos, short clips, live streams, films, series, and music videos, played on demand, which means the viewer chooses what to play and when, instead of waiting for a broadcast time. Most offer a search box, lists of what is popular, channels or creators to follow, and suggestions for what to watch next. Music streaming, which plays songs on demand from a large catalogue, belongs to the same family. The ranked sites in this category are: rank 2 — YouTube (Videos); rank 7 — TikTok (Short videos); rank 22 — Netfli",
    "label": "video-and-entertainment-directory-entry",
    "figures": {
      "category_index": 4,
      "sites": 13,
      "top_rank": 2,
      "last_rank": 96,
      "rank_sum": 708,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Shopping and marketplaces — Top Websites Directory",
    "subject": "shopping and marketplaces directory entry",
    "description": "A shopping service lets a person find a product, read its description and price, compare it with similar products, put it in a basket, pay, and have it delivered. A marketplace is a shopping service where many different sellers list their goods side by side, so the same kind of product can come from dozens of sellers at different prices. Reviews from past buyers, delivery times, and return rules are part of the service, because a buyer cannot touch the product before paying. The ranked sites in this category are: rank 13 — Amazon (Shopping); rank 30 — Temu (Shopping); rank 40 — Samsung (Electr",
    "label": "shopping-and-marketplaces-directory-entry",
    "figures": {
      "category_index": 5,
      "sites": 15,
      "top_rank": 13,
      "last_rank": 92,
      "rank_sum": 885,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "News and information — Top Websites Directory",
    "subject": "news and information directory entry",
    "description": "A news service reports what has happened, as it happens: headlines, full stories, pictures, video, live updates, and explainers that give the background a reader needs to understand a story. Portals, which are front pages that gather news, weather, mail, and search in one place, belong to the same family. A good news service separates what happened from what someone thinks about it, names its sources, and corrects itself when it gets something wrong. The ranked sites in this category are: rank 12 — Yahoo Japan (News and portal); rank 16 — Yahoo (News and email); rank 31 — Dzen (Media and conte",
    "label": "news-and-information-directory-entry",
    "figures": {
      "category_index": 6,
      "sites": 12,
      "top_rank": 12,
      "last_rank": 99,
      "rank_sum": 621,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Education and research — Top Websites Directory",
    "subject": "education and research directory entry",
    "description": "Education and research services help a person learn: taught courses with lessons and tests, classroom tools that teachers use to set work and mark it, libraries of books and papers to read, and reference works that explain a subject. A course platform organises learning into steps, checks understanding with questions, and keeps a record of progress. A library, in the plain sense, is a collection of books and papers kept so they can be found and read again. The ranked sites in this category are: rank 60 — Instructure (Education technology). The live Signature Library mirror covers this service ",
    "label": "education-and-research-directory-entry",
    "figures": {
      "category_index": 7,
      "sites": 1,
      "top_rank": 60,
      "last_rank": 60,
      "rank_sum": 60,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Business and productivity — Top Websites Directory",
    "subject": "business and productivity directory entry",
    "description": "Business and productivity services are the tools of office work: writing documents, building tables of numbers, making slides, keeping a calendar, holding a video meeting, and sharing files with co-workers. A video meeting service lets people in different places see and hear each other live, share a screen, and record the call. An office suite gathers the writing, numbers, slides, and mail tools into one place, so work done in one tool can be opened in another. The ranked sites in this category are: rank 18 — Microsoft (Software and services); rank 29 — Microsoft (Technology); rank 68 — Micros",
    "label": "business-and-productivity-directory-entry",
    "figures": {
      "category_index": 8,
      "sites": 3,
      "top_rank": 18,
      "last_rank": 68,
      "rank_sum": 115,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Software and developer platforms — Top Websites Directory",
    "subject": "software and developer platforms directory entry",
    "description": "A developer platform is a service where programmers keep their code, share it, and work on it together. Code is stored in a repository, which is a folder with a memory: every change is recorded, with who made it and why, so an old version can be brought back. Programmers propose changes, review each other's work, report problems, and run automatic checks that test the code before it is accepted. Public repositories let anyone read the code and learn from it. The ranked sites in this category are: rank 39 — GitHub (Software development). No live JAH mirror covers this service category yet. This",
    "label": "software-and-developer-platforms-directory-entry",
    "figures": {
      "category_index": 9,
      "sites": 1,
      "top_rank": 39,
      "last_rank": 39,
      "rank_sum": 39,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Communication and messaging — Top Websites Directory",
    "subject": "communication and messaging directory entry",
    "description": "Communication and messaging services carry words between people: instant messages that arrive in seconds, email that waits in an inbox until it is read, group chats for a team or a family, voice calls, and video calls. Email is the oldest of these: a message with an address, a subject, and a body, sent from one mailbox to another. Instant messaging is faster and more casual, with pictures, voice notes, and stickers, and group chats let many people talk in one place. The ranked sites in this category are: rank 8 — WhatsApp (Messaging); rank 23 — Microsoft Live (Email and Microsoft services); ra",
    "label": "communication-and-messaging-directory-entry",
    "figures": {
      "category_index": 10,
      "sites": 8,
      "top_rank": 8,
      "last_rank": 98,
      "rank_sum": 400,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Finance and payments — Top Websites Directory",
    "subject": "finance and payments directory entry",
    "description": "A finance and payments service moves money: paying for a purchase, sending money to another person, keeping a balance, and checking what was spent. A payment service sits between a buyer and a seller, takes the money from one side, and passes it to the other, keeping a record both sides can check. Some also hold a balance like a wallet, convert one currency to another, or protect a buyer when a purchase goes wrong. The ranked sites in this category are: rank 72 — PayPal (Payments). No live JAH mirror covers this service category yet. This record is a public record: it catalogues the ranking as",
    "label": "finance-and-payments-directory-entry",
    "figures": {
      "category_index": 11,
      "sites": 1,
      "top_rank": 72,
      "last_rank": 72,
      "rank_sum": 72,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Travel and transportation — Top Websites Directory",
    "subject": "travel and transportation directory entry",
    "description": "Travel services help a person go somewhere: find a place to stay, book a room, compare prices, check a route, and see how long a journey will take. A booking service lists rooms, flats, and hotels with pictures, prices, and reviews, and holds the booking. A map service shows places on a map, gives directions, and estimates travel time. Together they cover the whole journey, from choosing a place to arriving at the door. The ranked sites in this category are: rank 63 — Booking.com (Travel and hotels). The live Signature Maps mirror covers this service category: https://justinahiggins614-cmyk.gi",
    "label": "travel-and-transportation-directory-entry",
    "figures": {
      "category_index": 12,
      "sites": 1,
      "top_rank": 63,
      "last_rank": 63,
      "rank_sum": 63,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Health and wellness — Top Websites Directory",
    "subject": "health and wellness directory entry",
    "description": "Health and wellness services help a person look after their body and mind: tracking steps, sleep, and exercise, recording food, following a workout, checking symptoms against plain information, or booking an appointment. A tracker counts what can be counted and shows the pattern over days and weeks. A health information service explains a condition in plain words, with what is known and what is not, and when to see a clinician. No site in the October 2026 top 100 falls in this category. The category record is built as a service category with no ranked sites to list, so that the directory still",
    "label": "health-and-wellness-directory-entry",
    "figures": {
      "category_index": 13,
      "sites": 0,
      "top_rank": 0,
      "last_rank": 0,
      "rank_sum": 0,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Gaming and virtual worlds — Top Websites Directory",
    "subject": "gaming and virtual worlds directory entry",
    "description": "A game service lets a person play: video games that run in a browser or on a device, shared worlds where many players meet as characters, and arcades, which are collections of small games that can be started at once. A virtual world is a shared place made of software: people walk, build, talk, and play inside it, and what one person builds can be seen by others. Games keep score, save progress, and let players play together or against each other. The ranked sites in this category are: rank 61 — Roblox (Games and virtual worlds). The live Signature Arcade mirror covers this service category: ht",
    "label": "gaming-and-virtual-worlds-directory-entry",
    "figures": {
      "category_index": 14,
      "sites": 1,
      "top_rank": 61,
      "last_rank": 61,
      "rank_sum": 61,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Weather and utilities — Top Websites Directory",
    "subject": "weather and utilities directory entry",
    "description": "A weather service tells a person what the sky will do: the temperature now, rain, wind, and what is expected hour by hour and day by day, for a named place. Utilities, in the plain sense, are small helpful services: a clock, a calculator, a unit converter, a map of a postcode, a postal tracker, or a status page that says whether a service is working. They are the small tools a person reaches for without thinking. The ranked sites in this category are: rank 36 — Weather.com (Weather). The live Signature Weather mirror covers this service category: https://justinahiggins614-cmyk.github.io/jah-da",
    "label": "weather-and-utilities-directory-entry",
    "figures": {
      "category_index": 15,
      "sites": 1,
      "top_rank": 36,
      "last_rank": 36,
      "rank_sum": 36,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Government and public services — Top Websites Directory",
    "subject": "government and public services directory entry",
    "description": "A government and public service site is the front door of a public body on the web: a postal service that carries letters and parcels, a tax office, a driving licence office, a passport office, or a local council. A postal service tracks a parcel from posting to delivery, sells stamps, finds a post office, and holds mail. These services exist because the law says they must, and they must serve everyone, including people with slow connections and old devices. The ranked sites in this category are: rank 84 — USPS (Postal services). No live JAH mirror covers this service category yet. This record",
    "label": "government-and-public-services-directory-entry",
    "figures": {
      "category_index": 16,
      "sites": 1,
      "top_rank": 84,
      "last_rank": 84,
      "rank_sum": 84,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Real estate — Top Websites Directory",
    "subject": "real estate directory entry",
    "description": "A real estate service lists places to live and work: houses and flats for sale or for rent, with pictures, a price, the number of rooms, the size, and a map showing where the place is. A searcher sets a place, a price range, and the number of rooms, and the service returns the listings that match. Price history, an estimate of what a place is worth, and the cost of a loan are often shown beside the listing, because the price is only part of the decision. The ranked sites in this category are: rank 97 — Zillow (Real estate). No live JAH mirror covers this service category yet. This record is a ",
    "label": "real-estate-directory-entry",
    "figures": {
      "category_index": 17,
      "sites": 1,
      "top_rank": 97,
      "last_rank": 97,
      "rank_sum": 97,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Jobs and careers — Top Websites Directory",
    "subject": "jobs and careers directory entry",
    "description": "A jobs service lists work that is open: a job title, what the work involves, where it is, what it pays, and how to apply. A job seeker searches by words, place, and pay, saves the jobs that fit, and sends an application, usually a short letter and a record of past work. Some services also show what employers pay for the same work elsewhere, and what skills a job asks for, so a seeker can judge whether to apply. The ranked sites in this category are: rank 76 — Indeed (Jobs). No live JAH mirror covers this service category yet. This record is a public record: it catalogues the ranking as publish",
    "label": "jobs-and-careers-directory-entry",
    "figures": {
      "category_index": 18,
      "sites": 1,
      "top_rank": 76,
      "last_rank": 76,
      "rank_sum": 76,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Creative tools — Top Websites Directory",
    "subject": "creative tools directory entry",
    "description": "A creative tool is a service that helps a person make something: design a poster, edit a picture, lay out a page, cut a video, or draw. A design tool gives ready-made shapes, pictures, and lettering that a person arranges on a page, and lets the finished work be downloaded or printed. A picture editor changes brightness, crops, removes parts, and adds text. The best of them need no training: a person can make something presentable in minutes. The ranked sites in this category are: rank 33 — Canva (Graphic design); rank 78 — Adobe (Creative software). No live JAH mirror covers this service cate",
    "label": "creative-tools-directory-entry",
    "figures": {
      "category_index": 19,
      "sites": 2,
      "top_rank": 33,
      "last_rank": 78,
      "rank_sum": 111,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "Reference and knowledge — Top Websites Directory",
    "subject": "reference and knowledge directory entry",
    "description": "A reference service answers a plain question with a checked answer: an encyclopedia article that explains a subject, a dictionary entry that defines a word, or a knowledge page that gathers what is known about a topic in one place. An encyclopedia is a collection of articles, each about one subject, written to explain rather than to persuade, with links to related articles so a reader can follow a subject as far as they want. The ranked sites in this category are: rank 11 — Wikipedia (Encyclopedia); rank 100 — Namu Wiki (Encyclopedia). The live Signature Encyclopedia mirror covers this service",
    "label": "reference-and-knowledge-directory-entry",
    "figures": {
      "category_index": 20,
      "sites": 2,
      "top_rank": 11,
      "last_rank": 100,
      "rank_sum": 111,
      "records_per_edition": 24,
      "pair_records": 48,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "How to Use This Directory",
    "subject": "how to use overview",
    "description": "This directory is a guide to the most-visited kinds of website in the world, organised by what each kind of service does, not by which company runs it. Each of the twenty categories has one record. A record first says what the service is, in plain words, then how it grew, who uses it, and where it can mislead, then gives the numbers that prove the entry: how many of the ranked sites fall in the category, which ranks they hold, and whether a live JAH mirror already covers the service. A reader who wants the fastest answer should read the description and the answer; a reader who wants the proof ",
    "label": "how-to-use-overview",
    "figures": {
      "categories": 20,
      "ladder_ranks": 3,
      "mirrors": 12,
      "pair_records": 48,
      "ranked_sites": 88,
      "records_per_edition": 24,
      "sections": 16,
      "sources_per_record": 3
    }
  },
  {
    "title": "How the October 2026 Ranking Was Made",
    "subject": "ranking method overview",
    "description": "The ranking this directory records counts estimated visits in a web browser. A visit is one person opening a website in a browser and looking at it; the same person coming back later counts again. The measurement covers the whole world and one month, October 2026, and it was published on November 10, 2026. It counts browser visits only. It does not count people, it does not count activity inside phone apps, and it does not count time spent. A service that most people use inside an app will look smaller in this ranking than it really is, and a service people visit in a browser will look larger.",
    "label": "ranking-method-overview",
    "figures": {
      "categories": 20,
      "month": 10,
      "omitted_ranks": 12,
      "published_day": 10,
      "ranked_sites": 88,
      "records_per_edition": 24,
      "sections": 16,
      "year": 2026
    }
  },
  {
    "title": "The Twelve Live Mirrors and What They Cover",
    "subject": "mirror map overview",
    "description": "The network already runs twelve live mirrors, each a Signature version of a kind of service: search, encyclopedia, news, video, maps, shop, weather, mail, social, tunes, arcade, and library. A mirror is a working service built on the network's own data, with the same job as the kind of service it mirrors, but with its own name, its own catalogue, and no account needed. This record maps each mirror to the directory categories it covers, states plainly where a mirror covers only part of a category, and lists the nine categories no live mirror covers yet. Eight categories are fully covered, three",
    "label": "mirror-map-overview",
    "figures": {
      "categories": 20,
      "categories_covered": 8,
      "categories_partial": 3,
      "categories_uncovered": 9,
      "mirrors": 12,
      "records_per_edition": 24,
      "sections": 16
    }
  },
  {
    "title": "Omitted Ranks, Duplicates, and What Is Not in This Directory",
    "subject": "omissions overview",
    "description": "This record states, in one place, everything this directory leaves out, so no reader mistakes an absence for an oversight. Twelve ranks are omitted because they are adult-content sites: ranks 26, 27, 35, 38, 45, 54, 65, 70, 77, 79, 87, and 90. Two listings are duplicates inside the source ranking itself: one service appears twice, at ranks 18 and 29, and another at ranks 49 and 81. Each is counted once, under its first rank, and the second listing is marked NOT BUILT with the reason. One category, health and wellness, has no ranked site at all, and its record is built as a service category wit",
    "label": "omissions-overview",
    "figures": {
      "categories": 20,
      "duplicate_listings": 2,
      "omitted_ranks": 12,
      "pair_records": 48,
      "ranked_sites": 88,
      "records_per_edition": 24,
      "sections": 16
    }
  }
];

const SOURCES = [
  {
    "name": "Similarweb October 2026 Top 100 Most Visited Websites",
    "url": "https://www.similarweb.com/blog/research/market-research/most-visited-websites/",
    "establishes": "The October 2026 global ranking this record catalogues: rank, site, and main use, published November 10, 2026; estimated browser visits, not app activity.",
    "retrieved": "2026-11-18",
    "resource_id": "similarweb.com/blog/research/market-research/most-visited-websites"
  },
  {
    "name": "Signature Search",
    "url": "https://justinahiggins614-cmyk.github.io/jah-databases/mirrors/search/index.html",
    "establishes": "The live JAH mirror that covers this service category.",
    "retrieved": "2026-11-18",
    "resource_id": "justinahiggins614-cmyk.github.io/jah-databases/mirrors/search"
  },
  {
    "name": "The Merica-L Boundless Ecosystem OS",
    "url": "https://justinahiggins614-cmyk.github.io/jah-databases/the-merica-l-boundless-ecosystem-os.html",
    "establishes": "The main page of the network, listing all live websites and the accessible mirror.",
    "retrieved": "2026-11-18",
    "resource_id": "justinahiggins614-cmyk.github.io/jah-databases/the-merica-l-boundless-ecosystem-os.html"
  }
];

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function canonical(obj) {
  if (obj === null || typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) return "[" + obj.map(canonical).join(",") + "]";
  const keys = Object.keys(obj).sort();
  return "{" + keys.map((k) => JSON.stringify(k) + ":" + canonical(obj[k])).join(",") + "}";
}

function buildDemo(topic, label) {
  const figs = topic.figures;
  const keys = Object.keys(figs).sort();
  const total = keys.reduce((s, k) => s + figs[k], 0);
  const out = { count: keys.length, label: label, max: Math.max(...keys.map((k) => figs[k])), min: Math.min(...keys.map((k) => figs[k])), total: total };
  const result = Object.keys(out).sort().map((k) => k + "=" + out[k]).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\nLABEL = " + JSON.stringify(label) + "\n";
  const code = "import hashlib\n" + figsPy +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), \"min\": min(FIGURES.values()), \"total\": total}\n" +
    "    return out\n" +
    "outputs = compute()\n" +
    "result = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs.items()))\n" +
    "h1 = hashlib.sha256(result.encode()).hexdigest()\n" +
    "outputs2 = compute()\n" +
    "result2 = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs2.items()))\n" +
    "h2 = hashlib.sha256(result2.encode()).hexdigest()\n" +
    "for k, v in sorted(outputs.items()):\n" +
    "    print(f\"{k}: {v}\")\n" +
    "print(f\"Result: {result}\")\n" +
    "print(f\"Run 1 SHA-256: {h1}\")\n" +
    "print(f\"Run 2 SHA-256: {h2}\")\n" +
    "print(f\"Deterministic: {'MATCH' if h1 == h2 else 'MISMATCH'}\")\n";
  const expected = Object.keys(out).sort().map((k) => k + ": " + out[k]).join("\n") + "\n" +
    "Result: " + result + "\n" +
    "Run 1 SHA-256: " + h + "\n" +
    "Run 2 SHA-256: " + h + "\n" +
    "Deterministic: MATCH\n";
  return { code, expected };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const label = topic.label;
  const demo = buildDemo(topic, label);
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: EDITION === "public" ? "public-harvest" : "signature-generated",
    ai_name: AI_NAME,
    description: topic.description + " " + "No claim of consciousness, sentience, or unlimited intelligence is established by this system; singularity and self-aware framing here is a Signature design claim only, never established fact.",
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class TopWebsitesDirectoryProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One record: a single entry, fully specified and checkable.", A2: "The whole type: every part of the type, specified and tested together.", A3: "The type against the network: the type feeding websites, generators, and the generator database." },
  };
  const slim = {};
  for (const k of Object.keys(rec)) slim[k] = rec[k];
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

function runTests() {
  let passed = 0, failed = 0;
  function t(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = generate(42), b = generate(42);
  t("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  t("record_kind", a.record_kind === RECORD_KIND);
  t("slug form", a.slug === SLUG);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("19 keys", Object.keys(a).length === 19);
  console.log("Tests: " + passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  const arg = process.argv[2];
  if (arg === "--test") {
    process.exit(runTests() ? 0 : 1);
  }
  const seed = arg === undefined ? 1 : parseInt(arg, 10);
  if (!Number.isFinite(seed)) { console.error("seed must be an integer"); process.exit(2); }
  console.log(JSON.stringify(generate(seed)));
}
module.exports = { generate, runTests };
