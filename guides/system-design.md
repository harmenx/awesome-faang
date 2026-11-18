# System Design

A system design round gives you about 45 minutes to design a large service out loud, such as a URL shortener, a news feed, or a chat app. There is no single right answer. Interviewers score how you scope the problem, whether the design works, and how well you reason about the trade-offs you made.

## Contents

- [What is scored at each level](#what-is-scored-at-each-level)
- [A 45-minute plan](#a-45-minute-plan)
- [Back-of-the-envelope estimates](#back-of-the-envelope-estimates)
- [Building blocks](#building-blocks)
- [Choosing a database](#choosing-a-database)
- [Common questions and what they test](#common-questions-and-what-they-test)
- [Mistakes that cost offers](#mistakes-that-cost-offers)
- [Where to learn more](#where-to-learn-more)

## What is scored at each level

| Level | Typical title | What a strong answer shows |
| --- | --- | --- |
| Mid-level | SDE II, E4, L4 | A complete, working design. You know the standard building blocks and use them correctly. |
| Senior | Senior, E5, L5 | You drive the conversation, find the hard part of the problem yourself, and go deep on it with clear trade-offs. |
| Staff and above | Staff, E6+, L6+ | You weigh several valid designs, reason about cost, operations, and failure, and adapt when requirements change. |

Many companies do not run a system design round for new graduates and early-career roles. Ask your recruiter.

## A 45-minute plan

Keep an eye on the clock. Running out of time before the deep dive is the most common way to fail this round.

| Minutes | Step | What to produce |
| --- | --- | --- |
| 0–5 | **Requirements** | Three to five core features, and the non-functional needs that matter: scale, latency, availability or consistency, durability. State what you are leaving out. |
| 5–10 | **Entities and API** | The main objects (user, post, message) and the endpoints or calls that use them, with their inputs and outputs. |
| 10–25 | **High-level design** | A diagram that satisfies every functional requirement end to end: clients, services, databases, caches, queues. Walk one request through it. |
| 25–40 | **Deep dives** | Pick the two or three hardest problems, usually the ones your non-functional requirements create, and solve them properly. |
| 40–45 | **Wrap-up** | Bottlenecks, failure modes, monitoring, and what you would do next with more time. |

Do estimates when they change a decision, for example whether data fits on one machine. Skip them when they do not.

## Back-of-the-envelope estimates

Round aggressively. The goal is the order of magnitude, not the exact number.

**Handy conversions**

| Quantity | Approximate value |
| --- | --- |
| Seconds in a day | 86,400, call it 10⁵ |
| Requests per second from 1 million requests per day | about 12 |
| Requests per second from 1 billion requests per day | about 12,000 |
| 1 KB × 1 billion | 1 TB |
| 2¹⁰, 2²⁰, 2³⁰, 2⁴⁰ | thousand, million, billion, trillion |

**Latency, by order of magnitude.** Modern hardware is faster than these classic figures, but the ratios between them still hold.

| Operation | Rough time |
| --- | --- |
| Read from memory | 100 ns |
| Read 1 MB sequentially from memory | 10 µs |
| Random read from SSD | 100 µs |
| Round trip within a data center | 0.5 ms |
| Read 1 MB sequentially from SSD | 1 ms |
| Disk seek | 10 ms |
| Round trip between continents | 150 ms |

**A worked example.** A photo app with 100 million daily active users, each viewing 50 photos and uploading 1 photo of 200 KB per day:

```python
daily_users = 100_000_000
seconds_per_day = 86_400

reads_per_second = daily_users * 50 / seconds_per_day
writes_per_second = daily_users * 1 / seconds_per_day
storage_per_year_tb = daily_users * 200_000 * 365 / 1e12

assert round(reads_per_second, -3) == 58_000      # about 60,000 reads per second
assert round(writes_per_second, -2) == 1_200       # about 1,200 uploads per second
assert round(storage_per_year_tb, -3) == 7_000     # about 7 PB of photos per year
```

What this tells you: reads outnumber writes 50 to 1, so caching and a CDN matter most, and petabytes of images belong in object storage, not a database.

## Building blocks

| Block | Use it for | Trade-off to mention |
| --- | --- | --- |
| Load balancer | Spreading traffic across stateless servers | Sticky sessions break horizontal scaling; keep servers stateless. |
| Cache (Redis, Memcached) | Hot reads, sessions, counters | Invalidation and staleness. Say which strategy: cache-aside, write-through, or write-back. |
| CDN | Static files and media near users | Cost, and purging when content changes. |
| Relational database | Structured data, transactions, joins | Harder to scale writes; needs replicas and eventually sharding. |
| Key-value or wide-column store | Very high write rates, simple access by key | Limited queries and weaker transactions. |
| Object storage (S3) | Images, video, backups, large files | Higher latency; serve through a CDN. |
| Message queue or log (SQS, Kafka) | Decoupling services, absorbing spikes, async work | At-least-once delivery means consumers must be idempotent. |
| Search index (Elasticsearch) | Full-text and faceted search | A second copy of the data to keep in sync. |
| Replication | Read scaling and failover | Replica lag; reads may be stale. |
| Sharding | Write scaling and large datasets | Choosing the key; hot shards; cross-shard queries. |
| Consistent hashing | Spreading keys across a changing set of nodes | Needs virtual nodes to balance load. |
| Rate limiter | Protecting services from abuse and spikes | Token bucket versus sliding window; where the counters live. |
| Idempotency keys | Safe retries for payments and writes | Storing and expiring the keys. |

Two concepts come up in almost every round:

- **Consistency versus availability.** During a network partition, a system must choose between rejecting requests and serving possibly stale data. Payments and inventory usually choose consistency. Feeds, likes, and view counts usually choose availability.
- **Fan-out on write versus fan-out on read.** Pushing each new post into followers' feeds makes reads fast but is expensive for accounts with millions of followers. Most real feeds mix the two.

## Choosing a database

Pick based on access patterns, not fashion, and say why.

| If you need | Lean towards |
| --- | --- |
| Transactions across rows, joins, a well-understood schema | PostgreSQL or MySQL |
| Huge write volume with access by a known key | Cassandra or DynamoDB |
| Flexible documents read as a whole | MongoDB or DynamoDB |
| Sub-millisecond reads of hot data | Redis in front of the main store |
| Relationships many hops deep | A graph database, or adjacency lists in a relational store |
| Time-ordered metrics | A time-series database |

## Common questions and what they test

| Question | The hard part interviewers want you to find |
| --- | --- |
| URL shortener | Generating unique short IDs at scale, and a read-heavy cache path |
| Rate limiter | Algorithm choice and keeping counters accurate across many servers |
| News feed | Fan-out on write versus read, and the celebrity problem |
| Chat or messaging | Persistent connections, message ordering, delivery receipts, offline users |
| Notification system | Fan-out to many channels, retries, deduplication, user preferences |
| Ride sharing or nearby places | Geospatial indexing and frequent location updates |
| Web crawler | Politeness per domain, deduplication, prioritizing a huge frontier |
| Typeahead or search suggestions | Prefix lookups at low latency and updating rankings |
| Video streaming | Upload and transcoding pipeline, adaptive bitrate, CDN delivery |
| Ticket booking | Contention for the same seat, reservations that expire, no double booking |
| Distributed key-value store | Partitioning, replication, and consistency settings |
| Top K or leaderboard | Counting at high volume, approximate versus exact, time windows |
| Payment system | Idempotency, exactly-once effects, reconciliation |

Worked answers for most of these are linked from [System Design](../README.md#system-design) in the main list.

## Mistakes that cost offers

- Drawing boxes before agreeing on requirements.
- Spending fifteen minutes on estimates that never influence a decision.
- Naming technologies without saying why. "Kafka" is not a reason; "we need to replay events after a consumer fails" is.
- A design where one database or one service handles everything, with no plan for when it fails.
- Waiting for the interviewer to choose the deep dive. At senior levels, you are expected to pick it.
- Ignoring the requirement that makes the problem hard, such as ordering in chat or double booking in tickets.

## Where to learn more

See [System Design](../README.md#system-design) and [Engineering Blogs and Papers](../README.md#engineering-blogs-and-papers) in the main list.
