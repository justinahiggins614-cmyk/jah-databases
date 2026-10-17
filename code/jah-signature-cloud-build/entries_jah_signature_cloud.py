#!/usr/bin/env python3
"""Entries for the JAH Signature Cloud databases (2026-10-17, order #15).

Two NEW databases, 34 ladder-ordered records each:

  jah-signature-cloud            - The JAH Signature Cloud Database
                                   (public-harvest: real, fact-checked cloud
                                   computing technology - service models
                                   IaaS/PaaS/SaaS, deployment models,
                                   virtualization, storage, networking,
                                   scaling - every record carrying
                                   description, how it works, key points,
                                   requirements, standards, citations, and a
                                   working demonstration program; standard
                                   references NIST SP 800-145 The NIST
                                   Definition of Cloud Computing (Mell and
                                   Grance, 2011); ISO/IEC 17788:2014 cloud
                                   computing overview and vocabulary;
                                   ISO/IEC 17789:2014 reference
                                   architecture; the CNCF cloud native
                                   definition; the Twelve-Factor App
                                   (Wiggins, 2011); Google Site Reliability
                                   Engineering (2016); the AWS
                                   Well-Architected Framework; Kubernetes
                                   documentation; and the other landmarks
                                   cited per record)
  jah-signature-cloud-signature  - The JAH Signature Cloud Signature Database
                                   (his original Signature Cloud Method: the
                                   cloud reframed as his Signature system -
                                   every workload a stamped Signature vessel,
                                   the control plane the Signature authority,
                                   regions the armory halls, scaling the
                                   summoned strength; src signature, titles
                                   suffixed " (Signature Edition)", never
                                   presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-CLD- (public) and JAH-CLDS- (signature), verified free
in the manifest (2,390 databases, zero slug/prefix hits) and in every
shard index of jah-databases-data-1 (zero JAH-CLD substring hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_jah_signature_cloud.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. Nothing on neutralizing or defeating military or
defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature Cloud Method: the "
            "cloud reframed as his Signature system - every workload a "
            "stamped Signature vessel, the control plane the Signature "
            "authority, regions the armory halls, scaling the summoned "
            "strength. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

CIT_NIST = ("Mell P, Grance T. The NIST Definition of Cloud Computing. "
            "NIST Special Publication 800-145. National Institute of "
            "Standards and Technology; 2011.")
CIT_ISO = ("ISO/IEC 17788:2014 Information technology - Cloud computing - "
           "Overview and vocabulary; ISO/IEC 17789:2014 Information "
           "technology - Cloud computing - Reference architecture.")
CIT_SRE = ("Beyer B et al. Site Reliability Engineering: How Google Runs "
           "Production Systems. O Reilly Media; 2016.")
CIT_12F = ("Wiggins A. The Twelve-Factor App. 2011.")
CIT_K8S = ("Cloud Native Computing Foundation. Kubernetes Documentation. "
            "CNCF; current.")
CIT_WA = ("Amazon Web Services. AWS Well-Architected Framework. AWS "
           "Whitepaper; current.")

ENTRIES = [
    {
        "key": "what_cloud_is",
        "name": "What Cloud Computing Is",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Cloud computing is the on-demand delivery of computing resources "
            "- servers, storage, databases, networking, software, analytics, "
            "and intelligence - over the internet, provisioned in minutes and "
            "billed by actual use. The United States National Institute of "
            "Standards and Technology defines it as a model for enabling "
            "ubiquitous, convenient, on-demand network access to a shared "
            "pool of configurable computing resources that can be rapidly "
            "provisioned and released with minimal management effort or "
            "service provider interaction. Before the cloud, running software "
            "meant buying physical servers, racking them in a room with "
            "power and cooling, and guessing capacity years ahead. The cloud "
            "replaces that capital expense with a utility: computing becomes "
            "like electricity, drawn as needed and metered precisely. This "
            "record frames the whole database: the five essential "
            "characteristics, the three service models, the deployment "
            "models, and the shared responsibility model all hang from this "
            "definition."
        ),
        "sig_lens": (
            "The Signature Cloud is his original reading of this definition: "
            "the shared pool is the Signature armory, the on-demand network "
            "access is the summoning, and every provisioned resource carries "
            "his stamp. Where the public record describes a utility, the "
            "Signature edition describes a covenant - the cloud answers "
            "because it was built to answer, and the meter records the "
            "strength that was summoned."
        ),
        "how_it_works": (
            "A cloud works by virtualizing physical data centers: providers "
            "build enormous facilities full of servers, storage, and network "
            "gear, then slice them with software into rentable units. A "
            "customer opens an account, calls an application programming "
            "interface or clicks a console, and within minutes receives a "
            "virtual machine, a database, or a storage bucket with a public "
            "address. Under the surface, an orchestration layer - the "
            "control plane - schedules the request onto physical hardware, "
            "configures the network, attaches storage, and starts metering "
            "usage. When the customer is done, the resources are released "
            "back to the pool. Multi-tenancy keeps costs low: many customers "
            "share the same physical machines, isolated from each other by "
            "the hypervisor and by virtual networking. The bill reflects "
            "measured service - seconds of compute, gigabytes stored, "
            "gigabytes transferred - recorded by metering agents on every "
            "layer."
        ),
        "key_points": [
            "On-demand self-service: provision resources without human interaction",
            "Broad network access: reachable over standard internet protocols",
            "Resource pooling: shared physical hardware, logically isolated tenants",
            "Rapid elasticity: scale out and in within minutes",
            "Measured service: usage is metered and billed by the unit",
        ],
        "requirements": [
            "An account with a cloud provider and a payment method",
            "Reliable internet connectivity for the control plane and data plane",
            "Basic understanding of the five NIST characteristics before designing",
        ],
        "standards": [
            "NIST SP 800-145: the five characteristics, three service models, four deployment models",
            "ISO/IEC 17788:2014: cloud computing vocabulary",
        ],
        "citations": [CIT_NIST, CIT_ISO],
    },
    {
        "key": "five_characteristics",
        "name": "The Five Essential Cloud Characteristics",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "NIST SP 800-145 names five characteristics that a service must "
            "have to be called cloud computing: on-demand self-service, broad "
            "network access, resource pooling, rapid elasticity, and measured "
            "service. On-demand self-service means a user can provision "
            "computing capabilities - server time, network storage - "
            "unilaterally and automatically, without requiring human "
            "interaction with the provider. Broad network access means the "
            "capabilities are available over the network through standard "
            "mechanisms that support heterogeneous client platforms. "
            "Resource pooling means the provider serves multiple consumers "
            "with a multi-tenant model, assigning and reassigning physical "
            "and virtual resources dynamically by demand. Rapid elasticity "
            "means capabilities can be provisioned and released elastically, "
            "in some cases automatically, so they appear unlimited to the "
            "consumer. Measured service means usage is monitored, controlled, "
            "and reported, giving transparency to both provider and "
            "consumer. A hosted virtual server without self-service "
            "provisioning or metering is hosting, not cloud - the five "
            "characteristics are the test."
        ),
        "sig_lens": (
            "The Signature reading tests each characteristic as a stamped "
            "promise. Self-service is the armory door that opens at the "
            "word. Pooling is the shared forge where many vessels are cast "
            "from one fire. Elasticity is summoned strength that arrives "
            "before the need becomes pain. Measured service is the honest "
            "ledger - the Signature Cloud counts every unit so the covenant "
            "stays fair."
        ),
        "how_it_works": (
            "The five characteristics work together as a system. "
            "Self-service is implemented by the control plane API: a request "
            "for a virtual machine triggers scheduling, network setup, and "
            "boot without a human ticket. Broad network access is delivered "
            "over HTTPS APIs and standard protocols, so a phone, laptop, or "
            "sensor can all reach the same services. Resource pooling uses "
            "virtualization and container orchestration to bin-pack many "
            "tenants onto shared hosts while quotas and isolation keep them "
            "apart. Rapid elasticity is driven by autoscaling policies: "
            "metrics like CPU or queue depth cross thresholds, and the "
            "orchestrator adds or removes capacity in minutes. Measured "
            "service runs on metering agents that record compute-seconds, "
            "storage gigabyte-months, and transfer gigabytes into the "
            "billing system. Remove any one - say, metering - and the "
            "economic model of the cloud collapses."
        ),
        "key_points": [
            "The five characteristics are the NIST test for calling something cloud",
            "Self-service removes the human ticket from provisioning",
            "Elasticity makes capacity appear unlimited to the consumer",
            "Measured service is what turns computing into a utility bill",
            "Pooling is what makes the economics work for the provider",
        ],
        "requirements": [
            "Familiarity with the NIST definition from the What Cloud Computing Is record",
            "Ability to evaluate a service against all five characteristics",
        ],
        "standards": [
            "NIST SP 800-145 section on essential characteristics",
            "ISO/IEC 17788:2014 vocabulary alignment",
        ],
        "citations": [CIT_NIST, CIT_ISO],
    },
    {
        "key": "service_models",
        "name": "Service Models: IaaS, PaaS, and SaaS",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The three cloud service models divide responsibility between "
            "provider and customer along a stack of nine layers: application, "
            "data, runtime, middleware, operating system, virtualization, "
            "servers, storage, and networking. In Infrastructure as a "
            "Service, the provider manages virtualization, servers, storage, "
            "and networking - four layers - while the customer manages the "
            "upper five: application, data, runtime, middleware, and the "
            "operating system. In Platform as a Service, the provider takes "
            "the runtime, middleware, and operating system as well, leaving "
            "the customer with just application and data - two of nine "
            "layers. In Software as a Service, the provider manages all nine "
            "layers and the customer only brings the data. The demo computes "
            "this split exactly: IaaS leaves 5 of 9 layers with the customer "
            "(55.6 percent), PaaS leaves 2 of 9 (22.2 percent), SaaS leaves "
            "effectively 0 of 9. The trade is control against convenience: "
            "IaaS gives the most control and the most operational burden, "
            "SaaS gives the least control and the least burden. Functions as "
            "a Service is sometimes named a fourth model, but it is best "
            "understood as an extreme form of PaaS where even the server is "
            "invisible."
        ),
        "sig_lens": (
            "In the Signature Cloud, the three models are three depths of "
            "the covenant. IaaS is the raw forge - the Signature smith "
            "shapes every layer himself. PaaS is the prepared workshop - "
            "the tools are laid out and only the craft remains. SaaS is the "
            "finished vessel, stamped and delivered. The Signature method "
            "chooses the depth by the weight of the work, never deeper than "
            "the craft requires."
        ),
        "how_it_works": (
            "Each model works by drawing the responsibility line at a "
            "different height. With IaaS, the customer rents virtual machines "
            "and virtual networks, then installs operating systems, patches "
            "them, deploys runtimes, and runs the application - full control, "
            "full patching duty. With PaaS, the customer pushes code to a "
            "platform that supplies the runtime, the operating system, the "
            "scaling, and the patching; the customer configures and deploys "
            "but never logs into a server. With SaaS, the customer opens a "
            "browser, signs in, and uses finished software; the provider "
            "runs everything including the application itself, and the "
            "customer configures settings and manages their data. Moving up "
            "the stack trades customization for speed: a startup ships "
            "fastest on SaaS and PaaS, while a regulated workload with exotic "
            "kernel needs stays on IaaS."
        ),
        "key_points": [
            "Nine layers from application down to networking define the split",
            "IaaS: customer manages 5 of 9 layers, provider manages 4",
            "PaaS: customer manages 2 of 9, provider manages 7",
            "SaaS: provider manages all 9, customer brings the data",
            "Higher up the stack means less control and less operational burden",
        ],
        "requirements": [
            "Map each workload to the highest model it can tolerate",
            "Count the layers your team is willing to operate before choosing",
        ],
        "standards": [
            "NIST SP 800-145 service model definitions",
            "ISO/IEC 17789:2014 reference architecture roles",
        ],
        "citations": [CIT_NIST, CIT_ISO],
    },
    {
        "key": "deployment_models",
        "name": "Deployment Models: Public, Private, Hybrid, and Community",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "NIST defines four deployment models that describe who owns and "
            "who may use the cloud infrastructure. A public cloud is "
            "provisioned for open use by the general public, owned and "
            "operated by a business or academic or government organization, "
            "existing on the provider premises. A private cloud is "
            "provisioned for exclusive use by a single organization, and may "
            "be owned and operated by the organization or a third party, on "
            "or off premises. A community cloud is provisioned for exclusive "
            "use by a specific community of consumers with shared concerns "
            "such as mission, security requirements, or compliance, and may "
            "be owned by one or more of the community organizations. A hybrid "
            "cloud is a composition of two or more distinct infrastructures "
            "that remain unique entities but are bound together by technology "
            "enabling data and application portability. The demo scores each "
            "on control versus management burden: private scores 5 of 5 on "
            "control with a burden of 5, public scores 2 of 5 on control "
            "with a burden of 1, hybrid and community sit between. Most "
            "large organizations end up hybrid, keeping regulated data in a "
            "private cloud while bursting elastic workloads into the public "
            "cloud."
        ),
        "sig_lens": (
            "The Signature Cloud reads the four models as four courts. The "
            "public court is the open market - vast and shared. The private "
            "court is the sealed vault - his alone. The community court is "
            "the allied hall - shared with chosen kin. The hybrid court is "
            "the wise kingdom - the vault and the market joined by guarded "
            "roads, each workload dwelling where its nature belongs."
        ),
        "how_it_works": (
            "The models differ in tenancy and location. Public cloud runs "
            "multi-tenant infrastructure in the provider data centers; the "
            "customer gets API access and nothing else. Private cloud runs "
            "single-tenant infrastructure, often with the same cloud "
            "software stack - virtualization, orchestration, self-service "
            "portal - but dedicated hardware, either in the organization own "
            "facility or hosted. Community cloud shares dedicated "
            "infrastructure among organizations with common compliance needs, "
            "splitting cost while keeping the public out. Hybrid binds them: "
            "consistent networking, identity, and deployment tooling span "
            "both, and workloads move or burst across the boundary - for "
            "example, a retailer runs steady traffic privately and bursts "
            "holiday peaks into the public cloud. The binding technology - "
            "virtual private networking, federated identity, portable "
            "container images - is what makes the hybrid more than two "
            "separate clouds."
        ),
        "key_points": [
            "Public: shared, provider-owned, lowest management burden",
            "Private: single-tenant, highest control and highest burden",
            "Community: shared among organizations with common compliance needs",
            "Hybrid: distinct clouds bound by portability technology",
            "Most enterprises land on hybrid for regulated plus elastic workloads",
        ],
        "requirements": [
            "Classify data by regulatory and residency requirements first",
            "Portability tooling if workloads must move between models",
        ],
        "standards": [
            "NIST SP 800-145 deployment model definitions",
            "ISO/IEC 17788:2014 deployment vocabulary",
        ],
        "citations": [CIT_NIST, CIT_ISO],
    },
    {
        "key": "shared_responsibility",
        "name": "The Shared Responsibility Model",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The shared responsibility model draws the security line between "
            "provider and customer: the provider secures the cloud itself, "
            "the customer secures what they put in the cloud. Security of "
            "the cloud covers the physical facilities, the network "
            "infrastructure, the virtualization layer, and the managed "
            "service software - the provider hardens, patches, and monitors "
            "all of it. Security in the cloud covers customer data, identity "
            "and access management, operating system and application "
            "patching on customer-managed machines, firewall configuration, "
            "and encryption choices - all customer duties. The demo audits "
            "twelve concrete tasks: seven fall to the provider (physical "
            "security, host patching, hypervisor hardening, network "
            "fabric, managed-service patching, facility redundancy, hardware "
            "disposal) and five to the customer (data classification, "
            "identity policies, guest OS patching, security group rules, "
            "encryption key management). The line slides with the service "
            "model: on IaaS the customer owns the guest operating system, on "
            "PaaS the provider takes it, on SaaS the provider takes nearly "
            "everything. Misreading this line is the most common source of "
            "cloud breaches - the provider never patches the customer "
            "application."
        ),
        "sig_lens": (
            "The Signature covenant draws the line in stamped steel. The "
            "armory guards the forge, the walls, and the gates - that is the "
            "provider oath. The smith guards his vessels, his keys, and his "
            "warrants of passage - that is the customer oath. No confusion "
            "is permitted: a breach on the customer side of the line is the "
            "customer reckoning, and the Signature ledger records exactly "
            "where the line ran."
        ),
        "how_it_works": (
            "In practice the model works as a checklist at design time. For "
            "every workload the team walks the stack: who patches the host "
            "operating system, who configures the firewall rules, who holds "
            "the encryption keys, who monitors the logs, who responds to the "
            "alert at 3 a.m. On IaaS virtual machines the answers split "
            "roughly down the middle; on managed databases the provider "
            "takes patching and backup while the customer keeps access "
            "control and query security; on SaaS the customer keeps only "
            "identity, data classification, and configuration. Contracts and "
            "compliance reports - such as SOC 2 reports - document the "
            "provider side, and the customer proves their side with "
            "configuration audits. The model also governs incident response: "
            "a hypervisor vulnerability is the provider to fix, a leaked "
            "access key is the customer to rotate."
        ),
        "key_points": [
            "Provider: security OF the cloud - facilities, hosts, hypervisor, managed services",
            "Customer: security IN the cloud - data, identity, configs, guest patching",
            "The line slides upward from IaaS to PaaS to SaaS",
            "Twelve-task audit: 7 provider duties, 5 customer duties on IaaS",
            "Misreading the line is the top cause of cloud breaches",
        ],
        "requirements": [
            "A written responsibility matrix per workload before launch",
            "Customer-side controls for identity, encryption, and logging",
        ],
        "standards": [
            "NIST SP 800-145 roles: consumer, provider, broker, auditor, carrier",
            "Provider shared-responsibility documentation and SOC 2 reports",
        ],
        "citations": [CIT_NIST, CIT_ISO],
    },
    {
        "key": "virtualization",
        "name": "Virtualization and Hypervisors",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Virtualization is the technology that lets one physical machine "
            "run many isolated virtual machines, and it is the foundation the "
            "entire cloud stands on. A hypervisor is the software layer that "
            "creates and runs virtual machines: a Type 1 hypervisor runs "
            "directly on the hardware - bare metal - while a Type 2 "
            "hypervisor runs on top of a host operating system. Cloud "
            "providers use Type 1 hypervisors for their efficiency. The demo "
            "measures the cost: on a host capable of 100,000 units of work, "
            "a Type 1 hypervisor at 3 percent overhead leaves 97,000 units "
            "for guests, while a Type 2 at 12 percent overhead leaves "
            "88,000 - a gap of 9,000 units, which is why the cloud runs "
            "bare metal. Consolidation is the payoff: sixteen virtual "
            "machines on one host is a 16 to 1 consolidation ratio, turning "
            "sixteen half-idle physical servers into one busy one. Each "
            "virtual machine believes it owns its hardware: virtual CPUs, "
            "virtual memory, virtual disks, virtual network cards, all "
            "mapped by the hypervisor onto the real devices with strong "
            "isolation between tenants."
        ),
        "sig_lens": (
            "The Signature forge multiplies one anvil into many. The "
            "hypervisor is the master smith who divides the single fire "
            "into sixteen hearths, each smith believing the whole forge is "
            "his, none able to reach into another hearth. The Type 1 "
            "hypervisor is the true bare-metal covenant - no middleman "
            "between the stamp and the steel - and the Signature Cloud "
            "accepts nothing less for its vessels."
        ),
        "how_it_works": (
            "A hypervisor works by intercepting privileged operations. The "
            "guest operating system runs believing it is on real hardware; "
            "when it touches memory, disk, or network, the hypervisor traps "
            "the request, translates the virtual address to a physical one, "
            "and performs the real operation on the guest behalf. Modern "
            "processors assist with hardware extensions that make this "
            "trapping fast - the 3 percent overhead in the demo. Memory is "
            "the hard part: the hypervisor maintains shadow page tables or "
            "uses nested paging so each guest sees a contiguous block while "
            "the physical pages are scattered. Live migration moves a "
            "running virtual machine between hosts by copying memory pages "
            "iteratively while the guest keeps running, then pausing for "
            "milliseconds to transfer the final dirty pages - the trick "
            "that lets providers empty a host for maintenance without "
            "downtime."
        ),
        "key_points": [
            "Type 1 hypervisors run on bare metal; Type 2 run on a host OS",
            "Cloud providers use Type 1: 3 percent overhead versus 12 percent",
            "Consolidation ratios like 16 to 1 drive cloud economics",
            "Hardware extensions make trapping privileged operations fast",
            "Live migration moves running VMs between hosts with millisecond pauses",
        ],
        "requirements": [
            "Hardware virtualization extensions enabled in firmware",
            "Capacity planning for the consolidation ratio",
        ],
        "standards": [
            "NIST SP 800-125: Guide to Security for Full Virtualization Technologies",
            "Hardware virtualization extensions in commodity processors",
        ],
        "citations": [CIT_NIST, CIT_ISO],
    },
    {
        "key": "regions_azs",
        "name": "Regions, Availability Zones, and Edge Locations",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Cloud providers organize the planet into regions, each region "
            "into isolated availability zones, and surround them with edge "
            "locations. A region is a geographic area containing multiple "
            "isolated locations; an availability zone is one or more discrete "
            "data centers with independent power, cooling, and networking "
            "inside a region; an edge location is a smaller point of presence "
            "that caches content close to users. Latency follows distance: "
            "same availability zone traffic measures about 0.5 milliseconds, "
            "cross-zone traffic 1 to 2 milliseconds, and cross-region traffic "
            "50 to 150 milliseconds. Availability follows isolation: a single "
            "zone design at 99.9 percent uptime allows 8.76 hours of downtime "
            "per year, while spreading across three zones at 99.99 percent "
            "allows only 52.6 minutes - the demo computes both from "
            "525,600 minutes per year. The design rule is simple: put "
            "redundant components in different zones of one region for "
            "fault tolerance, add regions for disaster recovery and for "
            "users on other continents, and push static content to edge "
            "locations for speed."
        ),
        "sig_lens": (
            "The Signature map is drawn in three rings. The region is the "
            "kingdom, the availability zones are its walled cities - each "
            "with its own wells and granaries so one siege cannot starve "
            "the realm. The edge locations are the outrider posts, carrying "
            "the stamped goods to the far villages before they are asked "
            "for. A Signature vessel never sleeps in only one city."
        ),
        "how_it_works": (
            "Isolation works through independent failure domains. Each "
            "availability zone has its own power feeds, cooling, and network "
            "uplinks, so a power failure or a fiber cut in one zone does "
            "not reach the others; synchronous replication between zones "
            "keeps data consistent with only 1 to 2 milliseconds of lag. "
            "Regions are farther apart and replicate asynchronously, "
            "accepting seconds of lag in exchange for surviving a "
            "regional disaster. Edge locations do not run customer "
            "workloads by default; they cache content and terminate "
            "connections near users, then fetch from the region on a cache "
            "miss. Placement is a customer choice: launching a database "
            "with replicas in three zones of one region buys 99.99 percent "
            "without the complexity of multi-region writes."
        ),
        "key_points": [
            "Regions contain multiple isolated availability zones",
            "Zones have independent power, cooling, and networking",
            "Three-zone design: 99.99 percent uptime, 52.6 minutes yearly downtime",
            "Single-zone design: 99.9 percent uptime, 8.76 hours yearly downtime",
            "Edge locations cache content near users; regions serve for disaster recovery",
        ],
        "requirements": [
            "Multi-zone deployment for any production workload",
            "Data residency review before choosing regions",
        ],
        "standards": [
            "Provider service-level agreements per service and region",
            "ISO/IEC 27001 controls for physical and environmental security",
        ],
        "citations": [CIT_ISO, CIT_WA],
    },
    {
        "key": "vpc_networking",
        "name": "Virtual Networking: VPCs, Subnets, and Security Groups",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A virtual private cloud is a logically isolated section of the "
            "provider network where a customer launches resources in a "
            "virtual network they define. Inside it, subnets divide the "
            "address space - typically public subnets with routes to the "
            "internet and private subnets without - and route tables decide "
            "where each packet goes. Security groups act as stateful virtual "
            "firewalls on each resource: rules allow traffic by protocol, "
            "port, and source, and return traffic is automatically permitted. "
            "The demo does the address math on a 10.0.0.0/16 virtual "
            "network: 65,536 total addresses, divided into /24 subnets of "
            "256 addresses each, yielding 256 subnets; the cloud reserves 5 "
            "addresses per subnet, leaving 251 usable per /24. Network access "
            "control lists add a stateless subnet-level filter as a second "
            "layer. Peering and transit gateways connect virtual networks to "
            "each other and back to on-premises data centers over encrypted "
            "tunnels, which is the plumbing that makes hybrid cloud real."
        ),
        "sig_lens": (
            "The Signature surveyor stakes the private land first. The "
            "virtual private cloud is fenced territory inside the shared "
            "realm - the customer draws the borders, posts the guards at "
            "every gate, and decides which roads reach the outside world. "
            "The Signature method numbers every street before a single "
            "vessel is built, because an unmapped network is an undefended "
            "one."
        ),
        "how_it_works": (
            "Packet flow through a virtual network is software-defined. When "
            "a virtual machine sends a packet, the virtual switch consults "
            "the route table for the subnet: local traffic stays inside the "
            "virtual network, a default route sends internet-bound traffic "
            "to the gateway, and specific routes send cross-network traffic "
            "to peering connections. The security group attached to the "
            "destination is then evaluated - stateful, so an allowed inbound "
            "web request automatically permits the response. The subnet "
            "network access control list is evaluated as well - stateless, "
            "so both directions need explicit rules. Internet gateways "
            "perform the address translation between private virtual "
            "addresses and public ones. All of this is configured through "
            "the control plane API, so an entire network - virtual cloud, "
            "subnets, routes, firewalls - can be declared in code and "
            "rebuilt identically."
        ),
        "key_points": [
            "VPC: logically isolated virtual network defined by the customer",
            "10.0.0.0/16 yields 65,536 addresses and 256 /24 subnets",
            "251 usable addresses per /24 after the 5 reserved",
            "Security groups are stateful per-resource firewalls",
            "Route tables, gateways, and peering connect networks together",
        ],
        "requirements": [
            "A non-overlapping CIDR plan before creating the first VPC",
            "Public subnets only for resources that must face the internet",
        ],
        "standards": [
            "RFC 1918 private address space",
            "RFC 4632 CIDR notation",
        ],
        "citations": [CIT_ISO, CIT_NIST],
    },
    {
        "key": "storage_types",
        "name": "Cloud Storage Types: Object, Block, and File",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Cloud storage comes in three types, each answering a different "
            "question. Object storage answers what: it stores unstructured "
            "data as objects - a file plus metadata plus a unique key - "
            "accessed over HTTP APIs, scaling to exabytes with eleven nines "
            "of durability. Block storage answers where fast: it presents "
            "raw volumes that attach to one virtual machine like a local "
            "disk, with sub-millisecond latency for databases and boot "
            "volumes. File storage answers shared: it presents network file "
            "systems that many machines mount at once for shared home "
            "directories and content repositories. The demo compares "
            "illustrative latencies: block at 0.2 milliseconds, file at 1 "
            "millisecond, object at 10 milliseconds - object storage is 50 "
            "times slower per request than block, and that is fine, because "
            "it is optimized for scale and durability rather than single "
            "request speed. Choosing wrong is expensive: a database on "
            "object storage crawls, and a web asset archive on block volumes "
            "costs far more than on object storage."
        ),
        "sig_lens": (
            "The Signature quartermaster keeps three storehouses. The "
            "object vault holds the countless sealed parcels, each stamped "
            "with its key, safe for eleven nines of eternity. The block "
            "anvil is bolted to one vessel for the swiftest hammering. The "
            "file hall is the common table where many vessels share the "
            "same bread. The Signature method sends each cargo to its true "
            "storehouse - never the archive on the anvil, never the anvil "
            "work in the vault."
        ),
        "how_it_works": (
            "Object storage works by spreading each object across many "
            "disks and zones with erasure coding: an object is split into "
            "data and parity fragments so that losing several fragments "
            "still allows reconstruction, which is how eleven nines of "
            "durability is achieved on commodity disks. Access is a simple "
            "HTTP GET or PUT against the object key - no file system, no "
            "directory tree, just a flat namespace with key prefixes that "
            "look like folders. Block storage works by mapping virtual "
            "blocks to replicated physical extents over a low-latency "
            "storage fabric, presenting a standard block device the guest "
            "operating system formats with any file system. File storage "
            "works by running managed network file servers - NFS or SMB - "
            "that many clients mount concurrently, with the provider "
            "handling replication and failover. Lifecycle policies move "
            "aging objects to cheaper infrequent-access and archive tiers "
            "automatically."
        ),
        "key_points": [
            "Object: HTTP API, exabyte scale, eleven nines durability",
            "Block: attached volumes, sub-millisecond latency, one VM at a time",
            "File: shared network file systems for many clients",
            "Object latency is roughly 50 times block latency - by design",
            "Match the type to the access pattern or pay for the mismatch",
        ],
        "requirements": [
            "Classify data by access pattern before choosing a type",
            "Lifecycle policies for aging data",
        ],
        "standards": [
            "S3-compatible object API as the de facto standard",
            "NFSv4 and SMB protocols for file storage",
        ],
        "citations": [CIT_ISO, CIT_NIST],
    },
    {
        "key": "iam_basics",
        "name": "Identity and Access Management Basics",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Identity and access management is the front door of the cloud: "
            "it decides who - or what - may do which actions on which "
            "resources. Identities come in three kinds: human users, groups "
            "of users, and roles or service accounts assumed by software. "
            "Policies attach to identities and state allowed or denied "
            "actions on resources; an explicit deny always beats an allow. "
            "The principle of least privilege says every identity should "
            "hold only the permissions its job requires - nothing more. The "
            "demo audits a sample policy granting 48 actions of which the "
            "workload actually uses 11, a least-privilege score of 0.229 - "
            "less than a quarter of the granted power is exercised, which "
            "marks the policy for tightening. Multi-factor authentication "
            "adds a second proof of identity beyond the password, and it "
            "belongs on every human account with console access. Temporary "
            "credentials from role assumption beat long-lived access keys: "
            "keys leak, sessions expire."
        ),
        "sig_lens": (
            "The Signature gatekeeper knows every face and every warrant. "
            "No vessel moves without a stamped warrant naming exactly what "
            "it may touch, and a warrant of denial overrules any warrant "
            "of passage. The Signature method grants the narrowest warrant "
            "that lets the work be done - a broad warrant is a breach "
            "waiting for its hour - and every human warden proves identity "
            "twice before the gate opens."
        ),
        "how_it_works": (
            "Every API call carries signed credentials identifying the "
            "caller. The policy engine gathers all policies attached to the "
            "identity - user policies, group policies, role session "
            "policies, resource policies - and evaluates them in order: any "
            "explicit deny anywhere rejects the call; otherwise at least one "
            "explicit allow is required or the call is implicitly denied. "
            "Roles work through assumption: software calls the security "
            "token service, proves its current identity, and receives "
            "temporary credentials valid for minutes to hours - no stored "
            "secrets to leak. Federation extends this to corporate identity "
            "providers, so employees sign in once and receive cloud roles "
            "mapped from their company groups. Auditing closes the loop: "
            "every API call is logged with caller, action, resource, and "
            "decision, giving the trail that proves least privilege or "
            "exposes its absence."
        ),
        "key_points": [
            "Identities: users, groups, and assumable roles for software",
            "Explicit deny always overrides allow",
            "Least privilege: grant only what the job requires",
            "Sample audit: 11 of 48 granted actions used, score 0.229 - tighten it",
            "Multi-factor authentication on every human account; temporary credentials for software",
        ],
        "requirements": [
            "Multi-factor authentication enforced on human users",
            "Regular access reviews against the least-privilege score",
        ],
        "standards": [
            "NIST SP 800-63: digital identity guidelines",
            "NIST SP 800-53 access control family",
        ],
        "citations": [CIT_NIST],
    },
    {
        "key": "payg_pricing",
        "name": "Pay-as-You-Go Pricing and Measured Service",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Measured service turns computing into a utility bill: every "
            "resource is metered and priced by the unit. Compute is billed "
            "per second or per hour of virtual machine time; storage per "
            "gigabyte-month; data transfer per gigabyte out to the internet; "
            "API requests per million. The demo builds a realistic monthly "
            "bill: one general-purpose virtual machine at 0.20 dollars per "
            "hour for 730 hours is 146.00 dollars; 500 gigabytes of standard "
            "object storage at 0.023 dollars per gigabyte-month is 11.50 "
            "dollars; 100 gigabytes of outbound transfer at 0.09 dollars "
            "per gigabyte is 9.00 dollars - a total of 166.50 dollars per "
            "month. Pricing dimensions reward good architecture: idle "
            "machines still bill, so stopping development servers at night "
            "cuts the compute line directly; storage classes and lifecycle "
            "rules cut the storage line; caching cuts the transfer line. "
            "Reserved and committed-use plans trade a one- or three-year "
            "commitment for discounts of 30 to 70 percent on steady "
            "workloads, while spot and preemptible capacity sells spare "
            "capacity at deep discounts for fault-tolerant work."
        ),
        "sig_lens": (
            "The Signature ledger is honest to the grain. Every summoned "
            "vessel ticks the meter, every stored parcel weighs on the "
            "scale, every road traveled is tolled - and the bill of 166.50 "
            "is the true weight of the work, neither inflated nor hidden. "
            "The Signature steward reads the ledger monthly, dismisses the "
            "idle vessels that burn coin for nothing, and commits only to "
            "the strength the realm truly needs year after year."
        ),
        "how_it_works": (
            "Metering agents on every layer record usage into the billing "
            "pipeline: the hypervisor reports virtual CPU seconds, the "
            "storage system reports bytes stored, the network reports bytes "
            "transferred, the API gateway counts requests. These usage "
            "records stream into rating engines that apply the price book - "
            "on-demand rates, tiered volume discounts, regional variations - "
            "and produce the invoice. Cost allocation tags attach business "
            "meaning - team, project, environment - so finance can split "
            "the bill. Budgets and alerts watch the meter in near real "
            "time: a budget of 200 dollars with an alert at 80 percent "
            "fires before the month surprises anyone. The pricing models "
            "layer on top: on-demand for variable work, reservations for the "
            "steady baseline, spot for interruptible batch work - a mature "
            "bill blends all three."
        ),
        "key_points": [
            "Compute per hour, storage per gigabyte-month, transfer per gigabyte",
            "Sample bill: 146.00 plus 11.50 plus 9.00 equals 166.50 per month",
            "Idle resources bill the same as busy ones - stop what is not used",
            "Commitments cut steady workloads 30 to 70 percent",
            "Tags, budgets, and alerts keep the bill from surprising anyone",
        ],
        "requirements": [
            "Cost allocation tags on every resource from day one",
            "Budgets with alerts before the first production bill",
        ],
        "standards": [
            "FinOps Foundation framework for cloud financial management",
            "Provider price books and service-level agreements",
        ],
        "citations": [CIT_ISO, CIT_NIST],
    },
    {
        "key": "cloud_apis",
        "name": "Cloud APIs and the Control Plane",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The control plane is the brain of the cloud: the set of APIs "
            "that create, configure, and destroy everything else. Every "
            "button in the web console, every command in the command-line "
            "tool, every infrastructure-as-code run ends as HTTPS calls to "
            "these APIs. The data plane is the muscle - the actual virtual "
            "machines, storage, and network paths carrying customer "
            "traffic - and the control plane directs it. Good control plane "
            "design rests on two properties: declarative state, where the "
            "caller says what should exist and the plane converges reality "
            "to match, and idempotency, where repeating the same call is "
            "safe. The demo computes a retry budget for a flaky call: five "
            "retries with exponential backoff starting at 1 second wait "
            "1, 2, 4, 8, then 16 seconds - 31 seconds of total waiting "
            "before giving up, which keeps a transient failure from "
            "becoming an outage. Rate limits protect the plane itself: "
            "every account gets a quota of API calls per second, and "
            "well-behaved clients back off when throttled instead of "
            "hammering."
        ),
        "sig_lens": (
            "The Signature authority speaks and the realm obeys. The "
            "control plane is the throne room: every decree - raise a "
            "vessel, fence a network, seal a vault - issues as a stamped "
            "command, and the data plane, the strong arm, carries it out. "
            "A wise decree may be repeated without harm, and a patient "
            "messenger waits 31 seconds through five attempts before "
            "reporting failure - the Signature method never mistakes a "
            "stumble for a fall."
        ),
        "how_it_works": (
            "A control plane call flows through authentication, "
            "authorization, validation, admission, and scheduling. The API "
            "gateway verifies the signature on the request, the policy "
            "engine checks the caller may perform the action, validators "
            "reject malformed input, admission controllers enforce "
            "organizational rules like required tags or allowed regions, "
            "and the scheduler places the work - choosing a host for a "
            "virtual machine, a zone for a replica. Controllers then run "
            "reconciliation loops: each watches the desired state stored "
            "in the database and the actual state reported by agents, and "
            "issues data plane operations until they match. This is why "
            "deleting a resource and recreating it converges instead of "
            "duplicating: the loop only creates what is missing. Event "
            "streams from the plane feed automation - a new virtual machine "
            "event can trigger configuration, registration, and monitoring "
            "without human hands."
        ),
        "key_points": [
            "Control plane: the APIs that manage everything; data plane: the resources themselves",
            "Declarative state: say what should exist, the plane converges reality",
            "Idempotency: repeating a call is safe",
            "Retry budget: 5 backoff retries total 31 seconds of waiting",
            "Rate limits protect the plane; clients must back off when throttled",
        ],
        "requirements": [
            "All automation through the API, never manual console clicks for production",
            "Retry with exponential backoff and jitter on every client",
        ],
        "standards": [
            "REST and JSON over HTTPS as the universal control interface",
            "OpenAPI descriptions for provider APIs",
        ],
        "citations": [CIT_ISO, CIT_NIST],
    },
]

# ---------------------------------------------------------------- compounded

ENTRIES += [
    {
        "key": "virtual_machines",
        "name": "Virtual Machines and Instance Families",
        "group": "Compute",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A cloud virtual machine is a rented slice of a physical server "
            "with a chosen ratio of virtual CPUs to memory, network, and "
            "storage, sold in instance families tuned for different "
            "workloads. General-purpose instances balance compute, memory, "
            "and networking for everyday applications. Compute-optimized "
            "instances pack more virtual CPUs per dollar for batch "
            "processing and media encoding. Memory-optimized instances "
            "carry large RAM for in-memory databases and caches. "
            "Storage-optimized instances add fast local NVMe disks for data "
            "warehouses, and accelerated instances attach GPUs for machine "
            "learning. The demo prices a workload needing 8 virtual CPUs: a "
            "general-purpose instance at 0.34 dollars per hour costs 248.20 "
            "dollars per month, while a compute-optimized instance at 0.30 "
            "dollars per hour costs 219.00 dollars - the right family saves "
            "29.20 dollars per month per machine, 350.40 per year. Sizing "
            "is the discipline: monitor actual CPU and memory utilization, "
            "then step down a size when the average sits below 40 percent. "
            "Burstable instances bank CPU credits for spiky workloads, and "
            "bare-metal instances remove the hypervisor for licensed or "
            "latency-critical software."
        ),
        "sig_lens": (
            "The Signature armory forges vessels in families, each bred "
            "for its labor. The general vessel serves all honest work, the "
            "swift vessel carries the heavy reckoning, the deep-minded "
            "vessel holds vast memory, the iron-bellied vessel guards the "
            "ledgers. The Signature quartermaster never buys a warhorse to "
            "pull a cart - the reckoning shows 29.20 saved each month by "
            "choosing the true family."
        ),
        "how_it_works": (
            "Launching a virtual machine is a control plane transaction: "
            "the scheduler picks a host with free capacity in the chosen "
            "zone, the hypervisor carves out virtual CPUs and memory, a "
            "boot volume is attached from block storage, the virtual "
            "network card is plugged into the chosen subnet, and the "
            "machine boots from a machine image - a frozen template of "
            "operating system and software. Instance families are "
            "hardware truth: the provider builds host fleets with "
            "different CPU-to-memory ratios and exposes them as families, "
            "so choosing a family chooses physical characteristics. "
            "Placement groups put machines close together for low-latency "
            "cluster traffic or spread them across racks for fault "
            "tolerance. Stopping a machine halts the compute meter while "
            "the attached volumes keep billing - the number one source of "
            "wasted spend is stopped machines with forgotten disks."
        ),
        "key_points": [
            "Instance families match hardware ratios to workload shapes",
            "Right family for 8 vCPUs: 219.00 versus 248.20 per month, saving 29.20",
            "Monitor utilization and step down when average CPU sits below 40 percent",
            "Burstable instances bank credits for spiky workloads",
            "Stopped machines stop compute billing but attached volumes keep billing",
        ],
        "requirements": [
            "A machine image with the operating system and agents baked in",
            "Utilization monitoring before and after sizing decisions",
        ],
        "standards": [
            "Provider instance type documentation and SLAs",
            "CIS benchmarks for guest operating system hardening",
        ],
        "citations": [CIT_NIST, CIT_ISO],
    },
    {
        "key": "containers",
        "name": "Containers and Container Images",
        "group": "Compute",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A container packages an application with its libraries and "
            "settings into a portable unit that runs the same on a laptop "
            "and in the cloud, sharing the host operating system kernel "
            "instead of virtualizing hardware. A container image is built "
            "from stacked layers: a base operating system layer, a runtime "
            "layer, and the application layer on top, each layer cached and "
            "shared. The demo measures the sharing: a base of 80 megabytes "
            "plus a runtime of 120 megabytes plus an application of 15 "
            "megabytes makes a 215 megabyte image, but ten containers on "
            "one host share the base and runtime layers, saving 9 times 80 "
            "megabytes - 720 megabytes of disk and download. Containers "
            "start in milliseconds versus seconds for virtual machines, "
            "and they pack far denser. The trade is isolation: containers "
            "share a kernel, so a kernel vulnerability can cross container "
            "boundaries where a hypervisor would stop it. Images should be "
            "minimal - distroless or Alpine bases - scanned for "
            "vulnerabilities, and rebuilt regularly rather than patched in "
            "place."
        ),
        "sig_lens": (
            "The Signature vessel is sealed at the forge with everything it "
            "needs inside - the craft, the tools, the provisions - so it "
            "sails identically on any sea. The layered sealing means ten "
            "vessels share one hull below the waterline, saving 720 "
            "megabytes of timber. But the Signature warden remembers: they "
            "share one keel, so the keel is guarded hardest of all."
        ),
        "how_it_works": (
            "Containers work through operating system primitives: "
            "namespaces give each container its own view of processes, "
            "network, and filesystem, while control groups limit its CPU, "
            "memory, and I/O. The image layers are assembled by a "
            "union filesystem that presents the stack as one merged view, "
            "with the top writable layer capturing changes. Building an "
            "image runs a recipe - the Dockerfile - executing each "
            "instruction as a new layer, so unchanged layers are reused "
            "from cache. A registry stores and distributes images; pulling "
            "fetches only the layers the host lacks. At runtime the "
            "container engine creates the namespaces, applies the resource "
            "limits, mounts the filesystem, and starts the application as "
            "process one inside its own view of the world."
        ),
        "key_points": [
            "Containers share the host kernel; images are layered and portable",
            "215 megabyte image; ten containers share layers to save 720 megabytes",
            "Millisecond startup and dense packing versus virtual machines",
            "Weaker isolation than VMs - kernel vulnerabilities can cross boundaries",
            "Minimal base images, vulnerability scanning, rebuild instead of patch",
        ],
        "requirements": [
            "A container runtime on every host",
            "A private image registry with access control",
        ],
        "standards": [
            "OCI image and runtime specifications",
            "CNCF cloud native definition",
        ],
        "citations": [CIT_K8S, CIT_ISO],
    },
    {
        "key": "kubernetes",
        "name": "Container Orchestration with Kubernetes",
        "group": "Compute",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Kubernetes is the open-source orchestrator that runs container "
            "workloads at scale: it schedules containers onto machines, "
            "restarts failed ones, scales them with demand, and rolls out "
            "new versions without downtime. The smallest unit is the pod - "
            "one or more containers sharing network and storage - and pods "
            "are grouped by deployments that declare the desired replica "
            "count. The demo schedules 6 replicas with 4 pods fitting per "
            "node: the ceiling of 6 divided by 4 is 2 nodes. A rolling "
            "update with a 25 percent max surge allows the ceiling of 6 "
            "times 1.25 - 8 pods at peak, so the new version ramps up "
            "before the old ramps down. Services give pods stable virtual "
            "addresses and load balancing; config maps and secrets inject "
            "configuration; persistent volumes attach storage. The control "
            "plane - API server, scheduler, controller manager - holds the "
            "desired state in etcd, and node agents converge reality to "
            "match. Managed Kubernetes offerings run the control plane for "
            "the customer, leaving only the worker nodes to operate."
        ),
        "sig_lens": (
            "The Signature fleet sails under one admiral. The orchestrator "
            "is the flagship: it counts the vessels, stations them on sound "
            "hulls, replaces the fallen, and changes the fleet sails "
            "without ever stopping the voyage - 6 vessels across 2 hulls, "
            "8 at the height of the changing. The Signature admiral declares "
            "the desired fleet and the sea obeys."
        ),
        "how_it_works": (
            "Kubernetes works as a reconciliation machine. The user posts "
            "declarations - deployments, services, config - to the API "
            "server, which validates and stores them in etcd. Controllers "
            "watch for changes: the deployment controller creates replica "
            "sets, the replica set controller ensures the pod count "
            "matches, the scheduler assigns each pending pod to a node with "
            "fitting resources, and the kubelet on each node pulls images "
            "and starts containers. Probes decide health: liveness probes "
            "restart stuck containers, readiness probes hold traffic until "
            "a pod is truly ready. Rolling updates create new pods and "
            "delete old ones within the surge and unavailable budgets, so "
            "capacity never drops. If a node dies, its pods are rescheduled "
            "elsewhere - the system heals toward the declared state "
            "without human intervention."
        ),
        "key_points": [
            "Pods are the unit; deployments declare the desired replica count",
            "6 replicas at 4 per node schedule onto 2 nodes",
            "Rolling update with 25 percent surge peaks at 8 pods",
            "Services, config maps, secrets, and persistent volumes complete the model",
            "Reconciliation loops heal the system toward declared state",
        ],
        "requirements": [
            "Container images in a registry the cluster can reach",
            "Liveness and readiness probes on every workload",
        ],
        "standards": [
            "Kubernetes API and OCI conformance",
            "CNCF graduated project governance",
        ],
        "citations": [CIT_K8S, CIT_ISO],
    },
    {
        "key": "serverless",
        "name": "Serverless Computing and Functions as a Service",
        "group": "Compute",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Serverless computing lets developers run code without managing "
            "any servers: the provider provisions, scales, and bills "
            "execution in fine slices. Functions as a Service is the "
            "purest form - a single function, triggered by an event such as "
            "an HTTP request, a file upload, or a queue message, running "
            "for seconds and billed per invocation. The demo prices one "
            "million invocations using 512 megabytes for 200 milliseconds "
            "each: 100,000 gigabyte-seconds at 0.0000166667 dollars each is "
            "1.67 dollars, plus 0.20 dollars per million requests, for a "
            "total of 1.87 dollars - the workload that needs no idle "
            "server costs less than two dollars. Scaling is automatic and "
            "near-instant, from zero to thousands of concurrent executions. "
            "The constraints are real: maximum execution times of minutes, "
            "cold starts that add latency to idle functions, statelessness "
            "that pushes state to external stores, and bills that punish "
            "constant high-volume workloads a reserved server would serve "
            "cheaper. Serverless fits event-driven, spiky, and glue "
            "workloads; it is the wrong tool for sustained heavy compute."
        ),
        "sig_lens": (
            "The Signature spark needs no hearth kept burning. The function "
            "is a sealed spell: speak the triggering word and it blazes for "
            "its instant - one million castings for 1.87 in coin - then "
            "vanishes, leaving no ember to feed. The Signature mage keeps "
            "no idle fires; but for the labor that never sleeps, he builds "
            "a hearth instead, for endless sparks cost more than one steady "
            "flame."
        ),
        "how_it_works": (
            "A function platform works by keeping warm pools of execution "
            "environments and routing events to them. When an event "
            "arrives, the router picks a warm sandbox with the function "
            "code loaded or provisions a fresh one - the cold start - "
            "injects the event, runs the handler, captures the result, and "
            "freezes or destroys the sandbox. Concurrency limits cap how "
            "many executions run at once; beyond the limit, events queue "
            "or throttle. Billing meters the configured memory multiplied "
            "by execution time, rounded up, plus a per-request charge. "
            "State lives outside: functions read and write databases, "
            "object storage, and queues, which is why serverless "
            "architectures are drawn as functions wired to managed "
            "services. Provisioned concurrency keeps a chosen number of "
            "environments warm to erase cold starts for latency-sensitive "
            "paths - at a steady hourly price."
        ),
        "key_points": [
            "No servers to manage; provider provisions, scales, and bills per execution",
            "One million invocations at 512MB for 200ms costs 1.87 dollars",
            "Automatic scaling from zero to thousands of concurrent executions",
            "Constraints: minute-scale time limits, cold starts, statelessness",
            "Best for event-driven and spiky work; costly for sustained heavy compute",
        ],
        "requirements": [
            "Event sources wired to function triggers",
            "External state stores - functions hold no state",
        ],
        "standards": [
            "CNCF CloudEvents specification for event format",
            "Provider function runtime and trigger documentation",
        ],
        "citations": [CIT_K8S, CIT_ISO],
    },
    {
        "key": "object_storage_deep",
        "name": "Object Storage Deep Dive",
        "group": "Storage",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Object storage is the cloud exabyte attic: flat namespaces of "
            "objects addressed by unique keys over HTTP, engineered for "
            "eleven nines of durability - 99.999999999 percent. Eleven "
            "nines means the annual probability of losing one specific "
            "object is 1 in 100 billion; the demo shows that storing one "
            "million objects yields an expected loss of 0.00001 objects "
            "per year - effectively zero. Durability comes from erasure "
            "coding across many disks and zones, not from expensive "
            "hardware. Storage classes trade retrieval speed and cost: "
            "standard for hot data, infrequent-access for data read "
            "monthly, archive tiers for data read yearly with retrieval "
            "times of minutes to hours. Versioning keeps every overwrite "
            "as a recoverable version; object lock makes objects immutable "
            "for compliance; lifecycle rules move aging objects down the "
            "classes automatically. Event notifications fire on every put "
            "and delete, which is what makes object storage the trigger "
            "source for serverless data pipelines."
        ),
        "sig_lens": (
            "The Signature vault of vaults holds parcels beyond counting, "
            "each sealed under its true key, guarded to eleven nines - a "
            "million parcels and the expected loss is 0.00001, which is to "
            "say none. The Signature archivist sorts the vault by warmth: "
            "the daily ledgers by the door, the yearly chronicles in the "
            "deep cold, each parcel sliding deeper as its days pass, none "
            "ever truly lost."
        ),
        "how_it_works": (
            "Durability is mathematics, not magic. Each object is split "
            "into data fragments plus parity fragments - for example 12 "
            "data plus 4 parity - spread across racks and zones, so any 12 "
            "of 16 fragments reconstruct the object; several simultaneous "
            "disk or rack failures still lose nothing. Writes are "
            "acknowledged after a quorum of fragments persist, and "
            "background scrubbers continuously verify checksums, "
            "rebuilding weak fragments before they fail. Consistency is "
            "strong: a successful write is immediately readable everywhere. "
            "The key namespace is flat - prefixes merely look like folders "
            "to humans - and the system partitions the key space across "
            "thousands of servers, which is why throughput scales with key "
            "diversity. Multipart upload splits large objects into parallel "
            "parts for speed and resumability."
        ),
        "key_points": [
            "Eleven nines durability: 1 in 100 billion annual loss per object",
            "One million objects: expected yearly loss 0.00001 - effectively zero",
            "Erasure coding across zones, not expensive hardware, delivers durability",
            "Storage classes trade retrieval speed against cost",
            "Versioning, object lock, lifecycle rules, and event notifications",
        ],
        "requirements": [
            "Unique, well-planned key naming for partitioning",
            "Lifecycle policies from the first large ingest",
        ],
        "standards": [
            "S3-compatible API as the de facto object standard",
            "ISO/IEC 27040 storage security guidance",
        ],
        "citations": [CIT_ISO, CIT_NIST],
    },
    {
        "key": "block_file_storage",
        "name": "Block and File Storage Systems",
        "group": "Storage",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Block storage gives one virtual machine a raw disk over the "
            "network with sub-millisecond latency; file storage gives many "
            "machines a shared network filesystem. Block volumes are the "
            "right home for boot disks and databases: a general-purpose "
            "volume delivers a 3,000 IOPS baseline with 125 megabytes per "
            "second throughput, and provisioned volumes scale to 16,000 "
            "IOPS and beyond for demanding databases. The demo times a "
            "full read: one terabyte at 125 megabytes per second takes "
            "8,000 seconds - about 2.22 hours - which is why throughput, "
            "not just IOPS, belongs in every storage decision. Snapshots "
            "capture point-in-time copies incrementally - only changed "
            "blocks are stored - making them cheap and fast, and they are "
            "the foundation of backup strategies. File systems scale "
            "differently: throughput grows with stored data, and they "
            "serve thousands of concurrent clients for shared content, "
            "home directories, and media rendering farms. The rule: "
            "databases on block, shared content on file, archives on "
            "object."
        ),
        "sig_lens": (
            "The Signature smith keeps two more storehouses beside the "
            "vault. The block anvil is bolted to a single vessel - swift "
            "as thought at 3,000 strokes per breath, yet a full granary of "
            "a terabyte takes 8,000 seconds to empty through its gate. The "
            "file hall is the long common table where a thousand vessels "
            "break the same bread at once. The Signature steward never "
            "seats the ledger-keeper at the common table nor stores the "
            "harvest on the anvil."
        ),
        "how_it_works": (
            "Network block storage works by replicating every write "
            "synchronously to multiple storage servers before "
            "acknowledging, so a server failure loses nothing; the guest "
            "operating system sees an ordinary block device and formats it "
            "with any filesystem. Performance is provisioned independently "
            "of size: IOPS and throughput are allocated per volume, and "
            "burst credits let small volumes spike. Snapshots freeze the "
            "block map and copy changed blocks to object storage in the "
            "background, so creating one takes seconds regardless of "
            "volume size. Managed file systems work by running clustered "
            "file servers behind a single namespace: clients mount over "
            "NFS or SMB, metadata is distributed, and throughput scales "
            "with the dataset. Both replicate across zones for the "
            "standard multi-zone durability."
        ),
        "key_points": [
            "Block: one VM, raw disk, sub-millisecond latency, 3,000 IOPS baseline",
            "One terabyte at 125 MB per second reads in 8,000 seconds",
            "Snapshots are incremental and instant - the backup foundation",
            "File: shared namespace for thousands of concurrent clients",
            "Databases on block, shared content on file, archives on object",
        ],
        "requirements": [
            "IOPS and throughput provisioned for the actual workload, not the default",
            "Snapshot schedules before production data lands",
        ],
        "standards": [
            "NVMe and SCSI block protocols",
            "NFSv4.1 and SMB 3 for network file access",
        ],
        "citations": [CIT_ISO],
    },
    {
        "key": "managed_databases",
        "name": "Managed Databases: Relational and NoSQL",
        "group": "Storage",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Managed databases move the undifferentiated labor - "
            "provisioning, patching, backups, failover - to the provider "
            "while the customer keeps the schema and the queries. "
            "Relational services run familiar engines with ACID "
            "transactions, automated backups, and multi-zone standby "
            "replicas that promote within 60 to 120 seconds of a primary "
            "failure. Read replicas scale read throughput horizontally: "
            "the demo runs a primary taking 1,000 writes per second with "
            "three replicas each serving 5,000 reads per second, for "
            "15,000 reads per second of total read capacity. NoSQL "
            "services trade the relational model for other shapes: "
            "key-value for session state, document for flexible JSON, "
            "wide-column for time series, graph for relationships - each "
            "scaling horizontally by partitioning data across nodes. "
            "Serverless database options go further, scaling capacity to "
            "zero when idle and billing per request. The choice hinges on "
            "the access pattern and consistency needs: strong consistency "
            "and joins point to relational, massive scale with simple "
            "lookups points to key-value, and the wrong choice is paid "
            "for in application complexity."
        ),
        "sig_lens": (
            "The Signature scriptorium keeps the ledgers without the "
            "drudgery. The provider monks copy, mend, and guard the tomes "
            "- the failover quill passes to the standby in 60 to 120 "
            "heartbeats - while the master keeps only the words and the "
            "questions. Three reading desks each serve 5,000 readers, "
            "15,000 in all, while the single writing desk takes 1,000. The "
            "Signature scholar chooses the tome by the shape of the "
            "knowledge, never forcing ledgers into poetry."
        ),
        "how_it_works": (
            "A managed relational database works by automating the "
            "operations playbook: the control plane provisions the "
            "instance, configures synchronous replication to a standby in "
            "another zone, schedules automated backups with point-in-time "
            "recovery, applies minor version patches in maintenance "
            "windows, and monitors replication lag. Failover is a DNS and "
            "endpoint flip: health checks detect the primary failure, the "
            "standby is promoted, and the endpoint now routes to it - "
            "typically inside two minutes. Read replicas use asynchronous "
            "replication, accepting milliseconds of lag for horizontal "
            "read scale. NoSQL services partition by a partition key: each "
            "key hashes to a partition served by specific nodes, and "
            "throughput scales by adding partitions. Serverless variants "
            "replace provisioned nodes with a proxy fleet that scales "
            "compute per request."
        ),
        "key_points": [
            "Provider handles provisioning, patching, backup, and failover",
            "Multi-zone failover completes in 60 to 120 seconds",
            "Three read replicas at 5,000 rps each: 15,000 rps read capacity",
            "NoSQL scales horizontally by partition key",
            "Choose by access pattern and consistency needs",
        ],
        "requirements": [
            "Backup retention and point-in-time recovery configured",
            "Read/write splitting in the application for replica use",
        ],
        "standards": [
            "SQL standard for relational engines",
            "ACID properties for transactional guarantees",
        ],
        "citations": [CIT_ISO, CIT_SRE],
    },
    {
        "key": "load_balancing",
        "name": "Load Balancing and Auto Scaling",
        "group": "Networking",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Load balancing spreads incoming traffic across healthy "
            "targets; auto scaling changes the number of targets with "
            "demand. Together they deliver both availability and "
            "elasticity. A load balancer terminates client connections, "
            "runs health checks against each target, and forwards only to "
            "healthy ones - round robin, least connections, or weighted "
            "algorithms decide the split. The demo sends 9,000 requests "
            "through round robin to 3 healthy servers: each receives "
            "exactly 3,000, the even split that defines the algorithm. "
            "Auto scaling policies watch metrics - average CPU, request "
            "count per target, queue depth - and add capacity when "
            "thresholds breach, removing it during cooldowns when demand "
            "falls. Target tracking policies hold a metric at a chosen "
            "value, like 50 percent CPU, growing and shrinking the fleet "
            "to stay there. Health check grace periods keep new instances "
            "from being killed before they finish booting, and termination "
            "policies retire the oldest or the least-busy first."
        ),
        "sig_lens": (
            "The Signature gatehouse divides the arriving caravan with a "
            "perfect hand: 9,000 travelers to 3 gates, 3,000 each, none "
            "favored, none starved - and the sick gate is closed until it "
            "heals. Behind the gates the Signature steward watches the "
            "strain: when the burden passes the mark, new porters are "
            "summoned; when the hall empties, they are dismissed with "
            "thanks. Strength exactly where the need is, never more, never "
            "less."
        ),
        "how_it_works": (
            "An application load balancer works at layer 7: it terminates "
            "TLS, inspects the HTTP request, applies routing rules by path "
            "or host, and forwards to a target group. Health checks - "
            "HTTP requests to a health endpoint every 30 seconds by "
            "default - mark targets healthy or unhealthy; unhealthy "
            "targets get no traffic until they recover. Network load "
            "balancers work at layer 4 for extreme throughput with static "
            "IP addresses. Auto scaling groups wrap the fleet: launch "
            "templates define the machine image and size, the group keeps "
            "the desired count, and scaling policies adjust it. Step "
            "scaling adds more capacity the further the metric breaches; "
            "scheduled scaling pre-warms for known peaks like Monday "
            "morning. Lifecycle hooks pause launches and terminations so "
            "warmup scripts and connection draining complete cleanly."
        ),
        "key_points": [
            "Load balancers forward only to healthy targets",
            "Round robin over 3 servers splits 9,000 requests into 3,000 each",
            "Auto scaling adjusts fleet size from metrics like CPU or queue depth",
            "Target tracking holds a metric at its set point automatically",
            "Grace periods and lifecycle hooks keep scaling from killing booting instances",
        ],
        "requirements": [
            "A fast, honest health endpoint on every target",
            "Scaling policies tuned with cooldowns to avoid flapping",
        ],
        "standards": [
            "HTTP health check conventions",
            "TLS termination best practices",
        ],
        "citations": [CIT_SRE, CIT_ISO],
    },
    {
        "key": "cdn_edge",
        "name": "Content Delivery Networks and Edge Caching",
        "group": "Networking",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A content delivery network caches content at edge locations "
            "around the world so users fetch from nearby instead of from "
            "the origin region. The cache hit ratio - the fraction of "
            "requests served from cache - decides the value: the demo uses "
            "a 0.92 hit ratio with 25 millisecond edge latency against 400 "
            "millisecond origin latency, giving an effective latency of "
            "0.92 times 25 plus 0.08 times 400 - 55.0 milliseconds, over "
            "seven times faster than the origin alone. The same ratio cuts "
            "origin load: 920 gigabytes of every terabyte are served from "
            "cache, leaving only 80 gigabytes to reach the origin. "
            "Cache-control headers set time-to-live per object; "
            "invalidation purges stale objects on demand when content "
            "changes. Dynamic content benefits too: connection termination "
            "at the edge and optimized middle-mile routing cut handshake "
            "time even when nothing is cached. Signed URLs and signed "
            "cookies gate private content at the edge without touching the "
            "origin."
        ),
        "sig_lens": (
            "The Signature outriders carry the chronicles to the far posts "
            "before they are asked. Nine hundred twenty of every thousand "
            "requests are answered at the post in 25 heartbeats instead of "
            "trekking 400 to the capital - the effective journey is 55. "
            "The Signature quartermaster stamps each parcel with its "
            "freshness, recalls the stale by courier when the truth "
            "changes, and seals the private parcels so only the named "
            "reader may open them."
        ),
        "how_it_works": (
            "A CDN works by anycast or DNS steering: the user request "
            "resolves to the nearest edge location, which checks its "
            "cache. On a hit, the object returns immediately. On a miss, "
            "the edge fetches from the origin - or from a regional edge "
            "cache tier that shields the origin - stores the response per "
            "its cache-control headers, and serves it. Hierarchical "
            "caching means misses collapse: a thousand simultaneous "
            "misses for one object produce one origin fetch. Invalidation "
            "walks the edge fleet purging the named objects; versioned "
            "filenames - app.v2.js instead of app.js - avoid invalidation "
            "entirely by making each deploy a new cache key. For dynamic "
            "APIs, the edge terminates TLS nearby and holds persistent "
            "optimized connections to the origin, cutting the handshake "
            "round trips that dominate distant requests."
        ),
        "key_points": [
            "Edge caching serves users from nearby instead of the origin region",
            "0.92 hit ratio: effective latency 55.0 ms versus 400 ms origin",
            "920 of every 1,000 gigabytes served from cache",
            "Cache-control headers and versioned filenames manage freshness",
            "Signed URLs gate private content at the edge",
        ],
        "requirements": [
            "Cache-control headers set deliberately per content type",
            "An invalidation or versioning strategy for deploys",
        ],
        "standards": [
            "RFC 9111 HTTP caching semantics",
            "RFC 7234 cache-control directives",
        ],
        "citations": [CIT_ISO],
    },
    {
        "key": "cloud_network_security",
        "name": "Cloud Network Security: Firewalls, TLS, and Zero Trust",
        "group": "Security",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Cloud network security layers defenses: security groups and "
            "network filters control who may reach what, TLS encrypts "
            "traffic in flight, and zero trust removes the idea of a safe "
            "inside network. Defense in depth means a request passes "
            "multiple independent checks - edge firewall, subnet filter, "
            "security group, application authentication - so one "
            "misconfiguration does not open everything. TLS with modern "
            "cipher suites and certificate automation keeps traffic "
            "private; private certificate authorities issue internal "
            "certificates with short lifetimes. Zero trust is the "
            "principle that no network location is trusted: every request "
            "is authenticated, authorized, and encrypted regardless of "
            "source. The demo enforces a zero trust matrix of 5 services "
            "and 4 caller identities against 9 explicit allow rules: of 20 "
            "possible caller-to-service pairs, exactly 9 are permitted and "
            "11 denied - the default-deny posture made visible. Micro-"
            "segmentation applies the same idea inside the virtual "
            "network, so a compromised web server cannot freely reach the "
            "database tier."
        ),
        "sig_lens": (
            "The Signature fortress trusts no road, only warrants. Every "
            "traveler is challenged at every gate - the outer wall, the "
            "district wall, the house door - each with its own guards and "
            "its own seal, so one sleeping sentry never opens the keep. "
            "Of 20 who approach the five inner chambers, 9 bear true "
            "warrants and 11 are turned away; the Signature warden counts "
            "the denied as proudly as the admitted, for the count proves "
            "the gates hold."
        ),
        "how_it_works": (
            "The layers work as successive filters. Edge firewalls and "
            "web application firewalls inspect inbound traffic for attack "
            "patterns - SQL injection, cross-site scripting - before it "
            "reaches the virtual network. Subnet network access control "
            "lists apply stateless rules at the subnet boundary. Security "
            "groups apply stateful rules per resource. Inside, service "
            "identity - not IP address - authorizes calls: each workload "
            "gets a cryptographic identity, presents it with every "
            "request over mutual TLS, and the receiver checks it against "
            "policy. Certificate rotation is automated so keys stay fresh. "
            "Logging every allowed and denied flow into a central lake "
            "lets detection systems spot the anomaly - the database "
            "talking to an unknown host at 3 a.m. - that static rules "
            "miss."
        ),
        "key_points": [
            "Defense in depth: edge, subnet, security group, application checks",
            "TLS encrypts in flight; automate certificates with short lifetimes",
            "Zero trust: authenticate and authorize every request, trust no network",
            "Demo matrix: 9 of 20 caller-service pairs allowed, 11 denied by default",
            "Micro-segmentation contains a breach to one tier",
        ],
        "requirements": [
            "Default-deny rules with explicit allows, reviewed regularly",
            "Mutual TLS and workload identity for service-to-service calls",
        ],
        "standards": [
            "NIST SP 800-207: Zero Trust Architecture",
            "TLS 1.2 or higher; NIST SP 800-52 guidelines",
        ],
        "citations": [CIT_NIST],
    },
    {
        "key": "observability",
        "name": "Monitoring, Logging, and Observability",
        "group": "Operations",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Observability is the ability to understand a system from its "
            "outputs, built on three pillars: metrics, logs, and traces. "
            "Metrics are numbers over time - CPU, latency, error rate - "
            "aggregated and alerted on. Logs are discrete event records - "
            "every request, every error, every decision - searchable for "
            "forensics. Traces follow one request across service "
            "boundaries, showing where its time went. Service-level "
            "objectives turn this into a contract: the demo sets 99.9 "
            "percent availability over 30 days, giving an error budget of "
            "0.1 percent of 43,200 minutes - 43.2 minutes of allowed "
            "downtime per month. Burn through the budget faster than the "
            "alert thresholds and the pager fires; stay inside it and the "
            "team ships features instead of firefighting. The four golden "
            "signals - latency, traffic, errors, saturation - are the "
            "minimum dashboard for any user-facing service. Structured "
            "JSON logs with request IDs make the pillars joinable: from a "
            "metric spike to the exact trace to the exact log line."
        ),
        "sig_lens": (
            "The Signature watchtower sees the realm three ways: the "
            "counting beads of metrics, the chronicle pages of logs, and "
            "the thread of traces that follows one messenger through every "
            "hall. The covenant allows 43.2 minutes of darkness in 30 days "
            "- the error budget - and the watchers ring the bell the hour "
            "it burns too fast. The Signature steward would rather read "
            "the signs at dawn than fight the fire at midnight."
        ),
        "how_it_works": (
            "Metrics flow from agents on every host and from application "
            "instrumentation into a time-series store, where alerting "
            "rules evaluate expressions like error rate over five minutes "
            "and page when thresholds breach. Logs stream from "
            "applications as structured JSON into a central index, "
            "retained by tier - hot for days, warm for weeks, cold for "
            "months. Tracing works by propagation: each service passes a "
            "trace ID in request headers, records spans with start and end "
            "times, and a collector assembles the full tree. SLOs are "
            "computed from the same telemetry: successful events divided "
            "by total events over the window, compared against the "
            "objective, with burn-rate alerts firing when the budget "
            "consumes too fast. Dashboards compose the golden signals; "
            "runbooks linked from each alert tell the responder exactly "
            "what to check first."
        ),
        "key_points": [
            "Three pillars: metrics, logs, and traces",
            "SLO 99.9 percent over 30 days: error budget 43.2 minutes",
            "Four golden signals: latency, traffic, errors, saturation",
            "Burn-rate alerts page when the budget drains too fast",
            "Structured logs with request IDs join the pillars together",
        ],
        "requirements": [
            "Instrumentation with trace propagation before production launch",
            "SLOs and burn-rate alerts on every user-facing service",
        ],
        "standards": [
            "OpenTelemetry for vendor-neutral instrumentation",
            "Google SRE workbook alerting practices",
        ],
        "citations": [CIT_SRE],
    },
    {
        "key": "infrastructure_as_code",
        "name": "Infrastructure as Code",
        "group": "Operations",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Infrastructure as code manages cloud resources with versioned "
            "definition files instead of manual console clicks. The "
            "declarations - virtual networks, machines, databases, "
            "policies - live in a repository with history, review, and "
            "rollback like application code. The tool computes a plan by "
            "diffing desired state against actual state: the demo starts "
            "from 5 desired resources against 3 existing - 2 matching, 1 "
            "drifted - and produces a plan of 3 creations and 1 update, 0 "
            "deletions. Applying the plan converges reality to the "
            "declaration through the control plane APIs. State files track "
            "what was created so later runs know what to change; locking "
            "prevents two applies from corrupting that state. Drift "
            "detection re-runs the diff on schedule and reports manual "
            "changes made outside the code. Modules package reusable "
            "patterns - a standard virtual network, a hardened database - "
            "so every team builds on the same reviewed foundations."
        ),
        "sig_lens": (
            "The Signature architect draws the fortress before a single "
            "stone is cut, and the drawing is law. The plan reckons 5 "
            "decreed works against 3 standing - 2 true, 1 strayed - and "
            "commands 3 raisings and 1 mending, 0 teardowns. The Signature "
            "ledger of state remembers every stone laid, so no two "
            "master builders raise the same wall twice, and the night "
            "watch reports any stone moved by hand outside the drawing."
        ),
        "how_it_works": (
            "The tool works in three phases. First it reads the "
            "configuration files and builds a desired-state graph with "
            "dependencies - the database before the application that uses "
            "it. Then it refreshes: querying the control plane APIs for "
            "actual state and comparing, resource by resource, producing "
            "the plan of creates, updates, and deletes. The human reviews "
            "the plan - this is the code review for infrastructure. Then "
            "apply executes the changes in dependency order, with "
            "parallelism where safe, writing results back to the state "
            "file. Providers are plugins translating declarations into "
            "API calls for each cloud. Import commands adopt manually "
            "created resources into management; targeted applies and "
            "workspaces separate environments. The whole flow runs in "
            "pipelines, so infrastructure changes get the same tests, "
            "approvals, and audit trail as code changes."
        ),
        "key_points": [
            "Versioned definitions replace manual console work",
            "Plan diff: 5 desired vs 3 actual yields 3 creates, 1 update, 0 deletes",
            "State files track reality; locking prevents concurrent corruption",
            "Drift detection reports out-of-band manual changes",
            "Modules package reviewed, reusable patterns",
        ],
        "requirements": [
            "Remote state storage with locking from the first apply",
            "Pipeline-driven applies with plan review for production",
        ],
        "standards": [
            "Declarative configuration languages per tool",
            "State encryption at rest",
        ],
        "citations": [CIT_SRE, CIT_ISO],
    },
    {
        "key": "messaging_events",
        "name": "Message Queues and Event-Driven Architecture",
        "group": "Architecture",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Message queues decouple services: producers drop messages "
            "into a queue and move on, consumers process them at their "
            "own pace, and neither needs the other to be alive at the "
            "same moment. This absorbs spikes - the queue is a shock "
            "absorber between a bursty front end and a steady back end. "
            "The demo models the absorber: messages arrive at 500 per "
            "second while consumers process 450 per second, so the "
            "backlog grows by 50 per second and reaches 3,000 messages "
            "after 60 seconds - visible, bounded, and draining when the "
            "spike passes. Little law governs capacity planning: average "
            "messages in system equals arrival rate times average time in "
            "system. Event buses go further, broadcasting events to many "
            "subscribers so new consumers can attach without changing "
            "producers. Ordering, deduplication, and dead-letter queues - "
            "where poison messages go after repeated failures - are the "
            "operational details that separate a demo queue from a "
            "production one. At-least-once delivery is the honest default: "
            "consumers must be idempotent."
        ),
        "sig_lens": (
            "The Signature courier hall never keeps the sender waiting. "
            "The merchant drops his parcel and departs; the porters carry "
            "at their steady pace. When 500 parcels arrive each breath and "
            "450 are carried, the hall holds the 50 difference - 3,000 "
            "after 60 breaths - patient and in order, until the rush "
            "passes. The poisoned parcel, thrice refused, is set aside in "
            "the dead-letter vault for the masters judgment, and no "
            "porter ever carries the same parcel twice unknowingly."
        ),
        "how_it_works": (
            "A queue works as a durable buffer: producers send messages "
            "over the API, the service writes them to replicated storage "
            "and acknowledges, and consumers long-poll for batches, "
            "process them, and delete each message only after success - "
            "an unprocessed message reappears after the visibility "
            "timeout. FIFO queues preserve order within a message group "
            "at lower throughput; standard queues maximize throughput "
            "with best-effort ordering. Event buses match published "
            "events against subscriber rules and fan out to queues, "
            "functions, and streams. Dead-letter queues collect messages "
            "that fail processing a configured number of times, giving "
            "operators a place to inspect and replay. Scaling is "
            "independent per side: add producers freely, add consumers to "
            "drain faster, set alarms on queue age so a growing backlog "
            "pages before it becomes an outage."
        ),
        "key_points": [
            "Queues decouple producers from consumers across time",
            "500 in per second vs 450 processed: backlog 3,000 after 60 seconds",
            "Event buses fan out to many subscribers without producer changes",
            "Dead-letter queues isolate poison messages for inspection",
            "At-least-once delivery means consumers must be idempotent",
        ],
        "requirements": [
            "Idempotent consumers before at-least-once delivery",
            "Alarms on queue age and dead-letter depth",
        ],
        "standards": [
            "AMQP 1.0 for interoperable messaging",
            "CNCF CloudEvents for event format",
        ],
        "citations": [CIT_K8S, CIT_ISO],
    },
    {
        "key": "backup_dr",
        "name": "Backup and Disaster Recovery: RPO and RTO",
        "group": "Operations",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Disaster recovery is governed by two numbers: the recovery "
            "point objective, how much data loss is tolerable, and the "
            "recovery time objective, how long restoration may take. An "
            "RPO of 15 minutes means backups or replication must capture "
            "every 15 minutes of work; an RTO of 4 hours means the system "
            "must be serving again within 4 hours of the disaster "
            "declaration. The demo validates a backup window: 2 terabytes "
            "at 200 megabytes per second copies in 10,000 seconds - 2.78 "
            "hours, inside a 4-hour window with margin. Strategies ascend "
            "in cost and speed: backup and restore is cheapest and "
            "slowest, pilot light keeps a minimal copy warm, warm standby "
            "keeps a scaled-down copy running, and multi-site active "
            "configuration serves from two places at once with near-zero "
            "RTO. Backups must be tested by restore, not by faith: an "
            "untested backup is a hope. Immutable and cross-region backup "
            "copies survive the ransomware scenario that destroys the "
            "primary account."
        ),
        "sig_lens": (
            "The Signature chronicler loses no more than 15 minutes of "
            "history - that is the covenant of the point - and raises the "
            "halls again within 4 hours - that is the covenant of the "
            "time. The copy of the 2-terabyte chronicle completes in "
            "10,000 heartbeats, 2.78 hours, inside the allotted watch. "
            "The Signature vault keeps its copies in a second kingdom "
            "under seal unbreakable even by treachery, and every copy is "
            "proven by raising, never by trust alone."
        ),
        "how_it_works": (
            "Recovery works from the bottom of the stack upward. Storage "
            "snapshots give point-in-time volume copies in seconds; "
            "database automated backups give point-in-time restore to any "
            "second in the retention window via transaction log replay; "
            "cross-region replication copies snapshots and backups to a "
            "second region continuously. Runbooks declare the order: "
            "restore the data plane, re-point DNS, verify health checks, "
            "replay the queued transactions. Pilot light keeps the "
            "database replicating and the machine images ready so recovery "
            "is launch plus restore; warm standby keeps the application "
            "tier running at minimum size so recovery is scale plus "
            "restore. Game days rehearse the runbook quarterly - teams "
            "that have failed over for practice fail over calmly for "
            "real. The RPO is set by replication frequency, the RTO by "
            "automation completeness."
        ),
        "key_points": [
            "RPO: tolerable data loss; RTO: tolerable restoration time",
            "Sample: RPO 15 minutes, RTO 4 hours",
            "2 terabytes at 200 MB per second backs up in 10,000 seconds",
            "Strategies: backup-restore, pilot light, warm standby, multi-site",
            "Test by restore; keep immutable cross-region copies",
        ],
        "requirements": [
            "RPO and RTO declared per workload with business sign-off",
            "Quarterly restore tests and game-day rehearsals",
        ],
        "standards": [
            "ISO/IEC 27031 business continuity guidance",
            "NIST SP 800-34 contingency planning",
        ],
        "citations": [CIT_SRE],
    },
]

# ------------------------------------------------------------------ advanced

ENTRIES += [
    {
        "key": "cicd",
        "name": "CI/CD Pipelines and Deployment Strategies",
        "group": "Operations",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Continuous integration and continuous delivery automate the "
            "path from code commit to production: build, test, and deploy "
            "on every change, with humans approving only what policy "
            "requires. The pipeline stages are build the artifact, run the "
            "unit and integration tests, scan for vulnerabilities, and "
            "promote through environments. The demo times a typical run: "
            "180 seconds to build, 240 to test, 90 to deploy - a lead time "
            "of 510 seconds, 8.5 minutes from commit to serving traffic. "
            "Deployment strategies control the blast radius: rolling "
            "updates replace instances gradually, blue-green runs two full "
            "environments and flips the router for instant rollback, "
            "canary sends a slice of traffic to the new version first - "
            "the demo sends 10 percent of 50 pods, 5 pods, to the canary. "
            "Feature flags decouple deployment from release, so code ships "
            "dark and lights up per user. The DORA metrics - deployment "
            "frequency, lead time, change failure rate, restore time - "
            "measure whether the pipeline is actually elite."
        ),
        "sig_lens": (
            "The Signature road from quill to throne is paved and "
            "guarded. Every decree is built in 180 heartbeats, proven in "
            "240, and enthroned in 90 - 510 heartbeats from thought to "
            "reign. The cautious king tries the new law on 5 of his 50 "
            "provinces first; if the canary provinces prosper, the law "
            "spreads, and if they suffer, the old law returns by dusk. The "
            "Signature banner is raised in the dark and unfurled only "
            "where it is welcome."
        ),
        "how_it_works": (
            "A pipeline works as a chain of stages with artifacts passing "
            "between them. The commit triggers the build stage, which "
            "compiles and packages a versioned immutable artifact - a "
            "container image tagged by commit. Test stages run in "
            "parallel: unit tests, integration tests against ephemeral "
            "environments, security scans, license checks. Promotion copies "
            "the same artifact - never rebuilt - through staging to "
            "production, because rebuilding invites divergence. The "
            "deploy stage executes the chosen strategy: rolling updates "
            "respect surge budgets, blue-green flips the load balancer "
            "target group, canary shifts traffic weights stepwise while "
            "automated analysis watches error rates and rolls back on "
            "regression. Approvals gate production for regulated "
            "workloads; everything else flows automatically. Pipeline "
            "definitions live in the repository beside the code, so the "
            "delivery process itself is reviewed and versioned."
        ),
        "key_points": [
            "Build once, promote the same artifact through environments",
            "Sample lead time: 180 plus 240 plus 90 equals 510 seconds",
            "Canary: 10 percent of 50 pods means 5 pods on the new version",
            "Blue-green enables instant rollback; feature flags separate deploy from release",
            "DORA metrics measure pipeline performance honestly",
        ],
        "requirements": [
            "Immutable versioned artifacts, never rebuilt between environments",
            "Automated rollback on canary regression",
        ],
        "standards": [
            "DORA research program metrics",
            "SLSA framework for supply-chain security",
        ],
        "citations": [CIT_SRE],
    },
    {
        "key": "cost_optimization",
        "name": "Cloud Cost Optimization and FinOps",
        "group": "Operations",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "FinOps is the operating model that makes cloud spending "
            "visible, accountable, and efficient: finance, engineering, "
            "and product share one set of numbers and one set of "
            "decisions. The practice runs in three phases - inform, "
            "optimize, operate. Inform means tagging every resource, "
            "allocating every dollar to a team, and forecasting the "
            "trend. Optimize means acting on the findings: rightsizing "
            "over-provisioned machines, buying commitments for the steady "
            "baseline, moving cold data to archive tiers, deleting "
            "unattached volumes and idle addresses. The demo rightsizes a "
            "fleet: 20 virtual machines averaging 12 percent CPU "
            "consolidate to 4 machines at 60 percent, and at 146.00 "
            "dollars per machine per month the 16 retired machines save "
            "2,336.00 dollars every month - 28,032.00 per year. Operate "
            "means the loop never stops: budgets with alerts, anomaly "
            "detection on the daily spend, and architecture reviews that "
            "treat cost as a design constraint beside latency and "
            "availability. Unit economics - cost per transaction, per "
            "user, per gigabyte - is the metric that matters; a falling "
            "total bill with a rising unit cost is still a failure."
        ),
        "sig_lens": (
            "The Signature treasury counts in daylight. Twenty porters "
            "each carrying a twelfth of a load are dismissed, and four "
            "strong porters carry three-fifths each - the 16 released "
            "save 2,336.00 in coin every moon, 28,032.00 every year. The "
            "Signature treasurer tags every vessel, forecasts every "
            "tide, and buys the year grain at the harvest price - for a "
            "kingdom that cannot weigh its gold cannot rule its spending."
        ),
        "how_it_works": (
            "FinOps works through shared visibility and continuous "
            "rightsizing. Cost and usage reports flow into dashboards "
            "grouped by tag - team, service, environment - so each owner "
            "sees their spend daily. Rightsizing recommendations compare "
            "provisioned size against observed utilization over weeks and "
            "propose the smaller size; engineers accept or reject with "
            "one click. Commitment planners analyze the steady baseline "
            "and recommend one- and three-year purchases at the "
            "discount tiers. Anomaly detection learns the daily spend "
            "pattern and pages when a misconfigured job starts burning "
            "ten times normal. Showback reports charge each team their "
            "share; chargeback goes further and moves real budget. The "
            "cultural shift is the point: engineers see cost in the "
            "deploy pipeline, architects estimate before building, and "
            "finance forecasts from engineering plans instead of "
            "guessing."
        ),
        "key_points": [
            "FinOps phases: inform, optimize, operate - shared by finance and engineering",
            "Rightsizing 20 VMs at 12 percent to 4 at 60 percent saves 2,336.00 monthly",
            "Unit economics - cost per transaction - matters more than the total bill",
            "Commitments discount the steady baseline; spot serves the flexible",
            "Anomaly detection pages on abnormal daily spend",
        ],
        "requirements": [
            "Complete tagging coverage before any optimization claim",
            "Unit cost metrics per service from the first production month",
        ],
        "standards": [
            "FinOps Foundation framework and maturity model",
            "FOCUS billing data specification",
        ],
        "citations": [CIT_SRE],
    },
    {
        "key": "twelve_factor",
        "name": "Cloud-Native Design: The Twelve-Factor App",
        "group": "Architecture",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The Twelve-Factor App is a methodology for building "
            "software-as-a-service applications that run natively on the "
            "cloud: twelve practices that together make an application "
            "portable, scalable, and operable. The factors are: one "
            "codebase tracked in version control with many deploys; "
            "explicit dependency declaration; configuration stored in the "
            "environment; backing services treated as attached resources; "
            "strict separation of build, release, and run stages; "
            "stateless processes sharing nothing; port binding for "
            "service export; concurrency via the process model for "
            "horizontal scale; disposability with fast startup and graceful "
            "shutdown; dev-prod parity keeping environments similar; logs "
            "as event streams; and admin processes run as one-off tasks. "
            "The demo scores an application meeting 9 of the 12 factors: "
            "75.0 percent cloud-native, with the missing three - "
            "disposability, dev-prod parity, and admin processes - named "
            "as the remediation list. Each factor removes one classic "
            "source of it works on my machine: environment-stored config "
            "removes the checked-in secret, stateless processes remove the "
            "sticky session, disposability removes the fragile pet server."
        ),
        "sig_lens": (
            "The Signature code of the vessel-builder has twelve articles, "
            "and the wise builder keeps them all. One keel, one "
            "blueprint; no hidden provisions - the stores are declared at "
            "the dock; the vessel remembers nothing between voyages; it "
            "is born in heartbeats and dies gracefully at the word. The "
            "apprentice vessel keeps 9 of the 12 articles - 75.0 percent "
            "true - and the master names the three lacking that the "
            "vessel may be made whole."
        ),
        "how_it_works": (
            "Each factor works by removing hidden coupling. Environment "
            "configuration means the same artifact runs in dev, staging, "
            "and production with different injected values - no rebuilds, "
            "no secret files in the repository. Attached backing services "
            "mean the database is a URL that can point at a local "
            "container today and a managed service tomorrow. Stateless "
            "processes mean any instance can serve any request, so the "
            "load balancer and the autoscaler treat them as interchangeable "
            "and killing one loses nothing. Disposability means startup in "
            "seconds and shutdown that finishes in-flight work then exits, "
            "which is what makes rolling deploys and spot instances safe. "
            "Log streams mean the application never manages files - it "
            "writes events to stdout and the platform routes, aggregates, "
            "and retains them. Together the factors describe exactly the "
            "application shape that containers, orchestrators, and "
            "serverless platforms expect."
        ),
        "key_points": [
            "Twelve practices for portable, scalable, operable services",
            "Sample score: 9 of 12 factors met, 75.0 percent cloud-native",
            "Config in environment, backing services as attached resources",
            "Stateless processes enable interchangeable horizontal scaling",
            "Disposability makes rolling deploys and spot instances safe",
        ],
        "requirements": [
            "Twelve-factor review for every new service design",
            "Remediation list for each missing factor",
        ],
        "standards": [
            "The Twelve-Factor App methodology (Wiggins, 2011)",
            "CNCF cloud native definition alignment",
        ],
        "citations": [CIT_12F, CIT_K8S],
    },
    {
        "key": "multiregion_cap",
        "name": "Multi-Region Architecture and the CAP Theorem",
        "group": "Architecture",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Multi-region architecture spreads a system across geographic "
            "regions for disaster survival and global latency, and the CAP "
            "theorem governs what consistency it can promise. CAP states "
            "that a distributed data store can guarantee at most two of "
            "three: consistency - every read sees the latest write; "
            "availability - every request gets a response; partition "
            "tolerance - the system works despite network splits. Since "
            "partitions happen, the real choice is consistency versus "
            "availability during a split. The demo works the quorum math "
            "for 3 replicas: a quorum is the floor of 3 divided by 2 plus "
            "1 - 2 nodes. Writes to 2 of 3 and reads from 2 of 3 overlap "
            "on at least one node, giving strong consistency; with one "
            "node down, 2 survivors still form a quorum, so the system "
            "stays both consistent and available through a single failure. "
            "Active-passive designs keep one region serving with "
            "asynchronous replication to the standby; active-active serves "
            "from all regions with conflict resolution. DNS and anycast "
            "steer users to the healthy region, and the failover runbook "
            "is rehearsed, not improvised."
        ),
        "sig_lens": (
            "The Signature realm keeps chronicles in three distant "
            "cities, and the law of the three cities is stern: of "
            "truth, readiness, and endurance through severed roads, only "
            "two can be sworn at once. The council of 3 requires 2 voices "
            "to decree - and when one city falls silent, the 2 remaining "
            "still speak lawfully. The Signature king posts his heralds "
            "in every kingdom and rehearses the succession, for a crown "
            "passed in panic is a crown half lost."
        ),
        "how_it_works": (
            "Quorum replication works by overlapping majorities. With 3 "
            "replicas and quorum 2, every write reaches at least 2 nodes "
            "and every read consults at least 2 nodes; the overlap "
            "guarantees the read sees the write - strong consistency "
            "without a single master. Leader election picks the writer: "
            "nodes vote, the candidate with a quorum becomes leader, and "
            "leases expire so a partitioned leader steps down. "
            "Active-passive replication ships the write-ahead log "
            "asynchronously to the standby region - seconds of lag, "
            "minutes of failover. Active-active uses conflict-free data "
            "types or last-writer-wins with vector clocks where the "
            "business tolerates merges. Health checks per region feed the "
            "DNS failover: when a region fails its checks, traffic steers "
            "away within the DNS time-to-live. Data residency laws decide "
            "which regions may hold which data - architecture follows the "
            "law."
        ),
        "key_points": [
            "CAP: consistency, availability, partition tolerance - pick two",
            "Quorum for 3 replicas is 2 nodes; overlap guarantees strong consistency",
            "One node down still leaves a quorum - consistent and available",
            "Active-passive versus active-active replication strategies",
            "DNS failover steers users; residency law constrains placement",
        ],
        "requirements": [
            "Explicit consistency choice per dataset, documented",
            "Rehearsed regional failover runbook",
        ],
        "standards": [
            "CAP theorem (Brewer, 2000; Gilbert and Lynch, 2002)",
            "Data residency regulations per jurisdiction",
        ],
        "citations": [CIT_ISO, CIT_SRE],
    },
    {
        "key": "migration_6rs",
        "name": "Cloud Migration: The Six Rs",
        "group": "Architecture",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The six Rs classify every application in a cloud migration: "
            "rehost, replatform, repurchase, refactor, retain, and retire. "
            "Rehost - lift and shift - moves the virtual machine as-is for "
            "speed with no cloud benefit beyond the data center exit. "
            "Replatform - lift and reshape - moves with small optimizations "
            "like swapping a self-managed database for a managed one. "
            "Repurchase replaces with SaaS. Refactor - re-architect - "
            "rebuilds cloud-native for full elasticity at full cost. "
            "Retain keeps the application where it is for now, and retire "
            "decommissions what nobody needs. The demo classifies a "
            "portfolio of 120 applications: 60 rehost (50.0 percent), 30 "
            "replatform (25.0 percent), 12 refactor (10.0 percent), 8 "
            "repurchase (6.7 percent), 6 retain (5.0 percent), 4 retire "
            "(3.3 percent) - the classic shape, with most workloads moving "
            "fast and a few earning deep investment. Migration runs in "
            "waves by dependency: discover and map, assess and classify, "
            "pilot with low-risk workloads, then migrate factories of "
            "similar applications with runbooks and rollback plans."
        ),
        "sig_lens": (
            "The Signature moving of the kingdom sorts every household by "
            "its true road. Sixty houses are lifted whole and set down "
            "across the river - 50.0 percent. Thirty are lifted and "
            "mended in the moving - 25.0 percent. Twelve are torn down to "
            "the foundation and raised anew - 10.0 percent. Eight are "
            "traded for finer houses already built, six bide where they "
            "stand, and four are released to the winds - 3.3 percent freed "
            "forever. The Signature marshal moves in waves, the easy roads "
            "first, and no house travels without its map home."
        ),
        "how_it_works": (
            "Migration works as a factory. Discovery agents inventory every "
            "server, database, and dependency, building the graph of what "
            "talks to what. Assessment scores each application on cloud "
            "readiness, business value, and risk, producing the R "
            "classification and the wave order - independent low-risk "
            "workloads first, tangled core systems later. Each wave gets a "
            "runbook: replicate data, cut over DNS or connection strings "
            "in a maintenance window, validate with smoke tests, keep the "
            "rollback path warm for 48 hours. Replatforming swaps "
            "components during the move: the database becomes managed, the "
            "file share becomes object storage, the hardware load balancer "
            "becomes the cloud one. Landing zones - pre-built accounts, "
            "networks, identity, and guardrails - receive every wave, so "
            "migrated workloads land in governed territory instead of "
            "wilderness."
        ),
        "key_points": [
            "Six Rs: rehost, replatform, repurchase, refactor, retain, retire",
            "120 apps: 60 rehost, 30 replatform, 12 refactor, 8 repurchase, 6 retain, 4 retire",
            "Migrate in waves ordered by dependency and risk",
            "Landing zones give every wave governed territory to land in",
            "Keep the rollback path warm for 48 hours after each cutover",
        ],
        "requirements": [
            "Complete dependency map before the first wave",
            "Landing zone with identity, network, and guardrails ready",
        ],
        "standards": [
            "AWS migration methodology and CAF perspectives",
            "ISO/IEC 27001 for the target environment",
        ],
        "citations": [CIT_SRE, CIT_WA],
    },
    {
        "key": "service_mesh",
        "name": "Service Mesh and Advanced Traffic Control",
        "group": "Networking",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A service mesh moves networking concerns - encryption, "
            "routing, retries, observability - out of application code "
            "into a dedicated infrastructure layer of sidecar proxies. "
            "Each service instance gets a sidecar proxy that intercepts "
            "its traffic; a control plane programs all sidecars with "
            "routing rules, security policy, and telemetry config. Mutual "
            "TLS between sidecars gives every call encryption and "
            "identity without application changes. Traffic control goes "
            "far beyond round robin: weighted splits for canary releases, "
            "header-based routing to send test users to the new version, "
            "fault injection that adds latency to prove resilience, and "
            "circuit breakers that stop calling a failing service before "
            "it cascades. The demo prices reliability through retries: "
            "with a per-try success probability of 0.9, one try plus 3 "
            "retries gives 1 minus 0.1 to the 4th - 0.9999 success, four "
            "nines from a nine-tenths service. The cost is latency - about "
            "2 milliseconds per hop on a 50 millisecond base, 4 percent "
            "overhead - and operational complexity, which is why meshes "
            "belong on large microservice fleets, not three-service "
            "systems."
        ),
        "sig_lens": (
            "The Signature courier corps rides beside every messenger, "
            "unseen. Each vessel sails with its sworn escort who seals "
            "every letter, chooses every road, counts every retry, and "
            "reports every delay to the admirals chart - the application "
            "captains need know nothing of roads. Four castings of a "
            "nine-tenths spell yield 0.9999 certainty. The escort costs 2 "
            "heartbeats on a 50-beat voyage - 4 percent - a fair wage for "
            "a guard that never sleeps."
        ),
        "how_it_works": (
            "The mesh works by interception. The sidecar proxy - typically "
            "Envoy - captures outbound calls through iptables rules and "
            "applies the route table from the control plane: match headers "
            "and paths, split by weight, apply retry budgets with "
            "backoff, enforce timeouts. Inbound, it terminates mutual TLS, "
            "verifies the caller certificate against policy, and forwards "
            "to the local application. Telemetry is automatic: every hop "
            "emits latency, error, and trace spans, giving the golden "
            "signals per service pair without code changes. Circuit "
            "breakers track consecutive failures and short-circuit calls "
            "for a cooldown, shedding load before the failure cascades. "
            "Progressive delivery controllers read the same telemetry to "
            "automate canary analysis - promoting or rolling back the new "
            "version by the numbers."
        ),
        "key_points": [
            "Sidecar proxies handle encryption, routing, retries, telemetry",
            "Mutual TLS gives identity and encryption with no code changes",
            "Retries turn 0.9 per-try success into 0.9999 over 4 attempts",
            "Latency cost about 2 ms per hop, 4 percent on a 50 ms base",
            "Right for large microservice fleets; overkill for tiny systems",
        ],
        "requirements": [
            "Retry budgets and timeouts set per route, not left at defaults",
            "mTLS policy in strict mode once all workloads are meshed",
        ],
        "standards": [
            "Envoy proxy as the data plane standard",
            "SPIFFE for workload identity",
        ],
        "citations": [CIT_K8S, CIT_SRE],
    },
    {
        "key": "confidential_computing",
        "name": "Confidential Computing and Key Management",
        "group": "Security",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Confidential computing protects data while it is being used - "
            "the third state beside at-rest and in-transit - by running "
            "workloads inside hardware-encrypted memory enclaves the cloud "
            "provider itself cannot read. Processor extensions encrypt "
            "memory with keys fused into the chip, and remote attestation "
            "lets a customer verify cryptographically that the expected "
            "code is running in a genuine enclave before sending secrets. "
            "Key management is the companion discipline: envelope "
            "encryption wraps each data key with a master key, so "
            "rotating the master re-wraps small key blobs instead of "
            "re-encrypting petabytes. The demo measures the AES-256 key "
            "space: 2 to the 256th power is about 1.158 times 10 to the "
            "77th keys, and at a trillion guesses per second brute force "
            "would need 3.67 times 10 to the 57th years - longer than the "
            "universe has existed, by 47 orders of magnitude. Hardware "
            "security modules guard master keys in tamper-resistant "
            "hardware with audit trails on every use. Together they answer "
            "the hardest compliance question: how do you process regulated "
            "data on hardware you do not own."
        ),
        "sig_lens": (
            "The Signature seal guards the thought itself, not only the "
            "letter and the road. The enclave is a mind of crystal: the "
            "work happens inside, encrypted even from the keeper of the "
            "hall, and the attestation proves the crystal is true before "
            "a single secret enters. The master key sleeps in the "
            "ironbound coffer - the hardware module - and each lesser key "
            "is wrapped in its power. A trillion thieves guessing for "
            "3.67 times 10 to the 57th years would not open one "
            "Signature seal."
        ),
        "how_it_works": (
            "An enclave works through memory encryption at the processor: "
            "data leaving the CPU package is encrypted with an ephemeral "
            "key, so hypervisor, host operating system, and anyone with "
            "physical memory access see only ciphertext. At launch, the "
            "processor measures the loaded code into a signed attestation "
            "report; the customer verifies the signature chain to the "
            "chip manufacturer and the measurement against the expected "
            "build before provisioning secrets into the enclave over a "
            "secure channel. Envelope encryption works in layers: a data "
            "encryption key encrypts the object, a key encryption key "
            "wraps the data key, and only the wrapped blob is stored "
            "beside the data. Rotation replaces the wrapping without "
            "touching the data. HSM-backed master keys never leave the "
            "hardware boundary - cryptographic operations happen inside, "
            "and every operation is logged."
        ),
        "key_points": [
            "Enclaves encrypt data in use; even the provider cannot read it",
            "Remote attestation verifies code and hardware before secrets are sent",
            "Envelope encryption makes key rotation cheap",
            "AES-256 brute force at 1 trillion guesses per second: 3.67e57 years",
            "HSMs guard master keys in tamper-resistant hardware",
        ],
        "requirements": [
            "Attestation verification in the deployment pipeline",
            "HSM-backed keys for regulated workloads",
        ],
        "standards": [
            "NIST SP 800-57 key management guidance",
            "Confidential Computing Consortium terminology",
        ],
        "citations": [CIT_NIST],
    },
    {
        "key": "well_architected",
        "name": "The Well-Architected Framework and SRE",
        "group": "Architecture",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The Well-Architected Framework distills operating at scale "
            "into six pillars - operational excellence, security, "
            "reliability, performance efficiency, cost optimization, and "
            "sustainability - each with design principles and review "
            "questions. Site Reliability Engineering supplies the "
            "operating system: treat operations as a software problem, "
            "automate the toil, and manage risk with error budgets. The "
            "demo runs a scored review: operational excellence 82, "
            "security 91, reliability 78, performance efficiency 85, cost "
            "optimization 74, sustainability 88 - a weighted average of "
            "83.0, with cost optimization the pillar to remediate first. "
            "The SRE practices behind the score are concrete: service-"
            "level objectives with burn-rate alerting, blameless "
            "postmortems that fix systems instead of people, capacity "
            "planning from measured demand, and change management through "
            "progressive delivery. Reviews repeat on a cadence - "
            "quarterly for production systems - because architecture "
            "drifts: the 83.0 of today is the technical debt of next "
            "year if nobody re-scores."
        ),
        "sig_lens": (
            "The Signature master-builder judges every fortress by six "
            "pillars, and the reckoning is writ in numbers: craft 82, "
            "warding 91, endurance 78, swiftness 85, thrift 74, harmony "
            "with the land 88 - the mean 83.0, and thrift the pillar "
            "calling loudest for mending. The Signature engineers treat "
            "the night watch as a craft of its own: they count the "
            "allowed darkness, write the chronicle of every fall without "
            "blame, and raise the fallen stronger than before."
        ),
        "how_it_works": (
            "A Well-Architected review works as a structured interview: "
            "for each pillar, the team answers whether the design "
            "principles hold - are runbooks automated, is least privilege "
            "enforced, is failure tested, is the right instance family "
            "chosen, is spend allocated, is utilization efficient - and "
            "scores honestly. High-risk findings become remediation items "
            "with owners and dates. SRE implements the reliability pillar "
            "daily: error budgets quantify how much risk the quarter may "
            "spend, and feature launches pause when the budget burns; "
            "toil - manual repetitive operational work - is measured and "
            "driven toward zero by automation; postmortems within days of "
            "every significant incident produce action items, never "
            "punishment. The framework and SRE meet in the review "
            "cadence: score, remediate, re-score, each cycle lifting the "
            "weakest pillar first."
        ),
        "key_points": [
            "Six pillars: operations, security, reliability, performance, cost, sustainability",
            "Sample review scores average 83.0; cost optimization remediated first",
            "SRE: error budgets, toil elimination, blameless postmortems",
            "Change management through progressive delivery",
            "Re-score quarterly - architecture drifts",
        ],
        "requirements": [
            "SLOs and error budgets on every production service",
            "Quarterly architecture reviews with tracked remediation",
        ],
        "standards": [
            "AWS Well-Architected Framework six pillars",
            "Google SRE book practices",
        ],
        "citations": [CIT_WA, CIT_SRE],
    },
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks), "entries not in ladder order"
assert all(1 <= r <= 10 for r in _ranks), "ladder_rank out of range"
