#!/usr/bin/env python3
"""Entries for the Transaction Records databases (missing-115 #46, Wave 1).

Item 46 scope: orders, purchases, payments, returns, transfers, and
reconciliations - the anatomy of a transaction record, lifecycle states
(pending/settled/reversed), double-entry reconciliation, idempotency keys,
chargebacks/refunds, audit trails. Public records cite real standards
(ISO 20022, NACHA, SWIFT MT/MX message types, PCI DSS as public-standards
context).

Two databases, 34 ladder-ordered records each:

  transaction-records            - The Transaction Records Database
                                   (public-harvest: real, fact-checked
                                   operational transaction data)
  transaction-records-signature  - The Transaction Records Signature Database
                                   (his original Signature Transaction
                                   Method: every transaction a sealed
                                   covenant between parties, the ledger the
                                   book of covenants, reconciliation the
                                   truth-telling, the idempotency seal that
                                   cannot be double-stamped, and the audit
                                   trail the unbroken chain of witness;
                                   src signature, titles suffixed
                                   " (Signature Edition)", never presented
                                   as authentic public record)

34 records each, teaching ladder (ladder_rank 1-10 non-decreasing,
foundations -> compounded -> advanced).

ID prefixes: JAH-TRX- (public) and JAH-TRXS- (signature), verified free
2026-10-17: zero hits in all 2,390 manifest id_prefix values and zero hits
in all 789 shard index.jsonl.gz files in jah-databases-data-1.

Dedupe: all 68 titles (34 + 34 Signature Edition variants) checked against
the whole system via DedupeGate 2026-10-17 before authoring - zero
refusals.

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_transaction_records.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; build.py machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Transaction "
            "Method: every transaction a sealed covenant between parties, "
            "the ledger the book of covenants, reconciliation the "
            "truth-telling, the idempotency seal that cannot be "
            "double-stamped, and the audit trail the unbroken chain of "
            "witness. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

CIT_ISO20022 = ("ISO 20022-1:2021. Financial services - Universal financial "
                "industry message scheme - Part 1: Metamodel. Payments "
                "messages include pain.001 (credit transfer initiation), "
                "pacs.008 (customer credit transfer), and camt.053 (bank to "
                "customer statement).")
CIT_NACHA = ("NACHA Operating Rules & Guidelines. National Automated "
             "Clearing House Association. Defines the ACH file layout: file "
             "header record type 1, batch header type 5, entry detail type "
             "6, addenda type 7, batch control type 8, and file control "
             "type 9, with balanced batch and file control totals.")
CIT_SWIFT = ("SWIFT message standards. MT101/MT103 customer credit "
             "transfers, MT202 general financial institution transfer, "
             "MT940/950 customer statements; the MX migration maps these to "
             "ISO 20022 equivalents pacs.008, pacs.009, and camt.053.")
CIT_PCI = ("PCI Security Standards Council. Payment Card Industry Data "
           "Security Standard (PCI DSS) v4.0. March 2022. Prohibits "
           "storage of full magnetic-stripe data and card verification "
           "values after authorization; requires PAN rendering unreadable "
           "where stored.")
CIT_ISO8583 = ("ISO 8583-1:2021. Financial transaction card originated "
               "messages - Interchange message specifications. Defines the "
               "authorization, clearing, and settlement message grammar used "
               "by card networks.")
CIT_ISO4217 = ("ISO 4217:2015. Codes for the representation of currencies. "
               "Assigns three-letter codes and minor-unit counts, for "
               "example USD with 2 minor units, JPY with 0, BHD with 3.")
CIT_FEDNOW = ("Board of Governors of the Federal Reserve System. FedNow "
              "Service operating procedures. Instant payments service "
              "operating around the clock, using ISO 20022 message "
              "specifications, launched July 2023.")
CIT_RTP = ("The Clearing House. Real-Time Payments (RTP) system rules and "
           "message specifications. Instant credit-transfer rail operating "
           "continuously since 2017.")
CIT_WEYGANDT = ("Weygandt JJ, Kimmel PD, Kieso DE. Financial Accounting. "
                "Wiley. Double-entry bookkeeping: every transaction posts "
                "equal debits and credits, and the trial balance proves the "
                "ledger balances.")
CIT_RFC9110 = ("Fielding R et al. RFC 9110: HTTP Semantics. IETF, June "
               "2022. Standardizes idempotent methods and the "
               "Idempotency-Key request header for safe retry of unsafe "
               "operations.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is a Transaction Record",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A transaction record is the written memory of money moving: "
            "proof that an order was placed, a purchase was paid for, a "
            "payment was sent, a return was accepted, a transfer was made, "
            "or two ledgers were reconciled. Every transaction record "
            "answers the same six questions: who paid, who was paid, how "
            "much, in what currency, when, and under what identifier. "
            "Businesses keep transaction records to prove what happened, "
            "banks keep them to settle what is owed, and auditors keep them "
            "to verify that the story the books tell is true. A good "
            "transaction record is complete at birth - it never needs "
            "someone to remember the context later - and it is permanent: "
            "mistakes are corrected by new records, never by editing the "
            "old one. This database catalogs the whole anatomy of "
            "transaction records, from the humble receipt through "
            "double-entry ledgers, idempotency keys, chargebacks, and "
            "audit trails, in the order a student should learn them."
        ),
        "how_it_works": (
            "A transaction record works by freezing one economic event into "
            "a structured, timestamped, identified fact. The event happens "
            "in the world - a card is swiped, an order is clicked, a wire "
            "is sent - and the system writes a record carrying the amount, "
            "the parties, the currency, the time, and a unique identifier. "
            "That record then travels a lifecycle: it starts pending while "
            "the world confirms it, becomes settled when money actually "
            "moves, and can be reversed by a compensating record if the "
            "event is undone. Later, reconciliation matches the record "
            "against independent copies - the bank statement, the "
            "counterparty ledger - and any mismatch is a break to "
            "investigate. The record is the atom; the ledger is the "
            "molecule; the audit trail is the full crystal."
        ),
        "key_points": [
            "A transaction record proves one economic event: order, purchase, payment, return, transfer, or reconciliation.",
            "Every record answers who, whom, how much, what currency, when, and under what identifier.",
            "Records are written once and never edited - corrections arrive as new records, never as changes.",
            "Each record lives a lifecycle: pending, then settled, possibly reversed, always retained.",
            "Reconciliation matches records against independent copies; a mismatch is a break, not a mystery.",
        ],
        "requirements": [
            "A unique identifier so the record can be named, found, and referenced by every later record.",
            "An amount with an explicit currency, stored in minor units so rounding cannot corrupt it.",
            "A timestamp with a time zone, so the moment of the event is unambiguous across the planet.",
            "Named parties - payer and payee at minimum - so the record says who moved value to whom.",
            "A lifecycle state - pending, settled, or reversed - so readers know whether the money moved yet.",
        ],
        "standards": [
            "Transaction messaging follows public standards: ISO 20022 for the MX message grammar, ISO 8583 for card-originated messages, and NACHA rules for ACH files.",
            "Currency codes and minor-unit counts follow ISO 4217 so every system agrees what one cent means.",
            "Card data protection follows PCI DSS v4.0, which forbids storing sensitive authentication data after authorization.",
        ],
        "citations": [CIT_ISO20022, CIT_ISO8583, CIT_ISO4217],
        "sig_lens": (
            "The Signature read: the transaction record is the sealed "
            "covenant of commerce - the moment two parties bind themselves "
            "in writing. The Signature Transaction Method treats every "
            "record as an oath with six witnesses: who, whom, how much, "
            "what coin, when, and under what seal."
        ),
    },
    {
        "key": "anatomy",
        "name": "The Anatomy of a Transaction Record",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Open any transaction record and you find the same organs in "
            "the same order. The identifier is the skeleton: a reference "
            "number, UUID, or idempotency key that names this record and no "
            "other. The parties are the actors: payer, payee, and often a "
            "merchant, an acquirer, or a bank standing between them. The "
            "amount and currency are the muscle: the quantity of value that "
            "moved, in minor units so a cent can never fall between two "
            "floats. The timestamps are the heartbeat: when the record was "
            "created, when the event occurred, and the value date when the "
            "money legally moves. The state is the posture: pending, "
            "settled, or reversed. And the lineage is the memory: links to "
            "the order that caused the payment, the authorization that "
            "preceded the capture, the refund that answered the sale. A "
            "record missing any organ is a body that cannot stand "
            "inspection."
        ),
        "how_it_works": (
            "Anatomy works by convention: every system that reads the "
            "record agrees in advance what each field means, so a program "
            "written in one company can settle with a program written in "
            "another. The identifier lets later records point at this one - "
            "the refund names the original sale, the reversal names the "
            "original transfer. Amounts live in minor units - cents, not "
            "dollars - because binary floating point cannot represent most "
            "decimals exactly, and a rounding error of a tenth of a cent, "
            "multiplied by a million transactions, is real money. "
            "Timestamps carry their time zone so a payment made at midnight "
            "in Tokyo is not mistaken for one made at midnight in New York. "
            "State fields are append-only history: the record never flips "
            "from settled back to pending; a new reversal record carries "
            "that news instead."
        ),
        "key_points": [
            "Identifier, parties, amount plus currency, timestamps, state, and lineage - the six organs of every record.",
            "Amounts are stored in minor units (integer cents), never as binary floating-point dollars.",
            "Timestamps carry time zones so the moment of the event is global and unambiguous.",
            "Lineage links every record to the records that caused it and the records that answered it.",
            "State is history, not a flag: a settled record is never edited; a reversal record announces the undo.",
        ],
        "requirements": [
            "A unique identifier in a stated format (reference number, UUID, or message ID) present on every record.",
            "Amount as an integer count of ISO 4217 minor units, with the three-letter currency code beside it.",
            "At least one timestamp with an explicit time zone or UTC offset; value date where settlement lags.",
            "Named payer and payee; intermediaries named where they touch the money.",
            "A lineage pointer to the originating record for every derived record (refund, reversal, fee).",
        ],
        "standards": [
            "Currency representation follows ISO 4217 codes and minor-unit counts.",
            "Cross-border payment messages follow ISO 20022 MX grammar or SWIFT MT field conventions.",
            "Timestamps in interchange messages follow the format rules of the rail they travel (ISO 20022, NACHA, ISO 8583).",
        ],
        "citations": [CIT_ISO4217, CIT_ISO20022, CIT_SWIFT],
        "sig_lens": (
            "The Signature read: the anatomy is the anatomy of the "
            "covenant. The identifier is the seal, the parties the "
            "covenant-makers, the amount the promise, the timestamps the "
            "witnesses, the state the standing of the oath, and the lineage "
            "the genealogy of every promise kept and unmade."
        ),
    },
    {
        "key": "lifecycle_states",
        "name": "Transaction Lifecycle States: Pending, Settled, Reversed",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every transaction record is born pending, grows up settled, "
            "and may end reversed. Pending means the intent is recorded but "
            "the money has not moved: an authorized card hold, an ACH file "
            "waiting for its effective date, an order awaiting capture. "
            "Settled means value actually changed hands and the books may "
            "treat it as final: the capture posted, the wire credited, the "
            "batch balanced. Reversed means a later record undid the "
            "effect: a refund, a chargeback, a returned ACH - and crucially, "
            "the original record is never deleted or edited; the reversal "
            "is a separate record that points back to it. Between these "
            "three stand the waiting rooms: authorized, captured, cleared, "
            "failed, expired. Failed is a terminal state with no money "
            "movement, distinct from reversed, which moves money back. "
            "Reading the state field correctly is the difference between "
            "counting revenue and counting promises."
        ),
        "how_it_works": (
            "Lifecycle works as a state machine with guarded transitions. "
            "A record may move from pending to settled, from pending to "
            "failed, or from settled to reversed - it may never move from "
            "settled back to pending, nor from failed to settled, because "
            "history does not run backward. Each transition is itself a "
            "recorded event with a timestamp: the authorization event, the "
            "capture event, the settlement event, the reversal event. "
            "Systems enforce the machine: a capture referencing an expired "
            "authorization is rejected, a refund exceeding the settled "
            "amount is rejected, a second settlement of the same "
            "authorization is rejected by the idempotency check. The "
            "current state is always derivable by replaying the events in "
            "order - which is why append-only ledgers and state machines "
            "are the same idea wearing different clothes."
        ),
        "key_points": [
            "Pending: intent recorded, money not yet moved. Settled: value moved, books may treat it as final. Reversed: a later record undid the effect.",
            "Failed is terminal with no money movement; reversed moves money back - they are different states.",
            "Transitions are guarded: settled never returns to pending; each transition is a timestamped event.",
            "Reversals are new records pointing at the original; originals are never edited or deleted.",
            "The current state is always re-derivable by replaying the event history in order.",
        ],
        "requirements": [
            "A stated state machine: the legal states and the legal transitions between them, documented per record type.",
            "A timestamp on every state transition, so the order of events is provable.",
            "Terminal states (settled, failed) must be distinguishable from intermediate states (authorized, captured).",
            "Reversal records must carry a pointer to the original record and the reason for reversal.",
            "State must be re-derivable from the event log - the log is the truth, the state is a cache.",
        ],
        "standards": [
            "Card lifecycle messaging follows ISO 8583 authorization, clearing, and reversal message types.",
            "ACH return and reversal entries follow NACHA return reason codes and timeframes.",
            "ISO 20022 payment status messages (pacs.002) standardize pending/accepted/rejected reporting.",
        ],
        "citations": [CIT_ISO8583, CIT_NACHA, CIT_ISO20022],
        "sig_lens": (
            "The Signature read: the lifecycle is the life of the "
            "covenant. Pending is the promise spoken, settled the promise "
            "kept, reversed the promise released by mutual release. The "
            "Signature Method forbids rewriting a kept promise - release "
            "requires its own witnessed act."
        ),
    },
]
ENTRIES.extend([
    {
        "key": "txn_types",
        "name": "Orders, Purchases, Payments, and Transfers",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The transaction family has four siblings, and confusing them "
            "is the most common beginner error. An order is a request: a "
            "customer asks for goods, listing line items, quantities, and "
            "prices, but no money moves yet. A purchase is an order "
            "accepted and paid for in one motion: the retail card swipe, "
            "the click that both orders and pays. A payment is the movement "
            "of money itself, with or without goods attached: paying an "
            "invoice, sending a wire, settling a bill. A transfer moves "
            "value between accounts owned by the same party or between "
            "parties, often with no merchant involved: moving savings to "
            "checking, wiring funds to a supplier. Around them cluster the "
            "cousins: the return, which undoes a purchase; the refund, "
            "which undoes a payment; the chargeback, which undoes a payment "
            "by force; and the reconciliation, which proves the family "
            "tells a consistent story. Each type carries its own record "
            "shape, its own lifecycle, and its own rules."
        ),
        "how_it_works": (
            "Types work by carrying different promises. An order promises "
            "intent: it reserves inventory and quotes a price, and it can "
            "be cancelled freely because nothing of value has moved. A "
            "purchase collapses order and payment into one event, which is "
            "why a retail receipt is both an order record and a payment "
            "record. A payment promises value movement and therefore needs "
            "authorization (permission) and settlement (actual movement) as "
            "separate, checkable steps. A transfer promises reallocation: "
            "the books show the same total before and after, just in "
            "different places. The type determines which later records are "
            "legal: orders accept cancellations, payments accept refunds "
            "and chargebacks, transfers accept reversals, and every type "
            "accepts reconciliation. Filing a refund against an order that "
            "never became a payment is a category error the record types "
            "exist to prevent."
        ),
        "key_points": [
            "Order: a request for goods, no money moved yet, cancellable. Purchase: order and payment in one motion.",
            "Payment: value moves, with or without goods; needs authorization and settlement as separate steps.",
            "Transfer: value reallocated between accounts; the books total the same before and after.",
            "Return undoes a purchase, refund undoes a payment, chargeback undoes a payment by force.",
            "The record type determines which follow-up records are legal - a refund needs a payment to refund.",
        ],
        "requirements": [
            "A declared transaction type on every record, from a controlled vocabulary the system documents.",
            "Orders must carry line items with quantities and unit prices; payments must carry payer, payee, amount.",
            "Each type must document which follow-up types it accepts (order->cancel, payment->refund/chargeback).",
            "Type transitions must be validated: a record cannot change type after creation.",
            "Reporting must separate pending orders from settled payments so revenue is never double-counted.",
        ],
        "standards": [
            "ISO 20022 message types encode the transaction family: pain messages initiate, pacs messages move value, camt messages report.",
            "Card network processing distinguishes purchase, refund, and cash transactions in ISO 8583 processing codes.",
            "NACHA standard entry classes (PPD, CCD, WEB, TEL) distinguish consumer, corporate, internet, and telephone debits.",
        ],
        "citations": [CIT_ISO20022, CIT_ISO8583, CIT_NACHA],
        "sig_lens": (
            "The Signature read: the four siblings are four kinds of "
            "covenant - the covenant of intent (order), the covenant of "
            "exchange (purchase), the covenant of value (payment), and the "
            "covenant of place (transfer). The Signature Method gives each "
            "its own seal so no one can answer an intent with a refund."
        ),
    },
    {
        "key": "double_entry_basics",
        "name": "Double-Entry Bookkeeping in One Lesson",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Double-entry bookkeeping is the five-hundred-year-old trick "
            "that makes ledgers self-checking: every transaction posts at "
            "least two entries, debits equal to credits, so the books must "
            "balance or something is wrong. Sell a book for 20 dollars in "
            "cash: debit cash 20, credit sales revenue 20. Pay 5 dollars of "
            "that for postage: debit postage expense 5, credit cash 5. At "
            "any moment the trial balance - every account's balance summed "
            "with debits positive and credits negative - must total zero. "
            "If it does not, an entry is missing or mistyped, and the "
            "arithmetic says so before any human notices. Debits and "
            "credits are not good and bad; they are left and right. Assets "
            "and expenses grow with debits, liabilities and revenue grow "
            "with credits. Every transaction record in this database, from "
            "a one-line receipt to a cross-border wire, can be expressed as "
            "balanced double entries - which is why reconciliation at scale "
            "is just double-entry with computers."
        ),
        "how_it_works": (
            "Double-entry works because value is conserved: money cannot "
            "appear in one account without disappearing from another, so "
            "each event is written twice, once as a debit and once as a "
            "credit, and the two must be equal. Posting is the act of "
            "adding the entries to the ledger; journaling is the act of "
            "recording the event in chronological order first. The chart of "
            "accounts names every bucket - cash, receivables, revenue, "
            "expenses - and each entry names its bucket. The trial balance "
            "sums all buckets: debits minus credits must equal zero, and "
            "any nonzero total is a provable error, not a suspicion. Modern "
            "transaction systems implement this mechanically: the payment "
            "processor debits the merchant payable and credits the "
            "settlement account in the same atomic write, so a crash "
            "between the two is impossible. Reversals post mirror-image "
            "entries, which is why the original entries are never edited."
        ),
        "key_points": [
            "Every transaction posts equal debits and credits; the trial balance must sum to zero.",
            "Debits and credits are left and right, not good and bad: assets and expenses grow with debits.",
            "A nonzero trial balance is a provable error, caught by arithmetic before humans notice.",
            "Atomic posting writes both entries together so a crash cannot leave a half-transaction.",
            "Reversals post mirror-image entries; originals are never edited.",
        ],
        "requirements": [
            "Every journal entry must name an account, a debit or credit direction, and an amount in minor units.",
            "Each transaction must balance: total debits equal total credits, checked at posting time.",
            "A trial balance must be computable at any moment and must total zero.",
            "Postings must be atomic: both sides commit together or neither commits.",
            "Reversals must reference the original transaction and post exact mirror entries.",
        ],
        "standards": [
            "Double-entry principles follow generally accepted accounting practice as taught in standard financial accounting texts.",
            "Revenue recognition timing follows FASB ASC 606 for accrual-basis records.",
            "Electronic journal records must meet the same completeness and immutability expectations as paper ledgers.",
        ],
        "citations": [CIT_WEYGANDT],
        "sig_lens": (
            "The Signature read: double-entry is the covenant of "
            "conservation - nothing gained without something given. The "
            "Signature Method calls the balanced books the twin witnesses: "
            "two entries testifying to one truth, and the trial balance "
            "their sworn agreement."
        ),
    },
    {
        "key": "reading_receipt",
        "name": "Reading a Receipt Like a Record",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The receipt is the transaction record most humans ever meet, "
            "and it already contains the full anatomy in miniature. At the "
            "top: the merchant name and location - the payee. Then the "
            "date and time of the event. Then the line items: what was "
            "bought, how many, at what unit price. Then the subtotal, the "
            "tax computed at the stated rate, and the total - the amount "
            "in minor units, though printed with a decimal point. Then the "
            "payment method and the last four digits of the card, the "
            "authorization code - the identifier - and often a transaction "
            "or reference number. A receipt you can audit is one where the "
            "arithmetic checks out: line items sum to the subtotal, tax "
            "equals the rate times the subtotal within a cent of rounding, "
            "and the total equals subtotal plus tax. When a receipt fails "
            "this check, either the tax rate was misapplied or a line item "
            "is missing - the same two failure modes as a million-dollar "
            "ledger."
        ),
        "how_it_works": (
            "A receipt works by being both a human-readable summary and a "
            "machine-checkable record. The point-of-sale system computes "
            "each line extension as quantity times unit price, sums the "
            "extensions into the subtotal, multiplies by the tax rate and "
            "rounds to the minor unit to get the tax, and adds tax to "
            "subtotal for the total. Rounding is the subtle organ: tax is "
            "rounded once per receipt (or per jurisdiction's rule), never "
            "per line, because per-line rounding accumulates error. The "
            "authorization code ties the paper to the electronic "
            "authorization record, and the reference number ties it to the "
            "settlement batch. Returns reference the original receipt "
            "number, which is how the store knows the refund matches a "
            "real sale. The receipt is thus the seed of the whole lineage "
            "tree: sale, then possibly return, refund, or chargeback, each "
            "pointing back to this slip of paper."
        ),
        "key_points": [
            "A receipt carries payee, timestamp, line items, subtotal, tax, total, method, and authorization code.",
            "Auditable arithmetic: line items sum to subtotal; tax equals rate times subtotal within rounding; total equals subtotal plus tax.",
            "Tax is rounded once per receipt, not per line, so rounding error cannot accumulate.",
            "The authorization code and reference number tie the paper to the electronic records.",
            "Returns and refunds reference the original receipt number, seeding the lineage tree.",
        ],
        "requirements": [
            "Line items must show description, quantity, and unit price so extensions are checkable.",
            "The tax rate must be stated and the tax amount must match it within one minor unit of rounding.",
            "The total must equal subtotal plus tax exactly in minor-unit arithmetic.",
            "An authorization or reference identifier must be printed for electronic payments.",
            "The merchant identity and event timestamp must be unambiguous.",
        ],
        "standards": [
            "Receipt tax computation follows the taxing jurisdiction's stated rate and rounding rule.",
            "Card receipts must follow PCI DSS receipt rules: truncated PAN showing at most the last four digits.",
            "Electronic receipts must preserve the same data elements as paper for audit equivalence.",
        ],
        "citations": [CIT_PCI, CIT_ISO4217],
        "sig_lens": (
            "The Signature read: the receipt is the covenant in the "
            "customer's pocket - small, complete, and sworn. The Signature "
            "Method honors the humble receipt as the first ledger most "
            "people ever keep, and the model every larger record must live "
            "up to."
        ),
    },
    {
        "key": "minor_units",
        "name": "Money in Minor Units: Cents, Rounding, and Precision",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Money in transaction records is never stored as 19.99. It is "
            "stored as 1999 - an integer count of minor units, the cents "
            "of the currency. The reason is binary floating point: the "
            "number 0.1 cannot be represented exactly in binary, so adding "
            "ten cents ten times in floating point can yield 0.9999999 or "
            "1.0000001 instead of 1.00, and across millions of records "
            "those phantoms become real discrepancies. ISO 4217 assigns "
            "each currency its minor-unit count: US dollars have 2 (cents), "
            "Japanese yen have 0 (the yen is the minor unit), Bahraini "
            "dinars have 3 (fils). Rounding converts computed amounts to "
            "storable ones: half-up rounding sends 2.675 cents-worth to 3, "
            "and bankers rounding sends it to the even neighbor. The rule "
            "is simple and absolute: compute in high precision, round once "
            "at the boundary, store integers."
        ),
        "how_it_works": (
            "Minor units work by moving the decimal point out of the "
            "computation. To store 19.99 USD, multiply by 10 to the power "
            "of the minor-unit count (2) to get 1999, and store the integer. "
            "Addition and subtraction of integers are exact, so ledger sums "
            "never drift. Multiplication and division - tax rates, "
            "percentages, splits - produce fractions, so they are computed "
            "in decimal or rational arithmetic and rounded once, with the "
            "stated rounding mode, to the minor unit. The rounding mode "
            "must be documented because half-up and bankers rounding "
            "disagree exactly at the halfway point, and two systems using "
            "different modes will disagree by a cent on large volumes. "
            "Currency conversion multiplies by the rate in high precision "
            "and rounds once to the target currency's minor units. Every "
            "amount field in every standard message - ISO 20022, SWIFT, "
            "NACHA - is defined with an explicit decimal convention for "
            "exactly this reason."
        ),
        "key_points": [
            "Store money as integer minor units (1999 cents), never as binary floating-point dollars.",
            "ISO 4217 sets the minor-unit count: USD 2, JPY 0, BHD 3.",
            "Compute in high precision, round once at the boundary, with a documented rounding mode.",
            "Half-up and bankers rounding disagree at the halfway point - the mode must be stated.",
            "Integer addition and subtraction are exact, so ledger sums never drift.",
        ],
        "requirements": [
            "Every amount field must be an integer count of minor units with the currency code beside it.",
            "The minor-unit count must follow ISO 4217 for the stated currency.",
            "A rounding mode must be documented wherever computed amounts become stored amounts.",
            "Floating-point types must never hold money in record storage or ledger arithmetic.",
            "Currency conversion must round once to the target currency's minor units.",
        ],
        "standards": [
            "Currency codes and minor-unit counts follow ISO 4217.",
            "ISO 20022 amount fields carry explicit decimal and currency conventions.",
            "NACHA entry amounts are stated in dollars and cents as fixed-format numeric fields.",
        ],
        "citations": [CIT_ISO4217, CIT_ISO20022, CIT_NACHA],
        "sig_lens": (
            "The Signature read: the minor unit is the indivisible atom of "
            "the covenant - the smallest promise that can be kept. The "
            "Signature Method forbids the phantom cent: if the books "
            "cannot name it exactly, they cannot claim it at all."
        ),
    },
    {
        "key": "timestamps",
        "name": "Timestamps, Time Zones, and Value Dates",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A transaction record carries not one time but several, and "
            "each answers a different question. The event timestamp says "
            "when the thing happened in the world: the card swipe, the "
            "click, the wire instruction. The record timestamp says when "
            "the system wrote it down, which can lag the event by "
            "milliseconds or hours in batch systems. The value date says "
            "when the money legally moves for interest and availability "
            "purposes - often a business day after the event. And the "
            "settlement date says when the rail actually delivered the "
            "funds. Each timestamp needs a time zone, because a payment "
            "at 00:30 in Tokyo on Tuesday is still Monday in New York, and "
            "cutoff times - the hour after which a payment counts as the "
            "next business day - are defined in local rail time. Records "
            "that store local times without zones are ambiguous twice a "
            "year at daylight-saving transitions and always across borders."
        ),
        "how_it_works": (
            "Timestamps work by separating the moment from the meaning. "
            "The system captures the event in UTC - the single global "
            "clock - and stores any local presentation time beside it, "
            "never instead of it. Value dating then applies the rail's "
            "calendar: a wire sent after the 5 p.m. Eastern cutoff gets "
            "tomorrow's value date, and no interest accrues until then. "
            "Batch systems like ACH stamp the file creation time and the "
            "effective entry date separately, because the file is built "
            "today for value two days hence. Reconciliation leans on "
            "timestamps to pair records: the merchant's sale at 14:03:22 "
            "UTC matches the processor's authorization at the same second, "
            "while the settlement record lands two days later with the "
            "same lineage but a different date. Cutoff logic is pure "
            "calendar arithmetic on the timestamp plus the rail's holiday "
            "schedule."
        ),
        "key_points": [
            "Event time, record time, value date, and settlement date answer different questions - keep them separate.",
            "Store the event in UTC; local time is presentation, never the source of truth.",
            "The value date decides interest and availability; the cutoff time decides the value date.",
            "Batch rails stamp file time and effective entry date separately.",
            "Reconciliation pairs records by event timestamp and lineage, not by settlement date.",
        ],
        "requirements": [
            "Every timestamp must carry an explicit time zone or be stated as UTC.",
            "Event time and record time must be separate fields where batching can separate them.",
            "Value date must be stated where settlement lags the event by design.",
            "Cutoff times must be documented in the rail's local time with its holiday calendar.",
            "Timestamps must have enough resolution (at least seconds) to order same-day events.",
        ],
        "standards": [
            "ISO 20022 date-time fields follow ISO 8601 with explicit offsets.",
            "SWIFT MT field 32A carries the value date as YYMMDD beside the currency and amount.",
            "NACHA file headers carry the file creation date and time plus the effective entry date.",
        ],
        "citations": [CIT_ISO20022, CIT_SWIFT, CIT_NACHA],
        "sig_lens": (
            "The Signature read: time is the witness that cannot be "
            "bribed. The Signature Method demands each covenant name its "
            "moment in the one global clock, its legal day, and its day "
            "of delivery - three witnesses, none allowed to contradict."
        ),
    },
    {
        "key": "parties",
        "name": "The Parties to a Transaction",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Every transaction has at least two parties - the payer who "
            "gives value and the payee who receives it - and most have a "
            "supporting cast. In a card purchase: the cardholder pays, the "
            "merchant is paid, the issuer (the cardholder's bank) fronts "
            "the money, the acquirer (the merchant's bank) collects it, and "
            "the network (Visa, Mastercard) carries the messages and sets "
            "the rules. In a wire: the originator instructs, the "
            "originator's bank sends, correspondent banks relay, and the "
            "beneficiary's bank credits the beneficiary. In an ACH: the "
            "originator, the originating depository financial institution "
            "(ODFI), the receiving depository financial institution "
            "(RDFI), and the receiver. Records must name the parties "
            "precisely because liability follows the names: the party that "
            "authorized is the party that pays, and a record that cannot "
            "say who authorized it cannot prove anything."
        ),
        "how_it_works": (
            "Parties work by role, not by name alone. The record assigns "
            "each participant a role - debtor, creditor, originator, "
            "beneficiary, issuer, acquirer - and the role determines what "
            "the party is allowed and required to do. Authorization binds "
            "the payer's role to the payment: the cardholder's PIN or the "
            "corporate treasurer's signed instruction is what makes the "
            "debit legitimate. Settlement then moves value along the chain "
            "of intermediaries, each hop recorded: issuer to network to "
            "acquirer to merchant. Fees are sliced at each hop, which is "
            "why the merchant receives less than the cardholder paid. "
            "Disputes walk the chain backward: the cardholder complains to "
            "the issuer, the issuer debits the acquirer through the "
            "network, the acquirer debits the merchant. The record's party "
            "fields are the map every dispute follows."
        ),
        "key_points": [
            "Minimum cast: payer and payee; typical cast adds issuer, acquirer, network, or correspondent banks.",
            "Roles (debtor, creditor, originator, beneficiary) determine what each party may and must do.",
            "Authorization binds the payer's role to the payment - without it the debit is illegitimate.",
            "Settlement moves value hop by hop, with fees sliced at each hop.",
            "Disputes walk the party chain backward, so the record's party fields are the dispute map.",
        ],
        "requirements": [
            "Every record must name payer and payee with identifiers, not just display names.",
            "Intermediaries that touch the money must be named with their role.",
            "The authorizing party and the authorization method must be recorded.",
            "Party identifiers must be stable across records so lineage can be followed.",
            "Beneficial ownership must be traceable through correspondent chains for cross-border records.",
        ],
        "standards": [
            "ISO 20022 party identification uses structured name, address, and account elements for debtor and creditor.",
            "SWIFT MT103 fields 50 (ordering customer) and 59 (beneficiary customer) name the end parties.",
            "NACHA entries carry ODFI and RDFI routing numbers identifying the originating and receiving institutions.",
        ],
        "citations": [CIT_ISO20022, CIT_SWIFT, CIT_NACHA],
        "sig_lens": (
            "The Signature read: the parties are the covenant-makers and "
            "their witnesses. The Signature Method names every maker, "
            "every witness, and the one whose hand sealed the promise - "
            "because a covenant with an unnamed maker binds no one."
        ),
    },
    {
        "key": "identifiers",
        "name": "Transaction Identifiers and Reference Numbers",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A transaction without an identifier is a rumor. Identifiers "
            "give each record a name that no other record shares, so "
            "refunds can point at sales, reversals at originals, and "
            "reconciliation can pair the merchant's copy with the bank's. "
            "The family includes reference numbers (human-readable, often "
            "sequential per merchant), UUIDs (128-bit random values with "
            "negligible collision odds), network reference numbers (the "
            "acquirer reference number that follows a card transaction "
            "through authorization, clearing, and disputes), and "
            "idempotency keys (client-chosen tokens that make retries "
            "safe). Good identifiers are unique within their scope, stable "
            "over time, and opaque - they carry no meaning that could go "
            "stale, like an amount or a date embedded in the number. "
            "Sequential numbers are easy to audit for gaps; random UUIDs "
            "are unguessable; each has its place."
        ),
        "how_it_works": (
            "Identifiers work by being the join key of the whole system. "
            "When the authorization response returns an approval code, the "
            "capture references it; when the batch settles, the settlement "
            "record references the capture; when the customer disputes, "
            "the chargeback references the settlement - one thread through "
            "four records. Idempotency keys work differently: the client "
            "generates the key before sending, and the server stores the "
            "result under the key, so a retried request returns the stored "
            "result instead of charging twice. The network reference number "
            "(ARN) works across companies: the merchant, acquirer, network, "
            "and issuer all stamp the same ARN, so a dispute filed months "
            "later can still find its transaction. Uniqueness is enforced "
            "by database constraints on the identifier column - the last "
            "line of defense when all the application logic above it has "
            "failed."
        ),
        "key_points": [
            "Identifiers are the join key: refunds, reversals, and disputes all point at originals by identifier.",
            "Reference numbers are human-readable and gap-auditable; UUIDs are unguessable with negligible collision odds.",
            "The acquirer reference number follows a card transaction across merchant, acquirer, network, and issuer.",
            "Idempotency keys let clients retry safely: the server returns the stored result instead of acting twice.",
            "Database uniqueness constraints on identifiers are the last line of defense against duplicates.",
        ],
        "requirements": [
            "Every record must carry at least one identifier unique within its stated scope.",
            "Derived records must carry the identifier of the record they derive from.",
            "Idempotency keys must be client-generated, stored with results, and honored on retry.",
            "Identifiers must be opaque - no embedded amounts, dates, or other meaning that can go stale.",
            "Uniqueness must be enforced by a database constraint, not just by application logic.",
        ],
        "standards": [
            "Idempotency-Key semantics for HTTP are standardized in RFC 9110 and widely adopted by payment APIs.",
            "ISO 20022 messages carry end-to-end and instruction identification elements for cross-system tracing.",
            "SWIFT field 20 (transaction reference number) provides the sender's unique identifier on MT messages.",
        ],
        "citations": [CIT_RFC9110, CIT_ISO20022, CIT_SWIFT],
        "sig_lens": (
            "The Signature read: the identifier is the seal pressed into "
            "the covenant - unique, unforgeable, and the handle by which "
            "all later acts take hold of the first. The Signature Method "
            "treats the idempotency key as the seal that cannot be "
            "double-stamped."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "order_records",
        "name": "Order Records: Carts, Line Items, and Order States",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "An order record is the transaction before the transaction: "
            "the customer's intent captured in full before any money "
            "moves. It carries a header - order number, customer, order "
            "date, status - and line items, each naming a product, a "
            "quantity, and a unit price, with extensions that sum to the "
            "subtotal. Around the subtotal cluster the adjustments: "
            "discounts, coupons, taxes computed per jurisdiction, shipping "
            "charges, and the grand total the customer agreed to. The "
            "order then walks its own state machine: created, then "
            "awaiting payment, then paid or cancelled, then fulfilled in "
            "whole or in part, then possibly returned. Splitting one order "
            "into several shipments creates fulfillment records that "
            "reference the order; capturing payment against the order "
            "creates payment records that reference it too. The order "
            "record is thus the root of a tree, and every later financial "
            "record is a branch that must sum back to the trunk."
        ),
        "how_it_works": (
            "Order records work by separating intent from money. The cart "
            "collects intent with no commitment; submitting the order "
            "freezes the prices, the inventory reservation, and the total "
            "into an immutable order snapshot, because the price at "
            "checkout is a promise. Payment authorization then attaches to "
            "the order, and capture converts the authorized amount into "
            "settled funds - usually when goods ship, since charging "
            "before shipment creates refund work. Partial fulfillment "
            "splits the tree: two shipments, two capture records, one "
            "order total, and the sum of captures must never exceed the "
            "authorized amount. Cancellation is legal only before capture; "
            "after capture, the undo is a refund, not a cancellation, "
            "because money has moved. Reconciliation ties the knot: the "
            "sum of payment records referencing the order must equal the "
            "order total minus refunds."
        ),
        "key_points": [
            "The order record freezes intent: line items, prices, discounts, tax, shipping, and the agreed total.",
            "Submitting the order snapshots prices and reserves inventory - the checkout price is a promise.",
            "Authorization attaches to the order; capture usually follows shipment, not the click.",
            "Partial fulfillment splits one order into several capture records that must sum within the authorization.",
            "After capture, the undo is a refund, not a cancellation - money has moved.",
        ],
        "requirements": [
            "Line items must show product identifier, quantity, and unit price with checkable extensions.",
            "The order total must equal subtotal plus tax plus shipping minus discounts, in minor units.",
            "The order state machine must be documented: created, awaiting payment, paid, fulfilled, cancelled, returned.",
            "Payment records must reference the order identifier; the sum of captures must not exceed authorization.",
            "Price snapshots must be immutable once the order is submitted.",
        ],
        "standards": [
            "Order-to-cash record linkage follows the same lineage principles as ISO 20022 end-to-end identification.",
            "Tax computation on orders follows the taxing jurisdiction's rate and rounding rules.",
            "Card-on-file and delayed-capture practices follow card network rules for authorization validity windows.",
        ],
        "citations": [CIT_ISO20022, CIT_ISO8583],
        "sig_lens": (
            "The Signature read: the order is the covenant of intent - "
            "the promise before the price is paid. The Signature Method "
            "freezes the intent at the moment of speaking, so no later "
            "hand can quietly rewrite what was agreed."
        ),
    },
    {
        "key": "auth_capture",
        "name": "Authorization and Capture: The Two-Step Card Payment",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Most card payments are two transactions wearing one name. "
            "Authorization is the issuer's promise: yes, this card is "
            "valid, the funds or credit exist, and this amount is now "
            "reserved - held against the cardholder's balance so it cannot "
            "be spent twice. Capture (also called settlement or clearing "
            "submission) is the merchant's claim: actually move the money "
            "now. Between them lies the hold, visible on the cardholder's "
            "statement as pending, reducing the available balance without "
            "yet being a charge. The split exists so merchants can verify "
            "funds before shipping and capture the exact shipped amount "
            "afterward - including partial captures when an order ships in "
            "pieces. Authorizations expire, typically in about seven days "
            "(longer for travel and lodging), after which the hold falls "
            "off and the merchant must re-authorize. A capture without a "
            "valid authorization is rejected; a capture above the "
            "authorized amount is rejected; the machine guards both doors."
        ),
        "how_it_works": (
            "Authorization travels as an ISO 8583 authorization request "
            "from merchant to acquirer to network to issuer, and the "
            "approval travels back with an authorization code - the "
            "identifier the capture will reference. The issuer places a "
            "hold for the authorized amount, memo-posting it against the "
            "account so available balance drops immediately while the "
            "posted balance waits. Capture travels later as a clearing "
            "message carrying the authorization code and the final amount, "
            "which may be less than authorized (partial capture) but never "
            "more. At clearing, the network computes interchange and the "
            "acquirer settles net funds to the merchant. If the merchant "
            "never captures, the authorization expires and the hold "
            "releases - no money moved, no charge. If the merchant captures "
            "late, the network may treat it as a new authorization and "
            "re-check funds. Voiding an authorization before capture "
            "releases the hold immediately instead of waiting for expiry."
        ),
        "key_points": [
            "Authorization reserves funds (a hold); capture actually moves the money - two steps, two records.",
            "The authorization code is the identifier the capture must reference.",
            "Captures may be partial (less than authorized) but never exceed the authorized amount.",
            "Authorizations expire (about seven days typical); expired holds release with no charge.",
            "A void before capture releases the hold immediately; after capture, the undo is a refund.",
        ],
        "requirements": [
            "Authorization records must carry the approval code, amount, timestamp, and expiry.",
            "Capture records must reference the authorization code and state the captured amount.",
            "The sum of captures against one authorization must never exceed the authorized amount.",
            "Expired authorizations must release holds automatically with no settlement.",
            "Partial captures must each reference the same authorization and track the remaining balance.",
        ],
        "standards": [
            "Card authorization and clearing messages follow ISO 8583 message types and processing codes.",
            "Authorization validity windows and capture rules follow the card networks published operating regulations.",
            "Interchange computation at clearing follows the networks published interchange schedules.",
        ],
        "citations": [CIT_ISO8583, CIT_PCI],
        "sig_lens": (
            "The Signature read: authorization is the covenant spoken, "
            "capture the covenant sealed in money. The Signature Method "
            "keeps the two acts distinct - a spoken promise reserves, only "
            "the sealed act pays - and forbids collecting on a promise "
            "whose time has passed."
        ),
    },
    {
        "key": "payment_methods",
        "name": "Payment Methods Compared: Cards, ACH, Wires, Wallets",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Four rails carry most electronic value, and each writes a "
            "different kind of record. Cards (credit and debit) authorize "
            "in seconds, settle in a day or two, cost the merchant a "
            "percentage plus a fixed fee, and carry rich dispute rights - "
            "the chargeback. ACH (Automated Clearing House) batches "
            "payments into files, settles in one to two business days (or "
            "same-day for a fee), costs pennies per transaction, and "
            "reverses through return codes rather than chargebacks. Wires "
            "(Fedwire, SWIFT) move large amounts same-day with finality - "
            "a sent wire is essentially irreversible - and cost a flat fee "
            "per transfer. Digital wallets (Apple Pay, Google Pay) are not "
            "a rail but a credential vault: they tokenize the card, so the "
            "merchant never sees the real number, and the underlying "
            "record is still a card transaction. Choosing a method is "
            "choosing a bundle: speed, cost, finality, and dispute rights "
            "cannot all be maximized at once."
        ),
        "how_it_works": (
            "Each method works by trading off the four properties. Cards "
            "buy speed and buyer protection with high merchant fees: the "
            "network guarantees the merchant gets paid (minus interchange) "
            "and guarantees the cardholder can dispute. ACH buys cheap "
            "bulk movement with slowness and batching: the originator's "
            "bank sends a file of thousands of entries, settlement nets "
            "through the Federal Reserve, and returns arrive days later "
            "with reason codes. Wires buy finality and size with cost and "
            "irreversibility: each wire is individually authorized, "
            "settled gross in central-bank money, and once credited it "
            "stays credited. Wallets buy security with indirection: the "
            "device holds a token, the token maps to the real card only "
            "inside the network's vault, and a stolen token is useless "
            "elsewhere. The record shape follows the rail: card records "
            "carry authorization codes, ACH records carry batch and trace "
            "numbers, wire records carry IMAD/UTR references."
        ),
        "key_points": [
            "Cards: seconds to authorize, percent-plus-fixed fees, strong dispute rights via chargeback.",
            "ACH: batched, one to two days, pennies per item, reversals via return codes.",
            "Wires: same-day, flat fee, essentially irreversible finality for large amounts.",
            "Wallets tokenize the card credential; the underlying record is still a card transaction.",
            "Speed, cost, finality, and dispute rights trade off - no method maximizes all four.",
        ],
        "requirements": [
            "The payment method and rail must be a stated field on every payment record.",
            "Card records must carry authorization code and network reference; ACH records batch and trace numbers; wires the bank reference.",
            "Fee records must name the fee type (interchange, per-item, flat) and the rail that levied it.",
            "Reversal rights must be documented per method: chargeback windows for cards, return timeframes for ACH, finality for wires.",
            "Settlement timing expectations must be stated per method so pending states are interpretable.",
        ],
        "standards": [
            "Card processing follows ISO 8583 and the card networks operating regulations.",
            "ACH processing follows NACHA Operating Rules including return reason codes and timeframes.",
            "Wire transfers follow Federal Reserve Fedwire format and operating circulars, or SWIFT MT/MX standards cross-border.",
        ],
        "citations": [CIT_ISO8583, CIT_NACHA, CIT_SWIFT],
        "sig_lens": (
            "The Signature read: the four rails are four roads to the "
            "same market - the swift road, the cheap road, the final "
            "road, and the masked road. The Signature Method chooses the "
            "road by the covenant's needs: haste, thrift, certainty, or "
            "secrecy, and never pretends one road is all four."
        ),
    },
    {
        "key": "idempotency",
        "name": "Idempotency Keys and Exactly-Once Processing",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Networks fail, phones lose signal, and users tap pay twice. "
            "Idempotency is the engineering answer: design the operation "
            "so repeating it is harmless. The idempotency key is the "
            "mechanism - a client-generated unique token sent with the "
            "request, which the server stores alongside the result. The "
            "first request with a new key executes and stores its result; "
            "any retry carrying the same key returns the stored result "
            "without executing again. The customer tapped twice but was "
            "charged once; the phone retried three times but the transfer "
            "posted once. Without idempotency, every retry is a gamble: "
            "did the first request fail before charging, or after? The key "
            "turns that gamble into a lookup. Keys must be unique per "
            "intended action (one key per checkout click, not one key per "
            "customer), stored durably, and kept long enough to cover the "
            "retry window - typically at least 24 hours for payments."
        ),
        "how_it_works": (
            "Idempotency works as a guarded write. The client generates a "
            "UUID before sending and includes it as the Idempotency-Key "
            "header (standardized for HTTP in RFC 9110 and adopted by "
            "payment APIs). The server, inside the same database "
            "transaction that posts the payment, inserts the key with the "
            "result; a unique constraint on the key column makes the "
            "second insert fail atomically, so the retry path reads the "
            "stored result instead. The response to a retry is byte-"
            "identical to the original response, which is how the client "
            "knows it was a replay rather than a new charge. Keys expire "
            "after their retention window, after which reuse is rejected "
            "or treated as a new action - documented, either way. The "
            "pattern composes with double-entry: the ledger insert and the "
            "key insert commit together, so a crash cannot charge without "
            "remembering the key."
        ),
        "key_points": [
            "Idempotency makes repeats harmless: the retry returns the stored result instead of acting again.",
            "The client generates the key before sending; the server stores key plus result atomically.",
            "A unique constraint on the key column is the atomic guard - application logic alone is not enough.",
            "One key per intended action: one per checkout click, never one per customer.",
            "Keys need a documented retention window (typically 24 hours or more for payments).",
        ],
        "requirements": [
            "Payment and transfer APIs must accept a client-supplied idempotency key on every mutating call.",
            "Key and result must be stored in the same atomic transaction as the ledger posting.",
            "A database unique constraint must enforce key uniqueness.",
            "Retry responses must be identical to the original response.",
            "The retention window and the behavior after expiry must be documented.",
        ],
        "standards": [
            "Idempotency-Key header semantics follow RFC 9110 HTTP Semantics.",
            "Payment API idempotency practices follow industry-standard patterns for safe retry.",
            "Key storage must meet the same durability and audit requirements as the ledger itself.",
        ],
        "citations": [CIT_RFC9110, CIT_WEYGANDT],
        "sig_lens": (
            "The Signature read: the idempotency key is the seal that "
            "cannot be double-stamped. The Signature Method treats the "
            "repeated knock at the door as one knock heard twice - the "
            "house answers from memory, and the covenant is sealed exactly "
            "once."
        ),
    },
    {
        "key": "refunds",
        "name": "Refunds: Full, Partial, and How They Post",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A refund is the merchant's voluntary undo of a payment: the "
            "customer returns the goods or cancels the service, and the "
            "merchant sends money back through the same rail it arrived "
            "on. A full refund returns the entire settled amount and "
            "closes the sale's books; a partial refund returns part - the "
            "damaged item in a multi-item order, the unused portion of a "
            "service - and the sale remains partly settled. The refund "
            "record must reference the original payment's identifier, "
            "state its own amount in minor units, and carry a reason code "
            "the business can report on. Timing matters: a refund issued "
            "before the original capture settles is really a void or a "
            "reduced capture, not a refund, and the books treat it "
            "differently. Multiple partial refunds may stack, but their "
            "sum must never exceed the settled amount - the machine "
            "guards that door too. Refunds typically reach the customer's "
            "account in three to ten business days, riding the same "
            "settlement rails in reverse."
        ),
        "how_it_works": (
            "A refund works as a linked compensating record. The merchant "
            "system creates a refund record naming the original payment "
            "identifier and the refund amount, validates that settled "
            "minus already-refunded covers the new amount, and submits it "
            "to the processor as a refund (not a new payment) so the "
            "networks route it back along the original path. In double-"
            "entry terms the refund posts mirror entries: debit revenue "
            "(or a refunds-contra account) and credit cash or the merchant "
            "payable. The card networks report the refund in the "
            "merchant's settlement batch as a negative, which is why a "
            "day's net settlement can go negative when refunds exceed "
            "sales. The customer's issuer posts the credit to the account, "
            "usually within days, referencing the original transaction so "
            "the statement shows the pair. Chargebacks are refunds by "
            "force; voluntary refunds are cheaper than chargebacks in fees "
            "and in standing, which is why merchants prefer to refund "
            "before the customer disputes."
        ),
        "key_points": [
            "Full refund returns the whole settled amount; partial refunds stack but must never exceed it.",
            "Every refund references the original payment identifier and carries a reason code.",
            "A pre-capture undo is a void or reduced capture, not a refund - the books differ.",
            "Refunds post as mirror double-entries and settle as negatives in the merchant batch.",
            "Voluntary refunds cost less than chargebacks in fees and standing - refund before dispute.",
        ],
        "requirements": [
            "Refund records must reference the original payment identifier.",
            "The sum of refunds against a payment must never exceed the settled amount - enforced at write time.",
            "Refund reason codes must come from a documented list for reporting.",
            "Refunds must post as new compensating records; the original payment record is never edited.",
            "Settlement reporting must show refunds as negatives against the merchant's net.",
        ],
        "standards": [
            "Card refund processing follows ISO 8583 refund/credit message types and network rules.",
            "ACH reversals and returns follow NACHA return reason codes and timeframes.",
            "Refund accounting follows revenue-reversal practice under standard financial accounting.",
        ],
        "citations": [CIT_ISO8583, CIT_NACHA, CIT_WEYGANDT],
        "sig_lens": (
            "The Signature read: the refund is the honorable release - "
            "the merchant unsealing the covenant by hand rather than by "
            "force. The Signature Method honors the voluntary release "
            "above the forced one, and writes it as its own witnessed act."
        ),
    },
    {
        "key": "returns",
        "name": "Returns and Reverse Logistics Records",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A return is the physical twin of the refund: the goods travel "
            "backward through the supply chain while the money travels "
            "backward through the payment rail. The return record begins "
            "with a return merchandise authorization (RMA) - permission "
            "to send it back, with a window (often 30 days) and conditions "
            "(unopened, with receipt). Receiving inspects the goods and "
            "grades them: resellable to stock, refurbishable to the repair "
            "bench, or disposable to salvage. The grade decides the money: "
            "full refund for resellable, partial for damaged, restocking "
            "fees where policy allows. Each step writes records - RMA "
            "issued, goods received, inspection grade, refund authorized - "
            "and the refund record references the RMA, which references "
            "the order, which references the original payment. Reverse "
            "logistics is forward logistics in a mirror, and the records "
            "must mirror too, or returned goods vanish into a warehouse "
            "with no paper trail."
        ),
        "how_it_works": (
            "Returns work as a gated pipeline. The RMA gate checks the "
            "return window and the order's eligibility, then issues the "
            "authorization with a shipping label; no RMA, no return - this "
            "is how the warehouse knows the box arriving Tuesday is "
            "expected. Receiving scans the RMA, which pulls up the order "
            "and its line items, and inspection records the condition "
            "grade per item. The grade drives the financial decision "
            "through policy rules: resellable triggers full refund of the "
            "item price, damaged triggers partial, missing parts trigger "
            "deductions. The refund record then references both the RMA "
            "and the original payment, closing the loop. Inventory "
            "records update in the same transaction: resellable units "
            "return to available stock, so the website can sell them "
            "again. The whole pipeline is auditable because every gate "
            "stamped a record with a timestamp."
        ),
        "key_points": [
            "The RMA is the gate: permission, window, and conditions, issued before goods move.",
            "Inspection grades each item - resellable, refurbishable, or salvage - and the grade drives the money.",
            "The record chain runs refund to RMA to order to original payment, fully traceable.",
            "Restocking fees and deductions must follow stated policy and appear on the records.",
            "Resellable units return to available stock in the same transaction as the refund decision.",
        ],
        "requirements": [
            "RMA records must carry the order identifier, the return window, and the return conditions.",
            "Receiving and inspection must each write timestamped records with the item grades.",
            "Refund records must reference both the RMA and the original payment identifier.",
            "Policy-driven deductions (restocking fees, damage) must cite the policy and show the math.",
            "Inventory updates for resellable returns must be atomic with the refund authorization.",
        ],
        "standards": [
            "Return windows and condition standards follow the merchant's published policy and consumer protection law.",
            "Inventory record updates follow standard perpetual-inventory practice.",
            "Refund settlement follows the same rail rules as the original payment method.",
        ],
        "citations": [CIT_WEYGANDT, CIT_ISO8583],
        "sig_lens": (
            "The Signature read: the return is the covenant walked "
            "backward with honor - goods and money retracing their steps "
            "through witnessed gates. The Signature Method requires each "
            "gate to stamp its witness, so nothing vanishes on the road "
            "home."
        ),
    },
    {
        "key": "chargebacks",
        "name": "Chargebacks and the Dispute Lifecycle",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A chargeback is a forced refund: the cardholder tells the "
            "issuer the charge was wrong, and the issuer pulls the money "
            "back from the merchant through the network - with a fee. The "
            "dispute lifecycle runs in rounds. First the chargeback "
            "itself, coded by reason: fraud (the cardholder denies the "
            "transaction), authorization issues, processing errors "
            "(duplicate, wrong amount), or consumer disputes (goods not "
            "received, not as described). Then representment: the merchant "
            "answers with evidence - the signed receipt, the delivery "
            "confirmation, the matching IP address - and the network "
            "decides. Then, if the merchant loses, pre-arbitration and "
            "arbitration: escalating rounds with escalating fees. "
            "Timeframes are measured in tens of days per round, and the "
            "whole cycle can span months. Merchants track two numbers "
            "religiously: the chargeback rate (chargebacks divided by "
            "transactions, which must stay under network thresholds around "
            "one percent) and the win rate on representment."
        ),
        "how_it_works": (
            "Chargebacks work by reversing the settlement chain under "
            "network law. The issuer debits the acquirer through the "
            "network for the disputed amount plus a dispute fee; the "
            "acquirer debits the merchant the same day. The merchant's "
            "record for the day shows the forced debit referencing the "
            "original sale by its network reference number. Representment "
            "is the merchant's counter-record: a dispute response message "
            "carrying compelling evidence, submitted before the deadline, "
            "which either reverses the debit or advances the dispute. "
            "Reason codes route the evidence requirements - fraud "
            "disputes want proof the cardholder participated, "
            "not-received disputes want proof of delivery. Prevention is "
            "cheaper than fighting: clear billing descriptors, prompt "
            "refunds, and delivery confirmation stop most disputes before "
            "they are filed. A merchant whose chargeback rate breaches "
            "network thresholds enters monitoring programs with fines - "
            "the network's way of pricing fraud risk back to its source."
        ),
        "key_points": [
            "A chargeback pulls money from the merchant by force, plus a dispute fee, through the network.",
            "Reason codes group disputes: fraud, authorization, processing errors, consumer disputes.",
            "Representment lets the merchant answer with evidence before the deadline.",
            "Lost disputes can escalate to pre-arbitration and arbitration with rising fees.",
            "The chargeback rate must stay under network thresholds; breaching them brings monitoring and fines.",
        ],
        "requirements": [
            "Dispute records must carry the reason code, the disputed amount, and the original network reference.",
            "Representment evidence must be submitted before the network deadline with a timestamp.",
            "Each round (chargeback, representment, pre-arbitration, arbitration) must be a separate linked record.",
            "The chargeback rate must be computed and monitored against network thresholds.",
            "Billing descriptors must be clear and recognizable to prevent disputes at the source.",
        ],
        "standards": [
            "Dispute reason codes and timeframes follow the card networks published dispute rules (for example Visa dispute categories 10 through 13).",
            "Dispute message flows follow ISO 8583 chargeback and representment message types.",
            "Representment evidence standards follow each network's compelling-evidence rules.",
        ],
        "citations": [CIT_ISO8583, CIT_PCI],
        "sig_lens": (
            "The Signature read: the chargeback is the covenant contested "
            "- one maker crying foul, the network sitting as judge. The "
            "Signature Method meets contest with evidence, round by "
            "round, and counts the cost of broken trust in fees."
        ),
    },
    {
        "key": "bank_transfers",
        "name": "Bank Transfers: ACH Batches and Wire Records",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Bank transfers move money directly between bank accounts, and "
            "the two great systems could hardly be more different. ACH "
            "(Automated Clearing House) is the batch system: the "
            "originator's bank assembles a file of thousands of entries - "
            "payrolls, bill payments, debits - each entry naming the "
            "receiving bank by routing number, the account, and the "
            "amount. The file carries batch headers and control totals "
            "that must balance, travels to the Federal Reserve, and "
            "settles in one to two business days (same-day available). "
            "Wires (Fedwire domestically, SWIFT internationally) are the "
            "individual system: each transfer is authorized alone, settled "
            "gross in central-bank money, usually within hours, with "
            "finality - once credited, it stays credited. ACH records are "
            "files of many; wire records are messages of one. ACH can be "
            "returned with reason codes days later; wires essentially "
            "cannot be undone."
        ),
        "how_it_works": (
            "ACH works by file discipline. The originator builds entries "
            "under batch headers (record type 5), each entry a type-6 "
            "record with the receiver's routing and account numbers, "
            "amount, and trace number. Batch control records (type 8) "
            "total the entries - debit and credit totals, entry count, "
            "and a hash of the routing numbers - and the file control "
            "record (type 9) totals the batches; any imbalance rejects "
            "the file. The ODFI (originating bank) warrants the "
            "entries are authorized and sends the file to the ACH "
            "operator; the RDFI (receiving bank) posts to receivers on "
            "the effective entry date. Returns flow back with codes like "
            "R01 (insufficient funds) or R10 (unauthorized), debiting the "
            "originator days after the original credit. Wires work by "
            "message finality: the sending bank debits the sender, sends "
            "a Fedwire or SWIFT message with a unique reference (IMAD "
            "domestically), the receiving bank credits the beneficiary, "
            "and settlement between banks happens in central-bank money "
            "the same day."
        ),
        "key_points": [
            "ACH batches thousands of entries into balanced files; wires settle individually with finality.",
            "ACH files carry batch headers, entry details, and control totals that must balance or the file rejects.",
            "Settlement: ACH in one to two business days (same-day available); wires usually within hours.",
            "ACH returns arrive days later with reason codes; wires are essentially irreversible.",
            "The ODFI warrants authorization for ACH; each wire is individually authorized before sending.",
        ],
        "requirements": [
            "ACH files must contain balanced batch and file control totals or be rejected.",
            "Each ACH entry must carry originator and receiver routing numbers, account, amount, and trace number.",
            "Wire records must carry the bank's unique reference (IMAD or SWIFT reference) for tracing.",
            "Return records must carry the NACHA return reason code and reference the original trace number.",
            "Effective entry dates must respect the rail's processing calendar and cutoff times.",
        ],
        "standards": [
            "ACH file layout, batching, and return codes follow NACHA Operating Rules & Guidelines.",
            "Domestic wires follow Federal Reserve Fedwire format and operating circulars.",
            "Cross-border wires follow SWIFT MT/MX message standards.",
        ],
        "citations": [CIT_NACHA, CIT_SWIFT],
        "sig_lens": (
            "The Signature read: ACH is the covenant of the multitude - "
            "thousands of promises balanced in one sealed file - and the "
            "wire is the covenant of the single great promise, sealed "
            "alone and forever. The Signature Method honors both: the "
            "many weighed together, the one weighed alone."
        ),
    },
    {
        "key": "card_flow",
        "name": "The Card Transaction Flow: Authorization to Clearing",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Follow one card swipe from the terminal to the merchant's "
            "bank account and you walk the whole payment industry. The "
            "terminal reads the card (or its token) and sends an "
            "authorization request: card number or token, amount, "
            "merchant identifier. The acquirer routes it to the network "
            "(Visa, Mastercard), which routes it to the issuer - the "
            "cardholder's bank. The issuer checks the account: valid "
            "card, sufficient funds or credit, no fraud flag - and "
            "replies with an approval code or a decline code, in about "
            "two seconds. The approval code returns to the terminal, the "
            "sale completes, and the issuer posts a hold. Later that day "
            "the merchant's system submits the clearing file: every "
            "approved authorization with its final captured amount. The "
            "network computes interchange (the issuer's fee, a percentage "
            "of each transaction), nets everything multilaterally, and "
            "the acquirer deposits the net - sales minus refunds minus "
            "fees - into the merchant's account, usually next business "
            "day. Five companies touched the money; the records at each "
            "hop must agree."
        ),
        "how_it_works": (
            "The flow works as a relay of ISO 8583 messages. The "
            "authorization request (message type 0100) carries the "
            "primary account number or token, processing code, amount, "
            "and merchant data; the response (0110) carries the approval "
            "or decline code. Clearing messages (1240/1440 family) carry "
            "the same transaction with the final amount and the "
            "authorization code for matching. The network's clearing "
            "system pairs each clearing record with its authorization, "
            "applies the interchange schedule for the card product and "
            "merchant category, and produces settlement totals per "
            "acquirer and issuer. Settlement is net: each participant's "
            "day sums to one number owed or owing, moved by wire between "
            "settlement accounts. Reconciliation at each hop matches the "
            "hop's sent records against received records; a clearing "
            "record with no matching authorization is an exception, and "
            "an authorization with no clearing record expires quietly."
        ),
        "key_points": [
            "Authorization approves in about two seconds; clearing submits the final amounts later the same day.",
            "The approval code links the authorization to its clearing record across all five hops.",
            "Interchange is computed at clearing from the card product and merchant category schedules.",
            "Settlement is multilateral netting: each participant settles one net number per day.",
            "Clearing without authorization is an exception; authorization without clearing expires quietly.",
        ],
        "requirements": [
            "Authorization records must carry the approval code, amount, timestamp, and card or token identifier.",
            "Clearing records must carry the same approval code with the final captured amount.",
            "Interchange computations must cite the applicable schedule (card product, merchant category).",
            "Settlement records must show the net position per participant with the component totals.",
            "Each hop must reconcile sent against received records daily.",
        ],
        "standards": [
            "Message types and fields follow ISO 8583-1.",
            "Interchange schedules follow the card networks published interchange programs.",
            "Settlement timing follows the networks operating regulations for the region.",
        ],
        "citations": [CIT_ISO8583],
        "sig_lens": (
            "The Signature read: the card flow is the covenant relayed "
            "by five sworn messengers - terminal, acquirer, network, "
            "issuer, and back. The Signature Method requires each "
            "messenger to stamp the relay, so the promise can be traced "
            "hand to hand from swipe to settlement."
        ),
    },
    {
        "key": "reconciliation",
        "name": "Reconciliation: Matching Two Ledgers",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Reconciliation is the daily proof that the money story is "
            "true: take two independent records of the same events - the "
            "merchant's sales ledger and the processor's settlement "
            "report, the company's books and the bank statement - and "
            "match them line by line. Every match is a confirmed truth; "
            "every break is a question. The unmatched items have names: "
            "timing differences (the sale recorded today settles "
            "tomorrow), fees (the processor deducted interchange the "
            "merchant never recorded), duplicates (the retry that posted "
            "twice), and orphans (the refund with no findable sale). The "
            "process runs in three passes: automatic matching on "
            "identifier and amount, fuzzy matching on amount and date for "
            "the stragglers, and human review for the remainder. A clean "
            "reconciliation ends with every item matched or explained and "
            "the two totals agreeing to the cent. An unreconciled ledger "
            "is an unaudited claim - the numbers might be right, but "
            "nobody has proven it."
        ),
        "how_it_works": (
            "Reconciliation works by joining on identity. The engine "
            "loads both ledgers into a common shape - identifier, "
            "amount in minor units, currency, event date, type - and "
            "matches first on exact identifier plus amount, which clears "
            "the vast majority. The leftovers go to tolerance matching: "
            "same amount within a date window (catching settlement lag), "
            "then same identifier with a fee-sized difference (catching "
            "unrecorded fees). Each proposed match carries a confidence "
            "and a rule name, and anything below the auto-match threshold "
            "queues for a human with both records side by side. Breaks "
            "are classified, not just listed: timing, fee, duplicate, "
            "orphan, amount mismatch - because the classification "
            "decides the fix. The run itself is a record: which ledgers, "
            "which rules, how many matched, which breaks remain, signed "
            "off by whom. Tomorrow's run starts from today's open breaks, "
            "so nothing ages silently."
        ),
        "key_points": [
            "Reconciliation matches two independent records of the same events, line by line.",
            "Three passes: exact matching on identifier and amount, fuzzy matching on amount and date, human review.",
            "Breaks are classified - timing, fee, duplicate, orphan, amount mismatch - because the class decides the fix.",
            "The reconciliation run is itself a record: ledgers, rules, match counts, open breaks, sign-off.",
            "Open breaks carry forward daily so nothing ages silently.",
        ],
        "requirements": [
            "Both ledgers must be normalized to identifier, minor-unit amount, currency, event date, and type before matching.",
            "Match rules must be documented with confidence thresholds; below-threshold matches need human review.",
            "Every break must be classified and assigned, never merely listed.",
            "The run record must name the ledgers, rules, counts, and the sign-off party.",
            "Unresolved breaks must age visibly with escalating review.",
        ],
        "standards": [
            "Bank reconciliation practice follows standard financial accounting controls for cash.",
            "ISO 20022 camt.053 bank statements provide the standard electronic form of one side of the match.",
            "NACHA return and correction records provide the standard form of ACH-side breaks.",
        ],
        "citations": [CIT_WEYGANDT, CIT_ISO20022, CIT_NACHA],
        "sig_lens": (
            "The Signature read: reconciliation is the truth-telling - "
            "two witnesses sworn separately, their stories laid side by "
            "side. The Signature Method calls a matched line a confirmed "
            "covenant and an unmatched line an open question, and forbids "
            "closing the books while questions stand."
        ),
    },
    {
        "key": "settlement",
        "name": "Clearing and Settlement",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Clearing and settlement are the two acts that turn promises "
            "into money. Clearing computes who owes whom: the network "
            "takes the day's authorizations-turned-captures, applies fees, "
            "and produces net positions - each participant's single number "
            "for the day. Settlement moves the money: the debtors pay the "
            "net amounts, usually by wire between settlement accounts at "
            "a central bank, and the creditors are credited. The two are "
            "separated because netting collapses thousands of gross "
            "transfers into a handful of net ones - cheaper, faster, and "
            "less risky than moving every payment individually. Settlement "
            "can be gross (each transfer settled alone, as in Fedwire and "
            "real-time systems) or net (batched and offset, as in card "
            "networks and ACH). Finality is the legal moment the payment "
            "becomes irrevocable, and it arrives at settlement, not at "
            "authorization - a promise is not a payment until it settles."
        ),
        "how_it_works": (
            "Clearing works by multilateral netting. Each participant "
            "submits its clearing records; the clearinghouse sums each "
            "participant's debits and credits across all counterparties "
            "into one net position - positive meaning owed money, "
            "negative meaning owing. Settlement then moves only the net "
            "amounts: in a net system, participants with negative "
            "positions fund the settlement account and positives are paid "
            "out, all in central-bank money. Gross systems skip the "
            "netting: each payment settles individually and finally in "
            "real time. Timing is by cycle: card networks settle next "
            "business day, ACH settles on the effective entry date, wires "
            "settle same-day, instant rails settle in seconds. Settlement "
            "risk - a participant failing between clearing and settlement "
            "is managed by collateral, caps, and loss-sharing rules, "
            "which is why settlement records name the guarantors as well "
            "as the amounts."
        ),
        "key_points": [
            "Clearing computes net positions; settlement moves the net money - two acts, often a day apart.",
            "Multilateral netting collapses thousands of gross transfers into a handful of net payments.",
            "Gross settlement (Fedwire, instant rails) settles each payment alone and finally.",
            "Finality arrives at settlement, not at authorization - a promise is not a payment until it settles.",
            "Settlement risk between clearing and settlement is managed by collateral, caps, and loss-sharing.",
        ],
        "requirements": [
            "Clearing records must show gross components and the resulting net position per participant.",
            "Settlement records must show the funding movements in central-bank or settlement-account money.",
            "The settlement cycle (same-day, next-day, instant) must be stated per rail.",
            "Finality rules must be documented: the exact moment a payment becomes irrevocable.",
            "Failed-settlement procedures (collateral use, loss sharing) must be part of the record set.",
        ],
        "standards": [
            "Card network settlement follows the networks operating regulations for the region.",
            "Fedwire settlement follows Federal Reserve operating circulars.",
            "Cross-border settlement messaging follows SWIFT and ISO 20022 standards.",
        ],
        "citations": [CIT_ISO8583, CIT_SWIFT, CIT_ISO20022],
        "sig_lens": (
            "The Signature read: clearing is the reckoning, settlement "
            "the paying. The Signature Method separates the counting of "
            "the debt from the delivery of the coin - and declares the "
            "covenant fulfilled only when the coin is delivered, never "
            "when it is merely counted."
        ),
    },
    {
        "key": "fees",
        "name": "The Anatomy of a Fee: Interchange, Assessment, Markup",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Every electronic payment carries a tax nobody voted for: the "
            "processing fee, and it has three organs. Interchange is the "
            "largest - a percentage of the transaction (plus a small fixed "
            "amount) paid to the cardholder's issuer, compensating the "
            "issuer for fraud risk, funding costs, and rewards programs. "
            "Its rate depends on the card product (rewards cards cost "
            "more than basic debit), the merchant category, and how the "
            "card was presented (in-person cheaper than keyed-in). "
            "Assessments are the network's own toll - fractions of a "
            "percent paid to Visa or Mastercard for carrying the "
            "messages. Markup is the processor's margin: the acquirer's "
            "cut for onboarding the merchant, providing the terminal, and "
            "taking the settlement risk. A 100-dollar sale might lose "
            "1.65 to interchange, 0.13 to assessments, and 0.25 to "
            "markup - 2.03 total - leaving the merchant 97.97. ACH moves "
            "the same 100 dollars for pennies; wires for a flat fee. The "
            "fee records matter because they are the merchant's second-"
            "largest controllable cost after labor."
        ),
        "how_it_works": (
            "Fees work by deduction at clearing. When the network clears "
            "the day's transactions, it looks up each transaction's "
            "interchange rate from the published schedule - hundreds of "
            "rows keyed by card product, merchant category code, and "
            "transaction conditions - and computes the issuer's share. "
            "Assessments are computed on gross volume at the network's "
            "stated rate. The acquirer then applies the merchant's "
            "pricing model: interchange-plus passes all three components "
            "through transparently itemized; tiered or flat-rate pricing "
            "bundles them into qualified, mid-qualified, and non-"
            "qualified buckets (or one flat percent). The merchant's "
            "settlement deposit is the net: sales minus refunds minus all "
            "three fee components. Reconciliation proves the fees: the "
            "merchant re-computes interchange from the schedule for a "
            "sample of transactions and compares it to what was "
            "deducted - the standard defense against padded markups."
        ),
        "key_points": [
            "Interchange (to the issuer) is the largest component, set by published schedules on card product and merchant category.",
            "Assessments (to the network) are fractions of a percent on gross volume.",
            "Markup (to the processor) is the acquirer's margin; pricing models pass it through or bundle it.",
            "The merchant's deposit is net: sales minus refunds minus all three fee components.",
            "Merchants defend themselves by re-computing interchange from the schedule and comparing.",
        ],
        "requirements": [
            "Fee records must itemize interchange, assessment, and markup separately, never as one lump.",
            "Interchange computations must cite the schedule row (card product, merchant category, conditions).",
            "The merchant pricing model (interchange-plus, tiered, flat) must be documented.",
            "Settlement reports must show gross sales, refunds, each fee component, and the net deposit.",
            "Fee disputes must reference the specific transactions and schedule rows in question.",
        ],
        "standards": [
            "Interchange rates follow the card networks published interchange schedules for the region.",
            "Assessment rates follow the networks published network fee schedules.",
            "Merchant category codes follow ISO 18245 for retail financial services.",
        ],
        "citations": [CIT_ISO8583, CIT_PCI],
        "sig_lens": (
            "The Signature read: the fee is the toll on the covenant "
            "road - paid to the guards (issuer), the road-keepers "
            "(network), and the guides (processor). The Signature Method "
            "demands the toll be itemized in the open, for a hidden toll "
            "is a tax, and a tax unagreed is no covenant."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "double_entry_scale",
        "name": "Double-Entry Reconciliation at Scale",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Double-entry bookkeeping stops being a classroom exercise "
            "and becomes infrastructure at about a thousand transactions "
            "a day. At scale, every payment event fans out into a spray "
            "of balanced entries: the sale debits cash and credits "
            "revenue; the fee debits processing expense and credits the "
            "merchant payable; the settlement debits the payable and "
            "credits the bank account; the refund reverses the sale's "
            "entries through a contra-revenue account so gross sales stay "
            "honest. The trial balance runs continuously, not monthly - "
            "a streaming sum over the journal that must read zero at "
            "every commit, enforced by database constraints rather than "
            "by hope. Partitioning keeps it fast: the journal is append-"
            "only and partitioned by day, account balances are "
            "materialized caches recomputed from the journal, and the "
            "cache is never the truth - the journal is. When the trial "
            "balance breaks at scale, the cause is almost always one of "
            "three: a non-atomic write that posted one leg without the "
            "other, a rounding mode disagreement between two systems, or "
            "an entry posted to a retired account."
        ),
        "how_it_works": (
            "Scale works by making balance a property of the write path. "
            "Each business event is translated into its entry set by a "
            "posting rules engine - sale, fee, settlement, refund, "
            "chargeback each have their debit-credit template - and the "
            "whole set commits in one database transaction with a check "
            "constraint that debits equal credits. The journal table is "
            "insert-only: no updates, no deletes, with a monotonically "
            "increasing sequence so replay order is unambiguous. Account "
            "balances are maintained as running totals updated by "
            "triggers or stream processors, and a nightly job re-derives "
            "every balance from the raw journal and compares - the "
            "reconciliation of the ledger with itself. Multi-currency "
            "adds a dimension: each entry carries the transaction "
            "currency amount and the functional-currency equivalent at "
            "the day's rate, and FX gains and losses post as their own "
            "balanced entries. The audit trail is the journal itself, "
            "hash-chained per batch so tampering breaks the chain."
        ),
        "key_points": [
            "At scale each payment event fans out into a spray of balanced entries: sale, fee, settlement, refund.",
            "Balance is enforced by database constraints on the write path, not by periodic hope.",
            "The journal is append-only and partitioned; balances are caches, and the journal is the truth.",
            "A nightly re-derivation reconciles the ledger with itself, catching cache drift.",
            "Multi-currency entries carry both currencies; FX gains and losses post as their own balanced entries.",
        ],
        "requirements": [
            "A posting rules engine must translate each business event into a balanced entry set via documented templates.",
            "All legs of an event must commit atomically with a debits-equal-credits constraint.",
            "The journal must be insert-only with a monotonic sequence for unambiguous replay order.",
            "Balances must be re-derivable from the journal on demand; caches must be verified, not trusted.",
            "Rounding modes must be identical across every system that posts to the journal.",
        ],
        "standards": [
            "Journal completeness and immutability follow standard financial accounting control practice.",
            "Multi-currency translation follows FASB ASC 830 foreign currency guidance.",
            "Electronic record retention follows applicable financial recordkeeping regulations.",
        ],
        "citations": [CIT_WEYGANDT],
        "sig_lens": (
            "The Signature read: at scale the twin witnesses become a "
            "legion - every coin with its shadow, every promise with its "
            "mirror, all marching in step. The Signature Method keeps the "
            "legion honest with one law above all: no entry walks alone."
        ),
    },
    {
        "key": "iso20022",
        "name": "ISO 20022: The MX Message Grammar",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "ISO 20022 is the dictionary the world's payment systems are "
            "converging on: a single standardized grammar for financial "
            "messages, written in XML (and increasingly JSON), that "
            "replaces the patchwork of legacy formats. Its payments "
            "messages have a strict family structure. The pain family "
            "(payment initiation) carries customer-to-bank instructions: "
            "pain.001 is the credit transfer initiation - pay these "
            "people these amounts. The pacs family (payments clearing and "
            "settlement) carries bank-to-bank value movement: pacs.008 "
            "is the customer credit transfer - the actual money message. "
            "The camt family (cash management) carries reporting: camt.053 "
            "is the bank-to-customer statement, camt.054 the debit-credit "
            "notification. Every message is built from a shared business "
            "model - parties, accounts, amounts with ISO 4217 currencies, "
            "identifiers - so a pain.001 from a corporate in Ohio and a "
            "pacs.008 from a bank in Singapore describe the same reality "
            "in the same words. The global migration (SWIFT, Fedwire, "
            "TARGET2, CHIPS) makes ISO 20022 the native tongue of "
            "cross-border value."
        ),
        "how_it_works": (
            "ISO 20022 works through layered definition. The business "
            "model defines concepts - debtor, creditor, amount, "
            "identification - once, in a central repository; each message "
            "type is a view over that model, so pain.001 and pacs.008 "
            "cannot disagree about what a debtor is. Messages are "
            "validated against published XML schemas: a pacs.008 missing "
            "its required debtor agent element is rejected before it "
            "travels. Identification elements provide the lineage: the "
            "instruction ID (the sender's reference), the end-to-end ID "
            "(surviving the whole chain from debtor to creditor), and "
            "the transaction ID (the system's own). Status reporting "
            "closes the loop: pacs.002 reports acceptance or rejection "
            "with reason codes, so the sender's pending becomes settled "
            "or failed with a machine-readable why. Richer data rides "
            "along - structured remittance information, ultimate debtor "
            "and creditor - which is why compliance screening and "
            "reconciliation both improve under ISO 20022."
        ),
        "key_points": [
            "pain initiates (customer to bank), pacs moves value (bank to bank), camt reports (bank to customer).",
            "One shared business model means all message types agree on what debtor, creditor, and amount mean.",
            "Messages validate against published schemas; missing required elements reject before traveling.",
            "Instruction ID, end-to-end ID, and transaction ID provide lineage across the whole chain.",
            "pacs.002 status reports close the loop with machine-readable acceptance or rejection reasons.",
        ],
        "requirements": [
            "Messages must validate against the published ISO 20022 schema for their type and version.",
            "Every payment message must carry instruction, end-to-end, and transaction identifiers.",
            "Amounts must carry ISO 4217 currency codes with the message's decimal conventions.",
            "Structured party identification (debtor, creditor, agents) must be present where the message requires.",
            "Status reports must be processed to move records from pending to settled or failed with reasons.",
        ],
        "standards": [
            "Message definitions follow ISO 20022-1:2021 and the published message usage guidelines.",
            "Currency and amount representation follows ISO 4217 within ISO 20022 decimal rules.",
            "Migration timelines follow each market infrastructure's published ISO 20022 adoption plan.",
        ],
        "citations": [CIT_ISO20022, CIT_ISO4217],
        "sig_lens": (
            "The Signature read: ISO 20022 is the common tongue of the "
            "covenant - one grammar so that a promise spoken in Ohio is "
            "understood in Singapore. The Signature Method honors the "
            "shared words, for covenants fail first in translation."
        ),
    },
    {
        "key": "swift_mt_mx",
        "name": "SWIFT MT and MX Messages for Cross-Border Payments",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Before the MX grammar there was the MT grammar, and trillions "
            "still travel in it. SWIFT MT messages are the terse, "
            "field-tagged telegrams of correspondent banking: MT103 is "
            "the single customer credit transfer - pay this beneficiary "
            "this amount - with fields like :20: (sender's reference), "
            ":32A: (value date, currency, amount), :50: (ordering "
            "customer), and :59: (beneficiary). MT202 is the bank-to-bank "
            "transfer moving the cover funds behind the MT103. MT940 and "
            "MT950 are the customer statements, the other side of the "
            "reconciliation match. The MX migration maps each to an ISO "
            "20022 equivalent: MT103 becomes pacs.008, MT202 becomes "
            "pacs.009, MT940/950 become camt.053. During the long "
            "coexistence, translation services convert between them - and "
            "translation is where data is lost, because MT fields are "
            "terse and unstructured where MX elements are rich and "
            "structured. Cross-border records must therefore carry both "
            "forms during migration, and reconciliation must match across "
            "the translation."
        ),
        "how_it_works": (
            "MT messages work as structured telegrams. Each message is a "
            "sequence of tagged fields - :20:, :32A:, :50K:, :59: - with "
            "fixed formats validated by the SWIFT network before delivery; "
            "a malformed :32A: never leaves the sender's terminal. The "
            "correspondent chain works by cover: the ordering customer's "
            "bank sends the MT103 with the payment details directly to "
            "the beneficiary's bank, and sends the MT202 cover moving the "
            "actual funds through correspondent accounts - two messages, "
            "one economic event, matched by reference. Fees are taken in "
            "transit under the OUR/BEN/SHA charge options: OUR means the "
            "sender pays all charges, SHA splits them, BEN deducts them "
            "from the beneficiary. The MX equivalents carry the same "
            "economics with structured parties and remittance data, which "
            "is why sanctions screening and straight-through processing "
            "rates improve - fewer payments stop for manual repair."
        ),
        "key_points": [
            "MT103 carries the customer payment details; MT202 moves the cover funds; MT940/950 report the statements.",
            "Tagged fields (:20:, :32A:, :50:, :59:) are validated by the network before delivery.",
            "OUR/BEN/SHA charge options decide who pays the transit fees.",
            "MX migration maps MT103 to pacs.008, MT202 to pacs.009, MT940/950 to camt.053.",
            "Translation between MT and MX can lose data - carry both forms and reconcile across them.",
        ],
        "requirements": [
            "Cross-border payment records must carry the sender's reference (:20:) and the full field set.",
            "Value date, currency, and amount (:32A:) must be validated to format before sending.",
            "The charge option (OUR/BEN/SHA) must be stated and the deducted charges itemized.",
            "Cover payments (MT202/pacs.009) must be linked to their customer transfers (MT103/pacs.008) by reference.",
            "During migration, records must retain both the MT and MX forms of each message.",
        ],
        "standards": [
            "MT field formats and validation follow the SWIFT message standards.",
            "MX equivalents follow ISO 20022 message definitions.",
            "Charge option semantics follow SWIFT and market practice for correspondent banking.",
        ],
        "citations": [CIT_SWIFT, CIT_ISO20022],
        "sig_lens": (
            "The Signature read: the MT telegram is the covenant sent by "
            "wire across the sea - terse, exact, and unforgiving of "
            "error. The Signature Method keeps both the old telegram and "
            "the new letter, and reconciles across the translation so no "
            "promise is lost between tongues."
        ),
    },
    {
        "key": "nacha",
        "name": "NACHA and the ACH Record Layout",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The NACHA file is the most literal transaction record in "
            "American finance: a fixed-width text file where every line "
            "is a record and every column has a meaning. A file opens "
            "with a type-1 file header naming the originator and the "
            "creation date-time. Inside, each batch opens with a type-5 "
            "batch header (company name, effective entry date, entry "
            "class code), carries its type-6 entry detail records (each "
            "with the receiver's routing number, account number, amount, "
            "and trace number), optionally type-7 addenda (one extra "
            "record of remittance text per entry), and closes with a "
            "type-8 batch control record totaling the batch. The file "
            "closes with a type-9 file control record totaling the "
            "batches. The control totals are the file's conscience: debit "
            "totals, credit totals, entry counts, and a hash of the "
            "routing numbers must agree with the detail records, or the "
            "whole file is rejected. Returns come back as new entries "
            "with R-codes - R01 insufficient funds, R10 unauthorized - "
            "referencing the original trace number."
        ),
        "how_it_works": (
            "The layout works by positional discipline. Every record is "
            "94 characters; the record type sits in position 1, and each "
            "field occupies fixed columns - amount in columns 88-97 as "
            "dollars and cents, routing numbers as nine digits with a "
            "check digit. The batch control's entry hash adds the "
            "eight-digit routing prefixes of every entry and keeps the "
            "rightmost ten digits - a checksum that catches transposed "
            "digits. The ODFI (the originating bank) validates the file, "
            "warrants that each debit was authorized, and submits it to "
            "the ACH operator by the submission deadline; the operator "
            "sorts entries to RDFIs, which post them on the effective "
            "entry date. Same-day ACH adds extra submission windows with "
            "earlier deadlines and per-transaction amount caps. Returns "
            "must be dispatched within the NACHA timeframes - two banking "
            "days for most, longer for unauthorized consumer debits - and "
            "each return references the original trace number so the "
            "originator can match it to the exact entry."
        ),
        "key_points": [
            "Fixed 94-character records: type 1 file header, 5 batch header, 6 entry detail, 7 addenda, 8 batch control, 9 file control.",
            "Control totals (debits, credits, counts, routing hash) must agree with detail records or the file rejects.",
            "The ODFI warrants authorization and submits by deadline; the RDFI posts on the effective entry date.",
            "Same-day ACH adds earlier windows and amount caps for faster value.",
            "Returns carry R-codes and the original trace number within NACHA timeframes.",
        ],
        "requirements": [
            "Every record must be exactly 94 characters with fields in their specified columns.",
            "Batch and file control totals must be computed from the detail records and must balance.",
            "Each entry must carry a trace number unique within the file for return matching.",
            "Amounts must be stated in dollars and cents as fixed-format numerics.",
            "Return entries must carry the NACHA return reason code and the original trace number.",
        ],
        "standards": [
            "File layout, batching, and control totals follow NACHA Operating Rules & Guidelines.",
            "Return reason codes and timeframes follow the NACHA return rules.",
            "Routing numbers follow the ABA nine-digit format with check digit.",
        ],
        "citations": [CIT_NACHA],
        "sig_lens": (
            "The Signature read: the NACHA file is the covenant ledger "
            "in its most disciplined form - ninety-four columns, no more, "
            "no less, every promise in its place and the totals sworn at "
            "the end. The Signature Method admires the fixed column: "
            "freedom in the promise, iron in the form."
        ),
    },
    {
        "key": "pci_dss",
        "name": "PCI DSS and Protecting Card Data",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "PCI DSS - the Payment Card Industry Data Security Standard, "
            "version 4.0 published March 2022 - is the rulebook for "
            "everyone who touches card data, and it shapes transaction "
            "records directly. Its core commandments for records: never "
            "store sensitive authentication data after authorization - no "
            "full magnetic-stripe data, no card verification codes (CVV), "
            "no PIN blocks, ever. The primary account number (PAN), where "
            "stored, must be rendered unreadable - encrypted, hashed, or "
            "truncated. Receipts and displays must show at most the last "
            "four digits. Access to card data must be logged, restricted "
            "to business need, and reviewed. For transaction records this "
            "means the record keeps the last four digits, the "
            "authorization code, the token or network reference - "
            "everything needed to reconcile and dispute - and discards or "
            "never captures the rest. Tokenization completes the picture: "
            "the merchant stores a random token, the vault maps it to the "
            "real PAN, and a breach of the merchant yields nothing usable."
        ),
        "how_it_works": (
            "Protection works by shrinking what the record knows. At the "
            "point of capture, the PAN travels encrypted from the "
            "terminal to the processor; the processor returns a token "
            "that the merchant's systems use forever after - the "
            "transaction record references the token, not the card. "
            "Where the PAN must be stored (by processors and acquirers), "
            "it is encrypted with managed keys or replaced by a "
            "one-way hash for searching, with the last four kept in the "
            "clear for customer service. Truncation rules govern every "
            "display: receipts, screens, and logs show at most the first "
            "six and last four digits, and usually just the last four. "
            "The standard's twelve requirement groups then wrap the "
            "systems around the data: firewalls, no vendor defaults, "
            "protected stored data, encrypted transmission, anti-malware, "
            "secure development, restricted access, authentication, "
            "physical security, logging, testing, and policy. A "
            "transaction record that follows the rules is reconcilable "
            "and disputable without being stealable."
        ),
        "key_points": [
            "Never store sensitive authentication data after authorization: no full stripe data, no CVV, no PIN blocks.",
            "Stored PANs must be rendered unreadable - encrypted, hashed, or truncated.",
            "Receipts and displays show at most the last four digits.",
            "Records keep tokens and network references - everything needed to reconcile - and discard the rest.",
            "Tokenization means a merchant breach yields tokens, not card numbers.",
        ],
        "requirements": [
            "Transaction records must never contain full magnetic-stripe data, CVV, or PIN blocks.",
            "Any stored PAN must be encrypted or hashed, with access logged and restricted.",
            "All displays and receipts must truncate the PAN to at most the last four digits.",
            "Card numbers in records should be replaced by tokens wherever the business allows.",
            "Access to cardholder data environments must follow the PCI DSS requirement groups.",
        ],
        "standards": [
            "Card data protection follows PCI DSS v4.0 (PCI Security Standards Council, March 2022).",
            "Receipt PAN truncation follows PCI DSS display requirements.",
            "Tokenization follows industry token vault practices under PCI scope guidance.",
        ],
        "citations": [CIT_PCI, CIT_ISO8583],
        "sig_lens": (
            "The Signature read: PCI DSS is the law of the sealed "
            "letter - the covenant's secret kept from all but its "
            "makers. The Signature Method keeps the seal (the last four) "
            "and burns the wax impression (the full number), so the "
            "promise can be proven without being stolen."
        ),
    },
    {
        "key": "fraud_signals",
        "name": "Fraud Signals Hidden in Transaction Records",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Fraud rarely announces itself; it whispers in the records. "
            "The signals are patterns across transactions, not single "
            "events. Velocity: a card used twelve times in ten minutes "
            "across three cities is not shopping, it is testing. Amount "
            "anomalies: a 1-dollar authorization followed by a large "
            "purchase is the classic card-testing probe. Geography: a "
            "card present in New York and in Singapore within the hour "
            "defies physics. Merchant mismatch: a grocery card suddenly "
            "buying electronics at 3 a.m. breaks the cardholder's "
            "profile. Refund anomalies: refunds with no matching sale, "
            "or refund amounts exceeding sales, signal internal fraud or "
            "processing errors. Round-number wires just under reporting "
            "thresholds signal structuring. Each signal is weak alone - "
            "people do travel, do shop at 3 a.m. - so systems score them "
            "in combination: velocity plus geography plus amount anomaly "
            "is a blocked transaction; any one alone is a step-up "
            "authentication. The records are the evidence; the scoring is "
            "the judgment."
        ),
        "how_it_works": (
            "Detection works by comparing each transaction against "
            "history in real time. The authorization request arrives with "
            "card, amount, merchant, location, and device data; the risk "
            "engine looks back over the card's recent history - counts "
            "and sums over sliding windows (10 minutes, 24 hours), "
            "distinct locations, merchant categories - and computes "
            "features. Rules catch the known shapes: more than N "
            "authorizations in M minutes, amounts matching probe "
            "patterns, impossible travel between consecutive locations. "
            "Models catch the unknown shapes: the transaction's distance "
            "from the cardholder's learned profile across dozens of "
            "dimensions. The score routes the decision: approve, decline, "
            "or step up (demand a second factor). Every decision writes "
            "a record - the score, the top contributing signals, the "
            "outcome - because a declined good customer is a cost, and "
            "the records of past decisions train tomorrow's models. "
            "Post-authorization, settlement-time review catches what "
            "real-time missed: the refund anomaly, the structuring "
            "pattern, the merchant whose chargebacks cluster."
        ),
        "key_points": [
            "Signals: velocity, amount anomalies, impossible geography, merchant mismatch, refund anomalies, structuring.",
            "Each signal is weak alone; scored in combination they route approve, decline, or step-up.",
            "Real-time scoring compares the transaction against sliding-window history and the learned profile.",
            "Every decision is recorded - score, signals, outcome - because false declines cost money too.",
            "Settlement-time review catches refund anomalies and structuring that real-time missed.",
        ],
        "requirements": [
            "Risk decisions must be recorded with the score, contributing signals, and outcome.",
            "Velocity and aggregation windows must be documented per signal.",
            "Step-up authentication must be available as a middle path between approve and decline.",
            "Decline and step-up rates must be monitored to bound false-positive cost.",
            "Post-settlement review must cover refunds, chargeback clusters, and threshold-proximate amounts.",
        ],
        "standards": [
            "Card fraud reporting follows the card networks fraud reporting programs and thresholds.",
            "Transaction monitoring for money-laundering patterns follows applicable AML recordkeeping rules.",
            "Authentication step-up follows strong customer authentication practice where required.",
        ],
        "citations": [CIT_ISO8583, CIT_PCI],
        "sig_lens": (
            "The Signature read: fraud signals are the signs of the "
            "false covenant - the seal pressed too often, the witness in "
            "two cities at once. The Signature Method reads the signs "
            "together, for one sign is rumor and three are testimony."
        ),
    },
    {
        "key": "audit_trails",
        "name": "Audit Trails: Hash Chains and Immutable History",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "An audit trail is the transaction record's memory of itself: "
            "a complete, ordered, tamper-evident history of everything "
            "that happened to the records. Every creation, every state "
            "transition, every correction-as-new-record, every human who "
            "touched them - who, what, when, and the before-and-after "
            "values. Tamper-evidence comes from hash chaining: each trail "
            "entry includes the cryptographic hash of the previous entry, "
            "so altering any entry breaks every later link, and the break "
            "is detectable by recomputation. Immutability comes from "
            "write-once storage and access controls: the trail is "
            "append-only, and even administrators cannot rewrite it - "
            "corrections are new entries. Completeness is the hard part: "
            "a trail that misses the database administrator's direct "
            "edits is theater, so all write paths - application, batch, "
            "manual - must flow through the trail. Auditors do not trust; "
            "they verify: replay the chain, check the hashes, and the "
            "history proves itself."
        ),
        "how_it_works": (
            "Hash chaining works like a daisy chain of fingerprints. "
            "Entry N contains the event data plus H(entry N-1), where H "
            "is a cryptographic hash such as SHA-256. To verify, the "
            "auditor recomputes each hash from the stored previous entry "
            "and compares it to the stored hash; any alteration of any "
            "entry changes its hash, which mismatches the next entry's "
            "stored previous-hash, and the mismatch cascades to the "
            "head. Timestamps are bound into the hashed data so entries "
            "cannot be reordered silently. For stronger proof, chains are "
            "anchored: the periodic head hash is published or countersigned "
            "externally, so even the chain's keeper cannot rewrite from "
            "the start without the anchor disagreeing. Retention policies "
            "decide how long the trail lives - years for financial "
            "records - and destruction at end of life is itself a "
            "trailed event. The trail's own integrity checks run on a "
            "schedule, not just at audit time, because a broken chain "
            "found early is an incident and found late is a scandal."
        ),
        "key_points": [
            "Every record event - creation, transition, correction, access - is trailed with who, what, when, before and after.",
            "Hash chaining makes tampering detectable: altering one entry breaks every later link.",
            "The trail is append-only across all write paths; corrections are new entries, never edits.",
            "External anchoring of periodic head hashes prevents rewriting history from the start.",
            "Chain integrity is verified on a schedule, not only at audit time.",
        ],
        "requirements": [
            "All write paths (application, batch, manual) must emit trail entries - no side doors.",
            "Each entry must hash-bind the previous entry's hash and its own timestamp.",
            "Trail storage must be append-only with access controls that block rewriting.",
            "Head hashes must be anchored externally on a documented schedule.",
            "Integrity verification must run on a schedule with alerts on any break.",
        ],
        "standards": [
            "Audit trail completeness follows standard financial internal-control practice.",
            "Hash algorithms used for chaining follow published cryptographic standards (for example SHA-256).",
            "Record retention periods follow applicable financial recordkeeping regulations.",
        ],
        "citations": [CIT_WEYGANDT, CIT_PCI],
        "sig_lens": (
            "The Signature read: the audit trail is the unbroken chain "
            "of witness - each link holding the fingerprint of the last, "
            "back to the first promise. The Signature Method seals every "
            "act into the chain, for a covenant without witnesses is "
            "only a story."
        ),
    },
    {
        "key": "fx",
        "name": "Multi-Currency Transactions and FX",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Money crosses borders carrying its currency with it, and "
            "somewhere the conversion happens - that somewhere is priced. "
            "A multi-currency transaction record names two amounts: the "
            "transaction currency amount (what the customer agreed to) "
            "and the settlement or billing currency amount (what actually "
            "moved), joined by the exchange rate and its timestamp. The "
            "rate has a source - a market feed, a network rate, a bank's "
            "board rate - and a spread: the difference between the buy "
            "and sell price that pays the converter. Dynamic currency "
            "conversion at the point of sale lets the traveler pay in "
            "home currency, but the merchant's rate usually loses to the "
            "card network's rate. Settlement between banks happens in an "
            "agreed currency, and the FX gain or loss between the trade "
            "date and the settlement date posts as its own balanced "
            "entry. Records must keep both amounts because each answers "
            "a different audit question: the customer asks about the "
            "first, the books about the second, and the spread is the "
            "difference."
        ),
        "how_it_works": (
            "FX works by rate plus spread plus timing. The transaction "
            "captures the rate at authorization time and stamps its "
            "source and timestamp; the authorized home-currency amount "
            "is computed in high precision and rounded once to the home "
            "currency's minor units. Between authorization and settlement "
            "the rate moves, so the settled amount differs from the "
            "authorized estimate - card networks disclose this as the "
            "exchange rate applied on the posting date. The merchant or "
            "bank books both: the receivable in transaction currency, "
            "the cash in settlement currency, and the FX difference to a "
            "gain/loss account, all balanced. Netting across many "
            "transactions in the same pair can use one blended rate, but "
            "the blended rate must be documented and applied "
            "consistently. Triangulation through a vehicle currency "
            "(often USD) is standard where no direct market exists, and "
            "each leg's rate is recorded so the chain is auditable."
        ),
        "key_points": [
            "Every FX record names both amounts, the rate, its source, and its timestamp.",
            "The spread between buy and sell rates is the converter's price - disclose it.",
            "Authorized and settled home-currency amounts differ when rates move between the two dates.",
            "FX gains and losses post as their own balanced double-entries.",
            "Blended or triangulated rates must be documented and applied consistently.",
        ],
        "requirements": [
            "FX records must carry transaction-currency amount, settlement-currency amount, rate, source, and timestamp.",
            "Conversion must compute in high precision and round once to the target currency's minor units.",
            "The rate source hierarchy (market feed, network rate, board rate) must be documented.",
            "FX gain/loss entries must post balanced to a dedicated account.",
            "Customer-facing amounts and book amounts must both be retained for audit.",
        ],
        "standards": [
            "Currency codes and minor units follow ISO 4217.",
            "Cross-border FX messaging follows SWIFT and ISO 20022 amount and rate conventions.",
            "FX translation in financial statements follows FASB ASC 830.",
        ],
        "citations": [CIT_ISO4217, CIT_SWIFT, CIT_WEYGANDT],
        "sig_lens": (
            "The Signature read: foreign exchange is the covenant "
            "translated - the same promise weighed in two coins. The "
            "Signature Method names both weighings, the scales used, and "
            "the toll of the translator, for a translated promise must "
            "still balance."
        ),
    },
    {
        "key": "ledger_design",
        "name": "Designing an Append-Only Transaction Ledger",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The transaction ledger is the database this whole database "
            "describes: the system of record for money movement. Its "
            "first design law is append-only - inserts only, no updates, "
            "no deletes - because the past is not editable and every "
            "correction is a new entry. Its second law is balance: every "
            "write commits a balanced set of debit and credit entries, "
            "enforced by constraints, so the trial balance is zero at "
            "every commit. Its third law is order: a monotonic sequence "
            "number on every entry makes replay deterministic - the same "
            "entries in the same order always yield the same balances. "
            "Derived state (account balances, pending totals) is cached "
            "from the journal and re-derivable, never the source of "
            "truth. Partitioning by time keeps writes fast and old data "
            "cheap; hash-chaining per partition makes tampering evident; "
            "idempotency keys on the write API make retries safe. A "
            "ledger designed this way is boring in the best sense: it "
            "does exactly one thing - remember, in order, forever."
        ),
        "how_it_works": (
            "The design works by separating the journal from everything "
            "else. The journal table holds one row per entry: sequence "
            "number, transaction ID, account, debit or credit, minor-unit "
            "amount, currency, timestamp, and lineage pointers. A check "
            "constraint or write-path validation guarantees each "
            "transaction's debits equal its credits before commit. "
            "Balance caches subscribe to the journal as an event stream: "
            "each committed entry updates the affected accounts' running "
            "totals, and a reconciliation job periodically replays the "
            "journal to verify the caches. Reads of current balance hit "
            "the cache; audits and disputes read the journal. Retention "
            "archives old partitions to cold storage with their hash "
            "chains intact, and retrieval re-verifies the chain on "
            "rehydration. Concurrency is handled by the sequence: writers "
            "take the next number atomically, so two simultaneous "
            "payments cannot interleave into ambiguity. Backups capture "
            "the journal plus the sequence counter - everything else can "
            "be rebuilt."
        ),
        "key_points": [
            "Append-only: inserts only; corrections are new entries, never edits.",
            "Every commit is balanced - debits equal credits - enforced by constraints on the write path.",
            "A monotonic sequence number makes replay deterministic and concurrency safe.",
            "Balances are derived caches; the journal is the source of truth and re-derivation verifies the caches.",
            "Partition by time, hash-chain per partition, idempotency keys on the write API.",
        ],
        "requirements": [
            "The journal schema must include sequence, transaction ID, account, direction, minor-unit amount, currency, timestamp, lineage.",
            "Balance enforcement (debits equal credits per transaction) must be a constraint, not a convention.",
            "Sequence numbers must be assigned atomically with no gaps in committed order.",
            "Balance caches must be re-derivable from the journal and verified on a schedule.",
            "Archives must retain hash chains and verify them on retrieval.",
        ],
        "standards": [
            "Journal design follows standard financial accounting control practice for completeness and immutability.",
            "Electronic record retention follows applicable financial recordkeeping regulations.",
            "Hash chaining follows published cryptographic practice for tamper evidence.",
        ],
        "citations": [CIT_WEYGANDT, CIT_RFC9110],
        "sig_lens": (
            "The Signature read: the ledger is the book of covenants - "
            "written once, in order, forever, every promise with its "
            "mirror. The Signature Method builds the book to outlive its "
            "keepers: the journal remembers what the clerks forget."
        ),
    },
    {
        "key": "reversals",
        "name": "Reversal Records and Compensating Transactions",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "When money must go back, the record does not rewind - it "
            "answers. A reversal record is a new, first-class transaction "
            "that undoes the economic effect of an earlier one while "
            "leaving the original intact: the refund answers the sale, "
            "the chargeback answers the capture, the ACH return answers "
            "the original entry, the compensating transfer answers the "
            "mistaken wire. The reversal carries the original's "
            "identifier in its lineage, an equal and opposite amount, "
            "its own timestamp and identifier, and a reason code. In "
            "double-entry terms it posts mirror-image entries, so the "
            "pair nets to zero while both remain visible - the audit "
            "trail shows the mistake and its correction, not a gap where "
            "the mistake was. Partial reversals undo part of the effect "
            "(the partial refund); full reversals undo all of it. The "
            "discipline is absolute: no edit, no delete, no backdating - "
            "the undo is always a new record, because history is the "
            "asset the ledger protects."
        ),
        "how_it_works": (
            "Reversals work through linked compensation. The system "
            "creates the reversal referencing the original identifier, "
            "validates that the reversible amount remains (settled minus "
            "already-reversed covers the new reversal), and posts the "
            "mirror entries atomically with the linkage. Netting is then "
            "arithmetic: original plus reversals equals the outstanding "
            "effect, and a fully reversed transaction nets to zero while "
            "remaining fully visible. Time matters: some rails allow "
            "same-day voids (no money moved, just release the hold), "
            "while next-day undos must travel as reversals through "
            "settlement (money moves back). Cross-system reversals need "
            "matching on both sides - the ACH return's trace number must "
            "match the originator's original entry, the chargeback's "
            "reference must match the merchant's sale. Unmatched "
            "reversals are breaks: money moved with no explained cause, "
            "and reconciliation flags them until the lineage is found or "
            "the investigation closes."
        ),
        "key_points": [
            "A reversal is a new record that undoes the effect; the original is never edited, deleted, or backdated.",
            "The reversal carries the original's identifier, an opposite amount, and a reason code.",
            "Mirror double-entries make the pair net to zero while both stay visible.",
            "Same-day undos may void (no money moved); later undos must travel as reversals through settlement.",
            "Unmatched reversals are reconciliation breaks: money moved with no explained cause.",
        ],
        "requirements": [
            "Reversal records must reference the original transaction identifier and state the reason.",
            "Reversible amount must be validated: settled minus already-reversed must cover the new reversal.",
            "Reversals must post balanced mirror entries atomically with the lineage link.",
            "Voids (pre-settlement) and reversals (post-settlement) must be distinct record types.",
            "Unmatched reversals must be flagged as breaks and investigated, never auto-cleared.",
        ],
        "standards": [
            "Card reversal and refund messaging follows ISO 8583 and network rules.",
            "ACH returns follow NACHA return reason codes and timeframes.",
            "Reversal accounting follows standard contra-entry practice in financial accounting.",
        ],
        "citations": [CIT_ISO8583, CIT_NACHA, CIT_WEYGANDT],
        "sig_lens": (
            "The Signature read: the reversal is the honorable unmaking "
            "- the covenant released by a second witnessed act, not "
            "erased. The Signature Method keeps both the making and the "
            "unmaking on the page, for a ledger that forgets its "
            "mistakes will repeat them."
        ),
    },
    {
        "key": "realtime_payments",
        "name": "Real-Time Payments: RTP and FedNow Records",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Real-time payments collapse the old timeline: authorization, "
            "clearing, and settlement happen in seconds, around the "
            "clock, every day of the year. The Clearing House's RTP "
            "network (operating since 2017) and the Federal Reserve's "
            "FedNow Service (launched July 2023) both move bank-to-bank "
            "credit transfers that settle in central-bank money within "
            "seconds of initiation - no batches, no next-day, no pending "
            "for days. The records reflect the compression: a single "
            "payment message (ISO 20022-based, pacs.008 family) carries "
            "the instruction and the settlement together, and the "
            "confirmation returns with finality - the money is there, "
            "irrevocably, before the sender's app finishes its animation. "
            "Request-for-payment flips the direction: the biller sends a "
            "payment request and the payer approves it, replacing the "
            "pull of a check or ACH debit with a push the payer "
            "controls. Amount caps apply (network limits per "
            "transaction), and because settlement is instant and final, "
            "there are no returns - errors are corrected by a new payment "
            "going the other way."
        ),
        "how_it_works": (
            "Real-time works by settling gross, immediately. The sending "
            "bank validates the instruction, checks funds and fraud "
            "signals, and submits the pacs.008-style message to the "
            "network; the network routes it to the receiving bank, which "
            "must accept or reject within seconds; on acceptance, the "
            "central settlement accounts debit and credit simultaneously "
            "and the confirmation flows back. Finality is instant: the "
            "receiving bank credits the beneficiary with good funds "
            "immediately, which is why fraud controls run pre-send - "
            "there is no recall window. Liquidity is managed continuously "
            "rather than per batch: banks fund their settlement accounts "
            "and monitor positions around the clock, since payments never "
            "sleep. Request-for-payment messages carry the biller's "
            "invoice data; the payer's approval converts the request "
            "into a standard instant payment. Records carry the "
            "network's transaction identifiers end to end, and because "
            "everything settles in seconds, the pending state barely "
            "exists - the lifecycle is essentially initiated, then "
            "settled or rejected."
        ),
        "key_points": [
            "Authorization, clearing, and settlement complete in seconds, 24/7/365 - no batches, no next-day.",
            "Settlement is gross and final in central-bank money; the beneficiary is credited with good funds immediately.",
            "Messages are ISO 20022-based (pacs.008 family) with end-to-end identifiers.",
            "Request-for-payment lets billers request and payers approve, replacing pull debits with payer-controlled pushes.",
            "No returns exist: errors are corrected by a new payment in the opposite direction.",
        ],
        "requirements": [
            "Payment records must carry the network transaction identifiers end to end.",
            "Receiving banks must accept or reject within the network's seconds-scale timeout.",
            "Fraud and funds checks must run pre-send, since there is no recall window after finality.",
            "Amount caps per transaction must be enforced at initiation.",
            "Liquidity positions must be monitored continuously given round-the-clock settlement.",
        ],
        "standards": [
            "RTP messages and rules follow The Clearing House RTP specifications.",
            "FedNow messages and operating procedures follow the Federal Reserve's published specifications.",
            "Both networks use ISO 20022 message grammar for payment instructions.",
        ],
        "citations": [CIT_RTP, CIT_FEDNOW, CIT_ISO20022],
        "sig_lens": (
            "The Signature read: real-time payment is the covenant kept "
            "at the speed of speech - promised and paid in one breath. "
            "The Signature Method treats instant finality with instant "
            "seriousness: check before you speak, for the word cannot be "
            "unsaid."
        ),
    },
    {
        "key": "lifecycle_capstone",
        "name": "The Full Transaction Lifecycle, End to End",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "This record walks one transaction through every station in "
            "this database, from intent to archive. A customer places an "
            "order for 500 dollars of goods: the order record freezes the "
            "line items and total (pending). The merchant authorizes the "
            "card for 500 dollars: the authorization record holds the "
            "funds (pending). The goods ship in two boxes: two partial "
            "captures, 300 and 200 dollars, each referencing the "
            "authorization (settling). Clearing computes interchange and "
            "the acquirer deposits the net (settled). The bank statement "
            "arrives: reconciliation matches the merchant's ledger "
            "against the processor's report - every line matched "
            "(verified). One box arrives damaged: the customer returns "
            "it, the RMA gates the return, inspection grades it, and a "
            "partial refund of 200 dollars posts, referencing the "
            "original payment (reversed in part). Every step wrote "
            "balanced double-entries; the trial balance reads zero; the "
            "audit trail hash-chains every event; and the net effect - "
            "300 dollars of kept sale, 200 refunded - is provable from "
            "the journal alone. That is the whole database in one story: "
            "anatomy, lifecycle, reconciliation, reversal, audit - the "
            "covenant spoken, kept, partly released, and forever "
            "remembered."
        ),
        "how_it_works": (
            "The end-to-end lifecycle works because every station speaks "
            "the same record language. The order's identifier flows into "
            "the authorization, the authorization code into the captures, "
            "the capture references into the clearing batch, the batch "
            "totals into the settlement report, the settlement lines "
            "into reconciliation, and the RMA and refund point back up "
            "the whole chain - one unbroken lineage from click to refund. "
            "Double-entry postings at each station keep the books "
            "balanced continuously: the 500-dollar sale, the fee entries, "
            "the settlement entries, and the 200-dollar refund's mirror "
            "entries all net correctly, leaving 300 dollars of revenue "
            "and zero suspense. State transitions are guarded at every "
            "step - no capture beyond authorization, no refund beyond "
            "settlement, no second settlement of one authorization - and "
            "idempotency keys make every retry safe. The audit trail "
            "records each transition with its actor and timestamp, hash-"
            "chained, so years later an auditor can replay the story and "
            "arrive at the same numbers. This is the machine the other "
            "thirty-three records describe, running."
        ),
        "key_points": [
            "One identifier lineage runs unbroken from order through authorization, captures, clearing, settlement, return, and refund.",
            "Balanced double-entries at every station keep the trial balance at zero continuously.",
            "Guarded state transitions block capture beyond authorization and refund beyond settlement.",
            "Idempotency keys make every retry safe across the whole lifecycle.",
            "The hash-chained audit trail lets an auditor replay the story years later and reach the same numbers.",
        ],
        "requirements": [
            "Every record in the chain must carry lineage pointers to its predecessor records.",
            "Each station must post balanced double-entries before the next station proceeds.",
            "State-machine guards must be enforced at every transition, not just documented.",
            "Idempotency keys must cover every mutating call in the chain.",
            "The complete chain must be replayable from the journal to re-derive all balances.",
        ],
        "standards": [
            "Order, payment, clearing, and reporting messages follow ISO 20022, ISO 8583, and NACHA as applicable per rail.",
            "Double-entry postings follow standard financial accounting practice.",
            "Audit trail practice follows financial internal-control standards with hash-chained tamper evidence.",
        ],
        "citations": [CIT_ISO20022, CIT_ISO8583, CIT_NACHA, CIT_WEYGANDT],
        "sig_lens": (
            "The Signature read: this is the covenant's whole life - "
            "spoken at the order, sealed at the capture, counted at the "
            "clearing, proven at the reconciliation, partly released at "
            "the refund, and remembered forever in the chain. The "
            "Signature Method's final lesson: a promise fully traced is "
            "a promise fully kept."
        ),
    },
])
