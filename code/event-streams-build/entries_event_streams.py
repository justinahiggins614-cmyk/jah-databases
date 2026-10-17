#!/usr/bin/env python3
"""Entries for The Event Streams Database and The Event Streams Signature
Database (missing-115 program, Wave 1 - operational data, item 48).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,390 databases),
prefix check of every id_prefix value, and a full grep of every shard
index in jah-databases-data-1 for '"id":"JAH-EVS': zero 'event-streams'
slugs/names; zero title collisions across all 68 titles (public plus
' (Signature Edition)' forms) checked through the whole-system dedupe
gate before authoring. The paste's rule was applied by name/purpose/record
schema/capabilities: a database of event sequences, timestamps,
processing state, and replay - event schemas, ordering and causality,
stream partitioning, exactly-once semantics, change-data-capture,
event-store design, snapshotting, consumer offsets, replay and
reprocessing - is a distinct capability, so BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  event-streams              - The Event Streams Database (public-harvest:
                               real, fact-checked event-stream engineering:
                               events, timestamps, logs, schemas, ordering
                               and causality, partitioning, delivery
                               semantics, CDC, outbox, event stores,
                               snapshots, offsets, event sourcing, stream
                               processing, schema evolution, replay,
                               observability, and recovery; standard
                               references Kleppmann Designing
                               Data-Intensive Applications 2017; Kreps The
                               Log 2013; Fowler Event Sourcing; Young on
                               event stores and CQRS; Helland Life Beyond
                               Distributed Transactions 2007; Lamport Time
                               Clocks and the Ordering of Events 1978;
                               Garcia-Molina and Salem Sagas 1987;
                               CloudEvents CNCF v1.0; Avro schema
                               resolution; and the other landmarks cited
                               per record)
  event-streams-signature    - The Event Streams Signature Database
                               (his original Signature Stream Method:
                               every event a signed testimony carrying
                               its lineage, the log the ledger of
                               testimony, the stream the river, replay
                               the return, src signature, titles suffixed
                               " (Signature Edition)", never presented
                               as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written
in ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-EVS- (public) and JAH-EVSS- (signature), verified free
in the manifest id_prefix values and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_event_streams.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos before the pages
are written.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Stream Method: "
            "every event a signed testimony carrying its lineage stamp, "
            "the log the ledger of testimony, the stream the river, replay "
            "the return, ordering the oath of sequence, partitioning the "
            "allotment, exactly-once the pledge of single delivery. Clearly "
            "labeled Signature-made, never presented as authentic public "
            "record.")

CIT_KLEPPMANN = ("Kleppmann M. Designing Data-Intensive Applications. "
                 "O'Reilly Media; 2017. (chapters 3, 5, 11: storage engines, "
                 "replication, stream processing)")
CIT_KREPS = ("Kreps J. The Log: What every software engineer should know "
             "about real-time data's unifying abstraction. LinkedIn "
             "Engineering blog; 2013.")
CIT_FOWLER_ES = ("Fowler M. Event Sourcing. martinfowler.com/bliki; 2005.")
CIT_FOWLER_CQRS = ("Fowler M. CQRS. martinfowler.com/bliki; 2011.")
CIT_YOUNG = ("Young G. Event Sourcing writings on event stores, expected "
             "version, and aggregate design; CQRS documents.")
CIT_HELLAND = ("Helland P. Life beyond Distributed Transactions: an "
               "Apostate's Opinion. CIDR; 2007.")
CIT_LAMPORT = ("Lamport L. Time, Clocks, and the Ordering of Events in a "
               "Distributed System. Communications of the ACM; 1978.")
CIT_SAGAS = ("Garcia-Molina H, Salem K. Sagas. ACM SIGMOD; 1987.")
CIT_CLOUDEVENTS = ("CloudEvents Specification. Cloud Native Computing "
                   "Foundation (CNCF); v1.0.")
CIT_AVRO = ("Apache Avro Specification 1.11: schema resolution rules for "
            "reader and writer schemas.")
CIT_PROTOBUF = ("Protocol Buffers documentation: field numbering and wire "
                "compatibility (as architecture knowledge; not an "
                "endorsement).")
CIT_KAFKA = ("Apache Kafka documentation: log design, transactions, and "
             "log compaction (as architecture knowledge; not an "
             "endorsement).")
CIT_ESDB = ("EventStoreDB documentation: streams, expected revision, "
            "projections (as architecture knowledge; not an endorsement).")
CIT_DEBEZIUM = ("Debezium documentation: change data capture connectors "
                "and the outbox event router (as architecture knowledge; "
                "not an endorsement).")
CIT_CONFLUENT_EOS = ("Confluent documentation: exactly-once semantics with "
                     "idempotent producers and transactions (as architecture "
                     "knowledge; not an endorsement).")
CIT_OTEL = ("OpenTelemetry Specification: trace context and W3C "
            "traceparent propagation for correlation.")
CIT_W3C_TRACE = ("W3C Trace Context recommendation: traceparent and "
                 "tracestate headers.")

ENTRIES = [
    # ------------------------------- Foundations (ranks 1-3)
    {
        "key": "what_is_event",
        "name": "What Is an Event",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "An event is an immutable record of something that has already "
            "happened: 'OrderPlaced at 14:02:11', 'TemperatureRead at "
            "09:00:00', 'PaymentAuthorized with amount 49.99'. The defining "
            "trait of an event is that it is a fact about the past - it "
            "cannot be edited or deleted, only superseded by a later event. "
            "Every event carries three things at minimum: an identity (a "
            "unique event id), a type (what kind of fact it is), and a "
            "timestamp (when it happened). Around that core, events carry a "
            "payload - the data of the fact, such as the order id, the "
            "temperature value, the customer id. Event-driven systems treat "
            "the event, not the current database row, as the primary truth: "
            "the row is a summary of the events so far, and the events are "
            "the history that produced it. This record frames the whole "
            "database: every later record is one shelf of the event-stream "
            "shelf, and every shelf teaches schemas, ordering, delivery, "
            "storage, and replay of events."
        ),
        "how_it_works": (
            "A producer observes a state change in the world - a sensor "
            "reading, a user click, a completed transaction - and emits an "
            "event record describing it. The record is serialized into bytes "
            "and appended to an ordered log under a stream name or topic, "
            "receiving a position (an offset or sequence number) that fixes "
            "its place in history. Consumers read the log from their last "
            "remembered position, apply each event to their own state, and "
            "advance their position. Because events are immutable, a new "
            "consumer can start at the beginning and rebuild the entire "
            "present from the past: replay is simply reading the same log "
            "again. Nothing about the event itself changes as it is read; "
            "only the consumers' interpretations move forward."
        ),
        "key_points": [
            "An event is an immutable fact about the past, carrying an id, a type, a timestamp, and a payload - it is written once and never edited.",
            "The event log is the primary truth; any current database row is a derived summary of the events that produced it.",
            "Events are ordered by position in the log (offset or sequence number), which is what makes replay deterministic.",
            "A producer emits events, a stream carries them in order, and consumers read them and maintain their own state.",
            "Because nothing in an event changes after writing, many different consumers can read the same history independently.",
        ],
        "requirements": [
            "A unique event id per event so duplicates can be detected downstream.",
            "A stable event type name so consumers can route and interpret the payload.",
            "An event timestamp recording when the fact happened, separate from when it was processed.",
            "A serialized payload whose structure is described by a schema.",
            "An append-only store that assigns each event a fixed position in the stream.",
        ],
        "standards": [
            "CloudEvents CNCF v1.0 - the standard envelope for event metadata (id, source, type, time).",
            "ISO 8601 - timestamp representation for event time.",
        ],
        "citations": [CIT_CLOUDEVENTS, CIT_KREPS],
        "sig_lens": (
            "His original Signature Stream Method treats every event as a "
            "signed testimony: it happened, it is written, and it carries "
            "its lineage stamp so the river of testimony can always be "
            "traced back to its source."
        ),
    },
    {
        "key": "commands_events_state",
        "name": "Commands, Events, and State",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Commands, events, and state are the three characters in every "
            "event-driven story, and confusing them is the most common "
            "beginner mistake. A command is a wish expressed in the present "
            "tense: 'PlaceOrder', 'ChargeCard'. It may fail - the card may "
            "be declined, the item may be out of stock - so a command is "
            "handled by exactly one receiver that decides. An event is a "
            "fact in the past tense: 'OrderPlaced', 'CardCharged'. It "
            "cannot fail or be un-happened; many receivers may observe it. "
            "State is the accumulated memory: the current balance, the "
            "order status, derived by folding all past events together. "
            "The pattern is always the same: commands arrive, decisions "
            "are made, events are recorded, state is derived. Keeping the "
            "three separate is what lets an event stream be replayed, "
            "audited, and rebuilt without re-deciding anything."
        ),
        "how_it_works": (
            "A command handler receives 'ChargeCard' and validates it "
            "against current state: is the card on file, is the amount "
            "positive, is the account in good standing. If validation "
            "fails, no event is written - the command is rejected and the "
            "failure itself may be recorded as its own event. If validation "
            "succeeds, the handler appends 'CardCharged' to the event log "
            "with the charge details. Downstream, any number of consumers "
            "observe 'CardCharged' and update their own state: the ledger "
            "adds the debit, the fraud monitor updates its risk score, the "
            "notification service queues a receipt. Current state is never "
            "written directly by consumers; it is always the fold of the "
            "events they have seen. Replay the commands' resulting events "
            "from the beginning and the same state reappears."
        ),
        "key_points": [
            "Commands are wishes in the present tense handled by one decider; events are facts in the past tense observed by many.",
            "Commands can fail and be rejected; events, once recorded, cannot be un-happened.",
            "State is always derived by folding past events together, never written directly by observers.",
            "Separating the three lets the log be replayed and audited without re-running any decisions.",
            "The flow is fixed: command arrives, decision is made, event is recorded, state is derived.",
        ],
        "requirements": [
            "Commands carry an intent and the data needed to validate it.",
            "Exactly one handler owns each command type and decides accept or reject.",
            "Every accepted command produces one or more immutable events.",
            "State is recomputed from events, so consumers must process events in order per stream.",
            "Rejected commands are reported without writing business events.",
        ],
        "standards": [
            "CQRS pattern literature (command/query responsibility segregation) for the command-side separation.",
        ],
        "citations": [CIT_FOWLER_CQRS, CIT_YOUNG],
        "sig_lens": (
            "The Signature Stream Method names them plainly: the command is "
            "the asking, the event the testimony that the asking was "
            "answered, and state the standing record built from testimony - "
            "asking and testimony never share a page."
        ),
    },
    {
        "key": "event_time_processing_time",
        "name": "Event Time Versus Processing Time",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Every event lives on two clocks at once. Event time is when "
            "the fact happened in the world: the sensor took the reading at "
            "09:00:00, the customer clicked at 14:02:11. Processing time is "
            "when the system got around to handling it: the reading arrived "
            "over a flaky radio link at 09:00:47, the click event sat in a "
            "queue until 14:02:13. The gap between the two clocks is the "
            "lateness of the event, and real systems are full of late "
            "events - retries, offline devices, batch uploads, clock skew. "
            "Stream processors that compute on processing time give fast "
            "but wrong answers when data arrives late; processors that "
            "compute on event time give right answers but must wait for "
            "latecomers. The whole discipline of watermarks, windows, and "
            "allowed lateness exists to reconcile these two clocks."
        ),
        "how_it_works": (
            "The producer stamps each event with event time from its own "
            "clock (or a trusted source clock) at the moment of capture. "
            "The event then travels: serialized, transmitted, queued, "
            "partitioned, and finally read by the processor, which notes "
            "the processing time on arrival. A stream engine groups events "
            "into windows by event time - 'all readings from 09:00 to "
            "09:05' - and uses watermarks, which are promises that 'all "
            "events with event time earlier than X have now arrived', to "
            "decide when a window is complete enough to emit a result. "
            "Events arriving after the watermark are late; the system "
            "either drops them, updates the result, or routes them "
            "elsewhere, according to its lateness policy. Choosing event "
            "time for correctness and processing time for speed is the "
            "central trade-off of stream processing."
        ),
        "key_points": [
            "Event time is when the fact happened; processing time is when the system handled it; the difference is lateness.",
            "Late events are normal: retries, offline devices, batch uploads, and clock skew all produce them.",
            "Computing on processing time is fast but wrong under lateness; computing on event time is right but must wait.",
            "Watermarks are the mechanism that declares event time complete enough to emit window results.",
            "Every stream design needs an explicit lateness policy: drop, update, or reroute late events.",
        ],
        "requirements": [
            "Producers stamp event time at capture from the best available clock.",
            "The pipeline carries event time through every hop without overwriting it.",
            "Windows are defined on event time, not arrival time.",
            "A watermark strategy declares when event time is considered complete.",
            "A documented policy handles events that arrive after the watermark.",
        ],
        "standards": [
            "ISO 8601 for timestamp interchange on both clocks.",
            "NTP (RFC 5905) as the usual basis for keeping producer clocks close enough.",
        ],
        "citations": [CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method keeps two ledgers on every "
            "testimony: the hour it happened and the hour it was heard, so "
            "late witnesses are marked late instead of being mistaken for "
            "present ones."
        ),
    },
    {
        "key": "append_only_log",
        "name": "The Append-Only Event Log",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The append-only log is the simplest durable structure in "
            "computing and the foundation of every event stream: new "
            "records are only ever added at the end, never modified in "
            "place, never deleted from the middle. Each appended event "
            "receives the next position number - offset 0, 1, 2, and so "
            "on - which fixes its order forever. Because writes only go to "
            "the tail, the log can accept enormous write rates; because "
            "reads are just 'give me everything after position N', many "
            "consumers can read the same log independently at their own "
            "pace. The log is also the system's memory: crash recovery is "
            "reading the log again, auditing is reading the log, and a new "
            "service joining the system catches up by reading the log from "
            "the beginning. Retention policies eventually trim the head, "
            "but while an event lives in the log its position and content "
            "are permanent."
        ),
        "how_it_works": (
            "The producer serializes an event and sends an append request "
            "to the log. The log writes the bytes sequentially to durable "
            "storage - disk, replicated across machines - and returns the "
            "assigned offset. Batches of appends are grouped for "
            "throughput, and the log's segments roll over to new files as "
            "they fill. A consumer keeps a single number: the offset of the "
            "last event it processed. To read, it asks for 'offset N+1 "
            "onward'; the log returns the next batch. If the consumer "
            "crashes, it restarts from its saved offset - no event is "
            "skipped, none is invented. Old segments whose events have all "
            "passed the retention horizon are deleted from the head, which "
            "is the only deletion the log ever performs."
        ),
        "key_points": [
            "Appends go only to the tail and each event gets a permanent position number (offset).",
            "Reads are 'everything after my last offset', so many consumers read the same log at their own pace.",
            "Crash recovery, auditing, and onboarding new services are all the same operation: reading the log.",
            "The only deletion is trimming old segments from the head under a retention policy.",
            "Sequential tail writes plus independent offset-based reads are why logs scale so well.",
        ],
        "requirements": [
            "Durable sequential storage for the tail with replication for fault tolerance.",
            "A monotonically increasing offset assigned atomically at append time.",
            "Segment files that roll over and can be read and trimmed independently.",
            "A retention policy defining how long offsets remain readable.",
            "Consumers that persist their own read positions outside the log.",
        ],
        "standards": [
            "Log-structured storage principles (as described in Kleppmann ch. 3).",
        ],
        "citations": [CIT_KREPS, CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method calls it the ledger of testimony: "
            "new lines only at the bottom, every line numbered in ink, no "
            "erasing - the river only flows forward."
        ),
    },
    {
        "key": "event_schemas",
        "name": "Event Schemas and Contracts",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "An event schema is the written contract between the producer "
            "who writes events and every consumer who reads them: it names "
            "each field, its type, and whether it must be present. Without "
            "a schema, the payload is a handshake deal - it works until "
            "someone renames a field, changes an integer to a string, or "
            "drops a field a downstream report depended on, and then "
            "production breaks at 2 a.m. With a schema, producers and "
            "consumers share one versioned definition, changes are reviewed "
            "against compatibility rules, and bad events are rejected at "
            "the door instead of poisoning a warehouse. The schema is also "
            "documentation: a new engineer reads the schema and knows "
            "exactly what 'OrderPlaced' promises to contain. In mature "
            "systems the schemas live in a registry where every version is "
            "kept, so an old consumer can still read today's stream."
        ),
        "how_it_works": (
            "The team writes the schema for 'OrderPlaced' in a schema "
            "language: fields like order_id (string, required), amount "
            "(decimal, required), coupon_code (string, optional), each with "
            "a fixed field number or name. The schema is registered under "
            "the event type with version 1. The producer serializes events "
            "using version 1 and stamps the version on the wire. The "
            "consumer fetches the same version 1 schema and deserializes. "
            "When the producer needs a new field, it registers version 2 "
            "following compatibility rules - new optional fields are safe, "
            "renaming a required field is not - and old consumers keep "
            "reading with version 1 while new consumers adopt version 2. "
            "A validator at the stream entrance can reject any event that "
            "fails its schema, so malformed facts never enter the log."
        ),
        "key_points": [
            "The schema is the contract: field names, types, and required-vs-optional, shared by producer and all consumers.",
            "Unversioned handshake payloads break silently; schemas break loudly at registration time instead.",
            "Compatibility rules decide which changes are safe: adding optional fields is safe, renaming required fields is not.",
            "A schema registry keeps every version so old consumers keep reading new streams.",
            "Entrance validation rejects malformed events before they can poison the log.",
        ],
        "requirements": [
            "Every event type has a written schema in a schema language.",
            "Schemas are versioned and stored where producers and consumers both reach them.",
            "Changes pass compatibility checks before deployment.",
            "Producers stamp the schema version on each event.",
            "Consumers declare which schema versions they can read.",
        ],
        "standards": [
            "Apache Avro schema resolution rules; Protocol Buffers field-numbering rules.",
            "JSON Schema (draft 2020-12) for JSON payloads.",
            "CloudEvents attribute naming for the standard envelope fields.",
        ],
        "citations": [CIT_AVRO, CIT_PROTOBUF, CIT_CLOUDEVENTS],
        "sig_lens": (
            "The Signature Stream Method treats the schema as the oath of "
            "shape: the testimony promises to arrive in an agreed form, "
            "and any testimony that breaks the oath is turned away at the "
            "riverbank."
        ),
    },
    {
        "key": "ordering_causality",
        "name": "Ordering, Causality, and Happened-Before",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "In a single log, order is obvious: offset 5 comes after offset "
            "4. Across distributed streams, order gets subtle, because two "
            "machines' clocks never agree exactly and messages arrive out "
            "of order. The key insight, from Lamport's 1978 paper, is that "
            "wall-clock time is the wrong tool: what matters is causality. "
            "Event A 'happened-before' event B if A could have caused B - "
            "for example, a request event happened-before the response it "
            "triggered. If neither could have caused the other, the two "
            "events are concurrent, and no honest system may claim one is "
            "'first'. Lamport clocks and vector clocks are mechanisms that "
            "capture this causal order without trusting any clock: they let "
            "a consumer know 'I have seen everything that could have "
            "influenced this event' before acting on it. Getting causality "
            "right is what keeps distributed state consistent."
        ),
        "how_it_works": (
            "Each process keeps a Lamport clock, a simple counter. Before "
            "sending an event it increments the counter and stamps the "
            "event with the value; on receiving an event it sets its "
            "counter to one more than the maximum of its own value and the "
            "received stamp. If event A carries stamp 3 and event B carries "
            "stamp 7, B did not happen-before A - though they might still "
            "be concurrent. Vector clocks go further: each process keeps "
            "one counter per process, so comparing two vectors reveals "
            "exactly whether A caused B, B caused A, or they are "
            "concurrent. Stream systems use these ideas in practice: "
            "partition keys keep causally related events in one ordered "
            "partition, and causation ids link each event to the event that "
            "triggered it, forming a causal chain a debugger can walk."
        ),
        "key_points": [
            "Causality, not wall-clock time, is the correct basis for ordering distributed events.",
            "Happened-before means A could have caused B; otherwise the events are concurrent and unordered.",
            "Lamport clocks give a consistent causal tick without trusting any machine clock.",
            "Vector clocks additionally detect concurrency exactly by tracking one counter per process.",
            "In practice: partition keys keep related events ordered, and causation ids chain each event to its trigger.",
        ],
        "requirements": [
            "Events that must stay ordered share a partition key or a single stream.",
            "Causally linked events carry causation ids pointing at their trigger.",
            "No component assumes cross-partition wall-clock order.",
            "Clock skew between producers is measured and bounded, never trusted blindly.",
            "Replay preserves the original causal order of the log.",
        ],
        "standards": [
            "Lamport 1978 happened-before relation as the reference model.",
            "W3C Trace Context for carrying causal trace linkage on the wire.",
        ],
        "citations": [CIT_LAMPORT, CIT_W3C_TRACE],
        "sig_lens": (
            "The Signature Stream Method records the chain of witness: "
            "every testimony names the testimony that summoned it, so the "
            "river keeps its true order - cause before consequence, always."
        ),
    },
    {
        "key": "partitioning",
        "name": "Stream Partitioning",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A single ordered log cannot absorb the write rate of a large "
            "system, so streams are partitioned: the log is split into "
            "many independent ordered sub-logs called partitions, and each "
            "event is assigned to one partition by a partition key. The "
            "contract is precise and powerful: events with the same key "
            "always land in the same partition and keep their order; "
            "events with different keys may land anywhere and have no "
            "order between them. Choose the key well - the order id for "
            "order events, the device id for sensor readings, the user id "
            "for user activity - and every consumer sees each entity's "
            "life story in perfect sequence. Choose it badly and one "
            "partition drowns while others sit idle (a hot partition), or "
            "related events scatter and lose their order. Partitioning is "
            "how event streams scale horizontally: more partitions, more "
            "parallel consumers, more throughput."
        ),
        "how_it_works": (
            "The producer hashes the partition key - say, order id "
            "'ORD-8812' - and takes the hash modulo the partition count to "
            "pick partition 7 of 24. The event is appended to partition "
            "7's log with that partition's next offset. A consumer group "
            "divides the 24 partitions among its members: consumer A reads "
            "partitions 0-7, consumer B reads 8-15, and so on, each "
            "tracking its own offsets. Because all events for 'ORD-8812' "
            "land in partition 7, consumer A sees that order's events in "
            "exact sequence: Placed, then Paid, then Shipped. If the team "
            "later grows to 48 partitions, the key-to-partition mapping "
            "changes and the stream must be rebalanced or re-keyed with "
            "care, since order only holds within a partition."
        ),
        "key_points": [
            "Partitioning splits one stream into many ordered sub-logs; the partition key decides placement.",
            "Same key means same partition means preserved order; different keys have no ordering between them.",
            "The key should be the entity id whose life story must stay sequential: order id, device id, user id.",
            "A hot partition - one key dominating traffic - starves the parallelism partitioning was meant to buy.",
            "Changing the partition count re-maps keys, so it must be planned like a migration, not a toggle.",
        ],
        "requirements": [
            "A partition key chosen from the entity whose ordering matters.",
            "A stable hash from key to partition that every producer computes identically.",
            "Enough partitions for the target parallelism, with headroom for growth.",
            "Monitoring of per-partition throughput to catch hot partitions early.",
            "A documented procedure for changing partition counts without scrambling order.",
        ],
        "standards": [
            "Consistent hashing principles for key-to-partition assignment.",
        ],
        "citations": [CIT_KAFKA, CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method calls it the allotment: each "
            "lineage is given its own channel of the river, and every "
            "testimony of that lineage flows down its own channel in true "
            "order."
        ),
    },
    {
        "key": "serialization",
        "name": "Serializing Events: Formats and Choices",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Events travel as bytes, and serialization is the translation "
            "between the in-memory event and those bytes. JSON is the "
            "human-readable default: self-describing, easy to debug, and "
            "universally supported, but verbose and schema-optional, which "
            "invites the handshake-deal breakage schemas prevent. Avro "
            "carries a schema with it and resolves differences between the "
            "writer's schema and the reader's schema by rule, making it the "
            "workhorse of schema-registry ecosystems. Protocol Buffers uses "
            "numbered fields for compact binary encoding and safe "
            "evolution: unknown fields are skipped, not errors. The choice "
            "shapes the system: JSON for debugging-friendly low-volume "
            "streams, Avro where a registry governs evolution, Protobuf "
            "where payload size and cross-language support dominate. Every "
            "format must answer the same questions: how are types encoded, "
            "how are missing fields handled, and what happens when reader "
            "and writer disagree."
        ),
        "how_it_works": (
            "The producer takes the event object, looks up the schema for "
            "its type and version, and encodes each field: strings as "
            "length-prefixed bytes, integers in the format's chosen "
            "representation, nested records recursively. With Avro, the "
            "writer's schema fingerprint travels with the payload; the "
            "consumer fetches both schemas and applies resolution rules - "
            "a field present in the writer but absent in the reader is "
            "dropped, a field with a declared default that the writer "
            "omitted is filled in. With Protobuf, each field's number is "
            "encoded on the wire, so a consumer that has never heard of "
            "field 7 simply skips those bytes and keeps reading. The "
            "deserialized object the consumer's code sees is then the "
            "event, ready for business logic."
        ),
        "key_points": [
            "Serialization translates events to bytes; the format choice shapes debugging, size, and evolution safety.",
            "JSON is readable and universal but verbose and schema-optional.",
            "Avro pairs payloads with schemas and resolves writer/reader differences by rule.",
            "Protocol Buffers uses numbered fields so unknown fields are skipped, not errors.",
            "Every format must define type encoding, missing-field handling, and reader/writer disagreement behavior.",
        ],
        "requirements": [
            "A chosen format per stream, documented with its schema language.",
            "Schema lookup available to both producer and consumer at runtime.",
            "Defaults declared for any field a newer writer might omit.",
            "Field identifiers (names or numbers) that are never reused for different meanings.",
            "A policy for undecodable payloads: quarantine, never silent drop.",
        ],
        "standards": [
            "Apache Avro Specification 1.11 (schema resolution).",
            "Protocol Buffers encoding documentation.",
            "JSON (RFC 8259) and JSON Schema (draft 2020-12) for JSON streams.",
            "CloudEvents bindings for each format (JSON, Avro, Protobuf).",
        ],
        "citations": [CIT_AVRO, CIT_PROTOBUF, CIT_CLOUDEVENTS],
        "sig_lens": (
            "The Signature Stream Method demands the testimony be written "
            "in a hand every reader can read: the encoding is part of the "
            "oath, and a testimony no reader can decode is a testimony "
            "lost."
        ),
    },
    {
        "key": "consumers_groups",
        "name": "Consumers and Consumer Groups",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A consumer is a process that reads events from a stream and "
            "does something with them: updates a database, sends an email, "
            "trains a model. A consumer group is the scaling mechanism: a "
            "set of consumer instances that split a stream's partitions "
            "among themselves so the work parallelizes. The group has one "
            "iron rule - each partition is read by exactly one member at a "
            "time - which guarantees that each event is processed once per "
            "group while letting many members share the load. When a "
            "member joins or crashes, the group rebalances: partitions are "
            "reassigned, each member resumes from its saved offsets, and "
            "processing continues. Different groups read the same stream "
            "independently - the billing group, the analytics group, and "
            "the search-index group each keep their own offsets and never "
            "interfere. The group is thus both a parallelism tool and an "
            "isolation boundary."
        ),
        "how_it_works": (
            "Three consumers join group 'billing' on a 12-partition "
            "stream. The group's coordinator assigns partitions 0-3 to "
            "consumer A, 4-7 to B, 8-11 to C. Each polls its partitions, "
            "processes events, and commits offsets back to the group's "
            "offset store. Consumer B crashes; the coordinator detects the "
            "missed heartbeat, triggers a rebalance, and reassigns "
            "partitions 4-7 to A and C, which resume from B's last "
            "committed offsets. Meanwhile group 'analytics' reads the same "
            "12 partitions with its own members and its own offsets, "
            "entirely unaffected. When a fourth billing consumer joins, "
            "partitions redistribute to three per member. The rebalance "
            "pauses processing briefly - the famous stop-the-world moment - "
            "which is why stable membership and incremental rebalancing "
            "matter at scale."
        ),
        "key_points": [
            "A consumer reads and acts; a consumer group parallelizes by splitting partitions among members.",
            "Each partition belongs to exactly one group member at a time: processed once per group, in order.",
            "Rebalancing reassigns partitions on join, leave, or crash, resuming from committed offsets.",
            "Different groups read the same stream independently with their own offsets.",
            "Rebalances pause processing, so stable membership keeps throughput smooth.",
        ],
        "requirements": [
            "A group id naming the shared work: one group per independent processing purpose.",
            "Partition assignment that each member honors exclusively.",
            "Heartbeat and failure detection so dead members release partitions promptly.",
            "An offset store scoped per group, durable across restarts.",
            "A rebalance strategy chosen for the workload: eager for simplicity, cooperative for smoothness.",
        ],
        "standards": [
            "Consumer-group protocol concepts as documented in Kafka design docs (as knowledge; not an endorsement).",
        ],
        "citations": [CIT_KAFKA, CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method calls the group a company of "
            "witnesses: each channel of the river is heard by exactly one "
            "witness at a time, and companies hear independently without "
            "disturbing one another."
        ),
    },
    {
        "key": "delivery_semantics",
        "name": "Delivery Semantics: At-Most, At-Least, Exactly-Once",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Delivery semantics answer one question: when a failure "
            "strikes mid-processing, what happens to the event? At-most-"
            "once means the event is processed zero or one times - fast "
            "and simple, but a crash loses events silently, fit only for "
            "metrics and samples where loss is acceptable. At-least-once "
            "means the event is processed one or more times: the consumer "
            "commits its offset only after processing, so a crash replays "
            "the last events and duplicates appear. Duplicates are safe "
            "only if processing is idempotent - doing it twice has the "
            "same effect as doing it once. Exactly-once means the event's "
            "effect happens precisely one time, which in distributed "
            "systems is achieved not by magic delivery but by making the "
            "whole pipeline idempotent or transactional: deduplicate by "
            "event id, or commit the offset and the output atomically. "
            "Choosing the semantics is choosing where the complexity "
            "lives: in accepted loss, in idempotent handlers, or in "
            "transactions."
        ),
        "how_it_works": (
            "Under at-least-once, the consumer reads events 100-109, "
            "updates its database, then commits offset 109. If it crashes "
            "after the database write but before the commit, it restarts "
            "at 100 and reprocesses - the database must tolerate the "
            "replay, e.g. by keying writes on the event id so the second "
            "write is a no-op. Under exactly-once with transactions, the "
            "consumer opens a transaction, processes the events, writes "
            "results, and commits the offsets all atomically: either every "
            "effect lands or none does, and a crash leaves no partial "
            "state. Under at-most-once, the consumer commits the offset "
            "before processing; a crash after the commit but before the "
            "work loses the events. The pattern is universal: the "
            "stronger the guarantee, the more coordination it costs."
        ),
        "key_points": [
            "At-most-once: zero or one processing; simple and fast but silently loses events on failure.",
            "At-least-once: one or more processings; safe only with idempotent handlers that tolerate duplicates.",
            "Exactly-once: the effect happens once, achieved via idempotency or atomic transactions, never by the network alone.",
            "The commit point - before or after processing - is what selects the semantics.",
            "Stronger guarantees cost more coordination; match the guarantee to what the business actually needs.",
        ],
        "requirements": [
            "A declared delivery semantic per consumer group, chosen deliberately.",
            "Idempotent handlers wherever at-least-once is used: key writes by event id.",
            "Offset commits positioned after successful processing for at-least-once.",
            "Transactional output plus offset commits for exactly-once pipelines.",
            "Monitoring that counts duplicates and losses so the real semantics are visible, not assumed.",
        ],
        "standards": [
            "Idempotency-key patterns (as in HTTP API design) applied to event handlers.",
        ],
        "citations": [CIT_KLEPPMANN, CIT_CONFLUENT_EOS],
        "sig_lens": (
            "The Signature Stream Method states the pledge plainly: every "
            "testimony shall be heard once - never lost, never double-"
            "counted - and the hearer proves it by the lineage stamps, not "
            "by promises."
        ),
    },
]

ENTRIES += [
    # ------------------------------- Compounded (ranks 4-7)
    {
        "key": "cdc",
        "name": "Change Data Capture (CDC)",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Change data capture turns a database's own change journal into "
            "an event stream: every insert, update, and delete committed to "
            "the database becomes an event that downstream systems can "
            "consume. The classic implementation reads the database's "
            "transaction log - the write-ahead log in Postgres, the binlog "
            "in MySQL - which the database already maintains for crash "
            "recovery, so CDC adds almost no load to the operational "
            "tables. Each captured change carries the before-image and "
            "after-image of the row, the transaction id, and the log "
            "position, giving consumers a complete ordered feed of "
            "everything the database did. CDC is the bridge between the "
            "request-response world and the event world: the application "
            "keeps writing to its familiar database, and the rest of the "
            "system learns about the writes as events - for search indexes, "
            "caches, warehouses, and audit trails that must track the "
            "operational data without polling it."
        ),
        "how_it_works": (
            "A CDC connector opens a replication slot on the Postgres "
            "primary and starts reading the write-ahead log from the last "
            "saved log sequence number. For each committed transaction it "
            "decodes the row changes into events: an update to the orders "
            "table becomes an event with the old row and the new row, the "
            "commit timestamp, and the LSN. The connector publishes each "
            "change event to the stream keyed by the row's primary key, so "
            "all changes to one row stay ordered in one partition. "
            "Consumers - a search indexer, a cache invalidator, a warehouse "
            "loader - read the stream and apply the changes to their own "
            "stores. If the connector restarts, it resumes from the saved "
            "LSN; no committed change is missed and none is invented. "
            "Schema changes to the source tables flow through as schema "
            "evolution on the change events."
        ),
        "key_points": [
            "CDC converts committed database changes into an ordered event stream by reading the transaction log.",
            "Reading the log adds almost no load to operational tables, unlike polling or triggers.",
            "Each change event carries before-image, after-image, transaction id, and log position.",
            "Keying change events by primary key keeps one row's history ordered in one partition.",
            "CDC bridges the request-response world and the event world without changing how applications write.",
        ],
        "requirements": [
            "A source database exposing its transaction log for replication.",
            "A connector that tracks its log position durably and resumes after restarts.",
            "Primary-key-based partitioning so each row's changes stay ordered.",
            "Handling of DDL/schema changes on source tables as event schema evolution.",
            "Monitoring of replication lag between the database commit and the published event.",
        ],
        "standards": [
            "Database replication protocol documentation (Postgres logical decoding, MySQL binlog) as the capture surface.",
        ],
        "citations": [CIT_DEBEZIUM, CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method treats the database journal as a "
            "witness that was already testifying: CDC simply opens the "
            "courtroom door so the testimony flows into the river instead "
            "of staying locked in the ledger room."
        ),
    },
    {
        "key": "outbox",
        "name": "The Outbox Pattern",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The outbox pattern solves the dual-write problem: when a "
            "service must update its database AND publish an event, doing "
            "the two as separate steps risks publishing without saving (a "
            "phantom event) or saving without publishing (a lost event). "
            "The outbox fixes this with one atomic transaction: the "
            "service writes its business row and, in the same transaction, "
            "inserts the event into an outbox table in the same database. "
            "Either both land or neither does - the database's own "
            "atomicity guarantees it. A relay process then reads new "
            "outbox rows and publishes them to the event stream, marking "
            "each as sent. Combined with change data capture on the outbox "
            "table, the relay becomes nearly free: the CDC connector "
            "notices the inserted outbox row and publishes it. The pattern "
            "gives exactly-once publication intent from the service's "
            "point of view, at the cost of one extra table and a relay."
        ),
        "how_it_works": (
            "The order service begins a database transaction, inserts the "
            "order row, and inserts an 'OrderPlaced' row into the outbox "
            "table with a unique event id and the serialized payload, then "
            "commits. The commit is atomic: the order and its event appear "
            "together or not at all. A CDC connector tails the outbox "
            "table's transaction log; each new outbox row becomes a "
            "published event on the stream, and the connector marks the "
            "row dispatched. If the relay crashes mid-publish, it replays "
            "from its last position - the event may publish twice, so "
            "consumers deduplicate on the event id. The service code never "
            "touches the message broker directly; it only writes to its "
            "own database, which keeps the service's failure modes simple "
            "and testable."
        ),
        "key_points": [
            "The outbox solves dual-write: business row and event are written in one atomic database transaction.",
            "Either both land or neither does, guaranteed by the database's own atomicity.",
            "A relay (often CDC on the outbox table) publishes outbox rows to the stream.",
            "The service never touches the broker directly, keeping its failure modes simple.",
            "Relay replays can duplicate publishes, so consumers deduplicate on the event id.",
        ],
        "requirements": [
            "An outbox table in the service's own database with event id, type, payload, and dispatch state.",
            "All business writes paired with their outbox insert inside one transaction.",
            "A relay process with a durable position in the outbox table.",
            "Unique event ids so duplicate publishes are detectable downstream.",
            "Retention and cleanup of dispatched outbox rows.",
        ],
        "standards": [
            "Transactional outbox as documented in microservices pattern literature (Richardson) and Debezium outbox router.",
        ],
        "citations": [CIT_DEBEZIUM, CIT_HELLAND],
        "sig_lens": (
            "The Signature Stream Method seals the testimony with the deed: "
            "the act and its record are written in one stroke of the pen, "
            "so no deed ever walks the world without its testimony beside "
            "it."
        ),
    },
    {
        "key": "event_store_design",
        "name": "Designing an Event Store",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "An event store is a database purpose-built for events: it "
            "stores immutable event records in named streams, assigns each "
            "a revision number within its stream, and enforces optimistic "
            "concurrency so two writers cannot silently overwrite each "
            "other's history. The core write contract is 'append to stream "
            "X, but only if its current revision is R' - the expected "
            "revision. If two processes both read revision 5 and both try "
            "to append, the first succeeds and the second gets a "
            "concurrency conflict instead of corrupting the story; the "
            "loser re-reads and retries. Streams are cheap and numerous - "
            "one per aggregate instance, like 'order-8812' - so each "
            "entity's history is its own ordered log. The store also keeps "
            "global ordering across streams for consumers that need the "
            "system-wide sequence, plus metadata, stream categories for "
            "querying families of streams, and idempotency on event ids so "
            "retried appends do not duplicate."
        ),
        "how_it_works": (
            "The service reads stream 'order-8812' and finds it at revision "
            "7. It validates the 'ShipOrder' command against the folded "
            "state, then appends 'OrderShipped' with expected revision 7. "
            "The store checks: current revision is 7, so it writes the "
            "event as revision 8 atomically and returns success. A "
            "concurrent writer that also read revision 7 now tries to "
            "append 'OrderCancelled' with expected revision 7; the store "
            "sees the stream is at 8 and rejects with a concurrency "
            "conflict. The loser re-reads (now seeing 'OrderShipped' at 8), "
            "re-validates its command against the new state, and either "
            "retries with expected revision 8 or rejects the command as "
            "now-invalid. Readers fetch a stream by name and revision "
            "range, or subscribe to the global feed for cross-stream "
            "consumers."
        ),
        "key_points": [
            "An event store keeps immutable events in named streams with per-stream revision numbers.",
            "The expected-revision write contract gives optimistic concurrency: conflicting appends fail loudly instead of corrupting history.",
            "Streams are cheap and numerous - typically one per aggregate instance.",
            "A global ordering across streams serves consumers that need the system-wide sequence.",
            "Event-id idempotency makes retried appends safe against duplication.",
        ],
        "requirements": [
            "Named streams with atomic per-stream revision assignment.",
            "Expected-revision checks on every append, rejecting stale writers.",
            "A global position or sequence across all streams for system-wide consumers.",
            "Stream categories or naming conventions for querying families of streams.",
            "Retention, archival, and snapshot support so old streams stay readable and cheap.",
        ],
        "standards": [
            "EventStoreDB stream, revision, and expected-version concepts (as architecture knowledge; not an endorsement).",
        ],
        "citations": [CIT_ESDB, CIT_YOUNG],
        "sig_lens": (
            "The Signature Stream Method builds the archive as a hall of "
            "scrolls: each lineage its own scroll, each line numbered, and "
            "no hand may add a line except atop the last true line it has "
            "read."
        ),
    },
    {
        "key": "snapshotting",
        "name": "Snapshotting Aggregates",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Rebuilding an aggregate by replaying its entire stream works "
            "beautifully until the stream grows to a hundred thousand "
            "events and every command waits on a full replay. A snapshot "
            "is a saved copy of the aggregate's state at a particular "
            "revision - a photograph of the story so far. Loading becomes "
            "fast: read the latest snapshot, then replay only the events "
            "after it. Snapshots are a pure performance optimization, not "
            "a second source of truth: the events remain authoritative, "
            "and a snapshot can always be discarded and rebuilt from the "
            "log. The strategy questions are when to snapshot (every N "
            "events, every T minutes, or when load latency demands it) and "
            "where to keep snapshots (a fast key-value store beside the "
            "event store). Done right, snapshots make long-lived aggregates "
            "feel instant; done wrong - snapshots treated as truth, or "
            "taken inconsistently - they become a corruption vector."
        ),
        "how_it_works": (
            "Stream 'account-4471' holds 12,000 events. The snapshotter "
            "runs nightly: it loads the last snapshot (state at revision "
            "11,500), replays events 11,501-12,000 through the fold "
            "function, and writes the resulting state tagged with revision "
            "12,000 into the snapshot store. When a 'Withdraw' command "
            "arrives, the service fetches the snapshot at 12,000, replays "
            "only the 14 events appended since, validates the command "
            "against the fresh state, and appends event 12,015 with "
            "expected revision 12,014. If a snapshot is ever suspect, it "
            "is deleted and the next load replays from event 0 - slower "
            "once, correct always. Snapshot writes are idempotent and "
            "versioned by revision so concurrent snapshotters cannot "
            "regress state."
        ),
        "key_points": [
            "A snapshot is a saved aggregate state at a revision; loading reads the snapshot then replays only newer events.",
            "Snapshots are a performance optimization, never a second source of truth - the events stay authoritative.",
            "A corrupt or stale snapshot is fixed by deleting it and replaying from the log.",
            "Snapshot strategy: every N events, every T minutes, or driven by measured load latency.",
            "Snapshot writes must be idempotent and revision-tagged so concurrent snapshotters cannot regress state.",
        ],
        "requirements": [
            "A deterministic fold function so replay from any snapshot converges to the same state.",
            "Revision-tagged snapshots stored beside, not inside, the event store.",
            "A snapshot cadence tied to stream length and load-latency budgets.",
            "Snapshot reads that always verify the snapshot revision before replaying the tail.",
            "A tested 'delete snapshot and rebuild' path for corruption recovery.",
        ],
        "standards": [
            "Event sourcing snapshot practices as described by Young and Fowler (as knowledge).",
        ],
        "citations": [CIT_YOUNG, CIT_FOWLER_ES],
        "sig_lens": (
            "The Signature Stream Method takes a portrait of the witness at "
            "milestones: the portrait speeds the telling, but the scroll "
            "of testimony remains the true record - a portrait may be "
            "repainted from the scroll at any time."
        ),
    },
    {
        "key": "consumer_offsets",
        "name": "Consumer Offsets and Seek",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A consumer offset is a consumer group's memory of where it "
            "stopped reading: 'billing group has processed partition 7 up "
            "to offset 4,112'. Offsets are the difference between a stream "
            "processor and a forgetful script - they make consumption "
            "resumable, and their management decides the system's delivery "
            "semantics. Commit the offset before processing and a crash "
            "loses events (at-most-once); commit after processing and a "
            "crash replays them (at-least-once); commit the offset in the "
            "same transaction as the output and the effect lands "
            "exactly-once. Offsets live in a durable store - often a "
            "compacted internal topic - keyed by group, stream, and "
            "partition. Seek is the operator's superpower: deliberately "
            "moving a group's offsets backward to reprocess history (a bug "
            "fix replay) or forward to skip poisoned stretches, always as "
            "an explicit, audited action."
        ),
        "how_it_works": (
            "The billing consumer processes events 4,100-4,112 from "
            "partition 7, writes the invoice updates, then commits offset "
            "4,112 to the offset store. On restart it asks the store for "
            "its offsets and resumes at 4,113. When engineers discover a "
            "pricing bug that corrupted invoices for the last two days, "
            "they stop the group, seek its offsets back to the position of "
            "two days ago, deploy the fixed code, and restart: the group "
            "reprocesses the window with corrected logic, overwriting the "
            "bad invoices idempotently. Lag monitoring compares the "
            "committed offset against each partition's newest offset; a "
            "growing gap pages the on-call engineer. All of this works "
            "because the offset is just a number, and numbers can be "
            "saved, compared, and moved."
        ),
        "key_points": [
            "Offsets are a group's durable memory of its read position, per stream and partition.",
            "Commit timing selects delivery semantics: before processing (at-most-once), after (at-least-once), transactional with output (exactly-once).",
            "Offsets live in a durable store keyed by group, stream, and partition.",
            "Seek deliberately moves offsets for replays or skips, always as an explicit audited action.",
            "Lag is the gap between committed offset and the partition tip - the primary health metric of consumption.",
        ],
        "requirements": [
            "A durable offset store with atomic commits per group and partition.",
            "Commit placement matched to the declared delivery semantic.",
            "Seek tooling restricted to operators with audit logging of every seek.",
            "Lag dashboards alerting on growing commit-to-tip gaps.",
            "Offset retention longer than the longest planned replay window.",
        ],
        "standards": [
            "Offset management concepts as implemented in Kafka consumer groups (as knowledge; not an endorsement).",
        ],
        "citations": [CIT_KAFKA, CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method gives each company of witnesses a "
            "bookmark in the scroll: where the reading stopped is written "
            "down, and moving the bookmark is a deliberate act, witnessed "
            "and recorded."
        ),
    },
    {
        "key": "event_sourcing",
        "name": "Event Sourcing Fundamentals",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Event sourcing is the decision to store the history instead "
            "of the present: an aggregate's state is never saved directly; "
            "only the events that produced it are stored, and current "
            "state is rebuilt by replaying them. A bank account is not a "
            "row with a balance column - it is the stream 'account-4471' "
            "holding Opened, Deposited, Withdrew events, with the balance "
            "computed by folding them. The payoff is total auditability "
            "(every state change is a named fact with a timestamp), "
            "temporal queries ('what was the balance on March 3rd?'), and "
            "bug recovery (fix the fold logic, replay, and the corrected "
            "past appears). The price is discipline: all state changes "
            "must go through events, the fold must be deterministic, and "
            "queries need read models (projections) because folding a "
            "million events per page view is not a plan. Event sourcing "
            "shines for domains where history matters - finance, orders, "
            "audit-heavy systems - and is overkill where only the present "
            "counts."
        ),
        "how_it_works": (
            "To open an account, the service appends 'AccountOpened' with "
            "the owner and opening deposit to a new stream. To withdraw, "
            "it loads the stream's events (or snapshot plus tail), folds "
            "them into the current balance, validates that the balance "
            "covers the withdrawal, and appends 'Withdrew' with expected "
            "revision. The balance itself is never stored as a column "
            "anywhere authoritative. A new regulatory report needs 'daily "
            "closing balances for 2025': instead of a migration, the team "
            "writes a projector that replays every account stream, "
            "computes the balance at each midnight boundary, and fills the "
            "report table - history answering a question nobody asked when "
            "the events were written. When the fold logic had a rounding "
            "bug, fixing it and replaying corrected every derived balance "
            "without touching the stored events."
        ),
        "key_points": [
            "Event sourcing stores the history (events), never the present; state is rebuilt by replay.",
            "The payoff: total auditability, temporal queries, and bug recovery by fixing the fold and replaying.",
            "The price: every state change must go through events, and the fold must be deterministic.",
            "Read models (projections) serve queries so page views never fold a million events.",
            "It shines where history matters - finance, orders, audit-heavy domains - and is overkill elsewhere.",
        ],
        "requirements": [
            "All state changes expressed as events appended to per-aggregate streams.",
            "A deterministic fold function from event sequence to state.",
            "Optimistic concurrency via expected revision on appends.",
            "Projections maintained for query serving.",
            "Snapshots for long streams so command latency stays bounded.",
        ],
        "standards": [
            "Event sourcing pattern as described by Fowler (2005) and Young.",
        ],
        "citations": [CIT_FOWLER_ES, CIT_YOUNG, CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method keeps the whole life story, not "
            "just the latest portrait: any question about the past is "
            "answered by walking the scroll again, and the scroll itself "
            "is never rewritten."
        ),
    },
    {
        "key": "stateful_stream_processing",
        "name": "Stateful Stream Processing",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Stateless processing treats each event alone - filter, map, "
            "forward. Stateful stream processing remembers: it keeps "
            "per-key state across events, which is what makes counting, "
            "sessionizing, joining, and fraud detection possible. The "
            "engine partitions state by key alongside the stream's "
            "partitions, so the counter for user-991 lives with user-991's "
            "events, and it checkpoints that state durably so a crash "
            "resumes without losing counts. The hard parts are all about "
            "the state: keeping it consistent with the offsets (so a "
            "replay neither double-counts nor loses), bounding its size "
            "(state that grows forever eventually dies), and handling late "
            "events that arrive after their window's state was emitted. "
            "Modern engines back state with embedded stores and replicate "
            "checkpoints, turning 'remember across events' from a bespoke "
            "database problem into a library call."
        ),
        "how_it_works": (
            "A fraud detector keeps per-card state: the running count and "
            "sum of transactions in the last hour. Each 'CardCharged' "
            "event routes by card id to the partition holding that card's "
            "state; the processor updates the count and sum, and if the "
            "velocity exceeds the threshold it emits a 'SuspiciousVelocity' "
            "alert event. Every few seconds the engine checkpoints: it "
            "writes the state deltas and the input offsets atomically to "
            "durable storage. On crash, it restores the last checkpoint "
            "and replays the input from the checkpointed offsets - the "
            "state and the position move forward together, which is what "
            "keeps the counts exactly-once. Old state - cards idle for 30 "
            "days - is expired by a TTL so the state store stays bounded."
        ),
        "key_points": [
            "Stateful processing remembers per-key state across events, enabling counts, sessions, joins, and detection.",
            "State is partitioned by key with the stream and checkpointed durably for crash recovery.",
            "Checkpoints must advance state and input offsets atomically to keep exactly-once counts.",
            "State needs bounds: TTLs and expiration, or it grows until it dies.",
            "Late events force a policy: update emitted results, or accept that the state has moved on.",
        ],
        "requirements": [
            "Key-partitioned state colocated with the key's stream partition.",
            "Atomic checkpoints coupling state snapshots with input offsets.",
            "State TTL and expiration policies sized to the workload.",
            "A late-event policy for state already emitted.",
            "State backends with replication so a lost node does not lose the counts.",
        ],
        "standards": [
            "Stream processing state semantics as described in Kleppmann ch. 11.",
        ],
        "citations": [CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method lets the witness keep a tally "
            "stick: each lineage has its own stick, the notches are "
            "counted as testimony flows, and the stick is copied to safety "
            "before the river rises."
        ),
    },
    {
        "key": "windows",
        "name": "Windows Over Event Time",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "An unbounded stream never ends, so computations need windows: "
            "bounded slices of event time over which to aggregate. Tumbling "
            "windows chop time into non-overlapping fixed chunks - every "
            "5 minutes - good for periodic rollups. Hopping (sliding) "
            "windows overlap - every 5 minutes of events computed every "
            "minute - good for moving averages. Session windows group by "
            "activity with gaps: a user's clicks belong to one session "
            "until 30 idle minutes pass, then a new session begins. Global "
            "windows with triggers handle the unbounded case explicitly. "
            "Every window type answers two questions: which events belong "
            "together, and when is the result emitted. Watermarks declare "
            "event-time completeness, triggers fire early or late results, "
            "and allowed lateness decides how long a window stays open for "
            "stragglers. Choosing the window is choosing what 'recent' "
            "means for the business."
        ),
        "how_it_works": (
            "A metrics pipeline uses 5-minute tumbling windows on event "
            "time to count API errors. Events with event time 09:00:00-"
            "09:04:59 fall in the 09:00 window. The watermark advances past "
            "09:05:00 once all partitions report event time beyond it; the "
            "engine then emits the 09:00 count. A dashboard also wants a "
            "moving picture, so a second query uses hopping windows: 5-"
            "minute windows evaluated every minute, each event counted in "
            "five windows. For user behavior, session windows group clicks "
            "with gaps under 30 minutes; when no click arrives for 30 "
            "minutes the session closes and its summary emits. An event "
            "arriving 12 minutes late for an already-emitted window is "
            "handled by the lateness policy: update the count and re-emit, "
            "or route to a late-data stream."
        ),
        "key_points": [
            "Windows bound unbounded streams into computable slices of event time.",
            "Tumbling windows are fixed non-overlapping chunks; hopping windows overlap for moving views; session windows follow activity gaps.",
            "Watermarks declare when a window's event time is complete enough to emit.",
            "Triggers and allowed lateness control early, on-time, and late emissions.",
            "The window type defines what 'recent' means - it is a business decision, not just a technical one.",
        ],
        "requirements": [
            "Event-time timestamps on every event entering windowed computation.",
            "A window type matched to the question: tumbling for rollups, hopping for moving views, sessions for behavior.",
            "Watermark strategy per stream reflecting its real lateness distribution.",
            "An explicit lateness policy: update-and-re-emit, or route late data aside.",
            "Window state bounds so high-cardinality keys cannot exhaust memory.",
        ],
        "standards": [
            "Windowing semantics as formalized in the Dataflow model (Akidau et al.) and Kleppmann ch. 11.",
        ],
        "citations": [CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method gathers testimony by the hour-"
            "glass: each turning of the glass is counted separately, the "
            "late witness is marked late, and the count is spoken when the "
            "glass is judged empty."
        ),
    },
    {
        "key": "pubsub_eda",
        "name": "Pub-Sub and Event-Driven Architecture",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "In publish-subscribe, producers publish events to named topics "
            "without knowing who reads them, and consumers subscribe to "
            "topics without knowing who wrote them. This mutual ignorance "
            "is the architecture's superpower: the order service publishes "
            "'OrderPlaced' and has no idea that billing, warehouse, "
            "analytics, fraud, and notifications all react - adding a "
            "sixth consumer means deploying the consumer, not touching the "
            "producer. Event-driven architecture builds whole systems this "
            "way: services communicate through the stream, each owning its "
            "data and reacting to others' events, which removes the "
            "temporal coupling of synchronous calls (no cascading "
            "timeouts). The trade-offs are real: eventual consistency "
            "replaces immediate answers, debugging crosses service "
            "boundaries, and the stream becomes critical infrastructure. "
            "Done well, the system grows by adding subscribers; done "
            "poorly, it becomes a distributed ball of mud where nobody "
            "knows who reacts to what."
        ),
        "how_it_works": (
            "The checkout service publishes 'OrderPlaced' to the orders "
            "topic and returns success to the customer immediately. The "
            "warehouse service, subscribed to orders, reserves inventory; "
            "the billing service charges the card; the notification "
            "service sends the confirmation email; the analytics service "
            "updates its dashboards. Each works at its own pace from its "
            "own offsets - if notifications are down for an hour, the "
            "events wait in the topic and send when it recovers, while "
            "checkout never noticed. When the business adds a loyalty "
            "service, it subscribes to the same topic and starts earning "
            "points from the live stream plus a replay of history - zero "
            "changes to checkout. A schema registry and an event catalog "
            "keep the mutual ignorance disciplined: producers promise "
            "contracts, consumers depend on contracts, never on each "
            "other's code."
        ),
        "key_points": [
            "Pub-sub decouples producers from consumers: neither knows the other, only the topic contract.",
            "New consumers attach without touching producers, so the system grows by subscription.",
            "Removing synchronous calls removes temporal coupling and cascading timeouts.",
            "The costs are eventual consistency, cross-boundary debugging, and the stream as critical infrastructure.",
            "Discipline comes from the event catalog: contracts are shared, implementations stay private.",
        ],
        "requirements": [
            "Named topics with documented ownership and schema contracts.",
            "Producers that never depend on any specific consumer's presence or speed.",
            "Consumers that tolerate replays and out-of-order arrival within their design.",
            "An event catalog recording who publishes and who subscribes to what.",
            "Monitoring of per-topic publish rates and per-group lag as first-class signals.",
        ],
        "standards": [
            "CloudEvents for portable event envelopes across pub-sub systems.",
            "AsyncAPI for documenting event-driven interfaces.",
        ],
        "citations": [CIT_CLOUDEVENTS, CIT_KREPS],
        "sig_lens": (
            "The Signature Stream Method proclaims testimony in the square: "
            "the herald does not know who listens, the listeners do not "
            "know the herald - all share only the oath of the message, and "
            "the square grows by listeners."
        ),
    },
    {
        "key": "schema_evolution",
        "name": "Schema Evolution",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Event schemas change because businesses change: a new "
            "required field appears, a type widens, a field splits in two. "
            "Schema evolution is the discipline of changing schemas without "
            "breaking running consumers. The compatibility rules are the "
            "law: backward compatible changes let new producers talk to "
            "old consumers (add optional fields, never remove required "
            "ones); forward compatible changes let old producers talk to "
            "new consumers (new consumers must tolerate missing fields); "
            "full compatibility allows both directions. A schema registry "
            "enforces the rules at registration time, rejecting a version "
            "2 that renames a required field before it ever reaches "
            "production. Strategies for hard changes include versioned "
            "event types ('OrderPlacedV2'), upcasting (transforming old "
            "events to the new shape on read), and dual-publish during "
            "migration. Evolution done lazily - handshake JSON with no "
            "checks - is how 2 a.m. pages are born."
        ),
        "how_it_works": (
            "The team needs 'currency' on 'PaymentAuthorized'. They "
            "register schema version 2 adding an optional 'currency' field "
            "with default 'USD': backward compatible, so old consumers "
            "keep reading. Producers deploy and start stamping v2; the "
            "registry's compatibility check passed at registration. Old "
            "consumers use their v1 reader schema and the Avro resolution "
            "rules drop the unknown field. Months later the team wants to "
            "rename 'amount' to 'amount_cents' - a breaking change. They "
            "instead publish a new event type 'PaymentAuthorizedV2' to a "
            "new topic, run both in parallel, migrate consumers one by "
            "one, and retire v1 after the last consumer confirms. For "
            "stored history, an upcaster transforms v1 bytes to the v2 "
            "shape when old streams are replayed, so one code path reads "
            "all of history."
        ),
        "key_points": [
            "Compatibility rules are the law: backward (new producer, old consumer), forward (old producer, new consumer), full (both).",
            "The registry enforces compatibility at registration time, before production ever sees the change.",
            "Safe changes add optional fields with defaults; renames and type changes are breaking.",
            "Hard changes use versioned event types, dual-publish migration, or upcasting on read.",
            "Unmanaged handshake evolution is the leading cause of 2 a.m. event-pipeline pages.",
        ],
        "requirements": [
            "A schema registry that checks compatibility on every new version.",
            "Defaults on every newly added field.",
            "A breaking-change playbook: versioned types, dual-publish, migration checklist.",
            "Upcasters for replaying old history through new code.",
            "Consumer version inventory so retirements wait for the last reader.",
        ],
        "standards": [
            "Apache Avro schema resolution; Protobuf field-numbering rules; JSON Schema versioning guidance.",
        ],
        "citations": [CIT_AVRO, CIT_PROTOBUF],
        "sig_lens": (
            "The Signature Stream Method lets the oath of shape grow but "
            "never break its word: new promises are added beside the old, "
            "old readers keep their understanding, and no testimony is "
            "rewritten to fit a new mold."
        ),
    },
    {
        "key": "correlation_ids",
        "name": "Correlation and Causation IDs",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "One user action fans out into dozens of events across many "
            "services: the click becomes 'CartCheckedOut', which becomes "
            "'PaymentAuthorized', 'InventoryReserved', 'EmailQueued', each "
            "in different streams. Without linkage, debugging is archaeology "
            "- grepping timestamps and hoping. Correlation ids fix this: a "
            "single id generated at the entry point travels on every event "
            "the action causes, so one query - 'show me everything with "
            "correlation 7f3a' - reconstructs the whole distributed story. "
            "Causation ids go one level deeper: each event names its direct "
            "parent ('PaymentAuthorized' was caused by 'CartCheckedOut' "
            "event 8812), forming a causal tree. Together they give "
            "observability across the event-driven system: the correlation "
            "id for the forest, the causation id for the branches. They "
            "cost almost nothing - two string fields on the envelope - and "
            "pay for themselves the first time production misbehaves."
        ),
        "how_it_works": (
            "The API gateway generates correlation id 'corr-7f3a9c' for an "
            "incoming checkout and puts it on the 'CheckoutStarted' event "
            "along with its own event id 'evt-100'. The payment service "
            "reads it, and its 'PaymentAuthorized' event carries "
            "correlation 'corr-7f3a9c' and causation 'evt-100'. The "
            "warehouse's 'InventoryReserved' carries the same correlation "
            "and causation pointing at its own trigger. Weeks later a "
            "customer reports a missing confirmation email; support "
            "queries the event store for correlation 'corr-7f3a9c' and sees "
            "the full chain - checkout, payment, inventory, and the email "
            "event stuck behind a failed template render. The causation "
            "chain shows exactly which step's output fed the failure. "
            "Distributed tracing systems propagate the same ids "
            "automatically as W3C trace context."
        ),
        "key_points": [
            "Correlation ids link every event caused by one entry-point action across all services.",
            "Causation ids name each event's direct parent, forming a causal tree for precise debugging.",
            "One correlation query reconstructs the whole distributed story without timestamp archaeology.",
            "Both ride on the event envelope as cheap string fields, set once at the entry point and propagated.",
            "They are the foundation of observability in event-driven systems, pairing with distributed tracing.",
        ],
        "requirements": [
            "Correlation id generated at the system entry point for every inbound action.",
            "Propagation of the correlation id through every derived event, with no service dropping it.",
            "Causation id set to the triggering event's id on every emitted event.",
            "Indexing of both ids in the event store for fast lookup.",
            "Alignment with W3C trace context where distributed tracing is used.",
        ],
        "standards": [
            "W3C Trace Context (traceparent/tracestate) for propagation.",
            "OpenTelemetry semantic conventions for messaging spans.",
            "CloudEvents extension attributes for correlation carriage.",
        ],
        "citations": [CIT_W3C_TRACE, CIT_OTEL, CIT_CLOUDEVENTS],
        "sig_lens": (
            "The Signature Stream Method brands every testimony of one "
            "asking with one mark, and each testimony names its parent: "
            "the whole lineage can be gathered by its mark and walked "
            "branch by branch."
        ),
    },
    {
        "key": "projections",
        "name": "Projections and Read Models",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Event streams are superb at writing history and terrible at "
            "answering 'show me page 3 of open orders sorted by total' - "
            "folding millions of events per query is not a plan. A "
            "projection is a read model built by consuming events and "
            "maintaining query-friendly state: a table of open orders, a "
            "search index, a dashboard cache. The write side stays pure "
            "events; the read side is whatever shape the queries need, and "
            "there can be many projections over the same stream, each "
            "optimized for its questions. Projections are disposable by "
            "design: drop one, replay the stream, and it rebuilds - which "
            "also makes them the fix for bugs (correct the projector, "
            "replay) and the path to new features (a question nobody asked "
            "before gets its own projection over old history). This "
            "separation of write model and read models is the 'Q' in CQRS, "
            "and it is what lets event-sourced systems serve fast queries."
        ),
        "how_it_works": (
            "An 'orders-read' projector subscribes to the orders stream "
            "from the beginning. For 'OrderPlaced' it inserts a row in the "
            "open_orders table; for 'OrderShipped' it moves the row to "
            "shipped_orders; for 'OrderCancelled' it deletes it. The web "
            "API serves 'list open orders' from open_orders with a plain "
            "indexed query - milliseconds, no event folding. When product "
            "asks for 'orders by coupon code', the team writes a second "
            "projector maintaining orders_by_coupon, replays history into "
            "it, and ships the feature without touching the write side. "
            "When a projector bug double-counted cancelled orders, the fix "
            "was: correct the code, truncate the table, replay - the "
            "stream's immutability made the read model fully rebuildable."
        ),
        "key_points": [
            "Projections turn event history into query-friendly read models: tables, indexes, caches.",
            "The write side stays pure events; each read side is shaped for its own questions.",
            "Many projections can serve many query patterns from one stream.",
            "Projections are disposable: drop, replay, rebuild - which fixes bugs and enables new features over old history.",
            "This write/read separation is CQRS, and it is how event-sourced systems stay fast at query time.",
        ],
        "requirements": [
            "Projectors that are deterministic functions of the event stream.",
            "Read stores with the indexes the queries actually need.",
            "Replay tooling that rebuilds any projection from scratch.",
            "Monitoring of projection lag: a stale read model is a wrong answer served fast.",
            "Idempotent projector handlers so replays converge.",
        ],
        "standards": [
            "CQRS read-model practices (Fowler 2011; Young).",
        ],
        "citations": [CIT_FOWLER_CQRS, CIT_YOUNG],
        "sig_lens": (
            "The Signature Stream Method keeps the scroll untouched and "
            "paints many portraits from it: each portrait answers its own "
            "questions, and any portrait may be repainted from the scroll "
            "when the questions change."
        ),
    },
    {
        "key": "replay_reprocessing",
        "name": "Replaying and Reprocessing Events",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Replay is the superpower that justifies the whole event-"
            "stream architecture: because history is immutable and ordered, "
            "any consumer can re-read it. The uses are everyday, not "
            "exotic: fix a bug in the projector and replay to rebuild the "
            "read model correctly; onboard a new service by replaying "
            "history so it starts with full state; backfill a warehouse "
            "after adding a column; re-run fraud scoring with a new model "
            "over last year's events; test a new consumer against the real "
            "past before it touches production. Reprocessing is replay "
            "with a purpose - usually re-running a transformation with "
            "corrected logic. The discipline is in the controls: replays "
            "must be idempotent (re-running writes the same result), scoped "
            "(a time range, a stream, a partition - not 'everything, "
            "hopefully'), and announced (downstream owners know a re-"
            "processing wave is coming). Replay without idempotency is how "
            "you double-charge customers."
        ),
        "how_it_works": (
            "The analytics team finds that the revenue projector "
            "miscounted refunds for six weeks. They stop the projector, "
            "note the stream's current tip offset, deploy the fixed "
            "projector code to a fresh table, and start it with its "
            "offsets seeked to six weeks ago. It reprocesses the window, "
            "writing corrected rows idempotently (keyed by event id, so a "
            "replayed event overwrites rather than duplicates). They "
            "validate the rebuilt table against spot checks, then swap the "
            "API to the new table and retire the old. For the new loyalty "
            "service, onboarding is simpler: start its consumer group at "
            "offset 0 with the current code and let it catch up to the "
            "tip, then flip it live. Both operations reuse the same "
            "primitive - seek and re-read - with different scopes and "
            "announcements."
        ),
        "key_points": [
            "Replay re-reads immutable history; reprocessing re-runs logic over it, usually with corrected code.",
            "Everyday uses: fixing projectors, onboarding services, backfills, re-scoring, pre-production testing.",
            "Replays must be idempotent, scoped (time range/stream/partition), and announced to downstream owners.",
            "Seek plus re-read is the single primitive behind onboarding, bug-fix rebuilds, and backfills.",
            "Replay without idempotency duplicates effects - that is how customers get double-charged.",
        ],
        "requirements": [
            "Retention long enough to cover the oldest replay anyone will need.",
            "Idempotent sinks keyed by event id for every reprocessable consumer.",
            "Seek tooling with scoping (range, stream, partition) and audit logging.",
            "A replay runbook: announce, isolate (fresh tables), validate, swap, retire.",
            "Lag and progress tracking during long replays so operators see completion.",
        ],
        "standards": [
            "Offset seek and replay practices from stream-platform operations guides.",
        ],
        "citations": [CIT_KAFKA, CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method calls it the return: the witness "
            "may walk the scroll again from any mark, and the retelling "
            "must match the first telling line for line - idempotent as a "
            "mirror."
        ),
    },
    {
        "key": "dead_letters",
        "name": "Dead Letters and Poison Events",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A poison event is one a consumer cannot process no matter how "
            "many times it retries: a malformed payload, a schema it "
            "cannot resolve, a business rule that throws on unexpected "
            "data. Without a plan, the poison event blocks its partition "
            "forever - the consumer retries, fails, retries, and the whole "
            "stream stalls behind one bad record. The dead-letter pattern "
            "is the plan: after N failed attempts, the consumer publishes "
            "the offending event - with the error, the stack trace, the "
            "attempt count, and the original bytes - to a dead-letter topic "
            "or table, commits past it, and keeps processing. The poison is "
            "quarantined, not lost: operators inspect dead letters, fix "
            "the data or the code, and replay the corrected events. Dead-"
            "letter queues need the same operational care as main streams - "
            "alerts on growth, retention, and a replay path - or they "
            "become a second, unmonitored failure."
        ),
        "how_it_works": (
            "The notification consumer reads event 9,041, tries to render "
            "the email template, and throws: the payload's 'locale' field "
            "holds an unexpected value. It retries with backoff - attempts "
            "1, 2, 3 - and still throws. On the fourth failure it writes "
            "the event plus error context to the dead-letter topic keyed "
            "by the original partition, commits offset 9,041, and continues "
            "with 9,042. An alert fires: dead-letter depth is 1. An "
            "operator inspects, sees the new locale value, updates the "
            "template mapping, and triggers a replay of the dead-letter "
            "topic through the fixed consumer, which now processes the "
            "event and sends the email. The main stream never stalled; the "
            "bad event got a second chance after the fix."
        ),
        "key_points": [
            "A poison event fails every retry; without quarantine it blocks its partition forever.",
            "Dead-lettering moves the event aside with full error context after N attempts, then processing continues.",
            "The poison is quarantined, not lost: inspect, fix data or code, replay the corrected event.",
            "The dead-letter store needs alerts, retention, and a replay path like any production stream.",
            "Retry budgets must be bounded - infinite retry is just a slower stall.",
        ],
        "requirements": [
            "A bounded retry policy with backoff per consumer.",
            "A dead-letter destination capturing original bytes, error, attempts, and source position.",
            "Commit-past semantics so one poison event never blocks its partition.",
            "Alerts on dead-letter growth rate and age of oldest unprocessed letter.",
            "A tested replay path from dead-letter back through the fixed consumer.",
        ],
        "standards": [
            "Dead-letter queue practices from enterprise integration patterns (Hohpe/Woolf).",
        ],
        "citations": [CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method sets the bitter testimony aside "
            "in its own jar, labeled with why it choked the witness: the "
            "river flows on, and the jar waits for a wiser hearing."
        ),
    },
    {
        "key": "watermarks",
        "name": "Watermarks and Late Data",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A watermark is a stream processor's best guess at event-time "
            "completeness: 'I believe I have now seen all events with "
            "event time earlier than 09:05:00.' It is a guess because "
            "networks delay and devices go offline - but it is the guess "
            "that lets windows close and results emit instead of waiting "
            "forever. Watermarks advance as new events arrive carrying "
            "newer event times; the common heuristic holds the watermark a "
            "fixed lateness bound behind the maximum observed event time "
            "(e.g. 5 minutes), which absorbs ordinary jitter. Events "
            "arriving with event time behind the watermark are late, and "
            "the system's lateness policy decides their fate: update the "
            "emitted window result, send them to a side output for "
            "separate handling, or drop them with a counter. Idle "
            "partitions complicate watermarks - a silent partition holds "
            "the global watermark back - so production systems add idle "
            "detection or per-partition watermarks. Tuning the lateness "
            "bound is tuning the correctness-latency trade-off itself."
        ),
        "how_it_works": (
            "The pipeline tracks the maximum event time seen: 09:12:00, "
            "with a lateness bound of 5 minutes, so the watermark stands "
            "at 09:07:00. The 09:00-09:05 tumbling window, fully behind "
            "the watermark, emits its count of 1,842 events. Then a "
            "sensor's buffered batch arrives: 40 events with event time "
            "09:03:12 - late. The lateness policy says 'update': the "
            "engine amends the window state to 1,882 and emits a corrected "
            "result flagged as a late update. Meanwhile partition 3 has "
            "gone silent; after 10 minutes of no events the idle detector "
            "marks it idle so it stops pinning the watermark, and the "
            "watermark resumes advancing on the live partitions. Operators "
            "watch two metrics: watermark lag (how far behind real time) "
            "and the late-event rate (how often the bound is wrong)."
        ),
        "key_points": [
            "A watermark asserts event-time completeness: all events earlier than X are believed seen.",
            "The usual heuristic holds the watermark a lateness bound behind the maximum observed event time.",
            "Late events (event time behind the watermark) follow the lateness policy: update, side-output, or drop.",
            "Idle partitions pin the global watermark; idle detection keeps one silent source from freezing results.",
            "The lateness bound is the correctness-latency trade-off made concrete and tunable.",
        ],
        "requirements": [
            "Event-time timestamps on all events feeding windowed computation.",
            "A lateness bound chosen from measured arrival-delay distributions, not guesses.",
            "Idle-partition detection so silent sources do not freeze watermarks.",
            "A lateness policy implemented and monitored: updates, side outputs, or drops with counters.",
            "Dashboards for watermark lag and late-event rate per stream.",
        ],
        "standards": [
            "Watermark semantics from the Dataflow model (Akidau et al., 2015).",
        ],
        "citations": [CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method posts a watchman at the river: he "
            "calls when he judges the hour's testimony complete, marks the "
            "late witnesses late, and never lets one silent channel hold "
            "the whole river waiting."
        ),
    },
    {
        "key": "routing_filtering",
        "name": "Event Routing and Filtering",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Not every consumer wants every event, and routing is how the "
            "right events reach the right readers without everyone "
            "drinking from the firehose. The simplest routing is by topic "
            "or stream name: orders go here, payments go there. Content-"
            "based routing goes finer: a router inspects event attributes - "
            "type, region, amount - and forwards matching events to "
            "different destinations, like sending high-value orders to a "
            "priority topic. Filtering is routing's quieter sibling: "
            "consumers subscribe with predicates ('only OrderPlaced from "
            "region EU') so the events they never wanted never arrive. "
            "Brokers increasingly push filtering server-side so unwanted "
            "events never cross the network. The design tension is between "
            "coarse topics (simple, but consumers filter client-side and "
            "waste bandwidth) and fine topics (precise, but topic sprawl "
            "becomes its own operations burden). A good routing design "
            "mirrors the organization's real consumption boundaries."
        ),
        "how_it_works": (
            "The router subscribes to the raw 'payments' topic. Its rules: "
            "events with amount over 10,000 go to 'payments.priority'; "
            "events with type 'PaymentFailed' go to 'payments.failures' "
            "for the fraud team; everything else continues to "
            "'payments.standard'. The fraud consumer subscribes only to "
            "'payments.failures' and never sees a successful payment. A "
            "regional analytics consumer uses a subscription filter "
            "'region = EU' on the orders topic, so the broker drops non-EU "
            "events before they cross the Atlantic link. When the business "
            "adds a VIP tier, operators add one routing rule - no producer "
            "changes, no consumer redeploys. The router itself is a "
            "stateless stream processor, so it scales horizontally and "
            "restarts cleanly from its offsets."
        ),
        "key_points": [
            "Routing directs events to destinations by topic, attributes, or content rules.",
            "Content-based routing inspects event attributes to split one stream into specialized ones.",
            "Filtering (often server-side) keeps unwanted events from ever reaching or crossing to the consumer.",
            "Coarse topics waste bandwidth on client-side filtering; fine topics risk operational sprawl.",
            "Good routing mirrors real consumption boundaries and changes without producer redeploys.",
        ],
        "requirements": [
            "Routing rules expressed as data (config), not buried in producer code.",
            "Subscription filters supported by the broker or the routing layer.",
            "Monitoring of per-route volumes to catch misrouted floods.",
            "A rule-change process with dry-run evaluation against live traffic samples.",
            "Dead-letter handling for events matching no route.",
        ],
        "standards": [
            "CloudEvents attribute-based filtering; AsyncAPI channel bindings.",
            "Enterprise integration patterns: content-based router, message filter (Hohpe/Woolf).",
        ],
        "citations": [CIT_CLOUDEVENTS],
        "sig_lens": (
            "The Signature Stream Method stations ferrymen at the forks of "
            "the river: each testimony is read for its marks and poled to "
            "the channel whose witnesses await it, and none are ferried "
            "where no witness waits."
        ),
    },
]

ENTRIES += [
    # ------------------------------- Advanced (ranks 8-10)
    {
        "key": "sagas",
        "name": "Sagas: Distributed Transactions Without Two-Phase Commit",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A business transaction that spans services - book the flight, "
            "reserve the hotel, charge the card - cannot use a database "
            "transaction, because no single database owns all three. "
            "Two-phase commit across services is theoretically possible "
            "and operationally dreaded: it couples availability to the "
            "slowest participant. The saga pattern, from Garcia-Molina "
            "and Salem (1987), replaces the atomic transaction with a "
            "sequence of local transactions, each publishing an event that "
            "triggers the next, plus compensating actions that undo "
            "completed steps if a later step fails. Book flight (event), "
            "reserve hotel (event), charge card (fails) - then run "
            "compensations: release the hotel, cancel the flight. "
            "Choreography lets each service react to events independently; "
            "orchestration puts one saga conductor in charge of the "
            "sequence. Either way the system accepts a truth atomic "
            "transactions hide: between steps, the world is temporarily "
            "inconsistent, and compensations - not rollbacks - restore "
            "order."
        ),
        "how_it_works": (
            "The trip-booking orchestrator starts a saga with id "
            "'saga-551'. Step 1: it sends 'ReserveFlight' to the airline "
            "service, which books locally and publishes 'FlightReserved'. "
            "Step 2: on seeing it, the orchestrator sends 'ReserveHotel'; "
            "the hotel service publishes 'HotelReserved'. Step 3: the "
            "payment service is asked to charge, but the card is declined "
            "and it publishes 'PaymentFailed'. The orchestrator now runs "
            "compensations in reverse: it sends 'ReleaseHotel' (the hotel "
            "service frees the room and publishes 'HotelReleased'), then "
            "'CancelFlight'. Each service's local work was a real database "
            "transaction; the saga's atomicity is the guarantee that "
            "either all steps complete or all completed steps are "
            "compensated. Every step and compensation is an event, so the "
            "saga's full history is auditable and replayable."
        ),
        "key_points": [
            "Sagas replace cross-service atomic transactions with sequences of local transactions plus compensating actions.",
            "Each local step publishes an event triggering the next; a failure triggers compensations in reverse order.",
            "Choreography distributes the sequence logic; orchestration centralizes it in a saga conductor.",
            "The system temporarily lives with inconsistency between steps - compensations, not rollbacks, restore order.",
            "Every step and compensation is an event, making the saga auditable and replayable.",
        ],
        "requirements": [
            "Each saga step implemented as a local transaction publishing its outcome event.",
            "A compensating action designed for every step that has visible effects.",
            "Idempotent step and compensation handlers, since events may redeliver.",
            "A saga id (correlation id) carried on every step and compensation event.",
            "Monitoring for stuck sagas: steps started but neither completed nor compensated.",
        ],
        "standards": [
            "Garcia-Molina H, Salem K. Sagas. ACM SIGMOD; 1987.",
            "Saga orchestration vs choreography as documented in microservices pattern literature.",
        ],
        "citations": [CIT_SAGAS, CIT_HELLAND],
        "sig_lens": (
            "The Signature Stream Method walks a long road in short "
            "legible strides: each stride is sealed as testimony, and if "
            "the road ends, the walker retraces each stride in reverse, "
            "unsealing as he goes, until the road is as if never walked."
        ),
    },
    {
        "key": "eos_end_to_end",
        "name": "End-to-End Exactly-Once Processing",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Exactly-once sounds like a delivery promise, but the network "
            "cannot promise it - the achievement is making the effect "
            "happen once even though delivery may repeat. End-to-end "
            "exactly-once spans read, process, and write: the consumer "
            "reads events, computes results, writes results to an output "
            "stream or store, and advances its offsets, with all of it "
            "atomic. Two architectures deliver this. Transactional "
            "pipelines commit the output writes and the offset commits in "
            "one transaction, so a crash leaves either everything or "
            "nothing - the classic Kafka transactions design. Idempotent "
            "pipelines accept at-least-once delivery and make every write "
            "idempotent, keyed by event id, so replays converge instead of "
            "duplicating. The transactional path costs coordination and "
            "throughput; the idempotent path costs careful key design and "
            "works only where the sink supports conditional or keyed "
            "writes. Most production 'exactly-once' is the idempotent "
            "kind, because it composes with any sink."
        ),
        "how_it_works": (
            "In the transactional design, the stream processor opens a "
            "transaction, reads events 500-509, computes per-key counts, "
            "writes the counts to the output topic and the consumed offsets "
            "to the offset topic, then commits - atomically. A crash "
            "before commit leaves no trace: on restart the processor "
            "re-reads 500-509 and recomputes. In the idempotent design, "
            "the processor reads the same events, computes counts, and "
            "writes each count with a key of (window, key, event-id-range) "
            "using the sink's upsert; a replayed batch overwrites identical "
            "values instead of adding duplicates. Both designs share one "
            "non-negotiable: the processing function itself must be "
            "deterministic, because non-determinism (random ids, wall-clock "
            "reads) makes replays diverge even when delivery is perfect."
        ),
        "key_points": [
            "Exactly-once is an effect guarantee achieved despite at-least-once delivery, never a network promise.",
            "Transactional pipelines commit output writes and offset commits atomically.",
            "Idempotent pipelines accept replays and make every sink write converge via event-id keying.",
            "The transactional path costs coordination; the idempotent path costs careful key design.",
            "The processing function must be deterministic, or replays diverge regardless of delivery.",
        ],
        "requirements": [
            "A chosen strategy per pipeline: transactional or idempotent, documented and tested.",
            "For transactional: a sink participating in the transaction protocol.",
            "For idempotent: sink writes keyed by event id with upsert/conditional semantics.",
            "Deterministic processing: no wall-clock reads or randomness inside the transform.",
            "Chaos testing that kills processors mid-batch and verifies converged, unduplicated output.",
        ],
        "standards": [
            "Kafka transactions and idempotent producer design (as knowledge; not an endorsement).",
        ],
        "citations": [CIT_CONFLUENT_EOS, CIT_KAFKA, CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method seals the pledge with two wax "
            "stamps: either the testimony, its telling, and the bookmark "
            "are sealed together in one pressing, or every telling is "
            "stamped with the testimony's own mark so retellings merge "
            "into one."
        ),
    },
    {
        "key": "compaction_retention",
        "name": "Compaction, Retention, and Archiving",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Streams grow forever, but disks do not, so every stream "
            "needs a policy for what happens to old events. Retention by "
            "time ('keep 30 days') or by size ('keep 500 GB') deletes the "
            "head of the log when the limit passes - simple, and right "
            "for telemetry and clickstreams where old data loses value. "
            "Log compaction is the subtler tool: for streams keyed by "
            "entity, it keeps only the latest event per key and discards "
            "superseded ones, so the log becomes the current snapshot of "
            "every entity - perfect for 'latest profile per user' or "
            "'current config per device'. Archiving moves old segments to "
            "cheap object storage instead of deleting them, preserving "
            "history for compliance and future replays at the cost of "
            "slower access. The three compose: compact the hot log, "
            "archive segments before deletion, retain archives per policy. "
            "Getting this wrong means either infinite storage bills or "
            "discovering - during an audit - that the history you needed "
            "was trimmed last quarter."
        ),
        "how_it_works": (
            "The 'user-profiles' topic is compacted and keyed by user id. "
            "Over a week, user-991 emits ProfileUpdated five times; the "
            "compactor retains only the fifth - the latest truth - plus "
            "tombstones (deletion markers) that remove keys. A new "
            "consumer starting at offset 0 reads one event per user: the "
            "current profile, not the week's edit history. The 'clicks' "
            "topic instead uses 30-day retention: segments older than 30 "
            "days are copied to archival object storage, then deleted "
            "from the hot log. When regulators ask for last year's "
            "clicks, the archive is restored to a replay topic. Operators "
            "monitor the compacted topic's 'bloat ratio' (how much "
            "superseded data awaits the next compaction pass) and the "
            "archive restore drill runs quarterly."
        ),
        "key_points": [
            "Retention deletes the log head by time or size; right for data whose value decays.",
            "Compaction keeps the latest event per key, turning the log into the current snapshot of every entity.",
            "Tombstones are deletion markers that compaction honors to remove keys.",
            "Archiving moves old segments to cheap storage for compliance and future replays.",
            "The policies compose: compact hot, archive before delete, retain archives per policy.",
        ],
        "requirements": [
            "A per-topic policy: retention limits, compaction on/off, archival destination.",
            "Keyed events with stable keys on any compacted topic.",
            "Tombstone handling so deletions propagate instead of resurrecting.",
            "Archive restore drills proving old history is actually recoverable.",
            "Storage and bloat monitoring so growth never surprises the budget or the auditors.",
        ],
        "standards": [
            "Log compaction semantics as documented in Kafka log design (as knowledge; not an endorsement).",
        ],
        "citations": [CIT_KAFKA, CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method tends the archive like a "
            "librarian: the living scrolls stay at hand, superseded lines "
            "are pressed into their final form, and the old scrolls rest "
            "in the vault - never burned, always retrievable."
        ),
    },
    {
        "key": "governance_registry",
        "name": "Event Governance and the Schema Registry",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "When hundreds of teams publish thousands of event types, "
            "anarchy scales faster than throughput. Event governance is "
            "the operating system for that scale: naming conventions "
            "(PastTense verb phrases, domain prefixes), ownership (every "
            "event type has a team that answers for it), a catalog "
            "recording who publishes what and who subscribes, "
            "compatibility enforcement, and lifecycle rules for "
            "deprecating event types. The schema registry is governance's "
            "engine room: it stores every schema version, checks "
            "compatibility on registration, and serves schemas to "
            "producers and consumers at runtime. Governance also covers "
            "the envelope - required metadata like event id, timestamps, "
            "correlation ids, and data classification - so cross-cutting "
            "concerns (PII handling, audit) work uniformly. The goal is "
            "not bureaucracy but safe autonomy: teams move fast because "
            "the contracts, not meetings, coordinate them."
        ),
        "how_it_works": (
            "A team designing 'PaymentAuthorized' opens the catalog and "
            "finds the payments domain's conventions: types are "
            "PastTense, prefixed 'payments.', owned by the payments team, "
            "envelope must carry event id, event time, correlation id, and "
            "a data-classification tag. They draft the schema and submit "
            "it; the registry checks compatibility against version 1 and "
            "rejects a renamed required field with a precise error. They "
            "fix it, version 2 registers, and the catalog records the new "
            "version plus its subscribers. A quarterly governance report "
            "lists event types with no owner, schemas unused for a year "
            "(deprecation candidates), and producers publishing unregistered "
            "types (blocked at the gateway). When the payments team "
            "deprecates v1, the catalog shows exactly which consumers "
            "still read it, and the retirement waits for the last one."
        ),
        "key_points": [
            "Governance is the operating system for event scale: naming, ownership, catalog, compatibility, lifecycle.",
            "The schema registry stores versions, enforces compatibility at registration, and serves schemas at runtime.",
            "Envelope standards (ids, timestamps, correlation, classification) make cross-cutting concerns uniform.",
            "The catalog maps publishers to subscribers, which is what makes safe deprecation possible.",
            "Good governance buys safe autonomy: contracts coordinate teams so meetings do not have to.",
        ],
        "requirements": [
            "Published naming conventions and envelope requirements for all event types.",
            "A named owner team for every event type, recorded in the catalog.",
            "A registry enforcing compatibility before any schema version goes live.",
            "A deprecation lifecycle: announce, migrate, verify zero readers, retire.",
            "Gateway or CI checks blocking unregistered or unowned event types from production.",
        ],
        "standards": [
            "CloudEvents envelope; AsyncAPI for interface docs; Avro/Protobuf compatibility rules.",
        ],
        "citations": [CIT_CLOUDEVENTS, CIT_AVRO],
        "sig_lens": (
            "The Signature Stream Method keeps a book of oaths beside the "
            "river: every testimony's form is sworn and recorded, every "
            "scribe is named, and no oath is retired until its last "
            "reader has turned the page."
        ),
    },
    {
        "key": "observability_lag",
        "name": "Observing Event Streams: Lag, Metrics, and Alerts",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "You cannot operate what you cannot see, and event streams "
            "fail in ways request-response systems do not: a consumer "
            "that falls behind, a partition with a hot key, a watermark "
            "that stops advancing, a dead-letter queue filling silently. "
            "Consumer lag - the gap between a group's committed offset "
            "and the partition tip, in events or in time - is the single "
            "most important metric: growing lag means the system is "
            "losing the race against its own input. Around it sits a "
            "constellation: publish rate and error rate per topic, "
            "per-partition throughput (for hot-key detection), watermark "
            "lag, end-to-end latency from event time to processed time, "
            "dead-letter depth and age, schema-registry rejection counts, "
            "and rebalance frequency. Alerts must distinguish the "
            "urgent (lag growing unboundedly) from the informational "
            "(a brief rebalance spike). Good observability also traces "
            "single events: given an event id, show its journey across "
            "topics, partitions, and services."
        ),
        "how_it_works": (
            "Every consumer group exports its committed offsets; the "
            "monitoring service compares them against each partition's "
            "high-water mark and computes lag in events and in seconds-"
            "behind. At 03:14 the 'billing' group's lag on partition 7 "
            "starts climbing: 200, 2,000, 20,000 events. The alert fires "
            "because the growth is sustained, not spiky. The dashboard "
            "shows partition 7's publish rate tripled - a hot key from "
            "one merchant's flash sale - while the consumer's processing "
            "time per event is flat, ruling out a code slowdown. The "
            "operator checks the event trace for a sample event id and "
            "sees it flowed normally through three topics in 900 ms; the "
            "problem is volume, not breakage. The response is capacity: "
            "split the hot key's traffic or add partitions, then watch "
            "lag drain back to zero before resolving the alert."
        ),
        "key_points": [
            "Consumer lag (committed offset vs partition tip) is the primary health metric of stream consumption.",
            "The supporting constellation: publish rates, per-partition throughput, watermark lag, end-to-end latency, dead-letter depth, rebalance frequency.",
            "Alerts must separate sustained growth (urgent) from transient spikes (informational).",
            "Per-partition throughput reveals hot keys; per-event tracing reveals broken journeys.",
            "Diagnosis follows the metric: lag plus flat processing time means a volume problem, not a code problem.",
        ],
        "requirements": [
            "Lag computed per group, topic, and partition, in both events and time-behind.",
            "Dashboards covering the full metric constellation, not just lag.",
            "Alert thresholds on sustained growth with runbook links.",
            "Per-event tracing from publish through every hop to sink.",
            "Retention of metrics long enough to compare against past incidents.",
        ],
        "standards": [
            "OpenTelemetry metrics and traces for pipeline instrumentation.",
            "RED/USE method adapted to stream components.",
        ],
        "citations": [CIT_OTEL, CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method posts watchmen along the river "
            "with gauges: how far the readers trail the writers, which "
            "channels run hot, where the water slows - and the watchmen "
            "cry out only when the river truly rises."
        ),
    },
    {
        "key": "multiregion",
        "name": "Multi-Region Replication and Failover",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A stream that lives in one region dies with that region's "
            "outage, so critical event systems replicate across regions. "
            "The patterns form a ladder of cost and safety. Active-passive "
            "keeps a standby region replicating the primary's log; on "
            "failure, consumers fail over and resume from replicated "
            "offsets - simple, but failover takes minutes and the standby "
            "sits idle. Active-active runs producers and consumers in "
            "both regions with bidirectional replication, which doubles "
            "throughput but demands conflict handling when the same "
            "entity's events land in both regions (last-writer-wins, "
            "vector clocks, or partition-by-region so conflicts cannot "
            "happen). Stretch clusters span regions with synchronous "
            "replication for zero data loss, at the price of write "
            "latency bounded by inter-region round trips. The failover "
            "plan must answer: how do consumers discover the new region, "
            "how are offsets translated, what happens to in-flight "
            "transactions, and how does traffic fail back without "
            "duplicating a day's events."
        ),
        "how_it_works": (
            "The orders stream runs active-passive between us-east and "
            "us-west. A replicator tails us-east's log and appends to "
            "us-west, translating offsets and preserving event ids. At "
            "14:02 us-east goes dark. The failover controller promotes "
            "us-west: DNS flips, producers point west, and consumer "
            "groups restart with an offset-translation map (east offset "
            "4,112,003 = west offset 4,098,771 - the replicator's last "
            "synced position). Consumers resume; events published during "
            "the 90-second gap are the only loss, and the runbook said "
            "that was acceptable for this stream (RPO 5 minutes). When "
            "us-east returns, replication reverses: east catches up as a "
            "standby before any failback, and failback itself is a "
            "controlled repeat of the same offset-translation dance, "
            "scheduled in a maintenance window - never a panicked flip."
        ),
        "key_points": [
            "Active-passive: standby replicates the primary; simple failover, minutes of downtime, idle standby cost.",
            "Active-active: both regions live; doubles throughput but needs a conflict strategy for shared entities.",
            "Stretch clusters: synchronous cross-region replication for zero loss, priced in write latency.",
            "Failover needs offset translation, consumer redirection, in-flight transaction handling, and a failback plan.",
            "The RPO/RTO for each stream must be declared before the outage, not discovered during it.",
        ],
        "requirements": [
            "A replication topology per critical stream with declared RPO and RTO.",
            "Offset translation between regions, tested, not theorized.",
            "Conflict handling for any active-active entity (partition-by-region preferred).",
            "Automated failover drills that actually move consumers and verify resumed processing.",
            "A failback runbook executed in maintenance windows, never as a panicked flip.",
        ],
        "standards": [
            "Disaster-recovery practices for log-based systems (RPO/RTO definitions per ISO 27031).",
        ],
        "citations": [CIT_KLEPPMANN, CIT_KAFKA],
        "sig_lens": (
            "The Signature Stream Method digs the river in two valleys: "
            "the testimony flows in both, the readers know both banks, "
            "and if one valley floods, the reading continues on the other "
            "without losing the place."
        ),
    },
    {
        "key": "security_redaction",
        "name": "Securing Event Data: Encryption and Redaction",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Event streams accumulate everything - including the data "
            "regulations care about most: names, emails, card numbers, "
            "health facts - and immutability makes 'just delete it' "
            "impossible. Security therefore has to be designed in, not "
            "bolted on. Encryption in transit (TLS between every hop) "
            "and at rest (encrypted volumes and object stores) is table "
            "stakes; field-level encryption goes further, encrypting "
            "sensitive payload fields so the stream infrastructure itself "
            "never sees plaintext. Access control decides who may publish "
            "to and read from each topic, with service identities rather "
            "than shared passwords. PII strategy is the hard part: "
            "tokenize sensitive fields at the edge (store the mapping in "
            "a vault, put tokens in events), so a deletion request means "
            "destroying the mapping - crypto-shredding - instead of "
            "rewriting history. Audit logging of who read what completes "
            "the picture, because the stream that remembers everything "
            "must also remember who looked."
        ),
        "how_it_works": (
            "At the API edge, the checkout service tokenizes the card "
            "number: the vault stores the real PAN mapped to token "
            "'tok_9f2', and the 'PaymentAuthorized' event carries only "
            "'tok_9f2'. The event flows through the stream, the warehouse, "
            "and three years of archives - none of which ever hold the "
            "real card number. When the customer invokes deletion, the "
            "vault destroys the mapping; the token in a million archived "
            "events becomes a meaningless string - crypto-shredding, "
            "effective deletion without touching immutable history. "
            "Meanwhile the stream itself runs on mutual TLS: every broker, "
            "producer, and consumer presents a certificate, topic ACLs "
            "grant the warehouse read-only on payments and nothing on "
            "HR events, and an audit topic records every read of "
            "classified topics. Key rotation happens quarterly with "
            "dual-key support so in-flight events decrypt cleanly."
        ),
        "key_points": [
            "Immutability makes retroactive deletion impossible, so sensitive data must be protected at publish time.",
            "Field-level encryption keeps plaintext out of the stream infrastructure itself.",
            "Tokenization at the edge plus vault-held mappings enables crypto-shredding for deletion requests.",
            "Topic ACLs with service identities control who can publish and read each stream.",
            "Audit logging of reads completes the picture: the stream that remembers everything records who looked.",
        ],
        "requirements": [
            "TLS everywhere: every hop between producers, brokers, and consumers.",
            "Encryption at rest for log segments and archives, with managed key rotation.",
            "A tokenization or field-encryption strategy for regulated fields, applied at the edge.",
            "Topic-level ACLs bound to service identities, reviewed regularly.",
            "An audit trail of access to classified topics, retained per policy.",
        ],
        "standards": [
            "TLS 1.2+ (RFC 8446 for 1.3); AES-256-GCM for field encryption.",
            "NIST SP 800-57 key management guidance; PCI DSS constraints on cardholder data in logs.",
        ],
        "citations": [CIT_KLEPPMANN],
        "sig_lens": (
            "The Signature Stream Method seals the tender words of "
            "testimony in cipher at the moment of speaking: the river "
            "carries sealed letters, only the rightful reader holds the "
            "key, and burning the key unreads every copy at once."
        ),
    },
    {
        "key": "temporal_queries",
        "name": "Temporal Queries and Time Travel",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Because an event-sourced system keeps its history, it can "
            "answer questions about the past that ordinary databases "
            "cannot: 'what was this customer's tier on March 3rd?', "
            "'which orders were open when the outage began?', 'show me "
            "the account exactly as the auditor saw it in Q2'. A temporal "
            "query replays a stream's events up to a chosen point in "
            "time - an as-of timestamp or a revision - and returns the "
            "state as it was then. Bi-temporal modeling goes further, "
            "tracking both when the fact was true in the world (valid "
            "time) and when the system learned it (transaction time), "
            "which correctly handles backdated corrections: the invoice "
            "was wrong from January, we learned in March. Time travel is "
            "also an operational tool: restore a projection to last "
            "Tuesday's state to investigate, or rebuild a deleted "
            "aggregate from its tombstoned stream. The cost is retention - "
            "you can only travel as far back as the history you kept - "
            "which is why retention policy and temporal query capability "
            "are designed together."
        ),
        "how_it_works": (
            "The auditor asks: 'what was account-4471's balance on "
            "2026-03-03 at midnight?' The query service loads the "
            "account's stream, filters to events with event time at or "
            "before the as-of instant, folds them, and returns 12,480.00 - "
            "the balance as it truly was that night, even though later "
            "corrections changed the current balance. For the backdated "
            "fee correction, bi-temporal records show: valid time January "
            "(when the fee should have applied), transaction time March "
            "(when the correction event arrived) - so the March report "
            "and the restated January report both come out right. "
            "Operationally, when a bad deploy corrupted the search index, "
            "the team rebuilt it with an as-of replay capped at the "
            "deploy minute, then let live events catch it up - time "
            "travel as a recovery procedure."
        ),
        "key_points": [
            "Temporal (as-of) queries replay history to a chosen instant and return state as it was then.",
            "Bi-temporal modeling separates valid time (when true in the world) from transaction time (when learned).",
            "Backdated corrections are handled correctly only when both times are tracked.",
            "Time travel is operational: investigate past states, rebuild from a point, recover from bad deploys.",
            "You can only travel as far back as retained history - retention and time-travel are designed together.",
        ],
        "requirements": [
            "Event-time timestamps trustworthy enough for as-of boundaries.",
            "Retention covering the oldest as-of query the business needs.",
            "A fold path that accepts an as-of cutoff, not just full replay.",
            "Bi-temporal fields on corrections where restatement matters.",
            "Access controls on historical queries - the past is as sensitive as the present.",
        ],
        "standards": [
            "SQL:2011 temporal table concepts as the relational analogue; bi-temporal modeling literature (Snodgrass).",
        ],
        "citations": [CIT_YOUNG, CIT_FOWLER_ES],
        "sig_lens": (
            "The Signature Stream Method lets the reader walk the scroll "
            "to any mark and see the world as it stood that hour: the "
            "past is not guessed from the present - it is reread, line "
            "by numbered line."
        ),
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
assert [e["ladder_rank"] for e in ENTRIES] == sorted(e["ladder_rank"] for e in ENTRIES), "ladder ranks not non-decreasing"
assert len({e["key"] for e in ENTRIES}) == 34, "duplicate entry keys"
