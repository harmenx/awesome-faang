# System Design Resources for FAANG Prep

A curated list of high-quality resources to prepare for system design interviews at FAANG and other top tech companies. Focused on fundamentals, common interview questions, and scalable design patterns.

---

## 1. **System Design Fundamentals**

- [System Design Primer (GitHub)](https://github.com/donnemartin/system-design-primer) – The gold standard starting point.  
- [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview) – Structured, interview-focused explanations.  
- [Designing Data-Intensive Applications (DDIA)](https://dataintensive.net/) – Deep understanding of real-world distributed systems.

Core topics to master:
- Scalability & performance
- Latency vs throughput
- Availability & reliability
- Consistency models (CAP, PACELC)
- Horizontal vs vertical scaling

---

## 2. **Key Components & Concepts**

### **Load Balancing**
- [Load Balancing Basics](https://www.nginx.com/resources/glossary/load-balancing/)  
- L4 vs L7 load balancers  
- Round-robin, least connections, consistent hashing

### **Caching**
- [Caching Strategies](https://aws.amazon.com/caching/)  
- Cache-aside vs write-through vs write-back  
- Redis, Memcached, CDN caching

### **Databases**
- [SQL vs NoSQL](https://www.mongodb.com/nosql-explained)  
- ACID vs BASE  
- Indexing, sharding, replication

### **Messaging & Streaming**
- [Message Queues Explained](https://www.cloudamqp.com/blog/message-queues-explained.html)  
- Kafka vs RabbitMQ vs SQS  
- Event-driven architectures

### **Storage**
- Object storage vs block vs file storage  
- Hot vs cold data  
- Data lifecycle policies

---

## 3. **Common System Design Interview Questions**

Practice designing these systems end-to-end:

- URL Shortener (bit.ly)  
- News Feed (Facebook / Twitter)  
- Chat / Messaging App (WhatsApp)  
- Video Streaming Platform (YouTube / Netflix)  
- Ride Sharing Service (Uber)  
- Search Autocomplete  
- Rate Limiter  
- File Storage (Google Drive / Dropbox)

Good reference:
- [System Design Interview Questions (GFG)](https://www.geeksforgeeks.org/top-10-system-design-interview-questions-and-answers/)

---

## 4. **Design Patterns for Interviews**

- Rate limiting (token bucket, leaky bucket)  
- Idempotency  
- Data partitioning & sharding strategies  
- Read/write separation  
- Eventual consistency  
- Circuit breakers  
- Backpressure

---

## 5. **System Design Framework (Interview Approach)**

Use a repeatable structure in interviews:

1. Clarify requirements (functional + non-functional)  
2. Estimate scale (users, QPS, storage)  
3. High-level architecture diagram  
4. Deep dive into critical components  
5. Identify bottlenecks & trade-offs  
6. Discuss optimizations & failure handling

Reference:
- [How to Crack the System Design Interview](https://www.educative.io/blog/system-design-interview)

---

## 6. **YouTube Channels & Playlists**

- [System Design Interview – Alex Xu](https://www.youtube.com/c/SystemDesignInterview)  
- [Gaurav Sen](https://www.youtube.com/c/GauravSensei) – Excellent intuition for distributed systems  
- [ByteByteGo](https://www.youtube.com/c/ByteByteGo) – Visual explanations of system design concepts  

---

## 7. **Mock Interviews & Practice**

- [Pramp](https://www.pramp.com/) – Free peer-to-peer mock interviews  
- [Interviewing.io](https://interviewing.io/) – Real FAANG interviewers  
- Whiteboard or diagram using Excalidraw / Miro

---

## 8. **Books**

- *Designing Data-Intensive Applications* – Martin Kleppmann  
- *System Design Interview – An Insider’s Guide* – Alex Xu  
- *Site Reliability Engineering* – Google  

---

> Tip: In FAANG interviews, clarity and trade-offs matter more than perfect architecture. Communicate assumptions, constraints, and reasoning clearly.
