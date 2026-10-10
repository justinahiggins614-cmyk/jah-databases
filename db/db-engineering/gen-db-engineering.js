(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
var CATS=['schemas','queries','indexing','transactions','nosql'];
var PREFIX='JAH-DBE-';
var SQLKW=/SELECT|INSERT|UPDATE|DELETE|CREATE|EXPLAIN|WITH|BEGIN|COMMIT|ALTER|DROP/i;

var T=[
{cat:'schemas',topic:'blog schema',t:'Blog schema — posts, authors, comments',
 d:'A normalized blog schema: authors own posts, comments hang off posts, tags link through a junction table. Foreign keys enforce the relationships; the junction table keeps the many-to-many clean.',
 ddl:'CREATE TABLE authors(id INTEGER PRIMARY KEY, name TEXT NOT NULL);\nCREATE TABLE posts(id INTEGER PRIMARY KEY, author_id INTEGER NOT NULL REFERENCES authors(id), title TEXT NOT NULL, body TEXT, published_at TEXT);\nCREATE TABLE tags(id INTEGER PRIMARY KEY, label TEXT UNIQUE NOT NULL);\nCREATE TABLE post_tags(post_id INTEGER NOT NULL REFERENCES posts(id), tag_id INTEGER NOT NULL REFERENCES tags(id), PRIMARY KEY(post_id, tag_id));\nCREATE TABLE comments(id INTEGER PRIMARY KEY, post_id INTEGER NOT NULL REFERENCES posts(id), body TEXT NOT NULL);',
 qs:[['SELECT p.title, a.name FROM posts p JOIN authors a ON a.id=p.author_id ORDER BY p.published_at DESC LIMIT 10;','Latest posts with author names.'],['SELECT t.label, COUNT(*) FROM post_tags pt JOIN tags t ON t.id=pt.tag_id GROUP BY t.label ORDER BY 2 DESC;','Tag popularity ranking.']],
 perf:'Index posts(author_id) and comments(post_id); the junction table\'s composite PK covers both join directions. Full-text search wants a dedicated index, not LIKE \'%x%\'.',
 pit:'N+1 queries when hydrating posts with authors and tags — fetch with joins or batched loads.'},
{cat:'schemas',topic:'e-commerce orders',t:'E-commerce schema — orders and line items',
 d:'Orders header plus line items: the header holds totals and status, items hold per-product rows. Totals are stored but recomputable — the items are the source of truth.',
 ddl:'CREATE TABLE customers(id INTEGER PRIMARY KEY, email TEXT UNIQUE NOT NULL);\nCREATE TABLE products(id INTEGER PRIMARY KEY, sku TEXT UNIQUE NOT NULL, price_cents INTEGER NOT NULL);\nCREATE TABLE orders(id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL REFERENCES customers(id), status TEXT NOT NULL, total_cents INTEGER NOT NULL, placed_at TEXT NOT NULL);\nCREATE TABLE order_items(order_id INTEGER NOT NULL REFERENCES orders(id), product_id INTEGER NOT NULL REFERENCES products(id), qty INTEGER NOT NULL, price_cents INTEGER NOT NULL, PRIMARY KEY(order_id, product_id));',
 qs:[['SELECT o.id, SUM(i.qty*i.price_cents) AS computed FROM orders o JOIN order_items i ON i.order_id=o.id GROUP BY o.id HAVING computed != o.total_cents;','Find orders whose stored total disagrees with line items.'],['SELECT p.sku, SUM(i.qty) FROM order_items i JOIN products p ON p.id=i.product_id GROUP BY p.sku ORDER BY 2 DESC LIMIT 5;','Top 5 products by units sold.']],
 perf:'Index orders(customer_id, placed_at) for customer history pages; order_items(order_id) is covered by its PK. Money in integer cents avoids float rounding.',
 pit:'Storing totals without a reconciliation query lets drift go unnoticed — run the check nightly.'},
{cat:'schemas',topic:'task tracker',t:'Task tracker schema — projects and assignments',
 d:'Projects contain tasks, tasks have assignees and states. A check constraint keeps state values legal; the assignee link is nullable for unassigned work.',
 ddl:'CREATE TABLE projects(id INTEGER PRIMARY KEY, name TEXT NOT NULL);\nCREATE TABLE members(id INTEGER PRIMARY KEY, name TEXT NOT NULL);\nCREATE TABLE tasks(id INTEGER PRIMARY KEY, project_id INTEGER NOT NULL REFERENCES projects(id), title TEXT NOT NULL, state TEXT NOT NULL CHECK(state IN (\'todo\',\'doing\',\'done\')), assignee_id INTEGER REFERENCES members(id), due TEXT);',
 qs:[['SELECT p.name, COUNT(*) FILTER (WHERE t.state != \'done\') AS open FROM tasks t JOIN projects p ON p.id=t.project_id GROUP BY p.name;','Open tasks per project.'],['SELECT name FROM members WHERE id NOT IN (SELECT assignee_id FROM tasks WHERE assignee_id IS NOT NULL);','Members with no assignments.']],
 perf:'Index tasks(project_id, state) for board views; tasks(assignee_id) for "my work" lists.',
 pit:'CHECK constraints are documentation the database enforces — prefer them over app-only validation.'},
{cat:'schemas',topic:'event log',t:'Append-only event log schema',
 d:'An append-only event table: immutable rows, a sequence id, and a payload. Nothing is ever updated or deleted — corrections are new compensating events. The audit trail pattern.',
 ddl:'CREATE TABLE events(seq INTEGER PRIMARY KEY AUTOINCREMENT, aggregate_id TEXT NOT NULL, kind TEXT NOT NULL, payload TEXT NOT NULL, recorded_at TEXT NOT NULL DEFAULT (datetime(\'now\')));\nCREATE INDEX ev_agg ON events(aggregate_id, seq);',
 qs:[['SELECT kind, payload FROM events WHERE aggregate_id=\'order-42\' ORDER BY seq;','Replay one aggregate\'s history in order.'],['SELECT date(recorded_at) AS d, COUNT(*) FROM events GROUP BY d ORDER BY d;','Event volume per day.']],
 perf:'The (aggregate_id, seq) index makes replay a range scan. Partition or archive by recorded_at when volume grows.',
 pit:'Never UPDATE or DELETE here — if the app can mutate history, the audit guarantee is fiction.'},
{cat:'schemas',topic:'multi-tenant saas',t:'Multi-tenant SaaS schema — tenant isolation',
 d:'Every tenant-owned table carries tenant_id, and a composite PK or unique constraint leads with it. Row-level isolation by convention, enforced by disciplined querying.',
 ddl:'CREATE TABLE tenants(id INTEGER PRIMARY KEY, name TEXT NOT NULL);\nCREATE TABLE accounts(id INTEGER PRIMARY KEY, tenant_id INTEGER NOT NULL REFERENCES tenants(id), email TEXT NOT NULL, UNIQUE(tenant_id, email));\nCREATE TABLE invoices(id INTEGER PRIMARY KEY, tenant_id INTEGER NOT NULL, account_id INTEGER NOT NULL, amount_cents INTEGER NOT NULL);',
 qs:[['SELECT t.name, COUNT(i.id) FROM tenants t LEFT JOIN invoices i ON i.tenant_id=t.id GROUP BY t.name;','Invoice counts per tenant.'],['SELECT * FROM invoices WHERE tenant_id=7 AND account_id=3;','Tenant-scoped lookup — tenant_id always in the predicate.']],
 perf:'Lead indexes with tenant_id: invoices(tenant_id, account_id). Consider row-level security policies where the database supports them.',
 pit:'One missing tenant_id predicate leaks data across tenants — centralize query building or use RLS.'},
{cat:'queries',topic:'top-N per group',t:'Top-N per group — ROW_NUMBER pattern',
 d:'ROW_NUMBER() OVER (PARTITION BY group ORDER BY metric DESC) ranks within each group; the outer query keeps rn <= N. The standard "best per category" query.',
 ddl:'CREATE TABLE sales(id INTEGER PRIMARY KEY, region TEXT NOT NULL, rep TEXT NOT NULL, amount INTEGER NOT NULL);',
 qs:[['SELECT region, rep, amount FROM (SELECT region, rep, amount, ROW_NUMBER() OVER (PARTITION BY region ORDER BY amount DESC) AS rn FROM sales) WHERE rn <= 3;','Top 3 reps per region.'],['SELECT region, rep, amount FROM (SELECT region, rep, amount, RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS r FROM sales) WHERE r = 1;','Tied-for-first variant with RANK.']],
 perf:'Needs a sort per partition; an index on (region, amount DESC) can feed it.',
 pit:'ROW_NUMBER breaks ties arbitrarily — use RANK when ties must share the top spot.'},
{cat:'queries',topic:'running total',t:'Running total — cumulative SUM window',
 d:'SUM(amount) OVER (ORDER BY day) accumulates across ordered rows. The frame defaults to everything up to the current row — exactly a running total.',
 ddl:'CREATE TABLE ledger(day TEXT PRIMARY KEY, amount INTEGER NOT NULL);',
 qs:[['SELECT day, amount, SUM(amount) OVER (ORDER BY day) AS running FROM ledger;','Daily amounts with cumulative balance.'],['SELECT day, AVG(amount) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS ma7 FROM ledger;','7-day moving average sibling.']],
 perf:'One ordered pass; index on the ORDER BY column avoids a sort.',
 pit:'Duplicate day values make the default frame nondeterministic — add a tiebreaker column.'},
{cat:'queries',topic:'gaps and islands',t:'Gaps and islands — session grouping',
 d:'The classic trick: subtract ROW_NUMBER from a date sequence and equal values mark one "island" of consecutive days. Groups consecutive activity into sessions.',
 ddl:'CREATE TABLE logins(user_id INTEGER NOT NULL, day TEXT NOT NULL);',
 qs:[['SELECT user_id, MIN(day) AS start_day, MAX(day) AS end_day, COUNT(*) AS days FROM (SELECT user_id, day, date(day, \'-\' || ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY day) || \' days\') AS grp FROM logins) GROUP BY user_id, grp;','Consecutive-day login streaks per user.'],['SELECT COUNT(*) AS streaks FROM (SELECT user_id, date(day, \'-\' || ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY day) || \' days\') AS grp FROM logins GROUP BY user_id, grp HAVING COUNT(*) >= 7);','Count streaks of 7+ days.']],
 perf:'Sorts per user; fine at moderate scale, consider incremental sessionization for huge logs.',
 pit:'Date arithmetic syntax varies by database — the pattern is portable, the functions are not.'},
{cat:'queries',topic:'funnel',t:'Funnel analysis — step conversion',
 d:'Conditional aggregation turns event rows into funnel stages: COUNT(DISTINCT CASE WHEN step>=1...) per stage. One pass, full funnel.',
 ddl:'CREATE TABLE events(user_id INTEGER NOT NULL, step INTEGER NOT NULL);',
 qs:[['SELECT COUNT(DISTINCT CASE WHEN step>=1 THEN user_id END) AS s1, COUNT(DISTINCT CASE WHEN step>=2 THEN user_id END) AS s2, COUNT(DISTINCT CASE WHEN step>=3 THEN user_id END) AS s3 FROM events;','Three-stage funnel counts.'],['SELECT s2*1.0/NULLIF(s1,0) FROM (SELECT COUNT(DISTINCT CASE WHEN step>=1 THEN user_id END) s1, COUNT(DISTINCT CASE WHEN step>=2 THEN user_id END) s2 FROM events);','Stage 1 to 2 conversion rate.']],
 perf:'Single scan with hashing; pre-aggregate daily funnels for dashboards.',
 pit:'COUNT(DISTINCT) is approximate-friendly — HyperLogLog variants trade exactness for speed.'},
{cat:'queries',topic:'cohort retention',t:'Cohort retention matrix',
 d:'Cohort = first-activity month; retention = active in month N after cohort. A self-join of first-touch to activity builds the matrix.',
 ddl:'CREATE TABLE activity(user_id INTEGER NOT NULL, month TEXT NOT NULL);',
 qs:[['WITH first AS (SELECT user_id, MIN(month) AS c0 FROM activity GROUP BY user_id) SELECT f.c0 AS cohort, a.month, COUNT(DISTINCT a.user_id) AS active FROM first f JOIN activity a ON a.user_id=f.user_id AND a.month>=f.c0 GROUP BY f.c0, a.month ORDER BY 1,2;','Cohort retention matrix.'],['WITH first AS (SELECT user_id, MIN(month) AS c0 FROM activity GROUP BY user_id) SELECT c0 AS cohort, COUNT(*) AS size FROM first GROUP BY c0 ORDER BY c0;','Cohort sizes.']],
 perf:'The MIN aggregation is the heavy step; index activity(user_id, month).',
 pit:'Months as TEXT sort correctly only in ISO YYYY-MM format.'},
{cat:'indexing',topic:'composite index order',t:'Composite index column order',
 d:'In a composite index, equality columns come first, then range/sort columns. (tenant_id, status, created_at) serves "tenant + status + order by date" perfectly; reversed, it cannot.',
 ddl:'CREATE TABLE orders(id INTEGER PRIMARY KEY, tenant_id INTEGER NOT NULL, status TEXT NOT NULL, created_at TEXT NOT NULL);\nCREATE INDEX o_tenant_status_created ON orders(tenant_id, status, created_at);',
 qs:[['SELECT * FROM orders WHERE tenant_id=7 AND status=\'open\' ORDER BY created_at LIMIT 20;','Uses the full index: equality, equality, ordered range.'],['EXPLAIN QUERY PLAN SELECT * FROM orders WHERE tenant_id=7 AND status=\'open\' ORDER BY created_at LIMIT 20;','Verify the index is used, no sort step.']],
 perf:'Leftmost-prefix rule: the index serves queries on (tenant_id), (tenant_id,status), or all three — not on (status) alone.',
 pit:'Low-cardinality leading columns (like a boolean) waste the index\'s first slot.'},
{cat:'indexing',topic:'covering index',t:'Covering index — index-only scans',
 d:'If the index contains every column the query needs, the database never touches the table: an index-only scan. Include select-list columns after the key columns.',
 ddl:'CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT NOT NULL, name TEXT NOT NULL);\nCREATE INDEX u_email_name ON users(email, name);',
 qs:[['SELECT name FROM users WHERE email=\'a@x.com\';','Index-only: email lookup returns name from the index.'],['EXPLAIN QUERY PLAN SELECT name FROM users WHERE email=\'a@x.com\';','Confirm "USING COVERING INDEX".']],
 perf:'Dramatically faster for hot lookups; wider indexes cost more on writes — measure the tradeoff.',
 pit:'SELECT * defeats covering — select only needed columns.'},
{cat:'indexing',topic:'partial index',t:'Partial index — index the hot subset',
 d:'A partial index covers only rows matching a predicate: WHERE status=\'open\'. Smaller, faster, cheaper to maintain than a full index when queries target the subset.',
 ddl:'CREATE TABLE tasks(id INTEGER PRIMARY KEY, title TEXT NOT NULL, status TEXT NOT NULL);\nCREATE INDEX t_open ON tasks(status) WHERE status=\'open\';',
 qs:[['SELECT * FROM tasks WHERE status=\'open\' ORDER BY id LIMIT 50;','Uses the small partial index.'],['SELECT COUNT(*) FROM tasks WHERE status=\'open\';','Count served by the partial index.']],
 perf:'Index size proportional to the subset; ideal when <10% of rows are hot.',
 pit:'The query predicate must imply the index predicate, or the planner ignores it.'},
{cat:'indexing',topic:'expression index',t:'Expression index — index a computation',
 d:'Indexing LOWER(email) makes case-insensitive lookups fast without a generated column. The index stores the computed value.',
 ddl:'CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT NOT null);\nCREATE INDEX u_email_lower ON users(LOWER(email));',
 qs:[['SELECT * FROM users WHERE LOWER(email)=LOWER(\'A@X.COM\');','Uses the expression index.'],['SELECT COUNT(*) FROM users WHERE LOWER(email) LIKE \'a%\';','Prefix search also served by the expression index.']],
 perf:'One index serves all case-insensitive email lookups; keep the expression identical in queries.',
 pit:'Wrapping the column differently (e.g. UPPER) misses the index — exact expression match required.'},
{cat:'transactions',topic:'isolation levels',t:'Isolation levels — phenomena map',
 d:'Read uncommitted < read committed < repeatable read < serializable. Each level forbids more phenomena: dirty reads, non-repeatable reads, phantoms. Stronger means slower — pick the weakest level that stays correct.',
 ddl:'-- conceptual record: no DDL; the "schema" is the isolation ladder itself\n-- dirty read: T2 sees T1\'s uncommitted write (forbidden at read committed+)\n-- non-repeatable read: T2 re-reads and the row changed (forbidden at repeatable read+)\n-- phantom: T2 re-queries and new rows appear (forbidden at serializable)',
 qs:[['-- T1: BEGIN; UPDATE accounts SET bal=bal-100 WHERE id=1;\n-- T2 (read uncommitted): SELECT bal FROM accounts WHERE id=1; -- sees the uncommitted change','Dirty-read demonstration at the weakest level.'],['SET TRANSACTION ISOLATION LEVEL SERIALIZABLE; BEGIN; -- your critical section here; COMMIT;','Strongest level for money movement.']],
 perf:'Serializable can serialize (retry!) or deadlock — apps must handle serialization failures with retry loops.',
 pit:'The default level differs per database (Postgres: read committed; MySQL: repeatable read) — never assume.'},
{cat:'transactions',topic:'lost update',t:'Lost update — the classic race',
 d:'Two transactions read balance=100, both add 10, both write 110: one update is lost. The canonical argument for proper isolation or optimistic locking.',
 ddl:'CREATE TABLE accounts(id INTEGER PRIMARY KEY, bal INTEGER NOT NULL);',
 qs:[['-- T1: BEGIN; SELECT bal FROM accounts WHERE id=1; -- 100\n-- T2: BEGIN; SELECT bal FROM accounts WHERE id=1; -- 100\n-- T1: UPDATE accounts SET bal=110 WHERE id=1; COMMIT;\n-- T2: UPDATE accounts SET bal=110 WHERE id=1; COMMIT; -- lost update','Interleaving that loses 10.'],['UPDATE accounts SET bal = bal + 10 WHERE id = 1;','Atomic increment — no read-modify-write race.']],
 perf:'Single-statement atomic updates avoid the race entirely and are the fastest fix.',
 pit:'ORMs that read-then-write in app code reintroduce this silently.'},
{cat:'transactions',topic:'optimistic locking',t:'Optimistic locking — version column',
 d:'Each row carries a version; updates include WHERE version=:v and bump it. If another writer got there first, zero rows update and the app retries. No locks held while thinking.',
 ddl:'CREATE TABLE docs(id INTEGER PRIMARY KEY, body TEXT NOT NULL, version INTEGER NOT NULL DEFAULT 1);',
 qs:[['UPDATE docs SET body=\'new\', version=version+1 WHERE id=1 AND version=3;','Succeeds only if nobody else wrote since version 3.'],['SELECT changes(); -- in SQLite: rows affected by the last statement','Zero means conflict — reload and retry.']],
 perf:'Zero lock contention on reads; retries cost only on actual conflict.',
 pit:'Every writer must use the version predicate — one raw UPDATE bypassing it breaks the scheme.'},
{cat:'transactions',topic:'deadlock',t:'Deadlock anatomy — lock ordering',
 d:'T1 locks A then wants B; T2 locks B then wants A: both wait forever. The fix is global lock ordering — always acquire locks in the same sequence.',
 ddl:'CREATE TABLE a(id INTEGER PRIMARY KEY, v INTEGER);\nCREATE TABLE b(id INTEGER PRIMARY KEY, v INTEGER);',
 qs:[['-- T1: BEGIN; UPDATE a SET v=1 WHERE id=1; -- holds A\n-- T2: BEGIN; UPDATE b SET v=1 WHERE id=1; -- holds B\n-- T1: UPDATE b SET v=2 WHERE id=1; -- waits\n-- T2: UPDATE a SET v=2 WHERE id=1; -- DEADLOCK','Classic deadly embrace.'],['-- Fix: both transactions lock a before b, always.','Lock ordering prevents the cycle.']],
 perf:'Deadlocks abort one transaction; apps must catch and retry the loser.',
 pit:'Keep transactions short and touch the fewest rows possible.'},
{cat:'nosql',topic:'document model',t:'Document model — when documents fit',
 d:'Documents (JSON-like) shine when data is accessed as a unit: an order with its items, a user with preferences. Embed what you read together; reference what grows unbounded.',
 ddl:'-- MongoDB-style: db.orders.insertOne({ _id: 1, customer: "a@x.com", items: [{sku:"p1", qty:2}], total_cents: 5000 })\n-- Rule: embed for read-together, reference for many-to-many or unbounded growth',
 qs:[['-- db.orders.find({ "customer": "a@x.com" }, { items: 1 })','Fetch one order with its embedded items — single read.'],['-- db.orders.updateOne({ _id: 1 }, { $push: { items: { sku: "p2", qty: 1 } } })','Atomic push into the embedded array.']],
 perf:'Single-document reads are fast; document growth causes moves — cap embedded arrays.',
 pit:'Embedding unbounded arrays (all comments ever) creates unmanageable documents.'},
{cat:'nosql',topic:'key-value sessions',t:'Key-value store — session pattern',
 d:'Sessions are the canonical KV use: key=session:id, value=serialized session, TTL=expiry. O(1) reads, automatic cleanup, no SQL needed.',
 ddl:'-- Redis-style:\n-- SET session:abc123 \'{"user":7}\' EX 1800\n-- GET session:abc123\n-- DEL session:abc123  (logout)',
 qs:[['-- SET session:abc123 \'{"user":7}\' EX 1800','Write with 30-minute TTL.'],['-- GET session:abc123','O(1) session lookup.']],
 perf:'In-memory KV serves millions of ops/sec; persistence (AOF/RDB) trades speed for durability.',
 pit:'Storing sessions without TTL leaks memory forever.'},
{cat:'nosql',topic:'wide-column time series',t:'Wide-column — time-series pattern',
 d:'Wide-column stores (Cassandra-style) partition by series key and cluster by time: (sensor_id, timestamp). Writes append, reads scan time ranges — the time-series shape.',
 ddl:'-- CQL-style:\n-- CREATE TABLE readings(sensor_id UUID, ts TIMESTAMP, value DOUBLE, PRIMARY KEY(sensor_id, ts));\n-- SELECT * FROM readings WHERE sensor_id=? AND ts >= ? AND ts < ?;',
 qs:[['-- SELECT * FROM readings WHERE sensor_id=? AND ts >= ? AND ts < ?;','Time-range scan within one partition — the fast path.'],['-- SELECT COUNT(*) FROM readings WHERE sensor_id=? AND ts >= ?;','Count in a range, still partition-local.']],
 perf:'Partition by series keeps related data together; avoid huge partitions (tens of MB max).',
 pit:'Querying across partitions (no sensor_id) triggers a cluster-wide scatter — design queries first.'},
{cat:'nosql',topic:'counter pattern',t:'Distributed counter — sharded increments',
 d:'High-write counters shard across N keys and sum on read: increments scatter, reads aggregate. The standard fix for hot-key contention.',
 ddl:'-- Redis-style: INCR counter:shard:{i} for i in 0..N-1\n-- read: sum(GET counter:shard:*)  (or Lua script)',
 qs:[['-- INCR pageviews:shard:3','One of N shards takes the write.'],['-- EVAL "local s=0; for _,k in ipairs(KEYS) do s=s+redis.call(\'GET\',k) end; return s" 8 pageviews:shard:0 ...','Sum shards on read.']],
 perf:'Write throughput scales with shard count; reads cost N GETs — cache the sum briefly.',
 pit:'Shard counts must be stable; changing N re-shards history.'},
{cat:'queries',topic:'dedupe',t:'Delete duplicates — keep one row',
 d:'ROW_NUMBER() over the duplicate key flags extras; deleting rn > 1 keeps exactly one copy. Deterministic with an id tiebreaker.',
 ddl:'CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT NOT NULL);',
 qs:[['DELETE FROM users WHERE id IN (SELECT id FROM (SELECT id, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn FROM users) WHERE rn > 1);','Keep the lowest id per email.'],['SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;','Audit remaining duplicates (expect zero).']],
 perf:'One pass with a sort; run in a transaction and verify counts before/after.',
 pit:'Always verify the survivor rule before deleting in production.'},
{cat:'indexing',topic:'index maintenance',t:'When not to index — write cost',
 d:'Every index taxes writes: each INSERT/UPDATE/DELETE maintains every index on the table. Index the queries you have, not the queries you imagine — and drop indexes with zero reads.',
 ddl:'CREATE TABLE logs(id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL, msg TEXT NOT NULL);',
 qs:[['-- Hypothetical: CREATE INDEX logs_msg ON logs(msg);\n-- But no query filters by msg -> pure write tax. DROP it.','Index audit reasoning.'],['SELECT * FROM logs WHERE ts >= date(\'now\', \'-7 days\') ORDER BY ts DESC LIMIT 100;','The ts index earns its keep here.']],
 perf:'Measure index usage (pg_stat_user_indexes / query plans) and drop the unused.',
 pit:'More indexes are not "safer" — each one slows writes and bloats storage.'}
];

function balanced(s){var d=0;for(var i=0;i<s.length;i++){if(s[i]==='(')d++;else if(s[i]===')'){d--;if(d<0)return false;}}return d===0;}

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var pool=opts.category?T.filter(function(x){return x.cat===opts.category;}):T;
  if(!pool.length)pool=T;
  var t=pick(pool,rnd);
  var qs=shuffle(t.qs,rnd).slice(0,2).map(function(q){
    var sql=q[0];
    if(!SQLKW.test(sql))sql='SELECT 1; -- nosql-shell: '+sql.replace(/^--\s*/,'');
    return {query:sql,explanation:q[1]};
  });
  var id=PREFIX+String(seed).padStart(7,'0');
  return {id:id,title:t.t,category:t.cat,topic:t.topic,
    description:t.d+' This record is Signature-generated original content: a compact, practical reference entry written for this archive.',
    schema_sql:t.ddl,example_queries:qs,performance_notes:t.perf,pitfalls:t.pit,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-DBE-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.topic!=='string'||!r.topic.length)e.push('topic');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120)e.push('description');
  if(typeof r.schema_sql!=='string'||!r.schema_sql.length)e.push('schema_sql');
  if(!balanced(r.schema_sql||''))e.push('schema-parens');
  if(!Array.isArray(r.example_queries)||r.example_queries.length<2||r.example_queries.length>4)e.push('example_queries');
  else r.example_queries.forEach(function(q){
    if(!q||typeof q.query!=='string'||!q.query.length||typeof q.explanation!=='string'||!q.explanation.length)e.push('query');
    else{
      if(!SQLKW.test(q.query))e.push('query-kw');
      if(!balanced(q.query))e.push('query-parens');
    }
  });
  if(typeof r.performance_notes!=='string'||r.performance_notes.length<60)e.push('performance_notes');
  if(typeof r.pitfalls!=='string'||!r.pitfalls.length)e.push('pitfalls');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  if(r.source==='online'&&!(typeof r.source_ref==='string'&&r.source_ref.length))e.push('source_ref');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-db-engineering-1.0',generate:generate,validate:validate,PREFIX:PREFIX};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-engineering',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
