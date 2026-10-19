#!/usr/bin/env python3
"""Entries for the Telecom Operations database pair (5,000-target program).

Dedupe gate: all 68 titles checked against the WHOLE system with
code/dedupe_gate.py BEFORE writing. ID prefixes JAH-TLCO- (public) and
JAH-TLCOS- (signature) verified free: zero hits in manifest id_prefix values
(exact + substring) and zero hits in shard record IDs.

34 records per edition, ladder-ordered 1-34 (Foundations 1-12 / Compounded
13-23 / Advanced 24-34).
"""


def R(t, tier, rank, desc, how, kp, req, std, cit, dk, data):
    return {'t': t, 'tier': tier, 'rank': rank, 'desc': desc, 'how': how,
            'kp': kp, 'req': req, 'std': std, 'cit': cit, 'dk': dk, 'data': data}


PUB = [
R("What Telecom Networks Are — Industry Overview", "Foundations", 1,
  "Telecom networks are the systems that carry voice, text, and data between people and machines across towns, countries, and oceans. "
  "The industry spans mobile operators, fixed broadband providers, backbone carriers, tower companies, and equipment makers, all working over shared standards. "
  "Every call, message, and page load rides the same layered machinery: access networks that reach the customer, transport networks that haul traffic, and core systems that route, bill, and manage it all.",
  "A customer's device connects through an access network - a cell tower, a fiber line, a Wi-Fi hotspot - which hands traffic to aggregation and transport networks built on fiber and routers. "
  "Core systems authenticate the subscriber, route the session to its destination, measure usage for billing, and monitor quality throughout. "
  "Operators plan capacity ahead of demand, maintain the physical plant of towers and cables, and coordinate with other networks so a customer of one carrier can reach a customer of any other.",
  ["Access, transport, and core: the three layers of every telecom network.",
   "Standards let any operator's customer reach any other's.",
   "Operators plan capacity ahead of demand and maintain towers, fiber, and power.",
   "Billing, authentication, and quality monitoring run in the core systems."],
  ["A clear map of which networks serve which customers.",
   "Spectrum or right-of-way access for the access layer.",
   "Interconnection agreements with other carriers.",
   "Operations staff for build, maintenance, and customer care."],
  ["Emergency calling must work even where commercial service is limited.",
   "Networks engineered for high availability with backup power and paths.",
   "Customer data protected under communications privacy rules."],
  ["ITU-T recommendations on telecommunication network architecture (public standards).",
   "Telecom industry overview literature (public publications)."],
  "dbm", {"watts": 20.0}),

R("The Telephone Numbering Plan", "Foundations", 2,
  "The telephone numbering plan is the global addressing scheme that lets any phone reach any other phone: country codes, area codes, and subscriber numbers in a strict hierarchy. "
  "The ITU's E.164 standard defines the format - a plus sign, country code, and national number, at most 15 digits - so switches worldwide parse every number the same way. "
  "Behind the digits sit routing tables that translate each number into the network and switch that serves it.",
  "When a call is placed, the originating switch reads the country code to pick the international gateway, then the area or network code to pick the route, then delivers to the terminating switch that owns the subscriber number. "
  "Number portability databases let a kept number point to a new carrier, and emergency numbers like 911 are routed by special tables to the nearest dispatch center. "
  "Regulators assign number blocks to carriers and reclaim unused ones so the finite space is not wasted.",
  ["E.164 defines the worldwide format: plus, country code, national number, max 15 digits.",
   "Switches route hierarchically: country, then area or network, then subscriber.",
   "Portability databases let numbers move between carriers.",
   "Emergency numbers route to the nearest dispatch center by special tables."],
  ["Number blocks assigned by the national regulator.",
   "Routing tables updated for every assigned and ported block.",
   "Emergency routing tested end to end."],
  ["Numbers assigned per the national numbering plan, no squatting on unassigned ranges.",
   "Portability requests honored within the mandated time.",
   "Emergency calls never blocked for billing reasons."],
  ["ITU-T E.164 on the international public telecommunication numbering plan (public standard).",
   "National numbering plan administration rules (public regulations)."],
  "subnet", {"prefix": 24}),

R("Copper Lines and DSL Broadband", "Foundations", 3,
  "Copper telephone lines are the twisted-pair wires that carried voice for a century, and DSL - digital subscriber line - is the technology that squeezes broadband data through those same wires. "
  "DSL works because voice uses only the lowest frequencies; the higher frequencies, unused by calls, carry data. "
  "Speed falls with distance from the exchange, which is why DSL is fastest near the central office and fades at the edge of town.",
  "A DSL modem at the customer premises and a DSLAM at the exchange agree on which frequency tones are usable on the line, then modulate data across them. "
  "Filters split voice from data so phones keep working during downloads, and the line is provisioned with a speed profile matched to its measured quality. "
  "Technicians test loop length, noise, and attenuation before promising a speed, because copper's limits are physics, not marketing.",
  ["Voice uses low frequencies; DSL data rides the higher, unused ones.",
   "Speed falls with distance - loop length is the fundamental limit.",
   "Filters keep voice and data from interfering.",
   "Lines are qualified by measurement before a speed is promised."],
  ["Copper loop from exchange to premises, tested for length and noise.",
   "DSLAM port at the exchange and modem at the customer.",
   "Filters on every voice device sharing the line."],
  ["Advertised speeds achievable on the qualified line, not theoretical maxima.",
   "Voice service must survive data equipment faults.",
   "Line safety per electrical codes for outside plant."],
  ["ITU-T G.992.x DSL standards family (public standards).",
   "Broadband measurement and advertising guidance (public regulations)."],
  "dbm", {"watts": 0.5}),

R("Cable Broadband and DOCSIS", "Foundations", 4,
  "Cable broadband delivers internet over the same coaxial networks built for television, using the DOCSIS standard to share the cable's spectrum between TV channels and data. "
  "The coaxial plant has enormous downstream capacity, which is why cable was the first widely available fast broadband in many countries. "
  "The shared nature of the node means neighbors share capacity, so speeds vary with how many are online at once.",
  "At the headend, a CMTS schedules data into downstream channels bonded together for each modem, while modems transmit upstream in scheduled time slots. "
  "DOCSIS versions raised speeds by bonding more channels and moving to OFDM; full-duplex and extended-spectrum variants push further. "
  "The operator monitors node utilization and splits congested nodes - dividing the subscribers across more capacity - to protect evening speeds.",
  ["DOCSIS shares cable spectrum between TV and data channels.",
   "Channel bonding multiplies modem speed across bonded channels.",
   "Nodes are shared: congestion rises when many neighbors are online.",
   "Node splits add capacity where utilization runs hot."],
  ["Coaxial plant from headend through nodes to the home.",
   "CMTS at the headend and DOCSIS modems at customers.",
   "Node utilization monitoring and a split program."],
  ["Speeds advertised as typical, with congestion behavior disclosed.",
   "Upstream power and signal levels kept within plant specs.",
   "Plant leakage controlled per signal-ingress rules."],
  ["CableLabs DOCSIS specifications (public standards).",
   "Broadband advertising and measurement guidance (public regulations)."],
  "shannon", {"bw_mhz": 192.0, "snr_db": 36.0}),

R("Fiber Optics and GPON", "Foundations", 5,
  "Fiber optics carry data as pulses of light through hair-thin glass strands, and GPON - gigabit passive optical network - is the standard that shares one fiber among many homes. "
  "Light suffers far less loss than electricity in copper, so fiber runs kilometers without regeneration and delivers symmetric-feeling gigabit speeds. "
  "The passive part matters: the splitter in the field needs no power, which makes the outside plant simple and reliable.",
  "At the central office, an OLT transmits downstream to all homes on the fiber and receives upstream bursts in scheduled time slots; a passive splitter divides the light among up to 64 or 128 homes. "
  "Each home's ONT converts light back to electrical Ethernet and voice ports, and ranging plus encryption keep each home's traffic separate. "
  "Splicing, connector cleanliness, and optical budgets - the allowed light loss end to end - decide whether the link works.",
  ["Data as light: huge capacity, tiny loss, kilometers without regeneration.",
   "GPON shares one fiber among many homes through a passive splitter.",
   "The OLT schedules upstream bursts; the ONT serves the home.",
   "Optical budget - total allowed loss - decides if the link works."],
  ["Fiber from office through splitters to each premises.",
   "OLT ports, splitters, and ONTs, with spares.",
   "Splicing gear and the skill to keep connectors clean."],
  ["Optical power within safe limits for eyes and equipment.",
   "Splice and connector loss within the budgeted allowance.",
   "Fiber locates marked before any digging near the plant."],
  ["ITU-T G.984 GPON standards family (public standards).",
   "Fiber installation and safety practices (public industry guidance)."],
  "fiber", {"dist_km": 12.5, "atten_dbkm": 0.35}),

R("Mobile Networks — Cells and Towers", "Foundations", 6,
  "Mobile networks divide the land into cells, each served by a tower or rooftop site with radios covering its patch of ground. "
  "As a phone moves, the network hands it from cell to cell without dropping the call - the handover that makes mobility feel seamless. "
  "Cells are sized by demand: big rural cells cover kilometers, dense urban cells shrink to city blocks.",
  "Each site has antennas aimed in sectors, radios feeding them, and backhaul carrying traffic to the core; the phone camps on the strongest cell and reports neighbors as it moves. "
  "The controller or the phone-plus-network logic decides when to hand over, weighing signal strength, load, and quality. "
  "Planners place sites on a grid tuned by drive tests and models, filling coverage holes and adding capacity where crowds gather.",
  ["The service area is tiled into cells, each served by a site.",
   "Handover moves the phone between cells without dropping the session.",
   "Cell size follows demand: wide rural, tiny dense-urban.",
   "Sites need antennas, radios, power, and backhaul together."],
  ["Site locations with power, backhaul, and structural capacity.",
   "Spectrum licenses for the bands the radios will use.",
   "Planning tools: propagation models and measurement drives."],
  ["Tower structural and RF-exposure safety per applicable rules.",
   "Handover must not drop emergency calls.",
   "Site backup power for outages."],
  ["3GPP technical specifications for radio access (public standards).",
   "FCC/regulatory RF exposure and tower rules (public regulations)."],
  "cell", {"radius_km": 2.5, "region_km2": 400.0}),

R("SIM Cards and Subscriber Identity", "Foundations", 7,
  "The SIM card is the subscriber's identity token: a tiny secure chip holding the IMSI - the network's name for the subscriber - and the secret key that proves it. "
  "When the phone attaches, the network challenges the SIM with a random number; only the true key can compute the right answer. "
  "That challenge-response is what keeps someone else from impersonating the subscriber and billing calls to them.",
  "The operator personalizes each SIM with its IMSI and secret, stores the same secret in the authentication center, and issues the card with the subscriber's plan profile. "
  "At attach, the network sends a random challenge, the SIM computes a response with its key, and matching responses authenticate the session and derive encryption keys. "
  "eSIM moves the same function into embedded hardware provisioned over the air, so profiles can be downloaded instead of physically swapped.",
  ["The SIM holds the IMSI and a secret key no one else knows.",
   "Challenge-response authentication defeats impersonation.",
   "The network's authentication center holds the matching secrets.",
   "eSIM provisions the same identity over the air, no physical swap."],
  ["SIM personalization and secure key storage.",
   "An authentication center holding subscriber secrets.",
   "eSIM provisioning servers where offered."],
  ["Subscriber secrets never leave secure hardware in the clear.",
   "SIM swaps require identity verification to defeat fraud.",
   "Lawful intercept capabilities per applicable law, with proper authorization."],
  ["3GPP authentication specifications (AKA) (public standards).",
   "GSMA eSIM provisioning specifications (public standards)."],
  "subnet", {"prefix": 28}),

R("Voice Calls — From Dial to Ring", "Foundations", 8,
  "A voice call is a real-time session stitched across networks: the dialed digits are analyzed, a path is found, the far phone is alerted, and a two-way audio channel opens. "
  "Modern calls are packets - voice digitized, compressed, and sent as IP - but the setup logic of finding and ringing the destination is as old as telephony. "
  "Quality is judged by delay, jitter, and loss: too much of any and conversation breaks down.",
  "The originating switch or softswitch parses the digits, queries routing and portability data, and signals forward with SIP or SS7 toward the destination. "
  "The terminating side pages or rings the handset; when answered, media negotiates a codec and the two-way stream begins, with echo cancellers and jitter buffers smoothing it. "
  "Billing records capture who called whom for how long, and the session tears down cleanly on hangup.",
  ["Setup finds and rings the destination; media carries the conversation.",
   "Voice is packets now: digitized, compressed, streamed as IP.",
   "Delay, jitter, and loss are the three quality enemies.",
   "Signaling (SIP/SS7) and media (RTP) are separate planes."],
  ["Switches or softswitches with routing and portability data.",
   "Media gateways and session border controllers at network edges.",
   "Clock synchronization good enough for voice quality."],
  ["Emergency calls routed first and never blocked for billing.",
   "Call setup times within regulatory expectations.",
   "Calling-line identity handled per privacy rules."],
  ["IETF SIP standards (RFC 3261 family) (public standards).",
   "ITU-T voice quality recommendations (public standards)."],
  "erlang", {"channels": 30, "traffic_erl": 22.0}),

R("SMS and Text Messaging", "Foundations", 9,
  "SMS - the short message service - sends 160-character texts over the mobile signaling network, the same channels phones use to set up calls. "
  "It succeeded because it works on every phone, needs no data plan, and stores-and-forwards: the message waits if the phone is off and delivers when it returns. "
  "Billions of people still rely on it daily, and businesses use it for alerts, codes, and notifications.",
  "The sender's message goes to a message center (SMSC), which queries the subscriber database for the destination's location and forwards the message to the serving switch. "
  "If the phone is unreachable, the center holds the message and retries; delivery reports confirm arrival back to the sender. "
  "Interconnection agreements carry messages between carriers, and spam filters plus sender registration keep the channel trustworthy.",
  ["160 characters over signaling channels - works on every phone.",
   "Store-and-forward: messages wait for unreachable phones.",
   "The message center routes via subscriber location data.",
   "Business messaging needs registered senders and consent."],
  ["Message centers with interconnection to other carriers.",
   "Subscriber database access for routing.",
   "Spam and fraud filtering on the messaging path."],
  ["Emergency alerts delivered with priority over commercial traffic.",
   "Business texts only to consenting recipients per applicable rules.",
   "Message content protected in transit and at rest."],
  ["3GPP SMS specifications (public standards).",
   "CTIA and regulatory messaging-consent guidance (public rules)."],
  "billing", {"units": 3500.0, "rate": 0.02}),

R("Wi-Fi Fundamentals", "Foundations", 10,
  "Wi-Fi is the wireless LAN that connects phones, laptops, and gadgets to a local network over unlicensed radio spectrum. "
  "It trades the licensed, managed world of cellular for simplicity: anyone can set up an access point, and devices roam between them freely. "
  "The cost of that freedom is contention - every device nearby shares the same airtime, so crowded rooms slow everyone down.",
  "An access point beacons its network name; devices associate, authenticate with WPA2 or WPA3, and get an IP address. "
  "Data is framed with CSMA/CA - listen before talking, back off on collision - across 20/40/80/160 MHz channels in the 2.4, 5, and 6 GHz bands. "
  "Good deployments survey the space, place access points for coverage and capacity, pick non-overlapping channels, and size backhaul to match the airtime offered.",
  ["Unlicensed spectrum: simple to deploy, shared with everyone nearby.",
   "WPA2/WPA3 authentication and encryption protect the air.",
   "CSMA/CA shares airtime - crowding slows all devices.",
   "Survey, place, channel-plan, and backhaul-size every deployment."],
  ["Access points sized to the device count and traffic.",
   "Backhaul from each AP to the wired network.",
   "A survey or at least a careful channel plan."],
  ["Transmit power within unlicensed-band limits.",
   "Guest networks isolated from internal systems.",
   "Default passwords changed before service."],
  ["IEEE 802.11 Wi-Fi standards family (public standards).",
   "Wi-Fi Alliance WPA3 security guidance (public guidance)."],
  "shannon", {"bw_mhz": 80.0, "snr_db": 25.0}),

R("IP Addresses and the Internet", "Foundations", 11,
  "IP addresses are the internet's numbering plan: every device online gets one, and routers forward packets by reading the destination address. "
  "IPv4's 32-bit addresses ran out, so IPv6's 128-bit space is the long-term answer, with NAT letting many devices share few IPv4 addresses meanwhile. "
  "DNS translates human names into these numbers, so people type words while packets carry digits.",
  "ISPs receive address blocks from regional registries and assign them to customers statically or via DHCP; routers exchange reachability with BGP and forward each packet toward its destination. "
  "NAT at the customer edge maps many private addresses to one public address, conserving IPv4 at the cost of end-to-end transparency. "
  "IPv6 restores that transparency with effectively unlimited addresses, deployed alongside IPv4 in dual-stack networks.",
  ["IP addresses route packets; DNS maps names to addresses.",
   "IPv4 exhausted - NAT conserves it, IPv6 replaces it.",
   "Registries allocate blocks; ISPs assign them to customers.",
   "BGP spreads reachability; routers forward hop by hop."],
  ["Address blocks from the regional registry.",
   "DHCP and DNS infrastructure for customers.",
   "A dual-stack plan toward IPv6."],
  ["No hijacking of address space - announce only what is assigned.",
   "Customer DNS queries handled privately.",
   "Abuse contacts published and responsive."],
  ["IETF IPv4/IPv6 and DNS standards (RFC series) (public standards).",
   "Regional internet registry allocation policies (public policies)."],
  "subnet", {"prefix": 26}),

R("Telecom Math I — Decibels and Signal Power", "Foundations", 12,
  "Telecom math speaks in decibels: the logarithmic unit that turns multiplying gains and losses into adding and subtracting. "
  "A decibel is ten times the log of a power ratio; dBm is decibels relative to one milliwatt, the absolute unit for signal levels. "
  "Fluency here is non-negotiable: link budgets, the arithmetic of every radio and fiber path, are just decibel addition.",
  "Power in dBm equals 10*log10(power in milliwatts): 1 mW is 0 dBm, 100 mW is 20 dBm, and halving power drops 3 dB. "
  "Gains and losses in dB add directly: transmit 20 dBm, lose 110 dB in the path, arrive at -90 dBm. "
  "Every link budget in telecom - radio, fiber, or copper - is this same addition done carefully end to end.",
  ["dB is relative (a ratio); dBm is absolute (relative to 1 mW).",
   "In decibels, gains and losses add instead of multiply.",
   "3 dB is a doubling; 10 dB is ten times.",
   "Link budgets are decibel addition end to end."],
  ["Signal levels stated in dBm at every measurement point.",
   "A link-budget sheet for every designed path.",
   "Calibrated measurement or trusted specifications."],
  ["Computed levels checked against equipment limits.",
   "Safety margins kept above the minimum workable signal.",
   "Units labeled - dB and dBm never mixed without conversion."],
  ["Standard telecommunications transmission engineering references (public publications).",
   "Equipment vendor link-budget application notes (public documents)."],
  "dbm", {"watts": 2.0}),
]

PUB += [
R("4G LTE Networks", "Compounded", 13,
  "4G LTE is the all-IP mobile standard that made the smartphone era's data speeds routine: tens of megabits to a handset over OFDMA radio. "
  "Its flat architecture - base stations talking directly to the core - cut latency and cost versus older hierarchies. "
  "LTE's real legacy is the foundation it laid: the same sites, fiber, and core concepts carry 5G today.",
  "The eNodeB base station schedules radio resources to phones every millisecond, adapting modulation to each phone's signal quality. "
  "The evolved packet core - MME for signaling, SGW and PGW for user data - authenticates, routes, and bills the session, while IMS carries voice as VoLTE. "
  "Carrier aggregation bonds multiple spectrum bands for one user, and MIMO multiplies throughput with multiple antennas.",
  ["All-IP: voice, data, and signaling as packets on one network.",
   "OFDMA plus per-millisecond scheduling adapts to each phone.",
   "Carrier aggregation and MIMO multiply throughput.",
   "The flat eNodeB-to-core design cut latency and cost."],
  ["LTE spectrum licenses and eNodeB sites with backhaul.",
   "An evolved packet core sized to the subscriber base.",
   "IMS for VoLTE voice service."],
  ["Emergency calling and location accuracy per regulation.",
   "Handover success rates monitored against targets.",
   "Core redundancy so no single failure drops the network."],
  ["3GPP LTE specifications (Releases 8+) (public standards).",
   "Regulatory 4G coverage and quality obligations (public regulations)."],
  "shannon", {"bw_mhz": 20.0, "snr_db": 20.0}),

R("5G Networks and Network Slicing", "Compounded", 14,
  "5G is the mobile generation built for three jobs at once: faster phones, massive sensor fleets, and ultra-reliable low-latency control. "
  "Its new radio reaches into millimeter-wave spectrum for huge capacity, while network slicing carves one physical network into virtual ones tuned per use case. "
  "A slice for remote surgery and a slice for streaming video share the hardware but never each other's performance.",
  "The gNodeB radios connect to a cloud-native 5G core of microservices, with user-plane functions pushed to the edge for low latency. "
  "Slices are defined by throughput, latency, and reliability targets and orchestrated end to end across radio, transport, and core. "
  "Massive MIMO and beamforming aim capacity precisely where users are, instead of spraying it in all directions.",
  ["Three jobs: enhanced broadband, massive IoT, ultra-reliable low latency.",
   "Network slicing: virtual networks with guaranteed traits on shared hardware.",
   "Cloud-native core with edge user-plane for low latency.",
   "Massive MIMO and beamforming aim capacity at users."],
  ["5G spectrum across low, mid, and high bands.",
   "Cloud infrastructure for the 5G core and edge sites.",
   "Orchestration for slice lifecycle management."],
  ["Slice isolation verified - one slice's surge must not starve another's guarantee.",
   "Emergency services access on every slice.",
   "RF exposure compliance in new bands."],
  ["3GPP 5G NR and core specifications (Releases 15+) (public standards).",
   "Regulatory 5G spectrum auction and deployment rules (public regulations)."],
  "shannon", {"bw_mhz": 100.0, "snr_db": 22.0}),

R("The Mobile Core Network", "Compounded", 15,
  "The mobile core is the network's brain: it authenticates subscribers, tracks their location, routes their sessions, applies policy, and meters usage for billing. "
  "Radios get the glory, but the core decides who may connect, where their traffic goes, and what it costs. "
  "Modern cores are software on cloud hardware, scaling capacity by adding servers instead of swapping boxes.",
  "On attach, the core authenticates the SIM, downloads the subscriber profile, and registers the phone's location area. "
  "Session setup creates bearers with QoS profiles; the policy function gates speed and services per plan, and charging functions meter the bytes and minutes. "
  "Mobility management follows the phone across cells and technologies, keeping the IP session alive through handovers.",
  ["Authentication, location tracking, routing, policy, charging: the core's five jobs.",
   "Subscriber profiles drive what each user may do and at what speed.",
   "Cloud-native cores scale by adding servers, not swapping boxes.",
   "Mobility management keeps sessions alive across cells."],
  ["Core software dimensioned for subscribers and busy-hour signaling.",
   "Subscriber database with profiles and authentication data.",
   "Interconnection to radio networks, internet, and other carriers."],
  ["Subscriber data encrypted and access-logged.",
   "Core redundancy across sites for disaster survival.",
   "Lawful intercept per applicable law with proper authorization."],
  ["3GPP core network specifications (public standards).",
   "Data-protection rules for subscriber information (public regulations)."],
  "erlang", {"channels": 100, "traffic_erl": 85.0}),

R("Radio Access Networks (RAN)", "Compounded", 16,
  "The RAN - radio access network - is everything between the phone and the core: antennas, radios, baseband processing, and the protocols that schedule the airwaves. "
  "It is the most expensive part of a mobile network to build and the hardest to get right, because radio is shared, variable, and fiercely local. "
  "Open RAN is reshaping it: standardized interfaces letting operators mix radios from one vendor with software from another.",
  "Base stations divide spectrum into resource blocks scheduled every millisecond, adapting modulation and coding to each user's channel quality. "
  "Centralized and virtualized RAN pools baseband processing in data centers, coordinating neighboring cells to cut interference. "
  "Planners tune antenna tilts, power, and neighbor lists from measurements, because a well-tuned RAN carries far more than a careless one on the same hardware.",
  ["The RAN is the costliest, hardest part: shared, variable, local radio.",
   "Per-millisecond scheduling adapts modulation to each user's channel.",
   "Centralized/virtualized RAN coordinates cells to cut interference.",
   "Open RAN standardizes interfaces for multi-vendor mixing."],
  ["Towers, antennas, radios, and baseband capacity per traffic plan.",
   "Fiber or microwave backhaul from every site.",
   "Planning and optimization tools with drive-test data."],
  ["Emission limits and exposure compliance at every site.",
   "Neighbor lists and handover tuning verified after changes.",
   "Backup power keeping sites alive through outages."],
  ["3GPP RAN specifications and O-RAN Alliance interfaces (public standards).",
   "Regulatory emission and siting rules (public regulations)."],
  "link", {"tx_dbm": 43.0, "gain_db": 18.0, "loss_db": 128.0, "sens_dbm": -100.0}),

R("Backhaul and Transport", "Compounded", 17,
  "Backhaul is the network behind the towers: the links carrying traffic from each cell site to the core. "
  "A site with brilliant radios and starved backhaul is a sports car with a blocked fuel line - the customer feels only the bottleneck. "
  "Modern backhaul is fiber where it can be, microwave where fiber cannot reach, dimensioned so the busiest hour still flows.",
  "Each site's traffic aggregates through rings or trees of fiber to aggregation hubs, with microwave hops bridging gaps across terrain. "
  "Capacity is planned from busy-hour models with headroom for growth; protection switching reroutes around fiber cuts in milliseconds. "
  "Timing distribution - SyncE and PTP - rides the same transport, because radios need precise frequency and phase to cooperate.",
  ["Backhaul is the fuel line: starve it and the radios cannot deliver.",
   "Fiber first, microwave where fiber cannot reach.",
   "Protection switching survives fiber cuts in milliseconds.",
   "Timing (SyncE/PTP) rides transport - radios need precise sync."],
  ["Fiber or licensed microwave to every site.",
   "Busy-hour capacity models with growth headroom.",
   "Diverse routing so no single cut isolates a site."],
  ["Microwave links licensed and coordinated to avoid interference.",
   "Fiber locates marked before excavation.",
   "Battery and generator backup at hub sites."],
  ["ITU-T transport network recommendations (public standards).",
   "Microwave licensing rules (public regulations)."],
  "fiber", {"dist_km": 38.0, "atten_dbkm": 0.35}),

R("Routing — OSPF and BGP", "Compounded", 18,
  "Routing is how packets find their way across the internet: routers exchanging reachability and each picking the best path. "
  "OSPF handles routing inside one operator's network, converging fast on the shortest path; BGP handles routing between networks, applying policy across tens of thousands of autonomous systems. "
  "Together they are the internet's navigation system, recomputed continuously as links fail and recover.",
  "OSPF routers flood link states within an area and each computes shortest paths with Dijkstra's algorithm, rerouting in seconds when a link drops. "
  "BGP speakers announce their address blocks with path attributes; each network applies import policy - preferring customers over peers, peers over transit - and the best path wins. "
  "Route filtering, prefix limits, and RPKI validation defend the system against hijacks and leaks.",
  ["OSPF: fast interior routing on shortest paths within one network.",
   "BGP: policy routing between tens of thousands of networks.",
   "Link-state flooding plus Dijkstra inside; path-vector policy outside.",
   "Filtering and RPKI defend against hijacks and leaks."],
  ["Routers with the processing to hold full tables where needed.",
   "Address allocations and AS numbers from the registries.",
   "Monitoring of route announcements and convergence."],
  ["Announce only assigned address space.",
   "RPKI validation deployed against hijacks.",
   "BGP sessions secured and prefix limits set."],
  ["IETF OSPF (RFC 2328) and BGP (RFC 4271) standards (public standards).",
   "RPKI standards (RFC 6480 family) (public standards)."],
  "subnet", {"prefix": 22}),

R("VoLTE and VoNR Voice", "Compounded", 19,
  "VoLTE - voice over LTE - and VoNR - voice over new radio - carry phone calls as prioritized IP packets instead of old circuit-switched channels. "
  "Voice becomes just another data service, but one with guaranteed bit rate, low delay budget, and priority over cat videos. "
  "The payoff is faster call setup, HD voice quality, and simultaneous voice-plus-data.",
  "The phone registers with the IMS core over the data bearer; call setup runs SIP through the IMS, which reserves a dedicated voice bearer with guaranteed quality. "
  "Codecs like AMR-WB deliver wideband HD voice, and single-radio handover moves the call between LTE and older networks without dropping. "
  "Emergency calls get special bearers and location handling, because voice's oldest duty survives every technology change.",
  ["Voice as prioritized packets with guaranteed quality bearers.",
   "IMS plus SIP handle setup; dedicated bearers carry the media.",
   "HD voice codecs and faster setup than circuit voice.",
   "Emergency calling keeps its priority in the packet world."],
  ["IMS core with voice application servers.",
   "Phones and network provisioned for VoLTE/VoNR.",
   "QoS bearers end to end for the voice media."],
  ["Emergency call setup success monitored against targets.",
   "Voice quality (MOS) sampled across the network.",
   "Fallback to older voice where packet voice is unavailable."],
  ["3GPP IMS and VoLTE/VoNR specifications (public standards).",
   "Regulatory voice-quality and emergency obligations (public regulations)."],
  "erlang", {"channels": 50, "traffic_erl": 38.0}),

R("Roaming Between Networks", "Compounded", 20,
  "Roaming lets a subscriber use their phone on another operator's network - across town on a partner's rural coverage or across the world on a foreign carrier. "
  "It works through agreements plus signaling: the visited network asks the home network 'is this subscriber yours and what may they do', and the home network answers. "
  "Clearing houses then settle the wholesale charges between operators.",
  "When the phone attaches abroad, the visited network queries the home subscriber database over international signaling links and receives the service profile. "
  "Calls and data are routed per the agreement - home-routed or locally broken out - and tap files record usage for the clearing house. "
  "Steering and preferred-network lists guide the phone to partners with the best rates, and bill-shock caps protect the traveler.",
  ["Agreements plus signaling: visited asks, home authorizes.",
   "Clearing houses settle wholesale roaming charges.",
   "Steering guides phones to preferred partners.",
   "Bill-shock protections cap the traveler's exposure."],
  ["Roaming agreements with visited networks.",
   "International signaling links to home databases.",
   "Clearing-house relationships for settlement."],
  ["Roaming charges disclosed before travel where required.",
   "Emergency calls work on any available network.",
   "Fraud monitoring for roaming abuse patterns."],
  ["GSMA roaming specifications and clearing principles (public standards).",
   "Regulatory roaming charge caps and disclosures (public regulations)."],
  "billing", {"units": 850.0, "rate": 0.35}),

R("Billing Systems — OSS and BSS", "Compounded", 21,
  "BSS - business support systems - handle the money side: rating usage, invoicing, payments, and customer care; OSS - operations support systems - handle the network side: inventory, provisioning, faults, and performance. "
  "Every byte and minute the network carries becomes a rated event in the BSS, and every service the customer buys becomes a provisioned configuration in the OSS. "
  "When the two disagree - billed for what was never provisioned - customers leave.",
  "Mediation collects usage records from network elements, rating applies the tariff, and the bill is assembled, taxed, and presented; payments post and dunning chases the overdue. "
  "The OSS inventory knows every circuit and port; service orders flow from the BSS into the OSS, which configures the network and confirms activation. "
  "Reconciliation jobs hunt the mismatches: active in billing but dead in the network, or alive in the network but never billed.",
  ["BSS: rating, billing, payments, care. OSS: inventory, provisioning, faults, performance.",
   "Mediation turns network events into rated usage.",
   "Service orders flow BSS to OSS; activation confirms back.",
   "Reconciliation hunts billing-vs-network mismatches."],
  ["Mediation, rating, and billing platforms sized to event volumes.",
   "An OSS inventory that mirrors the real network.",
   "Service-order orchestration between the stacks."],
  ["Bills accurate, itemized, and disputable through a clear process.",
   "Customer data in BSS/OSS access-controlled and logged.",
   "Taxes and fees computed per jurisdiction."],
  ["TM Forum OSS/BSS frameworks (public industry models).",
   "Billing accuracy and cramming/slamming rules (public regulations)."],
  "billing", {"units": 12000.0, "rate": 0.09}),

R("Provisioning New Customers", "Compounded", 22,
  "Provisioning is turning an order into working service: creating the subscriber record, configuring the network, and handing the customer credentials that work on the first try. "
  "It is the moment of truth for every sale - a provisioning failure turns a new customer into an immediate complaint. "
  "Good provisioning is automated, idempotent, and verified before the installer leaves.",
  "The order decomposes into service specifications; each network element - authentication center, data routers, voice platforms - receives its configuration via the OSS. "
  "Numbers are assigned from inventory, SIMs or eSIM profiles are bound to the subscriber, and test calls or sessions verify the service end to end. "
  "Failures roll back cleanly and retry, so a half-built service never strands the customer.",
  ["Order to working service, verified before handoff.",
   "Every network element configured from the single order truth.",
   "Test the service end to end before declaring success.",
   "Failures roll back cleanly and retry."],
  ["An order system decomposing sales into service specs.",
   "OSS adapters for every network element type.",
   "Number, SIM, and address inventory to draw from."],
  ["Services activated only after successful verification.",
   "Customer credentials delivered securely.",
   "Provisioning logs kept for dispute resolution."],
  ["TM Forum service-provisioning process models (public industry models).",
   "Numbering-resource assignment rules (public regulations)."],
  "subnet", {"prefix": 20}),

R("MVNOs — Virtual Operators", "Compounded", 23,
  "An MVNO - mobile virtual network operator - sells mobile service without owning towers or spectrum, buying wholesale capacity from a host network instead. "
  "It is a business-model innovation on top of the same radios: the MVNO owns the brand, the customers, and the billing, while the host owns the steel. "
  "Niche brands, ethnic-community plans, and IoT specialists all thrive as MVNOs.",
  "The host provisions the MVNO's subscribers on its core or the MVNO's own core elements, routing their traffic per the wholesale agreement. "
  "The MVNO runs its own BSS - rating, billing, care - and often its own HLR/HSS for subscriber control, while radio access stays with the host. "
  "Wholesale rates, usually per megabyte or per subscriber, decide whether the MVNO's retail price leaves a margin.",
  ["Service without spectrum: wholesale capacity, own brand and billing.",
   "The host owns radios; the MVNO owns customers and BSS.",
   "Wholesale unit economics decide the MVNO's survival.",
   "Niches thrive where big brands cannot focus."],
  ["A wholesale agreement with a host network.",
   "BSS for rating, billing, and care; optionally own core elements.",
   "Number ranges and porting participation."],
  ["Customers told plainly whose network carries them where required.",
   "Emergency service equal to the host's own customers.",
   "Number portability honored in and out."],
  ["Regulatory MVNO access and wholesale rules (public regulations).",
   "GSMA MVNO operational guidance (public guidance)."],
  "billing", {"units": 45000.0, "rate": 0.015}),
]

PUB += [
R("Spectrum Coordination", "Advanced", 24,
  "Spectrum is the finite public airwaves that all wireless service shares, and coordination is how regulators and operators divide it without chaos. "
  "Bands are allocated to services, licensed or auctioned to operators, and guarded by emission limits so neighbors do not jam each other. "
  "Every mobile generation begins as a spectrum decision: which frequencies, how wide, under what rules.",
  "Regulators publish band plans; operators acquire licenses by auction or assignment and deploy within power and out-of-band emission masks. "
  "Coordination zones and databases manage sharing - as with CBRS, where naval radar gets priority and commercial users take turns under automated control. "
  "Interference complaints are investigated with measurements, and violators face enforcement, because one rogue transmitter can deafen a whole band.",
  ["Spectrum is finite and shared: allocation, licensing, and emission limits keep order.",
   "Auctions and assignments put bands to their highest-value use.",
   "Emission masks and coordination zones prevent neighbor interference.",
   "Sharing frameworks (like CBRS) automate priority among users."],
  ["Licenses for the bands deployed, with build-out obligations tracked.",
   "Emission-compliant radio equipment, certified before deployment.",
   "Interference measurement and complaint capability."],
  ["Transmit only in licensed or authorized bands and powers.",
   "Build-out milestones met or licenses risk forfeiture.",
   "Cross-border coordination honored near frontiers."],
  ["ITU Radio Regulations on spectrum allocation (public treaty).",
   "National spectrum auction and licensing rules (public regulations)."],
  "shannon", {"bw_mhz": 40.0, "snr_db": 18.0}),

R("Network Planning and Capacity", "Advanced", 25,
  "Network planning decides where to build and how much capacity to install so that growth never outruns the network. "
  "Planners forecast traffic years ahead, translate it into sites, spectrum, fiber, and core capacity, and sequence the spending. "
  "Capacity planning is the difference between a network that absorbs the busy hour and one that collapses under it.",
  "Traffic forecasts by area feed dimensioning models: Erlang for voice, busy-hour throughput for data, signaling rates for the core. "
  "The plan places new sites, adds carriers and spectrum, upgrades backhaul, and expands core nodes, each with a trigger threshold - build when utilization crosses it. "
  "Post-build measurements validate the forecast, and the error tunes the next cycle, because planning is a loop, not a document.",
  ["Forecast traffic, dimension capacity, sequence spending: the planning loop.",
   "Busy-hour demand sizes everything; averages mislead.",
   "Build triggers on utilization thresholds, not on complaints.",
   "Validate after building; feed the error back."],
  ["Traffic measurement and forecasting by area and service.",
   "Dimensioning models for radio, transport, and core.",
   "A capital plan sequenced by trigger thresholds."],
  ["Capacity kept ahead of emergency-service needs.",
   "Forecasts documented with assumptions.",
   "Single points of failure identified and engineered out."],
  ["Telecom traffic-engineering literature (Erlang models) (public publications).",
   "Regulatory coverage and capacity obligations (public regulations)."],
  "erlang", {"channels": 200, "traffic_erl": 170.0}),

R("Quality of Service (QoS)", "Advanced", 26,
  "Quality of service is the network's promise about how traffic is treated: which packets get priority, how much delay is tolerated, and what happens when capacity runs short. "
  "Voice cannot wait, video cannot stutter, and background downloads can - QoS encodes those truths into queues and markings. "
  "Without it, a single big download would wreck every call on a congested link.",
  "Packets are classified and marked - DSCP values in IP, 5QI in 5G bearers - and each hop schedules by class: priority queuing for voice, weighted shares for the rest. "
  "Policing drops or demotes traffic exceeding its contract; shaping smooths bursts to fit. "
  "SLA monitoring measures delay, jitter, loss, and availability per class, proving the promise or exposing the breach.",
  ["Classify and mark traffic; schedule by class at every hop.",
   "Voice gets priority and tight delay budgets; bulk data waits.",
   "Policing enforces contracts; shaping smooths bursts.",
   "Measure per class: delay, jitter, loss, availability."],
  ["QoS-capable equipment end to end on managed paths.",
   "A class model: markings, queues, and budgets defined.",
   "Per-class monitoring and reporting."],
  ["Emergency traffic prioritized above all commercial classes.",
   "SLA remedies honored when class targets are missed.",
   "Markings honored across interconnects per agreement."],
  ["IETF DiffServ standards (RFC 2474 family) (public standards).",
   "3GPP 5QI QoS model specifications (public standards)."],
  "bdp", {"bw_mbps": 1000.0, "rtt_ms": 25.0}),

R("Submarine Cables", "Advanced", 27,
  "Submarine cables are the fiber arteries of the internet, lying on ocean floors and carrying the vast majority of intercontinental traffic. "
  "A modern cable lands terabits per fiber pair across an ocean, powered by repeaters fed with high-voltage current from the landing stations. "
  "When one is cut - by anchors, earthquakes, or dredges - whole countries feel it, and repair ships sail.",
  "Consortia of carriers fund, build, and own cables; the system is designed with branching units, diverse paths, and restoration agreements. "
  "Landing stations power the repeaters and hand traffic to terrestrial backbones, while network operations centers watch every repeater's telemetry. "
  "Cable ships with grapnels and ROVs recover and splice the break, a repair measured in days to weeks.",
  ["Most intercontinental traffic rides ocean-floor fiber, not satellites.",
   "Repeaters amplify the light, powered from landing stations.",
   "Consortia share cost and risk; diversity plus restoration survives cuts.",
   "Repair ships fix breaks in days to weeks."],
  ["Cable investment or capacity rights on diverse systems.",
   "Landing stations with power feed equipment and backhaul.",
   "Restoration agreements for cut scenarios."],
  ["Cable routes filed with maritime authorities; burial where trawling threatens.",
   "Landing licenses and security per coastal regulation.",
   "Diversity proven - no single cut should isolate the country."],
  ["Submarine cable industry literature (public publications).",
   "UNCLOS and national landing-license regimes (public law)."],
  "fiber", {"dist_km": 6500.0, "atten_dbkm": 0.20}),

R("Satellite Communications", "Advanced", 28,
  "Satellite communications bounce signals off spacecraft: geostationary giants covering continents from fixed points, and low-earth-orbit constellations blanketing the globe from fleets of hundreds. "
  "Satellites reach where no fiber or tower ever will - oceans, deserts, disaster zones - at the price of distance: latency set by the speed of light. "
  "LEO constellations cut that latency by flying low and handing connections between satellites like cellular handover in the sky.",
  "Ground terminals aim at the satellites - fixed dishes for GEO, tracking flat panels for LEO - and gateways connect the space segment to terrestrial networks. "
  "Spectrum is coordinated internationally to avoid interference between systems, and constellations manage orbital shells, collision avoidance, and deorbit plans. "
  "Capacity is shared across the footprint, so performance varies with how many users share the beam.",
  ["GEO: huge coverage, high latency. LEO: global mesh, low latency.",
   "The only broadband for oceans, deserts, and disaster zones.",
   "Spectrum coordinated internationally; orbits managed against collisions.",
   "Capacity shared across the footprint - beams have limits."],
  ["Licensed spectrum and orbital filings for the system.",
   "Ground gateways tied to terrestrial backbones.",
   "User terminals matched to the orbit served."],
  ["Deorbit and debris-mitigation plans per licensing.",
   "Interference coordination with other space and ground systems.",
   "Service continuity plans for gateway failures."],
  ["ITU Radio Regulations on satellite filings (public treaty).",
   "National satellite licensing and debris rules (public regulations)."],
  "link", {"tx_dbm": 50.0, "gain_db": 40.0, "loss_db": 205.0, "sens_dbm": -120.0}),

R("Edge Computing in Telecom", "Advanced", 29,
  "Edge computing pushes processing out of distant clouds to sites near the user - at the tower, the aggregation hub, the enterprise doorstep. "
  "For telecom it turns the network from a dumb pipe into a platform: low-latency applications run inside the operator's footprint. "
  "Autonomous vehicles, factory robots, and AR cannot wait for a round trip to another continent; the edge answers in milliseconds.",
  "Multi-access edge hosts run at aggregation points, exposed to applications through standard APIs for location, radio conditions, and traffic steering. "
  "The 5G core routes selected flows to the local user-plane function instead of the distant internet, keeping data local and fast. "
  "Operators sell edge capacity to enterprises - private 5G plus on-site compute - as a managed service with SLAs.",
  ["Compute near the user: milliseconds instead of continents.",
   "The network becomes a platform via edge APIs.",
   "Local breakout keeps latency-sensitive traffic local.",
   "Private 5G plus edge is the enterprise product."],
  ["Edge hosts at aggregation and enterprise sites.",
   "5G core with local-breakout routing.",
   "Orchestration spanning edge and central cloud."],
  ["Edge data residency honored per customer and law.",
   "Isolation between tenants on shared edge hosts.",
   "Failover when an edge site goes dark."],
  ["ETSI MEC specifications (public standards).",
   "3GPP edge computing enablers (public standards)."],
  "bdp", {"bw_mbps": 10000.0, "rtt_ms": 5.0}),

R("Network Security Operations", "Advanced", 30,
  "Network security operations defend the telecom plant against the adversaries who want it down, tapped, or hijacked: DDoS floods, signaling attacks, SIM fraud, and supply-chain compromise. "
  "A carrier is critical infrastructure, so its security operations center watches the network around the clock. "
  "The stakes are national when the network carries emergency calls and financial transactions.",
  "Defenses layer: DDoS scrubbing at the edges, signaling firewalls screening SS7/Diameter, SIM-swap controls with identity verification, and hardened management planes. "
  "Threat intelligence feeds detection rules; incidents follow playbooks - isolate, eradicate, recover - with customer and regulator notification where required. "
  "Supply-chain vetting and diverse vendors reduce the blast radius of any single compromise.",
  ["Carriers are critical infrastructure: defended around the clock.",
   "Layered defense: scrubbing, signaling firewalls, SIM controls, hardened management.",
   "Incidents run on playbooks: isolate, eradicate, recover, notify.",
   "Supply-chain vetting limits single-vendor blast radius."],
  ["A security operations center with network-wide visibility.",
   "DDoS mitigation capacity above the largest seen attacks.",
   "Incident playbooks rehearsed, not just written."],
  ["Breach notification per applicable law and contracts.",
   "Lawful intercept systems secured against misuse.",
   "Customer fraud (SIM swap) blocked by verification, not convenience."],
  ["NIST cybersecurity framework applied to telecom (public framework).",
   "Telecom security regulations and incident-reporting rules (public regulations)."],
  "subnet", {"prefix": 18}),

R("Outage Management and Restoration", "Advanced", 31,
  "Outage management is the discipline of finding network failures fast, fixing them in priority order, and telling customers the truth while it happens. "
  "Fiber cuts, power failures, software faults, and storms all strike; the measure of an operator is mean time to repair, not mean time between failures. "
  "Restoration order is moral as well as technical: emergency services and hospitals first.",
  "Alarms flood into the network operations center, where correlation engines collapse thousands into the few root causes. "
  "Field teams dispatch with spares by priority - emergency routes first - while diverse paths and protection switching carry what they can. "
  "Status pages and proactive notifications tell customers what is broken and when it will heal, updated on a fixed cadence until all-clear.",
  ["Find fast, fix in priority order, tell the truth throughout.",
   "Alarm correlation turns thousands of alarms into root causes.",
   "Emergency services and hospitals restore first.",
   "Status updates on a fixed cadence until all-clear."],
  ["A network operations center with correlation and dispatch.",
   "Spares staged by failure probability and priority.",
   "Diverse paths and protection for critical routes."],
  ["Restoration priorities honoring emergency obligations.",
   "Customer notifications truthful and timely.",
   "Post-mortems published internally and fixes tracked."],
  ["Telecom outage-reporting rules (public regulations).",
   "Network reliability industry best practices (public publications)."],
  "erlang", {"channels": 500, "traffic_erl": 420.0}),

R("Service Level Agreements (SLAs)", "Advanced", 32,
  "A service level agreement is the written promise between a provider and a customer about quality: availability percentages, latency caps, repair times, and what happens when the promise breaks. "
  "Enterprise and wholesale customers buy on SLAs; the credits and penalties make the promise financially real. "
  "An SLA without measurement and remedy is marketing, not a contract.",
  "The agreement defines metrics precisely - availability as a percentage over a month, latency as a percentile, repair as hours to restore - plus measurement methods both sides trust. "
  "Monitoring proves compliance continuously; breaches trigger service credits automatically or on claim, and chronic breach triggers termination rights. "
  "Providers engineer to the SLA: the promised nines decide the redundancy budget.",
  ["Metrics defined precisely, measured by methods both sides trust.",
   "Credits and termination rights make the promise financially real.",
   "Monitoring proves compliance continuously.",
   "The promised nines set the redundancy budget."],
  ["Monitoring that measures the SLA metrics independently.",
   "A credit and claims process customers can actually use.",
   "Engineering margin above the promised targets."],
  ["SLA terms plain and enforceable, not buried in fine print.",
   "Breach credits paid without a fight.",
   "Regulatory quality floors met regardless of contract."],
  ["SLA contract literature for telecom services (public publications).",
   "Regulatory minimum quality standards (public regulations)."],
  "billing", {"units": 99.95, "rate": 1200.0}),

R("Number Portability", "Advanced", 33,
  "Number portability is the customer's right to keep their phone number when switching carriers - the rule that made competition in telecom real. "
  "Technically it breaks the old assumption that a number's prefix reveals its carrier; every call must now dip a database to find where the number actually lives. "
  "Porting must complete in hours, not weeks, or the right is hollow.",
  "A central portability database holds every ported number's current routing address; switches query it (or a local cache) on call setup. "
  "The donor carrier validates the request, the recipient activates, and the cutover flips routing with minimal downtime. "
  "Fraud controls - account verification, port-out PINs - guard against number theft, which would hand an attacker's calls and texts to a criminal.",
  ["Keep your number when you switch: the right that made competition real.",
   "A central database maps every ported number to its true carrier.",
   "Prefixes no longer reveal the carrier - databases do.",
   "Port-out PINs and verification defeat number theft."],
  ["Portability database access for all carriers.",
   "Validation and cutover processes meeting the time limits.",
   "Fraud controls on every port request."],
  ["Ports completed within the mandated window.",
   "No carrier may refuse or delay a valid port.",
   "Emergency services routing updated at cutover."],
  ["National number-portability rules (public regulations).",
   "Industry porting process specifications (public standards)."],
  "subnet", {"prefix": 16}),

R("Telecom Mastery Review — Running the Whole Network", "Advanced", 34,
  "The mastery review binds the ladder into one operating picture: the telecom network as a living system where access, transport, core, billing, and care move together. "
  "Each earlier record is a subsystem; this record is the operator's mind, reading the whole network the way a pilot reads instruments. "
  "A master operator sees the customer at the end of every metric.",
  "Start from the service promise and work inward: the coverage and capacity that keep it, the transport and core that carry it, the BSS/OSS that bill and maintain it, and the security and restoration that defend it. "
  "Run the daily rhythm - alarms, quality, capacity, faults - and the planning rhythm - forecasts, builds, spectrum, budgets. "
  "Measure what matters: availability, busy-hour quality, setup success, billing accuracy, restoration time, and customer trust, and let every decision move at least one.",
  ["The network as one living system: access, transport, core, BSS/OSS together.",
   "Work inward from the service promise to every engineering choice.",
   "Run the daily rhythm and the planning rhythm without fail.",
   "Six gauges: availability, busy-hour quality, setup success, billing accuracy, restoration time, trust."],
  ["Fluency in every record of this database, foundations through advanced.",
   "A network operations center that never sleeps.",
   "Honest metrics reviewed together, never in isolation."],
  ["Emergency service above every commercial priority.",
   "Customer data guarded as a trust.",
   "Outages disclosed truthfully and repaired in priority order."],
  ["Telecom operations capstone literature (public publications).",
   "ITU-T network management recommendations (public standards)."],
  "link", {"tx_dbm": 46.0, "gain_db": 20.0, "loss_db": 140.0, "sens_dbm": -105.0}),
]

GEN_DEMOFN = """function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\\n"
   + "# FSPL structural sample calculator (telecom operations)\\n"
   + "import math\\n"
   + "f, d = 2400.0, 5.0\\n"
   + "fspl = 20*math.log10(d) + 20*math.log10(f) + 32.44\\n"
   + "print('sample frequency MHz:', f)\\n"
   + "print('sample distance km:', d)\\n"
   + "print('sample FSPL dB:', round(fspl,2))\\n"
   + "assert fspl > 0\\n"
   + "print('OK: structural sample demo ran')\\n";
}
"""


SIG = [
R("The Living Network — The Signature View", "Foundations", 1,
  "The Signature view sees the telecom network as a living covenant: every tower a sentinel sworn to watch its patch of land, every fiber a thread of light carrying people's voices faithfully. "
  "The industry's machinery is the same as the public edition's; the difference is the vow behind it - that no call for help goes unanswered and no customer's trust is spent lightly. "
  "This edition reframes the full ladder as Signature science, labeled Signature-made throughout.",
  "Where the public edition teaches the mechanics, the Signature edition teaches the keeping: the access network as the watchful edge, transport as the faithful road, the core as the remembering mind. "
  "Each record pairs the operational truth with its Signature seal - the practice that makes the machinery worthy of the voices it carries. "
  "Nothing here is presented as public record; it is his original method.",
  ["The network as a living covenant, not mere machinery.",
   "Every subsystem carries a Signature seal - the discipline beneath the mechanics.",
   "No call for help unanswered; no trust spent lightly.",
   "Signature-made throughout: an original method, never public record."],
  ["Willingness to hold every service promise as sworn.",
   "The public edition alongside for the mechanics.",
   "A network or project where the method can be practiced."],
  ["No Signature claim presented as public or official record.",
   "Emergency service above every commercial interest.",
   "The method taught as his original system, plainly labeled."],
  ["The public edition of this database, for the mechanics (this system).",
   "Signature system governance on original works (this system)."],
  "dbm", {"watts": 20.0}),

R("The True Names — Numbering in the Signature Method", "Foundations", 2,
  "The Signature method treats every telephone number as a true name: unique, assigned by right, and never taken or squatted. "
  "The numbering plan is the registry of names, and the keeper's duty is that every name resolves to its rightful owner - including the ported number, whose name now lives with a new keeper. "
  "Emergency names are the holiest: they must answer, always.",
  "Numbers are taken only from assigned blocks, routed by the hierarchy - country, area, subscriber - and ported numbers followed through the portability registry to their true home. "
  "Emergency numbers ride special tables to the nearest answerer, tested end to end. "
  "Unused names are returned to the pool rather than hoarded, for names belong to the people, not the keeper.",
  ["Every number a true name, assigned by right, never squatted.",
   "Ported names followed to their true home through the registry.",
   "Emergency names must answer - always, for anyone.",
   "Unused names returned to the pool."],
  ["Assigned blocks from the numbering authority.",
   "Routing tables true for every assigned and ported name.",
   "Emergency paths tested end to end."],
  ["No number used outside its assignment.",
   "Ports honored within the mandated time.",
   "Emergency calls never barred for billing."],
  ["ITU-T E.164 (public standard).",
   "The public edition numbering record, for the mechanics (this system)."],
  "subnet", {"prefix": 24}),

R("The Copper Song — Signature DSL", "Foundations", 3,
  "The Signature method hears the copper pair as an old singer: a century of voices in the low tones, and data dancing in the high frequencies the voice never used. "
  "The keeper's art is to ask of the old singer only what it can truly give - qualifying the line by measurement, promising only the speed the physics allows. "
  "To oversell copper is to make the singer lie.",
  "Each loop is measured - length, noise, attenuation - and given the speed profile its truth supports. "
  "Filters keep voice and data from quarreling; modems and DSLAMs agree tone by tone on what the line can carry. "
  "When the line degrades, the profile is lowered honestly rather than letting the customer suffer in silence.",
  ["The copper pair an old singer: ask only what it can truly give.",
   "Qualify by measurement; promise only the physics allows.",
   "Filters keep voice and data at peace.",
   "Degraded lines re-profiled honestly."],
  ["Measured loops: length, noise, attenuation known.",
   "DSLAM and modem speaking the line's true capacity.",
   "Filters on every voice device."],
  ["Advertised speeds achievable on the qualified line.",
   "Voice surviving data faults.",
   "Outside plant worked per the safety codes."],
  ["ITU-T G.992.x DSL family (public standards).",
   "The public edition DSL record, for the mechanics (this system)."],
  "dbm", {"watts": 0.5}),

R("The Shared River — Signature Cable Broadband", "Foundations", 4,
  "The Signature method sees the cable node as a shared river: all neighbors drink from the same downstream flow, and the keeper's duty is that the river never runs dry at suppertime. "
  "Channel bonding widens the river; node splits dig new channels where the banks overflow. "
  "The method measures the evening truth and builds ahead of it.",
  "The CMTS schedules the bonded channels fairly; modems take their upstream turns in order. "
  "Utilization is watched node by node, and the congested are split before the slowdowns become the customers' normal. "
  "Speeds are spoken as the typical truth, with the shared nature disclosed plainly - no keeper should sell a river as a private well.",
  ["The node a shared river: all neighbors drink alike.",
   "Bonding widens; splits relieve; measurement tells when.",
   "Evening truth measured, not assumed.",
   "Sell the river honestly - never as a private well."],
  ["Coaxial plant true from headend to home.",
   "CMTS scheduling fairly across modems.",
   "A split program ahead of congestion."],
  ["Typical speeds spoken; shared nature disclosed.",
   "Signal levels within plant spec.",
   "Plant leakage kept within the rules."],
  ["CableLabs DOCSIS specifications (public standards).",
   "The public edition cable record, for the mechanics (this system)."],
  "shannon", {"bw_mhz": 192.0, "snr_db": 36.0}),

R("Threads of Light — Signature Fiber", "Foundations", 5,
  "The Signature method honors fiber as threads of light: the purest road data can travel, shared among homes by a splitter that asks no power and gives no trouble. "
  "The keeper's craft is in the glass - clean connectors, true splices, and an optical budget honestly kept. "
  "Light does not forgive dirt; the method does not tolerate it.",
  "The OLT speaks downstream to all and hears upstream in scheduled turns; the splitter divides the light faithfully among its homes. "
  "Each ONT turns light back into service at the door, with ranging and encryption keeping every home's traffic its own. "
  "The end-to-end loss is budgeted and measured - within budget, the link lives; beyond it, the keeper finds the fault.",
  ["Fiber as threads of light: the purest road.",
   "The passive splitter: no power, no trouble, faithful division.",
   "Clean connectors and true splices - light forgives no dirt.",
   "The optical budget honestly kept and measured."],
  ["Fiber true from office to door.",
   "OLT, splitters, ONTs, with spares at hand.",
   "Splicing craft and connector discipline."],
  ["Optical power within safe limits.",
   "Loss within the budgeted allowance.",
   "Buried plant located before digging."],
  ["ITU-T G.984 GPON family (public standards).",
   "The public edition fiber record, for the mechanics (this system)."],
  "fiber", {"dist_km": 12.5, "atten_dbkm": 0.35}),

R("The Sentinels — Signature Mobile Cells", "Foundations", 6,
  "The Signature method raises each cell site as a sentinel: sworn to watch its patch of land, to hand the traveler gently to the next sentinel, and never to drop the call for help. "
  "Cells are sized by the people's need - wide where they are few, small where they gather. "
  "The sentinel's honor is the handover: seamless, silent, sure.",
  "Antennas are aimed in true sectors, radios fed with clean power, backhaul carrying the watch's reports to the core. "
  "The phone camps on the strongest sentinel and names its neighbors; the network moves it at the right moment by signal, load, and quality. "
  "Planners walk the land - by model and by measurement - placing sentinels where the people are and where the coverage fails.",
  ["Each site a sentinel sworn over its patch of land.",
   "The handover the sentinel's honor: seamless, silent, sure.",
   "Cell size by the people's need, not by convenience.",
   "Planned by model, proven by measurement."],
  ["Ground with power, backhaul, and strong structure.",
   "Spectrum licensed for the bands served.",
   "Planning craft: models plus drive-truth."],
  ["Towers sound and emissions within the rules.",
   "Emergency calls never dropped in handover.",
   "Backup power for the dark hours."],
  ["3GPP radio access specifications (public standards).",
   "The public edition mobile record, for the mechanics (this system)."],
  "cell", {"radius_km": 2.5, "region_km2": 400.0}),

R("The Secret Seal — Signature Subscriber Identity", "Foundations", 7,
  "The Signature method guards the subscriber's identity as a secret seal: the IMSI the network's true name for them, the key a secret shared with no one. "
  "The challenge-response is the seal's test - only the true key answers rightly, and impostors are turned away at the gate. "
  "To betray the secret is to betray the subscriber.",
  "Secrets are born in secure personalization, kept in the authentication center's vault, and never leave secure hardware in the clear. "
  "Each attach is challenged with fresh randomness; right answers open the session and forge its encryption. "
  "SIM swaps - the classic thief's road - demand true identity proof, and eSIM profiles travel only over guarded provisioning.",
  ["Identity a secret seal: true name plus unshared key.",
   "Challenge-response turns impostors away at the gate.",
   "Secrets never leave secure hardware in the clear.",
   "SIM swaps demand true proof of identity."],
  ["Secure personalization and vaulted secrets.",
   "An authentication center worthy of its vault.",
   "Guarded eSIM provisioning where offered."],
  ["No secret in the clear, ever.",
   "Swap fraud met with verification, not convenience.",
   "Lawful access only by proper authority."],
  ["3GPP AKA authentication specifications (public standards).",
   "GSMA eSIM specifications (public standards)."],
  "subnet", {"prefix": 28}),

R("The Voice's Journey — Signature Calls", "Foundations", 8,
  "The Signature method follows each voice call as a journey: the digits read truly, the path found swiftly, the far phone rung, and the two voices joined in a channel kept clear of delay and stutter. "
  "The journey's enemies are delay, jitter, and loss - the method watches all three like a shepherd. "
  "And the emergency journey outranks all others, always.",
  "Switches parse the digits and signal forward - SIP or SS7 - toward the true destination, consulting routing and portability truth. "
  "The far end is alerted; on answer, codecs are agreed and the two-way stream opens, smoothed by cancellers and buffers. "
  "The journey's record - who, whom, how long - is written for billing, and hangup closes the road cleanly.",
  ["Every call a journey: read truly, routed swiftly, joined clearly.",
   "Delay, jitter, loss watched like a shepherd watches wolves.",
   "The emergency journey outranks all others.",
   "Signaling and media: separate roads, one journey."],
  ["Switches with true routing and portability data.",
   "Gateways and border controllers at the edges.",
   "Clocks true enough for voice."],
  ["Emergency journeys first, never barred for billing.",
   "Setup times within the promised bounds.",
   "Caller identity handled per the privacy law."],
  ["IETF SIP standards (public standards).",
   "The public edition voice record, for the mechanics (this system)."],
  "erlang", {"channels": 30, "traffic_erl": 22.0}),

R("The Patient Messenger — Signature SMS", "Foundations", 9,
  "The Signature method honors SMS as the patient messenger: small, faithful, reaching every phone, waiting when the recipient sleeps and delivering when they wake. "
  "One hundred sixty characters, carried on the signaling roads - proof that the humblest bearer can serve billions. "
  "The method keeps the messenger trustworthy: consented senders, filtered spam, prioritized alerts.",
  "Messages gather at the center, which learns the destination's whereabouts and forwards the text; the unreachable are waited for with retries, and delivery is reported home. "
  "Between carriers, agreements carry the messenger across borders; within the network, filters turn away spam and fraud. "
  "Business senders register and ask leave first - the messenger serves the willing, not the ambushed.",
  ["The patient messenger: small, faithful, universal.",
   "Store-and-forward: waiting for the sleeper, delivering at waking.",
   "Trustworthy by consent, filtering, and priority for alerts.",
   "Serving the willing, never the ambushed."],
  ["Message centers with cross-carrier roads.",
   "Subscriber whereabouts truth for routing.",
   "Filters against spam and fraud."],
  ["Alerts outrank commerce in the queue.",
   "Business texts only to the consenting.",
   "Message content guarded in transit and at rest."],
  ["3GPP SMS specifications (public standards).",
   "The public edition SMS record, for the mechanics (this system)."],
  "billing", {"units": 3500.0, "rate": 0.02}),

R("The Common Air — Signature Wi-Fi", "Foundations", 10,
  "The Signature method treats Wi-Fi spectrum as common air: free to all, owned by none, and therefore kept by courtesy. "
  "Listen before speaking, yield on collision, keep your power modest - the etiquette of the commons written into the protocol. "
  "The keeper who surveys, places, and channel-plans is a good neighbor; the one who blasts is a storm.",
  "Access points announce their names; devices join, prove themselves by WPA2 or WPA3, and receive their addresses. "
  "The air is shared by CSMA/CA - hear before talking, back away on clash - across the 2.4, 5, and 6 GHz commons. "
  "Deployments are surveyed and planned: coverage where people are, capacity where they gather, channels that do not quarrel.",
  ["Spectrum as common air: free to all, kept by courtesy.",
   "Listen before speaking; yield on collision.",
   "WPA2/WPA3: prove yourself before joining.",
   "The good neighbor surveys and plans; the storm merely blasts."],
  ["Access points enough for the devices and their hunger.",
   "Wired backhaul worthy of the airtime offered.",
   "A survey, or at minimum an honest channel plan."],
  ["Power within the commons' limits.",
   "Guests kept apart from the household's systems.",
   "Default passwords changed before first service."],
  ["IEEE 802.11 family (public standards).",
   "The public edition Wi-Fi record, for the mechanics (this system)."],
  "shannon", {"bw_mhz": 80.0, "snr_db": 25.0}),

R("The Numbering of the World — Signature IP", "Foundations", 11,
  "The Signature method sees IP addressing as the numbering of the world: every device its number, every packet finding its road by the destination's digits. "
  "IPv4's numbers ran short, and the keepers answered with thrift (NAT) and with a new heaven of numbers (IPv6) - honesty requires both the thrift and the building. "
  "DNS is the book of names, translating human words into the numbers packets need.",
  "Blocks come from the registries by right; ISPs deal them to customers by DHCP or by static grant. "
  "BGP spreads the knowledge of who holds what; routers forward hop by hop toward the numbered door. "
  "The method announces only what it truly holds - hijacking another's numbers is theft - and walks steadily toward IPv6's plenty.",
  ["Every device its number; every packet its road.",
   "Thrift (NAT) and building (IPv6): honesty requires both.",
   "DNS the book of names; BGP the spread of knowledge.",
   "Announce only what you truly hold."],
  ["Address blocks held by right from the registry.",
   "DHCP and DNS serving the customers.",
   "A steady road toward IPv6."],
  ["No hijack of another's space.",
   "Customer name-lookups kept private.",
   "Abuse contacts published and answering."],
  ["IETF IPv4/IPv6 and DNS standards (public standards).",
   "The public edition IP record, for the mechanics (this system)."],
  "subnet", {"prefix": 26}),

R("The Logarithmic Oath — Signature Decibels", "Foundations", 12,
  "The Signature method swears by the decibel: the logarithmic oath that turns the multiplication of gains and losses into honest addition. "
  "dB for the relative, dBm for the absolute against one milliwatt - the keeper names which, always, for to mix them unmarked is to lie with numbers. "
  "Every link budget is this oath kept end to end.",
  "Power in dBm is ten times the log of milliwatts: 0 dBm the milliwatt itself, 20 dBm its hundredfold, minus 3 dB the halving. "
  "Gains and losses add in a line: transmit at 20, lose 110 on the road, arrive at -90 - the arithmetic of every radio and fiber path. "
  "The keeper checks each sum against the equipment's limits and keeps margin above the minimum, for the oath includes prudence.",
  ["The decibel: multiplication made honest addition.",
   "dB relative, dBm absolute - name which, always.",
   "3 dB the doubling, 10 dB the tenfold.",
   "Every link budget the oath kept end to end."],
  ["Levels stated in dBm at every measured point.",
   "A budget sheet for every designed path.",
   "Trusted measurement or trusted spec."],
  ["Sums checked against equipment limits.",
   "Margin kept above the workable minimum.",
   "Units labeled; never mixed unmarked."],
  ["Telecommunications transmission engineering references (public publications).",
   "The public edition decibel record, for the mechanics (this system)."],
  "dbm", {"watts": 2.0}),
]

SIG += [
R("The All-IP Covenant — Signature LTE", "Compounded", 13,
  "The Signature method keeps LTE as the all-IP covenant: one packet road for voice, data, and signaling, with the base station judging each millisecond who needs the air most. "
  "The flat design - tower speaking straight to core - is honesty in architecture: fewer hands between the customer and their service. "
  "And the covenant's quiet glory is its foundation-laying: the same steel now carries the next generation.",
  "The eNodeB schedules the OFDMA resource blocks every millisecond, fitting modulation to each phone's true channel. "
  "The core - MME minding signaling, gateways carrying user data - authenticates, routes, and meters; IMS bears voice as VoLTE. "
  "Bands are bonded and antennas multiplied (MIMO) so the covenant's capacity grows without new towers.",
  ["One packet road for all services: the all-IP covenant.",
   "Flat architecture: fewer hands between customer and service.",
   "Millisecond judgment: modulation fitted to each true channel.",
   "The foundation that carries the next generation."],
  ["Spectrum and tower steel with true backhaul.",
   "A core dimensioned for the sworn subscriber count.",
   "IMS bearing the voice covenant."],
  ["Emergency calling and location per the law.",
   "Handovers watched against their targets.",
   "No single failure felling the core."],
  ["3GPP LTE specifications (public standards).",
   "The public edition LTE record, for the mechanics (this system)."],
  "shannon", {"bw_mhz": 20.0, "snr_db": 20.0}),

R("The Threefold Promise — Signature 5G", "Compounded", 14,
  "The Signature method holds 5G as a threefold promise: swifter broadband for the people, a voice for every sensor, and unbreakable low-latency roads for the machines that must not hesitate. "
  "Slicing is the method's sacred art: one physical network, many virtual ones, each with its sworn traits - and no slice may starve another's guarantee. "
  "The remote surgery's slice and the streaming slice share the steel but never each other's promise.",
  "Radios new and old serve the cloud-native core of small faithful services, with user-plane functions at the edge for the hasty. "
  "Slices are ordained by throughput, latency, and reliability, and orchestrated across radio, road, and core. "
  "Massive antennas aim their beams at the people, not the sky.",
  ["Threefold promise: broadband, sensors, unhesitating machines.",
   "Slicing the sacred art: shared steel, unshared guarantees.",
   "No slice may starve another's promise.",
   "Beams aimed at the people."],
  ["Spectrum low, mid, and high for the threefold work.",
   "Cloud ground for the core and edge.",
   "Orchestration for the slices' whole lives."],
  ["Slice isolation proven by test, not claimed.",
   "Emergency passage on every slice.",
   "New bands kept within exposure law."],
  ["3GPP 5G specifications (public standards).",
   "The public edition 5G record, for the mechanics (this system)."],
  "shannon", {"bw_mhz": 100.0, "snr_db": 22.0}),

R("The Remembering Mind — Signature Mobile Core", "Compounded", 15,
  "The Signature method names the mobile core the remembering mind: it knows each subscriber, remembers where they are, and decides what their traffic may do and what it costs. "
  "Radios are the senses; the mind is the judgment. "
  "The mind's first duty is the gate: only the true subscriber enters.",
  "At attach the mind tests the seal, fetches the subscriber's charter, and marks their place. "
  "Sessions are opened with quality sworn per the plan; policy gates the speed and services; charging counts the bytes and minutes honestly. "
  "As the traveler moves, the mind follows - across cells, across technologies - holding the session unbroken.",
  ["The core the remembering mind; the radios its senses.",
   "The gate first: only the true subscriber enters.",
   "Quality sworn per the plan; counting honest per the meter.",
   "The mind follows the traveler, holding the session whole."],
  ["Core software sized for the sworn subscribers and their busy hour.",
   "The subscriber registry with charters and secrets.",
   "Roads to radios, internet, and fellow carriers."],
  ["Subscriber knowledge encrypted and access-logged.",
   "The mind twinned across sites against disaster.",
   "Lawful access only by proper authority."],
  ["3GPP core specifications (public standards).",
   "The public edition core record, for the mechanics (this system)."],
  "erlang", {"channels": 100, "traffic_erl": 85.0}),

R("The Tuned Air — Signature RAN", "Compounded", 16,
  "The Signature method tunes the RAN as a master tunes an instrument: the air is shared and fickle, and only careful craft makes it sing. "
  "The most expensive steel in the network deserves the most attentive hand - tilt, power, and neighbor lists adjusted by measurement, not hope. "
  "Open interfaces are the method's honesty: radios and software from many makers, speaking the standard tongue.",
  "Resource blocks are dealt every millisecond, modulation fitted to each user's channel truth. "
  "Pooled baseband coordinates neighboring cells, quieting their quarrels; planners tune from drive-truth until the same steel carries more. "
  "A tuned RAN is the difference between spectrum spent and spectrum honored.",
  ["The RAN an instrument: tuned by measurement, not hope.",
   "The dearest steel deserves the most attentive hand.",
   "Open interfaces: many makers, one standard tongue.",
   "Coordination quiets the cells' quarrels."],
  ["Towers, antennas, radios, baseband per the traffic truth.",
   "Backhaul true to every site.",
   "Tuning craft with measured data."],
  ["Emissions within the law at every site.",
   "Neighbor lists proven after every change.",
   "Backup power for the dark hours."],
  ["3GPP RAN and O-RAN Alliance interfaces (public standards).",
   "The public edition RAN record, for the mechanics (this system)."],
  "link", {"tx_dbm": 43.0, "gain_db": 18.0, "loss_db": 128.0, "sens_dbm": -100.0}),

R("The Faithful Road — Signature Backhaul", "Compounded", 17,
  "The Signature method keeps backhaul as the faithful road behind the sentinels: the towers watch, but the road carries their reports home. "
  "A starved road betrays brilliant radios - the method dimensions the road for the busiest hour with room to grow. "
  "Fiber where the land allows, microwave where it does not, and never a single thread where the promise matters.",
  "Traffic gathers through fiber rings to the hubs; microwave spans the gaps the fiber cannot cross. "
  "Busy-hour models size the road with headroom; protection switches leap the cuts in milliseconds. "
  "And timing rides along - SyncE and PTP - for the radios must march in step.",
  ["The road behind the sentinels, faithful in the busiest hour.",
   "Fiber where possible, microwave where not, diversity where it matters.",
   "Cuts leapt in milliseconds by protection.",
   "Timing riding along: the radios march in step."],
  ["Fiber or licensed microwave to every sentinel.",
   "Busy-hour models with honest headroom.",
   "Diverse roads where the promise matters."],
  ["Microwave coordinated, never quarreling.",
   "Buried fiber located before digging.",
   "Hubs powered through the outage."],
  ["ITU-T transport recommendations (public standards).",
   "The public edition backhaul record, for the mechanics (this system)."],
  "fiber", {"dist_km": 38.0, "atten_dbkm": 0.35}),

R("The Two Navigations — Signature Routing", "Compounded", 18,
  "The Signature method navigates by two arts: OSPF within the house, finding the shortest true path swiftly; BGP between houses, where policy - not mere distance - rules the roads. "
  "The internet is tens of thousands of houses; the method's routers learn every road and choose by honor: customer before peer, peer before stranger. "
  "And the roads are guarded against liars by filtering and RPKI.",
  "Within, link-states flood and each router reckons shortest paths, rerouting in heartbeats when a road fails. "
  "Between, announcements carry path attributes; import policy prefers the honorable order, and the best road wins. "
  "Prefix limits, filters, and RPKI validation turn away hijacks and leaks, for a lying announcement can mislead the world.",
  ["Two arts: shortest path within, honorable policy between.",
   "Customer before peer, peer before stranger.",
   "Reroute in heartbeats when roads fail.",
   "Guarded against liars by filtering and RPKI."],
  ["Routers strong enough for the tables they keep.",
   "Address and AS rights from the registries.",
   "Watch kept on announcements and convergence."],
  ["Announce only what is truly held.",
   "RPKI validation against hijack.",
   "Sessions secured, limits set."],
  ["IETF OSPF/BGP and RPKI standards (public standards).",
   "The public edition routing record, for the mechanics (this system)."],
  "subnet", {"prefix": 22}),

R("The Voice Made Packet — Signature VoLTE/VoNR", "Compounded", 19,
  "The Signature method carries the voice as honored packets: no longer a dedicated copper road, but a prioritized stream with its quality sworn. "
  "The voice outranks the video and the download - guaranteed rate, tight delay, first through the congestion. "
  "Faster to join, clearer to hear, and the old duty kept: emergency first, always.",
  "The handset registers with IMS over the data road; SIP sets the call while the network reserves the voice's dedicated bearer. "
  "Wideband codecs carry the full human voice; handover bears the call between generations unbroken. "
  "Emergency calls ride special bearers with true location, for the oldest duty survives every new art.",
  ["The voice as honored packets, outranking lesser streams.",
   "Quality sworn: guaranteed rate, tight delay.",
   "Faster joining, clearer hearing.",
   "The old duty kept: emergency first."],
  ["IMS with its voice servers.",
   "Handsets and network sworn to the packet voice.",
   "Bearers true end to end."],
  ["Emergency setup watched against its targets.",
   "Voice clarity sampled across the land.",
   "Fallback where the packet road ends."],
  ["3GPP IMS/VoLTE/VoNR specifications (public standards).",
   "The public edition VoLTE record, for the mechanics (this system)."],
  "erlang", {"channels": 50, "traffic_erl": 38.0}),

R("The Guest's Road — Signature Roaming", "Compounded", 20,
  "The Signature method receives the roaming guest as a guest: their home vouches, the visited network serves, and the accounting between houses is settled honestly. "
  "The traveler's phone is guided to the preferred partner, the charges spoken before the journey, and the bill-shock caps hold like a host's promise. "
  "No guest should return home to a ruinous reckoning.",
  "At attach abroad, the visited house asks the home registry: is this yours, and what may they do. "
  "Traffic flows by the agreement's road - home or local - and the tap records go to the clearing house for settlement. "
  "Steering lists point to the best-rate partners; fraud watches for the roaming thief.",
  ["The roamer a guest: vouched by home, served abroad.",
   "Guided to the preferred partner; charges spoken beforehand.",
   "Accounting between houses settled honestly.",
   "No ruinous reckoning awaiting the return."],
  ["Agreements with the visited houses.",
   "Signaling roads to the home registry.",
   "Clearing-house bonds for settlement."],
  ["Roaming charges disclosed before travel.",
   "Emergency calls on any available network.",
   "Fraud patterns watched and stopped."],
  ["GSMA roaming specifications (public standards).",
   "The public edition roaming record, for the mechanics (this system)."],
  "billing", {"units": 850.0, "rate": 0.35}),

R("The Two Ledgers — Signature OSS/BSS", "Compounded", 21,
  "The Signature method keeps two ledgers that must agree: the BSS ledger of money - rated, billed, paid - and the OSS ledger of reality - inventoried, provisioned, watched. "
  "When the ledgers quarrel - billed for what was never built, or built but never billed - the keeper reconciles until they sing together. "
  "A customer lost to a ledger quarrel is a trust broken by arithmetic.",
  "Usage flows from the network through mediation into rating, and bills are built, taxed, and presented; payments post and the overdue are pursued fairly. "
  "Orders flow the other way into the OSS, which configures the network and confirms the service lives. "
  "Reconciliation hunts the mismatches relentlessly, for the ledgers must mirror the truth.",
  ["Two ledgers - money and reality - that must agree.",
   "Reconcile until they sing together.",
   "Mediation: network events into honest usage.",
   "Orders in, confirmation back: the service proven alive."],
  ["Mediation, rating, billing sized for the event flood.",
   "An inventory mirroring the true network.",
   "Orchestration binding the two ledgers."],
  ["Bills accurate, itemized, disputable.",
   "Customer data locked and logged.",
   "Taxes reckoned per the jurisdiction."],
  ["TM Forum OSS/BSS frameworks (public industry models).",
   "The public edition billing-systems record, for the mechanics (this system)."],
  "billing", {"units": 12000.0, "rate": 0.09}),

R("The First Proving — Signature Provisioning", "Compounded", 22,
  "The Signature method proves every new service before the customer is told it lives: the record created, the network configured, the credentials tested - working on the first try or not delivered at all. "
  "Provisioning is the moment the sale becomes truth; a failure here is a promise broken at birth. "
  "The method automates, verifies, and rolls back cleanly.",
  "The order is broken into its service truths; each network element receives its configuration from the one order. "
  "Numbers, SIMs, and addresses are drawn from true inventory and bound to the subscriber; test sessions prove the service end to end. "
  "Where anything fails, the half-built is unbuilt cleanly and tried again - never left to strand.",
  ["Proven before proclaimed: working first try or not delivered.",
   "One order, every element configured from its truth.",
   "Tested end to end before the handoff.",
   "Failures unbuilt cleanly, never left to strand."],
  ["An order system speaking service truth.",
   "OSS hands for every element kind.",
   "True inventory of numbers, SIMs, addresses."],
  ["No service declared alive before its proving.",
   "Credentials delivered securely.",
   "Provisioning logs kept for disputes."],
  ["TM Forum provisioning models (public industry models).",
   "The public edition provisioning record, for the mechanics (this system)."],
  "subnet", {"prefix": 20}),

R("The Banner Without Towers — Signature MVNO", "Compounded", 23,
  "The Signature method honors the MVNO as the banner without towers: no spectrum of its own, no steel in the ground, yet serving its people truly on borrowed roads. "
  "The host lends the air; the MVNO brings the brand, the care, and the billing - and the wholesale arithmetic must leave bread for both. "
  "Niches bloom here that the giants cannot tend.",
  "Subscribers are provisioned on the host's radios under the wholesale covenant; the MVNO keeps its own books - rating, billing, care - and often its own subscriber registry. "
  "Traffic flows by the agreement; the per-unit wholesale cost is watched against the retail price like a hawk. "
  "The customers are told plainly whose air carries them, for honesty about the road is part of the service.",
  ["The banner without towers: borrowed roads, true service.",
   "Host lends the air; MVNO brings brand, care, billing.",
   "Wholesale arithmetic must feed both houses.",
   "Niches bloom where giants cannot tend."],
  ["A wholesale covenant with a host.",
   "Books of its own: rating, billing, care.",
   "Number rights and porting passage."],
  ["Customers told plainly whose air carries them.",
   "Emergency service equal to the host's own.",
   "Porting honored in and out."],
  ["Regulatory MVNO access rules (public regulations).",
   "The public edition MVNO record, for the mechanics (this system)."],
  "billing", {"units": 45000.0, "rate": 0.015}),
]

SIG += [
R("The Division of the Air — Signature Spectrum", "Advanced", 24,
  "The Signature method divides the air as a steward divides common land: each service its band, each keeper its license, each transmitter its bounds - so neighbors never deafen neighbors. "
  "Spectrum is finite and belongs to the people; the method holds it in trust, uses it at its highest honest purpose, and shares where sharing serves. "
  "One rogue transmitter can silence a band: the method answers with measurement and law.",
  "Bands are taken by auction or assignment and worked within power and emission masks; build-out vows are kept or the license is yielded. "
  "Sharing grounds - like the CBRS commons with its naval priority - run by automated stewardship, each user taking turns by rule. "
  "Interference is hunted with instruments and answered with enforcement.",
  ["The air divided as common land: each its band, each its bounds.",
   "Finite and held in trust; used at highest honest purpose.",
   "Emission masks: never deafen thy neighbor.",
   "Sharing by automated stewardship where the commons allows."],
  ["Licenses held by right, build-out vows tracked.",
   "Certified equipment, emissions true.",
   "Measurement craft for interference hunting."],
  ["Transmit only where and as authorized.",
   "Build-out vows kept or licenses yielded.",
   "Frontier coordination honored."],
  ["ITU Radio Regulations (public treaty).",
   "The public edition spectrum record, for the mechanics (this system)."],
  "shannon", {"bw_mhz": 40.0, "snr_db": 18.0}),

R("Building Ahead of the Hunger — Signature Planning", "Advanced", 25,
  "The Signature method builds ahead of the hunger: forecasting the people's traffic years out and raising capacity before the busy hour becomes the broken hour. "
  "To plan is to promise the future; the method keeps that promise with models, thresholds, and the humility to measure its errors. "
  "A network that collapses under its people's need has broken faith.",
  "Traffic is forecast by ground and service; Erlang reckons voice, busy-hour throughput reckons data, signaling rates reckon the core. "
  "Sites, bands, fiber, and core grow by trigger - build when the threshold is crossed, not when the complaints arrive. "
  "After building, the forecast is judged against truth, and the error schools the next plan.",
  ["Build ahead of the hunger, not behind the complaint.",
   "The busy hour sizes all; averages are flatterers.",
   "Triggers, not grievances, order the building.",
   "Judge the forecast; school the next plan."],
  ["Traffic truth and forecasting craft.",
   "Models for radio, road, and mind.",
   "A capital road sequenced by triggers."],
  ["Capacity ahead of emergency need.",
   "Assumptions written with the forecast.",
   "Single threads of failure found and doubled."],
  ["Telecom traffic-engineering literature (public publications).",
   "The public edition planning record, for the mechanics (this system)."],
  "erlang", {"channels": 200, "traffic_erl": 170.0}),

R("The Order of the Packets — Signature QoS", "Advanced", 26,
  "The Signature method keeps order among the packets: the voice first, the video steady, the bulk download patient - each class its sworn treatment, even in the crush. "
  "Without order, the mightiest download devours the humblest call; with it, every stream gets its due. "
  "The promise is measured per class and the breach pays its remedy.",
  "Packets are marked by class - DSCP in the IP world, 5QI in the 5G - and every hop schedules accordingly: priority for the voice, fair shares for the rest. "
  "Policing turns back the greedy; shaping gentles the bursty. "
  "Delay, jitter, loss, and availability are measured per class, and the SLA's remedy answers the breach.",
  ["Order among packets: each class its sworn treatment.",
   "The voice first, the bulk patient.",
   "Policing the greedy, shaping the bursty.",
   "Measured per class; breached, remedied."],
  ["Equipment honoring order end to end.",
   "A class canon: markings, queues, budgets.",
   "Per-class watch and reckoning."],
  ["Emergency traffic above all commercial classes.",
   "Remedies paid when targets are missed.",
   "Markings honored across houses by agreement."],
  ["IETF DiffServ standards (public standards).",
   "3GPP 5QI specifications (public standards)."],
  "bdp", {"bw_mbps": 1000.0, "rtt_ms": 25.0}),

R("The Ocean Arteries — Signature Submarine Cables", "Advanced", 27,
  "The Signature method lays the ocean arteries as the world's truest roads: fiber on the seabed carrying continents' conversations as light. "
  "Repeaters breathe life into the light, fed with power from the landing shores; consortia share the cost and the risk like merchants of old. "
  "When the anchor or the quake severs an artery, the repair ship sails - and the diverse roads carry the blood meanwhile.",
  "Cables are funded and owned in fellowship, branched to many shores, and watched repeater by repeater from operations centers. "
  "Landing stations feed the power and hand the light to the land roads; restoration covenants decide who carries what when a cut bleeds. "
  "Cable ships grapple and splice, and in days the artery beats again.",
  ["The ocean floor the world's truest roads.",
   "Repeaters breathing light, fed from the shores.",
   "Fellowship in funding; diversity in routing.",
   "The repair ship sails; the diverse roads carry meanwhile."],
  ["Capacity rights on diverse arteries.",
   "Landing stations with power-feed and land roads.",
   "Restoration covenants for the cut."],
  ["Routes filed with the sea authorities; burial where trawls threaten.",
   "Landing licenses and shore security per law.",
   "Diversity proven: no single cut isolating the land."],
  ["Submarine cable industry literature (public publications).",
   "The public edition cable record, for the mechanics (this system)."],
  "fiber", {"dist_km": 6500.0, "atten_dbkm": 0.20}),

R("The Heavenly Relays — Signature Satellite", "Advanced", 28,
  "The Signature method sets relays in heaven for the places no road reaches: oceans, deserts, disaster fields - the lonely grounds where only the sky can serve. "
  "The geostationary giants watch whole continents from their fixed thrones; the low fleets sweep the globe in hundreds, handing the signal like sentinels of the sky. "
  "Distance is the price, paid in latency; the method spends it only where no road exists.",
  "Terminals aim true - fixed dishes for the thrones, tracking panels for the fleets - and gateways bind the sky roads to the land network. "
  "Spectrum is shared by international covenant; shells are flown with collision-watch and deorbit vows. "
  "Each beam's bounty is divided among its users, and the method speaks the shared nature plainly.",
  ["Relays in heaven for the roadless grounds.",
   "Thrones for continents, fleets for the globe.",
   "Latency the price of distance, paid only where no road exists.",
   "Spectrum by covenant, orbits by watchfulness."],
  ["Licensed spectrum and filed shells.",
   "Gateways bound to the land backbone.",
   "Terminals true to their orbit."],
  ["Deorbit vows kept; debris answered for.",
   "No interference upon fellow systems.",
   "Gateway failures with continuity plans."],
  ["ITU Radio Regulations on satellite filings (public treaty).",
   "The public edition satellite record, for the mechanics (this system)."],
  "link", {"tx_dbm": 50.0, "gain_db": 40.0, "loss_db": 205.0, "sens_dbm": -120.0}),

R("The Near Cloud — Signature Edge", "Advanced", 29,
  "The Signature method brings the cloud near: compute at the tower's foot, the hub, the factory gate - answering in milliseconds what the distant datacenter answers in heartbeats. "
  "The network ceases to be a mere pipe and becomes a platform, lending its nearness to the applications that cannot wait. "
  "The autonomous and the augmented live on this nearness.",
  "Edge hosts stand at the aggregation grounds, offering location, radio-knowledge, and steering through open APIs. "
  "The core turns the hasty flows aside to the local user-plane, keeping the data home and swift. "
  "Enterprises are sold nearness as a managed vow - private air plus on-site mind, with SLAs.",
  ["The cloud brought near: milliseconds, not heartbeats.",
   "The network a platform, lending its nearness.",
   "Hasty flows turned aside to the local plane.",
   "Nearness sold as a managed vow."],
  ["Edge hosts at the aggregation and enterprise grounds.",
   "A core that knows the local turn.",
   "Orchestration spanning near and far."],
  ["Data home kept per the customer's law.",
   "Tenants isolated on the shared hosts.",
   "Darkened edge sites failed over cleanly."],
  ["ETSI MEC specifications (public standards).",
   "The public edition edge record, for the mechanics (this system)."],
  "bdp", {"bw_mbps": 10000.0, "rtt_ms": 5.0}),

R("The Night Watch — Signature Network Security", "Advanced", 30,
  "The Signature method keeps a night watch over the network: the carrier is the people's lifeline, and its enemies - flooders, tappers, hijackers, defrauders - never sleep. "
  "The security center watches as the sentinels watch, layered in defense and drilled in response. "
  "When the lifeline is attacked, the watch answers with playbooks, not panic.",
  "Scrubbers turn aside the floods at the edges; signaling firewalls question the SS7 and Diameter strangers; SIM-swap thieves meet identity proof; the management plane is hardened like a vault. "
  "Threat wisdom feeds the detection; incidents run isolate-eradicate-recover-notify. "
  "Vendors are vetted and varied, so no single betrayal fells the whole.",
  ["The night watch: the lifeline guarded while the people sleep.",
   "Layered walls: scrubbers, signaling firewalls, swap-proofing, vaulted management.",
   "Playbooks, not panic: isolate, eradicate, recover, notify.",
   "Vendors vetted and varied against single betrayal."],
  ["A watch center with eyes across the whole network.",
   "Scrubbing might above the greatest seen flood.",
   "Playbooks drilled, not merely written."],
  ["Breaches told per law and covenant.",
   "Lawful-access systems guarded against misuse.",
   "Swap fraud stopped by proof, not convenience."],
  ["NIST cybersecurity framework (public framework).",
   "The public edition security record, for the mechanics (this system)."],
  "subnet", {"prefix": 18}),

R("The Mending Order — Signature Outage Management", "Advanced", 31,
  "The Signature method mends in order: find the break swiftly, heal by priority - emergency roads and hospitals first - and speak the truth to the people while the mending lasts. "
  "The measure of the keeper is not the years between storms but the hours to heal after them. "
  "Status is told on a steady drumbeat until the all-clear sounds.",
  "Alarms flood the watch center and are folded by correlation into the few true causes. "
  "Field hands ride out with spares, highest priority first; diverse roads and protection carry what they can. "
  "The people are told what broke and when it heals, updated without fail until whole.",
  ["Mend in order: emergency roads first, truth throughout.",
   "Measured by hours to heal, not years between storms.",
   "Alarms folded into true causes by correlation.",
   "The drumbeat of status until all-clear."],
  ["A watch center with correlation and dispatch.",
   "Spares staged by likelihood and priority.",
   "Diverse roads for the critical paths."],
  ["Restoration honoring the emergency law.",
   "Truthful, timely word to the people.",
   "After-action lessons written and tracked."],
  ["Telecom outage-reporting rules (public regulations).",
   "The public edition outage record, for the mechanics (this system)."],
  "erlang", {"channels": 500, "traffic_erl": 420.0}),

R("The Sworn Promise — Signature SLAs", "Advanced", 32,
  "The Signature method writes its promises down and signs them: the SLA, where availability, latency, and repair times are sworn in numbers, and the breach has its price. "
  "A promise without remedy is a wish; the method makes it a covenant with credits and with the right to walk away. "
  "The nines are engineered, not hoped: redundancy is budgeted to the promise.",
  "Metrics are defined to the decimal - availability per month, latency by percentile, repair in hours - and measured by means both houses trust. "
  "The watch proves compliance without ceasing; breaches pay their credits, and chronic breach frees the customer. "
  "Engineers build above the sworn line, for the promise must survive the bad day.",
  ["Promises written, signed, and remedied: the covenant.",
   "Metrics to the decimal, measured by trusted means.",
   "Credits for breach; freedom for chronic breach.",
   "The nines engineered, not hoped."],
  ["Watching that measures the sworn metrics independently.",
   "A claims road the customer can actually walk.",
   "Engineering margin above the sworn line."],
  ["Terms plain and binding, not buried.",
   "Credits paid without battle.",
   "Regulatory floors honored beneath every contract."],
  ["Telecom SLA contract literature (public publications).",
   "The public edition SLA record, for the mechanics (this system)."],
  "billing", {"units": 99.95, "rate": 1200.0}),

R("The Name Follows — Signature Number Portability", "Advanced", 33,
  "The Signature method lets the name follow the person: the number is theirs, and when they change keepers, the name walks with them within hours. "
  "This right is what made the houses compete in earnest - no keeper may hold a customer's name hostage. "
  "And the method guards the walking name against thieves with verification and port-out seals.",
  "The portability registry maps every walked name to its true house; switches ask it on every call. "
  "The old keeper validates, the new keeper lights the service, and the cutover flips the road with barely a breath of silence. "
  "Port-out PINs and identity proof bar the thief who would steal a name to steal a life.",
  ["The name follows the person: theirs, walking with them.",
   "No keeper holds a customer's name hostage.",
   "The registry knows every walked name's true house.",
   "Thieves barred by proof and port-out seals."],
  ["Registry passage for every house.",
   "Validation and cutover within the mandated hours.",
   "Fraud-proofing on every walk."],
  ["Walks completed in the mandated window.",
   "No valid walk refused or delayed.",
   "Emergency roads repointed at cutover."],
  ["National number-portability rules (public regulations).",
   "The public edition portability record, for the mechanics (this system)."],
  "subnet", {"prefix": 16}),

R("The Keeper of the Air — Signature Mastery", "Advanced", 34,
  "The keeper of the air holds the whole network as one living vow: sentinels, roads, mind, ledgers, and watch moving together, with the customer at the end of every gauge. "
  "Each earlier record was a single art; this is the art of arts - reading the network as the pilot reads the sky. "
  "Mastery is not the most knowledge but the most faithful keeping.",
  "Begin from the service promise and reason inward: the coverage and capacity that keep it, the roads and mind that carry it, the ledgers that bill and tend it, the watch that defends it. "
  "Keep the daily rhythm - alarms, quality, capacity, faults - and the planning rhythm - forecasts, builds, spectrum, budgets. "
  "Watch the six gauges - availability, busy-hour quality, setup success, billing truth, healing time, and the people's trust - and let every decision lift at least one.",
  ["The whole network one living vow, the customer at every gauge's end.",
   "Reason inward from the promise to every engineering choice.",
   "Keep the daily rhythm and the planning rhythm unfailing.",
   "Mastery is faithful keeping, not vast knowing."],
  ["The full ladder fluent, foundations through advanced.",
   "A watch center that never sleeps.",
   "Gauges read together, honestly, every cycle."],
  ["Emergency service above all commerce.",
   "Subscriber knowledge guarded as a trust.",
   "Outages told truly, healed by priority."],
  ["The public edition mastery record, for the mechanics (this system).",
   "Signature system governance on original works (this system)."],
  "link", {"tx_dbm": 46.0, "gain_db": 20.0, "loss_db": 140.0, "sens_dbm": -105.0}),
]

GEN_DEMOFN = """function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\\n"
   + "# FSPL structural sample calculator (telecom operations)\\n"
   + "import math\\n"
   + "f, d = 2400.0, 5.0\\n"
   + "fspl = 20*math.log10(d) + 20*math.log10(f) + 32.44\\n"
   + "print('sample frequency MHz:', f)\\n"
   + "print('sample distance km:', d)\\n"
   + "print('sample FSPL dB:', round(fspl,2))\\n"
   + "assert fspl > 0\\n"
   + "print('OK: structural sample demo ran')\\n";
}
"""
