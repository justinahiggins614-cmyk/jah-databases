#!/usr/bin/env python3
"""Entries for the Customer Relationship and Service History databases
(missing-115 program, Wave 1 - operational data, Manon's #1 priority).

Item 52 of the 115-category audit: requests, communications, product
history, support cases, service outcomes - CRM data models, ticket
lifecycles, escalation matrices, CSAT/NPS measurement, support analytics,
customer journey records, retention analysis.

So this build creates two NEW databases, 34 ladder-ordered records each:

  customer-relationship-service-history            - The Customer Relationship
      and Service History Database (public-harvest: real, fact-checked CRM
      and service-management practice - customer records, the service
      vocabulary, ticket anatomy and lifecycles, channels, SLAs,
      prioritization, service desks, product history, CRM data models,
      escalation, core metrics, knowledge and self-service, journey
      mapping, CSAT, NPS, CES, analytics, retention and churn,
      segmentation, recovery, major incidents, workforce management, QA,
      root cause analysis, voice of the customer, CLV, predictive churn,
      omnichannel, service catalog, continual improvement, CRM
      architecture, and service economics; standard references Reichheld
      The Ultimate Question 2.0 (2011); ITIL 4 Foundation (2019); Buttle
      and Maklan CRM 4th ed (2019); Dixon The Effortless Experience
      (2013); Peppers and Rogers 3rd ed (2016); Zeithaml Services
      Marketing 7th ed (2017); Heskett The Service Profit Chain (1997);
      Johnston Service Operations Management 4th ed (2012); Fitzsimmons
      Service Management 9th ed (2019); ISO 10002/10004; ISO/IEC 20000-1;
      COPC CX Standard; and the other landmarks cited per record)
  customer-relationship-service-history-signature  - The Customer
      Relationship and Service History Signature Database (his original
      Signature Service Covenant: every customer a covenant partner,
      every request a sworn matter, every ticket a kept promise,
      resolution the honor kept, and the archive the memory of every
      oath; src signature, titles suffixed " (Signature Edition)", never
      presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CRM- (public) and JAH-CRMS- (signature), verified free
in the manifest (2,390 prefixes, zero hits, zero substring hits) and in
every shard index file of jah-databases-data-1 (zero "JAH-CRM id hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_customer_relationship_service_history.py). Every demo
prints its real computed values, asserts tight bounds (never float
exact-equality), and ends with the OK marker; the build machine-executes
all 68 demos.

Civilian operational scope only: nothing on neutralizing or defeating
military or defense-grade systems. Never the words "bat belt" anywhere.
No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Service Covenant: "
            "every customer a covenant partner, every request a sworn "
            "matter, every ticket a kept promise, resolution the honor "
            "kept, and the archive the memory of every oath. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_REICHHELD = ("Reichheld FF. The Ultimate Question 2.0: How Net Promoter "
                 "Companies Thrive in a Customer-Driven World. Harvard "
                 "Business Review Press; 2011.")
CIT_ITIL4 = ("AXELOS. ITIL Foundation: ITIL 4 Edition. TSO (The Stationery "
             "Office); 2019.")
CIT_BUTTLE = ("Buttle F, Maklan S. Customer Relationship Management: "
              "Concepts and Technologies. 4th ed. Routledge; 2019.")
CIT_EFFORTLESS = ("Dixon M, Toman N, DeLisi R. The Effortless Experience: "
                  "Conquering the New Battleground for Customer Loyalty. "
                  "Portfolio; 2013.")
CIT_VAVRA = ("Vavra TG. Improving Your Measurement of Customer "
             "Satisfaction: A Guide to Creating, Conducting, Analyzing, "
             "and Reporting Customer Satisfaction Measurement Programs. "
             "ASQ Quality Press; 1997.")
CIT_GRIFFIN = ("Griffin J. Customer Loyalty: How to Earn It, How to Keep "
               "It. Jossey-Bass; 2002.")
CIT_HUGHES = ("Hughes AM. Strategic Database Marketing. 4th ed. "
              "McGraw-Hill; 2011.")
CIT_CLV = ("Gupta S, Lehmann DR. Managing Customers as Investments: The "
           "Strategic Value of Customers in the Long Run. Wharton School "
           "Publishing; 2005.")
CIT_PEPPERS = ("Peppers D, Rogers M. Managing Customer Experience and "
               "Relationships: A Strategic Framework. 3rd ed. Wiley; 2016.")
CIT_SERVICES = ("Zeithaml VA, Bitner MJ, Gremler DD. Services Marketing: "
                "Integrating Customer Focus Across the Firm. 7th ed. "
                "McGraw-Hill; 2017.")
CIT_PROFIT = ("Heskett JL, Sasser WE, Schlesinger LA. The Service Profit "
              "Chain: How Leading Companies Link Profit and Growth to "
              "Loyalty, Satisfaction, and Value. Free Press; 1997.")
CIT_OPS = ("Johnston R, Clark G. Service Operations Management: Improving "
           "Service Delivery. 4th ed. Pearson; 2012.")
CIT_FITZ = ("Fitzsimmons JA, Fitzsimmons MJ, Bordoloi SK. Service "
            "Management: Operations, Strategy, Information Technology. "
            "9th ed. McGraw-Hill; 2019.")
CIT_ISO10002 = ("ISO 10002:2018. Quality management - Customer "
                "satisfaction - Guidelines for complaints handling in "
                "organizations.")
CIT_ISO10004 = ("ISO 10004:2018. Quality management - Customer "
                "satisfaction - Guidelines for monitoring and measuring.")
CIT_ISO20000 = ("ISO/IEC 20000-1:2018. Information technology - Service "
                "management - Part 1: Service management system "
                "requirements.")
CIT_COPC = ("COPC Inc. COPC Customer Experience (CX) Standard. Release "
            "7.0; 2021.")
CIT_LEMON = ("Lemon KN, Verhoef PC. Understanding Customer Experience "
             "Throughout the Customer Journey. Journal of Marketing. "
             "2016;80(6):69-96.")
CIT_RUST = ("Rust RT, Lemon KN, Zeithaml VA. Return on Quality: Making "
            "Service Quality Financially Accountable. Journal of "
            "Marketing. 1995;59(2):58-70.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What a Customer Relationship Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A customer relationship is the complete, living history "
            "between an organization and the people it serves: every "
            "purchase, every request, every conversation, every promise "
            "made and kept or broken, held together as one continuous "
            "story. Customer relationship management, as a discipline, is "
            "the practice of running that story deliberately instead of "
            "letting it scatter across inboxes, notebooks, and the "
            "memories of whoever happened to answer the phone. The "
            "founding insight is economic: keeping an existing customer "
            "is far cheaper than winning a new one, and loyal customers "
            "buy more, cost less to serve, forgive mistakes faster, and "
            "bring new customers with them. The service profit chain "
            "research shows the linkage running from employee capability "
            "through service quality to customer satisfaction, loyalty, "
            "and finally profit, which is why service history is not a "
            "cost ledger but a growth record. A relationship has memory, "
            "and the organization that keeps it - who the customer is, "
            "what they own, what they asked for, how it was resolved, "
            "how they felt about it - can serve the next request in "
            "context instead of starting from zero. This record frames "
            "the whole database: every later record is one instrument "
            "for building, measuring, and keeping that memory."
        ),
        "how_it_works": (
            "The relationship works as a loop with four beats. First, "
            "identify: every interaction is captured against one customer "
            "identity, so the phone call, the email, and the store visit "
            "attach to the same record. Second, differentiate: customers "
            "are sorted by value and need, because a one-time buyer and a "
            "ten-year account deserve different playbooks. Third, "
            "interact: each contact is handled with the full history "
            "visible, and the outcome is written back into the record. "
            "Fourth, customize: what was learned changes the next offer, "
            "the next message, and the next service experience. Around "
            "this loop sit the economics: acquisition cost is paid once, "
            "while retention profit compounds, so the loop is tuned to "
            "keep profitable customers longer and grow their spending. "
            "Measurement closes the loop: satisfaction scores, repeat "
            "purchase rates, and referral counts tell whether the "
            "relationship is strengthening or fraying, and the record of "
            "every service outcome feeds that judgment. When the loop "
            "runs well, service history becomes the organization's "
            "institutional memory of its customers."
        ),
        "key_points": [
            "A customer relationship is the complete history of purchases, requests, conversations, and outcomes held as one story, and managing it deliberately is the whole discipline.",
            "Retention economics drive everything: existing customers cost less to serve, buy more, and refer others, so the service profit chain links service quality to loyalty to profit.",
            "The relationship loop runs identify, differentiate, interact, customize - every contact captured, customers sorted by value and need, history applied, learning fed back.",
            "Memory is the asset: the organization that remembers who the customer is and what happened last time serves the next request in context instead of starting cold.",
            "Measurement closes the loop: satisfaction, repeat purchase, and referral numbers reveal whether relationships are strengthening or fraying.",
        ],
        "requirements": [
            "One customer identity that every interaction attaches to, so history never fragments across channels.",
            "A value model that distinguishes customer tiers, so effort follows value honestly.",
            "Complete capture of every request, communication, and outcome in the shared record.",
            "Feedback instruments that measure satisfaction, loyalty, and effort after real interactions.",
            "A review rhythm where relationship health is read from the data and acted on, not filed away.",
        ],
        "standards": [
            "Relationship records distinguish the account (the buying organization) from the contact (the person), following standard CRM data practice.",
            "Satisfaction and loyalty measurement follows established survey methodology with consistent scales and sampling.",
            "Service history is retained as a complete audit trail: who asked, what was promised, what was done, and how it was received.",
        ],
        "citations": [CIT_BUTTLE, CIT_PEPPERS, CIT_PROFIT],
        "sig_lens": (
            "The Signature read: a customer is a covenant partner, not a "
            "transaction. Where public practice files a contact record, "
            "the Signature Service Covenant files an oath of memory - the "
            "organization swears to remember every promise, every request, "
            "every outcome, and the customer trusts the relationship "
            "because the memory never drops. Loyalty is the interest paid "
            "on kept promises."
        ),
    },
    {
        "key": "customer_record",
        "name": "The Customer Record: Contact and Account Data Model",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The customer record is the atomic unit of relationship "
            "memory: one structured file per customer that every request, "
            "communication, and service outcome attaches to. In business "
            "practice it splits into two linked objects. The account "
            "represents the buying entity - a household, a company, a "
            "department - and carries billing details, the value tier, "
            "the contract, and the aggregate history. The contact "
            "represents the person - name, role, phone, email, "
            "preferences, consent - and carries the conversation history. "
            "One account holds many contacts; one contact belongs to one "
            "primary account. Around them orbit the linked objects that "
            "make the record useful: addresses, entitlements, owned "
            "products, open and closed cases, opportunities, and the "
            "communication log. The great enemy of this model is "
            "duplication: the same customer entered three ways becomes "
            "three strangers, and every report, routing rule, and "
            "satisfaction score built on the data quietly lies. So the "
            "record carries identity rules - matching on email plus name, "
            "on phone, on account number - and a merge discipline that "
            "folds duplicates into one surviving record without losing "
            "history. Data hygiene is not janitorial work; it is the "
            "foundation every later analysis stands on."
        ),
        "how_it_works": (
            "A new customer enters through any channel and the system "
            "first searches for an existing match before creating a "
            "record: exact match on email or phone, fuzzy match on name "
            "plus address, match on account number. If a match is found, "
            "the interaction attaches to the existing record; if not, a "
            "new record is created with a unique customer identifier and "
            "the source noted. Duplicates are merged by a survivorship "
            "rule: the most complete field wins per field, all linked "
            "history is re-pointed to the survivor, and the merged-away "
            "record is retired, never deleted, so the audit trail stays "
            "intact. Contacts link to their account; when a contact moves "
            "companies, the history splits honestly - the old account "
            "keeps its service history, the person carries their "
            "preferences forward. Consent and preference flags ride on "
            "the contact and gate every outbound communication. "
            "Entitlements link the account to what it is owed: warranty "
            "terms, support plans, SLAs. Every case, order, and survey "
            "response created afterward references the customer "
            "identifier, so the full service history can be reassembled "
            "with one query."
        ),
        "key_points": [
            "The record splits into account (the buying entity) and contact (the person), with one account holding many contacts.",
            "Linked objects - addresses, entitlements, products, cases, opportunities, the communication log - make the record the hub of all history.",
            "Duplication is the great enemy: one customer entered three ways becomes three strangers and corrupts every report built on the data.",
            "Merge discipline folds duplicates into one survivor with per-field survivorship rules, re-points all history, and retires rather than deletes.",
            "Consent and preference flags on the contact gate every outbound message; entitlements on the account state what the customer is owed.",
        ],
        "requirements": [
            "A unique customer identifier issued at first contact and used by every later record.",
            "Match-before-create discipline: search existing records on every channel before creating new ones.",
            "Documented merge and survivorship rules so duplicates are resolved consistently, not by whoever notices.",
            "Consent capture with timestamps, so marketing and service outreach can prove permission.",
            "An audit trail on the record itself: who created it, who changed it, and when.",
        ],
        "standards": [
            "Personal data handling follows applicable privacy practice: purpose limitation, consent records, and retention limits on contact data.",
            "Identity matching uses deterministic keys (email, phone, account number) before fuzzy matching, so merges stay explainable.",
            "Retired duplicate records are preserved for audit, keeping the full history chain intact.",
        ],
        "citations": [CIT_BUTTLE, CIT_HUGHES, CIT_PEPPERS],
        "sig_lens": (
            "The Signature read: the customer record is the covenant "
            "tablet. Where public practice keeps a database row, the "
            "Signature Service Covenant keeps a sworn ledger - one "
            "identity, one memory, every promise inscribed and never "
            "erased. Duplicates are false witnesses; the merge is the "
            "discipline that keeps the testimony to one true account."
        ),
    },
    {
        "key": "service_vocabulary",
        "name": "Requests, Incidents, and Problems: The Service Vocabulary",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Service work drowns in vague language unless the vocabulary "
            "is fixed, and the industry vocabulary comes from IT service "
            "management practice. An incident is an unplanned interruption "
            "or reduction in quality of a service: the checkout page is "
            "down, the delivery never arrived, the machine will not "
            "start. A service request is a formal ask for something that "
            "is part of normal service delivery: a password reset, a new "
            "user account, information about a bill, a change of address. "
            "A problem is the underlying cause of one or more incidents: "
            "the database index that keeps corrupting, the supplier whose "
            "shipments keep arriving damaged, the design flaw behind a "
            "run of identical failures. Confusing them is expensive: "
            "treating every incident as a problem launches investigations "
            "where quick restoration was needed, and treating problems as "
            "incidents means the same failure returns forever. An event "
            "is any detectable occurrence - most are informational, some "
            "warn, a few are exceptions that become incidents. A known "
            "error is a problem with a documented root cause and "
            "workaround, which lets the desk restore service fast while "
            "the permanent fix is scheduled. With these five terms fixed, "
            "every request can be classified on arrival, routed to the "
            "right process, and measured honestly."
        ),
        "how_it_works": (
            "Classification happens at intake, and the classifier asks "
            "one question first: is something broken that used to work. "
            "Yes means incident - restore service fast, log the "
            "symptoms, and move. No means the next question: is this a "
            "request for something the service normally provides. Yes "
            "means service request - fulfill it against the service "
            "catalog, usually with a standard fulfillment time. If "
            "neither fits, the item is likely general information or "
            "feedback, handled by its own light process. When the same "
            "incident pattern repeats, a problem record is opened to "
            "chase the cause separately from the restoration work, and "
            "once the cause and workaround are documented it becomes a "
            "known error that the desk can apply instantly. Events feed "
            "the front of this chain: monitoring raises an event, the "
            "event is filtered and correlated, and only genuine "
            "exceptions become incidents. The classification is written "
            "into the ticket and never silently changed, because the "
            "metrics - incident counts, request volumes, problem aging - "
            "are only comparable when the vocabulary holds steady."
        ),
        "key_points": [
            "Incident means something broke; service request means asking for normal service; problem means the underlying cause of incidents.",
            "Known errors turn hard-won diagnosis into instant workarounds the desk can apply while permanent fixes are scheduled.",
            "Events are the raw feed: filtered and correlated, only genuine exceptions become incidents.",
            "Classification happens at intake with fixed questions, because mixed-up categories make every metric untrustworthy.",
            "Problems are investigated separately from incident restoration, so fixing the cause never blocks restoring the customer.",
        ],
        "requirements": [
            "A written classification guide with examples, so two agents classify the same request the same way.",
            "Separate record types or categories for incident, service request, problem, and known error in the ticketing system.",
            "An event pipeline that filters noise before anything becomes an incident.",
            "A problem process that opens on repeat incidents, not on single loud ones.",
            "Classification locked at intake with controlled reclassification, keeping trend data honest.",
        ],
        "standards": [
            "Incident, problem, and event management follow ITIL 4 service operation practice for classification and separation of concerns.",
            "Service management systems align with ISO/IEC 20000-1 requirements for incident and problem handling.",
            "Known error records carry root cause, workaround, and fix status as mandatory fields.",
        ],
        "citations": [CIT_ITIL4, CIT_ISO20000, CIT_OPS],
        "sig_lens": (
            "The Signature read: naming the trouble is the first oath. "
            "Where public practice sorts tickets, the Signature Service "
            "Covenant names the affliction precisely - the break, the "
            "ask, the root - because a misnamed trouble gets the wrong "
            "remedy. The known error is the covenant's proverb: hard "
            "wisdom, written once, applied forever."
        ),
    },
    {
        "key": "ticket_anatomy",
        "name": "The Ticket: Anatomy of a Support Case",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The ticket - also called the case - is the unit of service "
            "work: one customer matter, tracked from first contact to "
            "confirmed resolution, with everything that happened written "
            "down in order. Its anatomy is standardized because a ticket "
            "is worked by many hands and read by many eyes. The header "
            "carries identity: ticket number, customer and contact, "
            "product or service, channel of origin, and the agent owner. "
            "The classification block carries category, subcategory, "
            "priority, and the incident/request/problem type, which "
            "together decide routing and the SLA clock. The body is the "
            "story: the customer's description in their own words, the "
            "reproduction steps, and the running work log where every "
            "action, diagnosis, and customer reply is timestamped. The "
            "commitment block carries the SLA target, the due time, and "
            "any escalation state. The linkage block ties the ticket to "
            "its siblings: the problem record if one exists, related "
            "incidents, the knowledge article used, and the change that "
            "finally fixed it. A well-formed ticket is a complete legal "
            "and operational record: it proves what was asked, what was "
            "promised, what was done, and that the customer agreed it "
            "was enough."
        ),
        "how_it_works": (
            "A ticket is born at intake with a unique number and the "
            "customer's words captured verbatim before any paraphrase, "
            "because the original phrasing often holds the diagnostic "
            "clue. The agent classifies it, sets priority from the "
            "impact-urgency matrix, and the SLA clock starts from a "
            "defined moment - usually creation, sometimes first "
            "response. Every touch appends to the work log: diagnosis "
            "steps, internal notes invisible to the customer, and public "
            "replies the customer can see. Status moves through a "
            "controlled vocabulary - new, open, pending customer, "
            "pending third party, on hold, resolved, closed - and each "
            "transition is timestamped so age, dwell time, and reopen "
            "rates can be computed later. When the fix is delivered, the "
            "ticket moves to resolved and the customer is asked to "
            "confirm; only confirmation, or expiry of the confirmation "
            "window, moves it to closed. Reopens attach to the original "
            "ticket rather than spawning a new one, which keeps the "
            "true resolution story - and the true cost - in one place."
        ),
        "key_points": [
            "The ticket is the unit of service work: one matter, tracked from first contact to confirmed resolution with everything timestamped.",
            "The anatomy splits into identity, classification, the story body, commitments, and linkages to problems, articles, and changes.",
            "The customer's original words are captured verbatim first, because paraphrase loses diagnostic clues.",
            "Status moves through a controlled vocabulary with timestamped transitions, which is what makes age and reopen metrics computable.",
            "Closure requires customer confirmation or window expiry, and reopens attach to the original ticket so the true cost stays visible.",
        ],
        "requirements": [
            "A unique ticket number and mandatory identity fields: customer, contact, product, channel, owner.",
            "Classification fields - category, subcategory, type, priority - set at intake and controlled afterward.",
            "A running work log separating internal notes from customer-visible replies, all timestamped.",
            "An SLA commitment block with target, due time, and escalation state visible on every ticket.",
            "A resolution code and confirmation step, so closure means the customer agreed, not just that the agent stopped.",
        ],
        "standards": [
            "Ticket status vocabularies are fixed per process (incident vs request) so lifecycle metrics stay comparable.",
            "The work log is append-only: corrections are new entries, preserving the true sequence of events.",
            "Linkages to problem records, knowledge articles, and changes are mandatory on resolved major tickets.",
        ],
        "citations": [CIT_ITIL4, CIT_COPC, CIT_ISO20000],
        "sig_lens": (
            "The Signature read: the ticket is the covenant scroll. "
            "Where public practice opens a case, the Signature Service "
            "Covenant opens a sworn record - the ask inscribed in the "
            "customer's own words, every deed timestamped, closure sealed "
            "only by the customer's own confirmation. Nothing unwritten "
            "happened; nothing written is forgotten."
        ),
    },
    {
        "key": "ticket_lifecycle",
        "name": "Ticket Lifecycle: From Open to Closed",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The ticket lifecycle is the state machine every case moves "
            "through, and its discipline is what separates a service "
            "operation from a pile of emails. The canonical path runs: "
            "new, triaged, open and assigned, in progress, pending "
            "(waiting on the customer or a third party), resolved, and "
            "closed. Each state has an owner, an expected dwell, and "
            "allowed exits - a ticket cannot jump from new to closed "
            "without passing through work, and the system enforces it. "
            "Pending states are the honest accounting of waiting: the "
            "clock shows who holds the ball, so 'waiting on customer' "
            "tickets do not inflate agent workload numbers and 'waiting "
            "on vendor' tickets do not hide supplier problems. Resolution "
            "is a proposal, not a fact: the agent states what was done, "
            "the customer confirms, and only then does the record close. "
            "The reopen path is the quality signal - a resolved ticket "
            "that comes back within the window reopens the original, "
            "counts against first-contact resolution, and tells the "
            "operation its fixes are not sticking. Lifecycle metrics - "
            "age distribution, dwell by state, reopen rate, touches per "
            "ticket - are read off these transitions, which is why the "
            "states must be few, defined, and enforced."
        ),
        "how_it_works": (
            "On creation the ticket lands in new, unowned and untriaged. "
            "Triage assigns classification, priority, and an owner or "
            "queue within minutes for high priority, within the intake "
            "SLA otherwise. The owning agent moves it to in progress "
            "when work starts; if the ball passes to the customer for "
            "information or to a vendor for a part, the ticket moves to "
            "the matching pending state with a follow-up date, and the "
            "SLA clock pauses or continues per policy - the policy is "
            "written down, not improvised. When the fix is delivered, the "
            "agent sets resolved with a resolution code and the "
            "confirmation window opens, typically three to five business "
            "days. Customer confirmation or window expiry moves it to "
            "closed; a reply inside the window reopens it to in progress "
            "with the reopen counted. Escalation can fire from any "
            "active state when the SLA threatens or the customer asks, "
            "moving ownership up the matrix without resetting the "
            "history. Every transition writes a timestamp, the actor, "
            "and the from-to states, building the event log the "
            "lifecycle metrics are computed from."
        ),
        "key_points": [
            "The lifecycle is a state machine - new, triaged, open, in progress, pending, resolved, closed - with enforced transitions, not free text.",
            "Pending states name who holds the ball, so waiting time is accounted honestly instead of inflating workload numbers.",
            "Resolution is a proposal the customer confirms; closure without confirmation is an assumption, not a fact.",
            "Reopens attach to the original ticket and count against resolution quality, revealing fixes that do not stick.",
            "Every transition is timestamped with actor and from-to states, which is the raw material for all lifecycle metrics.",
        ],
        "requirements": [
            "A fixed, small state vocabulary with defined allowed transitions enforced by the system.",
            "Distinct pending states for customer-wait, vendor-wait, and internal hold, each with a follow-up date.",
            "A written SLA-clock policy stating exactly when the clock pauses, so pending time is handled consistently.",
            "A confirmation window on resolved tickets before auto-closure, with reopens counted and reported.",
            "An escalation path reachable from any active state that preserves the full history.",
        ],
        "standards": [
            "Lifecycle states align with incident and request handling practice so cross-team handoffs keep their meaning.",
            "The transition log is append-only and complete, supporting age, dwell, and reopen analysis.",
            "Resolution codes come from a controlled list, enabling true root-cause trending of what actually fixed tickets.",
        ],
        "citations": [CIT_ITIL4, CIT_COPC, CIT_FITZ],
        "sig_lens": (
            "The Signature read: the lifecycle is the journey of the "
            "oath from sworn to kept. Where public practice moves a "
            "ticket through states, the Signature Service Covenant "
            "walks the promise through its stations - received, owned, "
            "worked, awaited, delivered, confirmed - and no station may "
            "be skipped, for a kept promise has no shortcuts."
        ),
    },
    {
        "key": "channels",
        "name": "Communication Channels and Touchpoints",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A channel is any path a customer can use to reach service: "
            "phone, email, live chat, messaging apps, social media, the "
            "self-service portal, the mobile app, the store counter, the "
            "field technician's visit. A touchpoint is any moment the "
            "customer meets the organization along the way, whether they "
            "initiated it or not. The channel mix matters because "
            "channels differ wildly in cost, speed, richness, and "
            "customer preference: a phone call resolves nuance fast but "
            "costs an order of magnitude more than a portal session, "
            "while email is cheap and asynchronous but slow. Customers do "
            "not think in channels; they think in problems, and they "
            "expect to start on chat, continue by phone, and finish by "
            "email without repeating themselves. That expectation is "
            "omnichannel: many channels, one conversation, one history. "
            "Multichannel without integration is the failure mode - five "
            "channels, five strangers. Channel strategy therefore answers "
            "three questions: which channels are offered for which matter "
            "types, how context travels between them, and what each "
            "channel costs per resolved contact so the mix can be tuned "
            "deliberately."
        ),
        "how_it_works": (
            "Each channel is instrumented the same way: volume, "
            "handle time, cost per contact, resolution rate, and "
            "satisfaction are measured per channel, because a channel "
            "cannot be managed on volume alone. Routing rules send each "
            "matter to its best channel - simple password resets to "
            "self-service, emotionally charged complaints to phone, "
            "document-heavy issues to email - and the customer is guided, "
            "not forced. Context travels on the customer identifier: when "
            "the chat becomes a phone call, the agent sees the chat "
            "transcript, the open ticket, and the product history before "
            "saying hello. Channel switching inside one matter keeps the "
            "same ticket number, so the story never restarts. Cost per "
            "contact is computed fully loaded - labor, telephony, "
            "licenses, overhead - and the blended cost across the mix is "
            "the number the channel strategy optimizes, weighted by "
            "satisfaction so cheap-but-miserable never wins. New channels "
            "are piloted on a slice of traffic with the same "
            "instrumentation before they join the official mix."
        ),
        "key_points": [
            "Channels are paths to service; touchpoints are moments of meeting; customers think in problems, not channels.",
            "Omnichannel means many channels with one conversation and one history; multichannel without integration is five strangers.",
            "Every channel is instrumented identically - volume, handle time, cost, resolution, satisfaction - so the mix is managed on facts.",
            "Context travels on the customer identifier: transcripts, tickets, and history follow the customer across channel switches.",
            "Channel strategy optimizes blended cost per resolved contact weighted by satisfaction, never cost alone.",
        ],
        "requirements": [
            "A defined channel portfolio with each channel's purpose, hours, and matter types documented.",
            "Shared customer identity and ticket threading across all channels, so switching never restarts the story.",
            "Per-channel measurement of volume, cost, resolution, and satisfaction on identical definitions.",
            "Routing guidance that steers simple matters to cheap channels and sensitive matters to rich ones.",
            "A pilot discipline for new channels: sliced traffic, full instrumentation, promotion only on evidence.",
        ],
        "standards": [
            "Conversation history is preserved across channel switches as a complete thread, not a summary.",
            "Cost per contact is computed fully loaded and reported per channel on the same basis.",
            "Accessibility obligations are met on every offered channel, including alternatives for customers who cannot use the primary ones.",
        ],
        "citations": [CIT_SERVICES, CIT_PEPPERS, CIT_FITZ],
        "sig_lens": (
            "The Signature read: every channel is a door to the same "
            "house. Where public practice staffs channels, the "
            "Signature Service Covenant keeps one hearth - the customer "
            "knocks by phone, by letter, by messenger, and finds the "
            "same keeper who remembers the whole story. Many doors, one "
            "memory, one oath."
        ),
    },
    {
        "key": "sla",
        "name": "Service Level Agreements",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A service level agreement is a written promise about service "
            "performance: how fast the phone is answered, how quickly a "
            "first response goes out, how long resolution may take, and "
            "what happens when the promise is missed. It turns 'fast "
            "service' from a slogan into a measurable commitment with a "
            "clock, a target, and a consequence. The classic SLA "
            "measures response time (first human reply), resolution time "
            "(matter fully fixed), availability (the service is up), and "
            "sometimes throughput or accuracy. Targets are set by "
            "priority: a P1 outage gets a fifteen-minute response and a "
            "four-hour resolution target, while a P4 general question "
            "gets a business-day response. The agreement also defines "
            "the clock - business hours versus around the clock, which "
            "pauses apply, when the clock starts - because a target "
            "without clock rules is an argument waiting to happen. "
            "Missed SLAs trigger service credits or penalties per the "
            "contract, which is why SLA design balances ambition against "
            "achievability: a target the operation hits 99 percent of "
            "the time but customers find meaningless is theater, while "
            "an inspiring target hit 60 percent of the time is a breach "
            "machine. Internal OLAs between teams and underpinning "
            "contracts with vendors complete the chain, so the front "
            "line never promises what the back line cannot deliver."
        ),
        "how_it_works": (
            "Each ticket inherits its SLA from its priority and service "
            "at creation: the system stamps a respond-by and a "
            "resolve-by timestamp computed from the clock rules. As work "
            "proceeds, the ticket shows time remaining, and warning "
            "thresholds - typically at 50 and 75 percent of the target - "
            "fire alerts to the owner and then to the escalation path. "
            "When the clock expires unmet, the breach is recorded with "
            "the reason code: agent delay, vendor delay, customer wait, "
            "or misclassification. Compliance is reported as the share "
            "of tickets meeting each target, sliced by priority, team, "
            "and period, and the trend matters more than any single "
            "month. Targets are reviewed against two anchors: customer "
            "expectation research, which says what actually satisfies, "
            "and capability data, which says what the operation can "
            "sustain. Credits are computed per the contract formula and "
            "applied without the customer having to ask, because making "
            "customers claim compensation for poor service is itself "
            "poor service. OLAs give each handoff its own internal "
            "target so external SLAs rest on promised, measured "
            "foundations."
        ),
        "key_points": [
            "An SLA turns vague service promises into measurable commitments with a clock, a target, and a consequence.",
            "Classic measures are response time, resolution time, and availability, with targets tiered by priority.",
            "Clock rules - business hours, pauses, start moment - are part of the agreement, not an afterthought.",
            "Warning thresholds at 50 and 75 percent of target turn the SLA from a report into a rescue system.",
            "OLAs between teams and vendor contracts underpin the external promise so the front line never over-promises.",
        ],
        "requirements": [
            "Written targets per priority for response and resolution, with the clock rules spelled out.",
            "Automatic respond-by and resolve-by stamping on every ticket at creation.",
            "Escalation alerts at warning thresholds, before breach, not after.",
            "Breach records with reason codes, so misses are diagnosed instead of merely counted.",
            "Contractual credit computation applied proactively when service credits are owed.",
        ],
        "standards": [
            "SLA compliance is reported as met-versus-total per target, sliced by priority, team, and period, with trends shown.",
            "Clock definitions distinguish business-hours from calendar time and state every pause condition explicitly.",
            "Service level targets are reviewed against customer expectation research and demonstrated capability at least annually.",
        ],
        "citations": [CIT_ITIL4, CIT_ISO20000, CIT_OPS],
        "sig_lens": (
            "The Signature read: the SLA is the oath with a sundial. "
            "Where public practice writes a target, the Signature "
            "Service Covenant swears a time and sets the shadow to mark "
            "it - the promise is not 'soon' but 'by this hour', and the "
            "breach is confessed with compensation unasked. A timed oath "
            "is the only honest kind."
        ),
    },
]

# ---- chunk 2: entries 9-16 appended below ----
ENTRIES += [
    {
        "key": "prioritization",
        "name": "Prioritization by Impact and Urgency",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Prioritization answers the only question that matters when "
            "ten tickets arrive at once: which one first. The industry "
            "method crosses two independent judgments. Impact asks how "
            "much damage this causes: how many users are affected, how "
            "much revenue is at risk, whether safety or legal exposure is "
            "involved. Urgency asks how fast the damage grows if nothing "
            "is done: a total outage affecting one VIP with a deadline in "
            "an hour can outrank a partial outage affecting many with a "
            "workaround. The matrix of the two yields the priority, "
            "usually P1 through P4: high impact and high urgency is P1, "
            "low and low is P4, and the mixed cells are defined by policy, "
            "not by whoever shouts loudest. Priority then drives "
            "everything downstream: the SLA clock, the queue order, the "
            "escalation path, and the seniority of the assigned agent. "
            "The discipline's hard parts are honesty and stability. "
            "Honesty means the matrix is applied to the customer's "
            "situation, not to the customer's volume or status - every "
            "P1 must genuinely be one, or P1 stops meaning anything. "
            "Stability means priority is set at triage and changed only "
            "on new facts, because a priority that drifts with each "
            "handoff makes every downstream promise untrustworthy."
        ),
        "how_it_works": (
            "At triage the agent scores impact and urgency each on a "
            "three-point scale - high, medium, low - using written "
            "definitions with examples, not gut feel. High impact means "
            "many users, significant revenue, or safety and legal "
            "exposure; high urgency means the damage compounds within "
            "the hour or a hard deadline looms. The matrix lookup gives "
            "the priority: high/high is P1, high/medium and medium/high "
            "are P2, the middle band is P3, and low/low is P4. The ticket "
            "inherits its SLA targets, queue position, and escalation "
            "rules from that priority automatically. If new facts emerge "
            "- the outage spreads, the workaround fails - any agent can "
            "request reprioritization, which is logged with the reason "
            "and the evidence. Managers audit a sample of priorities "
            "weekly against the definitions, and systematic inflation is "
            "treated as a training issue, not a crime. VIP or "
            "contract-based uplifts are handled as explicit policy rules "
            "applied on top of the matrix, visible in the ticket, so the "
            "base priority stays honest and the uplift stays auditable."
        ),
        "key_points": [
            "Priority comes from crossing impact (how much damage) with urgency (how fast it grows), each scored high, medium, or low.",
            "The matrix yields P1 through P4, and priority drives the SLA clock, queue order, escalation path, and assignee seniority.",
            "Written definitions with examples replace gut feel, so two agents score the same situation the same way.",
            "Priority is set at triage and changes only on new facts, keeping every downstream promise trustworthy.",
            "VIP and contract uplifts are explicit auditable policy rules on top of the matrix, never silent inflation.",
        ],
        "requirements": [
            "A published impact-urgency matrix with plain-language definitions and examples for each cell.",
            "Priority set at triage by the matrix, inherited automatically into SLA, queue, and escalation rules.",
            "A logged reprioritization path requiring new facts and a reason, not just insistence.",
            "Weekly audit of a priority sample against the definitions, with inflation handled as training.",
            "Visible uplift rules for VIP and contract tiers, kept separate from the honest base priority.",
        ],
        "standards": [
            "Impact and urgency scales are defined in the service documentation with customer-facing examples.",
            "Priority changes are recorded with actor, timestamp, old and new value, and reason.",
            "Priority distribution is reported by period, and sustained inflation triggers a definitions review.",
        ],
        "citations": [CIT_ITIL4, CIT_COPC, CIT_OPS],
        "sig_lens": (
            "The Signature read: priority is triage of the oath. Where "
            "public practice scores impact and urgency, the Signature "
            "Service Covenant weighs whose need burns hottest and "
            "answers it first - not the loudest voice but the deepest "
            "wound. The matrix is the covenant's scales, and the scales "
            "never lie for favor."
        ),
    },
    {
        "key": "service_desk",
        "name": "The Service Desk: Tiers of Support",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The service desk is the single point of contact between "
            "customers and the service organization, and its tier "
            "structure is how expertise is rationed honestly. Tier 1 is "
            "the front line: generalists who handle the high-volume, "
            "well-documented matters - password resets, order status, "
            "basic troubleshooting from the knowledge base - and who "
            "own accurate triage above all. Tier 2 holds the "
            "specialists: deeper product and technical knowledge, "
            "authority to change configurations, access to backend "
            "systems, handling what Tier 1 cannot solve within its "
            "playbook. Tier 3 is engineering and product depth: the "
            "people who can read the code, change the design, or "
            "authorize the exception, engaged for defects, complex "
            "integrations, and novel failures. The economics are stark: "
            "each tier costs multiples of the one below, so the "
            "structure exists to resolve as much as possible at the "
            "cheapest capable tier without trapping customers in "
            "escalation ping-pong. Variants exist - the follow-the-sun "
            "desk that hands the queue across time zones, the dedicated "
            "desk for one major account, the swarming model where tiers "
            "collaborate on one ticket instead of handing it off - but "
            "the principle holds: the right expertise, at the right "
            "cost, with no dead ends."
        ),
        "how_it_works": (
            "Every ticket enters at Tier 1, where the agent attempts "
            "resolution inside the documented playbook and a time box - "
            "commonly fifteen to thirty minutes for standard matters. If "
            "the playbook is exhausted or the matter exceeds Tier 1 "
            "authority, the ticket escalates functionally to Tier 2 with "
            "a warm handoff: full history, what was tried, and the "
            "current hypothesis travel with it, and the customer is told "
            "who has it now and when to expect contact. Tier 2 works "
            "with deeper tools and access; genuinely novel or defective "
            "behavior escalates to Tier 3, which treats the ticket as "
            "field intelligence for the product. Critically, ownership "
            "can stay with Tier 1 while expertise is borrowed - the "
            "swarming variant - so the customer keeps one throat to "
            "choke while specialists contribute behind the scenes. "
            "Escalation rates are measured per tier: a healthy desk "
            "resolves most volume at Tier 1, escalates a minority to "
            "Tier 2, and sends a trickle to Tier 3. When escalation "
            "rates climb, the response is better playbooks and training "
            "at the lower tier, not blame."
        ),
        "key_points": [
            "The desk is the single point of contact; tiers ration expertise so the cheapest capable tier resolves each matter.",
            "Tier 1 owns triage and the documented playbook; Tier 2 brings specialist depth; Tier 3 brings engineering authority.",
            "Escalation is a warm handoff with full history and a named new owner, never a cold bounce.",
            "Swarming lets Tier 1 keep ownership while borrowing expertise, giving the customer one accountable owner.",
            "Escalation rates per tier are the health metric; climbing rates mean the lower tier needs better playbooks.",
        ],
        "requirements": [
            "A documented playbook per tier stating exactly what each tier owns and when escalation is mandatory.",
            "Time boxes at each tier before escalation review, so tickets cannot stall silently.",
            "Warm handoff discipline: history, attempts, and hypothesis travel with every escalation.",
            "One named owner visible to the customer at all times, even when specialists swarm behind the scenes.",
            "Escalation rate reporting per tier with a standing improvement loop on the playbooks.",
        ],
        "standards": [
            "Tier definitions, skills, and authority limits are published so routing matches capability.",
            "Every escalation records the reason, the from-to tiers, and the handoff summary.",
            "Follow-the-sun and dedicated-desk variants keep the same tier discipline across sites and accounts.",
        ],
        "citations": [CIT_ITIL4, CIT_FITZ, CIT_COPC],
        "sig_lens": (
            "The Signature read: the tiers are the ranks of the "
            "covenant's guard. Where public practice staffs levels, the "
            "Signature Service Covenant posts its watch - the outer "
            "guard swift with the common remedies, the inner guard deep "
            "in craft, the high council for the unprecedented - and "
            "every escalation is a torch passed hand to hand, never "
            "dropped in the dark."
        ),
    },
    {
        "key": "product_history",
        "name": "Product History and Installed Base Records",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Product history is the memory of what the customer owns: "
            "every unit, license, subscription, and configuration "
            "attached to the account, with purchase date, version, "
            "serial or key, warranty terms, and the full trail of "
            "repairs, replacements, and upgrades. The installed base is "
            "the aggregate of all of it across customers - the fleet "
            "the organization is responsible for. This record is what "
            "makes service intelligent: the agent who sees that the "
            "failing unit is three months old with a known defect in "
            "its batch diagnoses in seconds what takes an hour blind. "
            "Entitlements ride on product history: warranty coverage, "
            "support plan level, and SLA tier are determined by what "
            "the customer owns and when, not by what they claim. "
            "Version tracking matters because most issues are "
            "version-specific - the bug fixed in 4.2, the incompatibility "
            "introduced in 5.0 - and the fix for a ticket often starts "
            "with 'which version are you on'. The installed base also "
            "drives the business: upgrade campaigns target the versions "
            "with known issues, recalls target the serial ranges with "
            "the defect, and end-of-life notices go to the owners of "
            "retiring products before they discover it mid-crisis."
        ),
        "how_it_works": (
            "At sale or activation, the product instance is registered "
            "to the account with its identifiers, version, and "
            "entitlement terms, and the warranty clock starts from the "
            "documented trigger - usually delivery or activation. Every "
            "service event appends to the instance history: repairs with "
            "parts used, replacements with new serials linked to old, "
            "firmware or version changes, and entitlement changes like "
            "support plan upgrades. When a ticket arrives, the product "
            "record auto-attaches by serial, account, or customer "
            "selection, and the agent sees age, version, warranty "
            "status, and prior events before asking a single question. "
            "Entitlement checks run automatically: in-warranty repairs "
            "flow to no-charge fulfillment, out-of-warranty offers the "
            "paid options with the price visible. Aggregations over the "
            "installed base - units by version, failure rates by batch, "
            "warranty exposure by month - feed quality, planning, and "
            "campaign targeting. When a unit is replaced, the old "
            "record is retired with its history preserved and linked "
            "to its successor, so the lineage never breaks."
        ),
        "key_points": [
            "Product history records every owned unit with identifiers, version, warranty, and the full trail of repairs and upgrades.",
            "The installed base is the aggregate fleet, and it makes service intelligent: age, batch, and version diagnose in seconds.",
            "Entitlements are computed from the product record - what coverage applies is determined by data, not by claim.",
            "Version tracking is diagnostic infrastructure, because most issues and fixes are version-specific.",
            "Replacement links old serial to new, preserving lineage so history survives the hardware.",
        ],
        "requirements": [
            "Registration of every product instance to its account at sale or activation with identifiers and entitlement terms.",
            "Automatic attachment of the product record to incoming tickets, with age, version, and warranty visible to the agent.",
            "An append-only service event log per instance: repairs, parts, replacements, version changes.",
            "Entitlement computation that routes in-warranty work to no-charge fulfillment and prices the rest transparently.",
            "Installed-base aggregation by version, batch, and age to feed quality analysis and campaign targeting.",
        ],
        "standards": [
            "Warranty clocks start from a documented trigger event, applied consistently across all records.",
            "Serial and version identity is unique per instance; replacements link predecessor to successor.",
            "End-of-life and recall communications target installed-base slices by version and serial range.",
        ],
        "citations": [CIT_BUTTLE, CIT_OPS, CIT_ISO10002],
        "sig_lens": (
            "The Signature read: product history is the genealogy of "
            "the covenant's gifts. Where public practice tracks assets, "
            "the Signature Service Covenant remembers every thing "
            "entrusted - its birth, its wounds, its healings, its "
            "successors - for a keeper who forgets what was given "
            "cannot honor what is owed."
        ),
    },
    {
        "key": "crm_models",
        "name": "CRM Data Models: Leads, Opportunities, and Accounts",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the service record, CRM carries the commercial "
            "memory: who might buy, who is buying, and who bought. The "
            "lead is the raw possibility - a name with a hint of "
            "interest, unqualified and unowned. Qualification sorts "
            "leads: marketing-qualified leads showed real engagement, "
            "sales-qualified leads survived human review against fit "
            "and need criteria. The opportunity is the qualified deal "
            "in motion, carried through stages - discovery, proposal, "
            "negotiation, close - each with an amount, a probability, "
            "and a date, which together produce the weighted pipeline "
            "the business forecasts from. Conversion to customer "
            "creates the account with its contacts, and the "
            "opportunity's history becomes the account's origin story. "
            "The funnel math is the discipline: conversion rates "
            "between stages reveal exactly where deals die, and the "
            "fix is aimed there instead of at 'more leads'. Service "
            "history feeds this model too - support interactions are "
            "buying signals and churn warnings, which is why the "
            "service and sales records share one customer identity "
            "instead of living in rival systems."
        ),
        "how_it_works": (
            "Leads enter from every source - web forms, events, "
            "referrals, purchased lists - and are scored on fit (right "
            "company, right role) plus behavior (real engagement "
            "signals). Score thresholds route them: hot leads to sales "
            "immediately, warm ones to nurture tracks, cold ones back "
            "to marketing. A salesperson accepts or rejects each "
            "routed lead with a reason, and the rejection reasons are "
            "mined to fix scoring. Accepted leads become opportunities "
            "with a defined sales process: each stage has entry and "
            "exit criteria, so 'proposal' means a written proposal "
            "exists, not a feeling. Stage probabilities weight the "
            "amounts into the forecast, and stalled opportunities - no "
            "stage movement in the stage's expected dwell - get flagged "
            "for review. Won opportunities convert: the account is "
            "created or extended, contacts linked, products registered, "
            "and the service record begins with the full sales history "
            "visible. Lost opportunities keep their loss reason, which "
            "is trended like any other defect data."
        ),
        "key_points": [
            "The commercial memory runs lead to qualified lead to opportunity to account, each stage with defined entry and exit criteria.",
            "Lead scoring on fit plus behavior routes hot leads to sales, warm to nurture, and cold back to marketing.",
            "Opportunity stages carry amount, probability, and date; weighted together they form the forecast.",
            "Funnel conversion rates pinpoint exactly where deals die, aiming fixes at the true leak.",
            "Won deals convert into accounts with products registered and sales history visible to service from day one.",
        ],
        "requirements": [
            "A single customer identity shared by sales and service records, so history and signals never split.",
            "Written qualification criteria and scoring rules, reviewed against actual conversion outcomes.",
            "Stage definitions with verifiable exit criteria, not feelings, for every opportunity stage.",
            "Accept and reject discipline on routed leads with mined rejection reasons feeding scoring fixes.",
            "Loss reasons captured on every lost opportunity and trended like defect data.",
        ],
        "standards": [
            "Forecast weights per stage are calibrated against historical win rates, not optimism.",
            "Stalled-opportunity thresholds per stage trigger review before deals quietly die.",
            "Nurture tracks carry consent records, keeping outreach provably permitted.",
        ],
        "citations": [CIT_BUTTLE, CIT_PEPPERS, CIT_HUGHES],
        "sig_lens": (
            "The Signature read: the funnel is the courtyard before the "
            "covenant hall. Where public practice scores leads, the "
            "Signature Service Covenant weighs suitors - fit of house, "
            "truth of interest - and only the proven enter the hall "
            "where promises are sworn. The forecast is the covenant's "
            "honest accounting of vows likely to be kept."
        ),
    },
    {
        "key": "escalation",
        "name": "Escalation Matrices: Functional and Hierarchical",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "An escalation matrix is the pre-agreed answer to 'who gets "
            "this when it goes wrong': a grid mapping priority and "
            "situation to the next owner, the next authority, and the "
            "time at which the handoff fires. Two axes run through it. "
            "Functional escalation moves the ticket sideways to deeper "
            "expertise - Tier 1 to Tier 2 to Tier 3 - when the matter "
            "exceeds the current tier's skill or authority. "
            "Hierarchical escalation moves it upward to management "
            "when the SLA threatens, the customer demands it, or the "
            "business risk crosses a threshold, bringing authority to "
            "approve exceptions, spend money, or break process. The "
            "matrix sets the timers: a P1 escalates functionally in "
            "fifteen minutes and hierarchically in thirty; a P3 might "
            "get hours before anyone above the agent is involved. Good "
            "matrices also name the triggers beyond time - customer "
            "request, repeat contact on the same matter, social media "
            "exposure, safety implication - because some situations "
            "escalate on meaning, not minutes. The matrix is published "
            "to customers in summary form ('P1 issues reach our duty "
            "manager within 30 minutes'), which turns escalation from a "
            "threat customers wield into a promise they rely on."
        ),
        "how_it_works": (
            "Every ticket carries its matrix position from its "
            "priority: the system computes the functional escalation "
            "deadline (when deeper expertise must be engaged) and the "
            "hierarchical deadline (when management must be informed) "
            "and shows both as countdowns on the ticket. When a "
            "deadline approaches, warnings fire to the owner first; at "
            "expiry, ownership or oversight transfers automatically "
            "with the full history attached - escalation never waits "
            "for someone to remember. The receiving tier or manager "
            "acknowledges within their own time box, and the ticket "
            "records the escalation chain as an auditable trail. "
            "Customers can trigger hierarchical escalation on request, "
            "which is honored promptly rather than treated as an "
            "insult - the data shows requested escalations handled well "
            "recover satisfaction better than suppressed ones. After "
            "resolution, escalated tickets are reviewed: was the "
            "escalation timely, did the matrix fire correctly, and "
            "what does the pattern say about tier capability. Matrix "
            "timers are tuned from this review, tightening where "
            "breaches cluster and loosening where false alarms waste "
            "senior time."
        ),
        "key_points": [
            "The matrix pre-answers who gets the ticket when it goes wrong, on two axes: functional (deeper expertise) and hierarchical (higher authority).",
            "Timers per priority set when each escalation fires, shown as countdowns on the ticket and executed automatically at expiry.",
            "Triggers beyond time - customer request, repeat contact, exposure, safety - escalate on meaning, not just minutes.",
            "Customer-requested escalation is honored promptly; handled well, it recovers satisfaction better than suppression.",
            "Post-resolution review of escalated tickets tunes the matrix from evidence, tightening where breaches cluster.",
        ],
        "requirements": [
            "A published matrix mapping priority to functional and hierarchical escalation owners and timers.",
            "Automatic countdowns on every ticket with warnings before expiry and transfer at expiry.",
            "Warm transfer discipline: full history attached, acknowledgment time-boxed, chain recorded.",
            "A customer-request path to hierarchical escalation that is honored, not punished.",
            "Regular review of escalated tickets to tune timers and spot tier capability gaps.",
        ],
        "standards": [
            "Escalation owners and their authority limits (spend, exception, process-break) are documented per matrix cell.",
            "Every escalation is logged with trigger, from-to, timestamp, and acknowledgment.",
            "The customer-facing summary of escalation commitments matches the internal matrix exactly.",
        ],
        "citations": [CIT_ITIL4, CIT_COPC, CIT_OPS],
        "sig_lens": (
            "The Signature read: escalation is the call up the "
            "covenant's tower. Where public practice routes tickets, "
            "the Signature Service Covenant keeps a sworn chain of "
            "command - every rank knowing when the call comes, what "
            "authority it carries, and that the call is never left "
            "unanswered. The tower stands because every level answers."
        ),
    },
    {
        "key": "core_metrics",
        "name": "Core Metrics: First Response, Resolution, and Handle Time",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Service operations run on a small set of core metrics, and "
            "each one measures a different promise. First response time "
            "measures how fast a human acknowledges the customer - the "
            "promise that 'we hear you'. First contact resolution "
            "measures the share of matters solved without handoff or "
            "callback - the promise of competence. Mean time to resolve "
            "measures how long matters take end to end - the promise of "
            "speed. Average handle time measures the agent's labor per "
            "contact - the cost lever. Reopen rate measures how often "
            "resolutions fail - the quality check. The art is reading "
            "them together, because each is gameable alone: agents "
            "chasing handle time rush customers off the phone and "
            "destroy resolution; chasing first response sends empty "
            "'we got it' replies; chasing resolution time closes "
            "tickets prematurely and spikes reopens. Balanced "
            "scorekeeping pairs every speed metric with a quality "
            "counterweight - handle time with satisfaction, resolution "
            "time with reopen rate - so improvement in one cannot be "
            "bought with damage to another. Targets come from customer "
            "expectation research and demonstrated capability, and they "
            "are always reported with distribution, not just the mean, "
            "because a fine average can hide a miserable tenth "
            "percentile."
        ),
        "how_it_works": (
            "Each metric has a locked definition computed from the "
            "ticket event log. First response time is creation to first "
            "human reply, excluding auto-acknowledgments. First contact "
            "resolution is resolved-without-reopen and without "
            "escalation or callback, divided by all resolved tickets. "
            "Mean time to resolve is creation to confirmed resolution, "
            "with the clock rules applied. Average handle time sums "
            "talk, hold, and after-call work per contact. Reopen rate is "
            "reopened divided by resolved inside the confirmation "
            "window. Dashboards show each metric by priority, channel, "
            "team, and agent, with trend lines and percentile bands - "
            "the 90th percentile response time tells the truth the mean "
            "hides. Alerts fire on drift, not on single bad tickets, "
            "and metric reviews pair every number with its "
            "counterweight: if handle time falls while satisfaction "
            "falls faster, the operation knows the gain was theft. "
            "Definitions are versioned and published, so a metric "
            "means the same thing this quarter as last."
        ),
        "key_points": [
            "Each core metric measures a different promise: response measures acknowledgment, FCR measures competence, MTTR measures speed, handle time measures cost, reopens measure quality.",
            "Every speed metric is gameable alone, so each is paired with a quality counterweight that exposes the gaming.",
            "Definitions are locked and computed from the event log - first human reply, no auto-acknowledgment inflation.",
            "Reporting shows distributions and percentiles, because a fine mean can hide a miserable tenth percentile.",
            "Targets come from customer expectation research and demonstrated capability, versioned and published.",
        ],
        "requirements": [
            "Locked, published definitions for FRT, FCR, MTTR, AHT, and reopen rate, computed from timestamps.",
            "Paired scorekeeping: every efficiency metric reported alongside its quality counterweight.",
            "Slicing by priority, channel, team, and agent with trend lines and percentile bands.",
            "Drift alerts on sustained movement, not on single tickets, to avoid metric panic.",
            "Versioned metric definitions so quarter-to-quarter comparisons stay honest.",
        ],
        "standards": [
            "Auto-replies never count as first response; only human acknowledgment starts the customer-visible clock.",
            "Reopen windows are fixed per priority and published, keeping FCR comparable across periods.",
            "Handle time includes talk, hold, and after-call work - partial measures are labeled as such.",
        ],
        "citations": [CIT_COPC, CIT_OPS, CIT_FITZ],
        "sig_lens": (
            "The Signature read: the metrics are the covenant's "
            "witnesses. Where public practice counts minutes, the "
            "Signature Service Covenant calls witnesses to every oath - "
            "how swiftly the call was answered, how truly the matter "
            "was settled, how rarely the promise broke twice. No "
            "witness may be bribed: speed never testifies against "
            "quality."
        ),
    },
    {
        "key": "knowledge",
        "name": "Knowledge Bases and Self-Service",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The knowledge base is the organization's memory made "
            "searchable: every solved problem, every how-to, every "
            "answer, written once and reused ten thousand times. "
            "Self-service is that memory offered directly to customers "
            "through portals, help centers, and virtual assistants, so "
            "the simple matters resolve without consuming agent time. "
            "The economics are compelling - a self-service resolution "
            "costs a fraction of an agent contact - but only when the "
            "knowledge is genuinely good: customers forgive a portal "
            "that lacks an answer far less than they forgive an agent "
            "who lacks one, because the failure feels like being left "
            "alone with a broken machine. Good knowledge articles share "
            "an anatomy: the symptom in the customer's words, the "
            "cause in plain language, the fix as numbered steps, the "
            "verification that it worked, and metadata - product, "
            "version, date, owner - so stale articles can be found and "
            "fixed. The creation discipline is capture at resolution: "
            "the agent who solved it writes the article while the "
            "knowledge is fresh, a reviewer checks it, and the article "
            "links to the tickets it came from. Deflection is measured "
            "honestly - sessions that resolved without creating a "
            "ticket, confirmed by follow-up - never by assuming every "
            "portal visit replaced a call."
        ),
        "how_it_works": (
            "When a ticket resolves with a reusable solution, the agent "
            "drafts or updates the article from a template: symptom, "
            "cause, steps, verification, metadata. A knowledge reviewer "
            "checks accuracy, clarity, and findability - titles carry "
            "the customer's words, not internal jargon - then "
            "publishes. Articles carry review dates, and ownership is "
            "real: the owning team must re-verify or retire each "
            "article on schedule, because a wrong article is worse than "
            "none. Search is tuned continuously from failed searches - "
            "every query with no good click is a content gap ticket. "
            "Self-service sessions are tracked end to end: article "
            "views, step completion, and whether a ticket followed "
            "within the window. Deflection counts only sessions with "
            "no subsequent ticket and, on samples, confirmed resolution. "
            "The feedback loop is closed by linking: tickets resolved "
            "with an article record which one, so article value is "
            "measured in tickets shortened and deflected, and the best "
            "articles earn their authors recognition."
        ),
        "key_points": [
            "The knowledge base is solved problems written once and reused ten thousand times; self-service offers that memory directly to customers.",
            "Article anatomy is fixed: symptom in customer words, cause plainly, fix as numbered steps, verification, and metadata.",
            "Capture happens at resolution while knowledge is fresh, with review before publishing and real ownership after.",
            "Failed searches become content gap tickets, so the base grows where customers actually look.",
            "Deflection is measured honestly - sessions with no subsequent ticket and confirmed resolution - never assumed from visits.",
        ],
        "requirements": [
            "An article template with symptom, cause, steps, verification, and metadata, used for every article.",
            "Capture-at-resolution discipline: the solver drafts while the knowledge is fresh.",
            "Review-before-publish plus scheduled re-verification with real named owners per article.",
            "Search analytics that convert failed queries into content gaps with owners and dates.",
            "Honest deflection measurement tied to ticket outcomes, not portal traffic.",
        ],
        "standards": [
            "Titles use customer language, verified against actual search terms, not internal terminology.",
            "Stale articles are retired or refreshed on schedule; known-wrong articles are pulled immediately.",
            "Article reuse is tracked per ticket, crediting the knowledge that shortened or deflected the work.",
        ],
        "citations": [CIT_ITIL4, CIT_EFFORTLESS, CIT_OPS],
        "sig_lens": (
            "The Signature read: the knowledge base is the covenant's "
            "library of answered prayers. Where public practice "
            "publishes articles, the Signature Service Covenant inscribes "
            "every solved trouble so no customer ever suffers it alone "
            "twice - the remedy, once earned, belongs to all. Self-service "
            "is the library door left open at every hour."
        ),
    },
    {
        "key": "journey",
        "name": "Customer Journey Mapping",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A customer journey map is the customer's experience drawn "
            "as they live it: a sequence of stages from first awareness "
            "through purchase, onboarding, use, support, renewal, and "
            "advocacy, with each stage showing what the customer does, "
            "thinks, and feels, which touchpoints they meet, and where "
            "the experience breaks. Organizations naturally see "
            "themselves as departments; customers experience one "
            "continuous journey, and the map is the tool that forces "
            "the inside-out view to confront the outside-in reality. "
            "Building one starts with research, not assumptions: "
            "interviews, ticket analysis, survey verbatims, and "
            "behavioral data reveal the actual path, including the "
            "workarounds customers invented for the organization's "
            "failures. Each stage gets the customer's goal, the "
            "touchpoints involved, the emotion curve, and the pain "
            "points with their frequency and severity. The map's power "
            "is prioritization: it shows which broken moments matter "
            "most - the onboarding confusion that drives week-one "
            "churn, the billing surprise that poisons renewals - so "
            "improvement money goes where the journey bleeds. Maps are "
            "living documents, refreshed as the journey changes, and "
            "the best organizations keep one map per key persona, "
            "because the enterprise buyer's journey and the household "
            "buyer's journey break in different places."
        ),
        "how_it_works": (
            "A cross-functional team assembles the evidence first: "
            "support tickets tagged by journey stage, satisfaction "
            "scores along the timeline, churn reasons, and direct "
            "customer interviews that capture language and emotion. "
            "The map is drawn as stages across the top and lanes "
            "beneath - actions, thoughts, feelings, touchpoints, pain "
            "points, opportunities - with the emotion curve making the "
            "valleys visible at a glance. Each pain point is scored by "
            "frequency times severity, producing the prioritized fix "
            "list, and each fix gets an owner and a target journey "
            "metric. Moments of truth - the handful of interactions "
            "that disproportionately decide loyalty, like the first "
            "support call or the renewal conversation - are marked and "
            "designed deliberately, with extra training and recovery "
            "authority. The map is validated back with customers "
            "before it drives investment, because an unvalidated map "
            "is just the organization's prejudices in diagram form. "
            "Refresh cadence is set - typically annual with quarterly "
            "metric check-ins - so the map tracks the journey as it "
            "actually evolves."
        ),
        "key_points": [
            "The journey map draws the experience as the customer lives it - stages, actions, thoughts, feelings, touchpoints, breaks - confronting the inside-out view with outside-in reality.",
            "Research precedes drawing: tickets, verbatims, interviews, and behavioral data reveal the actual path including customer-invented workarounds.",
            "Pain points scored by frequency times severity produce the prioritized fix list, aiming improvement money where the journey bleeds.",
            "Moments of truth - the few interactions that disproportionately decide loyalty - are marked and designed deliberately.",
            "Maps are validated with customers before driving investment and refreshed on cadence, one per key persona.",
        ],
        "requirements": [
            "Evidence-first construction: ticket analysis, scores, churn reasons, and interviews before any drawing.",
            "A standard lane structure - actions, thoughts, feelings, touchpoints, pains, opportunities - with a visible emotion curve.",
            "Scored pain points with owners and target journey metrics for each prioritized fix.",
            "Identified moments of truth with deliberate design, training, and recovery authority.",
            "Customer validation of the map and a refresh cadence so it tracks the real journey.",
        ],
        "standards": [
            "Journey stages use customer language for stage names, verified in research, not department names.",
            "Pain scoring uses consistent frequency and severity scales so maps stay comparable across personas.",
            "The map links each pain point to the tickets, scores, and verbatims evidencing it.",
        ],
        "citations": [CIT_LEMON, CIT_SERVICES, CIT_PEPPERS],
        "sig_lens": (
            "The Signature read: the journey map is the pilgrim's chart "
            "of the covenant road. Where public practice diagrams "
            "touchpoints, the Signature Service Covenant walks the road "
            "beside the traveler - marking where the path is smooth, "
            "where travelers stumble, where the guides must stand ready. "
            "No oath is kept by those who never walked the road."
        ),
    },
]

# ---- chunk 3: entries 17-24 appended below ----
ENTRIES += [
    {
        "key": "csat",
        "name": "CSAT: Measuring Customer Satisfaction",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Customer Satisfaction Score is the direct question - 'how "
            "satisfied were you with this interaction', answered on a "
            "1-to-5 scale - and the headline number is the top-two-box "
            "share: the percentage answering 4 or 5. Its virtue is "
            "immediacy and clarity: asked right after the ticket "
            "closes, it measures the specific experience while the "
            "memory is fresh, and it is simple enough that customers "
            "actually answer. The methodology discipline is what makes "
            "it trustworthy. Surveys go to a defined sample - commonly "
            "every nth resolved ticket or a random daily slice - not "
            "to whoever the agent feels like asking, because selective "
            "surveying manufactures a happy score. The question wording "
            "is locked: changing 'satisfied with the support you "
            "received' to 'satisfied with your agent' measures a "
            "different thing and breaks the trend. Response bias is "
            "acknowledged openly - the delighted and the furious answer "
            "more than the mildly content - so CSAT is read as a "
            "trend and a comparison across teams, not as an absolute "
            "truth about all customers. And the score is always paired "
            "with the verbatim: the number says how much, only the "
            "customers' words say what to fix."
        ),
        "how_it_works": (
            "On ticket resolution, the survey fires automatically to "
            "the sampled customers - by rule, not by agent choice - "
            "through the ticket's channel: an email with the single "
            "question and an optional comment box, a one-tap prompt "
            "in chat, an IVR keypress after the call. Responses land "
            "on the ticket and the customer record with the agent, "
            "team, matter type, and resolution attached as context. "
            "The top-two-box percentage aggregates by team, agent "
            "(with volume minimums), matter type, and period, always "
            "shown with response counts and the trend line. Low "
            "scores trigger the same closed loop as detractors: the "
            "owner reviews the ticket, contacts the customer where "
            "warranted, and fixes what was fixable. Comment verbatims "
            "are coded to themes monthly, and the theme frequencies "
            "join the improvement backlog. Survey program health is "
            "audited: response rates by segment, score distributions "
            "for coaching spikes, and periodic non-respondent checks "
            "so the operation knows whose silence the score "
            "represents."
        ),
        "key_points": [
            "CSAT asks satisfaction directly on a 1-to-5 scale right after the interaction; the headline is the top-two-box share answering 4 or 5.",
            "Sampling is by rule - every nth ticket or a random slice - never by agent choice, because selective surveying manufactures happiness.",
            "Question wording is locked; changing it measures a different thing and breaks the trend.",
            "Response bias is acknowledged: the delighted and furious answer most, so CSAT is read as trend and comparison, not absolute truth.",
            "The score is always paired with verbatims: the number says how much, only customer words say what to fix.",
        ],
        "requirements": [
            "Automatic post-resolution surveying to a defined sample, fired by rule across the ticket's channel.",
            "Locked question wording with version control, so trends measure experience change, not wording change.",
            "Response capture on the ticket and customer record with agent, team, and matter type context.",
            "Closed-loop follow-up on low scores with owner review and customer contact where warranted.",
            "Program audits: response rates by segment, distribution checks for coaching, non-respondent sampling.",
        ],
        "standards": [
            "Top-two-box (4-5 on the 1-5 scale) is the reported headline, with the full distribution available beside it.",
            "Agent-level scores carry volume minimums before any individual judgment is drawn.",
            "Survey timing is post-resolution; delayed or batched CSAT is labeled so it is not compared to immediate.",
        ],
        "citations": [CIT_VAVRA, CIT_ISO10004, CIT_COPC],
        "sig_lens": (
            "The Signature read: satisfaction is the partner's plain "
            "verdict on the kept oath. Where public practice surveys "
            "CSAT, the Signature Service Covenant asks directly and "
            "listens without flinching - the fours and fives are "
            "honors earned, the low scores are debts acknowledged - "
            "for a covenant that fears its partners' verdict has "
            "already lost their trust."
        ),
    },
    {
        "key": "nps",
        "name": "NPS: The Net Promoter System",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "The Net Promoter Score asks one question - 'how likely are "
            "you to recommend us', answered 0 to 10 - and sorts "
            "respondents into promoters (9-10), passives (7-8), and "
            "detractors (0-6). The score is promoters minus detractors, "
            "ranging from -100 to +100. Its power is not the arithmetic "
            "but the system around it: the question is asked after real "
            "experiences, every response can trigger a closed-loop "
            "follow-up with detractors, and the verbatims are mined for "
            "the reasons behind the number. Research behind the method "
            "found that this single question predicted business growth "
            "better than satisfaction batteries in many industries, "
            "because recommendation requires both satisfaction and "
            "enough enthusiasm to risk one's reputation. The method's "
            "honest limitations are well documented: scores vary by "
            "culture and industry, so benchmarking needs like-for-like "
            "comparisons; the number alone never says what to fix, only "
            "the verbatims do; and gaming - begging for tens, "
            "re-surveying the unhappy - corrupts it like any metric. Run "
            "properly, NPS splits into two rhythms: transactional NPS "
            "after individual interactions, which drives operational "
            "fixes, and relationship NPS on a regular cadence, which "
            "tracks overall loyalty and predicts growth."
        ),
        "how_it_works": (
            "Surveys go out after defined trigger events - a resolved "
            "ticket, a delivered order, a completed onboarding - plus a "
            "relationship survey to a sampled base on cadence. Each "
            "response lands on the customer record with its score, "
            "verbatim, and context, and detractor alerts route to an "
            "owner with a follow-up time box, typically 24 to 48 hours. "
            "The follow-up is a real conversation - acknowledge, "
            "understand, fix, confirm - and its outcome is logged back "
            "against the response, closing the loop. Scores aggregate by "
            "team, journey stage, product, and period, always with "
            "response counts and the verbatim themes beside the number. "
            "Improvement works the themes, not the score: if detractors "
            "cite billing confusion, the billing experience is fixed "
            "and the score follows. Gaming controls are explicit - no "
            "coaching respondents, no selective surveying, audit of "
            "score distributions for unnatural spikes at 10 - because "
            "a gamed NPS is worse than none, hiding the detractors who "
            "are already leaving."
        ),
        "key_points": [
            "One question, 0 to 10: promoters (9-10) minus detractors (0-6) gives a score from -100 to +100.",
            "The system matters more than the arithmetic: trigger-based asking, closed-loop detractor follow-up, and verbatim mining.",
            "Recommendation predicts growth because it requires satisfaction plus enough enthusiasm to risk reputation.",
            "Two rhythms: transactional NPS after interactions drives fixes; relationship NPS on cadence tracks loyalty.",
            "Gaming controls are mandatory - no coaching, no selective surveying - because a gamed score hides departing detractors.",
        ],
        "requirements": [
            "Defined trigger events for transactional surveys plus a sampled relationship cadence.",
            "Detractor alerts routed to owners with a 24 to 48 hour follow-up time box and logged outcomes.",
            "Every response stored on the customer record with score, verbatim, and context.",
            "Reporting that always pairs the score with response counts and verbatim themes by segment.",
            "Written anti-gaming rules with distribution audits for unnatural spikes.",
        ],
        "standards": [
            "The 0-10 scale and promoter/passive/detractor cutoffs follow the published Net Promoter methodology.",
            "Benchmarking compares like-for-like industries and cultures, never raw cross-industry scores.",
            "Closed-loop follow-up is attempted for every detractor, with attempt and outcome recorded.",
        ],
        "citations": [CIT_REICHHELD, CIT_VAVRA, CIT_ISO10004],
        "sig_lens": (
            "The Signature read: the promoter question asks whether the "
            "covenant is worth recommending to kin. Where public "
            "practice computes a score, the Signature Service Covenant "
            "hears a testimony - the promoter swears the oath is good, "
            "the detractor testifies it broke - and every detractor's "
            "testimony is answered personally, for an unanswered witness "
            "becomes an enemy."
        ),
    },
    {
        "key": "ces",
        "name": "CES: Customer Effort Score",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Customer Effort Score measures how hard the customer had "
            "to work to get their matter resolved, usually on a 1-to-7 "
            "scale from 'very easy' to 'very difficult', asked right "
            "after the interaction. The research behind it found that "
            "reducing effort predicts loyalty better than delighting "
            "customers: people do not leave because service was merely "
            "adequate, they leave because it was a painful hassle of "
            "repeats, transfers, and channel-switching. Effort has four "
            "classic drivers: repeat contacts on the same issue, the "
            "customer having to repeat information, transfers between "
            "agents, and being forced to switch channels mid-matter. "
            "CES is the operational complement to NPS and CSAT: where "
            "they ask how the customer feels, CES asks what the "
            "customer endured, and the answers point directly at "
            "process fixes. A low-effort experience is designed, not "
            "accidental - next-issue avoidance (solving the likely "
            "follow-on problem before it is asked), positive language, "
            "and anchoring the customer to the right channel are the "
            "documented techniques. Like all survey metrics it needs "
            "volume discipline: scores are read in aggregate by "
            "journey stage and matter type, never as verdicts on "
            "individual agents from a handful of responses."
        ),
        "how_it_works": (
            "The survey fires immediately after resolution - in the "
            "chat window, at the call's end, in the ticket-closed "
            "email - while the effort is fresh, with the single "
            "effort question and an optional 'what was hardest' "
            "follow-up. Responses attach to the ticket and the "
            "customer record, carrying the channel, agent, and matter "
            "type as context. Analysis slices the average and the "
            "low-effort share (scores 1-2) by journey stage, channel, "
            "and reason code, and the 'what was hardest' verbatims are "
            "coded to the four effort drivers. Improvement targets "
            "the drivers directly: repeat-contact analysis finds the "
            "unresolved first contacts, transfer analysis finds the "
            "routing failures, channel-switch analysis finds the broken "
            "handoff that forced the customer to start over. "
            "Next-issue avoidance is trained explicitly: agents learn "
            "the common follow-on issues per matter type and resolve "
            "them proactively. CES trends are reviewed alongside "
            "repeat-contact rate, because the two should move together "
            "if the measurement is honest."
        ),
        "key_points": [
            "CES asks how hard resolution was, on a 1-to-7 scale right after the interaction; reducing effort predicts loyalty better than adding delight.",
            "Four classic effort drivers: repeat contacts, repeated information, transfers, and forced channel switches.",
            "CES complements NPS and CSAT: they ask how the customer feels, CES asks what the customer endured, pointing at process fixes.",
            "Low effort is designed: next-issue avoidance, positive language, and right-channel anchoring are trained techniques.",
            "Scores are read in aggregate by stage and matter type, never as verdicts on agents from handfuls of responses.",
        ],
        "requirements": [
            "An immediate post-resolution survey with the effort question and a 'what was hardest' follow-up.",
            "Response capture linked to ticket, channel, agent, and matter type for honest slicing.",
            "Coding of effort verbatims to the four drivers, feeding targeted process fixes.",
            "Next-issue-avoidance training per matter type so agents resolve the likely follow-on unasked.",
            "Joint review of CES with repeat-contact rate, confirming the two move together.",
        ],
        "standards": [
            "The effort scale wording follows the published Customer Effort Score methodology for comparability.",
            "Survey timing is immediate post-interaction; delayed CES surveys are labeled as such.",
            "Low-effort share (scores 1-2) is reported alongside the mean, since the mean alone hides the struggling tail.",
        ],
        "citations": [CIT_EFFORTLESS, CIT_VAVRA, CIT_ISO10004],
        "sig_lens": (
            "The Signature read: effort is the weight the covenant lays "
            "on the traveler's back. Where public practice surveys "
            "ease, the Signature Service Covenant weighs every burden - "
            "every repeat, every transfer, every forced new beginning - "
            "and lifts what it can, for a covenant that wearies its "
            "partners will soon have none."
        ),
    },
    {
        "key": "analytics",
        "name": "Support Analytics: Queues, Backlogs, and Throughput",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Support analytics is the mathematics of the queue: how "
            "work arrives, how it waits, how it flows, and where it "
            "sticks. The backlog is the count of open tickets; the "
            "arrival rate is new tickets per hour or day; throughput "
            "is resolved tickets per the same period. When arrivals "
            "exceed throughput, the backlog grows by the difference, "
            "and Little's law gives the honest translation: average "
            "backlog equals arrival rate times average wait, so a "
            "backlog of 90 with 45 arrivals a day means customers wait "
            "about two days on average. Queue analytics slices the "
            "backlog by age buckets, priority, and team, because a "
            "backlog of fresh P4s is healthy while a backlog of aging "
            "P1s is a fire. Flow metrics - touches per ticket, "
            "handoff counts, dwell by state - reveal friction: tickets "
            "with many touches are usually misrouted or under-skilled "
            "at the first touch. Inflow analysis separates the "
            "signal: what share of arrivals are new matters versus "
            "reopens, follow-ups, and misrouted noise, because each "
            "demands a different fix. Done well, analytics turns the "
            "queue from a source of anxiety into an instrument panel "
            "with predictable levers."
        ),
        "how_it_works": (
            "Every ticket event - created, assigned, touched, pended, "
            "resolved, reopened - streams into the analytics store with "
            "timestamps, so arrival curves, age distributions, and "
            "state dwell are computed, not estimated. Dashboards show "
            "the queue health board: backlog by age bucket and "
            "priority, arrivals versus throughput with the gap "
            "highlighted, oldest tickets by owner, and SLA risk counts. "
            "Little's law checks keep the story honest: reported "
            "average waits must reconcile with backlog divided by "
            "arrival rate, and drift between them signals data or "
            "definition problems. Inflow tagging classifies each "
            "arrival as new, reopen, follow-up, or misroute, and each "
            "class gets its own trend and owner - reopens belong to "
            "quality, misroutes to routing rules. Weekly queue reviews "
            "walk the oldest and riskiest tickets one by one, because "
            "aggregates hide the individual customer waiting longest. "
            "Forecasting extends the arrival curves with seasonality, "
            "so staffing and backlog targets are set against predicted "
            "demand, not last month's hope."
        ),
        "key_points": [
            "Backlog, arrival rate, and throughput are the three queue primitives; when arrivals exceed throughput, the backlog grows by the difference.",
            "Little's law translates honestly: average backlog equals arrival rate times average wait.",
            "Age buckets by priority separate the healthy backlog of fresh low-priority work from the fire of aging high-priority work.",
            "Inflow tagging - new, reopen, follow-up, misroute - gives each arrival class its own trend, owner, and fix.",
            "Weekly reviews walk the oldest and riskiest tickets individually, because aggregates hide the longest-waiting customer.",
        ],
        "requirements": [
            "A complete event stream from the ticketing system with timestamps for every state transition.",
            "A queue health board: backlog by age and priority, arrivals versus throughput, oldest tickets, SLA risk.",
            "Little's law reconciliation checks that keep reported waits honest against backlog and arrival data.",
            "Inflow classification with per-class trends and named owners for reopens, follow-ups, and misroutes.",
            "Demand forecasting with seasonality feeding staffing and backlog targets.",
        ],
        "standards": [
            "Age is measured from creation under the published clock rules, consistent with SLA definitions.",
            "Arrival and throughput use identical periods and identical ticket populations, so the gap is real.",
            "Queue definitions are versioned; redefinition restates history or the trend break is labeled.",
        ],
        "citations": [CIT_OPS, CIT_FITZ, CIT_COPC],
        "sig_lens": (
            "The Signature read: the queue is the covenant's waiting "
            "hall, and no one waits unseen. Where public practice "
            "charts backlogs, the Signature Service Covenant numbers "
            "every waiting soul and knows the longest wait by name - "
            "for a promise delayed is a promise tested, and the test "
            "must never be forgotten."
        ),
    },
    {
        "key": "retention",
        "name": "Retention and Churn Analysis",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Retention is the share of customers still with the "
            "organization at period end; churn is the share lost. The "
            "two are the ultimate verdict on the relationship, because "
            "customers vote with renewal and repurchase. Analysis "
            "starts with cohort tables: customers acquired in the same "
            "period are tracked forward, and the retention curve shows "
            "exactly when they leave - the steep early drop that "
            "signals onboarding failure looks very different from the "
            "slow bleed of mature-account neglect, and each demands "
            "its own fix. Churn splits into voluntary (the customer "
            "chose to leave) and involuntary (payment failed, moved "
            "away), and further into avoidable versus unavoidable, "
            "because only the avoidable voluntary churn is the service "
            "organization's to fix. Leading indicators precede the "
            "verdict: declining usage, rising ticket volumes with "
            "falling satisfaction, support avoidance, and complaints "
            "about specific journey stages all show up quarters before "
            "the cancellation. The retention economics close the "
            "argument: even small retention gains compound into large "
            "profit gains because the retained customer's margin "
            "arrives without acquisition cost, which is why retention "
            "analysis sits at the center of the service strategy."
        ),
        "how_it_works": (
            "Cohorts are defined by acquisition period and tracked on "
            "retention curves showing the surviving share at each "
            "subsequent period, with the curve's shape diagnosing the "
            "failure mode. Every churned account gets an exit capture - "
            "reason codes from save-desk conversations, cancellation "
            "surveys, and payment-failure records - coded into "
            "voluntary versus involuntary and avoidable versus "
            "unavoidable. Save rates are measured on the avoidable "
            "voluntary segment: offers made, accepts, and the retained "
            "revenue, so the save desk is judged on profit, not on "
            "discounts given. Leading-indicator models score live "
            "accounts on usage decline, ticket sentiment, and payment "
            "health, and the at-risk list routes to proactive outreach "
            "with the specific remedy matched to the signal. Retention "
            "reporting always shows the rate alongside the absolute "
            "numbers and the revenue retained, because a steady rate "
            "on a shrinking base is not success."
        ),
        "key_points": [
            "Retention is the share still present; churn the share lost - the ultimate verdict on the relationship, voted with renewals.",
            "Cohort retention curves reveal when customers leave, and the shape diagnoses onboarding failure versus mature neglect.",
            "Churn splits voluntary versus involuntary and avoidable versus unavoidable; only avoidable voluntary churn is service's to fix.",
            "Leading indicators - usage decline, ticket sentiment falls, support avoidance - signal quarters before cancellation.",
            "Small retention gains compound into large profit gains because retained margin arrives without acquisition cost.",
        ],
        "requirements": [
            "Cohort definitions by acquisition period with retention curves tracked forward every period.",
            "Exit capture on every churned account with coded reasons split voluntary/involuntary and avoidable/unavoidable.",
            "Save-desk measurement on profit retained, not discounts given, for the avoidable voluntary segment.",
            "A live at-risk scoring model on usage, sentiment, and payment health routing to proactive outreach.",
            "Reporting that pairs rates with absolutes and revenue retained, so base shrinkage cannot hide.",
        ],
        "standards": [
            "Churn definitions (logo versus revenue, gross versus net) are fixed and labeled on every report.",
            "Cohort periods and windows are consistent, keeping curves comparable across acquisition periods.",
            "Exit reason codes come from a controlled list, enabling true trending of why customers leave.",
        ],
        "citations": [CIT_GRIFFIN, CIT_BUTTLE, CIT_CLV],
        "sig_lens": (
            "The Signature read: churn is the breaking of the covenant, "
            "and every break is mourned and studied. Where public "
            "practice counts lost logos, the Signature Service Covenant "
            "asks why each partner departed - and for every avoidable "
            "parting, the covenant reforms itself, for the oath is to "
            "keep, not merely to count."
        ),
    },
    {
        "key": "segmentation",
        "name": "Customer Segmentation: RFM and Value Tiers",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Segmentation is the honest admission that customers differ, "
            "so they should be treated differently - by value, by need, "
            "and by behavior. The classic behavioral model is RFM: "
            "recency (how recently they bought), frequency (how often), "
            "and monetary value (how much), each scored into quintiles "
            "and combined into segments with plain names - champions, "
            "loyal, at-risk, hibernating, lost. Value tiers translate "
            "segments into service policy: top-tier accounts get named "
            "agents, proactive outreach, and escalation uplifts, while "
            "low-value high-cost segments get efficient self-service "
            "paths. Needs-based segmentation cuts the other way: the "
            "technically sophisticated customer wants APIs and "
            "documentation, the time-poor one wants done-for-you "
            "service, and sending each the other's experience is a "
            "loyalty tax. The discipline's guardrails matter: segments "
            "must be reachable (you can actually treat them "
            "differently), substantial (worth the operational cost), and "
            "stable enough to plan against. Re-segmentation runs on "
            "cadence, because customers migrate between segments as "
            "their behavior changes, and a segment model frozen in "
            "2022 is a museum piece."
        ),
        "how_it_works": (
            "Transaction and interaction history feeds the RFM engine: "
            "recency as days since last purchase, frequency as "
            "transactions per period, monetary as total or average "
            "value, each ranked into quintiles across the base. The "
            "three digits combine into segment codes mapped to names "
            "and playbooks - 555 are champions, 111 are lost, and the "
            "migrating bands like 355 are at-risk former champions "
            "worth saving. Value tiers overlay margin and tenure, "
            "setting the service policy per tier: routing priority, "
            "proactive contact cadence, and escalation uplift rules. "
            "Needs-based overlays come from survey and behavioral "
            "signals - support channel preference, self-service "
            "success, feature usage - and tune the experience within "
            "the tier. Segment migration is tracked period to period: "
            "the flow from loyal to at-risk is the early warning, and "
            "win-back campaigns target the hibernating with the offer "
            "matched to their last known need. Every campaign and "
            "service change reports results by segment, so the "
            "organization learns which levers move which customers."
        ),
        "key_points": [
            "RFM scores recency, frequency, and monetary value into quintiles, combining into named segments from champions to lost.",
            "Value tiers turn segments into service policy: routing priority, proactive cadence, and escalation uplifts per tier.",
            "Needs-based overlays tune the experience within tiers, because the sophisticated and the time-poor want different service.",
            "Segments must be reachable, substantial, and stable; re-segmentation runs on cadence as customers migrate.",
            "Migration tracking - especially loyal to at-risk flows - is the early warning system for churn.",
        ],
        "requirements": [
            "Complete transaction and interaction history feeding RFM scoring on consistent definitions.",
            "A segment-to-playbook map: named segments with defined service policies per tier.",
            "Needs-based overlays from behavioral and survey signals tuning experience within tiers.",
            "Period-to-period migration tracking with win-back campaigns aimed at hibernating segments.",
            "By-segment reporting on every campaign and service change, learning which levers move whom.",
        ],
        "standards": [
            "Quintile breaks are recomputed on cadence and published, so segment membership stays meaningful as the base shifts.",
            "Value tier definitions state the exact service commitments per tier, matching what customers are told.",
            "Segment models are validated against actual behavior differences before driving policy.",
        ],
        "citations": [CIT_HUGHES, CIT_BUTTLE, CIT_PEPPERS],
        "sig_lens": (
            "The Signature read: segmentation is knowing each partner's "
            "station and need. Where public practice scores quintiles, "
            "the Signature Service Covenant learns its people - the "
            "steadfast champions honored, the wavering sought, the "
            "sleeping awakened - and no partner is treated as a "
            "stranger, for the covenant knows its own."
        ),
    },
    {
        "key": "recovery",
        "name": "Complaint Handling and Service Recovery",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Service recovery is what happens after the failure: the "
            "complaint is received, the wrong is acknowledged, the fix "
            "is delivered, and the relationship is repaired. Its "
            "founding paradox is that customers who suffered a failure "
            "and experienced excellent recovery can end up more loyal "
            "than customers who never had a problem - the recovery "
            "proved the organization's character under pressure. But "
            "the paradox is fragile: it holds only for genuine, "
            "well-handled recoveries, and organizations that chase it "
            "by tolerating failures learn the wrong lesson. Effective "
            "complaint handling follows a fixed anatomy: listen without "
            "interruption, acknowledge the specific harm, apologize "
            "sincerely for the organization's part, fix the problem, "
            "offer fair compensation proportional to the harm, and "
            "follow up to confirm. Complaints are also intelligence: "
            "each one is coded by cause, and the cause frequencies feed "
            "the improvement system, because a complaint fixed for one "
            "customer but left systemic is a promise to fail the next "
            "hundred. Recovery authority is pushed to the front line - "
            "agents empowered to compensate within bands without "
            "manager approval - since speed is the soul of recovery "
            "and escalation queues kill it."
        ),
        "how_it_works": (
            "Complaints arrive through every channel and are flagged "
            "as complaints distinctly from general requests, because "
            "they carry legal, regulatory, and reputational weight. "
            "The handling agent follows the recovery anatomy and works "
            "inside empowerment bands: standard compensation - credits, "
            "fee waivers, replacements - approved on the spot up to "
            "published limits, larger remedies escalated with a "
            "recommendation. Every complaint gets a cause code from the "
            "controlled list, and the cause frequencies are reviewed "
            "with the improvement team on cadence. Recovery quality is "
            "measured by post-recovery satisfaction and by the "
            "complaint-to-compliment conversion on the affected "
            "accounts. Follow-up is mandatory: the agent or owner "
            "contacts the customer after the fix to confirm the "
            "resolution held and the relationship is whole. Systemic "
            "causes graduate from complaint handling to problem "
            "management, where the permanent fix is owned and tracked, "
            "and the complaint record links forward so the customer "
            "can be told when the root cause is truly gone."
        ),
        "key_points": [
            "The service recovery paradox: genuinely excellent recovery can leave customers more loyal than no failure at all - but only when the recovery is real.",
            "Complaint anatomy is fixed: listen, acknowledge the specific harm, apologize sincerely, fix, compensate fairly, follow up.",
            "Every complaint is cause-coded intelligence feeding the improvement system; fixing one customer while leaving the systemic cause is a promise to fail the next hundred.",
            "Recovery authority sits with the front line inside empowerment bands, because speed is the soul of recovery.",
            "Follow-up after the fix confirms the resolution held and the relationship is whole, not just the ticket closed.",
        ],
        "requirements": [
            "Complaint flagging distinct from general requests, with the legal and reputational handling it requires.",
            "Published empowerment bands letting agents compensate on the spot up to defined limits.",
            "Cause coding on every complaint from a controlled list, reviewed with improvement owners on cadence.",
            "Mandatory post-recovery follow-up confirming the fix held and the relationship recovered.",
            "Graduation of systemic causes to problem management with the customer informed when truly fixed.",
        ],
        "standards": [
            "Complaint handling follows ISO 10002 guidance on accessibility, responsiveness, and objectivity.",
            "Compensation bands and approval authorities are documented and auditable.",
            "Recovery satisfaction is measured after the follow-up, not at the moment of the fix.",
        ],
        "citations": [CIT_ISO10002, CIT_SERVICES, CIT_PROFIT],
        "sig_lens": (
            "The Signature read: recovery is the covenant's atonement. "
            "Where public practice processes complaints, the Signature "
            "Service Covenant makes amends - the wrong named, the "
            "amends swift, the follow-up certain - for an oath broken "
            "and nobly mended can bind tighter than an oath never "
            "tested."
        ),
    },
    {
        "key": "major_incident",
        "name": "Major Incident Management",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A major incident is the failure too big for the normal "
            "queue: the outage affecting thousands, the data "
            "corruption, the safety-impacting defect. It gets its own "
            "process because normal ticketing optimizes for fairness "
            "across many matters, while a major incident demands total "
            "focus, command structure, and communication cadence. The "
            "response runs on an incident commander model: one person "
            "owns coordination, technical leads own diagnosis and "
            "mitigation, a communications lead owns customer and "
            "internal updates, and everyone else executes. The first "
            "priority is mitigation - stop the bleeding with "
            "workarounds, failover, or rollback - while root cause "
            "analysis runs in parallel without blocking restoration. "
            "Communication is the product during a major: status pages "
            "updated on a fixed cadence, even when the update is 'no "
            "change yet', because silence breeds rumor faster than bad "
            "news breeds panic. After restoration comes the blameless "
            "postmortem, which asks what the system allowed rather "
            "than who failed, and produces action items with owners "
            "and dates. Organizations are judged less by whether "
            "majors happen - they do - than by detection speed, "
            "mitigation speed, communication honesty, and whether the "
            "same major ever happens twice."
        ),
        "how_it_works": (
            "Declaration criteria are written in advance - impact "
            "thresholds, safety triggers, executive judgment - so "
            "declaring a major is a fast decision, not a debate. On "
            "declaration, the bridge opens, roles are assigned from "
            "the on-call roster, and the ticket becomes the major "
            "incident record linking all customer-impacted tickets as "
            "children. The commander runs short operational cycles: "
            "assess, decide, act, communicate, typically on fifteen to "
            "thirty minute cadences, with the communications lead "
            "publishing status on the fixed external cadence. "
            "Mitigation actions - rollback, failover, workaround - are "
            "logged with timestamps for the timeline. When service is "
            "restored and verified, the major moves to review: the "
            "blameless postmortem reconstructs the timeline, finds the "
            "contributing causes across technology, process, and "
            "human factors, and records action items in the "
            "improvement register with owners and due dates. Customer "
            "communication closes with the honest postmortem summary: "
            "what happened, what it meant for them, and what changes "
            "so it does not recur. Repeat majors of the same cause "
            "escalate to executive ownership of the permanent fix."
        ),
        "key_points": [
            "Major incidents get their own process - command structure, total focus, communication cadence - because the normal queue optimizes for fairness, not for fire.",
            "The incident commander model separates coordination, technical work, and communications into clear roles.",
            "Mitigation comes first and runs in parallel with root cause analysis, which never blocks restoration.",
            "Communication on a fixed cadence, even with no change to report, because silence breeds rumor faster than bad news breeds panic.",
            "The blameless postmortem asks what the system allowed, produces owned action items, and repeat causes escalate to executive ownership.",
        ],
        "requirements": [
            "Written declaration criteria so calling a major is fast, not debated.",
            "An on-call roster with commander, technical, and communications roles staffed around the clock.",
            "A major incident record linking all impacted customer tickets as children of one coordinated response.",
            "Fixed external communication cadence with honest status, including no-change updates.",
            "Blameless postmortems with action items in the improvement register, owned and dated.",
        ],
        "standards": [
            "Postmortems are blameless by rule: findings address system, process, and tooling, never individual fault.",
            "Timelines are reconstructed from logs with detection, mitigation, and restoration timestamps.",
            "Customers receive the honest postmortem summary: what happened, their impact, and the prevention plan.",
        ],
        "citations": [CIT_ITIL4, CIT_OPS, CIT_ISO20000],
        "sig_lens": (
            "The Signature read: the major incident is the covenant "
            "under siege. Where public practice opens a bridge, the "
            "Signature Service Covenant sounds the alarm and mans the "
            "walls - one commander, every hand at its post, the town "
            "crier honest at every bell - and afterward the council "
            "asks not whom to blame but how the walls shall be made "
            "stronger."
        ),
    },
    {
        "key": "wfm",
        "name": "Workforce Management: Forecasting and Scheduling",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Workforce management answers how many agents with which "
            "skills must be working at each hour so the queue meets "
            "its service targets without paying for idle hands. It "
            "runs in three movements. Forecasting predicts contact "
            "volumes per interval from history, seasonality, marketing "
            "calendars, and known events, because next Tuesday's demand "
            "is mostly last Tuesday's plus the product launch. "
            "Staffing translates forecast volumes into required agents "
            "using queueing mathematics - Erlang C for the classic "
            "phone queue, adapted models for chat concurrency and "
            "asynchronous email - computing how many agents achieve "
            "the target service level at the target handle time. "
            "Scheduling fits real humans into those requirements "
            "across shifts, breaks, skills, and labor rules, and "
            "intraday management adjusts in real time as actuals "
            "deviate from forecast. The mathematics carries a stern "
            "warning: queueing is non-linear, so being ten percent "
            "understaffed does not mean ten percent worse service - "
            "it can mean collapse, as waits explode when utilization "
            "nears capacity. Shrinkage - the share of paid time lost "
            "to breaks, training, sickness, and meetings - is applied "
            "honestly, because scheduling to the raw requirement "
            "guarantees understaffing."
        ),
        "how_it_works": (
            "Forecasting models blend historical interval volumes with "
            "seasonal indices, trend, and event calendars, producing "
            "per-interval contact forecasts with confidence bands; "
            "forecast accuracy is tracked as error versus actuals and "
            "the models retuned. The staffing engine applies Erlang C: "
            "from arrival rate and average handle time it computes "
            "offered load in Erlangs, then finds the smallest agent "
            "count whose probability-of-wait and service-level "
            "formulas meet the target - for example, 100 calls an "
            "hour at 180 seconds handle time needs 7 agents for about "
            "74 percent answered within 20 seconds. Shrinkage is then "
            "divided out: if 25 percent of paid time is non-productive, "
            "required bodies equal productive requirement divided by "
            "0.75. Scheduling optimizes shift patterns, skill mixes, "
            "and break placement against the requirement curve under "
            "labor constraints. Intraday analysts watch service level "
            "and queue in real time, pulling levers - voluntary time "
            "off, overtime, skill reallocation, callback offers - when "
            "actuals diverge, and every intervention is logged so its "
            "effectiveness can be judged."
        ),
        "key_points": [
            "Three movements: forecasting predicts interval volumes, staffing translates volumes to agents via queueing math, scheduling fits humans to requirements.",
            "Erlang C computes the agent count meeting the service target from arrival rate and handle time; queueing is non-linear, so small understaffing can collapse service.",
            "Shrinkage - breaks, training, sickness, meetings - is divided out honestly, or the schedule understaffs by construction.",
            "Intraday management adjusts in real time with logged levers: time off, overtime, skill moves, callback offers.",
            "Forecast accuracy is tracked as error versus actuals and the models are retuned, closing the loop.",
        ],
        "requirements": [
            "Interval-level history with seasonal indices, trend, and event calendars feeding the forecast.",
            "A staffing engine implementing Erlang C (and concurrency models for chat) from arrival rate and handle time.",
            "Honest shrinkage factors applied per team and period, reviewed against actual productive time.",
            "Schedules honoring shift, skill, break, and labor constraints while covering the requirement curve.",
            "Intraday monitoring with defined levers and logged interventions for effectiveness review.",
        ],
        "standards": [
            "Service level targets state both the time threshold and the percentage (for example, 80 percent in 20 seconds).",
            "Forecast error is reported per interval class, and systematic bias triggers model review.",
            "Schedule adherence is measured against the published schedule, distinguishing agent-driven from plan-driven variance.",
        ],
        "citations": [CIT_OPS, CIT_FITZ, CIT_COPC],
        "sig_lens": (
            "The Signature read: workforce management is mustering the "
            "covenant's guard for the watches. Where public practice "
            "runs Erlang, the Signature Service Covenant counts the "
            "sentries each bell requires - neither leaving the walls "
            "thin nor wasting strength on empty watches - for the oath "
            "is kept by the right number in the right place at the "
            "right hour."
        ),
    },
]

# ---- chunk 4: entries 25-34 appended below ----
ENTRIES += [
    {
        "key": "qa",
        "name": "Quality Assurance: Scorecards and Calibration",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Quality assurance in service listens to the work itself: "
            "sampled contacts are scored against a scorecard, and the "
            "scores reveal whether the operation delivers what it "
            "promises when nobody is watching the dashboard. The "
            "scorecard breaks quality into weighted dimensions - "
            "greeting and verification, needs assessment, product "
            "knowledge, process compliance, communication skill, "
            "resolution ownership, and closing - with each dimension "
            "defined by observable behaviors, not vibes. Sampling is "
            "stratified: every agent, every channel, every matter type "
            "gets coverage, with extra weight on high-risk and "
            "high-value interactions. Calibration is the discipline "
            "that keeps scoring honest: graders score the same contacts "
            "independently, disagreements are debated to consensus, and "
            "the scorecard definitions are sharpened where graders "
            "diverge. Without calibration, QA measures the grader, not "
            "the agent. Results feed coaching, not punishment: the "
            "score pattern per agent shows exactly which dimension to "
            "develop, and team-level patterns - everyone failing "
            "verification, say - point at process or training failures "
            "rather than people failures. QA closes the loop with the "
            "customer's voice: internal scores are correlated with "
            "satisfaction on the same contacts, and divergence between "
            "them means the scorecard is measuring the wrong things."
        ),
        "how_it_works": (
            "Each period, the sampling engine draws the stratified "
            "sample - commonly three to five contacts per agent per "
            "month across channels and matter types - and assigns them "
            "to certified graders blind to the agent's identity where "
            "practical. Graders score each dimension on its behavior "
            "anchors and the weighted total becomes the contact score; "
            "critical failures like privacy violations trigger "
            "automatic zero regardless of other dimensions. Monthly "
            "calibration sessions have all graders score shared "
            "contacts, and inter-grader variance is tracked: persistent "
            "divergence on a dimension forces a definition rewrite, "
            "not a shrug. Agent results roll into coaching plans owned "
            "by team leads, with the dimension pattern dictating the "
            "development focus and re-measurement confirming progress. "
            "Program-level reporting correlates QA scores with CSAT "
            "and resolution outcomes on matched contacts; when high QA "
            "scores accompany poor satisfaction, the scorecard is "
            "redesigned, because the customer's verdict outranks the "
            "rubric. Scorecard versions are controlled, and rescoring "
            "history on definition change keeps trends honest."
        ),
        "key_points": [
            "QA scores sampled contacts against a weighted scorecard of observable behaviors, revealing delivered quality beneath the dashboards.",
            "Stratified sampling covers every agent, channel, and matter type, weighted toward high-risk and high-value interactions.",
            "Calibration keeps scoring honest: graders score shared contacts, debate divergence, and rewrite definitions where they disagree.",
            "Results feed coaching per agent dimension pattern; team-wide failures point at process, not people.",
            "Internal scores are correlated with customer satisfaction on matched contacts; the customer's verdict outranks the rubric.",
        ],
        "requirements": [
            "A behavior-anchored scorecard with weighted dimensions and automatic-zero critical failures.",
            "Stratified sampling with defined per-agent coverage across channels and matter types.",
            "Certified graders, blind assignment where practical, and monthly calibration with tracked variance.",
            "Coaching plans per agent driven by dimension patterns, with re-measurement of progress.",
            "Correlation of QA scores with satisfaction and outcomes, triggering scorecard redesign on divergence.",
        ],
        "standards": [
            "Scorecard definitions state the observable behavior for each score point, not adjectives.",
            "Calibration variance per dimension is reported; sustained grader divergence forces definition review.",
            "Privacy and compliance dimensions carry automatic failure on violation, regardless of total score.",
        ],
        "citations": [CIT_COPC, CIT_OPS, CIT_ISO10004],
        "sig_lens": (
            "The Signature read: QA is the covenant's inspection of its "
            "own honor. Where public practice scores calls, the "
            "Signature Service Covenant examines its deeds against its "
            "oath - and the examiners themselves are examined, for a "
            "covenant that grades itself crookedly has already broken "
            "faith."
        ),
    },
    {
        "key": "rca",
        "name": "Root Cause Analysis and Problem Management",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Root cause analysis asks why the failure happened instead "
            "of merely fixing what broke, and problem management is the "
            "discipline of running that question to a permanent answer. "
            "Incidents restore service; problems prevent recurrence. "
            "The analysis techniques are deliberately simple: the five "
            "whys drill past symptoms to the actionable cause, fishbone "
            "diagrams spread the search across people, process, "
            "technology, and environment so the favorite suspect does "
            "not win by default, and Pareto analysis of incident "
            "populations shows which few causes produce most of the "
            "pain. A problem record tracks the investigation like a "
            "case: symptoms, hypotheses, evidence, the confirmed root "
            "cause, the workaround in the known error record, and the "
            "permanent corrective action with its owner and date. The "
            "hard part is organizational, not analytical: permanent "
            "fixes compete with feature work for engineering time, so "
            "problem management needs a prioritization rule - usually "
            "incident cost times frequency - and executive backing, or "
            "the known errors accumulate into a museum of diagnosed "
            "but unfixed failures. The payoff compounds: each "
            "eliminated root cause deletes its whole future incident "
            "stream, which is the only true way to reduce support "
            "volume."
        ),
        "how_it_works": (
            "Problem records open on triggers: repeat incidents matching "
            "a pattern, major incident postmortems, or proactive "
            "analysis spotting a rising cause. The investigator "
            "reconstructs the timeline from logs and ticket histories, "
            "applies the five whys or fishbone to generate candidate "
            "causes, and tests each against evidence until one "
            "survives - the root cause is the deepest cause the "
            "organization can actually fix. The known error record is "
            "published immediately with workaround and symptoms, so "
            "the desk benefits before the permanent fix lands. The "
            "corrective action - code fix, process change, supplier "
            "change, training - gets an owner, a date, and a place in "
            "the change process; temporary mitigations are labeled as "
            "such and never allowed to masquerade as fixes. "
            "Prioritization ranks problems by incident cost times "
            "frequency, reviewed with engineering leadership on "
            "cadence. Closure requires verification: the fix is "
            "deployed, the incident stream for that cause is monitored "
            "for a full cycle, and only sustained absence closes the "
            "problem. Trends report problems opened, aged, and closed, "
            "plus the incident volume each closure eliminated."
        ),
        "key_points": [
            "Incidents restore service; problems prevent recurrence - root cause analysis runs the why to a permanent answer.",
            "Five whys drill past symptoms, fishbone diagrams spread the search across cause families, Pareto shows which few causes make most pain.",
            "The known error record publishes the workaround immediately, so the desk benefits before the permanent fix lands.",
            "Prioritization by incident cost times frequency, with executive backing, keeps permanent fixes funded against feature work.",
            "Closure requires verification: fix deployed plus a full cycle with no recurrence of that cause's incident stream.",
        ],
        "requirements": [
            "Problem records with symptoms, hypotheses, evidence, confirmed cause, workaround, and corrective action with owner and date.",
            "Defined opening triggers: repeat incident patterns, major postmortems, proactive cause analysis.",
            "Immediate known error publication with workaround, decoupled from the permanent fix timeline.",
            "Prioritization by cost times frequency, reviewed with engineering leadership on cadence.",
            "Verification-based closure: sustained absence of the cause's incidents over a full cycle.",
        ],
        "standards": [
            "Root cause statements name the deepest fixable cause, evidenced, not the proximate symptom.",
            "Known error records carry workaround, affected versions, and fix status as mandatory fields.",
            "Problem aging is reported like ticket aging; stale investigations escalate to ownership review.",
        ],
        "citations": [CIT_ITIL4, CIT_ISO20000, CIT_OPS],
        "sig_lens": (
            "The Signature read: root cause analysis digs to the "
            "covenant's foundation stone. Where public practice "
            "investigates problems, the Signature Service Covenant "
            "refuses to merely sweep the floor while the beam rots - "
            "it finds the rot, names it, and replaces the beam, for "
            "only the deep fix honors the oath."
        ),
    },
    {
        "key": "voc",
        "name": "Voice of the Customer Programs",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A voice of the customer program is the organization's "
            "systematic listening apparatus: every survey, interview, "
            "verbatim, review, and behavioral signal gathered into one "
            "place, analyzed for themes, and routed to owners who act. "
            "It exists because customers constantly tell the "
            "organization exactly what is wrong - in ticket texts, in "
            "survey comments, in cancellation reasons, in social posts - "
            "and without a listening system that testimony evaporates. "
            "The program blends solicited voice (CSAT, NPS, CES "
            "surveys, interviews, panels) with unsolicited voice "
            "(reviews, social mentions, ticket verbatims), because "
            "each sees what the other misses: surveys measure, "
            "unsolicited voice surprises. Text analytics codes the "
            "unstructured flood into themes with sentiment and "
            "frequency, and the theme dashboard becomes the "
            "organization's shared reality of what customers "
            "experience. The critical discipline is closed loop at "
            "scale: every theme has an owner, every owner has a "
            "response - fix, explain, or consciously accept - and the "
            "response is communicated back where the voice was heard. "
            "Programs die when listening produces reports instead of "
            "actions; they thrive when the theme dashboard drives the "
            "improvement backlog and executives review it like "
            "financials."
        ),
        "how_it_works": (
            "All voice sources stream into one repository with common "
            "tagging: customer, journey stage, product, theme, "
            "sentiment. Solicited surveys run on their cadences with "
            "locked methodology; unsolicited sources are harvested "
            "continuously under the organization's listening policy. "
            "Text analytics - from coded taxonomies to language models "
            "under human review - assigns themes and sentiment, and "
            "analysts validate samples so the machine's themes stay "
            "honest. The theme dashboard ranks issues by volume times "
            "sentiment severity times business impact, producing the "
            "prioritized listening backlog. Each top theme gets an "
            "owner outside the VoC team - the billing theme belongs to "
            "billing leadership - with a response commitment and date. "
            "The inner loop closes individual detractor and complaint "
            "follow-ups; the outer loop closes themes, and closure is "
            "announced back through the channels where customers "
            "spoke. Program health is measured by theme resolution "
            "rate and by the correlation between listening actions "
            "and the movement of the headline metrics."
        ),
        "key_points": [
            "VoC gathers every signal - surveys, interviews, verbatims, reviews, behavioral data - into one analyzed, owned listening system.",
            "Solicited voice measures; unsolicited voice surprises; the program needs both to see the whole truth.",
            "Text analytics codes the unstructured flood into themes with sentiment and frequency, creating the shared reality dashboard.",
            "Every theme gets a non-VoC owner with a response commitment: fix, explain, or consciously accept, communicated back.",
            "Programs thrive when the theme dashboard drives the improvement backlog and executives review it like financials.",
        ],
        "requirements": [
            "A unified voice repository with common tagging across all solicited and unsolicited sources.",
            "Validated text analytics with human-reviewed samples keeping machine themes honest.",
            "A ranked theme dashboard by volume, sentiment severity, and business impact.",
            "Named theme owners outside the VoC team with response commitments and dates.",
            "Two closed loops: individual follow-up on detractors and complaints, and theme-level resolution announced back.",
        ],
        "standards": [
            "Survey methodology is locked and versioned; methodology changes restate or label trend breaks.",
            "Theme taxonomies are controlled and stable enough for trending, flexible enough for emerging issues.",
            "Listening policies state what is harvested, how it is used, and how privacy is protected.",
        ],
        "citations": [CIT_ISO10004, CIT_VAVRA, CIT_PEPPERS],
        "sig_lens": (
            "The Signature read: voice of the customer is the covenant "
            "keeping its ear to the ground of its people's hearts. "
            "Where public practice runs listening programs, the "
            "Signature Service Covenant hears every whisper of its "
            "partners and answers - not with reports, but with deeds - "
            "for an oath-keeper who stops listening has already begun "
            "to forget."
        ),
    },
    {
        "key": "clv",
        "name": "Customer Lifetime Value Modeling",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Customer lifetime value is the present value of all "
            "future profit a customer will generate: the number that "
            "turns 'the customer is valuable' from sentiment into "
            "arithmetic. The standard model multiplies annual margin "
            "by the retention rate and divides by one plus the "
            "discount rate minus retention - a customer yielding $240 "
            "a year in margin, retained at 82 percent, discounted at "
            "10 percent, is worth about $703. The model's power is "
            "decision discipline: acquisition spending is capped by "
            "the CLV of the acquired segment, service investment is "
            "aimed at the customers whose CLV justifies it, and "
            "retention offers are sized against the value at risk. "
            "Segmented CLV - computed per value tier or per cohort - "
            "is where the insight lives, because average CLV hides "
            "the champions worth saving and the chronic loss-makers "
            "worth firing. The honest limitations are stated up "
            "front: retention rates are estimated from history and "
            "shift with strategy, margins move with cost, and the "
            "discount rate is a judgment. Sensitivity analysis shows "
            "which inputs matter - usually retention dominates - and "
            "that is precisely where service investment should go. "
            "CLV is also the bridge to the service profit chain: "
            "every point of retention gained by better service "
            "compounds directly into lifetime value."
        ),
        "how_it_works": (
            "Finance and analytics agree the inputs first: annual "
            "margin per customer or segment (revenue minus true "
            "service and product cost), retention rate from cohort "
            "history, and the discount rate from corporate finance. "
            "The model computes CLV per segment with the standard "
            "formula, and sensitivity runs vary retention and margin "
            "to show the decision-relevant ranges. Acquisition teams "
            "receive CLV-based caps per segment: spend to acquire must "
            "stay below a defined fraction of expected CLV. Service "
            "teams receive the value-at-risk view: the CLV-weighted "
            "at-risk list, so save efforts and proactive outreach "
            "prioritize the highest lifetime value. Retention "
            "initiatives are business-cased in CLV terms: the "
            "projected retention lift times the affected base's CLV, "
            "minus program cost. The model is recalibrated as cohorts "
            "mature - predicted versus actual retention is tracked, "
            "and systematic over-optimism corrects the retention "
            "inputs. Reporting always shows CLV by segment with its "
            "input assumptions visible, never a single blended number "
            "presented as truth."
        ),
        "key_points": [
            "CLV is the present value of all future profit per customer: margin times retention divided by one plus discount rate minus retention.",
            "Decision discipline follows: acquisition spend capped by segment CLV, service aimed where CLV justifies it, save offers sized to value at risk.",
            "Segmented CLV reveals the champions worth saving and the loss-makers worth releasing; averages hide both.",
            "Sensitivity analysis shows retention usually dominates, which is exactly where service investment belongs.",
            "Inputs are estimated and stated openly; predicted versus actual retention is tracked and corrects the model.",
        ],
        "requirements": [
            "Agreed input definitions: true margin per segment, cohort-based retention, finance-set discount rate.",
            "Segmented CLV computation with visible assumptions and sensitivity ranges, never a lone blended number.",
            "CLV-based acquisition caps per segment enforced in marketing spend decisions.",
            "A CLV-weighted at-risk list driving save and proactive outreach prioritization.",
            "Recalibration against matured cohorts, correcting retention inputs where predictions ran optimistic.",
        ],
        "standards": [
            "Margin inputs use fully loaded service and product costs, not revenue alone.",
            "Retention rates come from cohort history with stated windows, not from aspiration.",
            "Model versions and assumption changes are documented so CLV trends stay interpretable.",
        ],
        "citations": [CIT_CLV, CIT_GRIFFIN, CIT_PROFIT],
        "sig_lens": (
            "The Signature read: lifetime value is the covenant's "
            "measure of a partnership's full harvest. Where public "
            "practice discounts cash flows, the Signature Service "
            "Covenant reckons the whole worth of keeping faith across "
            "the years - and spends to keep its partners in proportion "
            "to that worth, for honor invests where loyalty compounds."
        ),
    },
    {
        "key": "predictive",
        "name": "Predictive Churn and Next-Best-Action",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Predictive churn models score every live account on its "
            "probability of leaving, and next-best-action systems "
            "recommend what to do about it - turning retention from "
            "reaction into prevention. The churn model learns from "
            "history: which behavioral signals preceded past churn - "
            "usage decline, ticket sentiment drops, payment wobbles, "
            "support avoidance, contract milestones - and weights them "
            "into a risk score refreshed on cadence. Next-best-action "
            "goes further: for each at-risk customer it recommends the "
            "specific intervention most likely to retain - the "
            "proactive fix for the known issue, the plan better "
            "matched to usage, the executive outreach for the "
            "strategic account - chosen from the playbook of proven "
            "saves. The discipline around the models is what makes "
            "them trustworthy: predictions are validated against "
            "actual churn on holdout data, scores are explainable "
            "enough that an agent can say why a customer is flagged, "
            "and interventions are tested - treated versus control - "
            "so the organization learns what actually saves whom. "
            "Ethics ride along: scores never drive punitive treatment "
            "or discriminatory offers, and customers are never told "
            "they were algorithmically flagged."
        ),
        "how_it_works": (
            "Feature pipelines assemble the signals per account on "
            "schedule: usage trends, ticket volumes and sentiment, "
            "payment health, tenure, segment, and contract dates. The "
            "churn model - from transparent scoring to machine "
            "learning under governance - outputs a risk score and the "
            "top contributing reasons per account, because an "
            "unexplained score is unactionable. The next-best-action "
            "engine maps reason patterns to the intervention playbook: "
            "usage decline triggers the value-review call, ticket "
            "distress triggers the service recovery outreach, payment "
            "wobble triggers the billing assistance path. At-risk lists "
            "route to the right owner - agent, save desk, or account "
            "team - with the recommended action and the customer's "
            "context attached. Every intervention is logged and "
            "measured against control groups, and the win/loss feeds "
            "back into model retraining and playbook updates. Model "
            "performance - precision, recall, and realized save rates - "
            "is reported like any operational metric, and drift "
            "triggers revalidation before the scores quietly rot."
        ),
        "key_points": [
            "Churn models score live accounts on leave probability from behavioral signals; next-best-action recommends the specific proven intervention.",
            "Risk scores must be explainable: the agent needs to say why a customer is flagged, or the score is unactionable.",
            "Interventions are tested treated-versus-control, so the organization learns what actually saves whom.",
            "Reason patterns map to playbook actions: usage decline, ticket distress, and payment wobble each get their matched response.",
            "Model performance is reported operationally and drift triggers revalidation; scores never drive punitive or discriminatory treatment.",
        ],
        "requirements": [
            "Feature pipelines with usage, ticket, payment, tenure, and contract signals refreshed on cadence.",
            "Explainable risk scores with top contributing reasons attached per flagged account.",
            "An intervention playbook mapping reason patterns to proven save actions with named owners.",
            "Treated-versus-control measurement on every intervention feeding model and playbook updates.",
            "Governance: validation on holdout data, drift monitoring, and ethical rules against punitive use.",
        ],
        "standards": [
            "Model inputs exclude protected characteristics; fairness checks run on score distributions.",
            "Customers are never told they were algorithmically flagged; outreach is framed on the observed signal.",
            "Prediction definitions and windows are fixed so precision and recall stay comparable over time.",
        ],
        "citations": [CIT_BUTTLE, CIT_HUGHES, CIT_PEPPERS],
        "sig_lens": (
            "The Signature read: prediction is the covenant's watchman "
            "on the tower, seeing the storm before it breaks. Where "
            "public practice scores churn risk, the Signature Service "
            "Covenant watches its partners' horizons - the dimming "
            "lamp, the cooling hearth - and rides out early with the "
            "right remedy, for prevention is the highest form of "
            "keeping."
        ),
    },
    {
        "key": "omnichannel",
        "name": "Omnichannel Orchestration and Routing",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Omnichannel orchestration is the conductor's work above "
            "the channels: deciding, moment by moment, which customer "
            "goes to which agent on which channel with what context, "
            "so the whole system behaves as one. Routing starts with "
            "skill-based assignment - language, product expertise, "
            "certification, authority level - matching each contact to "
            "an agent genuinely able to resolve it, because misrouted "
            "contacts are the most expensive kind. Priority and value "
            "overlay the skills: the P1 outage and the top-tier "
            "account jump the queue by rule, visibly and auditable. "
            "Channel orchestration decides the channel itself: the "
            "customer starting in chat with a complex billing dispute "
            "is offered the phone with the transcript traveling along, "
            "not left to fail in the wrong medium. Capacity "
            "orchestration balances load across teams and sites in "
            "real time, spilling chat concurrency or overflowing calls "
            "by rule rather than by panic. The conversation record - "
            "one thread across channels, one ticket, one history - is "
            "what makes orchestration feel like one organization to "
            "the customer instead of a federation of queues."
        ),
        "how_it_works": (
            "Every contact enters the routing engine with its "
            "attributes: customer identity and tier, matter type and "
            "priority, channel, language, and required skills. The "
            "engine scores eligible agents on skill match, current "
            "load, and proficiency, then assigns by the configured "
            "strategy - longest-idle among the skilled, or "
            "proficiency-weighted for complex matters. Queue "
            "priority rules order waiting contacts by priority, tier, "
            "and wait time with aging so no contact waits forever. "
            "Channel-switch offers trigger on detected mismatch: long "
            "chat threads with confusion signals get the phone offer "
            "with context attached. Overflow rules cascade by plan: "
            "site to site, team to team, then to callback or "
            "scheduled follow-up, each step logged. Supervisors see "
            "the orchestration board - queues by skill, agent states, "
            "service levels per channel - and can reshape routing in "
            "real time during spikes. Routing decisions are logged "
            "per contact, feeding analysis of misroutes, wait "
            "fairness, and skill utilization that tunes the rules."
        ),
        "key_points": [
            "Orchestration conducts across channels: who goes to which agent on which channel with what context, behaving as one system.",
            "Skill-based routing matches contacts to agents genuinely able to resolve them; misroutes are the most expensive contacts.",
            "Priority and value overlays move urgent and top-tier contacts by visible, auditable rule.",
            "Channel-switch offers rescue customers failing in the wrong medium, with context traveling along.",
            "Capacity orchestration spills load by plan across teams and sites; every routing decision is logged for tuning.",
        ],
        "requirements": [
            "A skill inventory per agent - language, product, certification, authority - kept current and used in routing.",
            "A routing engine scoring skill match, load, and proficiency with configurable assignment strategies.",
            "Queue priority rules with aging, so urgency is honored and no contact waits forever.",
            "Planned overflow cascades across sites and teams, ending in callback or scheduled follow-up, never abandonment.",
            "Per-contact routing logs feeding misroute, fairness, and utilization analysis.",
        ],
        "standards": [
            "Routing rules and priority overlays are published internally and match the customer-facing commitments.",
            "Skill definitions state the verifiable capability required, not seniority alone.",
            "Wait fairness is monitored across segments; systematic disadvantage to any group triggers rule review.",
        ],
        "citations": [CIT_OPS, CIT_FITZ, CIT_COPC],
        "sig_lens": (
            "The Signature read: orchestration is the covenant's "
            "master of the hall, seating every guest rightly. Where "
            "public practice routes contacts, the Signature Service "
            "Covenant ushers each partner to the keeper best able to "
            "serve - by craft, by tongue, by urgency - and no one "
            "waits at the wrong door."
        ),
    },
    {
        "key": "service_catalog",
        "name": "The Service Catalog and Service Design",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The service catalog is the menu of everything the service "
            "organization offers, written for customers: each service "
            "with its description, who it is for, how to request it, "
            "what it costs, how long fulfillment takes, and what "
            "support comes with it. Behind the customer-facing menu "
            "sits the technical catalog with the supporting services, "
            "components, and supplier dependencies that make each "
            "offering real. Service design is the discipline of "
            "creating new catalog entries properly: the service is "
            "defined with its outcomes, the delivery process is "
            "designed end to end, capacity and skills are provisioned, "
            "support processes are readied, and only then is it "
            "published. The catalog prevents the two classic failures: "
            "the invisible service customers never discover, and the "
            "promised service the organization cannot actually "
            "deliver. Fulfillment workflows attach to each catalog "
            "item - the access request that provisions in hours, the "
            "hardware request that ships in days - with tasks, "
            "approvals, and timers predefined. Catalog governance "
            "keeps it honest: every entry has an owner, a review "
            "date, and measured fulfillment performance, and entries "
            "that consistently miss their targets are redesigned or "
            "retired, not left to disappoint."
        ),
        "how_it_works": (
            "New services enter through service design: the business "
            "case, the customer outcomes, the end-to-end process map, "
            "the capacity plan, the support readiness checklist, and "
            "the pilot with real customers. On approval, the catalog "
            "entry is published in customer language with request "
            "paths, fulfillment targets, and pricing, while the "
            "technical catalog records the dependencies and the "
            "supporting services. Each request for a catalog item "
            "spawns a fulfillment workflow with its predefined tasks, "
            "approvals, and timers - standard requests flow fast "
            "because the decisions were made at design time. "
            "Fulfillment performance per catalog item is measured "
            "against its published target and reviewed with the item "
            "owner; misses trigger redesign of the workflow or the "
            "target. Retired services go through end-of-life: "
            "customers are notified, migration paths offered, and the "
            "entry archived with its history. The catalog is "
            "audited against reality - mystery requests and fulfillment "
            "sampling confirm the menu matches the kitchen."
        ),
        "key_points": [
            "The service catalog is the customer-facing menu: every service with description, audience, request path, cost, fulfillment time, and support.",
            "The technical catalog behind it records supporting services and dependencies that make each offering real.",
            "Service design creates catalog entries properly: outcomes, end-to-end process, capacity, support readiness, then publication.",
            "Fulfillment workflows with predefined tasks, approvals, and timers make standard requests flow fast.",
            "Catalog governance - owners, review dates, measured performance, redesign or retirement - keeps the menu honest.",
        ],
        "requirements": [
            "A customer-language catalog entry for every offered service with request path, target, and price.",
            "A technical catalog mapping each offering to its supporting services and dependencies.",
            "A service design process with business case, process map, capacity plan, readiness checklist, and pilot.",
            "Predefined fulfillment workflows per catalog item with tasks, approvals, and timers.",
            "Owner, review date, and performance measurement per entry, with redesign or retirement on chronic misses.",
        ],
        "standards": [
            "Catalog entries are written for customers first; internal jargon is translated, not published.",
            "Fulfillment targets are set from demonstrated capability and reviewed against performance.",
            "End-of-life follows a defined path: notice, migration, archive - never silent disappearance.",
        ],
        "citations": [CIT_ITIL4, CIT_SERVICES, CIT_ISO20000],
        "sig_lens": (
            "The Signature read: the service catalog is the covenant's "
            "published vows. Where public practice lists offerings, "
            "the Signature Service Covenant sets its promises in the "
            "open - each vow named, priced, timed - so every partner "
            "knows what may be asked and what shall be delivered. No "
            "hidden vows, no hollow ones."
        ),
    },
    {
        "key": "improvement",
        "name": "Continual Improvement and the Seven-Step Process",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Continual improvement is the discipline of getting better "
            "on purpose instead of by accident: a register of "
            "improvement ideas, each with an owner, an expected "
            "benefit, and a date, worked through in priority order "
            "forever. The seven-step improvement process gives the "
            "rhythm: identify the strategy for improvement, define "
            "what will be measured, gather the data, process it into "
            "information, analyze for insight, present it for "
            "decisions, and implement the improvement - then begin "
            "again. Improvement ideas come from everywhere the "
            "operation already measures: complaint causes, QA "
            "patterns, queue analytics, VoC themes, postmortem "
            "actions, and agent suggestions from the people living "
            "the process. Prioritization weighs benefit against "
            "effort with strategic alignment as the tiebreaker, and "
            "the register is visible so good ideas are never lost to "
            "a manager's notebook. Each implemented improvement is "
            "measured against its expected benefit - did handle time "
            "actually fall, did reopens actually drop - and the "
            "verified wins are communicated, because an improvement "
            "culture starves without visible proof that improvement "
            "works. Maturity is judged by whether improvement is a "
            "project with an end date or a habit with a cadence."
        ),
        "how_it_works": (
            "The improvement register holds every idea with its "
            "source, owner, expected benefit in operational or "
            "financial terms, effort estimate, and target date. On "
            "cadence - usually monthly - the improvement board "
            "reviews the register: new ideas are scored on benefit, "
            "effort, and strategic fit; in-flight improvements report "
            "progress; completed ones report measured versus expected "
            "benefit. The seven steps run per improvement: the "
            "strategy names the goal, measurement defines the "
            "before-and-after metrics, data is gathered from the "
            "existing instrumentation, processing turns it into "
            "readable information, analysis finds the insight, "
            "presentation wins the decision, and implementation lands "
            "the change through the normal change process. Benefits "
            "are verified after a full measurement cycle - no victory "
            "laps on week-one data. The register's cumulative verified "
            "benefit is reported like revenue, and the habit is "
            "protected in planning: improvement capacity is budgeted, "
            "not squeezed into spare time that never exists."
        ),
        "key_points": [
            "Continual improvement is getting better on purpose: a visible register of ideas with owners, benefits, and dates, worked in priority order forever.",
            "The seven steps - strategy, measure definition, data gathering, processing, analysis, presentation, implementation - give the rhythm.",
            "Ideas come from existing instrumentation: complaints, QA, queues, VoC themes, postmortems, and agent suggestions.",
            "Every implemented improvement is measured against its expected benefit after a full cycle; verified wins are communicated.",
            "Improvement capacity is budgeted in planning, not squeezed into spare time that never exists.",
        ],
        "requirements": [
            "A visible improvement register with source, owner, expected benefit, effort, and target date per idea.",
            "A cadenced improvement board scoring new ideas and reviewing in-flight and completed work.",
            "Seven-step execution per improvement with before-and-after measurement defined up front.",
            "Benefit verification after a full measurement cycle, reported cumulatively like revenue.",
            "Budgeted improvement capacity in planning, protecting the habit from operational pressure.",
        ],
        "standards": [
            "Expected benefits are stated in operational or financial terms before work begins.",
            "Measurement definitions are fixed before implementation, preventing moving goalposts.",
            "The register is auditable: ideas cannot vanish without a recorded disposition.",
        ],
        "citations": [CIT_ITIL4, CIT_ISO20000, CIT_OPS],
        "sig_lens": (
            "The Signature read: continual improvement is the covenant "
            "sharpening its own blade, forever. Where public practice "
            "runs improvement registers, the Signature Service Covenant "
            "keeps a whetstone at the hall's center - every lesson "
            "honed into the steel, every victory measured and sung - "
            "for an oath kept the same way forever dulls, and a dull "
            "blade breaks faith."
        ),
    },
    {
        "key": "architecture",
        "name": "CRM Architecture: Integration, APIs, and Data Governance",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "CRM architecture is the engineering beneath the "
            "relationship memory: how the CRM connects to billing, "
            "ordering, marketing, telephony, and the product itself, "
            "and how data stays trustworthy across all of it. "
            "Integration patterns are chosen by need: real-time APIs "
            "for the agent's screen pop and entitlement check, "
            "event streams for the ticket-created and order-shipped "
            "notifications, batch sync for the nightly analytics "
            "load. The customer identifier is the join key across "
            "every system - the master data discipline that says one "
            "customer has one identity everywhere, resolved through "
            "matching and survivorship rules when systems disagree. "
            "Data governance names the owners: who may create "
            "customers, who may merge them, which system is the "
            "authoritative source for each field, and how long each "
            "data class is retained. API discipline keeps the mesh "
            "healthy: versioned contracts, authentication on every "
            "call, rate limits, and monitoring on sync lag and error "
            "rates, because a silently stale integration is a "
            "decision-support lie. Privacy engineering is built in, "
            "not bolted on: consent records flow to every consuming "
            "system, deletion requests propagate, and access is "
            "role-based with audit trails."
        ),
        "how_it_works": (
            "The integration map documents every connection: source "
            "system, target, pattern, frequency, and the fields "
            "flowing, with an owner per connection. Master data "
            "management runs the identity resolution: matching rules "
            "propose merges across systems, stewards approve them, "
            "and the golden record - the authoritative value per "
            "field per source system - is published to consumers. "
            "APIs expose customer, ticket, and entitlement operations "
            "under versioned contracts with authentication, "
            "throttling, and schema validation; breaking changes go "
            "through deprecation windows, never surprise. Sync "
            "monitoring tracks lag and error rate per connection "
            "with alerts on drift, and reconciliation jobs compare "
            "record counts and key fields across systems on schedule. "
            "Data governance councils - with business owners, not "
            "just IT - set the field authority matrix, the retention "
            "schedule, and the merge rules, and audit trails record "
            "every create, merge, and delete. Consent and deletion "
            "propagate through the mesh on defined SLAs, provable in "
            "audit."
        ),
        "key_points": [
            "Integration patterns match the need: real-time APIs for screen pops and entitlements, events for notifications, batch for analytics.",
            "One customer identity joins every system; master data management resolves disagreements through matching and survivorship.",
            "Field-level authority names the system of record per field, so conflicts resolve by rule, not by loudest system.",
            "API discipline - versioned contracts, auth, throttling, deprecation windows - keeps the mesh healthy and honest.",
            "Consent and deletion propagate across the mesh on defined SLAs, with audit trails proving compliance.",
        ],
        "requirements": [
            "A documented integration map: every connection with pattern, frequency, fields, and owner.",
            "Master data management with matching rules, steward approval, and a published golden record per field.",
            "Versioned API contracts with authentication, throttling, schema validation, and deprecation windows.",
            "Sync monitoring on lag and error rate per connection, with reconciliation jobs on schedule.",
            "A governance council setting field authority, retention, and merge rules, with full audit trails.",
        ],
        "standards": [
            "Breaking API changes follow deprecation windows; surprise breakage is treated as an incident.",
            "Retention schedules per data class are enforced automatically, not by manual cleanup.",
            "Access to customer data is role-based with complete audit trails on create, merge, and delete.",
        ],
        "citations": [CIT_BUTTLE, CIT_HUGHES, CIT_ISO20000],
        "sig_lens": (
            "The Signature read: architecture is the covenant's "
            "nervous system, carrying truth to every limb. Where "
            "public practice integrates systems, the Signature "
            "Service Covenant binds its senses into one body - one "
            "identity, one memory, every channel feeling what the "
            "others know - for a body whose limbs disagree cannot "
            "keep its oath."
        ),
    },
    {
        "key": "economics",
        "name": "The Economics of Service: Cost per Contact and ROI",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Service economics translates the operation into money: "
            "what each contact costs by channel, what quality is "
            "worth, and which investments pay. Cost per contact is "
            "computed fully loaded - agent labor with shrinkage, "
            "telephony and licenses, facilities, management overhead, "
            "and the technology stack - divided by resolved contacts, "
            "because dividing by raw contacts rewards deflection "
            "failure. Channel costs differ by an order of magnitude: "
            "the phone call costs many times the portal session, "
            "which is why channel strategy is a financial strategy. "
            "But cost without quality is a trap, so the economics "
            "pair cost with value: the cost of a repeat contact, the "
            "revenue protected by a save, the lifetime value kept by "
            "retention. ROI analysis governs investment: self-service "
            "is justified by deflected contacts times agent cost "
            "minus the knowledge investment; quality programs by "
            "reopen reduction times rework cost; proactive outreach by "
            "churn prevented times CLV. The return-on-quality research "
            "shows the mechanism: service quality spending pays "
            "through retention and word of mouth, not through cost "
            "cutting. Budgeting therefore funds both efficiency and "
            "effectiveness, and every major initiative carries its "
            "business case with measured payback."
        ),
        "how_it_works": (
            "Finance builds the fully loaded cost model per channel: "
            "labor cost per productive hour from payroll with "
            "shrinkage applied, technology and telephony per contact, "
            "facilities and overhead allocated by headcount, all "
            "divided by resolved contacts per period. The blended "
            "cost per resolved contact becomes the operation's unit "
            "economic, tracked monthly with the drivers - handle time, "
            "channel mix, shrinkage, wage rates - each visible. "
            "Investment business cases use the same unit economics: "
            "deflection ROI multiplies deflected contacts by agent "
            "cost per contact and subtracts content and platform "
            "cost; retention ROI multiplies prevented churn by "
            "segment CLV and subtracts program cost; quality ROI "
            "multiplies avoided rework by rework cost. Payback is "
            "measured after implementation against the case's "
            "projections, and variances are investigated rather than "
            "buried. Scenario planning tests the sensitivities - what "
            "a channel-mix shift or a wage change does to the unit "
            "economic - so strategy is priced before it is chosen."
        ),
        "key_points": [
            "Cost per contact is fully loaded and divided by resolved contacts, because raw-contact division rewards deflection failure.",
            "Channel costs differ by an order of magnitude, making channel strategy a financial strategy.",
            "Cost is always paired with value: repeat-contact cost, revenue protected by saves, lifetime value kept by retention.",
            "ROI cases use unit economics: deflection, retention, and quality investments each priced against what they avoid or earn.",
            "Payback is measured against projections after implementation, with variances investigated, and scenarios price strategy before choice.",
        ],
        "requirements": [
            "A fully loaded cost model per channel with visible drivers: handle time, mix, shrinkage, wage rates.",
            "The blended cost per resolved contact tracked monthly as the unit economic.",
            "Business cases for major initiatives with ROI priced in unit economics and measured payback.",
            "Value-side metrics - saves, retention, rework avoided - reported alongside cost, never alone.",
            "Scenario planning on mix shifts and rate changes so strategy is priced before chosen.",
        ],
        "standards": [
            "Cost allocations use consistent, documented bases across periods; methodology changes restate history.",
            "Resolved contacts, not raw contacts, are the denominator for all unit economics.",
            "Business cases state assumptions explicitly and report actuals against them post-implementation.",
        ],
        "citations": [CIT_RUST, CIT_PROFIT, CIT_OPS],
        "sig_lens": (
            "The Signature read: economics is the covenant's honest "
            "ledger of keeping. Where public practice counts cost per "
            "contact, the Signature Service Covenant reckons what "
            "faithfulness is worth - the saved partner, the kept "
            "decade, the spoken praise - and spends accordingly, for "
            "the cheapest oath is the one best kept."
        ),
    },
]
