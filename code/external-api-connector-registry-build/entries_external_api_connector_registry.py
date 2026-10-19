#!/usr/bin/env python3
"""Entries for the External API Connector Registry databases (JAH Databases
governance track, group F, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); ID prefixes JAH-EACR- (public) and
JAH-EACRS- (signature) verified free: zero exact or substring hits in
manifest id_prefix values and zero hits in all shard record IDs of
jah-databases-data-1. All 68 record titles checked against the whole
system (exact dedupe index + live shard index corpus) BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  external-api-connector-registry           - The External API Connector
      Registry Database (public-harvest: real, fact-checked connector
      knowledge - REST, GraphQL, webhooks, SOAP, gRPC, event streams, file
      transfer; authentication: API keys, OAuth 2.0, mutual TLS, HMAC
      webhooks; rate-limit models, pagination, retries with backoff,
      idempotency, versioning, caching, failover and circuit breaking, SLA
      tracking, cost metering, security audits, change management, test
      harnesses, documentation standards, multi-tenancy, deprecation,
      PII redaction, marketplace governance, federation rosters)
  external-api-connector-registry-signature - The External API Connector
      Registry Signature Database (the Signature Connector Doctrine: every
      external service a sworn covenant with explicit authentication,
      measured limits, declared formats, honest failure behavior; src
      signature, titles suffixed " (Signature Edition)", never presented
      as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_external_api_connector_registry.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - the Signature Connector Doctrine: every "
            "external service treated as a sworn covenant with explicit "
            "authentication, measured rate limits, declared data formats, "
            "and honest failure behavior, reviewed on a fixed cadence. "
            "Clearly labeled Signature-made, never presented as an "
            "authentic public record. Property of Justin Addam Higgins "
            "(JAH).")

ENTRIES = [
# ---------------- Foundations (1-10) ----------------
{
 "name": "Connector Registry Overview",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "demo_key": "d_overview", "demo_data": {"connector_types": 8, "auth_schemes": 5, "required_fields": 12, "review_cadence_days": 90},
 "description": ("An external API connector registry is the authoritative catalog of every "
   "outside service a system depends on: who the provider is, what the service does, how to "
   "authenticate, what the rate limits are, which data formats are accepted, how failures behave, "
   "and what the current operational status is. Without a registry, connector knowledge lives in "
   "scattered code comments, wiki pages, and developers' heads, so the same rate limit gets "
   "rediscovered - usually during an outage. The registry turns each connector into a governed "
   "record with an owner, a review date, and a declared contract, so any engineer can answer "
   "'what happens when this API is down' in seconds instead of hours."),
 "how_it_works": ("Each connector gets one registry record carrying twelve required fields: "
   "provider identity, service description, base URLs for production and sandbox, authentication "
   "requirements, rate-limit policy, supported data formats, error-code conventions, retry and "
   "timeout guidance, pagination behavior, webhook details if any, status-page URL, and an "
   "operational contact. Records are reviewed on a fixed cadence - every ninety days - because "
   "providers change limits and deprecate versions without asking. The registry feeds monitoring "
   "(which endpoints to probe), incident response (who to call, what the fallback is), cost "
   "tracking (what each call costs), and procurement (which contracts exist). A connector not in "
   "the registry is an ungoverned dependency: it may work today and it may not."),
 "key_points": [
   "One authoritative record per external service, owned and review-dated.",
   "Twelve required fields: identity, URLs, auth, limits, formats, errors, retries, pagination, webhooks, status page, contact.",
   "Ninety-day review cadence - providers change terms without asking.",
   "Feeds monitoring, incident response, cost tracking, and procurement.",
   "Ungoverned connectors (not in the registry) are treated as incidents waiting to happen.",
   "Sandbox and production endpoints recorded separately - never test credentials against production.",
 ],
 "requirements": [
   "Every production connector registered before first production call.",
   "A named owner accountable for the record's accuracy.",
   "Review date never older than ninety days for active connectors.",
   "Status-page URL or equivalent liveness signal for every connector.",
 ],
 "standards": [
   "Records follow the registry schema exactly - no free-form connector notes.",
   "Authentication secrets never stored in the registry - references to the vault only.",
   "Deprecation notices recorded the day they are announced, with the provider's sunset date.",
   "Version history kept: each record change is a new version, never a silent edit.",
 ],
 "citations": [
   "Fielding, R. T. Architectural Styles and the Design of Network-based Software Architectures. Doctoral dissertation, University of California, Irvine, 2000 (REST constraints underlying connector contracts).",
   "NIST Special Publication 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management (authentication assurance levels).",
 ],
 "sig_lens": ("The Signature Connector Doctrine reads this record as a covenant ledger: every "
   "external dependency is a promise made to the system's users, and a promise not written down "
   "is a promise that will be broken. The Signature registry therefore treats the owner field as "
   "a personal oath and the review cadence as a renewal ceremony - the covenant is re-sworn "
   "every ninety days or it is declared lapsed."),
},
{
 "name": "REST API Connector Profile",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "demo_key": "d_rest", "demo_data": {"methods": ["GET","POST","PUT","PATCH","DELETE"], "status_classes": 5, "idempotent_methods": ["GET","PUT","DELETE"], "max_timeout_s": 30},
 "description": ("The REST connector profile records how a system talks to a Representational State "
   "Transfer service: the resource URLs, the HTTP methods used, what each status code means for "
   "this provider, and which operations are safe to retry. REST is the dominant style for public "
   "APIs - resources addressed by URLs, manipulated with the standard HTTP verbs, described by "
   "status codes in five classes. The profile pins down the provider's actual behavior, because "
   "real APIs deviate: some return 200 with an error body, some use POST for everything, some "
   "rate-limit with 429 and some with 403. The profile documents the truth, not the ideal."),
 "how_it_works": ("The profile lists each endpoint family the connector uses with its method, URL "
   "template, required parameters, and the meaning of its success and error responses. Status "
   "codes are mapped per provider: 2xx success handling, 4xx client-error handling (including "
   "which 4xx means 'fix the request' versus 'you are rate-limited'), and 5xx server-error "
   "handling with the retry policy. Idempotent methods - GET, PUT, DELETE - are marked safe for "
   "automatic retry; POST and PATCH get explicit retry rules because repeating them can double-"
   "charge or double-create. Timeouts are set per endpoint family with a thirty-second ceiling "
   "for synchronous calls, and every call carries a request identifier for tracing."),
 "key_points": [
   "Resources, methods, and per-provider status-code meanings - the truth, not the ideal.",
   "Idempotent methods (GET, PUT, DELETE) are safe to retry automatically.",
   "POST and PATCH need explicit retry rules - repeats can double-create.",
   "Thirty-second ceiling on synchronous call timeouts.",
   "Every call carries a request identifier for tracing.",
   "Provider quirks (200-with-error-body, POST-for-everything) documented explicitly.",
 ],
 "requirements": [
   "Endpoint families documented with method, URL template, and parameters.",
   "Per-provider status-code map covering 2xx, 4xx, and 5xx handling.",
   "Retry safety marked per method.",
   "Timeout values recorded per endpoint family.",
 ],
 "standards": [
   "Follows RFC 7231 HTTP semantics for method and status-code interpretation.",
   "URL templates use RFC 6570-style variable notation.",
   "Error bodies parsed for provider error codes, not just HTTP status.",
   "Clock skew tolerance of five minutes assumed for timestamped requests.",
 ],
 "citations": [
   "Fielding, R. T. Architectural Styles and the Design of Network-based Software Architectures. Doctoral dissertation, University of California, Irvine, 2000.",
   "RFC 7231: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content. Fielding and Reschke, Eds., 2014.",
   "OpenAPI Specification v3.1.0, OpenAPI Initiative, Linux Foundation (machine-readable REST contracts).",
 ],
 "sig_lens": ("Under the Signature Connector Doctrine, a REST profile is a treaty with a foreign "
   "power: the provider's URL space is their territory, and the profile is the map the system "
   "carries across the border. The Signature edition demands the map be drawn from actual "
   "expeditions - recorded request and response pairs - never from the provider's brochure."),
},
{
 "name": "GraphQL Connector Profile",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "demo_key": "d_graphql", "demo_data": {"operations": ["query","mutation","subscription"], "complexity_limit": 1000, "depth_limit": 10, "rate_unit": "complexity points"},
 "description": ("The GraphQL connector profile records how a system talks to a GraphQL service: the "
   "single endpoint, the schema's queries and mutations in use, and - critically - how the "
   "provider measures cost. GraphQL replaces many REST endpoints with one endpoint that answers "
   "precisely-shaped queries, which shifts the rate-limit problem: instead of counting requests, "
   "providers count query complexity or depth. A naive client can burn a whole quota with a "
   "single deeply-nested query. The profile therefore records the provider's complexity rules, "
   "depth limits, and persisted-query requirements so clients stay inside the budget."),
 "how_it_works": ("The profile captures the endpoint URL, the schema version or introspection "
   "snapshot in use, and every query and mutation the system actually sends, each annotated with "
   "its computed complexity score. Depth is capped - commonly at ten levels - and complexity at "
   "the provider's published limit, commonly around one thousand points per request. Mutations "
   "are serialized where the provider requires it, and subscriptions are profiled separately "
   "with their transport (usually WebSocket) and heartbeat expectations. Query batching rules "
   "are recorded because some providers count a batch as one request and others count each "
   "operation. Persisted queries, where the provider requires pre-registered query hashes, are "
   "listed with their registration procedure."),
 "key_points": [
   "One endpoint, shaped queries - cost measured in complexity, not request count.",
   "Depth commonly capped at ten levels; complexity commonly capped near one thousand points.",
   "Every query in use annotated with its computed complexity score.",
   "Mutations serialized where required; subscriptions profiled with transport and heartbeat.",
   "Batching rules recorded - providers count batches differently.",
   "Persisted-query registration procedure documented where required.",
 ],
 "requirements": [
   "Schema snapshot or version pinned - never query against a moving schema blindly.",
   "Complexity score computed for every query before it ships.",
   "Subscription transport and reconnection behavior documented.",
   "Introspection disabled or restricted in production-facing profiles.",
 ],
 "standards": [
   "Follows the GraphQL Specification (GraphQL Foundation) for operation semantics.",
   "Errors follow the GraphQL error format with path and extensions parsed.",
   "Query documents stored under version control, referenced by hash.",
   "Complexity calculation method recorded so scores are reproducible.",
 ],
 "citations": [
   "GraphQL Specification, GraphQL Foundation (query, mutation, subscription semantics).",
   "RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format. Bray, Ed., 2017.",
 ],
 "sig_lens": ("The Signature edition treats a GraphQL profile as a precision instrument: because "
   "one query can cost a thousand points, the Signature doctrine requires every query to carry "
   "its complexity score like a price tag, computed before the query ever leaves the building."),
},
{
 "name": "Webhook Connector Profile",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "demo_key": "d_hmac", "demo_data": {"algorithm": "HMAC-SHA256", "header": "X-Signature", "tolerance_s": 300, "secret": "whsec_test_9f2c", "payload": "event=payment.succeeded&id=evt_881"},
 "description": ("The webhook connector profile records how a system receives push notifications from "
   "a provider: the endpoint URL, the event types subscribed, and - most importantly - how to "
   "verify that an incoming call really came from the provider. Webhooks invert the usual "
   "direction: the provider calls the system, which means the system's front door must "
   "distinguish genuine provider calls from forged ones. The standard defense is a signature "
   "header - an HMAC of the payload computed with a shared secret - checked before any business "
   "logic runs. The profile also records replay protection, because a captured genuine webhook "
   "can be re-sent by an attacker."),
 "how_it_works": ("The profile lists the public endpoint URL, the subscribed event types, and the "
   "signature scheme: usually HMAC-SHA256 over the raw request body with a shared secret, "
   "delivered in a named header. Verification recomputes the HMAC with a constant-time "
   "comparison - never a plain string equality that leaks timing information. Timestamps in the "
   "payload or header are checked against a tolerance window, commonly three hundred seconds, "
   "to reject replayed calls. Each event carries a unique delivery identifier so duplicate "
   "deliveries - which providers send freely - are deduplicated before processing. The endpoint "
   "responds quickly with success and processes asynchronously, because providers retry "
   "aggressively when responses are slow, multiplying load."),
 "key_points": [
   "Provider calls the system - signature verification runs before any business logic.",
   "HMAC-SHA256 over the raw body with a shared secret is the standard scheme.",
   "Constant-time comparison only - plain equality leaks timing information.",
   "Three-hundred-second tolerance window rejects replayed calls.",
   "Delivery identifiers deduplicated - providers redeliver freely.",
   "Acknowledge fast, process asynchronously - slow responses trigger retry storms.",
 ],
 "requirements": [
   "Shared secret stored in the vault, rotated on a schedule.",
   "Signature verification mandatory - unverified calls are rejected, never processed.",
   "Endpoint served over TLS with a valid certificate.",
   "Replay window enforced on every delivery.",
 ],
 "standards": [
   "HMAC per RFC 2104 / FIPS 198-1 with SHA-256.",
   "Timestamp tolerance of three hundred seconds unless the provider specifies otherwise.",
   "Idempotency on delivery identifiers - at-least-once delivery assumed.",
   "Secrets rotated at least annually and immediately on suspected exposure.",
 ],
 "citations": [
   "RFC 2104: HMAC: Keyed-Hashing for Message Authentication. Krawczyk, Bellare, and Canetti, 1997.",
   "NIST FIPS 198-1: The Keyed-Hash Message Authentication Code (HMAC), 2008.",
 ],
 "sig_lens": ("In the Signature Connector Doctrine a webhook endpoint is a guarded gate: the "
   "signature check is the password, the replay window is the curfew, and the delivery log is "
   "the guest book. The Signature edition insists the gate log every knock - verified or not - "
   "so forgery attempts become visible instead of silent."),
},
{
 "name": "API Key Authentication Profile",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "demo_key": "d_apikey", "demo_data": {"header": "X-API-Key", "rotation_days": 90, "scopes": ["read","write"], "prefix": "sk_live_"},
 "description": ("The API key authentication profile records the simplest widely-used credential "
   "scheme: a long random string the client sends with each request, usually in a header, that "
   "identifies the caller and authorizes the call. API keys are easy to issue and easy to use, "
   "which is why they are everywhere - and easy to leak, which is why they need discipline. A "
   "key found in a log file, a mobile app binary, or a public code repository is a compromised "
   "key. The profile records where the key travels, where it is stored, how it is scoped, and "
   "how it is rotated, so a leaked key is a bounded incident rather than a catastrophe."),
 "how_it_works": ("The profile names the header or parameter that carries the key, the key's "
   "prefix convention (which identifies the key type without revealing it), and the scopes the "
   "key holds - read-only keys for read-only jobs, never a master key where a scoped key will "
   "do. Keys live in the credential vault and reach applications as environment references, "
   "never baked into code or container images. Rotation happens on a ninety-day schedule and "
   "immediately on any suspected exposure, using the provider's overlap window so the old and "
   "new key both work during the changeover. Usage is monitored per key so an unexpected spike "
   "triggers an alert, and revoked keys are confirmed dead with a test call."),
 "key_points": [
   "Simplest credential scheme - and the easiest to leak, so it needs the most discipline.",
   "Scoped keys only: read-only jobs get read-only keys, never master keys.",
   "Keys live in the vault, referenced by environment - never baked into code or images.",
   "Ninety-day rotation plus immediate rotation on suspected exposure.",
   "Per-key usage monitoring - unexpected spikes raise alerts.",
   "Prefix conventions identify key type without revealing the key.",
 ],
 "requirements": [
   "Key transport (header name or parameter) documented.",
   "Scopes recorded and minimal for the connector's purpose.",
   "Rotation schedule documented and actually executed.",
   "Revocation procedure tested - a revoked key must provably stop working.",
 ],
 "standards": [
   "Keys generated with at least 128 bits of entropy from a cryptographic random source.",
   "TLS 1.2 or better for every key-bearing request.",
   "No keys in logs, error messages, URLs, or client-side code.",
   "Overlap rotation: old and new keys valid during changeover, old revoked after.",
 ],
 "citations": [
   "NIST Special Publication 800-63B, Digital Identity Guidelines: Authentication and Lifecycle Management (authenticator types and rotation).",
   "RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3. Rescorla, 2018.",
 ],
 "sig_lens": ("The Signature doctrine treats an API key as a house key handed to a contractor: "
   "it opens only the rooms the job needs, it is taken back when the job ends, and the locks "
   "are changed on a schedule whether or not anyone misbehaved. Trust is measured in days, "
   "not in intentions."),
},
{
 "name": "OAuth 2.0 Connector Profile",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "demo_key": "d_oauth", "demo_data": {"flows": ["authorization_code","client_credentials","refresh_token"], "token_lifetime_min": 60, "scopes": ["read","write"], "pkce": True},
 "description": ("The OAuth 2.0 connector profile records the delegated-authorization scheme that lets "
   "a system act on a user's behalf without ever seeing the user's password. Instead of "
   "credentials, the system holds tokens: short-lived access tokens that authorize calls and "
   "longer-lived refresh tokens that mint new access tokens. The profile records which flow the "
   "connector uses - authorization code for user-facing apps, client credentials for "
   "machine-to-machine calls - plus the token lifetimes, the scopes granted, and the refresh "
   "strategy. Getting OAuth wrong means expired tokens at 3 AM or, worse, tokens with broader "
   "scope than the job needs."),
 "how_it_works": ("The profile documents the authorization endpoint, token endpoint, and revocation "
   "endpoint, the client identifier (never the client secret, which stays in the vault), and the "
   "exact flow in use. User-facing connectors use the authorization code flow with PKCE, which "
   "binds the code exchange to the client that started it and defeats interception. "
   "Machine-to-machine connectors use the client credentials flow. Access tokens are treated as "
   "bearer credentials with lifetimes commonly around sixty minutes; refresh happens proactively "
   "before expiry, not reactively after a 401. Scopes are requested minimally - read scope for "
   "read jobs - and the granted scopes are recorded because providers sometimes grant less than "
   "asked. Token storage is encrypted at rest, and refresh tokens are rotated where the provider "
   "supports it."),
 "key_points": [
   "Delegated authorization: tokens, not passwords, cross the wire.",
   "Authorization code with PKCE for user-facing apps; client credentials for machines.",
   "Access tokens short-lived (commonly sixty minutes); refresh proactively before expiry.",
   "Minimal scopes requested; granted scopes recorded (providers may grant less).",
   "Client secret stays in the vault - never in the registry or code.",
   "Refresh-token rotation enabled wherever the provider supports it.",
 ],
 "requirements": [
   "Flow type documented and matched to the connector's actual use.",
   "Token lifetimes and refresh strategy recorded.",
   "Granted scopes verified against requested scopes.",
   "Revocation endpoint recorded and tested.",
 ],
 "standards": [
   "RFC 6749: The OAuth 2.0 Authorization Framework.",
   "RFC 7636: Proof Key for Code Exchange (PKCE) for public clients.",
   "Tokens encrypted at rest; transmitted only over TLS.",
   "Clock skew tolerance of five minutes for token expiry checks.",
 ],
 "citations": [
   "RFC 6749: The OAuth 2.0 Authorization Framework. Hardt, Ed., 2012.",
   "RFC 7636: Proof Key for Code Exchange by OAuth Public Clients. Sakimura, Bradley, and Agarwal, 2015.",
 ],
 "sig_lens": ("The Signature Connector Doctrine reads OAuth as a letter of marque: the token is a "
   "commission that authorizes specific acts for a limited time, and it expires by design. The "
   "Signature edition requires every connector to prove it can survive token expiry gracefully - "
   "a commission renewed in the dark, without waking the user."),
},
{
 "name": "Rate Limit Model Record",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "demo_key": "d_token_bucket", "demo_data": {"capacity": 100, "refill_per_s": 10, "requests": [0.0,0.05,0.1,0.2,0.5,1.0,1.1,2.0,5.0,10.0], "burst": 12},
 "description": ("The rate limit model record states exactly how fast a connector may call a "
   "provider before the provider starts refusing: the limit, the window it applies to, and what "
   "happens at the boundary. Providers express limits in several dialects - requests per second, "
   "per minute, per day; tokens per minute for AI services; complexity points per request for "
   "GraphQL - and exceeding them returns 429 Too Many Requests, sometimes with a Retry-After "
   "header and sometimes without. The record translates the provider's dialect into one "
   "enforceable client-side model, usually a token bucket, so the system throttles itself "
   "instead of being throttled."),
 "how_it_works": ("The record states the provider's published limit (for example, one hundred "
   "requests per burst with a refill of ten per second), the window semantics (fixed window, "
   "sliding window, or token bucket), and the response headers that report current usage - "
   "commonly X-RateLimit-Limit, X-RateLimit-Remaining, and X-RateLimit-Reset. The client "
   "implements a token bucket matching the provider's model: capacity one hundred tokens, refill "
   "ten per second, each request consuming one token, requests with no token waiting instead of "
   "firing. On a 429 the client honors Retry-After when present and otherwise backs off "
   "exponentially. The record also notes whether limits are per API key, per IP, or per account, "
   "because the same code behaves differently under each."),
 "key_points": [
   "Provider dialects translated into one enforceable client-side token-bucket model.",
   "Usage headers (Limit, Remaining, Reset) monitored, not ignored.",
   "Client throttles itself - being throttled by the provider is the failure case.",
   "429 handling: honor Retry-After when present, exponential backoff otherwise.",
   "Limit scope recorded: per key, per IP, or per account changes everything.",
   "Burst capacity and sustained rate modeled separately.",
 ],
 "requirements": [
   "Published limit, window, and scope documented from provider docs.",
   "Client-side limiter implemented and tested against the model.",
   "429 response handling verified with a real (sandbox) 429.",
   "Usage headers logged so quota burn is visible.",
 ],
 "standards": [
   "HTTP 429 semantics per RFC 6585 (Additional HTTP Status Codes).",
   "Retry-After header honored per RFC 7231 when the provider sends it.",
   "No more than the published burst in flight at once.",
   "Jitter added to backoff to avoid synchronized retry stampedes.",
 ],
 "citations": [
   "RFC 6585: Additional HTTP Status Codes. Nottingham and Fielding, 2012 (status 429).",
   "RFC 7231: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content. Fielding and Reschke, Eds., 2014 (Retry-After).",
 ],
 "sig_lens": ("The Signature doctrine treats a rate limit as a speed limit posted by the road's "
   "owner: the Signature connector drives under it by construction, with the token bucket as its "
   "governor. Speeding and apologizing is not a strategy; the Signature edition measures "
   "compliance in the client, not in the provider's forgiveness."),
},
{
 "name": "Data Format Profiles",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "demo_key": "d_formats", "demo_data": {"formats": ["JSON","XML","form-urlencoded","multipart"], "default": "JSON", "charset": "UTF-8", "date_format": "RFC 3339"},
 "description": ("The data format profiles record which representations a connector speaks: JSON for "
   "most modern APIs, XML for enterprise and legacy services, form-encoding for OAuth token "
   "endpoints, multipart for file uploads. Format handling is where silent corruption breeds - a "
   "date parsed as local time instead of UTC, a large integer losing precision in a JSON parser, "
   "an XML namespace ignored. The profile pins down the character encoding, the date and time "
   "format, number handling, and how unknown fields are treated, so parsing is deterministic "
   "instead of hopeful."),
 "how_it_works": ("The profile lists each supported format with its media type (application/json, "
   "application/xml, application/x-www-form-urlencoded, multipart/form-data), the character "
   "encoding - UTF-8 unless the provider proves otherwise - and the content negotiation the "
   "connector performs via Accept headers. Dates and times use RFC 3339 (a profile of ISO 8601) "
   "with explicit offsets; the profile states the rule for missing offsets rather than leaving "
   "it to parser defaults. Numbers that exceed 53-bit integer precision are transported as "
   "strings where the provider does so, and the profile says so. Unknown fields are ignored on "
   "read and never dropped on write-through, so provider additions do not break the client. "
   "Request and response examples are stored as fixtures for the test harness."),
 "key_points": [
   "Media types, UTF-8 encoding, and Accept-header negotiation recorded per connector.",
   "Dates in RFC 3339 with explicit offsets; missing-offset rule stated, not assumed.",
   "Large integers transported as strings where the provider does so.",
   "Unknown fields ignored on read, preserved on write-through.",
   "Request/response fixtures stored for the test harness.",
   "One default format per connector; alternatives documented, not guessed.",
 ],
 "requirements": [
   "Media type and charset documented for requests and responses.",
   "Date/time and number handling rules written down.",
   "Fixtures captured from real provider traffic.",
   "Unknown-field policy stated explicitly.",
 ],
 "standards": [
   "RFC 8259 for JSON; RFC 3339 for date/time.",
   "UTF-8 encoding unless the provider documents otherwise.",
   "Strict parsing of known fields, lenient handling of unknown ones.",
   "Fixtures refreshed when the provider versions its API.",
 ],
 "citations": [
   "RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format. Bray, Ed., 2017.",
   "RFC 3339: Date and Time on the Internet: Timestamps. Klyne and Newman, 2002.",
 ],
 "sig_lens": ("The Signature edition treats format profiles as translation treaties: every field "
   "that crosses the border must have its meaning fixed in writing. The Signature doctrine holds "
   "that most integration bugs are translation errors, and translation errors are prevented by "
   "treaties, not by hope."),
},
{
 "name": "Error Handling Conventions",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "demo_key": "d_errors", "demo_data": {"retryable": [429,500,502,503,504], "fatal": [400,401,403,404,422], "timeout_s": 30, "max_attempts": 4},
 "description": ("The error handling conventions record classifies every failure a connector can "
   "meet into three buckets: retryable, fatal, and unknown. Retryable errors - 429 rate limits, "
   "502/503/504 gateway problems, network timeouts - get another attempt with backoff. Fatal "
   "errors - 400 bad requests, 401/403 authorization failures, 404 missing resources, 422 "
   "unprocessable entities - never get retried, because repeating them changes nothing except "
   "the bill. The unknown bucket is the honest one: errors the provider never documented, which "
   "get logged in full, alerted on, and classified by a human before any retry policy applies."),
 "how_it_works": ("The record maps each documented provider error - HTTP status plus the provider's "
   "own error code from the response body - to a bucket and an action. Retryable errors enter "
   "the retry policy: up to four attempts total, exponential backoff with jitter, honoring "
   "Retry-After. Fatal errors surface immediately to the caller with the provider's error code "
   "and message preserved, so debugging starts from facts. Unknown errors are logged with the "
   "full request and response, counted in monitoring, and paged when their rate crosses a "
   "threshold, because a new undocumented error is often the first sign of a provider change. "
   "Timeouts are classified as retryable for idempotent operations and fatal otherwise. Every "
   "convention is verified against the sandbox before production."),
 "key_points": [
   "Three buckets: retryable, fatal, unknown - every error lands in exactly one.",
   "Retryable: 429, 502/503/504, timeouts - with backoff and jitter.",
   "Fatal: 400, 401/403, 404, 422 - surfaced immediately, never retried.",
   "Unknown: logged in full, alerted on, classified by a human first.",
   "Provider error codes from the body preserved - status alone is not enough.",
   "Conventions verified against the sandbox before production.",
 ],
 "requirements": [
   "Error map covering all documented provider errors.",
   "Retry policy with attempt cap, backoff, and jitter documented.",
   "Unknown-error alerting threshold set and tested.",
   "Fatal errors carry the provider's code and message to the caller.",
 ],
 "standards": [
   "Maximum four attempts per operation including the first try.",
   "Jitter on every backoff to prevent retry stampedes.",
   "Full request/response logging for unknown errors (secrets redacted).",
   "Error classification reviewed whenever the provider versions its API.",
 ],
 "citations": [
   "RFC 7231: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content. Fielding and Reschke, Eds., 2014 (status code semantics).",
   "RFC 7807: Problem Details for HTTP APIs. Nottingham and Wilde, 2016 (structured error bodies).",
 ],
 "sig_lens": ("The Signature doctrine holds that how a system fails is part of its contract: the "
   "Signature edition requires the error map to be complete enough that an on-call engineer can "
   "predict the system's behavior for any documented error without reading code. Unknown errors "
   "are treated as intelligence - each one teaches the registry something the provider never "
   "said."),
},
{
 "name": "Status and Health Check Endpoints",
 "group": "Foundations", "ladder_rank": 10, "ladder_tier": "foundations",
 "demo_key": "d_uptime", "demo_data": {"probes_per_day": 288, "downtime_min_month": 43, "sla_target": 99.9, "p95_latency_ms": 420},
 "description": ("The status and health check record states how the system knows whether a provider "
   "is alive: which endpoint to probe, how often, what counts as healthy, and where the "
   "provider's own status page lives. Probing every five minutes - 288 checks a day - turns "
   "'the API seems slow' into a timestamped record of exactly when degradation started. The "
   "record also captures the provider's published SLA, because a provider promising 99.9% "
   "uptime is allowed about forty-three minutes of downtime a month, and the system should know "
   "when the provider has spent that budget."),
 "how_it_works": ("The record names a lightweight probe endpoint - preferably the provider's "
   "dedicated health or status endpoint, otherwise the cheapest read the connector already "
   "uses - plus the probe interval (five minutes is the default), the timeout (ten seconds), "
   "and the success criteria (HTTP 200 with an expected body marker). Results feed a status "
   "timeline: up, degraded, or down, with latency percentiles tracked alongside. The provider's "
   "status page URL is recorded and its incident feed subscribed to, because provider-acknowledged "
   "incidents explain degradation the probes cannot. SLA accounting runs monthly: uptime "
   "percentage computed from probe results, compared against the provider's target, with "
   "breaches triggering the contract's service-credit process where one exists."),
 "key_points": [
   "Probe every five minutes (288 checks/day) against a lightweight endpoint.",
   "Success criteria explicit: status code plus expected body marker.",
   "Latency percentiles tracked alongside up/down state.",
   "Provider status page recorded and its incident feed subscribed.",
   "Monthly SLA accounting: 99.9% allows about forty-three downtime minutes.",
   "Breaches trigger the service-credit process where contracts provide one.",
 ],
 "requirements": [
   "Probe endpoint, interval, timeout, and success criteria documented.",
   "Status timeline retained for at least thirteen months.",
   "Provider status page URL recorded.",
   "SLA target and credit process recorded from the contract.",
 ],
 "standards": [
   "Probes use read-only operations - health checks never write.",
   "Probe credentials scoped to the minimum the endpoint needs.",
   "Degraded defined as p95 latency above target or elevated error rate, not just down.",
   "Status history exportable for contract disputes.",
 ],
 "citations": [
   "NIST Special Publication 800-53, control SI-4 (information system monitoring).",
   "Google Site Reliability Engineering, Chapter 4: Service Level Objectives (SLO/SLA practice). Beyer, Jones, Petoff, and Murphy, Eds., O'Reilly, 2016.",
 ],
 "sig_lens": ("The Signature edition treats the status timeline as a sworn witness: it testifies, "
   "month after month, whether the provider kept its promises. The Signature doctrine requires "
   "the witness to be impartial - probes run from infrastructure the provider does not control - "
   "so its testimony holds up in a contract dispute."),
},
# ---------------- Compounded (11-21) ----------------
{
 "name": "Retry and Backoff Behavior",
 "group": "Compounded", "ladder_rank": 11, "ladder_tier": "compounded",
 "demo_key": "d_backoff", "demo_data": {"base_s": 1.0, "factor": 2.0, "attempts": 4, "jitter_pct": 0.25, "retry_after_s": 30},
 "description": ("The retry and backoff record specifies exactly how a connector behaves when a "
   "call fails transiently: how many attempts, how long to wait between them, and how that wait "
   "grows. Naive retries - hammering a struggling provider at full speed - turn a small outage "
   "into a large one, a phenomenon operators call a retry storm. The disciplined alternative is "
   "exponential backoff with jitter: waits of roughly one, two, four, then eight seconds, each "
   "randomized by up to twenty-five percent so a fleet of clients does not retry in lockstep. "
   "The record also states when the provider's Retry-After header overrides the computed wait, "
   "because ignoring it is how clients get banned."),
 "how_it_works": ("The record sets a maximum of four attempts per operation including the first "
   "try, a base wait of one second doubling each attempt (1, 2, 4, 8 seconds), and jitter of up "
   "to twenty-five percent applied to each wait so retries spread out. When a 429 or 503 "
   "response carries a Retry-After header, its value wins - the record gives the example of a "
   "thirty-second Retry-After overriding the computed backoff. Only idempotent operations and "
   "classified-retryable errors enter the policy; everything else fails fast. Each attempt is "
   "logged with its wait so retry behavior is auditable, and a circuit breaker (see the advanced "
   "record) can suspend retries entirely when the provider is known down."),
 "key_points": [
   "Maximum four attempts per operation, including the first try.",
   "Exponential backoff: 1, 2, 4, 8 seconds with up to twenty-five percent jitter.",
   "Retry-After header overrides computed waits - ignoring it gets clients banned.",
   "Only idempotent operations and classified-retryable errors are retried.",
   "Jitter prevents lockstep retry stampedes across a fleet.",
   "Every attempt logged with its wait for auditability.",
 ],
 "requirements": [
   "Attempt cap, base wait, factor, and jitter documented and implemented.",
   "Retry-After handling verified against a real provider response.",
   "Retry eligibility tied to the error classification record.",
   "Backoff waits logged per attempt.",
 ],
 "standards": [
   "Backoff never exceeds the operation's overall deadline.",
   "Jitter applied to every wait, no exceptions.",
   "Total retry budget bounded: worst-case wait per operation computed and recorded.",
   "Policy re-verified whenever the provider changes rate-limit behavior.",
 ],
 "citations": [
   "RFC 7231: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content. Fielding and Reschke, Eds., 2014 (Retry-After).",
   "AWS Architecture Blog: Exponential Backoff and Jitter (standard client retry guidance).",
 ],
 "sig_lens": ("The Signature doctrine frames backoff as courtesy under fire: when the provider "
   "stumbles, the Signature connector steps back, waits its turn, and never joins a stampede. "
   "The Signature edition measures a connector's manners by its worst retry storm - which, "
   "properly governed, never happens."),
},
{
 "name": "Pagination Connector Behavior",
 "group": "Compounded", "ladder_rank": 12, "ladder_tier": "compounded",
 "demo_key": "d_pagination", "demo_data": {"total": 12500, "page_size": 100, "style": "cursor", "rate_per_s": 5},
 "description": ("The pagination record documents how a connector walks through a provider's "
   "large result sets: the paging style, the page size, and how to know when the walk is done. "
   "Providers paginate in three main styles - offset (page 1, 2, 3), cursor (an opaque token "
   "pointing at the next chunk), and keyset (continue after the last seen ID). Offset is simple "
   "but drifts when data changes mid-walk; cursor and keyset are stable. The record states the "
   "style, the maximum page size, the termination condition, and the walk's cost in requests, "
   "because twelve thousand five hundred records at one hundred per page is one hundred "
   "twenty-five requests - a quota line item, not a detail."),
 "how_it_works": ("The record names the paging style - cursor preferred, keyset acceptable, offset "
   "documented with its drift warning - and the page-size parameter with its maximum (commonly "
   "one hundred). The walk fetches pages sequentially, honoring the rate limit (five requests "
   "per second in the example), and stops on the provider's documented end signal: an empty "
   "next-cursor, a has-more flag set false, or a short page. Each page's cursor is checkpointed "
   "so an interrupted walk resumes instead of restarting, which matters when a full walk costs "
   "hundreds of requests. The record also states the sort order guarantee, because 'page 3' is "
   "meaningless if the provider does not promise a stable order."),
 "key_points": [
   "Cursor or keyset paging preferred; offset documented with its drift warning.",
   "Page size and maximum recorded (commonly one hundred per page).",
   "Termination condition explicit: empty cursor, has-more false, or short page.",
   "Cursors checkpointed - interrupted walks resume, never restart from zero.",
   "Walk cost computed in requests (12,500 records at 100/page = 125 requests).",
   "Sort-order guarantee recorded - pages are meaningless without stable order.",
 ],
 "requirements": [
   "Paging style, page-size parameter, and maximum documented.",
   "Termination condition tested against the real provider.",
   "Checkpointing implemented for walks longer than ten pages.",
   "Stable sort order confirmed or its absence flagged.",
 ],
 "standards": [
   "Sequential page fetches - parallel page walks only where the provider allows.",
   "Rate limit honored during walks; walks are quota-budgeted.",
   "Duplicate detection on resume - providers may repeat the boundary page.",
   "Full-walk cost estimated before the first production walk.",
 ],
 "citations": [
   "GraphQL Cursor Connections Specification (relay-style pagination pattern).",
   "RFC 8288: Web Linking. Nottingham, 2017 (Link-header pagination).",
 ],
 "sig_lens": ("The Signature edition treats a paginated walk as a census: every record counted, "
   "none counted twice, the walk resumable after any interruption. The Signature doctrine "
   "requires the checkpoint - a census taker who loses their place and starts over is not "
   "diligent, they are expensive."),
},
{
 "name": "Idempotency in Connectors",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "demo_key": "d_idempotency", "demo_data": {"key_header": "Idempotency-Key", "key_ttl_h": 24, "methods": ["POST","PATCH"], "replays": 3},
 "description": ("The idempotency record states how a connector makes unsafe operations safe to "
   "retry: the client generates a unique key per logical operation, sends it in a header, and "
   "the provider promises that repeats with the same key return the original result instead of "
   "performing the operation again. Without this, a retried payment creates two charges and a "
   "retried order creates two shipments - the classic double-effect of a blind retry. The "
   "record names the header (commonly Idempotency-Key), the key format, and how long the "
   "provider remembers keys, commonly twenty-four hours, because a key forgotten too soon is a "
   "double-charge waiting to happen."),
 "how_it_works": ("Before sending a POST or PATCH, the connector generates a version-4 UUID as the "
   "idempotency key and stores it with the operation's intent. If the call times out or returns "
   "a retryable error, the retry carries the same key; the provider recognizes it and returns "
   "the stored original response instead of re-executing. The record states the provider's key "
   "retention - twenty-four hours in the example - and the policy for what happens after: "
   "operations older than the retention window are never blindly retried, they are reconciled "
   "by reading current state first. Key collisions across different operations are prevented "
   "because keys are random UUIDs, and the record requires the provider's documented behavior "
   "for a reused key with a different payload (reject, the safe answer)."),
 "key_points": [
   "Unique key per logical operation, sent in a header (commonly Idempotency-Key).",
   "Repeats with the same key return the original result - no double charges.",
   "Keys are version-4 UUIDs, stored with the operation's intent.",
   "Provider key retention recorded (commonly twenty-four hours).",
   "Past the retention window: reconcile by reading state, never blindly retry.",
   "Same key with different payload must be rejected - verified, not assumed.",
 ],
 "requirements": [
   "Idempotency header name and key format documented per provider.",
   "Key retention window recorded from provider docs.",
   "Post-retention reconciliation procedure written.",
   "Key-reuse-with-different-payload behavior verified.",
 ],
 "standards": [
   "UUID version 4 for key generation (RFC 4122).",
   "Keys never reused across different logical operations.",
   "Idempotent methods (PUT, DELETE) still get keys where the provider supports them.",
   "Retry policy consults this record before any POST/PATCH retry.",
 ],
 "citations": [
   "RFC 4122: A Universally Unique IDentifier (UUID) URN Namespace. Leach, Mealling, and Salz, 2005.",
   "Stripe API Idempotency documentation (industry reference implementation).",
 ],
 "sig_lens": ("The Signature doctrine calls idempotency the oath against double-dealing: the "
   "connector swears that no failure of the network will ever cause the operation to happen "
   "twice. The Signature edition treats a missing idempotency key on a money-moving call as a "
   "breach of that oath - caught in review, never in production."),
},
{
 "name": "API Versioning Practice",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "demo_key": "d_versioning", "demo_data": {"scheme": "URL path", "current": "v3", "supported": ["v2","v3"], "sunset_v2": "2027-06-30"},
 "description": ("The API versioning record states how a provider evolves its interface without "
   "breaking existing clients: the versioning scheme, which versions are live, and when old "
   "ones die. Providers version in the URL path (/v3/), in a header, or by date; each has "
   "trade-offs the connector must live with. The critical field is the sunset date - the day "
   "the old version stops answering - because every un-migrated connector becomes an outage on "
   "that morning. The record tracks the current version, the supported versions, and the "
   "migration status of each connector pinned to an old version."),
 "how_it_works": ("The record names the provider's scheme (URL path versioning in the example), "
   "the version the connector currently uses, and every version the provider still supports. "
   "When the provider announces a new version, the record gains a migration entry: what changed "
   "(breaking vs additive), which endpoints the connector touches, the test plan against the "
   "new version in sandbox, and the cutover date - set at least thirty days before the "
   "provider's sunset date to leave margin. The example tracks v2 sunsetting on 2027-06-30 "
   "with the connector's migration scheduled a quarter earlier. Additive changes (new fields, "
   "new endpoints) are adopted opportunistically; breaking changes (removed fields, changed "
   "semantics) drive the migration schedule."),
 "key_points": [
   "Versioning scheme recorded: URL path, header, or date-based.",
   "Current, supported, and sunset versions all tracked with dates.",
   "Migration cutover set at least thirty days before the provider's sunset.",
   "Breaking changes drive migrations; additive changes adopted opportunistically.",
   "Example: v2 sunsets 2027-06-30, migration completed a quarter earlier.",
   "Un-migrated connectors are tracked as risks, not surprises.",
 ],
 "requirements": [
   "Provider versioning scheme and current version documented.",
   "Sunset dates recorded the day they are announced.",
   "Migration plan with sandbox test and cutover date for each breaking change.",
   "Connector's pinned version verified in production traffic.",
 ],
 "standards": [
   "Cutover at least thirty days before sunset - margin is mandatory.",
   "New versions tested in sandbox before any production cutover.",
   "Version pinned explicitly - never float on 'latest' in production.",
   "Sunset calendar reviewed monthly for the next two quarters.",
 ],
 "citations": [
   "OpenAPI Specification v3.1.0, OpenAPI Initiative (versioned contract description).",
   "SemVer 2.0.0: Semantic Versioning. Preston-Werner (versioning discipline reference).",
 ],
 "sig_lens": ("The Signature edition treats a sunset date as a prophecy with a deadline: the "
   "provider has foretold the day the old world ends, and the Signature connector is already "
   "living in the new one a quarter early. The doctrine forbids learning about a sunset from "
   "an outage."),
},
{
 "name": "Credential Vaulting for Connectors",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "demo_key": "d_vault", "demo_data": {"secrets": 14, "rotation_days": 90, "last_rotation": "2026-07-19", "engines": ["kv","dynamic"]},
 "description": ("The credential vaulting record states where connector secrets live and how they "
   "move: in a dedicated secrets vault, never in code, configuration files, chat logs, or the "
   "registry itself. Fourteen secrets across the connector fleet - API keys, OAuth client "
   "secrets, webhook signing secrets, mutual-TLS private keys - each with an owner, a rotation "
   "schedule, and an access policy. The vault encrypts at rest, audits every read, and issues "
   "short-lived dynamic credentials where the provider allows it, so a leaked credential dies "
   "on its own within minutes instead of living until the next rotation."),
 "how_it_works": ("The record inventories every secret the connector fleet holds: its purpose, its "
   "vault path, its owner, its rotation schedule (ninety days default), and its last rotation "
   "date - 2026-07-19 in the example, proving the schedule is real. Applications receive "
   "secrets as environment references resolved at startup, never as files on disk. Dynamic "
   "secrets are preferred: the vault mints a credential valid for minutes, the connector uses "
   "it, and it expires - nothing long-lived to steal. Every vault read is audit-logged with "
   "the requesting identity, and alerts fire on reads from unexpected identities or at "
   "unexpected hours. Rotation uses overlap windows so services never flap during the change."),
 "key_points": [
   "Secrets in the vault only - never in code, configs, chats, or the registry.",
   "Fourteen secrets inventoried with owner, schedule, and last rotation date.",
   "Dynamic short-lived credentials preferred where providers allow.",
   "Every vault read audit-logged; anomalous reads alerted.",
   "Ninety-day rotation default with overlap windows - no flapping.",
   "Applications get environment references resolved at startup, not files.",
 ],
 "requirements": [
   "Complete secret inventory with vault paths and owners.",
   "Rotation schedule documented and last-rotation dates current.",
   "Access policies: least privilege per application identity.",
   "Break-glass procedure for emergency rotation documented and drilled.",
 ],
 "standards": [
   "Encryption at rest with provider-managed or customer-managed keys.",
   "Audit log retained at least one year.",
   "No secret older than its rotation schedule in production.",
   "Dynamic credentials where supported; static only where required.",
 ],
 "citations": [
   "NIST Special Publication 800-63B, Digital Identity Guidelines (secret management).",
   "NIST Special Publication 800-57 Part 1 Rev. 5, Recommendation for Key Management (key lifecycles).",
 ],
 "sig_lens": ("The Signature doctrine treats the vault as the treasury and its audit log as the "
   "guard's journal: every withdrawal recorded, every guard's identity known. The Signature "
   "edition adds a standing rule - a secret whose rotation is overdue is treated as already "
   "compromised, because in security, lateness and breach are cousins."),
},
{
 "name": "Connector Logging and Telemetry",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "demo_key": "d_telemetry", "demo_data": {"retention_days": 90, "sample_rate": 1.0, "pii_fields": 6, "dashboards": 3},
 "description": ("The logging and telemetry record states what a connector records about every "
   "call it makes: the request identifier, the endpoint, the timing, the outcome - and what it "
   "deliberately does not record. Good telemetry turns 'the provider is slow' into 'p95 latency "
   "to the payments endpoint rose from 300 to 900 milliseconds at 14:02.' The record sets a "
   "ninety-day retention for full call logs, full sampling for errors with adaptive sampling "
   "for success, and a redaction list of six PII field patterns that are masked before a log "
   "line is ever written - because a log full of secrets is a breach waiting for a reader."),
 "how_it_works": ("Every outbound call emits a structured log record: timestamp, request ID, "
   "connector and endpoint identifiers, HTTP method and status, latency in milliseconds, "
   "request and response sizes, and the provider's request ID for correlation. Errors are "
   "sampled at one hundred percent; successful calls are sampled adaptively to bound volume. "
   "Six PII field patterns - tokens, card numbers, emails, phone numbers, national IDs, "
   "passwords - are redacted at the logging layer, before persistence. Three dashboards consume "
   "the telemetry: a real-time operations view, a weekly reliability review, and a monthly cost "
   "and quota view. Alerts fire on error-rate spikes, latency regression, and quota burn above "
   "eighty percent."),
 "key_points": [
   "Structured log per call: IDs, endpoint, timing, outcome, provider request ID.",
   "Ninety-day retention for full logs; errors sampled at one hundred percent.",
   "Six PII field patterns redacted at the logging layer, before persistence.",
   "Three dashboards: real-time ops, weekly reliability, monthly cost/quota.",
   "Alerts on error spikes, latency regression, and quota burn above eighty percent.",
   "Telemetry turns 'seems slow' into timestamped, percentile-measured fact.",
 ],
 "requirements": [
   "Log schema documented with every field's meaning.",
   "Redaction list maintained and tested with synthetic PII.",
   "Dashboards built and reviewed on their cadences.",
   "Alert thresholds set, tested, and owned.",
 ],
 "standards": [
   "Clock synchronization via NTP - timestamps must be comparable across services.",
   "No secrets or PII in logs, ever; redaction tested, not assumed.",
   "Log integrity: append-only storage with tamper evidence.",
   "Sampling decisions recorded so metrics stay unbiased.",
 ],
 "citations": [
   "NIST Special Publication 800-92, Guide to Computer Security Log Management (log lifecycle).",
   "Google Site Reliability Engineering, Chapters 5-6 (monitoring and alerting). Beyer et al., O'Reilly, 2016.",
 ],
 "sig_lens": ("The Signature edition treats telemetry as the connector's conscience: an honest, "
   "continuous account of what the system did in the world. The Signature doctrine requires the "
   "account to be complete enough that any user-visible failure can be traced to its cause "
   "within minutes - a conscience with gaps is just a story."),
},
{
 "name": "SOAP and Legacy Connector Profile",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "demo_key": "d_soap", "demo_data": {"wsdl_ops": 42, "envelope_kb": 18, "mtom": True, "ws_security": True},
 "description": ("The SOAP and legacy connector profile records how the system talks to older "
   "enterprise services: XML envelopes, WSDL-described operations, and WS-Security headers. "
   "SOAP is verbose - an eighteen-kilobyte envelope to move a few hundred bytes of business "
   "data is normal - but it is also precise: forty-two operations described in a machine-"
   "readable contract with strict typing. These connectors usually guard the most boring and "
   "most critical integrations: payroll, insurance claims, government filings. The profile "
   "treats them with respect: they are slow, they are rigid, and they absolutely must not "
   "break."),
 "how_it_works": ("The profile stores the WSDL URL and a pinned copy of the WSDL itself, because "
   "providers edit WSDLs in place and a drifting contract breaks code generation. Each of the "
   "forty-two operations in use is listed with its SOAP action, input and output types, and "
   "fault contracts. WS-Security is documented where used - usually UsernameToken or X.509 "
   "signing - with certificate expiry dates tracked like any other secret rotation. MTOM is "
   "noted for attachment-heavy operations to avoid base64 bloat. Timeouts are generous "
   "(legacy services are slow) but bounded, and every request carries a message ID for the "
   "provider's support desk, because debugging these integrations always ends on a phone call."),
 "key_points": [
   "WSDL pinned and stored - providers edit WSDLs in place.",
   "Forty-two operations listed with SOAP actions, types, and fault contracts.",
   "WS-Security documented; certificate expiries tracked like secret rotations.",
   "MTOM noted for attachments to avoid base64 bloat.",
   "Generous but bounded timeouts; message IDs for provider support calls.",
   "These guard payroll, claims, filings - slow, rigid, and must not break.",
 ],
 "requirements": [
   "Pinned WSDL stored under version control.",
   "Operation inventory with fault contracts.",
   "Certificate expiry calendar maintained.",
   "Provider support contact and escalation path recorded.",
 ],
 "standards": [
   "SOAP 1.1 or 1.2 envelope handling per W3C specifications.",
   "Strict XML parsing with schema validation on critical operations.",
   "No dynamic WSDL fetching in production - pinned copies only.",
   "Change review for any WSDL diff before regeneration.",
 ],
 "citations": [
   "W3C SOAP Version 1.2 Part 1: Messaging Framework (Second Edition), 2007.",
   "OASIS Web Services Security: SOAP Message Security 1.1, 2006.",
 ],
 "sig_lens": ("The Signature doctrine has a special respect for legacy connectors: they are the "
   "elders of the integration world, and the Signature edition treats their rigidity as a "
   "virtue to be preserved, not a flaw to be modernized. Change near them moves slowly and is "
   "announced loudly."),
},
{
 "name": "gRPC Connector Profile",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "demo_key": "d_grpc", "demo_data": {"services": 6, "methods": 31, "streaming": 4, "deadline_s": 10, "proto_version": "v2.4"},
 "description": ("The gRPC connector profile records high-performance service-to-service calls: "
   "Protocol Buffer contracts, HTTP/2 multiplexed transport, and four kinds of streaming. "
   "Where REST sends human-readable JSON over one-request-per-connection, gRPC sends compact "
   "binary messages over a persistent multiplexed channel - far faster, far less readable on "
   "the wire. The profile pins the .proto contract version (v2.4 in the example), lists the six "
   "services and thirty-one methods in use, and documents the four streaming methods "
   "separately, because a stream that never ends needs different timeout thinking than a call "
   "that answers."),
 "how_it_works": ("The profile stores the pinned .proto files under version control and records "
   "the contract version both sides have agreed on. Each method is listed with its type - unary, "
   "server-streaming, client-streaming, or bidirectional - and its deadline, ten seconds "
   "default for unary calls. Streaming methods get keepalive parameters, maximum stream "
   "duration, and reconnection behavior, because networks drop long-lived streams. Status codes "
   "follow the gRPC code set (OK, NOT_FOUND, UNAVAILABLE, RESOURCE_EXHAUSTED for rate limits), "
   "mapped to the connector's retry policy: UNAVAILABLE is retried, INVALID_ARGUMENT is not. "
   "TLS with mutual authentication is the default transport security, and compression "
   "(usually gzip) is noted where enabled."),
 "key_points": [
   "Protocol Buffer contracts pinned under version control (v2.4 in the example).",
   "Six services, thirty-one methods inventoried by streaming type.",
   "Four streaming methods with keepalive, max duration, and reconnection behavior.",
   "Deadlines: ten seconds default for unary calls; streams bounded separately.",
   "gRPC status codes mapped to retry policy (UNAVAILABLE retries; INVALID_ARGUMENT does not).",
   "Mutual TLS default; compression noted where enabled.",
 ],
 "requirements": [
   "Pinned .proto files with agreed contract version.",
   "Method inventory by type with deadlines.",
   "Streaming reconnection behavior documented and tested.",
   "Status-code to retry-bucket mapping recorded.",
 ],
 "standards": [
   "gRPC over HTTP/2 with TLS; plaintext only in isolated test environments.",
   "Deadlines set on every call - no unbounded waits.",
   "Contract changes follow the provider's compatibility policy.",
   "Binary payloads logged as metadata only - never decoded into logs.",
 ],
 "citations": [
   "gRPC documentation: Protocol Buffers and HTTP/2 transport (grpc.io).",
   "RFC 7540: Hypertext Transfer Protocol Version 2 (HTTP/2). Belshe, Peon, and Thomson, Eds., 2015.",
 ],
 "sig_lens": ("The Signature edition treats a .proto contract as a sworn compact between services: "
   "compact on the wire, exact in meaning. The Signature doctrine requires the compact to be "
   "pinned and versioned - a compact that drifts silently is not a compact at all."),
},
{
 "name": "Event Stream Connector Profile",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "demo_key": "d_stream", "demo_data": {"events_per_s": 850, "retention_h": 72, "partitions": 12, "consumer_lag_alert_s": 60},
 "description": ("The event stream connector profile records continuous data flows: eight hundred "
   "fifty events per second across twelve partitions, retained seventy-two hours, consumed by "
   "named consumer groups. Unlike request-response APIs, streams never answer a question - they "
   "narrate what is happening, and the system listens. The profile covers the transport "
   "(server-sent events, MQTT, or a log-based broker), the event schema and its versioning, "
   "consumer-group assignments, and lag monitoring, because a consumer sixty seconds behind is "
   "a system operating on the past."),
 "how_it_works": ("The profile names the transport and the topic or channel layout - twelve "
   "partitions keyed by entity ID so related events stay ordered. Producers are documented with "
   "their throughput (850 events/second sustained in the example) and the event schema version; "
   "schema changes follow append-only evolution rules so old consumers keep working. Consumers "
   "are organized into groups with committed offsets checkpointed durably, so a restarted "
   "consumer resumes where it stopped. Lag is monitored per group with a sixty-second alert "
   "threshold, and retention of seventy-two hours bounds how far behind a consumer may fall "
   "before data is gone. Dead-letter handling is specified for poison events that crash "
   "consumers - they are quarantined, not retried forever."),
 "key_points": [
   "850 events/second across twelve partitions; seventy-two-hour retention.",
   "Transport, topic layout, and partition keying recorded.",
   "Event schemas evolve append-only - old consumers keep working.",
   "Consumer groups with durably checkpointed offsets - restarts resume.",
   "Sixty-second lag alert threshold per consumer group.",
   "Poison events quarantined to dead-letter, never retried forever.",
 ],
 "requirements": [
   "Throughput, partition count, and retention documented from the provider.",
   "Event schema versioned and stored.",
   "Consumer-group assignments and offset storage documented.",
   "Dead-letter policy written and tested.",
 ],
 "standards": [
   "At-least-once delivery assumed; consumers idempotent.",
   "Ordered processing within a partition key; no global order assumed.",
   "Lag alerts owned with runbooks.",
   "Schema compatibility checked before any producer upgrade.",
 ],
 "citations": [
   "MQTT Version 5.0, OASIS Standard, 2019 (lightweight event transport).",
   "HTML Living Standard: Server-Sent Events (WHATWG).",
 ],
 "sig_lens": ("The Signature doctrine hears an event stream as a river: it cannot be dammed, only "
   "channeled, and the Signature connector is a mill built beside it - positioned deliberately, "
   "maintained constantly, never surprised when the water keeps coming."),
},
{
 "name": "File Transfer Connector Profile",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "demo_key": "d_sftp", "demo_data": {"files_per_day": 240, "avg_mb": 18, "checksum": "SHA-256", "window": "02:00-04:00 UTC"},
 "description": ("The file transfer connector profile records batch data movement: two hundred "
   "forty files a day, averaging eighteen megabytes, delivered over SFTP in a nightly window "
   "between 02:00 and 04:00 UTC. File transfer is the oldest integration pattern and still "
   "runs the world's payrolls, bank settlements, and insurance feeds. The profile covers the "
   "protocol (SFTP preferred, FTPS where required, never plain FTP), authentication (SSH keys, "
   "never passwords), file naming conventions, integrity checks via SHA-256 manifests, and the "
   "atomic-delivery pattern - files written with temporary names and renamed only when "
   "complete, so consumers never read a half-written file."),
 "how_it_works": ("The record names the protocol and the endpoints, the SSH key fingerprints in "
   "use, and the delivery window with timezone stated explicitly. Filenames follow a "
   "convention encoding date, sequence, and content type, validated on receipt. Integrity is "
   "verified against a SHA-256 manifest delivered alongside or computed by the sender; "
   "mismatches quarantine the file and alert. Delivery is atomic: the sender writes "
   "filename.tmp and renames to filename only when the transfer completes, and the consumer "
   "ignores .tmp files. The consumer tracks sequence numbers to detect missing files - a gap "
   "in the sequence is an incident, not a shrug - and archives processed files for the "
   "retention period."),
 "key_points": [
   "240 files/day, 18 MB average, nightly window 02:00-04:00 UTC.",
   "SFTP preferred; SSH keys, never passwords; plain FTP forbidden.",
   "SHA-256 manifests verify integrity; mismatches quarantine and alert.",
   "Atomic delivery: .tmp writes renamed only when complete.",
   "Sequence tracking - a missing file is an incident.",
   "Filenames encode date, sequence, and content type; validated on receipt.",
 ],
 "requirements": [
   "Protocol, endpoints, and key fingerprints documented.",
   "Filename convention and validation rules written.",
   "Integrity-check procedure and quarantine path tested.",
   "Delivery window with timezone and sequence monitoring in place.",
 ],
 "standards": [
   "SSH keys at least 2048-bit RSA or Ed25519.",
   "No plain FTP or unencrypted transfer, ever.",
   "Retention of processed files per data policy.",
   "Key rotation on the same schedule as API credentials.",
 ],
 "citations": [
   "RFC 4253: The Secure Shell (SSH) Transport Layer Protocol. Ylonen and Lonvick, Eds., 2006.",
   "NIST Special Publication 800-63B (authenticator assurance for key-based auth).",
 ],
 "sig_lens": ("The Signature edition treats batch files as sealed parcels: the manifest is the "
   "wax seal, the atomic rename is the unbroken ribbon, and the sequence check is the "
   "inventory. The Signature doctrine holds that a missing parcel is reported the morning it "
   "is missed - not discovered at month-end."),
},
{
 "name": "Connector Response Caching",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "demo_key": "d_cache", "demo_data": {"ttl_s": 300, "hit_rate": 0.72, "calls_per_day": 48000, "saved_calls": 34560},
 "description": ("The connector caching record states what the system remembers instead of "
   "re-asking: cacheable endpoints, time-to-live values, and the measured hit rate. With "
   "forty-eight thousand calls a day and a seventy-two percent hit rate, the cache absorbs "
   "thirty-four thousand five hundred sixty calls - quota not spent, latency not incurred, "
   "money not paid. Caching is also where staleness breeds, so the record is strict about "
   "what may be cached: idempotent reads with explicit TTLs, never authenticated personal "
   "data shared across users, never anything the provider marks no-store."),
 "how_it_works": ("The record lists each cacheable endpoint family with its TTL - three hundred "
   "seconds default, shorter for volatile data, longer for reference data - and the cache key "
   "composition: endpoint plus sorted parameters plus API version, never including "
   "credentials. Hit rate is measured and reported (0.72 in the example); a falling hit rate "
   "triggers review because it means the cache is misconfigured or the data changed shape. "
   "Invalidation rules are explicit: TTL expiry, explicit purge on webhook notifications of "
   "change, and manual purge tooling for incidents. Negative caching (remembering 404s briefly) "
   "is used where the provider documents stable absence, with short TTLs. Cache stampedes are "
   "prevented with request coalescing - one in-flight request per key."),
 "key_points": [
   "72% hit rate on 48,000 calls/day absorbs 34,560 calls.",
   "TTL per endpoint family: 300 seconds default, tuned by volatility.",
   "Cache keys: endpoint + sorted params + version - never credentials.",
   "Invalidation explicit: TTL, webhook-driven purge, manual purge tooling.",
   "No caching of personal data across users or no-store responses.",
   "Request coalescing prevents cache stampedes.",
 ],
 "requirements": [
   "Cacheable endpoints with TTLs documented.",
   "Hit rate measured and reviewed; drops investigated.",
   "Invalidation procedures written and tested.",
   "Purge tooling available to on-call.",
 ],
 "standards": [
   "Honor provider Cache-Control directives where sent.",
   "Personal data never shared across users in cache.",
   "Negative caching only with short TTLs and provider documentation.",
   "Cache size bounded with eviction policy stated.",
 ],
 "citations": [
   "RFC 7234: Hypertext Transfer Protocol (HTTP/1.1): Caching. Fielding, Nottingham, and Reschke, 2014.",
 ],
 "sig_lens": ("The Signature doctrine treats a cache as institutional memory: valuable, fallible, "
   "and in need of scheduled forgetting. The Signature edition requires every cached fact to "
   "carry its expiry like a milk carton carries its date - memory without a date is just rumor."),
},
# ---------------- Advanced (22-34) ----------------
{
 "name": "Failover and Circuit Breaking",
 "group": "Advanced", "ladder_rank": 22, "ladder_tier": "advanced",
 "demo_key": "d_circuit", "demo_data": {"failure_threshold": 5, "window_s": 60, "open_s": 30, "half_open_probes": 3, "states": ["closed","open","half-open"]},
 "description": ("The failover and circuit breaking record specifies how a connector stops hurting "
   "a sick provider and itself: after five failures in sixty seconds the circuit opens, calls "
   "fail fast for thirty seconds instead of piling onto the outage, then three probe calls in "
   "half-open state test whether the provider has recovered. Without a breaker, a dead "
   "provider turns every caller into a hammer - thousands of doomed requests consuming threads, "
   "timeouts, and money while the provider is down. The record also covers true failover: where "
   "a secondary provider or a cached/degraded mode exists, the conditions for switching and the "
   "conditions for switching back."),
 "how_it_works": ("The record sets the breaker parameters: five consecutive failures (or a fifty "
   "percent failure rate over the window) trips the circuit open for thirty seconds; during "
   "open state, calls fail immediately with a cached last-known-good response or a declared "
   "degraded answer where one exists. After the open interval, the breaker admits three probe "
   "calls - half-open state - and closes only if they succeed; a single probe failure re-opens "
   "for another thirty seconds. Failover targets are listed in priority order with their own "
   "registry records, and the switch-back rule is explicit: primary must pass probes for five "
   "continuous minutes before traffic returns. Every state transition is logged and alerted, "
   "because a flapping breaker is itself an incident."),
 "key_points": [
   "Five failures in sixty seconds opens the circuit; fail fast for thirty seconds.",
   "Half-open probes: three test calls decide whether the provider recovered.",
   "Open breakers serve cached last-known-good or declared degraded answers.",
   "Failover targets listed in priority order with switch-back rules.",
   "Switch-back requires five continuous minutes of healthy probes.",
   "Every state transition logged and alerted - flapping is an incident.",
 ],
 "requirements": [
   "Breaker thresholds, windows, and probe counts documented per connector.",
   "Degraded-mode answers declared in advance, not improvised during outages.",
   "Failover targets registered with their own records.",
   "Breaker behavior tested with fault injection, not just hoped for.",
 ],
 "standards": [
   "Breakers on every production connector - no exceptions.",
   "Fail-fast responses must be safe: never fail open on money or safety.",
   "Recovery proven by probes before traffic returns.",
   "Breaker metrics (trips, duration, probes) on the operations dashboard.",
 ],
 "citations": [
   "Nygard, M. T. Release It! Design and Deploy Production-Ready Software. Pragmatic Bookshelf, 2nd ed., 2018 (circuit breaker pattern).",
 ],
 "sig_lens": ("The Signature doctrine treats the circuit breaker as triage discipline: when the "
   "provider is wounded, the Signature connector stops demanding answers and protects the "
   "patient - the system itself - from the stampede of its own retries. Mercy, in distributed "
   "systems, is a configuration value."),
},
{
 "name": "Connector SLA Tracking",
 "group": "Advanced", "ladder_rank": 23, "ladder_tier": "advanced",
 "demo_key": "d_sla", "demo_data": {"target": 99.9, "measured": 99.94, "breach_min": 0, "credits": 0, "period": "2026-09"},
 "description": ("The SLA tracking record turns provider promises into monthly arithmetic: the "
   "target was 99.9%, the probes measured 99.94%, zero breach minutes, zero credits owed, for "
   "September 2026. Service-level agreements are only as real as their measurement, and "
   "provider-reported uptime is marketing until verified by independent probes. The record "
   "defines the SLA terms that matter - what counts as downtime, what is excluded "
   "(scheduled maintenance, force majeure), how credits are claimed and their deadlines - and "
   "keeps the monthly scorecard that makes the contract enforceable."),
 "how_it_works": ("Each month the record computes uptime from the probe timeline: successful "
   "probes divided by total probes, with degraded periods counted per the contract's "
   "definition. The September 2026 example shows 99.94% against a 99.9% target - no breach, no "
   "credits. When measured uptime falls below target, the record documents the breach minutes, "
   "the credit tier the contract specifies (commonly ten percent of the monthly fee per "
   "percentage point), and the claim deadline - many contracts require claims within thirty "
   "days, after which the money is gone. Exclusions are applied exactly as written: the "
   "provider's declared maintenance windows are excluded only if they were announced per the "
   "contract's notice terms. The scorecard is shared with procurement quarterly."),
 "key_points": [
   "Monthly arithmetic: target vs independently measured uptime, breach minutes, credits.",
   "Example: 99.94% measured vs 99.9% target - no breach, September 2026.",
   "Provider-reported uptime is unverified until probes confirm it.",
   "Credit tiers and claim deadlines recorded - many expire in thirty days.",
   "Exclusions applied exactly as the contract writes them.",
   "Scorecard shared with procurement quarterly.",
 ],
 "requirements": [
   "SLA terms extracted from the contract: definition, exclusions, credits, deadlines.",
   "Independent probe data retained for the claim window plus margin.",
   "Monthly scorecard computed and filed.",
   "Breach claims filed before deadlines.",
 ],
 "standards": [
   "Measurement by independent probes, not provider dashboards.",
   "Downtime definition matches the contract word for word.",
   "Scorecards retained for the contract term plus one year.",
   "Procurement owns the commercial relationship; engineering owns the measurement.",
 ],
 "citations": [
   "Google Site Reliability Engineering, Chapter 4: Service Level Objectives. Beyer et al., O'Reilly, 2016.",
 ],
 "sig_lens": ("The Signature edition treats the SLA scorecard as a ledger of promises kept or "
   "broken, settled monthly like any honest account. The Signature doctrine insists the "
   "ledger be kept by the promisee's own hand - a merchant who grades his own deliveries "
   "will always pass."),
},
{
 "name": "Connector Cost Metering",
 "group": "Advanced", "ladder_rank": 24, "ladder_tier": "advanced",
 "demo_key": "d_cost", "demo_data": {"per_1k": 1.5, "calls_month": 2400000, "monthly": 3600.0, "budget": 5000.0, "alert_at": 0.8},
 "description": ("The connector cost metering record answers 'what does this API cost us' with a "
   "number: two million four hundred thousand calls at one dollar fifty per thousand is three "
   "thousand six hundred dollars a month against a five-thousand-dollar budget, with an alert "
   "at eighty percent. External APIs are metered utilities - AI inference, maps, messaging, "
   "payments all bill per call - and unmetered usage grows until the invoice arrives. The "
   "record captures the pricing model (per call, per thousand, per token, tiered volume), the "
   "current burn rate, the budget, and the alert threshold, so cost is managed continuously "
   "instead of discovered quarterly."),
 "how_it_works": ("The record states the provider's unit price and pricing dimensions - the "
   "example uses $1.50 per thousand calls - plus tier breaks where volume discounts apply and "
   "which dimensions are billed (requests, tokens, data transfer, seats). Metering counts "
   "actual billed units from provider usage APIs or invoice reconciliation, not estimates, and "
   "computes the monthly run rate: 2,400,000 calls times $0.0015 equals $3,600. The budget "
   "($5,000) and alert threshold (eighty percent, i.e., $4,000) drive notifications; a second "
   "alert at one hundred percent triggers a cost review with the owning team. Unit cost trends "
   "are tracked because providers raise prices and usage patterns drift - a rising cost per "
   "business transaction is the signal that matters, not just the total."),
 "key_points": [
   "2.4M calls at $1.50/1k = $3,600/month against a $5,000 budget.",
   "Alert at eighty percent ($4,000); review triggered at one hundred percent.",
   "Pricing dimensions recorded: requests, tokens, transfer, seats, tiers.",
   "Metered from provider usage data, not estimated.",
   "Cost per business transaction tracked - the signal that matters.",
   "Volume tier breaks modeled so growth pricing is predictable.",
 ],
 "requirements": [
   "Provider pricing captured with tiers and billing dimensions.",
   "Monthly run rate computed from actual usage.",
   "Budget and alert thresholds set per connector.",
   "Invoice reconciliation performed monthly.",
 ],
 "standards": [
   "Costs attributed to owning teams (showback at minimum).",
   "Anomaly alerts on unexpected burn-rate changes.",
   "Price-change notices from providers recorded on receipt.",
   "Annual pricing review against alternative providers.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (cloud and API cost management practice).",
 ],
 "sig_lens": ("The Signature doctrine treats metered APIs as utilities with the meter on the "
   "wall: the Signature connector reads its own meter daily, because a bill should never "
   "contain a surprise. The Signature edition requires every connector to know its cost per "
   "business transaction - a service that cannot price its own work cannot govern it."),
},
{
 "name": "Connector Security Audit",
 "group": "Advanced", "ladder_rank": 25, "ladder_tier": "advanced",
 "demo_key": "d_secaudit", "demo_data": {"checks": 18, "passed": 16, "failed": 2, "critical": 0, "next_audit": "2027-01-15"},
 "description": ("The connector security audit record is the periodic adversarial review of a "
   "connector: eighteen checks, sixteen passed, two failed, zero critical, next audit "
   "2027-01-15. Connectors are trust boundaries - credentials cross them, customer data "
   "crosses them, money crosses them - which makes them attractive targets. The audit checks "
   "credential storage, transport security, scope minimality, input validation, output "
   "encoding, secret rotation compliance, webhook verification, dependency freshness, and "
   "incident history. Findings are graded critical, high, medium, low, with remediation "
   "deadlines: critical findings stop new deployments until fixed."),
 "how_it_works": ("The audit runs against the eighteen-point checklist: secrets in the vault (not "
   "in code or logs), TLS 1.2+ on all traffic, certificate validation enabled, OAuth scopes "
   "minimal, webhook signatures verified with constant-time comparison, API keys rotated on "
   "schedule, request/response validation on untrusted provider data, PII redaction in logs, "
   "rate limiting enforced client-side, retry budgets bounded, error messages free of secrets, "
   "dependencies patched, provider security advisories reviewed, incident history examined, "
   "access logs reviewed, data retention honored, deprecation status current, and documentation "
   "accurate. The example shows sixteen passed and two failed (non-critical), each failure "
   "with an owner and a thirty-day remediation date. Critical findings - exposed secrets, "
   "disabled certificate validation - halt deployments until resolved and verified."),
 "key_points": [
   "Eighteen-point checklist; example: 16 passed, 2 failed, 0 critical.",
   "Connectors are trust boundaries: credentials, customer data, and money cross them.",
   "Critical findings halt deployments until fixed and verified.",
   "Failed findings get owners and thirty-day remediation dates.",
   "Next audit date set (2027-01-15) - audits are recurring, not one-time.",
   "Provider security advisories reviewed as part of every audit.",
 ],
 "requirements": [
   "Audit checklist completed per connector on schedule.",
   "Findings graded with owners and remediation dates.",
   "Critical findings trigger deployment freeze until resolved.",
   "Next audit date scheduled before the current audit closes.",
 ],
 "standards": [
   "Annual audits minimum; high-risk connectors audited semi-annually.",
   "Audits performed by someone other than the connector's owner.",
   "Evidence retained for each check - assertions without evidence fail.",
   "Remediation verified by re-test, not by promise.",
 ],
 "citations": [
   "NIST Special Publication 800-53, controls CA-7 (continuous monitoring) and SI-4 (monitoring).",
   "OWASP API Security Top 10 (2023) (adversarial checklist reference).",
 ],
 "sig_lens": ("The Signature doctrine treats the security audit as a trial by a skeptical friend: "
   "the auditor's job is to break the connector's trust assumptions before an attacker does. "
   "The Signature edition requires the auditor to be someone other than the builder - a "
   "covenant witnessed only by its maker is not witnessed at all."),
},
{
 "name": "Connector Change Management",
 "group": "Advanced", "ladder_rank": 26, "ladder_tier": "advanced",
 "demo_key": "d_change", "demo_data": {"changes_ytd": 23, "breaking": 4, "rollback_tested": True, "lead_days": 14, "window": "Tue 10:00 UTC"},
 "description": ("The connector change management record governs how connector configurations "
   "evolve: twenty-three changes year-to-date, four of them breaking, every one rollback-"
   "tested, with a fourteen-day lead time and a Tuesday 10:00 UTC change window. Connector "
   "changes - new endpoints, credential rotations, version migrations, timeout tuning - are "
   "production changes to a dependency the system does not control, which makes them riskier "
   "than ordinary deploys. The record requires each change to state its blast radius, its "
   "rollback plan, and its verification method before it ships."),
 "how_it_works": ("Changes are proposed with a template: what is changing, why, the blast radius "
   "(which callers and volumes are affected), the rollback plan (exact steps, tested - the "
   "example notes rollback tested true), and the verification method (which dashboard or probe "
   "proves success). Non-breaking changes ship in the weekly window, Tuesdays at 10:00 UTC "
   "when staffing is full; breaking changes get a fourteen-day lead with customer and "
   "stakeholder notice. Credential rotations use overlap windows. Version migrations follow the "
   "versioning record's cutover plan. Every change is logged with its outcome, and the "
   "year-to-date counts (23 changes, 4 breaking) feed the reliability review - a connector "
   "changing constantly is a connector that needs a stability conversation with its provider."),
 "key_points": [
   "23 changes year-to-date, 4 breaking - every change rollback-tested.",
   "Change template: what, why, blast radius, rollback plan, verification.",
   "Weekly window Tuesdays 10:00 UTC; breaking changes need fourteen-day lead.",
   "Credential rotations use overlap windows; migrations follow cutover plans.",
   "Change frequency feeds reliability review - churn is a signal.",
   "Rollback plans tested, not just written.",
 ],
 "requirements": [
   "Change template completed for every production connector change.",
   "Rollback plan tested before the change ships.",
   "Breaking changes announced with fourteen-day lead.",
   "Change log maintained with outcomes.",
 ],
 "standards": [
   "No unreviewed production connector changes.",
   "Changes outside the window require incident-commander approval.",
   "Verification method defined before shipping, checked after.",
   "Post-change monitoring for at least one full business cycle.",
 ],
 "citations": [
   "Google Site Reliability Engineering, Chapter 8: Release Engineering (change discipline). Beyer et al., O'Reilly, 2016.",
   "ITIL 4: Change Enablement practice (change governance reference). Axelos.",
 ],
 "sig_lens": ("The Signature doctrine treats each connector change as an amendment to a treaty: "
   "proposed in writing, reviewed by the affected, reversible by design. The Signature edition "
   "forbids the midnight improvisation - a treaty amended in the dark binds no one but the "
   "amender."),
},
{
 "name": "Connector Test Harness",
 "group": "Advanced", "ladder_rank": 27, "ladder_tier": "advanced",
 "demo_key": "d_harness", "demo_data": {"cases": 64, "pass": 61, "fail": 3, "sandbox": True, "contract_tests": 22},
 "description": ("The connector test harness record describes the automated proving ground for a "
   "connector: sixty-four test cases, sixty-one passing, three failing, running against the "
   "provider's sandbox, including twenty-two contract tests. The harness proves the connector "
   "behaves as the registry claims - authentication works, pagination terminates, retries "
   "back off, errors classify correctly, webhooks verify - before production traffic depends "
   "on it. Contract tests are the core: recorded request/response pairs replayed against the "
   "provider to detect the day the provider changes something without telling anyone."),
 "how_it_works": ("The harness runs in three tiers. Unit tests verify the connector's internal "
   "logic - bucket math, backoff series, signature computation - with no network. Contract "
   "tests (twenty-two in the example) replay recorded fixtures against the provider's sandbox "
   "and diff the responses against expectations, catching undocumented provider changes. "
   "Failure-injection tests simulate 429s, 503s, timeouts, and malformed responses to prove "
   "the retry, breaker, and error-classification behavior. The suite runs on every connector "
   "change and nightly against the sandbox; the three failing cases in the example are "
   "tracked like bugs with owners, not ignored. Sandbox credentials are scoped and rotated, "
   "and the harness never touches production - proving behavior must not create real charges."),
 "key_points": [
   "64 cases, 61 passing, 3 failing (tracked as bugs) - against the provider sandbox.",
   "Three tiers: unit logic, contract tests, failure injection.",
   "22 contract tests replay fixtures to catch undocumented provider changes.",
   "Failure injection proves retry, breaker, and classification behavior.",
   "Runs on every change and nightly; failures tracked, never ignored.",
   "Sandbox only - tests must not create real charges.",
 ],
 "requirements": [
   "Harness covering auth, pagination, retry, errors, webhooks per connector.",
   "Contract tests with recorded fixtures.",
   "Failure-injection tests for 429/503/timeout/malformed responses.",
   "Nightly sandbox runs with tracked failures.",
 ],
 "standards": [
   "No production traffic from tests, ever.",
   "Fixtures refreshed when the provider versions its API.",
   "Failing tests block connector changes until fixed or waived with expiry.",
   "Sandbox credentials scoped minimally and rotated.",
 ],
 "citations": [
   "Pact contract testing documentation (consumer-driven contract pattern).",
   "Nygard, M. T. Release It!, 2nd ed. (failure-injection discipline).",
 ],
 "sig_lens": ("The Signature edition treats the test harness as the connector's sparring partner: "
   "it hits the connector with everything the real world might - rate limits, outages, "
   "garbage responses - in a room where no one gets hurt. The Signature doctrine holds that a "
   "connector untested against failure is a promise untested against reality."),
},
{
 "name": "Connector Documentation Standard",
 "group": "Advanced", "ladder_rank": 28, "ladder_tier": "advanced",
 "demo_key": "d_docs", "demo_data": {"sections": 9, "examples": 14, "stale_days": 16, "reviewed": "2026-10-01"},
 "description": ("The connector documentation standard defines what 'documented' means for a "
   "connector: nine required sections, fourteen working examples, sixteen days stale, last "
   "reviewed 2026-10-01. Documentation is the connector's user manual for the engineers who "
   "will debug it at 3 AM - which means it must answer 'what does this do, how do I call it, "
   "what can go wrong, and who do I call' without requiring anyone to read the source. The "
   "standard requires every example to be executed against the sandbox during review, because "
   "an untested example is fiction."),
 "how_it_works": ("The nine sections are: overview and ownership, authentication setup, endpoint "
   "reference, request/response examples, error catalog, rate limits and quotas, webhook "
   "handling, troubleshooting runbook, and change history. The fourteen examples cover the "
   "happy path, pagination, retries, error cases, and webhook verification - each executed "
   "against the sandbox at review time, with outputs captured. Staleness is measured: days "
   "since last review, with the example at zero because it was reviewed 2026-10-01. "
   "Documentation lives beside the registry record and is reviewed on the same ninety-day "
   "cadence; a connector whose docs are stale is flagged the same as one whose review is "
   "overdue. The troubleshooting runbook names the exact dashboards, log queries, and "
   "escalation contacts for the common failures."),
 "key_points": [
   "Nine required sections; fourteen working examples; sixteen days stale (reviewed 2026-10-01).",
   "Answers: what it does, how to call it, what can go wrong, who to call.",
   "Every example executed against the sandbox at review - untested examples are fiction.",
   "Troubleshooting runbook with dashboards, log queries, escalation contacts.",
   "Docs reviewed on the ninety-day cadence alongside the registry record.",
   "Stale documentation flagged like an overdue review.",
 ],
 "requirements": [
   "All nine sections complete per connector.",
   "Examples executed at review with captured outputs.",
   "Runbook with concrete dashboards, queries, and contacts.",
   "Review date current within the cadence.",
 ],
 "standards": [
   "Documentation versioned with the connector configuration.",
   "Examples in the consumer's language with copy-pasteable form.",
   "No screenshots of text that could be code blocks.",
   "Change history section updated with every connector change.",
 ],
 "citations": [
   "Google developer documentation style guide (technical writing practice).",
   "Diataxis documentation framework (tutorial/howto/reference/explanation structure).",
 ],
 "sig_lens": ("The Signature doctrine holds that documentation is a promise to a future "
   "stranger - the engineer who inherits the connector. The Signature edition requires that "
   "promise to be tested: every example proven working, every runbook step proven reachable. "
   "An untested manual is a map drawn from imagination."),
},
{
 "name": "Multi-Tenant Connector Design",
 "group": "Advanced", "ladder_rank": 29, "ladder_tier": "advanced",
 "demo_key": "d_multitenant", "demo_data": {"tenants": 140, "isolation": "per-tenant credentials", "quota_share": "fair", "noisy_neighbor_guards": True},
 "description": ("The multi-tenant connector design record states how one connector serves one "
   "hundred forty tenants without letting them interfere: per-tenant credentials, fair quota "
   "sharing, and noisy-neighbor guards. When many customers share one provider account - or "
   "one connector serves many provider accounts - the failure modes multiply: one tenant's "
   "runaway job burns the shared quota, one tenant's data leaks into another's logs, one "
   "tenant's misconfigured webhook floods the shared endpoint. The record designs these away "
   "with isolation at the credential level, quota partitioning, and per-tenant observability."),
 "how_it_works": ("Each of the 140 tenants gets its own credential set - separate API keys or "
   "OAuth grants - so revoking one tenant never affects the others and usage meters per "
   "tenant. The shared provider quota is partitioned fairly: each tenant gets a guaranteed "
   "floor plus a share of burst capacity, enforced by per-tenant token buckets in front of the "
   "shared limiter. Noisy-neighbor guards cap any single tenant at a fraction of total "
   "throughput and shed its excess load first. Telemetry is tagged per tenant so a spike is "
   "attributable in seconds, and logs are partitioned so tenant data never mingles. Webhook "
   "endpoints are per-tenant or carry tenant identifiers verified against the credential, "
   "never trusted from the payload alone."),
 "key_points": [
   "140 tenants, each with its own credential set - revocation is per-tenant.",
   "Quota partitioned: guaranteed floor per tenant plus shared burst.",
   "Per-tenant token buckets in front of the shared limiter.",
   "Noisy-neighbor guards shed the offender's excess load first.",
   "Telemetry and logs partitioned per tenant - spikes attributable in seconds.",
   "Webhook tenant identity verified against credentials, never from payload alone.",
 ],
 "requirements": [
   "Per-tenant credentials with independent revocation.",
   "Quota partition policy documented and enforced.",
   "Per-tenant telemetry tagging.",
   "Tenant data isolation verified in logs and caches.",
 ],
 "standards": [
   "No cross-tenant credential sharing, ever.",
   "One tenant's failure must not cascade to others (bulkhead).",
   "Tenant offboarding revokes credentials and purges cached data.",
   "Fair-share algorithm documented and auditable.",
 ],
 "citations": [
   "Nygard, M. T. Release It!, 2nd ed. (bulkhead pattern for isolation).",
   "NIST Special Publication 800-53, control SC-7 (boundary protection).",
 ],
 "sig_lens": ("The Signature doctrine treats multi-tenancy as a covenant with each tenant "
   "individually: the Signature connector promises every tenant that its neighbors cannot "
   "spend its quota, read its data, or break its service. Bulkheads are not an optimization - "
   "they are the walls between promises."),
},
{
 "name": "Connector Deprecation and Migration",
 "group": "Advanced", "ladder_rank": 30, "ladder_tier": "advanced",
 "demo_key": "d_deprecate", "demo_data": {"deprecated": 3, "migrated": 2, "remaining": 1, "sunset": "2027-03-31", "cutover": "2027-02-28"},
 "description": ("The connector deprecation and migration record tracks the end of life of "
   "provider versions: three connectors deprecated, two migrated, one remaining, with sunset "
   "2027-03-31 and the cutover set a month earlier on 2027-02-28. Deprecation is the phase "
   "where the provider has announced the end but the old version still answers - the "
   "dangerous comfortable middle where migration feels optional until the sunset morning "
   "arrives. The record lists every connector on a deprecated version, its migration owner, "
   "its test status against the new version, and its cutover date, so the remaining one is a "
   "managed task, not a surprise."),
 "how_it_works": ("When a provider announces deprecation, each affected connector gets a "
   "migration entry within one week: the old and new versions, the breaking changes affecting "
   "this connector, the owner, and the cutover date - set at least thirty days before sunset "
   "(the example uses a full month: cutover 2027-02-28, sunset 2027-03-31). Migration testing "
   "runs the connector's test harness against the new version in sandbox; parity checks "
   "compare old-version and new-version outputs on real traffic shadows. Cutover flips "
   "production in the change window with rollback ready; the old version stays configured for "
   "one week as the emergency fallback. After sunset passes with the migration complete, the "
   "record is archived - kept for the audit trail, not the active registry."),
 "key_points": [
   "3 deprecated, 2 migrated, 1 remaining - tracked as tasks, not surprises.",
   "Migration entry created within one week of the provider's announcement.",
   "Cutover at least thirty days before sunset (example: one full month).",
   "Sandbox parity checks compare old vs new outputs on shadowed traffic.",
   "Old version kept one week post-cutover as emergency fallback.",
   "Archived after sunset - kept for audit, not the active registry.",
 ],
 "requirements": [
   "Deprecation announced to owners within one week.",
   "Migration entries with owner, breaking changes, and cutover date.",
   "Sandbox testing against the new version completed.",
   "Cutover executed in the change window with rollback ready.",
 ],
 "standards": [
   "No connector left on a version past its sunset date.",
   "Shadow-traffic parity for behavior-critical migrations.",
   "Post-sunset verification that the old version is truly dead.",
   "Lessons recorded: what the provider changed and what it cost.",
 ],
 "citations": [
   "OpenAPI Specification v3.1.0 (versioned contracts for migration planning).",
   "Google Site Reliability Engineering, Chapter 8: Release Engineering (migration discipline).",
 ],
 "sig_lens": ("The Signature doctrine treats deprecation as a dignified retirement: the old "
   "connector served well, its replacement is proven before the handover, and nothing is "
   "abandoned to die unmourned on a sunset morning. The Signature edition requires the "
   "farewell to be planned - endings, like beginnings, are governed."),
},
{
 "name": "PII Redaction in Connectors",
 "group": "Advanced", "ladder_rank": 31, "ladder_tier": "advanced",
 "demo_key": "d_redact", "demo_data": {"patterns": 6, "redacted_per_day": 18200, "leaks_found": 0, "fields": ["email","phone","card","ssn","token","password"]},
 "description": ("The PII redaction record states how a connector keeps personal data out of "
   "places it does not belong: six field patterns redacted, eighteen thousand two hundred "
   "values masked per day, zero leaks found in the last audit. Connectors constantly handle "
   "names, emails, phone numbers, payment tokens, and credentials - and every one of those "
   "that lands in a log file, an error report, or a dashboard becomes a breach surface. The "
   "record defines the redaction patterns, where redaction is applied (at the logging layer, "
   "before persistence), and how leaks are hunted: automated scans of logs and telemetry for "
   "unredacted patterns, with findings treated as incidents."),
 "how_it_works": ("Six patterns are redacted: email addresses, phone numbers, payment card "
   "numbers, national ID numbers, authentication tokens, and passwords - each matched by a "
   "tested regular expression applied at the logging layer before any line is written. "
   "Structured logging carries a per-field sensitivity tag so the logger knows what to mask "
   "without guessing from content. Eighteen thousand two hundred values a day are masked in "
   "the example fleet - proof the redaction is load-bearing, not decorative. Weekly automated "
   "scans search stored logs for the patterns; the example shows zero leaks found. Any leak "
   "found triggers the incident process: scope the exposure, purge the data, fix the pattern, "
   "and re-scan history. Error reports to providers strip PII before leaving the building - "
   "a stack trace with a customer's email is a disclosure."),
 "key_points": [
   "Six patterns redacted at the logging layer, before persistence.",
   "18,200 values masked per day - load-bearing, not decorative.",
   "Per-field sensitivity tags in structured logs - no guessing from content.",
   "Weekly automated scans of stored logs; zero leaks in the example.",
   "Leaks are incidents: scope, purge, fix the pattern, re-scan history.",
   "Error reports to providers stripped of PII before leaving.",
 ],
 "requirements": [
   "Redaction patterns documented and tested with synthetic PII.",
   "Redaction applied before persistence, not after.",
   "Automated leak scans scheduled with owned findings.",
   "Provider-bound error reports reviewed for PII.",
 ],
 "standards": [
   "No PII in logs, metrics labels, or error messages - ever.",
   "Patterns reviewed when data models change.",
   "Scan history retained for audit.",
   "Minimization: connectors request and store only the PII the job needs.",
 ],
 "citations": [
   "NIST Special Publication 800-122, Guide to Protecting the Confidentiality of Personally Identifiable Information.",
   "OWASP Logging Cheat Sheet (sensitive data in logs).",
 ],
 "sig_lens": ("The Signature doctrine treats personal data as borrowed property: the connector "
   "is its temporary custodian, and a custodian who leaves valuables in the hallway has "
   "failed the trust. The Signature edition requires redaction to be structural - built into "
   "the logging layer - because discipline that depends on remembering always eventually "
   "forgets."),
},
{
 "name": "Connector Marketplace Governance",
 "group": "Advanced", "ladder_rank": 32, "ladder_tier": "advanced",
 "demo_key": "d_marketplace", "demo_data": {"listed": 47, "approved": 31, "pending": 9, "rejected": 7, "reviews_per_year": 2},
 "description": ("The connector marketplace governance record regulates the internal catalog where "
   "teams publish and discover connectors: forty-seven listed, thirty-one approved, nine "
   "pending review, seven rejected. Without governance, a marketplace becomes a junk drawer - "
   "five half-working Salesforce connectors, three abandoned by departed engineers, none "
   "trustworthy. The record sets the listing bar: a complete registry record, a passing test "
   "harness, current documentation, a named owner, and a security audit within the year. "
   "Listings are reviewed twice a year; stale or ownerless connectors are delisted, because a "
   "marketplace that lists what it cannot vouch for is a liability."),
 "how_it_works": ("Publishing a connector requires the full registry record, a green test "
   "harness, reviewed documentation, a named owner who accepts the oath, and a security audit "
   "no older than one year. A review board - rotating engineers from consuming teams - "
   "approves, requests changes, or rejects; the example shows seven rejections, which is "
   "healthy, not hostile. Approved connectors carry a trust badge with the audit date; "
   "consuming teams may use badged connectors without re-vetting. Twice-yearly reviews check "
   "that the owner still exists, the provider still exists, and the tests still pass - "
   "failures delist the connector until fixed. Usage metrics per listing show which "
   "connectors earn their keep and which are candidates for consolidation."),
 "key_points": [
   "47 listed: 31 approved, 9 pending, 7 rejected - rejection is healthy.",
   "Listing bar: registry record, green harness, docs, owner, audit within the year.",
   "Rotating review board from consuming teams approves listings.",
   "Trust badge with audit date - badged connectors need no re-vetting.",
   "Twice-yearly reviews; stale or ownerless connectors delisted.",
   "Usage metrics identify consolidation candidates.",
 ],
 "requirements": [
   "Publication checklist completed for every listing.",
   "Review board decision recorded with rationale.",
   "Trust badge dates current.",
   "Delisting process executed for failures.",
 ],
 "standards": [
   "No unbadged connector in production without a documented exception.",
   "Board membership rotates to prevent capture.",
   "Rejection rationales published - the bar must be legible.",
   "Duplicate connectors consolidated, not multiplied.",
 ],
 "citations": [
   "NIST Special Publication 800-53, control CM-14 (signed components) - provenance practice reference.",
 ],
 "sig_lens": ("The Signature edition treats the marketplace as a guild hall: a connector earns "
   "its place by proof, keeps it by maintenance, and loses it by neglect. The Signature "
   "doctrine holds that trust badges must be earned twice a year - trust, like bread, goes "
   "stale."),
},
{
 "name": "Federation Roster of Connectors",
 "group": "Advanced", "ladder_rank": 33, "ladder_tier": "advanced",
 "demo_key": "d_roster", "demo_data": {"members": 12, "shared": 8, "contracts": 8, "sync_h": 24, "divergent": 0},
 "description": ("The federation roster record coordinates connectors shared across organizational "
   "boundaries: twelve member organizations, eight shared connector contracts, synchronized "
   "every twenty-four hours, zero divergent. When multiple organizations use the same "
   "providers - a common pattern in federated systems - each maintaining its own connector "
   "profile wastes effort and diverges dangerously. The roster designates shared contracts: "
   "one canonical profile per provider, maintained by a designated steward, synchronized to "
   "members daily. Local extensions are allowed but must be declared, so a member's "
   "customization never silently contradicts the shared contract."),
 "how_it_works": ("The roster lists the twelve members, the eight shared contracts, and the "
   "steward organization for each contract. Stewards own the canonical profile - auth, limits, "
   "error maps, version tracking - and publish updates to the roster; members synchronize "
   "every twenty-four hours and report their sync status. The example shows zero divergent "
   "members, meaning all twelve run the current contract versions. Members may add local "
   "extensions (extra endpoints, custom timeouts) but must declare them in their local "
   "overlay, and overlays are validated against the shared contract on each sync. Breaking "
   "provider changes are coordinated: the steward announces, members acknowledge, and "
   "cutover happens on the shared schedule. A member that stops syncing is flagged - a silent "
   "member is a divergent member."),
 "key_points": [
   "12 members, 8 shared contracts, 24-hour sync, zero divergent.",
   "One canonical profile per provider, maintained by a designated steward.",
   "Local extensions allowed but declared - never silently contradicting.",
   "Overlays validated against the shared contract on every sync.",
   "Breaking changes coordinated on a shared cutover schedule.",
   "Silent members flagged - silence means divergence.",
 ],
 "requirements": [
   "Roster with members, contracts, and stewards documented.",
   "Sync cadence defined and sync status reported.",
   "Local overlays declared and validated.",
   "Coordinated cutover process for breaking changes.",
 ],
 "standards": [
   "Shared contracts versioned like any API contract.",
   "Steward rotation or succession planned - no single point of stewardship.",
   "Divergence measured and reported, not assumed absent.",
   "Members acknowledge breaking-change announcements explicitly.",
 ],
 "citations": [
   "NIST Special Publication 800-53, control CA-7 (continuous monitoring) - shared situational awareness reference.",
 ],
 "sig_lens": ("The Signature doctrine treats a federated roster as an alliance of covenant-"
   "keepers: each member swears the same profile, the steward keeps the canonical text, and "
   "divergence is desertion. The Signature edition requires the daily sync to be a roll call - "
   "every member answers, every day."),
},
{
 "name": "Registry Self-Audit and Mastery Record",
 "group": "Advanced", "ladder_rank": 34, "ladder_tier": "advanced",
 "demo_key": "d_mastery", "demo_data": {"records": 34, "complete": 34, "stale": 0, "ownerless": 0, "coverage": 1.0},
 "description": ("The registry self-audit and mastery record proves the registry governs itself: "
   "thirty-four connector archetypes catalogued, thirty-four complete, zero stale, zero "
   "ownerless, coverage one hundred percent. This is the record that closes the loop - the "
   "registry inspecting the registry. It verifies that every connector record has an owner, "
   "a current review date, a complete field set, a green test harness, and current "
   "documentation. It measures what the registry promised in its first record: no ungoverned "
   "dependencies, no expired reviews, no silent drift. A registry that cannot audit itself "
   "cannot govern anything else."),
 "how_it_works": ("The self-audit runs the registry's own rules against every record: field "
   "completeness (all twelve required fields present), owner assigned and still employed, "
   "review date within ninety days, test harness green within the week, documentation review "
   "current, security audit within the year, cost metering active, and SLA tracking current. "
   "The example scores thirty-four of thirty-four complete with zero stale and zero "
   "ownerless - coverage 1.0. Gaps become findings with owners and dates, tracked like any "
   "audit finding. The audit runs quarterly and its report goes to engineering leadership, "
   "because registry health is infrastructure health. This record also serves as the mastery "
   "checkpoint for the whole database: a reader who understands all thirty-four records - "
   "from the registry overview through profiles, behaviors, and advanced governance - "
   "understands external API connector governance end to end."),
 "key_points": [
   "34 archetypes catalogued, 34 complete, 0 stale, 0 ownerless - coverage 1.0.",
   "Self-audit checks: completeness, ownership, review currency, harness, docs, security, cost, SLA.",
   "Gaps become findings with owners and dates.",
   "Runs quarterly; report goes to engineering leadership.",
   "Registry health is infrastructure health.",
   "Mastery checkpoint: all 34 records together teach connector governance end to end.",
 ],
 "requirements": [
   "Self-audit executed quarterly with filed report.",
   "Every record scored on all eight dimensions.",
   "Findings tracked to closure.",
   "Mastery path documented from record 1 to record 34.",
 ],
 "standards": [
   "Coverage target 1.0 - every production connector governed.",
   "Zero ownerless records tolerated.",
   "Audit performed by someone outside the registry's daily operation.",
   "Year-over-year trend reported, not just the snapshot.",
 ],
 "citations": [
   "NIST Special Publication 800-53, control CA-7 (continuous monitoring).",
   "Google Site Reliability Engineering, Chapter 4: Service Level Objectives. Beyer et al., O'Reilly, 2016.",
 ],
 "sig_lens": ("The Signature edition closes the doctrine where it began: a covenant ledger that "
   "cannot account for itself accounts for nothing. The Signature self-audit is the registry "
   "swearing its own oath - complete, current, and owned - and the mastery record is the proof "
   "that the whole teaching holds together, simple to complex, without a gap."),
},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks) == list(range(1, 35)), "ladder ranks must be 1..34 in order"
