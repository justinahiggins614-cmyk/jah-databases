#!/usr/bin/env python3
"""Entries for the Cloud and Internet Things databases (Manon's 2026-10-17
15:32 EDT orders #16-17).

Dedupe pre-check 2026-10-17: all 68 titles (34 public + 34 Signature Edition)
checked against the whole-system dedupe gate before authoring. One refusal:
"Serverless Functions" collided with software-applications JAH-APP-000020
(and its signature edition with computer-utilities-signature
JAH-CUTG-000053); retitled to "Serverless Computing and Functions as a
Service" - CLEAN. No other collisions.

So this build creates two NEW databases, 34 ladder-ordered records each:

  cloud-internet-things            - The Cloud and Internet Things Database
                                     (public-harvest: real, fact-checked
                                     cloud and internet technology - cloud
                                     service and deployment models,
                                     virtualization, containers, CDNs, DNS,
                                     HTTP/TLS, internet infrastructure, edge
                                     computing, IoT connectivity; standard
                                     references NIST SP 800-145; ISO/IEC
                                     17788; RFC 1034/1035 DNS; RFC 791 IPv4;
                                     RFC 8200 IPv6; RFC 9110/9112 HTTP; RFC
                                     8446 TLS 1.3; RFC 9000 QUIC; ISO/IEC
                                     20922 MQTT; NIST SP 800-53; NIST SP
                                     800-207 zero trust; OCI specs; and the
                                     other landmarks cited per record)
  cloud-internet-things-signature  - The Cloud and Internet Things Signature
                                     Database
                                     (his original Signature Cloud Method:
                                     every cloud service a covenant of
                                     capacity, the internet the great
                                     exchange where covenants are kept,
                                     scaling the kept oath, security the
                                     guarded gate; src signature, titles
                                     suffixed " (Signature Edition)", never
                                     presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CIT- (public) and JAH-CITS- (signature), verified free
in the manifest (2,390 databases, 2,095 id_prefix values - zero hits for
JAH-CIT- or JAH-CITS-) and in every shard index in jah-databases-data-1
(zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_cloud_internet_things.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos before
commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
Nothing on neutralizing/defeating military or defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature Cloud Method: every "
            "cloud service a covenant of capacity, the internet the great "
            "exchange where covenants are kept, scaling the kept oath, and "
            "security the guarded gate. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_NIST145 = ("Mell P, Grance T. NIST Special Publication 800-145. The NIST "
               "Definition of Cloud Computing; 2011.")
CIT_ISO17788 = ("ISO/IEC 17788:2014. Information technology - Cloud "
                "computing - Overview and vocabulary.")
CIT_RFC1034 = ("Mockapetris P. RFC 1034. Domain Names - Concepts and "
               "Facilities; 1987.")
CIT_RFC1035 = ("Mockapetris P. RFC 1035. Domain Names - Implementation and "
               "Specification; 1987.")
CIT_RFC791 = ("Postel J. RFC 791. Internet Protocol; 1981.")
CIT_RFC8200 = ("Deering S, Hinden R. RFC 8200. Internet Protocol, Version 6 "
               "(IPv6) Specification; 2017.")
CIT_RFC9110 = ("Fielding R et al. RFC 9110. HTTP Semantics; 2022.")
CIT_RFC9112 = ("Fielding R et al. RFC 9112. HTTP/1.1; 2022.")
CIT_RFC8446 = ("Rescorla E. RFC 8446. The Transport Layer Security (TLS) "
               "Protocol Version 1.3; 2018.")
CIT_RFC9000 = ("Langley A et al. RFC 9000. QUIC: A UDP-Based Multiplexed and "
               "Secure Transport; 2021.")
CIT_DOCKER = ("Merkel D. Docker: Lightweight Linux Containers for Consistent "
              "Development and Deployment. Linux Journal; 2014.")
CIT_OCI = ("Open Container Initiative. OCI Image Format Specification and "
           "OCI Runtime Specification.")
CIT_K8S = ("Burns B, Grant B, Oppenheimer D, Brewer E, Wilkes J. Borg, "
           "Omega, and Kubernetes. ACM Queue; 2016.")
CIT_MQTT = ("ISO/IEC 20922:2016. Information technology - Message Queuing "
            "Telemetry Transport (MQTT) v3.1.1.")
CIT_NIST853 = ("Joint Task Force. NIST Special Publication 800-53 Rev. 5. "
               "Security and Privacy Controls for Information Systems and "
               "Organizations; 2020.")
CIT_NIST207 = ("Kindervag et al. NIST Special Publication 800-207. Zero "
               "Trust Architecture; 2020.")
CIT_WAFRAME = ("AWS Well-Architected Framework: operational excellence, "
               "security, reliability, performance efficiency, cost "
               "optimization, and sustainability pillars.")
CIT_BORG = ("Verma A et al. Large-scale cluster management at Google with "
            "Borg. EuroSys; 2015.")
CIT_REDIS = ("Redis Ltd. Redis documentation: in-memory data structures, "
             "persistence, replication, and clustering.")
CIT_KAFKA = ("Kreps J, Narkhede N, Rao J. Kafka: a Distributed Messaging "
             "System for Log Processing; 2011.")

ENTRIES = [
    {
        "key": "cloud_what_is",
        "name": "What Is Cloud Computing",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Cloud computing is the on-demand delivery of computing power, "
            "storage, databases, networking, and software over the internet "
            "with pay-as-you-go pricing, so nobody has to buy and run their "
            "own servers to launch a website, an app, or a data pipeline. "
            "The United States National Institute of Standards and Technology "
            "defines it by five essential characteristics: on-demand "
            "self-service (provision capacity yourself through a console or "
            "API), broad network access (reach it from any device over "
            "standard networks), resource pooling (your workload shares "
            "physical hardware with others, isolated by virtualization), "
            "rapid elasticity (scale up and down in minutes, even "
            "automatically), and measured service (metered billing for "
            "exactly what you use). The practical consequence is that a "
            "startup can rent the computing muscle of a supercomputer for "
            "the ten minutes it needs it, and a hobbyist can host a "
            "worldwide website for the price of a coffee. This record is the "
            "door into the whole database: every later record is one shelf "
            "of the cloud and internet world, from the packet to the planet-"
            "scale data center."
        ),
        "how_it_works": (
            "Cloud computing works because three older technologies finally "
            "met. First, virtualization lets one physical server pretend to "
            "be dozens of independent computers, each isolated from the "
            "others. Second, massive data centers gather tens of thousands "
            "of those servers under one roof with their own power, cooling, "
            "and fiber. Third, automation and self-service APIs let software "
            "itself request and release capacity without a human ticket "
            "queue. When you ask the cloud for a virtual machine, the "
            "orchestrator finds free capacity, carves out an isolated slice, "
            "attaches virtual disks and a virtual network, and bills you by "
            "the second. When demand spikes, elasticity rules add more "
            "copies automatically; when it falls, they are destroyed and "
            "billing stops. Measured service closes the loop: every second "
            "of CPU, every gigabyte stored, every gigabyte transferred is "
            "metered like electricity, which is why the cloud is often "
            "called the utility model of computing."
        ),
        "key_points": [
            "NIST defines cloud by five traits: on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service - memorize these and every cloud pitch decodes instantly.",
            "The cloud is rented computing with a meter, not owned computing: you trade capital expense for operating expense and trade fixed capacity for elastic capacity.",
            "Virtualization plus the data center plus self-service APIs are the three legs - remove any one and the model collapses.",
            "Elasticity is the killer feature: capacity follows demand automatically, so you pay for the peak you actually had, not the peak you feared.",
            "The same utility economics that made it cheap also made it the default home of the modern internet - most of the web you use daily runs on rented cloud capacity.",
        ],
        "requirements": [
            "A clear statement of which workload is moving to the cloud and why, so the economics can be checked instead of assumed.",
            "An account with the cloud provider and a billing alert set before the first resource is created, so metering never surprises.",
            "A network path from your users to the cloud region you choose, since geography still sets the speed limit.",
            "Basic fluency with virtual machines, storage, and networks - the cloud rents you these same primitives, only faster.",
            "A plan for who owns security on each layer, since the provider secures the cloud itself and you secure what you put in it.",
        ],
        "standards": [
            "The NIST SP 800-145 definition is the industry's common language for what counts as cloud computing.",
            "ISO/IEC 17788 gives the international vocabulary: roles, cloud capabilities, and deployment models.",
            "Billing and metering follow each provider's documented usage units - compare per-second vCPU, per-GB-month storage, and per-GB transfer like-for-like.",
        ],
        "citations": [CIT_NIST145, CIT_ISO17788],
        "sig_lens": (
            "The Signature read: the cloud is a covenant of capacity. Where "
            "public engineering rents the machine, the Signature Cloud "
            "Method swears it: capacity is promised, measured, and kept - "
            "elasticity is the kept oath that more strength arrives exactly "
            "when the work demands it."
        ),
    },
    {
        "key": "internet_packets",
        "name": "The Internet: How Packets Travel",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The internet is a network of networks: your home router, your "
            "internet provider, backbone carriers, and the data centers "
            "hosting the sites you visit, all speaking the same packet-"
            "switching language so a message can cross the planet without "
            "any single company owning the whole path. Nothing you send "
            "travels as one piece. Every email, video frame, and web page "
            "is chopped into packets - small envelopes each stamped with a "
            "source address, a destination address, and a sequence number. "
            "Routers read only the destination address and forward each "
            "packet toward it, hop by hop, across whatever links are working "
            "right now. Packets from the same message can take different "
            "routes, arrive out of order, or get lost; the receiving end "
            "reassembles them, asks for retransmission of the missing ones, "
            "and hands the complete message up. This design has no central "
            "switchboard and no single point of failure, which is why the "
            "network survived everything from cut cables to entire "
            "countries going dark."
        ),
        "how_it_works": (
            "Packet travel works in layers, each solving one problem. The "
            "Internet Protocol (IP) handles addressing and routing: every "
            "device gets an IP address, and routers keep tables of which "
            "direction leads toward which address ranges, updating them as "
            "links change. On top of IP rides the Transmission Control "
            "Protocol (TCP), which adds reliability: it numbers every byte, "
            "acknowledges receipt, retransmits what is lost, and paces "
            "itself to the speed the network can handle (congestion "
            "control). A lighter sibling, UDP, skips the guarantees for "
            "speed and is used where a late packet is worse than a lost one, "
            "like live video and games. The journey of one web request "
            "looks like this: your device asks its router, which asks your "
            "provider, which hands the packets to a backbone carrier, which "
            "delivers them across oceans of fiber to the data center; the "
            "reply retraces a path that may be entirely different. "
            "Traceroute-style tools expose these hops, each hop a router "
            "deciding, packet by packet, the next step home."
        ),
        "key_points": [
            "Everything is chopped into packets with source, destination, and sequence - the packet is the atom of the internet.",
            "IP routes; TCP guarantees. IP gets packets roughly toward their destination, TCP reassembles them into a reliable ordered stream.",
            "Packets may take different routes and arrive out of order - reliability is rebuilt at the endpoints, not guaranteed by the network.",
            "No central switchboard exists: routers make local forwarding decisions from tables that update as links change, so the network heals around damage.",
            "UDP trades TCP's guarantees for speed - the right choice when timeliness beats perfection, as in live media and games.",
        ],
        "requirements": [
            "An IP address on every device that wants to speak, assigned by DHCP or configured statically.",
            "A default gateway - the router that knows the way out to the wider internet.",
            "DNS resolution (the next record) so human names become the numeric addresses packets actually use.",
            "Routers along the path with working routes toward the destination network.",
            "End-to-end agreement on ports and protocols: both sides must speak TCP or UDP on the same port number.",
        ],
        "standards": [
            "IPv4 is defined by RFC 791 (1981); IPv6, the larger address space, by RFC 8200 (2017).",
            "TCP behavior is specified across RFC 793 and its updates; congestion control algorithms follow RFC 5681 and successors.",
            "Autonomous systems exchange reachability with BGP, the inter-domain routing protocol of the internet backbone.",
        ],
        "citations": [CIT_RFC791, CIT_RFC8200],
        "sig_lens": (
            "The Signature read: the packet is a sworn courier and the "
            "router its guidepost. The Signature Cloud Method treats every "
            "hop as a kept promise - the courier may wander, but the oath "
            "is delivery, and TCP is the ritual that makes every arrival "
            "whole."
        ),
    },
    {
        "key": "dns",
        "name": "DNS: The Internet Phone Book",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The Domain Name System is the phone book of the internet: it "
            "translates the names humans type, like example.com, into the "
            "numeric IP addresses that packets actually travel to. Without "
            "it, every web visit would require memorizing strings like "
            "93.184.216.34. DNS is a global distributed database with no "
            "single master copy. Authority is delegated down a hierarchy: "
            "root servers point to the servers for top-level domains like "
            ".com, which point to the name servers of each registered "
            "domain, which answer for the individual hostnames. Your device "
            "usually asks a resolver run by your provider or a public "
            "service; the resolver walks the hierarchy once, then caches "
            "the answer for its time-to-live so the next million lookups "
            "are instant. Because every web click, email, and app launch "
            "starts with a DNS lookup, DNS is the single most load-bearing "
            "invisible service on the internet - and the reason DNS outages "
            "feel like the whole internet broke."
        ),
        "how_it_works": (
            "A DNS lookup works by delegation. Your browser asks the "
            "configured resolver for the address of www.example.com. If the "
            "resolver has it cached and fresh, it answers immediately. "
            "Otherwise it asks one of the thirteen logical root server "
            "clusters, which do not know the answer but know who serves "
            ".com; the .com servers do not know the answer either but know "
            "the authoritative name servers for example.com; those servers "
            "finally return the A record (IPv4) or AAAA record (IPv6). "
            "Special record types do special jobs: MX routes email, CNAME "
            "aliases one name to another, TXT carries verification strings "
            "and policies, NS declares delegation, SOA holds zone metadata. "
            "Every answer carries a TTL in seconds telling resolvers how "
            "long to cache it - short TTLs let you move servers quickly, "
            "long TTLs cut query load. DNSSEC adds cryptographic signatures "
            "so resolvers can prove an answer was not forged in transit."
        ),
        "key_points": [
            "DNS maps names to addresses through delegated hierarchy: root to top-level domain to authoritative server, with resolvers caching answers by TTL.",
            "Record types are the vocabulary: A/AAAA for addresses, MX for mail, CNAME for aliases, TXT for policies, NS for delegation.",
            "TTL is the control knob: short for agility when you move, long for efficiency when you are stable.",
            "Caching makes DNS fast at planetary scale - the first lookup walks the hierarchy, the next million are instant.",
            "DNSSEC signs answers cryptographically; DNS over HTTPS and DNS over TLS encrypt the lookup itself against snooping.",
        ],
        "requirements": [
            "A registered domain name with authoritative name servers declared at the registrar.",
            "Correct A/AAAA records pointing each hostname at a reachable address.",
            "A sensible TTL strategy: low (60-300 seconds) before migrations, higher in steady state.",
            "A resolver path from every client - usually DHCP-provided or a public resolver.",
            "Monitoring of resolution from multiple vantage points, since a DNS failure looks exactly like a total outage.",
        ],
        "standards": [
            "DNS concepts, implementation, and operation are defined by RFC 1034 and RFC 1035 (1987).",
            "DNSSEC is specified in RFC 4033-4035; encrypted transports in RFC 8484 (DoH) and RFC 7858 (DoT).",
            "Reverse DNS (address to name) uses PTR records in the in-addr.arpa and ip6.arpa zones.",
        ],
        "citations": [CIT_RFC1034, CIT_RFC1035],
        "sig_lens": (
            "The Signature read: DNS is the directory of covenants - every "
            "name a sworn mapping, every record a kept address. The "
            "Signature Cloud Method treats the phone book as an oath ledger: "
            "names must resolve, TTLs must be honored, and a forged answer "
            "is a broken oath."
        ),
    },
    {
        "key": "ip_addressing",
        "name": "IP Addresses and Subnetting",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "An IP address is the street address of a device on the "
            "internet: the number routers use to deliver packets to the "
            "right door. The original IPv4 format is four numbers from 0 to "
            "255, like 192.0.2.44, giving about 4.3 billion possible "
            "addresses - a number that sounded infinite in 1981 and ran out "
            "for new allocations in the 2010s. Its successor IPv6 uses 128-"
            "bit addresses written as eight hex groups, like "
            "2001:db8::1, offering so many addresses that every grain of "
            "sand on Earth could have its own network. Subnetting is the "
            "art of dividing an address block into neighborhoods: a subnet "
            "mask (or the /24-style prefix length) splits each address into "
            "a network part, which identifies the neighborhood, and a host "
            "part, which identifies the house. Inside a cloud virtual "
            "network you will carve subnets for web servers, databases, and "
            "management - each with its own address range and its own "
            "firewall rules - and this record teaches the arithmetic that "
            "makes it exact."
        ),
        "how_it_works": (
            "IP addressing works by longest-prefix matching. A router holds "
            "a table of routes, each a network prefix like 203.0.113.0/24, "
            "meaning the first 24 bits are the network and the last 8 are "
            "hosts (256 addresses, 254 usable after reserving network and "
            "broadcast). For a packet addressed to 203.0.113.77, the router "
            "finds the longest matching prefix and forwards out the "
            "associated interface. Subnetting borrows host bits to make "
            "more, smaller networks: splitting a /24 into two /25s yields "
            "two neighborhoods of 128 addresses each. Private address "
            "ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 in IPv4) are "
            "never routed on the public internet, so homes and clouds reuse "
            "them freely behind network address translation (NAT), which "
            "rewrites private source addresses to one public address. IPv6 "
            "restores the original end-to-end vision: with 2^128 addresses, "
            "every device can hold a globally unique address and NAT "
            "becomes unnecessary."
        ),
        "key_points": [
            "IPv4 gives ~4.3 billion addresses (exhausted for new allocations); IPv6 gives 2^128 - address scarcity is a solved problem if you adopt v6.",
            "The prefix length (/24, /16, /8) splits every address into network part and host part - routing matches on the network part only.",
            "Subnetting borrows host bits to carve big blocks into isolated neighborhoods, each with its own firewall policy.",
            "Private ranges plus NAT let the whole world reuse the same addresses internally behind one public address.",
            "A /24 holds 256 addresses (254 usable); a /16 holds 65,536 - know these two and you can size any cloud network on sight.",
        ],
        "requirements": [
            "An address plan before creating the network: which prefix per subnet, sized for growth, never overlapping.",
            "A subnet mask or prefix length on every interface so the device knows its own neighborhood.",
            "A default route (0.0.0.0/0) pointing at the gateway for everything outside the local subnets.",
            "Reserved private ranges for internal use; public addresses only where the internet must reach directly.",
            "Documentation of the plan - subnets multiply, and an undocumented /16 becomes a mystery within a year.",
        ],
        "standards": [
            "IPv4 addressing and packet format: RFC 791; IPv6: RFC 8200.",
            "Private address space: RFC 1918; NAT terminology and behavior: RFC 2663.",
            "CIDR notation (the /24 style) replaced classful addressing per RFC 4632.",
        ],
        "citations": [CIT_RFC791, CIT_RFC8200],
        "sig_lens": (
            "The Signature read: the address is the covenant's seal and the "
            "subnet its walled district. The Signature Cloud Method assigns "
            "every district its streets deliberately - no two districts "
            "share a street, no courier knocks on the wrong door."
        ),
    },
    {
        "key": "http_web",
        "name": "HTTP and the Web Request",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "HTTP, the Hypertext Transfer Protocol, is the language of the "
            "web: the request-and-response dialogue your browser holds "
            "with every server, thousands of times a day. A request names "
            "a method (GET to fetch, POST to submit, PUT to replace, "
            "DELETE to remove), a path (which resource), headers (metadata "
            "like what formats you accept and who you are), and optionally "
            "a body (the form data or JSON you send). The server answers "
            "with a three-digit status code - 200 for success, 301/302 for "
            "redirects, 404 for not found, 500 for server failure - plus "
            "headers and the body of the page, image, or data. HTTP is "
            "stateless by design: each request stands alone, and continuity "
            "like logins is layered on top with cookies and tokens. Three "
            "major versions exist: HTTP/1.1 (one request at a time per "
            "connection, still everywhere), HTTP/2 (multiplexed streams "
            "over one connection, much faster), and HTTP/3 (built on QUIC "
            "over UDP, faster still on lossy networks like mobile). Every "
            "cloud service you will ever touch exposes HTTP APIs, so this "
            "record is really about the control language of the cloud "
            "itself."
        ),
        "how_it_works": (
            "A web request works as a short conversation over TCP (or QUIC). "
            "The browser resolves the name via DNS, opens a connection to "
            "the server's port 80 (or 443 for HTTPS), and sends the request "
            "line and headers as plain text (in HTTP/1.1) or as compressed "
            "binary frames (in HTTP/2 and 3). The server routes the path "
            "to a handler - a static file, an application, a cloud function "
            "- runs it, and streams back the status line, headers, and "
            "body. Caching headers (Cache-Control, ETag) let browsers and "
            "CDNs reuse answers without asking again; content negotiation "
            "headers let one URL serve HTML to browsers and JSON to apps. "
            "Cookies carry state across the stateless protocol: the server "
            "sets them, the browser returns them, and the session is "
            "remembered. When the response is done the connection may close "
            "or stay open (keep-alive) for the next request. HTTPS wraps "
            "this entire conversation in TLS encryption - the next record "
            "explains the lock on the conversation."
        ),
        "key_points": [
            "HTTP is a stateless request/response dialogue: method plus path plus headers in, status code plus headers plus body out.",
            "Status codes are grouped by hundreds: 2xx success, 3xx redirect, 4xx client error, 5xx server error - read the first digit and you know who is at fault.",
            "Statelessness is a feature: scale by adding identical servers, and carry continuity in cookies and tokens instead.",
            "HTTP/1.1, HTTP/2, and HTTP/3 are the same language on faster transports: multiplexing then QUIC removed the head-of-line bottlenecks.",
            "Caching headers turn the web into a distributed system - a correct Cache-Control can cut your server load tenfold.",
        ],
        "requirements": [
            "A server listening on the agreed port (80 for HTTP, 443 for HTTPS) with a handler for each path you advertise.",
            "Correct status codes for every outcome - clients and CDNs make decisions from them.",
            "Cache-Control and ETag headers on cacheable responses, so the edge can serve repeats.",
            "Cookie flags (Secure, HttpOnly, SameSite) set deliberately wherever sessions cross the stateless gap.",
            "HTTPS in production (see the next record) - plain HTTP exposes every byte to the network.",
        ],
        "standards": [
            "HTTP semantics: RFC 9110; HTTP/1.1 message syntax: RFC 9112; HTTP/2: RFC 9113; HTTP/3: RFC 9114.",
            "Cookies: RFC 6265; caching: RFC 9111.",
            "Status code registry maintained by IANA; methods GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS standardized in RFC 9110.",
        ],
        "citations": [CIT_RFC9110, CIT_RFC9112],
        "sig_lens": (
            "The Signature read: the request is a petition and the response "
            "a sworn answer. The Signature Cloud Method honors the codes - "
            "200 is a kept promise, 404 an honest admission, 500 a broken "
            "oath confessed - and every petition travels the guarded road "
            "of the next record."
        ),
    },
    {
        "key": "tls",
        "name": "TLS and HTTPS: Encryption in Transit",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "TLS, Transport Layer Security, is the encryption that turns "
            "HTTP into HTTPS - the padlock in your browser - and it "
            "protects nearly everything else that crosses the internet: "
            "email, APIs, database connections, and VPNs. It gives three "
            "guarantees: confidentiality (nobody between you and the "
            "server can read the traffic), integrity (nobody can alter it "
            "undetected), and authenticity (you are really talking to the "
            "server named in the address bar, proven by a certificate "
            "issued by a trusted certificate authority). The current "
            "version, TLS 1.3, completes its handshake in a single round "
            "trip, removed all the obsolete cipher suites that enabled a "
            "decade of famous attacks, and provides forward secrecy by "
            "default - meaning that even if a server's private key is "
            "stolen later, previously recorded traffic stays unreadable. "
            "Certificates are the identity documents of the system: they "
            "bind a public key to a domain name, expire (now typically "
            "after about a year), and are checked against revocation lists "
            "and transparency logs. Free automated authorities made HTTPS "
            "universal; today an unencrypted login page is negligence, "
            "not thrift."
        ),
        "how_it_works": (
            "The TLS 1.3 handshake works in one round trip. The client "
            "sends a ClientHello with its supported parameters and a key "
            "share; the server answers with its certificate chain and its "
            "own key share, and both sides independently compute the same "
            "session keys using elliptic-curve Diffie-Hellman - the keys "
            "never cross the wire. The client verifies the certificate: "
            "the signature chains to a trusted root, the domain matches, "
            "the dates are valid, and the certificate appears in public "
            "transparency logs. From then on, every byte is encrypted with "
            "an authenticated cipher (typically AES-GCM or ChaCha20-"
            "Poly1305) and each record carries a message authentication "
            "code, so tampering is detected instantly. Session resumption "
            "lets returning clients skip even the single round trip. "
            "Certificates are issued after the authority verifies control "
            "of the domain (usually via a DNS or HTTP challenge), renewed "
            "automatically by agents on the server, and served with the "
            "full chain so the client can walk from the leaf to its "
            "trusted root."
        ),
        "key_points": [
            "TLS gives confidentiality, integrity, and authenticity - encryption alone without authentication is a locked door with no address check.",
            "TLS 1.3 handshakes in one round trip with forward secrecy by default; disable everything older on public endpoints.",
            "Certificates bind keys to names via trusted authorities; verify the chain, the name match, the dates, and transparency-log presence.",
            "Forward secrecy means a future key theft cannot decrypt past traffic - ephemeral key exchange is the mechanism.",
            "Automated issuance and renewal removed the last excuse: HTTPS is now the baseline for anything carrying credentials or personal data.",
        ],
        "requirements": [
            "A valid certificate for every public hostname, served with its full chain to a trusted root.",
            "TLS 1.2 minimum, TLS 1.3 preferred; obsolete versions (1.0, 1.1) and weak ciphers disabled.",
            "Automatic renewal with monitoring and alerting well before expiry - expired certificates are the commonest self-inflicted outage.",
            "HSTS headers so browsers refuse to ever downgrade the site to plain HTTP.",
            "Private keys stored with restricted permissions, rotated on personnel changes, and never committed to code repositories.",
        ],
        "standards": [
            "TLS 1.3: RFC 8446; TLS 1.2: RFC 5246; deprecation of TLS 1.0/1.1: RFC 8996.",
            "Certificate profiles: RFC 5280; automated issuance (ACME): RFC 8555; certificate transparency: RFC 9162.",
            "HTTP Strict Transport Security (HSTS): RFC 6797.",
        ],
        "citations": [CIT_RFC8446],
        "sig_lens": (
            "The Signature read: TLS is the sealed envelope and the wax "
            "stamp in one. The Signature Cloud Method seals every covenant "
            "in transit - the envelope hides the words, the stamp proves "
            "the sender, and forward secrecy burns each envelope's wax so "
            "no stolen seal can ever open the past."
        ),
    },
    {
        "key": "virtualization",
        "name": "Virtualization: One Machine, Many",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Virtualization is the trick that makes cloud computing "
            "possible: software that lets one physical computer pretend to "
            "be many independent computers, each running its own operating "
            "system, each believing it owns the hardware. The software "
            "doing the pretending is the hypervisor. Type 1 hypervisors "
            "(like KVM, Hyper-V, and ESXi) run directly on the hardware and "
            "power the world's clouds; Type 2 hypervisors (like "
            "VirtualBox) run inside a desktop OS for development and "
            "testing. A virtual machine gets virtual CPUs carved from "
            "physical cores, virtual RAM from physical memory, virtual "
            "disks from physical storage, and virtual network cards on "
            "virtual switches - and strong isolation guarantees that a "
            "crash or a compromise in one VM cannot reach its neighbors. "
            "Because VMs are just files and metadata, they can be copied, "
            "snapshotted, paused, and moved live from one host to another "
            "without downtime. The cloud's entire business model - renting "
            "slices of shared hardware with hard walls between tenants - "
            "is virtualization industrialized."
        ),
        "how_it_works": (
            "A hypervisor works by interposing itself between the guest "
            "operating systems and the real hardware. Modern CPUs provide "
            "hardware virtualization extensions (Intel VT-x, AMD-V) that "
            "let the hypervisor run guest code directly on the processor "
            "at near-native speed, trapping only the privileged operations "
            "(like touching real hardware) for emulation or paravirtual "
            "handling. Memory is virtualized with extended page tables so "
            "each VM sees a contiguous block of RAM that is actually "
            "scattered across physical memory, with the hypervisor "
            "enforcing the boundaries. Virtual disks are files or volumes "
            "on shared storage, virtual networks are software switches "
            "inside the host, and devices are emulated or passed through. "
            "Overcommit lets the hypervisor promise more virtual resources "
            "than physically exist - safe because most VMs idle most of "
            "the time - with balloon drivers and live migration as the "
            "safety valves. Snapshots freeze a VM's disk and memory state "
            "so it can be cloned or rolled back; live migration copies a "
            "running VM's memory to another host iteratively until the "
            "final handoff is milliseconds long."
        ),
        "key_points": [
            "The hypervisor is the layer between guests and hardware: Type 1 runs on bare metal (the cloud's choice), Type 2 runs inside a desktop OS.",
            "Hardware extensions (VT-x, AMD-V) make virtualization near-native speed; only privileged operations trap to the hypervisor.",
            "Isolation is the product: a crashed or compromised VM cannot see its neighbors, which is what makes multi-tenant clouds safe to share.",
            "VMs are portable artifacts - snapshot, clone, and live-migrate them like files, which is how clouds do maintenance without downtime.",
            "Overcommit sells more virtual resources than physical ones exist, balanced by the statistical truth that most VMs idle most of the time.",
        ],
        "requirements": [
            "A hypervisor matched to the job: Type 1 for production servers and clouds, Type 2 for development sandboxes.",
            "Hardware virtualization extensions enabled in firmware, plus enough RAM - memory, not CPU, is usually the binding constraint.",
            "Virtual networks designed before the VMs: management, workload, and storage traffic separated.",
            "A snapshot and backup discipline, since virtual disks make it dangerously easy to skip real backups.",
            "License awareness: guest operating systems inside VMs still need their licenses counted per virtual instance.",
        ],
        "standards": [
            "Virtual machine packaging and portability: the Open Virtualization Format (OVF), DMTF DSP0243.",
            "Cloud infrastructure management: DMTF CIM and the OCCI interface family.",
            "Hardware interfaces: Intel VT-x / AMD-V CPU extensions; SR-IOV (PCI-SIG) for near-native virtual device performance.",
        ],
        "citations": [CIT_ISO17788, CIT_NIST145],
        "sig_lens": (
            "The Signature read: the hypervisor is the covenant-keeper of "
            "the machine - many tenants, one roof, and walls of honor "
            "between them. The Signature Cloud Method treats each virtual "
            "machine as a sworn chamber: sealed from its neighbors, "
            "portable as a scroll, and summoned or dismissed at the word "
            "of the keeper."
        ),
    },
    {
        "key": "service_models",
        "name": "Cloud Service Models: IaaS, PaaS, and SaaS",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Cloud services come in three layers of abstraction, and "
            "choosing among them is the first architectural decision of "
            "any cloud project. Infrastructure as a Service (IaaS) rents "
            "raw building blocks - virtual machines, disks, networks - and "
            "you install and manage everything above the hypervisor "
            "yourself. Platform as a Service (PaaS) rents a managed "
            "platform: you bring your code, the provider runs the "
            "operating system, runtime, scaling, and patching. Software as "
            "a Service (SaaS) rents finished software: you sign in and "
            "use it, the provider runs absolutely everything. The classic "
            "analogy is pizza: IaaS is renting the kitchen, PaaS is "
            "ordering the dough made and baking it yourself, SaaS is "
            "delivery. Control and responsibility move in opposite "
            "directions: IaaS gives maximum control with maximum "
            "operational burden; SaaS gives minimum control with zero "
            "burden. Most real systems mix all three - virtual machines "
            "for the custom core, a managed database platform beside "
            "them, and SaaS for email and office tools."
        ),
        "how_it_works": (
            "The models differ in where the provider's responsibility ends "
            "and yours begins - the shared responsibility line. With IaaS, "
            "you call an API for a virtual machine: the provider "
            "guarantees the host, the network, and the hypervisor, and you "
            "own the guest OS upward - patching, firewalls, backups, and "
            "the application. With PaaS, you push code or a container "
            "image: the provider owns the OS, runtime patching, load "
            "balancing, and scaling, and you own the code, the data, and "
            "the access controls. With SaaS, you configure users and "
            "permissions in someone else's running application and own "
            "only your data and who can see it. Billing follows the "
            "abstraction: IaaS meters machines and gigabytes, PaaS meters "
            "platform units like database throughput or function "
            "invocations, SaaS charges per user or per tier. Migration "
            "usually climbs the stack over time: lift-and-shift to IaaS "
            "first, then refactor pieces onto PaaS as the team learns what "
            "undifferentiated work it can hand to the provider."
        ),
        "key_points": [
            "IaaS rents raw infrastructure you manage; PaaS rents a managed platform you deploy code to; SaaS rents finished software you configure.",
            "The shared responsibility line moves with the model: higher abstraction means the provider owns more and you operate less.",
            "Choose by undifferentiated heavy lifting: anything that is not your competitive advantage belongs on the highest abstraction that fits.",
            "Billing follows abstraction: machines and bytes for IaaS, platform units for PaaS, seats and tiers for SaaS - compare total cost, not sticker price.",
            "Real architectures are hybrids of all three: IaaS for the custom core, PaaS for the database, SaaS for commodity tools.",
        ],
        "requirements": [
            "A responsibility map for each workload stating exactly which layers the provider owns and which the team owns.",
            "Operational skills matched to the choice: IaaS demands OS and network operations; PaaS demands deployment and data skills instead.",
            "An exit awareness for PaaS and SaaS: know what migration would cost before the abstraction becomes a cage.",
            "Cost modeling per model, since the cheapest abstraction for a steady workload is often IaaS and for a spiky one PaaS or serverless.",
            "Data ownership terms in every SaaS contract: export formats, retention, and deletion on termination.",
        ],
        "standards": [
            "Service model definitions: NIST SP 800-145 (IaaS, PaaS, SaaS) and ISO/IEC 17788 vocabulary.",
            "Service level agreements follow provider-published definitions of uptime, credits, and exclusions - read the SLA, not the marketing page.",
            "Interoperability and portability considerations: ISO/IEC 19941 (cloud computing interoperability and portability).",
        ],
        "citations": [CIT_NIST145, CIT_ISO17788],
        "sig_lens": (
            "The Signature read: the three models are three depths of "
            "covenant. IaaS swears the ground, PaaS swears the ground and "
            "the tools, SaaS swears the whole feast. The Signature Cloud "
            "Method chooses the depth deliberately - never swearing deeper "
            "than the work requires, never shallower than the team can keep."
        ),
    },
]

ENTRIES += [
    {
        "key": "deployment_models",
        "name": "Cloud Deployment Models: Public, Private, and Hybrid",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Where the cloud physically lives and who it serves is the "
            "deployment model, and it answers the question every regulated "
            "or cautious organization asks first: who else is on this "
            "hardware? The public cloud is the familiar one: infrastructure "
            "owned by a provider, shared among thousands of tenants, "
            "reached over the internet - maximum elasticity and minimum "
            "upfront cost. The private cloud is infrastructure dedicated to "
            "one organization, run in its own data center or hosted "
            "exclusively: maximum control over data location and "
            "neighbors, at the cost of owning the capacity planning. The "
            "hybrid cloud connects the two, letting workloads move or burst "
            "between private infrastructure and public capacity, with "
            "consistent tooling across both. A fourth sibling, the community "
            "cloud, shares infrastructure among organizations with common "
            "concerns, like government agencies or research networks. The "
            "choice is rarely ideological: data residency laws, latency to "
            "factories or hospitals, existing hardware investments, and the "
            "spikiness of demand each push toward a different answer, and "
            "large organizations routinely run all of them at once."
        ),
        "how_it_works": (
            "Deployment models differ in tenancy, location, and control "
            "plane. In the public cloud, a web of regions and availability "
            "zones hosts millions of virtual machines on shared hosts, "
            "isolated by hypervisors and virtual networks; you reach it "
            "over the internet or a private interconnect, and you never "
            "see the building. In the private cloud, the same virtualization "
            "and self-service APIs run on hardware reserved for one tenant, "
            "inside a facility the organization controls - sometimes its "
            "own, sometimes a provider's dedicated cages - giving audit-"
            "friendly certainty about where bits rest. The hybrid model "
            "joins them with encrypted tunnels or dedicated links, shared "
            "identity, and orchestration that can place a workload on "
            "either side: steady baseloads stay private where the hardware "
            "is already paid for, spikes burst to public capacity that "
            "would otherwise sit idle. The hard parts of hybrid are "
            "consistency - the same deployment pipelines, monitoring, and "
            "security policies on both sides - and data gravity: moving "
            "terabytes between clouds is slow and metered, so the data "
            "usually decides where the compute lives."
        ),
        "key_points": [
            "Public cloud: shared provider infrastructure, maximum elasticity, minimum upfront cost - the default for variable demand.",
            "Private cloud: single-tenant infrastructure under your control - chosen for data residency, latency, and existing investment.",
            "Hybrid connects both with shared identity and tooling, letting steady loads stay private and spikes burst public.",
            "The community cloud pools infrastructure among organizations with shared concerns, like agencies or research consortia.",
            "Data gravity rules placement: compute follows the data because moving terabytes is slow and metered - plan the data home first.",
        ],
        "requirements": [
            "A data classification stating which datasets may leave the organization's physical control and under which laws.",
            "Network connectivity between environments for hybrid: encrypted tunnels at minimum, dedicated interconnects for serious traffic.",
            "One identity system spanning all environments, so a person is the same person on both sides of the hybrid line.",
            "Consistent deployment and monitoring tooling across models, or the private side becomes a second-class citizen.",
            "An exit and repatriation plan: know the cost of moving each workload back before you need to.",
        ],
        "standards": [
            "Deployment model definitions: NIST SP 800-145 and ISO/IEC 17788.",
            "Data residency and sovereignty requirements derive from applicable law (for example GDPR data-transfer rules in the EU) - the model must satisfy the statute, not just the architecture diagram.",
            "Hybrid interconnect security: encrypted tunnels (IPsec) or provider dedicated interconnects with MACsec where offered.",
        ],
        "citations": [CIT_NIST145, CIT_ISO17788],
        "sig_lens": (
            "The Signature read: the deployment model is the covenant's "
            "territory. Public ground is the open market, private ground "
            "the walled estate, hybrid the road between them. The Signature "
            "Cloud Method places each workload on the ground its oath "
            "requires - and data, being heaviest, chooses the ground first."
        ),
    },
    {
        "key": "datacenters_regions",
        "name": "Data Centers, Regions, and Availability Zones",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The cloud is not in the sky; it is in buildings - enormous, "
            "windowless, humming buildings called data centers, and the "
            "geography of those buildings shapes everything about how your "
            "systems behave. Providers organize the planet into regions: "
            "a region is a geographic area, like the US East or EU West, "
            "containing one or more data centers. Inside each region sit "
            "availability zones: physically separate data centers, miles "
            "apart, with independent power, cooling, and network, connected "
            "by fast private fiber. Deploying across multiple zones means "
            "a fire, flood, or backhoe in one building does not take your "
            "service down; deploying across multiple regions means even a "
            "regional disaster does not. Regions also decide latency - the "
            "speed of light in fiber means every thousand miles adds "
            "roughly ten milliseconds of round trip - and legal "
            "jurisdiction, since data physically stored in a country falls "
            "under that country's laws. Choosing a region is therefore a "
            "three-way trade: closeness to users, closeness to the law you "
            "must satisfy, and distance from correlated disasters."
        ),
        "how_it_works": (
            "A data center works as a life-support system for computers. "
            "Grid power enters through redundant feeds and uninterruptible "
            "supplies into rows of racks; cooling - often evaporative or "
            "liquid-assisted at hyperscale - removes the megawatts of heat "
            "the servers produce; fiber enters through multiple carriers "
            "so no single cut isolates the building. Inside, servers are "
            "organized for failure: power and network are redundant to the "
            "rack, and orchestration constantly moves virtual machines "
            "away from ailing hosts. Availability zones turn this building-"
            "level resilience into architecture: synchronous replication "
            "of databases across zones (a few milliseconds apart) gives "
            "automatic failover with no data loss, while the zone "
            "separation guarantees the failures are uncorrelated. Regions "
            "are the unit of legal and latency reasoning: providers publish "
            "each region's location, and services let you pin data to "
            "regions to satisfy residency rules. The demo computes round-"
            "trip latency from fiber distance and shows why zone-redundant "
            "design survives a building loss."
        ),
        "key_points": [
            "Regions are geographic areas; availability zones are isolated data centers inside a region with independent power, cooling, and network.",
            "Multi-zone deployment survives a building failure; multi-region deployment survives a regional disaster - design to the threat you actually face.",
            "Latency is physics: roughly 10 milliseconds of round trip per thousand miles of fiber - place regions near your users.",
            "Data stored in a country falls under that country's laws - region choice is a legal decision as much as a technical one.",
            "Data centers are life-support for computers: redundant power, industrial cooling, and multi-carrier fiber, orchestrated so no single failure is fatal.",
        ],
        "requirements": [
            "Production workloads spread across at least two availability zones, with automated failover tested, not assumed.",
            "A region choice justified in writing: user latency, legal jurisdiction, and service availability in that region.",
            "Stateful data replicated across zones synchronously (or across regions asynchronously) to match the recovery objective.",
            "Power and cooling redundancy verified at the facility level for any private data center you operate.",
            "A game day that actually kills a zone and watches the system survive - untested failover is a hope, not a plan.",
        ],
        "standards": [
            "Data center tiers: the Uptime Institute Tier Standard (Tier I-IV) for power and cooling redundancy.",
            "Facility safety and operations: NFPA 75 (fire protection of IT equipment); energy efficiency measured by PUE (power usage effectiveness).",
            "Provider region/zone architectures are documented per provider; zone independence claims should be verified against provider status history.",
        ],
        "citations": [CIT_NIST145, CIT_WAFRAME],
        "sig_lens": (
            "The Signature read: the data center is the covenant's temple "
            "and the zones its separate sanctuaries. The Signature Cloud "
            "Method never keeps its oath in a single sanctuary - the "
            "promise is written in two buildings, so one building's fall "
            "cannot break it."
        ),
    },
    {
        "key": "storage_types",
        "name": "Cloud Storage: Object, File, and Block",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Cloud storage comes in three shapes, and picking the wrong "
            "one is the commonest expensive mistake in cloud architecture. "
            "Object storage keeps each file as an object in a flat "
            "namespace: you address it by a key like photos/2026/beach.jpg "
            "through an HTTP API, and the system replicates it across "
            "facilities to eleven nines of durability (99.999999999 "
            "percent). It is effectively infinite, cheap, and perfect for "
            "backups, media, data lakes, and static websites - but it is "
            "not a filesystem: there are no directories, no in-place "
            "edits, no file locking. File storage gives you a real shared "
            "filesystem (NFS or SMB) that many machines mount at once, "
            "for legacy applications and shared home directories. Block "
            "storage gives you raw virtual disks that attach to one virtual "
            "machine at a time and behave exactly like a local hard drive, "
            "for databases and anything needing low-latency random access. "
            "The rule of thumb: objects for the warehouse, files for "
            "sharing, blocks for the engine room."
        ),
        "how_it_works": (
            "Object storage works by content-addressed distribution. Your "
            "PUT request carries the bytes and the key; the system erasure-"
            "codes or replicates the bytes across drives, servers, and "
            "often facilities, then records the key in a massively "
            "distributed index. GET by key fetches from the nearest healthy "
            "copy; listing is eventually consistent in some systems. "
            "Versioning keeps every overwrite as a new version, and "
            "lifecycle policies move aging objects to cheaper, slower "
            "tiers automatically. File storage works by presenting the NFS "
            "or SMB protocols the operating system already speaks: the "
            "client mounts a share, and reads and writes become network "
            "calls handled by a managed filer with its own redundancy. "
            "Block storage works by exposing a virtual disk over the "
            "storage network: the guest OS formats it with any filesystem "
            "and issues block reads and writes, while the provider "
            "replicates each block and offers snapshots - point-in-time "
            "copies used for backups. Performance and price move together: "
            "block is fastest and dearest per gigabyte, object is slowest "
            "per operation and cheapest at scale."
        ),
        "key_points": [
            "Object storage: flat key-addressed warehouse, eleven-nines durability, HTTP API, effectively infinite and cheap - for backups, media, data lakes, static sites.",
            "File storage: real shared filesystems (NFS/SMB) mounted by many machines - for legacy apps and shared directories.",
            "Block storage: raw virtual disks attached to one VM, formatted like local drives - for databases and low-latency random access.",
            "Objects are immutable and versioned; files are shared and lockable; blocks are formattable and snapshotable - the API shapes the use.",
            "Lifecycle tiers move aging data to cheaper storage automatically - the difference between a tidy bill and a data-hoarding bill.",
        ],
        "requirements": [
            "A storage choice per dataset justified by access pattern: share of reads vs writes, latency needs, and sharing scope.",
            "Versioning enabled on object buckets holding anything irreplaceable, with lifecycle rules archiving or expiring old versions.",
            "Snapshots scheduled for every block volume carrying a database, tested by restoring to a scratch volume.",
            "Encryption at rest enabled (provider-managed keys at minimum; customer-managed keys for sensitive data) on all three types.",
            "Access policies denying public reads by default on object storage - open buckets are the classic cloud breach.",
        ],
        "standards": [
            "Object API conventions follow the S3 API de facto standard, widely cloned across providers.",
            "File protocols: NFSv4 (RFC 7530) and SMB3 (MS-SMB2); block transport commonly iSCSI (RFC 7143) or NVMe-oF.",
            "Durability claims (e.g. eleven nines) are provider design targets verified by erasure coding math and operational history, not magic.",
        ],
        "citations": [CIT_NIST145, CIT_WAFRAME],
        "sig_lens": (
            "The Signature read: storage is the covenant's vault, in three "
            "chambers - the warehouse of objects, the commons of files, "
            "the engine room of blocks. The Signature Cloud Method places "
            "each treasure in its proper chamber, seals every chamber with "
            "encryption, and never leaves the warehouse door standing open."
        ),
    },
    {
        "key": "containers",
        "name": "Containers and Container Images",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A container is a sealed box for software: your application "
            "plus everything it needs to run - libraries, runtime, "
            "configuration - packaged so it behaves identically on your "
            "laptop, in testing, and in production. Unlike a virtual "
            "machine, which carries a whole guest operating system, a "
            "container shares the host's kernel and isolates only what "
            "matters: its own filesystem, processes, and network "
            "namespace. The result starts in milliseconds instead of "
            "minutes and packs dozens of applications onto one host. The "
            "container image is the frozen blueprint: a stack of read-"
            "only layers, each layer the diff of one build step, content-"
            "addressed by cryptographic hash so the same hash always "
            "means the same bytes. Images live in registries, get pulled "
            "by hosts, and run as containers - build once, run anywhere. "
            "This is the packaging that made microservices practical: "
            "when every service ships as an immutable image, deploying "
            "version 47 of one service without touching the other forty-"
            "six becomes routine instead of terrifying."
        ),
        "how_it_works": (
            "Containers work through Linux kernel isolation primitives. "
            "Namespaces give the container its own view of the world: its "
            "own process IDs, its own network interfaces, its own mount "
            "table, its own hostname - so process 1 inside the container "
            "is just an ordinary process outside it. Control groups "
            "(cgroups) cap what the container may consume: this many CPU "
            "shares, that many megabytes of RAM, this much block I/O. The "
            "image is built layer by layer from a Dockerfile: each "
            "instruction (install packages, copy code, set environment) "
            "creates a new layer storing only the changed files, and "
            "layers are shared between images - ten images built on the "
            "same base share that base's bytes on disk. At runtime the "
            "layers are stacked read-only with a thin writable layer on "
            "top (the union filesystem), so containers start fast and "
            "stay immutable: kill a container and its writable layer "
            "vanishes, which is why real containers keep state in mounted "
            "volumes or external databases, never inside themselves."
        ),
        "key_points": [
            "Containers share the host kernel and isolate via namespaces and cgroups: millisecond startup, dense packing, strong-enough walls for most workloads.",
            "Images are immutable layered blueprints, content-addressed by hash - the same digest always runs the same bytes, everywhere.",
            "Layers are diffs: each build step adds one, and images sharing a base share its bytes - keep images small by keeping layers few and lean.",
            "Containers are ephemeral by design: writable layers vanish on stop, so state lives in volumes or external services, never in the container.",
            "Build once, run anywhere is the payoff: the image that passed testing is bit-for-bit the image that ships to production.",
        ],
        "requirements": [
            "A Dockerfile per service that is minimal (small base image), pinned (exact versions, not 'latest'), and scanned for known vulnerabilities.",
            "A private registry with access control for production images; public registries only for public artifacts.",
            "Resource limits (CPU and memory) declared on every container, so one runaway cannot starve its neighbors.",
            "No secrets baked into images: inject credentials at runtime from a secrets manager.",
            "A non-root user inside the image wherever the application allows it, shrinking the blast radius of a compromise.",
        ],
        "standards": [
            "Image and runtime formats: the Open Container Initiative (OCI) image and runtime specifications.",
            "The Dockerfile format and registry API were popularized by Docker (Merkel, 2014) and standardized through OCI distribution.",
            "Vulnerability scanning references the CVE database; base images should track minimal distributions (Alpine, distroless, or provider-minimal).",
        ],
        "citations": [CIT_DOCKER, CIT_OCI],
        "sig_lens": (
            "The Signature read: the container is a sealed reliquary - the "
            "application and its whole world, closed with wax. The "
            "Signature Cloud Method seals every service identically: the "
            "hash is the seal, immutability the oath, and nothing unsealed "
            "ever enters the temple of production."
        ),
    },
    {
        "key": "kubernetes",
        "name": "Kubernetes: Container Orchestration",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "If containers are sealed boxes, Kubernetes is the shipping "
            "port: the system that decides which box goes on which ship, "
            "restarts the ones that fall overboard, and routes the "
            "customers to the right dock. Born at Google from the lessons "
            "of its internal Borg and Omega systems and open-sourced in "
            "2014, Kubernetes (often K8s) schedules containers across a "
            "fleet of machines, keeps the requested number of copies "
            "running, rolls out new versions gradually, and wires up "
            "networking, storage, and configuration. You declare the "
            "desired state - 'three copies of this image, reachable on "
            "port 80, with this config' - and its control loops drive "
            "reality toward the declaration forever: a crashed container "
            "is restarted, a dead node is drained, a new version is rolled "
            "out pod by pod. Every major cloud offers it as a managed "
            "service, and it has become the standard dialect for running "
            "modern applications at scale."
        ),
        "how_it_works": (
            "Kubernetes works as a set of cooperating control loops around "
            "a declarative API. You POST YAML manifests to the API server "
            "describing Deployments (which template Pods - the smallest "
            "unit, one or more containers sharing network and storage), "
            "Services (stable virtual IPs and DNS names in front of "
            "shifting pods), ConfigMaps and Secrets (configuration and "
            "credentials), and PersistentVolumeClaims (storage). The "
            "scheduler assigns each unscheduled pod to a node with "
            "capacity; the kubelet on that node pulls the images and "
            "starts the containers; controllers watch and repair: the "
            "deployment controller keeps the replica count, the endpoints "
            "controller keeps the service's backend list current. "
            "Networking gives every pod its own cluster IP and flat "
            "reachability; an Ingress (or Gateway) exposes HTTP routes to "
            "the outside. Upgrades are rolling by default: new pods start, "
            "health checks pass, old pods drain - with automatic rollback "
            "if the new version fails its probes. Namespaces divide one "
            "cluster among teams; RBAC decides who may touch what."
        ),
        "key_points": [
            "Declare desired state in YAML; control loops reconcile reality with the declaration forever - crashed pods restart, dead nodes drain, versions roll.",
            "Pods are the atom (containers sharing network and storage); Deployments keep N copies; Services give them stable addresses.",
            "Rolling updates with health probes make deploys boring: new pods prove healthy before old ones drain, with automatic rollback.",
            "Every pod gets a cluster IP and flat networking; Ingress/Gateway maps external HTTP routes to internal services.",
            "Namespaces plus RBAC multi-tenant the cluster: teams share the port but hold separate docks and keys.",
        ],
        "requirements": [
            "Resource requests and limits on every pod, so the scheduler can place honestly and one workload cannot evict its neighbors.",
            "Liveness and readiness probes on every service, so broken pods are restarted and unready pods leave the load balancer.",
            "Secrets in the secret store (or an external secrets manager), never in YAML applied from a laptop.",
            "RBAC least privilege: service accounts and humans get only the verbs on the resources they need.",
            "A managed control plane for production unless operating etcd and the API server is genuinely your business.",
        ],
        "standards": [
            "Kubernetes API conventions and architecture (Cloud Native Computing Foundation, graduated project).",
            "Container runtimes via the Container Runtime Interface (CRI); networking via the Container Network Interface (CNI).",
            "Configuration and secret handling follow the 12-factor app principles popularized for cloud-native deployment.",
        ],
        "citations": [CIT_K8S, CIT_BORG, CIT_OCI],
        "sig_lens": (
            "The Signature read: Kubernetes is the harbor-master of the "
            "covenant fleet - every sealed box declared, placed, watched, "
            "and restored. The Signature Cloud Method declares the desired "
            "state as an oath and lets the harbor-master keep it: what is "
            "written shall float, what sinks shall be raised."
        ),
    },
    {
        "key": "load_balancing",
        "name": "Load Balancers and Auto Scaling",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A load balancer is the traffic cop in front of your servers: "
            "one public address receives all the visitors and distributes "
            "them across a pool of healthy backends, so no single machine "
            "carries the crowd and no single failure ends the show. It "
            "also terminates TLS, so your application servers see plain "
            "HTTP while the internet sees the padlock, and it health-checks "
            "every backend, quietly pulling the sick ones out of rotation "
            "until they recover. Auto scaling is the hiring manager beside "
            "the cop: it watches metrics like CPU utilization or request "
            "queue depth and adds servers when the crowd grows, removes "
            "them when it thins - on schedules you set (scale up before "
            "the morning rush) or on pure demand. Together they are the "
            "two halves of elasticity: the balancer spreads the present "
            "load, the scaler adjusts the capacity to the future load. "
            "Every viral moment in internet history - the product launch, "
            "the breaking news spike - is survived or not by whether these "
            "two were configured before the crowd arrived."
        ),
        "how_it_works": (
            "A load balancer works by sitting in the request path as a "
            "reverse proxy. Clients resolve your domain to the balancer's "
            "address; the balancer picks a backend per request using an "
            "algorithm - round robin, least connections, or latency-based "
            "- and forwards the request, returning the response. Layer 4 "
            "balancers route on IP and port (fast, dumb); Layer 7 "
            "balancers understand HTTP and route on path, host, or header "
            "(smart: /api to the API fleet, /static to the asset fleet). "
            "Sticky sessions can pin a user to one backend when the app "
            "keeps local state, though stateless design is preferred. "
            "Health checks - HTTP probes to a /health endpoint every few "
            "seconds - decide membership: consecutive failures eject the "
            "backend, consecutive successes readmit it. Auto scaling "
            "groups define a launch template (image, size, subnets) and "
            "policies: target-tracking (hold CPU at 60 percent), step "
            "scaling (add two servers per alarm level), or scheduled "
            "actions. Cooldowns prevent flapping; lifecycle hooks let "
            "servers drain connections before termination."
        ),
        "key_points": [
            "The balancer spreads live traffic across healthy backends and terminates TLS; the scaler grows and shrinks the backend pool on metrics.",
            "Layer 4 routes packets, Layer 7 routes requests - use Layer 7 when paths, hosts, or headers should choose the fleet.",
            "Health checks are the membership vote: fail the probe and you leave rotation silently until you recover.",
            "Target-tracking policies (hold CPU near a setpoint) beat threshold alarms for smooth scaling; schedules beat both for predictable rushes.",
            "Stateless backends make all of this trivial; sticky sessions are a crutch for state that should live in a shared store.",
        ],
        "requirements": [
            "A real /health endpoint on every backend that checks downstream dependencies, not just 'the process is alive'.",
            "The load balancer in front of anything public, with TLS terminated there and security groups allowing traffic only from the balancer.",
            "Auto scaling policies tested under synthetic load before the real spike - untested scaling is a rumor.",
            "Cooldowns and minimum/maximum bounds on the group, so a metric glitch cannot scale you to zero or to bankruptcy.",
            "Connection draining on scale-in, so in-flight requests finish instead of dying mid-answer.",
        ],
        "standards": [
            "Layer 7 routing semantics follow HTTP standards (RFC 9110); health-check design follows provider best practices.",
            "TLS termination at the balancer follows the TLS guidance in the encryption record (RFC 8446, HSTS per RFC 6797).",
            "Scaling metrics commonly use CPU utilization, request count per target, or queue depth - the right signal is the one that saturates first.",
        ],
        "citations": [CIT_RFC9110, CIT_RFC8446, CIT_WAFRAME],
        "sig_lens": (
            "The Signature read: the balancer is the fair steward of the "
            "gate, the scaler the wise quartermaster. The Signature Cloud "
            "Method swears no visitor waits unheard and no servant idles "
            "unpaid - the steward divides the crowd justly, the "
            "quartermaster hires exactly the strength the hour demands."
        ),
    },
]

ENTRIES += [
    {
        "key": "cdn",
        "name": "Content Delivery Networks",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A content delivery network is a planetary photocopier: "
            "hundreds of edge servers in cities worldwide each keep a "
            "copy of your static content - images, video, stylesheets, "
            "scripts, downloads - so every user fetches it from the "
            "nearest city instead of your one origin server. The physics "
            "is unbeatable: light in fiber needs about 10 milliseconds "
            "per thousand miles, so a user in Sydney served from Sydney "
            "gets your page an order of magnitude faster than from "
            "Virginia, and your origin survives the traffic spike because "
            "the edge absorbs it. Modern CDNs do far more than copy "
            "files: they terminate TLS at the edge, compress and convert "
            "images, shield the origin (only the CDN may talk to it), "
            "absorb denial-of-service floods across their enormous "
            "capacity, and run edge compute - small functions executing "
            "at the edge for personalization and A/B tests. The "
            "economics are striking: CDN bandwidth is typically far "
            "cheaper than origin bandwidth, so caching aggressively is "
            "one of the highest-return optimizations in all of web "
            "engineering."
        ),
        "how_it_works": (
            "A CDN works by DNS and caching choreography. You point your "
            "domain (or a subdomain like cdn.example.com) at the CDN; "
            "when a user requests an asset, the CDN's DNS answers with "
            "the edge node nearest that user (anycast routing or "
            "geo-DNS). The edge checks its cache: on a hit it serves "
            "instantly; on a miss it fetches from your origin (or a "
            "regional mid-tier cache), stores the copy for its TTL, and "
            "serves it. Cache keys combine URL, and optionally headers "
            "like Accept-Language; Cache-Control headers from your "
            "origin dictate TTL, and purge APIs invalidate stale copies "
            "on deploy. Request collapsing ensures a thousand "
            "simultaneous misses for the same hot asset become one "
            "origin fetch. TLS terminates at the edge with the CDN "
            "holding your certificate (or a shared one), then re-encrypts "
            "to the origin. For video, the CDN speaks adaptive-bitrate "
            "protocols (HLS, DASH), serving each viewer the quality "
            "their connection sustains from cached segments."
        ),
        "key_points": [
            "The CDN copies static content to edge cities worldwide: users fetch from nearby, latency collapses, and the origin is shielded from the crowd.",
            "Caching is DNS plus TTL choreography: edge hit serves instantly, miss fetches once and stores - purge deliberately on deploy.",
            "Cache keys and Cache-Control headers are the controls: correct headers can cut origin traffic by 90 percent or more.",
            "Edge TLS termination, image optimization, origin shielding, and DDoS absorption come standard on modern CDNs.",
            "CDN bandwidth is cheaper than origin bandwidth: caching aggressively is both a performance and a cost strategy.",
        ],
        "requirements": [
            "Cache-Control headers with deliberate max-age on every static asset, plus content-hashed filenames so new deploys are new URLs.",
            "A purge or versioning strategy for deploys: hashed filenames preferred, API purges as the fallback.",
            "Origin shielding: firewall the origin to accept traffic only from the CDN's published ranges.",
            "TLS configured end to end: edge certificate for users, valid certificate on the origin behind it.",
            "Cache-hit-ratio monitoring: a falling hit ratio means headers, keys, or query strings are defeating the cache.",
        ],
        "standards": [
            "Caching semantics: RFC 9111 (HTTP caching); cache directives Cache-Control, ETag, Last-Modified per RFC 9110/9111.",
            "Video delivery: HTTP Live Streaming (HLS, RFC 8216) and MPEG-DASH (ISO/IEC 23009-1).",
            "Anycast routing for edge steering: RFC 4786; TLS at the edge per RFC 8446.",
        ],
        "citations": [CIT_RFC9110, CIT_RFC8446],
        "sig_lens": (
            "The Signature read: the CDN is the covenant's choir of "
            "echoes - one sworn copy sung in every city, so no pilgrim "
            "travels far for the word. The Signature Cloud Method places "
            "the truth near every seeker and guards the original behind "
            "the choir, untouched by the crowd."
        ),
    },
    {
        "key": "virtual_networks",
        "name": "Virtual Networks, Subnets, and Firewalls",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A virtual network is your own private internet inside the "
            "cloud: an isolated address space where your virtual machines, "
            "containers, and databases live and talk, invisible to every "
            "other tenant. You carve it into subnets - public subnets "
            "holding the load balancers that face the internet, private "
            "subnets holding the application servers and databases that "
            "must never be directly reachable. Traffic between subnets, "
            "and between your network and the world, is governed by two "
            "kinds of firewall: security groups, which are stateful "
            "per-instance rule sets (allow this port from that source), "
            "and network access control lists, which are stateless "
            "subnet-level rules evaluated in order. The discipline this "
            "record teaches is defense in depth through topology: the "
            "database subnet accepts connections only from the application "
            "subnet, the application subnet only from the load balancer "
            "subnet, and the whole edifice is drawn before a single "
            "server is launched. Get the network right and security "
            "becomes geometry; get it wrong and every firewall rule is "
            "damage control."
        ),
        "how_it_works": (
            "A virtual network works by software-defined networking over "
            "the provider's physical fabric. You declare a CIDR block "
            "like 10.0.0.0/16; the control plane programs virtual "
            "switches on every host to enforce it, encapsulating your "
            "packets (commonly with VXLAN or GENEVE tunnels) as they "
            "cross the shared underlay. Subnets are slices of the block "
            "with route tables: a public subnet's table sends 0.0.0.0/0 "
            "to the internet gateway, a private subnet's table sends it "
            "to a NAT gateway (outbound only) or nowhere. Security "
            "groups attach to instances: stateful, so a permitted "
            "inbound request automatically permits the reply, evaluated "
            "as the union of all attached groups. Network ACLs attach "
            "to subnets: stateless, numbered rules evaluated lowest "
            "first, so you must allow both directions explicitly. "
            "Peering connects two virtual networks privately; transit "
            "gateways hub-and-spoke many networks and on-premises links "
            "together. Flow logs record every accepted and rejected "
            "packet for forensics."
        ),
        "key_points": [
            "The virtual network is your isolated address space; subnets divide it into public (internet-facing) and private (hidden) neighborhoods.",
            "Security groups are stateful per-instance allow-lists; network ACLs are stateless per-subnet numbered rules - use groups for precision, ACLs for coarse guardrails.",
            "Route tables decide each subnet's relationship with the world: internet gateway for public, NAT gateway for private outbound, none for the truly isolated.",
            "Defense in depth is topology: database accepts only from app tier, app tier only from the balancer - draw it before launching anything.",
            "Peering and transit gateways connect networks privately; flow logs make every packet decision auditable.",
        ],
        "requirements": [
            "An address plan with non-overlapping CIDRs per network and per environment, documented before creation.",
            "Public subnets containing only load balancers and bastions; everything stateful and applicative in private subnets.",
            "Security groups default-deny with explicit allows, scoped to the narrowest source (a balancer's group, not 0.0.0.0/0).",
            "Flow logs enabled on production networks, retained long enough for incident forensics.",
            "A NAT strategy for private subnets needing outbound access (updates, APIs) without inbound exposure.",
        ],
        "standards": [
            "Overlay encapsulation commonly uses VXLAN (RFC 7348) or GENEVE (RFC 8926) over the provider underlay.",
            "Firewall rule design follows least-privilege principles per NIST SP 800-53 (SC-7 boundary protection).",
            "Address planning uses RFC 1918 private space; IPv6 virtual networks follow RFC 8200 addressing.",
        ],
        "citations": [CIT_NIST853, CIT_RFC791],
        "sig_lens": (
            "The Signature read: the virtual network is the covenant's "
            "walled city - public gates for the market, private quarters "
            "for the household, and the vault beneath. The Signature "
            "Cloud Method draws the walls before raising a single roof, "
            "and every gate's guard knows exactly whom to admit."
        ),
    },
    {
        "key": "cloud_databases",
        "name": "Cloud Databases: Relational and NoSQL",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Databases in the cloud split into two great families, and "
            "choosing wrong is a multi-year regret. Relational databases "
            "(PostgreSQL, MySQL) store data in tables with strict schemas "
            "and guarantee ACID transactions - atomicity, consistency, "
            "isolation, durability - which is why money, orders, and "
            "anything that must never contradict itself lives there. "
            "NoSQL databases abandon the table for shapes that scale "
            "horizontally: key-value stores (Redis, DynamoDB) for "
            "millisecond lookups by key, document stores (MongoDB) for "
            "flexible JSON-like records, wide-column stores (Cassandra) "
            "for write-heavy time series, graph databases for "
            "relationship queries. The cloud adds managed operation: "
            "automated backups, multi-zone replication with automatic "
            "failover, read replicas for scaling reads, and serverless "
            "options that bill per request. The modern answer is rarely "
            "either-or: the order system on relational for correctness, "
            "the session store on key-value for speed, the product "
            "catalog on document for flexibility - polyglot persistence, "
            "each workload on the engine that fits."
        ),
        "how_it_works": (
            "A managed relational database works as a primary with "
            "standbys. Writes go to the primary, which streams its write-"
            "ahead log synchronously to a standby in another availability "
            "zone; if the primary fails, the standby is promoted "
            "automatically, usually within a minute or two, with the "
            "endpoint DNS flipping to the new writer. Read replicas take "
            "asynchronous copies for scaling reads. Automated backups "
            "snapshot the storage and retain transaction logs, enabling "
            "point-in-time restore to any second in the retention "
            "window. NoSQL engines scale differently: key-value and "
            "document stores partition data by hash of the key across "
            "many nodes, so throughput grows by adding nodes, trading "
            "the relational guarantees for partition tolerance per the "
            "CAP theorem - they offer tunable consistency (eventual by "
            "default, strong when requested at higher latency cost). "
            "Connection pooling, parameter groups, and maintenance "
            "windows are the operational surface the cloud manages for "
            "you; schema design, indexing, and query shape remain yours."
        ),
        "key_points": [
            "Relational for correctness (ACID transactions, strict schemas) - money and orders live here; NoSQL for shape and scale (key-value, document, wide-column, graph).",
            "Managed databases buy you multi-zone failover, automated backups with point-in-time restore, and read replicas - operate the data, not the engine.",
            "The CAP theorem frames the trade: partition tolerance is mandatory in distributed systems, so you choose between consistency and availability per workload.",
            "Polyglot persistence is the norm: relational for the ledger, key-value for sessions, document for catalogs - each engine for its fit.",
            "Indexes and query shape are still yours: the cloud manages the engine, but a missing index is your outage.",
        ],
        "requirements": [
            "A data-model decision per workload documented with its consistency needs before choosing the engine.",
            "Multi-AZ deployment for every production relational database, with failover actually tested.",
            "Automated backups with a retention window matching the business recovery point objective, plus periodic restore drills.",
            "Encryption at rest and in transit, with credentials in a secrets manager and never in application config files.",
            "Read replicas or caching in front of read-heavy workloads, so the primary is never the bottleneck it was never meant to be.",
        ],
        "standards": [
            "Relational query language: SQL standardized by ISO/IEC 9075; ACID properties formalized in transaction processing literature.",
            "NoSQL consistency models follow the CAP theorem (Brewer) and PACELC extensions; tunable consistency per engine documentation.",
            "Backup and recovery objectives (RPO/RTO) defined per NIST SP 800-34 contingency planning guidance.",
        ],
        "citations": [CIT_WAFRAME, CIT_REDIS, CIT_KAFKA],
        "sig_lens": (
            "The Signature read: the database is the covenant's memory - "
            "the ledger that must never lie, the cache that must never "
            "sleep. The Signature Cloud Method keeps the ledger on stone "
            "(relational truth), the working notes on swift tablets "
            "(NoSQL speed), and every memory copied to a second sanctuary."
        ),
    },
    {
        "key": "serverless",
        "name": "Serverless Computing and Functions as a Service",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Serverless computing is the cloud's boldest abstraction: you "
            "write a single function - 'when this HTTP request arrives, "
            "do this; when this file lands, do that' - and the provider "
            "runs it, scales it from zero to thousands of parallel "
            "copies, and bills you only for the milliseconds it executes. "
            "There are still servers, of course; you simply never see, "
            "patch, or pay for their idle time. Functions as a Service "
            "is the event-driven core: tiny stateless handlers triggered "
            "by HTTP, timers, queue messages, file uploads, or database "
            "changes. Around it grew the broader serverless family: "
            "serverless databases that pause to zero, serverless "
            "containers, and managed API gateways. The fit is perfect "
            "for spiky, event-driven work - webhooks, image processing, "
            "scheduled jobs, glue between services - and poor for "
            "long-running, stateful, or always-hot workloads where a "
            "reserved server is cheaper. The disciplines it demands are "
            "statelessness (state goes to managed stores), idempotency "
            "(the same event may fire twice), and cold-start awareness "
            "(the first invocation after idle pays a startup tax)."
        ),
        "how_it_works": (
            "A serverless function works as managed event dispatch. You "
            "upload code plus a handler signature; the provider keeps it "
            "at rest. When an event arrives - an HTTP request to the API "
            "gateway, a message in the queue, a timer firing - the "
            "control plane assigns it to an execution environment: a warm "
            "sandbox is reused if one is idle, otherwise a fresh one is "
            "provisioned (the cold start: container init plus runtime "
            "plus your initialization code, typically tens to hundreds "
            "of milliseconds, longer for large dependencies or VPC-"
            "attached functions). The handler runs with a hard timeout "
            "(seconds to 15 minutes depending on provider), then the "
            "sandbox is frozen for potential reuse or destroyed. Billing "
            "meters invocations plus gigabyte-seconds of execution. "
            "Concurrency limits cap simultaneous executions per function "
            "and per account - the safety valve against runaway cost and "
            "the throttle you must raise before big events. State is "
            "external by construction: the function reads and writes "
            "databases, object storage, and queues, keeping nothing "
            "local beyond the single invocation."
        ),
        "key_points": [
            "Write a stateless handler; the provider provisions, scales, patches, and bills per millisecond - zero idle cost is the headline.",
            "Events are the triggers: HTTP, timers, queue messages, file uploads, database streams - serverless is the glue of event-driven architecture.",
            "Cold starts tax the first invocation after idle: keep functions lean, dependencies small, and initialization outside the handler.",
            "Statelessness, idempotency, and external state are mandatory disciplines - the platform may retry any event.",
            "Serverless wins for spiky event-driven work and loses for always-hot or long-running workloads - price both before committing.",
        ],
        "requirements": [
            "Stateless handlers with all state in managed stores (database, object storage, cache) - local disk is scratch at best.",
            "Idempotent logic: the same event delivered twice must not double-charge, double-send, or double-write.",
            "Timeouts and memory sized to the workload, with concurrency limits set deliberately before traffic arrives.",
            "Cold-start budgeting for latency-sensitive paths: provisioned concurrency or warmed schedules where the tax is unacceptable.",
            "Cost alarms on invocations and duration from day one - per-millisecond billing still multiplies by millions.",
        ],
        "standards": [
            "Event shapes follow provider contracts; cross-provider portability is aided by the CloudEvents specification (CNCF).",
            "Function packaging commonly uses container images (OCI) or language zips; runtimes cover the major languages.",
            "Timeout, memory, and concurrency limits are provider-documented guardrails - design inside them, not against them.",
        ],
        "citations": [CIT_NIST145, CIT_OCI],
        "sig_lens": (
            "The Signature read: serverless is the covenant of the "
            "moment - strength summoned exactly when called, dismissed "
            "the instant the work is done, and no servant paid for "
            "idle hours. The Signature Cloud Method writes handlers as "
            "oaths of the instant: stateless, idempotent, and gone "
            "without a trace but the result."
        ),
    },
    {
        "key": "iam",
        "name": "Identity and Access Management in the Cloud",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Identity and access management is the lock system of the "
            "cloud: it decides who (or what) may do which action to which "
            "resource, and it is where most cloud breaches are actually "
            "born - not in exotic exploits but in over-broad keys and "
            "forgotten permissions. The cast: identities (human users, "
            "and service roles assumed by applications - never share "
            "credentials between the two), policies (JSON documents "
            "granting or denying actions on resources, evaluated by "
            "default-deny), and the credential types (passwords plus "
            "multi-factor authentication for humans; short-lived "
            "temporary credentials for services). The golden rules: least "
            "privilege (grant only the actions the job needs), separation "
            "of duties (no single identity can both approve and execute "
            "sensitive changes), and no long-lived access keys (rotate "
            "them or, better, eliminate them with workload identity). "
            "Every cloud action - launching a server, reading a bucket, "
            "deploying code - passes through this gate, which makes IAM "
            "the highest-leverage security investment in the entire "
            "database."
        ),
        "how_it_works": (
            "IAM works as a policy evaluation engine on every API call. "
            "When an identity requests an action on a resource, the "
            "engine gathers all applicable policies - identity-based "
            "(attached to the user or role), resource-based (attached "
            "to the bucket or queue), permission boundaries, and "
            "organization-level guardrails - and evaluates them: an "
            "explicit deny anywhere wins, otherwise an explicit allow "
            "grants, otherwise the default deny refuses. Conditions "
            "sharpen policies: allow only from the corporate network, "
            "only with MFA present, only during business hours, only on "
            "resources tagged for the project. Humans authenticate with "
            "password plus a second factor (authenticator app or hardware "
            "key); federated single sign-on maps company directory groups "
            "to cloud roles so joiners and leavers propagate automatically. "
            "Services authenticate by assuming roles: the instance or "
            "function receives temporary credentials that expire in "
            "minutes to hours, so there is no static key to steal. Access "
            "analyzers and credential reports continuously flag unused "
            "permissions and old keys for removal."
        ),
        "key_points": [
            "Default deny with explicit allows: every cloud API call is evaluated against the union of identity, resource, boundary, and organization policies - an explicit deny anywhere wins.",
            "Least privilege is the law: grant only the actions the job needs, sharpened with conditions (network, MFA, tags, time).",
            "Humans get MFA and federation; services get short-lived assumed roles - long-lived access keys are the breach vector to eliminate.",
            "Separation of duties: no single identity approves and executes sensitive changes - the policy should make fraud require conspiracy.",
            "Continuously prune: access analyzers flag unused permissions and stale keys - IAM is a garden, not a monument.",
        ],
        "requirements": [
            "MFA enforced on every human with console or API access, with hardware keys for administrators.",
            "No long-lived access keys for workloads: instance roles, function roles, and workload identity federation instead.",
            "Least-privilege policies reviewed on a schedule, with permission boundaries capping what delegated admins can grant.",
            "Federated single sign-on from the company directory, so deprovisioning one account revokes cloud access everywhere.",
            "Alerting on IAM changes themselves: new users, policy edits, and key creations are security events, not routine admin.",
        ],
        "standards": [
            "Access control models: RBAC and ABAC per NIST SP 800-53 (AC family); MFA per NIST SP 800-63B digital identity guidelines.",
            "Federation protocols: SAML 2.0 and OpenID Connect for single sign-on; OAuth 2.0 for delegated authorization.",
            "Credential hygiene follows provider IAM best practices and the CIS Benchmarks for each major cloud.",
        ],
        "citations": [CIT_NIST853],
        "sig_lens": (
            "The Signature read: IAM is the covenant's seal-ring - who "
            "may speak, what they may touch, and for how long. The "
            "Signature Cloud Method cuts every key narrow, sets every "
            "seal to expire, and trusts no bearer beyond the exact "
            "errand sworn."
        ),
    },
]

ENTRIES += [
    {
        "key": "queues_streams",
        "name": "Message Queues and Event Streams",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Queues and streams are the nervous system of distributed "
            "systems: instead of services calling each other directly "
            "and failing together, they drop messages into a durable "
            "buffer and move on, and consumers process them at their own "
            "pace. A message queue (like SQS or RabbitMQ) delivers each "
            "message to one consumer: order placed, email queued, worker "
            "sends it, message deleted. An event stream (like Kafka or "
            "Kinesis) keeps an ordered, replayable log of everything that "
            "happened: every click, every sensor reading, every trade - "
            "and many consumers read it independently, each at its own "
            "offset, able to rewind and reprocess history. The payoff is "
            "decoupling in time, speed, and fate: producers never wait "
            "for consumers, slow consumers never block producers, and a "
            "dead consumer's messages wait patiently instead of being "
            "lost. This record teaches the patterns - work queues, "
            "publish/subscribe, event sourcing - and the disciplines: "
            "idempotent consumers, dead-letter queues for poison "
            "messages, and retention sized to the business."
        ),
        "how_it_works": (
            "A queue works as a durable buffer with visibility semantics. "
            "The producer sends a message; the broker stores it "
            "redundantly. A consumer receives it (making it invisible to "
            "others for a timeout), processes it, then deletes it - if "
            "the consumer crashes before deleting, the message reappears "
            "for another worker, which is why consumers must be "
            "idempotent. Messages that fail repeatedly move to a "
            "dead-letter queue for inspection instead of poisoning the "
            "workers forever. FIFO queues add ordering and exactly-once "
            "deduplication for workloads that need it. A stream works as "
            "an append-only partitioned log: producers append events to "
            "partitions keyed by entity (user ID, device ID), preserving "
            "order per key; consumers track their own offsets per "
            "partition, committing progress as they go. Retention keeps "
            "events for hours to years, so new consumers can replay "
            "history and rebuild state - the foundation of event "
            "sourcing. Throughput scales by adding partitions and "
            "consumer instances in a group."
        ),
        "key_points": [
            "Queues decouple in time and fate: producers never wait, consumers process at their pace, and dead consumers' messages wait instead of vanishing.",
            "Queue discipline: idempotent consumers (redelivery is normal), visibility timeouts, and dead-letter queues for poison messages.",
            "Streams are replayable ordered logs: many consumers read independently at their own offsets, and history can be reprocessed.",
            "Partition by entity key for order where it matters and parallelism everywhere else - throughput scales with partitions.",
            "Choose queues for work distribution (each message handled once) and streams for event history (many readers, replay, analytics).",
        ],
        "requirements": [
            "Idempotent consumers everywhere: assume every message may be delivered more than once and design the handler accordingly.",
            "Dead-letter queues on every production queue, with alarms on their depth - silent poison messages are silent data loss.",
            "Retention and partition counts sized to the replay and throughput needs, reviewed as event volumes grow.",
            "Encryption in transit and at rest for message payloads carrying personal or financial data.",
            "Consumer lag monitoring: a growing gap between newest event and consumer offset is the early warning of overload.",
        ],
        "standards": [
            "Messaging patterns: enterprise integration patterns (Hohpe/Woolf) for queue, publish/subscribe, and competing-consumer designs.",
            "Kafka protocol and log semantics per the Kafka design documentation (Kreps et al., 2011).",
            "Managed queue services follow provider SLAs; message size limits and throughput quotas are provider-documented constraints.",
        ],
        "citations": [CIT_KAFKA, CIT_MQTT],
        "sig_lens": (
            "The Signature read: the queue is the covenant's patient "
            "courier, the stream its unforgetting chronicle. The "
            "Signature Cloud Method never lets a message die unheard - "
            "the courier waits, the chronicle remembers, and every "
            "handler swears to survive hearing the same news twice."
        ),
    },
    {
        "key": "cicd",
        "name": "CI and CD: Cloud Deployment Pipelines",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Continuous integration and continuous delivery are the "
            "assembly line of software: every code change flows through "
            "an automated pipeline that builds it, tests it, and ships "
            "it to production - dozens of times a day, without heroics. "
            "Continuous integration means developers merge to the main "
            "branch frequently, and each merge triggers automated builds "
            "and test suites, so integration pain is felt in minutes, "
            "not at release week. Continuous delivery extends the line: "
            "every green build is packaged into an immutable artifact "
            "(container image, deployment bundle) and staged for "
            "release, with production deployment one approval - or zero "
            "approvals, in continuous deployment - away. The pipeline "
            "stages are ritual: lint and unit tests (fast, every "
            "commit), integration and security scans (slower, every "
            "merge), staging deploy with smoke tests, then production "
            "with canary or blue-green strategy and automatic rollback. "
            "The cultural payoff is the real product: small changes, "
            "shipped constantly, each reversible in minutes, replacing "
            "the terror of the quarterly big-bang release."
        ),
        "how_it_works": (
            "A pipeline works as a directed graph of stages triggered by "
            "version control events. A push to the main branch (or a pull "
            "request) fires the pipeline: the build stage compiles code "
            "and builds the container image, tagged immutably with the "
            "commit hash. The test stage runs unit tests in parallel, "
            "then integration tests against ephemeral environments, plus "
            "static analysis and dependency vulnerability scans - any "
            "failure stops the line and notifies the author. The package "
            "stage pushes the image to the registry and signs it. The "
            "deploy stage applies the manifests to staging, runs smoke "
            "tests, then promotes to production using a safe strategy: "
            "canary (route 5 percent of traffic to the new version, "
            "watch error rates, then widen) or blue-green (stand up the "
            "full new fleet beside the old, flip the router, keep the "
            "old warm for instant rollback). Deployment automation is "
            "declarative - the pipeline applies the same manifests a "
            "human would, so the path from laptop to production has no "
            "manual snowflake steps."
        ),
        "key_points": [
            "CI merges small changes frequently with automated build and test on every commit; CD packages every green build into an immutable, releasable artifact.",
            "The pipeline is a quality gate sequence: fast unit tests, then integration plus security scans, then staged deploys with smoke tests.",
            "Immutable artifacts tagged by commit hash mean the tested thing is the shipped thing - no rebuilding between staging and production.",
            "Safe deploy strategies - canary and blue-green with automatic rollback - make releases boring instead of terrifying.",
            "Small, frequent, reversible changes beat rare big-bang releases on every measure: speed, safety, and engineer sanity.",
        ],
        "requirements": [
            "A comprehensive automated test suite fast enough to run per commit - a pipeline nobody waits for is a pipeline nobody trusts.",
            "Immutable artifact tagging (commit hash, never 'latest') from build through production.",
            "Security scanning in the pipeline: dependency vulnerabilities, image scans, and secret detection on every merge.",
            "A production deploy strategy with automatic rollback on health-check or error-rate failure.",
            "Branch protection: no direct pushes to main, required green pipeline and review before merge.",
        ],
        "standards": [
            "Pipeline-as-code: pipeline definitions stored in version control alongside the application (provider-agnostic principle).",
            "Artifact signing and provenance: SLSA framework levels for supply-chain integrity; image signing via Sigstore/Cosign conventions.",
            "Deployment safety patterns: canary analysis and blue-green deployment as documented in cloud architecture literature.",
        ],
        "citations": [CIT_OCI, CIT_WAFRAME],
        "sig_lens": (
            "The Signature read: the pipeline is the covenant's ritual "
            "of renewal - every change examined, every artifact sealed, "
            "every release reversible. The Signature Cloud Method ships "
            "in small sworn steps: what is built is tested, what is "
            "tested is sealed, what is sealed may sail - and any step "
            "may be unwound without shame."
        ),
    },
    {
        "key": "caching",
        "name": "Caching: Redis and Memcached",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Caching is the art of remembering answers: keeping "
            "frequently needed data in fast memory so the slow systems "
            "behind it - databases, APIs, computations - are asked once "
            "instead of a thousand times. The two classic in-memory "
            "stores are Memcached, the beautifully simple distributed "
            "key-value cache (get, set, delete, nothing else, sharded "
            "by client hashing), and Redis, the data-structure server "
            "that adds lists, sets, sorted sets, hashes, streams, and "
            "Lua scripting to the same in-memory speed, plus optional "
            "persistence and replication. The canonical pattern is "
            "cache-aside: the application checks the cache first, on a "
            "miss queries the database and stores the result with a "
            "time-to-live, on a hit skips the database entirely. Done "
            "well, caching cuts database load by an order of magnitude "
            "and response times from tens of milliseconds to under one. "
            "Done badly - no TTLs, no invalidation, cache as the system "
            "of record - it manufactures the subtlest bugs in "
            "engineering: stale data served with total confidence."
        ),
        "how_it_works": (
            "Cache-aside works as a polite shortcut. Read path: the app "
            "asks the cache for key 'user:8421'; on a hit it returns the "
            "cached JSON immediately; on a miss it queries the database, "
            "writes the result to the cache with a TTL (say 300 "
            "seconds), and returns it. Write path: the app updates the "
            "database, then deletes (or updates) the cache key - "
            "delete-on-write is simpler and safer than update-on-write, "
            "because the next read repopulates from the source of "
            "truth. TTLs bound staleness: even if invalidation is "
            "missed, the entry expires. Redis structures extend the "
            "vocabulary: sorted sets implement leaderboards and rate "
            "limiters (score by timestamp, trim old entries), lists "
            "implement queues, hashes store objects field-by-field, and "
            "streams add consumer-group messaging. Eviction policies "
            "(like allkeys-lru) decide what leaves when memory fills. "
            "For high availability, Redis replicates to replicas with "
            "automatic failover (Sentinel or Cluster); Memcached scales "
            "by adding nodes and letting clients hash across them."
        ),
        "key_points": [
            "Cache-aside is the core pattern: check cache, on miss read the database and store with a TTL - the database stays the system of record.",
            "Memcached is the simple sharded key-value cache; Redis adds data structures (sorted sets, hashes, streams) plus persistence and replication.",
            "TTLs bound staleness and delete-on-write keeps it simple: even missed invalidations expire on their own.",
            "Redis sorted sets natively implement leaderboards, rate limiters, and time-series windows - learn the structures and whole features collapse to one-liners.",
            "Never treat the cache as the system of record: caches evict, expire, and fail - the database is the truth, the cache is the shortcut.",
        ],
        "requirements": [
            "A TTL on every cached entry, chosen from the data's real freshness needs - no eternal keys.",
            "Invalidation on write for data that must be fresh, with TTL as the backstop for anything missed.",
            "Memory sizing plus an eviction policy matched to the workload (LRU for general use), monitored for eviction rate.",
            "Replication and failover for any cache whose loss would thundering-herd the database.",
            "Cache-hit-ratio dashboards: a falling ratio means keys, TTLs, or traffic patterns changed under you.",
        ],
        "standards": [
            "Redis data types, persistence, and replication per Redis documentation; Memcached protocol as implemented by memcached.org.",
            "Caching HTTP semantics where applicable: RFC 9111.",
            "Client sharding for Memcached commonly uses consistent hashing to minimize remapping on node changes.",
        ],
        "citations": [CIT_REDIS],
        "sig_lens": (
            "The Signature read: the cache is the covenant's ready "
            "memory - swift recall of sworn answers, never mistaken for "
            "the ledger itself. The Signature Cloud Method remembers "
            "eagerly but trusts the ledger: every cached answer carries "
            "its hour of expiry, and the truth is always re-readable "
            "from stone."
        ),
    },
    {
        "key": "edge",
        "name": "Edge Computing",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Edge computing moves computation out of the distant data "
            "center and onto devices near the data: the factory gateway, "
            "the cell tower, the retail store server, the camera itself. "
            "The motivation is physics and autonomy. Physics: a control "
            "loop that must react in 10 milliseconds cannot wait for a "
            "100-millisecond round trip to a region three time zones "
            "away. Autonomy: a mine, an oil rig, or a ship must keep "
            "running when the uplink dies. Bandwidth: a thousand cameras "
            "streaming raw video to the cloud is a ruinous bill; "
            "analyzing the video at the edge and sending only the "
            "'person detected at 14:02' event is cheap. Privacy: medical "
            "or biometric data analyzed on-device never crosses the "
            "internet at all. The architecture is a continuum, not a "
            "cliff: device edge (sensors and microcontrollers), far edge "
            "(gateways and on-prem servers), near edge (provider edge "
            "locations and 5G multi-access edge), and the regional cloud "
            "- with each tier handling what its latency, bandwidth, and "
            "compute budget suits, and the cloud remaining the training "
            "ground, the control plane, and the archive."
        ),
        "how_it_works": (
            "Edge computing works by placing the same cloud primitives - "
            "containers, functions, message brokers, ML inference - on "
            "small footprints near the data. A typical industrial setup: "
            "sensors publish readings over MQTT to a gateway running a "
            "local broker; stream-processing functions on the gateway "
            "filter, aggregate, and run anomaly detection; only "
            "exceptions and rollups sync to the cloud when connectivity "
            "allows, using store-and-forward queues that survive "
            "outages. Machine learning follows the train-in-cloud, "
            "infer-at-edge pattern: models train on the cloud's GPUs "
            "against the full historical dataset, then the compressed "
            "model ships to edge devices for millisecond inference. "
            "Management is the hard part at scale: fleets of thousands "
            "of edge nodes need the same deployment pipelines, "
            "monitoring, and security patching as the cloud, delivered "
            "over unreliable links - so edge platforms emphasize "
            "desired-state reconciliation (the node converges to the "
            "declared configuration whenever it can reach the control "
            "plane) and signed, atomic updates with automatic rollback."
        ),
        "key_points": [
            "Edge exists for physics (latency), autonomy (offline operation), bandwidth (filter before sending), and privacy (analyze without transmitting).",
            "The architecture is a continuum - device, far edge, near edge, regional cloud - with each tier doing what its latency and compute budget suits.",
            "Train in the cloud, infer at the edge: big GPUs learn from history, small devices decide in milliseconds.",
            "Store-and-forward messaging lets edge systems survive uplink outages and sync when the link returns.",
            "Fleet management is the real challenge: desired-state reconciliation, signed atomic updates, and monitoring across thousands of remote nodes.",
        ],
        "requirements": [
            "A latency budget per workload proving the edge is necessary - if 100 milliseconds is fine, the regional cloud is simpler.",
            "Offline autonomy designed in: local decision-making and store-and-forward for the workloads that must survive disconnection.",
            "The same deployment pipeline and monitoring for edge nodes as for cloud workloads, adapted to constrained links.",
            "Signed updates with automatic rollback, since a bricked remote gateway may require a very expensive truck roll.",
            "Physical security for edge hardware: locked enclosures, encrypted disks, and tamper-evident seals where the threat model demands it.",
        ],
        "standards": [
            "Edge architecture frameworks: ETSI MEC (multi-access edge computing) for telco edge; LF Edge projects for open edge stacks.",
            "IoT device messaging commonly uses MQTT (ISO/IEC 20922) between devices and edge gateways.",
            "Model deployment to edge follows ONNX or provider edge-runtime formats for portable inference.",
        ],
        "citations": [CIT_MQTT, CIT_NIST145],
        "sig_lens": (
            "The Signature read: the edge is the covenant's far watch - "
            "sworn sentinels posted where the data is born, deciding in "
            "the instant the distant temple cannot. The Signature Cloud "
            "Method trains its wisdom centrally but stations its judgment "
            "at the frontier: the watch decides now, the temple remembers "
            "forever."
        ),
    },
    {
        "key": "iot",
        "name": "IoT Connectivity: MQTT and Device Fleets",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The Internet of Things is the internet's second population "
            "explosion: not people and phones but sensors, meters, "
            "vehicles, appliances, and industrial machines - tens of "
            "billions of devices, most too small to run a web browser, "
            "many on batteries that must last years. They speak "
            "lightweight protocols designed for their constraints. MQTT, "
            "the workhorse, is a publish/subscribe messaging protocol "
            "so light its header can be two bytes: devices publish "
            "readings to topics like factory/line3/temperature, and any "
            "number of subscribers - dashboards, alerting engines, "
            "archivers - receive them, with the broker in the middle "
            "decoupling everyone. Three quality-of-service levels trade "
            "guarantees for cost: at most once (fire and forget), at "
            "least once (acknowledged, may duplicate), exactly once "
            "(acknowledged without duplicates). Around the protocol sits "
            "the fleet problem: provisioning unique identities to "
            "millions of devices, rotating their certificates, pushing "
            "firmware updates without bricking them, and knowing which "
            "ones have gone silent. Connectivity is the easy ten "
            "percent; fleet operations are the ninety."
        ),
        "how_it_works": (
            "MQTT works through a broker and topics. A device opens a "
            "long-lived TCP (or TLS) connection to the broker and "
            "publishes messages to hierarchical topics; the broker fans "
            "each message out to all current subscribers of matching "
            "topic filters (wildcards + for one level, # for many). "
            "Sessions can be persistent: the broker queues messages for "
            "a sleeping device (using its last-will message to announce "
            "unexpected disconnection) and delivers on reconnect. QoS 0 "
            "sends once, QoS 1 acknowledges and retries (duplicates "
            "possible), QoS 2 completes a four-step handshake for "
            "exactly-once. Retained messages let new subscribers "
            "instantly get the last known value. Fleet management layers "
            "on top: each device gets a unique X.509 certificate at "
            "manufacture or first boot (just-in-time provisioning), the "
            "device shadows (digital twins) in the cloud hold desired vs "
            "reported state so apps read state without waking devices, "
            "and jobs roll out firmware in staged waves with automatic "
            "halt on failure signals. Constrained devices that cannot "
            "hold TLS use lightweight cousins like MQTT-SN over UDP or "
            "CoAP, often through a gateway that speaks full MQTT "
            "upstream."
        ),
        "key_points": [
            "MQTT is the IoT workhorse: two-byte-header publish/subscribe over topics, with a broker decoupling millions of tiny publishers from their subscribers.",
            "QoS levels trade guarantees for cost: 0 fire-and-forget, 1 acknowledged (may duplicate), 2 exactly-once - match the level to the consequence of loss.",
            "Retained messages plus last-will give every device a persistent presence: newcomers learn the last value, the broker announces silent deaths.",
            "Digital twins (device shadows) separate desired state from reported state, letting apps command sleeping devices asynchronously.",
            "Fleet operations dominate: unique per-device identities, certificate rotation, staged firmware rollouts, and silence detection at scale.",
        ],
        "requirements": [
            "Unique cryptographic identity per device (X.509 certificates), provisioned securely at manufacture or first boot - no shared fleet-wide passwords.",
            "TLS on every device-to-cloud connection, with a cipher suite the smallest device in the fleet can actually afford.",
            "A firmware update pipeline with staged rollouts, health gates, and automatic halt - a bad fleet-wide push is a catastrophe, not a bug.",
            "Device shadows or twins so applications tolerate sleeping, roaming, and intermittently connected devices.",
            "Silence detection and alerting: in IoT, a device that stops talking is often the most important event of all.",
        ],
        "standards": [
            "MQTT v3.1.1: ISO/IEC 20922:2016; MQTT v5.0: ISO/IEC 20922:2020 (adds reason codes, shared subscriptions, user properties).",
            "Constrained devices: CoAP (RFC 7252) and MQTT-SN; device identity via X.509 (RFC 5280).",
            "IoT security baselines: NISTIR 8259 series (foundational cybersecurity for IoT devices).",
        ],
        "citations": [CIT_MQTT],
        "sig_lens": (
            "The Signature read: the device fleet is the covenant's "
            "countless quiet witnesses - each sworn to report truly, "
            "each sealed with its own name. The Signature Cloud Method "
            "gives every witness an unforgeable seal, listens through "
            "the patient broker, and treats a fallen silent witness as "
            "the loudest alarm of all."
        ),
    },
    {
        "key": "cloud_security",
        "name": "Cloud Security: The Shared Responsibility Model",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Cloud security rests on one sentence: the provider secures "
            "the cloud itself, and you secure what you put in it. The "
            "provider owns the physical buildings, the hypervisors, the "
            "network fabric, and the managed services' underlying "
            "infrastructure. You own everything you configure: your "
            "data, your access policies, your firewall rules, your "
            "application code, your encryption keys' usage. The line "
            "moves with the service model - with IaaS you patch the "
            "guest OS, with PaaS the provider does, with SaaS you own "
            "only data and access - but it never vanishes. The threat "
            "landscape this record maps: misconfigured storage buckets "
            "exposed to the world (the classic cloud breach), stolen or "
            "over-broad credentials, unpatched application "
            "vulnerabilities, malicious insiders, and supply-chain "
            "compromise through dependencies. The defensive program: "
            "encrypt everything (in transit and at rest), log everything "
            "(every API call, every packet decision), least-privilege "
            "everything, patch relentlessly, and assume breach - design "
            "so that any single compromise is contained by the layers "
            "around it."
        ),
        "how_it_works": (
            "The shared responsibility model works by contract and "
            "controls. The provider publishes exactly what it secures "
            "(physical security, host patching, managed-service "
            "infrastructure) and attests to it through compliance "
            "certifications (SOC 2, ISO 27001) that you inherit for "
            "your own audits. Your side is implemented through "
            "guardrails: organization-level policies that forbid "
            "dangerous configurations (no public buckets, no unencrypted "
            "databases, no resources outside approved regions), "
            "detective controls that alert on drift (a bucket made "
            "public triggers an alarm and auto-remediation), and the "
            "IAM, network, and encryption disciplines taught across this "
            "database. Logging closes the loop: cloud audit trails "
            "record every API call with identity, source, and result; "
            "flow logs record network decisions; these feed a security "
            "monitoring pipeline with detection rules and incident "
            "runbooks. Assume-breach design means blast-radius thinking: "
            "separate accounts per environment, separate networks per "
            "tier, so one stolen credential opens one room, not the "
            "building."
        ),
        "key_points": [
            "One sentence governs: the provider secures the cloud itself, you secure what you put in it - the line moves with IaaS/PaaS/SaaS but never vanishes.",
            "Most cloud breaches are misconfiguration and credential theft, not exotic exploits - guardrails beat heroics.",
            "Preventive guardrails (organization policies forbidding dangerous configs) plus detective controls (drift alarms with auto-remediation) form the program.",
            "Log everything: API audit trails, network flow logs, DNS query logs - you cannot investigate what you did not record.",
            "Assume breach and design blast radius: separate accounts, separate networks, so one compromise opens one room, not the building.",
        ],
        "requirements": [
            "Organization-level guardrails denying public storage, unencrypted databases, and unapproved regions before workloads exist.",
            "Centralized audit logging with tamper-evident retention, feeding detection rules with staffed response runbooks.",
            "Encryption at rest and in transit as non-negotiable defaults, with customer-managed keys for regulated data.",
            "Account separation per environment (production isolated from development) with no shared credentials across the boundary.",
            "A tested incident response plan: who declares, who contains, who communicates - rehearsed before the incident, not during.",
        ],
        "standards": [
            "Control catalogs: NIST SP 800-53 Rev. 5; cloud security guidance: NIST SP 800-144 and SP 800-210.",
            "Assurance inheritance: SOC 2 Type II and ISO/IEC 27001 certifications published by providers.",
            "Incident handling: NIST SP 800-61 incident response lifecycle (prepare, detect, contain, eradicate, recover, learn).",
        ],
        "citations": [CIT_NIST853, CIT_NIST145],
        "sig_lens": (
            "The Signature read: security is the covenant's guarded "
            "gate and its watchful scribes. The provider guards the "
            "city walls; the Signature Cloud Method guards everything "
            "within - every door locked by least privilege, every "
            "footstep recorded by the scribes, every room sealed so one "
            "breach cannot become a rout."
        ),
    },
]

ENTRIES += [
    {
        "key": "ddos_waf",
        "name": "DDoS Defense and Web Application Firewalls",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Two different shields guard the public cloud, against two "
            "different enemies. Distributed denial of service (DDoS) is "
            "brute force: botnets of compromised devices flood your "
            "servers with more traffic than they can process - volumetric "
            "floods measured in terabits per second, protocol attacks "
            "exhausting connection tables, application-layer floods of "
            "seemingly legitimate requests. Defense is absorption plus "
            "scrubbing: the enormous spare capacity of cloud and CDN "
            "edges soaks up the flood, while scrubbing centers separate "
            "attack traffic from real users by signature, rate, and "
            "behavioral analysis. The web application firewall (WAF) "
            "fights the opposite enemy: the single clever request - SQL "
            "injection smuggled in a form field, cross-site scripting in "
            "a comment, a path traversal reaching for /etc/passwd. The "
            "WAF inspects every HTTP request against managed rule sets "
            "(covering the OWASP Top 10) plus your custom rules, blocking "
            "the malicious and logging the suspicious. Together with the "
            "CDN and the load balancer from earlier records, they form "
            "the standard public-facing defensive stack: absorb the "
            "flood, inspect the clever."
        ),
        "how_it_works": (
            "DDoS defense works in layers. Always-on monitoring watches "
            "traffic baselines per endpoint; when volume or pattern "
            "deviates, mitigation engages: edge locations announce your "
            "address space (anycast) so attack traffic spreads across "
            "dozens of scrubbing sites instead of concentrating on one; "
            "each site applies filters - dropping known attack signatures, "
            "rate-limiting aggressive sources, challenging suspicious "
            "clients with JavaScript or CAPTCHA puzzles that botnets "
            "usually fail - and forwards only clean traffic to your "
            "origin over protected links. Application-layer attacks get "
            "behavioral treatment: request rates per IP, per session, "
            "per endpoint, with adaptive thresholds. The WAF works as an "
            "HTTP inspection proxy in front of the application: every "
            "request's method, path, headers, and body are matched "
            "against rule groups - SQL injection patterns, XSS payloads, "
            "known-bad user agents, geographic blocks, rate limits per "
            "IP. Managed rule sets update as new vulnerability classes "
            "emerge; custom rules encode your application's specific "
            "abuse patterns. WAFs run in count mode first (log what "
            "would block) so rules are tuned against real traffic "
            "before they enforce."
        ),
        "key_points": [
            "DDoS is brute-force flood (volumetric, protocol, application-layer); defense is absorption at planetary scale plus scrubbing that separates attack from legitimate traffic.",
            "Anycast spreads the flood across dozens of scrubbing sites; behavioral challenges (JS puzzles, CAPTCHAs) filter botnets from humans.",
            "The WAF fights the clever single request: SQL injection, XSS, path traversal - inspected against managed rules (OWASP Top 10) plus your custom rules.",
            "Run new WAF rules in count mode first: tune against real traffic before enforcing, or the shield blocks your own customers.",
            "The standard public stack is CDN plus WAF plus load balancer: absorb the flood at the edge, inspect the clever at the gate, spread the legitimate across backends.",
        ],
        "requirements": [
            "DDoS protection engaged before launch on every public endpoint - attack traffic arrives within hours of publicity, not months.",
            "A WAF in front of every public web application, with managed OWASP rule sets enabled and tuned.",
            "Origin shielding so attackers cannot bypass the CDN/WAF and hit your servers directly.",
            "Rate limiting per IP and per endpoint as a baseline control, tuned to legitimate peak usage plus headroom.",
            "An incident runbook for active attacks: who engages the provider's rapid-response team, what gets shed first, how customers are informed.",
        ],
        "standards": [
            "Web attack taxonomy: the OWASP Top 10; WAF rule semantics commonly follow the ModSecurity/CRS rule language lineage.",
            "DDoS taxonomy: volumetric, protocol, and application-layer classes per industry practice; mitigation capacity measured in Tbps.",
            "TLS and HSTS at the edge per RFC 8446 and RFC 6797 so the defensive stack never downgrades to plaintext.",
        ],
        "citations": [CIT_RFC8446],
        "sig_lens": (
            "The Signature read: these are the covenant's two shields - "
            "the great seawall that breaks the flood, and the keen-eyed "
            "gatekeeper who knows a dagger hidden in a scroll. The "
            "Signature Cloud Method raises both before the city opens "
            "its gates: the flood shall break upon the wall, and no "
            "clever poison shall pass the gatekeeper's eye."
        ),
    },
    {
        "key": "zero_trust",
        "name": "Zero Trust Network Architecture",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Zero trust is the security doctrine that ends the castle-"
            "and-moat era: never trust, always verify. The old model "
            "trusted everything inside the corporate network and "
            "suspected everything outside; attackers learned to breach "
            "the perimeter once and roam freely within. Zero trust "
            "assumes the network is already hostile - inside and out - "
            "and grants access per request, per resource, based on "
            "identity, device health, and context, never on network "
            "location. Its tenets, formalized by NIST: all data sources "
            "and services are resources to protect; all communication is "
            "secured regardless of location; access is granted per "
            "session with least privilege; policy is dynamic, computed "
            "from identity, device posture, behavior, and threat "
            "intelligence; the enterprise monitors everything and "
            "improves continuously. In practice this means "
            "identity-aware proxies instead of VPNs, micro-segmentation "
            "instead of flat networks, device certificates proving "
            "health before access, and continuous re-verification "
            "instead of one login at 9 AM. It is not a product but an "
            "architecture - and the direction every serious cloud "
            "security program is walking."
        ),
        "how_it_works": (
            "Zero trust works through policy decision and enforcement "
            "points on every access. When a user (or service) requests a "
            "resource, the request hits a policy enforcement point - an "
            "identity-aware proxy, a service-mesh sidecar, a device "
            "agent. The enforcement point asks the policy engine: who "
            "is this (strong authentication, MFA), what device is this "
            "(managed, patched, encrypted, with a valid certificate), "
            "what is the context (location, time, recent behavior, "
            "threat feeds)? The engine evaluates policy - allow this "
            "identity on this device to read this database, deny the "
            "admin console from unmanaged devices - and returns a "
            "short-lived decision, often a token valid for minutes. "
            "Micro-segmentation shrinks the network into tiny zones: "
            "workloads carry identities (not just IP addresses) and "
            "only declared pairs may communicate, so a compromised web "
            "server cannot wander to the database. Continuous "
            "diagnostics re-evaluate: a device falling out of patch "
            "compliance loses access mid-session. Implementation usually "
            "proceeds in waves: identity and MFA first, then device "
            "inventory, then application proxying, then segmentation - "
            "each wave shrinking implicit trust further."
        ),
        "key_points": [
            "Never trust, always verify: access is granted per session from identity, device health, and context - never from network location.",
            "The perimeter is dead as a trust boundary: assume breach inside and out, and make every access prove itself.",
            "Policy engine plus enforcement points: identity-aware proxies, mesh sidecars, and agents ask 'who, what device, what context' on every request.",
            "Micro-segmentation replaces flat networks: workloads carry identities and only declared pairs communicate, containing any compromise.",
            "Zero trust is an architecture walked in waves - identity and MFA, device inventory, application proxying, segmentation - not a product purchased once.",
        ],
        "requirements": [
            "Strong identity for every human and workload: MFA for people, cryptographic workload identity for services.",
            "A complete device inventory with health attestation (managed, patched, encrypted) as an access input.",
            "Identity-aware access to applications replacing broad network VPNs, with per-session short-lived authorization.",
            "Micro-segmentation policy declaring allowed workload-to-workload communication, default deny between segments.",
            "Continuous monitoring feeding the policy engine: behavior analytics and threat intelligence that can revoke trust mid-session.",
        ],
        "standards": [
            "NIST SP 800-207: Zero Trust Architecture - the canonical tenets and deployment models.",
            "Device identity commonly via X.509 certificates (RFC 5280); workload identity via SPIFFE/SPIRE standards.",
            "Federal implementations follow OMB M-22-09 and CISA's Zero Trust Maturity Model (for US government context).",
        ],
        "citations": [CIT_NIST207, CIT_NIST853],
        "sig_lens": (
            "The Signature read: zero trust is the covenant's final "
            "honesty - no courtyard is safe, no livery is proof, every "
            "visitor proves themselves at every door. The Signature "
            "Cloud Method abolishes the trusted courtyard: the seal is "
            "checked at each threshold, the watch never sleeps, and "
            "trust is re-earned with every single step."
        ),
    },
    {
        "key": "multicloud",
        "name": "Multi-Cloud and Hybrid Architecture",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Multi-cloud is the deliberate use of two or more public "
            "clouds - and usually the private data center too - as one "
            "system. The motives are real: avoiding single-provider "
            "dependence (when one cloud has a bad day, you are not "
            "entirely down), using each provider's best service (one's "
            "machine learning platform, another's global network), "
            "satisfying data-residency rules that differ by country, and "
            "negotiating leverage. The costs are equally real: every "
            "provider's networking, identity, and managed services work "
            "differently, so the team operates two or three platforms "
            "instead of one; data transfer between clouds is metered "
            "and slow; and consistency of deployment, monitoring, and "
            "security policy across providers is a permanent engineering "
            "tax. The architectures that survive are opinionated: "
            "workloads placed whole (the entire payments stack on one "
            "cloud, analytics on another) rather than smeared across "
            "both, connected by private interconnects, governed by one "
            "identity system and one deployment pipeline. Multi-cloud "
            "done accidentally is just twice the operational burden; "
            "done deliberately, it is resilience and leverage."
        ),
        "how_it_works": (
            "Multi-cloud works through abstraction and interconnection. "
            "The control plane is unified first: one identity provider "
            "federating into every cloud's IAM, one CI/CD pipeline "
            "deploying to all targets, one monitoring system scraping "
            "metrics from everywhere, infrastructure as code with per-"
            "cloud modules behind common interfaces. Connectivity runs "
            "over private interconnects or encrypted tunnels between "
            "clouds, with careful routing so cross-cloud traffic takes "
            "the private path instead of the metered public internet. "
            "Kubernetes is the common workload substrate: the same "
            "container images and manifests deploy to managed clusters "
            "in each cloud, with a service mesh or multi-cluster "
            "gateway handling cross-cloud service discovery and "
            "failover. Data placement follows gravity and law: each "
            "dataset lives primarily in one cloud (replicated for "
            "disaster recovery, not active-active, unless the business "
            "pays for the complexity), with residency rules pinning "
            "regulated data to approved jurisdictions. Cost governance "
            "is centralized: one FinOps view across all providers, "
            "because three separate bills hide three separate wastes."
        ),
        "key_points": [
            "Multi-cloud motives: resilience against provider failure, best-of-breed services, data residency, negotiating leverage - each must outweigh the operational tax.",
            "Place workloads whole per cloud, not smeared across both: the entire stack in one place, connected deliberately, beats a distributed tangle.",
            "Unify the control plane first: one identity, one pipeline, one monitoring system, infrastructure as code with per-cloud modules.",
            "Data follows gravity and law: primary home per dataset, cross-cloud replication for recovery - active-active across providers is a luxury good.",
            "Centralize cost governance: one FinOps view across providers, because separate bills hide separate wastes.",
        ],
        "requirements": [
            "A written motive per additional cloud with its cost-benefit case - 'strategy' without arithmetic is just complexity.",
            "Federated identity and a single deployment pipeline spanning all providers before the second workload lands.",
            "Private interconnects between clouds for production traffic, with routing that avoids the metered public path.",
            "A data placement map: primary home, residency jurisdiction, and recovery copy for every regulated dataset.",
            "Unified monitoring, logging, and cost dashboards - operational truth must not require three consoles.",
        ],
        "standards": [
            "Interoperability and portability considerations: ISO/IEC 19941; workload portability via OCI images and Kubernetes APIs.",
            "Identity federation: SAML 2.0 / OpenID Connect across providers; network interconnect security per provider documentation.",
            "Residency compliance derives from applicable statutes (e.g. GDPR Chapter V for EU data) applied per dataset.",
        ],
        "citations": [CIT_ISO17788, CIT_OCI, CIT_K8S],
        "sig_lens": (
            "The Signature read: multi-cloud is the covenant sworn in "
            "several courts at once - each court honored in its own "
            "tongue, all answering to one seal. The Signature Cloud "
            "Method keeps one oath across many grounds: one identity, "
            "one pipeline, one watchful eye - and each workload housed "
            "whole where its nature thrives."
        ),
    },
    {
        "key": "observability",
        "name": "Observability: Logs, Metrics, and Traces",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Observability is the discipline of knowing what your "
            "systems are doing without having to guess: the "
            "instrumentation that turns 'the site is slow' into 'the "
            "payments database replica lagged 4 seconds starting at "
            "14:03 because the nightly report query began'. It rests on "
            "three pillars. Logs are the diary: timestamped lines of "
            "what happened ('user 8421 checked out, order 99120, 200 "
            "OK'), indispensable for forensics, expensive at scale. "
            "Metrics are the vital signs: numbers over time (requests "
            "per second, error rate, CPU, queue depth), cheap to store "
            "and perfect for dashboards and alarms. Traces follow one "
            "request across services: the web call that touched the "
            "auth service, the catalog, and the database, stitched into "
            "one timeline showing exactly where the 800 milliseconds "
            "went. Mature practice adds the fourth signal, profiles, "
            "and the connective tissue: every log line and metric "
            "carrying the same request ID, so the three pillars answer "
            "together. The cultural rule: instrument first, because the "
            "outage you cannot see is the outage you cannot fix."
        ),
        "how_it_works": (
            "Observability works as a telemetry pipeline. Applications "
            "emit: structured logs (JSON lines with timestamp, level, "
            "request ID, and fields) to stdout, collected by agents; "
            "metrics (counters, gauges, histograms) to a time-series "
            "store via pull or push; traces via instrumentation that "
            "propagates a trace ID in request headers across service "
            "boundaries, each service recording spans (named timed "
            "operations) to a collector. The pipeline aggregates, "
            "indexes, and retains: hot storage for the last days "
            "(fast queries during incidents), warm and cold tiers for "
            "history. Dashboards visualize the vital signs; alerting "
            "rules fire on symptoms (error rate above threshold, "
            "latency percentile breached), not just causes, and route "
            "to the on-call with runbook links. Distributed tracing "
            "solves the microservices mystery: with dozens of services, "
            "only the trace shows which hop owned the latency. Sampling "
            "controls cost: keep every error trace, sample a fraction "
            "of successes. Cardinality discipline keeps metrics "
            "affordable: label values must stay bounded, or the "
            "time-series store drowns in a million unique series."
        ),
        "key_points": [
            "Three pillars: logs (the diary, for forensics), metrics (the vital signs, for dashboards and alarms), traces (one request's journey across services).",
            "Correlate with request IDs across all three: the trace finds the slow hop, the logs explain it, the metrics show how widespread it is.",
            "Alert on symptoms (error rate, latency percentiles), not just causes - symptoms catch the failures you never predicted.",
            "Sampling controls trace cost (keep all errors, sample successes); cardinality discipline controls metrics cost (bounded label values).",
            "Instrument first: the outage you cannot see is the outage you cannot fix - observability is built in, not bolted on after.",
        ],
        "requirements": [
            "Structured logging with request IDs from every service, collected centrally with hot retention covering the incident window.",
            "Dashboards for the four golden signals per service: latency, traffic, errors, saturation.",
            "Alerting rules on symptoms with runbook links, tuned to page humans only for user-facing impact.",
            "Distributed tracing across service boundaries with consistent header propagation.",
            "Retention and sampling policies balancing forensic needs against storage cost, reviewed as traffic grows.",
        ],
        "standards": [
            "Telemetry formats: OpenTelemetry (CNCF) for traces, metrics, and logs - vendor-neutral instrumentation.",
            "Log levels and structured logging conventions per engineering practice; metric types (counter, gauge, histogram) per Prometheus/OpenMetrics exposition.",
            "Alerting philosophy: symptom-based alerting per Google SRE practices (latency, traffic, errors, saturation).",
        ],
        "citations": [CIT_WAFRAME],
        "sig_lens": (
            "The Signature read: observability is the covenant's "
            "honest mirror - the diary, the pulse, and the traced "
            "footstep of every servant. The Signature Cloud Method "
            "watches its own household without flinching: the slow "
            "servant is found, the failing oath is named, and no "
            "outage hides in the dark."
        ),
    },
    {
        "key": "finops",
        "name": "Cloud Cost Engineering and FinOps",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The cloud's meter never sleeps, and without discipline the "
            "bill becomes the architecture's loudest critic. FinOps - "
            "cloud financial operations - is the practice of making "
            "spend visible, accountable, and efficient: engineering, "
            "finance, and product sharing one view of what everything "
            "costs and who ordered it. The levers: rightsizing (matching "
            "instance sizes to actual utilization - the cloud's most "
            "common waste is oversized servers idling at 8 percent CPU), "
            "commitment discounts (one- or three-year commitments and "
            "savings plans cutting steady-state compute by up to about "
            "70 percent versus on-demand), spot and preemptible capacity "
            "(spare capacity at deep discounts for fault-tolerant work), "
            "storage lifecycle (aging data to cheaper tiers, deleting "
            "what nobody needs), and network egress discipline (data "
            "transfer out is metered - keep traffic inside regions and "
            "behind CDNs). The organizational machinery: every resource "
            "tagged with owner, project, and environment; budgets with "
            "alerts per team; showback or chargeback so spend has a "
            "name attached; and a regular cadence reviewing the top "
            "spend drivers. The mindset shift: in the cloud, cost is an "
            "architectural property, designed in like latency or "
            "reliability - not a finance surprise at month's end."
        ),
        "how_it_works": (
            "FinOps works as a continuous loop: inform, optimize, "
            "operate. Inform: cost and usage data flows into dashboards "
            "broken down by tag (team, project, environment), with "
            "anomaly detection flagging sudden spikes - the forgotten "
            "load test, the runaway scaler. Optimize: rightsizing "
            "recommendations compare provisioned versus utilized CPU, "
            "memory, and IOPS per resource and propose smaller shapes; "
            "commitment analyzers find steady-state usage to cover with "
            "savings plans; idle detectors find unattached disks, "
            "orphaned snapshots, and load balancers with no backends. "
            "Operate: budgets per team with progressive alerts (50, 80, "
            "100 percent), automated policies (delete unattached "
            "volumes after N days, enforce lifecycle tiers), and "
            "deployment-time cost estimates in the pipeline so a pull "
            "request shows its monthly price. Unit economics close the "
            "loop: cost per request, per user, per order - so growth "
            "conversations are about efficiency, not just totals. The "
            "demo computes a rightsizing saving and a commitment-"
            "discount comparison from sample utilization data."
        ),
        "key_points": [
            "FinOps loop: inform (tag everything, dashboard spend, detect anomalies), optimize (rightsize, commit, use spot), operate (budgets, automation, unit economics).",
            "Rightsizing is the biggest lever: oversized idle servers are the cloud's most common waste - match shape to measured utilization.",
            "Commitment discounts (savings plans, reserved capacity) cut steady-state compute dramatically; spot capacity discounts fault-tolerant work deeply.",
            "Tag every resource with owner, project, and environment: untagged spend is unowned spend, and unowned spend never shrinks.",
            "Cost is an architectural property: estimate it in the deployment pipeline and track unit economics (cost per request), not just monthly totals.",
        ],
        "requirements": [
            "Mandatory tagging policy (owner, project, environment) enforced at creation, with untagged-resource reporting.",
            "Budgets with progressive alerts per team and anomaly detection on the total bill.",
            "A quarterly rightsizing and commitment review cadence with named owners for the top ten spend drivers.",
            "Storage lifecycle policies and idle-resource automation (unattached volumes, old snapshots) running continuously.",
            "Unit economics tracked per product: cost per request, per user, or per order, trended over time.",
        ],
        "standards": [
            "FinOps Framework (FinOps Foundation): inform, optimize, operate phases and capabilities.",
            "Commitment instruments: savings plans and reserved instances per provider documentation; spot/preemptible semantics per provider SLA.",
            "Cost allocation follows tagging standards defined per organization; showback/chargeback models per FinOps practice.",
        ],
        "citations": [CIT_NIST145, CIT_WAFRAME],
        "sig_lens": (
            "The Signature read: FinOps is the covenant's honest "
            "ledger of coin - every servant's wage recorded, every idle "
            "hour questioned, every bargain honored. The Signature "
            "Cloud Method spends deliberately: the right strength for "
            "the hour, the long oath discounted, and no coin paid for "
            "strength that sleeps."
        ),
    },
    {
        "key": "disaster_recovery",
        "name": "Disaster Recovery and Cloud Backups",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Disaster recovery is the answer to the question nobody "
            "wants to ask: when the region burns - literally or "
            "figuratively - how do we come back, and how much do we "
            "lose? Two numbers frame every plan. RPO, the recovery "
            "point objective, is how much data you can afford to lose, "
            "measured in time: an RPO of one hour means backups at "
            "least hourly. RTO, the recovery time objective, is how "
            "long you can afford to be down: an RTO of four hours "
            "means the business survives a four-hour outage, not a "
            "four-day one. The strategies form a ladder of cost and "
            "speed: backup and restore (cheapest, slowest - data "
            "copied to another region, rebuilt when needed), pilot "
            "light (core data replicated, servers launched on "
            "disaster), warm standby (a scaled-down copy running, "
            "scaled up on failover), and multi-site active-active (full "
            "capacity in two regions, fastest and dearest). Backups "
            "themselves are a discipline: automated, encrypted, tested "
            "by restore (an untested backup is a rumor), versioned "
            "against ransomware (immutable copies the attacker cannot "
            "delete), and retained per policy. The cloud's gift to DR "
            "is that the second site costs nearly nothing until the "
            "day you need it."
        ),
        "how_it_works": (
            "Disaster recovery works by rehearsed replication and "
            "promotion. Data protection: databases stream transaction "
            "logs or snapshots cross-region continuously (pilot light "
            "and above) or on schedule (backup and restore); object "
            "storage replicates buckets cross-region with versioning, "
            "so even a ransomware encryption of the primary leaves "
            "clean versions in the replica. Infrastructure is code: "
            "the entire environment - networks, servers, databases, "
            "DNS - is declared in templates that can be applied to the "
            "recovery region in minutes, which is what makes pilot "
            "light and warm standby practical. Failover is DNS and "
            "routing: health checks detect the primary's death, DNS "
            "fails over to the recovery region's endpoints (with TTLs "
            "kept low on critical records), and traffic flows to the "
            "promoted standby. Failback reverses the dance when the "
            "primary heals. Testing is the whole game: game days that "
            "actually fail over production (or a faithful shadow), "
            "restore drills that rebuild from backup to a scratch "
            "environment and verify the application boots and the data "
            "is intact. The demo computes RPO/RTO feasibility from "
            "backup intervals and models data-loss windows."
        ),
        "key_points": [
            "RPO is how much data you may lose (time), RTO is how long you may be down - every DR decision is priced in these two numbers.",
            "Four strategies climb cost and speed: backup/restore, pilot light, warm standby, multi-site active-active - match the strategy to the RPO/RTO, not to ambition.",
            "Infrastructure as code makes the second site nearly free until needed: the recovery environment is a template application away.",
            "Backups must be automated, encrypted, immutable (ransomware cannot delete what it cannot rewrite), and restore-tested - untested backups are rumors.",
            "Failover is DNS plus health checks; failback is the rehearsed return - both must be drilled, because the first real failover is the wrong time to learn.",
        ],
        "requirements": [
            "Written RPO and RTO per workload tier, signed off by the business owners who will live with them.",
            "Cross-region replication or backup for every production dataset, with immutability against ransomware.",
            "The full environment declarable as code and appliable to the recovery region - no snowflake servers that exist in one region only.",
            "Failover and restore drills on a schedule (at least annually for backup/restore, more often for standby strategies), with findings remediated.",
            "Low TTLs on failover-critical DNS records and health-checked endpoints driving the traffic shift.",
        ],
        "standards": [
            "Contingency planning: NIST SP 800-34 Rev. 1; backup guidance per NIST SP 800-53 (CP family).",
            "Ransomware-resistant backup design follows CISA and NIST guidance on immutable, offline/air-gapped copies.",
            "DNS failover mechanics per RFC 1034/1035 TTL semantics; health-check-driven routing per provider documentation.",
        ],
        "citations": [CIT_NIST853, CIT_RFC1034],
        "sig_lens": (
            "The Signature read: disaster recovery is the covenant's "
            "resurrection oath - the promise that even if the temple "
            "falls, the tablets survive and the temple rises again. The "
            "Signature Cloud Method writes its memory in two lands, "
            "rehearses the rising, and seals the copies where no "
            "ransom can reach."
        ),
    },
]

ENTRIES += [
    {
        "key": "iac",
        "name": "Infrastructure as Code",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Infrastructure as code is the practice of declaring your "
            "entire cloud environment - networks, servers, databases, "
            "firewalls, DNS - in version-controlled text files instead "
            "of clicking it into existence, so the whole system is "
            "reviewable, repeatable, and rebuildable. The tool reads "
            "your declarations and converges reality to match: creating "
            "what is missing, updating what drifted, and (with care) "
            "destroying what should not exist. Two philosophies share "
            "the space: declarative tools (describe the desired end "
            "state; the engine plans the steps) and imperative or "
            "procedural tooling (script the steps). State files track "
            "what was created so updates and destroys are precise; "
            "remote state with locking lets teams collaborate without "
            "corrupting each other. The disciplines that make it safe: "
            "plan before apply (review the proposed changes like code "
            "review), modules for reuse (one vetted network module "
            "used by every team), drift detection (alert when reality "
            "diverges from the declaration), and secrets never in the "
            "code (referenced from the secrets manager). The payoff is "
            "total: environments spun up identically for dev, staging, "
            "and prod; disaster recovery as a re-application; and the "
            "end of snowflake infrastructure that only one engineer "
            "understands."
        ),
        "how_it_works": (
            "Infrastructure as code works as a reconciliation loop over "
            "a state file. You write declarations: 'a virtual network "
            "10.0.0.0/16, two subnets, a database with these settings'. "
            "The plan phase compares declarations against the state "
            "file and the live cloud APIs, producing a diff: 3 to add, "
            "1 to change, 0 to destroy. You review the diff; the apply "
            "phase executes it through the provider APIs, updating the "
            "state file with the real IDs created. On the next run, "
            "the same comparison detects drift - someone's manual "
            "console change - and offers to revert it. Modules package "
            "reusable patterns (a 'production network' module with "
            "subnets, gateways, and flow logs) parameterized per use. "
            "Remote backends store state in versioned object storage "
            "with a lock (so two applies cannot interleave), and "
            "workspaces or directory structures separate environments. "
            "Policy as code gates the pipeline: rules that reject "
            "plans creating public databases or unencrypted storage "
            "before they ever apply. Secrets are passed as variables "
            "from the secrets manager at apply time, never committed."
        ),
        "key_points": [
            "Declare the environment in version-controlled text; the tool converges reality to the declaration - reviewable, repeatable, rebuildable infrastructure.",
            "Plan before apply: the diff is a code review for infrastructure - never apply a plan you have not read.",
            "State files are the memory: remote, versioned, and locked, so teams collaborate without corrupting each other's reality.",
            "Modules package vetted patterns once and reuse them everywhere; drift detection reverts the manual console changes that rot environments.",
            "Policy as code rejects dangerous plans before apply; secrets are referenced from the manager, never committed to the declarations.",
        ],
        "requirements": [
            "All production infrastructure declared in code and applied through the pipeline - no console-created resources in production.",
            "Remote versioned state with locking for every state file, with access limited to the pipeline identity.",
            "Plan output reviewed (by human or policy engine) before every apply, with destroys requiring explicit confirmation.",
            "Reusable modules for common patterns, versioned and consumed - not copy-pasted declarations drifting apart.",
            "Drift detection on a schedule with alerts, so manual changes are found and reconciled rather than accumulating.",
        ],
        "standards": [
            "Declarative IaC popularized by Terraform (HashiCorp) configuration language; alternatives include Pulumi, AWS CloudFormation, and OpenTofu.",
            "Policy as code: Open Policy Agent (Rego) and provider-native policy frameworks gating plans.",
            "State encryption at rest and access logging per the cloud security controls in this database's security record.",
        ],
        "citations": [CIT_WAFRAME, CIT_NIST853],
        "sig_lens": (
            "The Signature read: infrastructure as code is the "
            "covenant's written law - the whole city declared in "
            "scrolls, reviewable by all, rebuildable from the words "
            "alone. The Signature Cloud Method writes its law before "
            "raising its walls: what is written shall stand, what "
            "drifts shall be corrected, and no wall rises unwritten."
        ),
    },
    {
        "key": "service_mesh",
        "name": "Service Mesh",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A service mesh is the dedicated infrastructure layer for "
            "service-to-service communication in a microservices "
            "system: instead of every application coding its own retry "
            "logic, TLS, load balancing, and access policy, those "
            "concerns move into a proxy that sits beside every service "
            "instance. The architecture splits into the data plane - "
            "the sidecar proxies (commonly Envoy) intercepting every "
            "request in and out of each service - and the control plane, "
            "which distributes configuration, certificates, and policy "
            "to all the proxies. With the mesh in place, capabilities "
            "appear without application changes: mutual TLS between all "
            "services (every call authenticated and encrypted), "
            "fine-grained traffic policy (retry budgets, timeouts, "
            "circuit breaking, canary splits by percentage), and "
            "uniform telemetry (every hop emitting traces and metrics). "
            "The trade is complexity and overhead: another control "
            "plane to operate, added latency per hop, and resource "
            "cost for the sidecars. The mesh earns its keep when the "
            "service count passes the point where every team "
            "reimplementing resilience badly becomes the bigger risk."
        ),
        "how_it_works": (
            "A service mesh works by transparent interception. Each "
            "service pod gets a sidecar proxy injected; iptables rules "
            "(or equivalent) redirect the service's outbound and "
            "inbound traffic through it. The control plane pushes "
            "configuration via discovery APIs: which endpoints back "
            "each service, what the retry policy is, which certificate "
            "to present. When service A calls service B, A's sidecar "
            "opens mutual TLS to B's sidecar (both presenting mesh-"
            "issued certificates, rotated automatically), applies "
            "policy - load balance across B's instances, retry idempotent "
            "failures with backoff up to the retry budget, trip the "
            "circuit breaker if B's error rate spikes - and records a "
            "trace span and metrics. Authorization policy is enforced "
            "at the proxies: only the declared caller identities may "
            "reach each service's ports, implementing zero-trust "
            "micro-segmentation without touching application code. "
            "Traffic management enables progressive delivery: mirror a "
            "percentage of live traffic to the new version, split 5/95 "
            "canary, shift on success. The proxies also terminate "
            "perimeter concerns at the mesh gateways, which handle "
            "north-south ingress with the same policy language."
        ),
        "key_points": [
            "Sidecar proxies beside every service form the data plane; the control plane distributes config, certificates, and policy - communication concerns leave the application code.",
            "Mutual TLS everywhere: every service-to-service call authenticated and encrypted with automatically rotated certificates.",
            "Resilience as policy: retry budgets, timeouts, circuit breakers, and canary splits declared once and enforced at every hop.",
            "Authorization at the proxy implements zero-trust micro-segmentation: only declared caller identities reach each service.",
            "The mesh costs complexity, per-hop latency, and sidecar resources - adopt when the service count makes every team reimplementing resilience the bigger risk.",
        ],
        "requirements": [
            "A service count and communication complexity that justifies the control plane - the mesh is not free.",
            "Mutual TLS in permissive-then-strict rollout: observe plaintext callers before enforcing, or the mesh breaks the system it protects.",
            "Retry budgets and timeouts set deliberately: unbounded retries turn one slow service into a system-wide retry storm.",
            "Certificate rotation and control-plane high availability designed in - the mesh is now critical path for all traffic.",
            "Resource requests for sidecars sized per workload, monitored like any other production component.",
        ],
        "standards": [
            "Data-plane proxy: Envoy (CNCF graduated); control planes: Istio, Linkerd, Consul Connect (CNCF projects).",
            "Service mesh interface (SMI) and Gateway API (Kubernetes SIG-Network) standardize traffic policy expression.",
            "Workload identity for mesh mTLS commonly follows SPIFFE/SPIRE standards.",
        ],
        "citations": [CIT_K8S, CIT_NIST207],
        "sig_lens": (
            "The Signature read: the mesh is the covenant's fellowship "
            "of sworn messengers - every servant paired with a "
            "seal-bearer who encrypts, verifies, and witnesses each "
            "errand. The Signature Cloud Method posts a seal-bearer "
            "beside every servant: no message travels unsealed, no "
            "stranger's orders are obeyed, and every journey is "
            "recorded."
        ),
    },
    {
        "key": "future_internet",
        "name": "The Future Internet: IPv6, QUIC, and Beyond",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The internet is mid-migration to its next foundations, and "
            "this record maps where it is going. IPv6 adoption climbs "
            "steadily past one-third of global traffic: the 128-bit "
            "address space ends scarcity, restores end-to-end "
            "addressing without NAT, and simplifies the network - the "
            "remaining work is the long tail of enterprise and ISP "
            "migration, carried by dual-stack operation. QUIC is the "
            "transport revolution already underneath much of the web: "
            "built on UDP, it folds the TLS handshake into connection "
            "setup (faster starts), multiplexes streams without "
            "head-of-line blocking (one lost packet stalls one stream, "
            "not all), and migrates connections across networks (your "
            "video call survives the Wi-Fi to cellular handoff) - and "
            "HTTP/3 runs on it. Beyond: post-quantum cryptography is "
            "being standardized and deployed in hybrid modes before "
            "quantum computers break today's public-key algorithms; "
            "low-earth-orbit satellite constellations bring broadband "
            "to the unserved billions; and the edge-plus-AI pattern "
            "from earlier records keeps pushing intelligence outward. "
            "The through-line of forty years: the protocols get simpler "
            "at the core and smarter at the edges, and every generation "
            "moves the complexity to where the scale is."
        ),
        "how_it_works": (
            "The migration works through coexistence, not flag days. "
            "IPv6 deploys dual-stack: hosts and routers run IPv4 and "
            "IPv6 simultaneously, preferring IPv6 when available, with "
            "translation (NAT64) and tunneling bridging the gaps - the "
            "address plan from the IP record extends naturally to /64 "
            "per subnet. QUIC deploys inside applications: because it "
            "runs over UDP in user space, browsers and servers adopted "
            "it without waiting for operating system upgrades - the "
            "handshake combines transport and TLS 1.3 key exchange, "
            "cutting round trips, while per-stream flow control ends "
            "TCP's head-of-line blocking and connection IDs (rather "
            "than the four-tuple) let sessions survive address changes. "
            "Post-quantum migration works hybrid-first: key exchanges "
            "combining classical elliptic curves with new lattice-based "
            "algorithms (ML-KEM standardized by NIST), so security "
            "holds if either holds, deployed in TLS before the threat "
            "matures. Satellite broadband works as a space segment: "
            "thousands of low-orbit satellites with laser interlinks "
            "form a mesh network in the sky, ground terminals tracking "
            "them electronically, latency far below geostationary "
            "systems because the signal travels hundreds rather than "
            "tens of thousands of miles."
        ),
        "key_points": [
            "IPv6 ends address scarcity and restores end-to-end addressing: deploy dual-stack now, prefer v6, and plan the long-tail migration deliberately.",
            "QUIC (and HTTP/3) folds TLS into connection setup, ends head-of-line blocking, and survives network changes - the transport upgrade already carrying much of the web.",
            "Post-quantum cryptography migrates hybrid-first (classical plus ML-KEM): deploy before quantum computers arrive, not after.",
            "LEO satellite constellations bring low-latency broadband to unserved regions - the internet's geography is being rewritten from orbit.",
            "The forty-year pattern: simpler cores, smarter edges, complexity moving to where the scale is - design for the direction, not just the present.",
        ],
        "requirements": [
            "Dual-stack capability in all new network builds and procurement - single-stack IPv4 is technical debt with a known expiry.",
            "HTTP/3 and QUIC enabled on public endpoints where the stack supports it, with fallback measured, not assumed broken.",
            "A cryptographic inventory and agility plan: know where public-key cryptography lives so post-quantum migration is a project, not a panic.",
            "Edge and offline architectures (from the edge record) treated as the default assumption for new global systems.",
            "Continuous learning: the protocols will keep moving - budget engineering time to track the migrations that affect your threat model and performance.",
        ],
        "standards": [
            "IPv6: RFC 8200; transition mechanisms: RFC 4213 (dual-stack), RFC 6146 (NAT64).",
            "QUIC: RFC 9000; HTTP/3: RFC 9114; TLS 1.3 integration: RFC 8446.",
            "Post-quantum: NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA); hybrid key exchange in TLS per IETF drafts and early RFCs.",
        ],
        "citations": [CIT_RFC8200, CIT_RFC9000, CIT_RFC8446],
        "sig_lens": (
            "The Signature read: the future internet is the covenant's "
            "next country - wider streets, swifter couriers, seals "
            "forged against tomorrow's lockpicks. The Signature Cloud "
            "Method builds for the direction: addresses without end, "
            "couriers that survive the journey's interruptions, and "
            "oaths sealed against even the code-breakers of the coming "
            "age."
        ),
    },
]
