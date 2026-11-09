# ERROR: column "total" does not exist — Spec sheet

Record JAH-ERR-000003 — Public edition, error-fix-pairs.
JCC v1 code: JAHDB/error-fix-pairs#JAH-ERR-000003

## Spec
- **Mechanism:** ERROR: column "total" does not exist
LINE 39: SELECT total FROM (SELECT sum(amount) AS s FROM sales) t;

## Key figures

## Official demo output
- **total:** 148
- **mean:** 37
- **first plus second:** 139
- **first minus second:** -67
- **first times second:** 3708

Free forever. Part of The 'Merica-L Internet.