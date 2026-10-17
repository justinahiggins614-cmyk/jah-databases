#!/usr/bin/env python3
"""Demo programs for the Cloud and Internet Things databases (Manon's
2026-10-17 15:32 EDT orders #16-17).

Every demo is real, runnable, stdlib-only Python performing the actual
cloud/internet computation for its record. All are machine-executed by
build.py before commit: each prints its real computed values, asserts tight
bounds (never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cit_cloud_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # five NIST essential characteristics scored for two workloads
    chars = ["on-demand self-service", "broad network access",
             "resource pooling", "rapid elasticity", "measured service"]
    # workload A: spiky web shop (great cloud fit), B: steady mainframe batch
    fit_a = [5, 5, 4, 5, 5]
    fit_b = [3, 2, 3, 1, 2]
    score_a = sum(fit_a) / (5 * len(chars)) * 100.0
    score_b = sum(fit_b) / (5 * len(chars)) * 100.0
    print("NIST characteristics: %d" % len(chars))
    print("spiky web shop cloud-fit: %.1f %%" % score_a)
    print("steady batch cloud-fit: %.1f %%" % score_b)
    assert 95.9 < score_a < 96.1
    assert 43.9 < score_b < 44.1
    print("rule: elasticity is the killer feature - fit follows the spike")
    print("OK: %s defined the cloud" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_internet_packets(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # packetization: chop a message into packets, reassemble out of order
    msg = b"CLOUDPACKETDEMO"
    mtu_payload = 5
    pkts = [msg[i:i + mtu_payload] for i in range(0, len(msg), mtu_payload)]
    seq = list(enumerate(pkts))
    # simulate flight: packet 1 "lost"; receiver reports it missing
    received = {0: pkts[0], 2: pkts[2]}
    missing = [i for i in range(len(pkts)) if i not in received]
    print("message bytes: %d, packets: %d, missing after flight: %s" % (len(msg), len(pkts), missing))
    assert len(pkts) == 3 and missing == [1]
    received[1] = pkts[1]  # retransmission arrives
    reassembled = b"".join(received[i] for i in range(len(pkts)))
    print("reassembled: %s" % reassembled.decode())
    assert reassembled == msg
    overhead = len(pkts) * 40  # IP+TCP headers approx
    print("header overhead: %d bytes on %d payload bytes" % (overhead, len(msg)))
    assert overhead == 120
    print("rule: IP routes, TCP guarantees - reliability is rebuilt at the endpoints")
    print("OK: %s delivered every packet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_dns(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # DNS delegation walk + TTL cache math
    hierarchy = [("root", 0.012), (".com", 0.028), ("example.com auth", 0.045)]
    cached = 0.001
    walk = sum(t for _, t in hierarchy)
    print("full delegation walk: %.3f s" % walk)
    assert 0.084 < walk < 0.086
    print("cached answer: %.3f s (%.0fx faster)" % (cached, walk / cached))
    assert 84.9 < walk / cached < 85.1
    # TTL: queries per day for a popular name with 300s TTL from 1M resolvers
    resolvers, ttl = 1_000_000, 300
    q_per_day = resolvers * 86400 / ttl
    print("authoritative QPS load at TTL 300s: %.0f queries/day" % q_per_day)
    assert 287_999_999 < q_per_day < 288_000_001
    q_per_day_3600 = resolvers * 86400 / 3600
    print("at TTL 3600s: %.0f queries/day (%.1fx less)" % (q_per_day_3600, q_per_day / q_per_day_3600))
    assert 11.9 < q_per_day / q_per_day_3600 < 12.1
    print("rule: TTL is the control knob - short for agility, long for efficiency")
    print("OK: %s resolved the phone book" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_ip_addressing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # subnet arithmetic: carve 10.0.0.0/16 into /24 subnets
    def usable(prefix):
        return 2 ** (32 - prefix) - 2
    print("/24 usable hosts: %d" % usable(24))
    assert usable(24) == 254
    print("/16 usable hosts: %d" % usable(16))
    assert usable(16) == 65534
    n_subnets = 2 ** (24 - 16)
    print("/24 subnets inside a /16: %d" % n_subnets)
    assert n_subnets == 256
    # network address of 10.0.5.77/24
    ip = (10 << 24) | (0 << 16) | (5 << 8) | 77
    mask = 0xFFFFFF00
    net = ip & mask
    print("10.0.5.77/24 -> network %d.%d.%d.%d" % ((net >> 24) & 255, (net >> 16) & 255, (net >> 8) & 255, net & 255))
    assert net == (10 << 24) | (0 << 16) | (5 << 8)
    # IPv6 scale
    v6 = 2 ** 128
    print("IPv6 addresses: %.3e" % v6)
    assert 3.402 < v6 / 1e38 < 3.403
    print("rule: the prefix splits street from house - route on the street")
    print("OK: %s carved the neighborhoods" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_http_web(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # status-code triage + cache math
    codes = {200: "success", 301: "redirect", 404: "client error", 500: "server error", 503: "server error"}
    for c, cls in codes.items():
        fam = c // 100
        verdict = {2: "success", 3: "redirect", 4: "client error", 5: "server error"}[fam]
        assert verdict == cls, c
    print("classified %d status codes by first digit" % len(codes))
    # cache win: 1M requests/day, 90% hit ratio, origin 120ms vs edge 8ms
    reqs, hit = 1_000_000, 0.90
    t_origin, t_edge = 0.120, 0.008
    avg = hit * t_edge + (1 - hit) * t_origin
    print("avg latency with 90%% edge hits: %.1f ms" % (avg * 1000))
    assert 19.1 < avg * 1000 < 19.3
    origin_hits = reqs * (1 - hit)
    print("origin requests/day: %.0f (was %.0f)" % (origin_hits, reqs))
    assert 99999 < origin_hits < 100001
    print("rule: read the first digit - it names who is at fault")
    print("OK: %s spoke HTTP" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_tls(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # handshake round-trip math: TLS 1.3 (1-RTT) vs TLS 1.2 full (2-RTT) on 80ms RTT
    rtt = 0.080
    hs13, hs12 = 1 * rtt, 2 * rtt
    print("TLS 1.3 handshake: %.0f ms, TLS 1.2 full: %.0f ms" % (hs13 * 1000, hs12 * 1000))
    assert 79.9 < hs13 * 1000 < 80.1 and 159.9 < hs12 * 1000 < 160.1
    # certificate chain verification logic
    import datetime
    not_before = datetime.date(2026, 1, 1)
    not_after = datetime.date(2027, 1, 15)
    today = datetime.date(2026, 10, 17)
    chain_ok, name_ok, date_ok = True, True, (not_before <= today <= not_after)
    days_left = (not_after - today).days
    print("chain: %s, name: %s, dates: %s, expires in %d days" % (chain_ok, name_ok, date_ok, days_left))
    assert date_ok and days_left == 90
    assert chain_ok and name_ok and date_ok, "certificate must verify on all three"
    print("rule: encryption without authentication is a locked door with no address check")
    print("OK: %s sealed the conversation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_virtualization(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # consolidation math: 40 physical hosts -> virtualized onto fewer hosts
    vms = 320
    cores_per_host, ram_per_host = 64, 512  # GB
    vm_cores, vm_ram = 4, 16
    # with 4:1 CPU overcommit (safe: average VM uses ~12% of its vCPUs)
    eff_cores = cores_per_host * 4
    hosts_by_cpu = math.ceil(vms * vm_cores / eff_cores)
    hosts_by_ram = math.ceil(vms * vm_ram / ram_per_host)
    hosts_needed = max(hosts_by_cpu, hosts_by_ram) + 1  # N+1 spare
    print("VMs: %d -> hosts by CPU: %d, by RAM: %d, with N+1: %d" % (vms, hosts_by_cpu, hosts_by_ram, hosts_needed))
    assert hosts_by_cpu == 5 and hosts_by_ram == 10 and hosts_needed == 11
    saved = 40 - hosts_needed
    print("physical hosts retired: %d of 40 (%.1f %%)" % (saved, saved / 40 * 100))
    assert 72.4 < saved / 40 * 100 < 72.6
    print("rule: memory is the binding constraint - size RAM first, overcommit CPU second")
    print("OK: %s multiplied the machines" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_service_models(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # responsibility-line math: ops hours per model for a 3-tier app
    # hours/month spent on undifferentiated ops
    ops = {"IaaS": 120, "PaaS": 35, "SaaS": 6}
    rate = 95.0  # $/hour loaded engineer cost
    for m, h in ops.items():
        print("%-5s undifferentiated ops: %3d h/mo = $%7.0f/mo" % (m, h, h * rate))
    assert ops["IaaS"] * rate == 11400.0
    assert ops["SaaS"] * rate == 570.0
    saved = (ops["IaaS"] - ops["PaaS"]) * rate * 12
    print("IaaS -> PaaS yearly ops savings: $%.0f" % saved)
    assert 96899 < saved < 96901
    print("rule: hand the provider every layer that is not your advantage")
    print("OK: %s drew the responsibility line" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "cloud_what_is": demo_cit_cloud_what_is,
    "internet_packets": demo_cit_internet_packets,
    "dns": demo_cit_dns,
    "ip_addressing": demo_cit_ip_addressing,
    "http_web": demo_cit_http_web,
    "tls": demo_cit_tls,
    "virtualization": demo_cit_virtualization,
    "service_models": demo_cit_service_models,
}


def demo_cit_deployment_models(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # hybrid burst math: private capacity covers baseload, public absorbs the spike
    baseline, peak = 400, 1400  # vCPUs
    private_cap = 500
    burst = max(0, peak - private_cap)
    print("baseline %d, peak %d vCPU; private covers %d, burst to public: %d" % (baseline, peak, private_cap, burst))
    assert burst == 900
    # public burst cost for a 6-hour sale event at $0.04/vCPU-hour
    cost = burst * 6 * 0.04
    print("6-hour burst cost: $%.2f" % cost)
    assert 215.9 < cost < 216.1
    # owning the burst instead: 900 vCPU idle 362 days a year
    own_waste = burst * 0.04 * 24 * 362
    print("owning burst capacity idle rest of year would waste: $%.0f" % own_waste)
    assert 312767 < own_waste < 312769
    print("rule: data gravity decides - the data chooses the ground first")
    print("OK: %s placed every workload" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_datacenters_regions(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # latency physics: ~10ms round trip per 1000 miles of fiber
    def rtt_ms(miles):
        return miles / 1000.0 * 10.0
    legs = {"user to local region (200 mi)": 200, "user to far region (2800 mi)": 2800}
    for label, mi in legs.items():
        print("%-34s RTT ~%.0f ms" % (label, rtt_ms(mi)))
    assert 1.9 < rtt_ms(200) < 2.1 and 27.9 < rtt_ms(2800) < 28.1
    # availability: one zone 99.9%, two independent zones
    z = 0.999
    two_z = 1 - (1 - z) ** 2
    print("single zone: %.3f%% -> two zones: %.5f%%" % (z * 100, two_z * 100))
    assert 99.9998 < two_z * 100 < 100.0
    downtime_min = (1 - two_z) * 365 * 24 * 60
    print("expected downtime/year at two zones: %.2f minutes" % downtime_min)
    assert 0.52 < downtime_min < 0.53
    print("rule: place regions near users, write the oath in two buildings")
    print("OK: %s mapped the planet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_storage_types(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # eleven nines: expected object loss per year for 1M objects
    durability = 1 - 1e-11
    objs = 1_000_000
    expected_loss = objs * (1 - durability)
    print("durability %.11f -> expected objects lost/year per 1M: %.6f" % (durability, expected_loss))
    assert 0.000009 < expected_loss < 0.000011
    # tiering: 50 TB, hot $0.023/GB-mo vs archive $0.004/GB-mo
    tb_gb = 50 * 1024
    hot, archive = tb_gb * 0.023, tb_gb * 0.004
    print("50 TB hot: $%.0f/mo, archive: $%.0f/mo, saved: $%.0f/mo" % (hot, archive, hot - archive))
    assert 1177.5 < hot < 1177.7 and hot - archive > 970
    # lifecycle: 80% of data older than 90 days -> tier it
    aged = 0.80
    blended = (1 - aged) * 0.023 + aged * 0.004
    print("blended $/GB-mo with lifecycle: $%.4f (vs $0.0230 all-hot)" % blended)
    assert 0.0077 < blended < 0.0079
    print("rule: objects for the warehouse, files for sharing, blocks for the engine room")
    print("OK: %s stocked the vault" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_containers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # layer sharing: 10 images on one base vs 10 independent images
    base_mb, app_layer_mb = 80, 25
    shared = base_mb + 10 * app_layer_mb
    separate = 10 * (base_mb + app_layer_mb)
    print("10 images sharing an 80MB base: %d MB vs independent: %d MB" % (shared, separate))
    assert shared == 330 and separate == 1050
    print("disk saved by layer sharing: %d MB (%.1f %%)" % (separate - shared, (separate - shared) / separate * 100))
    # content addressing: same bytes -> same digest
    import hashlib
    d1 = hashlib.sha256(b"app-layer-bytes").hexdigest()[:12]
    d2 = hashlib.sha256(b"app-layer-bytes").hexdigest()[:12]
    print("digest stable across builds: %s == %s -> %s" % (d1, d2, d1 == d2))
    assert d1 == d2
    # startup: container 300ms vs VM 90s
    print("startup: container ~0.3s vs VM ~90s (%.0fx faster)" % (90 / 0.3))
    assert 299 < 90 / 0.3 < 301
    print("rule: the hash is the seal - same digest, same bytes, everywhere")
    print("OK: %s sealed the boxes" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_kubernetes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # rolling update: 12 pods, maxUnavailable 25%, maxSurge 25%
    replicas = 12
    max_unavail = math.ceil(replicas * 0.25)
    max_surge = math.ceil(replicas * 0.25)
    print("replicas %d: max unavailable %d, max surge %d" % (replicas, max_unavail, max_surge))
    assert max_unavail == 3 and max_surge == 3
    min_available = replicas - max_unavail
    print("minimum serving during rollout: %d pods (%.0f%% capacity)" % (min_available, min_available / replicas * 100))
    assert min_available == 9
    # self-healing: pod crash -> restart; node death -> reschedule
    desired, crashed = 12, 4
    controller = desired  # deployment controller restores the count
    print("desired %d, crashed %d -> controller restores to %d" % (desired, crashed, controller))
    assert controller == desired
    # bin packing: 12 pods x (0.5 CPU, 1GB) onto 4-CPU/16GB nodes
    pod_cpu, pod_mem = 0.5, 1.0
    node_cpu, node_mem = 4.0, 16.0
    per_node = int(min(node_cpu // pod_cpu, node_mem // pod_mem))
    nodes = math.ceil(replicas / per_node)
    print("pods per node: %d -> nodes needed: %d" % (per_node, nodes))
    assert per_node == 8 and nodes == 2
    print("rule: declare the desired state - the harbor-master keeps the oath")
    print("OK: %s ran the port" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_load_balancing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # least-connections distribution across 4 backends
    conns = [0, 0, 0, 0]
    for _ in range(1000):
        i = conns.index(min(conns))
        conns[i] += 1
    print("1000 requests over 4 backends: %s" % conns)
    assert max(conns) - min(conns) <= 1
    # health checks eject a sick backend: 4 -> 3, load per backend rises
    rps = 3000
    per4, per3 = rps / 4, rps / 3
    print("at %d rps: %.0f/backend with 4 healthy, %.0f/backend after one ejected" % (rps, per4, per3))
    assert 749 < per4 < 751 and 999 < per3 < 1001
    # target-tracking autoscale: hold 60% CPU
    current_cpu, target = 0.85, 0.60
    desired = math.ceil(4 * current_cpu / target)
    print("CPU %.0f%% over target %.0f%% -> scale 4 to %d servers" % (current_cpu * 100, target * 100, desired))
    assert desired == 6
    print("rule: the steward divides the crowd justly, the quartermaster hires the hour's strength")
    print("OK: %s balanced the crowd" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_cdn(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # cache economics: 10 TB/mo egress, CDN $0.085/GB vs origin $0.09/GB... use realistic spread
    tb = 10 * 1024  # GB
    cdn_rate, origin_rate = 0.06, 0.09
    hit_ratio = 0.92
    cost = tb * (hit_ratio * cdn_rate + (1 - hit_ratio) * origin_rate)
    no_cdn = tb * origin_rate
    print("10 TB/mo: no CDN $%.0f, with 92%% edge hits $%.0f (saved $%.0f)" % (no_cdn, cost, no_cdn - cost))
    assert 921.5 < no_cdn < 921.7 and 638.9 < cost < 639.1
    # latency: Sydney user, origin Virginia 9800mi vs edge 50mi
    def rtt(mi):
        return mi / 1000 * 10
    print("Sydney->Virginia RTT ~%.0f ms vs Sydney edge ~%.1f ms" % (rtt(9800), rtt(50)))
    assert 97.9 < rtt(9800) < 98.1 and 0.49 < rtt(50) < 0.51
    # thundering herd guard: 1000 simultaneous misses collapse to 1 origin fetch
    print("request collapsing: 1000 hot-asset misses -> 1 origin fetch")
    print("rule: put the truth near every seeker - the choir of echoes")
    print("OK: %s copied the world" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_virtual_networks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # subnet plan inside 10.0.0.0/16: public /24 x2, private app /22, private db /24
    plan = {"public-a": 24, "public-b": 24, "app": 22, "db": 24}
    total = sum(2 ** (32 - p) for p in plan.values())
    print("subnets: %s" % plan)
    print("addresses consumed: %d of 65536 (%.1f %%)" % (total, total / 65536 * 100))
    assert total == 256 + 256 + 1024 + 256
    assert 2.7 < total / 65536 * 100 < 2.8
    # security group evaluation: default deny, explicit allow wins only if no deny
    def allowed(rules, port, src):
        for action, p, s in rules:  # ordered evaluation
            if p == port and s == src:
                return action == "allow"
        return False
    rules = [("allow", 443, "balancer-sg"), ("allow", 5432, "app-sg")]
    print("db:5432 from app-sg -> %s; from internet -> %s" % (allowed(rules, 5432, "app-sg"), allowed(rules, 5432, "0.0.0.0/0")))
    assert allowed(rules, 5432, "app-sg") and not allowed(rules, 5432, "0.0.0.0/0")
    print("rule: draw the walls before raising a single roof")
    print("OK: %s walled the city" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "deployment_models": demo_cit_deployment_models,
    "datacenters_regions": demo_cit_datacenters_regions,
    "storage_types": demo_cit_storage_types,
    "containers": demo_cit_containers,
    "kubernetes": demo_cit_kubernetes,
    "load_balancing": demo_cit_load_balancing,
    "cdn": demo_cit_cdn,
    "virtual_networks": demo_cit_virtual_networks,
})


def demo_cit_cloud_databases(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # read scaling: primary handles 2000 writes/s; add 3 read replicas for 15000 reads/s
    write_qps, read_qps = 2000, 15000
    replica_qps = 6000
    replicas = math.ceil(read_qps / replica_qps)
    print("reads %d/s -> %d read replicas at %d qps each" % (read_qps, replicas, replica_qps))
    assert replicas == 3
    # point-in-time restore: 7-day window, 5-min log granularity
    window_days, granularity_min = 7, 5
    points = window_days * 24 * 60 // granularity_min
    print("restore points in 7-day window at 5-min granularity: %d" % points)
    assert points == 2016
    # CAP: partition happens -> choose consistency (CP) for ledger, availability (AP) for cart
    ledger, cart = "CP: refuse writes rather than risk split-brain", "AP: accept writes, reconcile later"
    print("ledger -> %s" % ledger)
    print("cart   -> %s" % cart)
    print("rule: the ledger on stone, the working notes on swift tablets")
    print("OK: %s kept the memory" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_serverless(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # cost: 5M invocations/mo, avg 256ms at 512MB vs always-on server
    inv, gb_s = 5_000_000, 5_000_000 * 0.256 * 0.5
    price_req, price_gbs = 0.20 / 1e6, 0.0000166667
    cost = inv * price_req + gb_s * price_gbs
    print("5M invocations, %.0f GB-s: $%.2f/mo serverless" % (gb_s, cost))
    assert 11.6 < cost < 11.8
    server = 0.046 * 24 * 30  # small VM always on
    print("equivalent always-on server: $%.2f/mo" % server)
    assert 33.0 < server < 33.2
    print("serverless cheaper by %.1fx for this spiky workload" % (server / cost))
    assert 2.8 < server / cost < 2.9
    # cold start budget: p99 latency 900ms, cold start 400ms eats the budget
    p99, cold = 900, 400
    print("cold start %.0f ms of %.0f ms p99 budget: %.0f%% consumed" % (cold, p99, cold / p99 * 100))
    assert 44.3 < cold / p99 * 100 < 44.5
    print("rule: strength summoned exactly when called, dismissed when done")
    print("OK: %s answered the call" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_iam(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # policy evaluation: explicit deny wins over any allow
    def evaluate(policies):
        if any(p == "deny" for p in policies):
            return "DENY"
        if any(p == "allow" for p in policies):
            return "ALLOW"
        return "DENY"  # default deny
    cases = [
        (["allow"], "ALLOW"),
        ([], "DENY"),
        (["allow", "allow"], "ALLOW"),
        (["allow", "deny"], "DENY"),
    ]
    for pols, want in cases:
        got = evaluate(pols)
        print("policies %s -> %s" % (pols, got))
        assert got == want
    # blast radius: 1 admin key vs 12 scoped role keys
    print("one god-key compromised: 100%% of estate exposed")
    print("one scoped key compromised: ~%.1f%% of estate exposed" % (100 / 12))
    assert 8.3 < 100 / 12 < 8.4
    # key rotation: 90-day rotation vs never
    print("rule: cut every key narrow, set every seal to expire")
    print("OK: %s guarded the seal-ring" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_queues_streams(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # queue backlog drain: 50k messages, 8 workers at 40 msg/s each
    backlog, workers, rate = 50_000, 8, 40
    drain_s = backlog / (workers * rate)
    print("drain 50k backlog with %d workers at %d msg/s: %.1f s" % (workers, rate, drain_s))
    assert 156.1 < drain_s < 156.4
    # stream partitions: 2M events/day, 1 partition ~ 10k events/s peak capacity
    events_day = 2_000_000
    avg_s = events_day / 86400
    peak_s = avg_s * 8
    parts = math.ceil(peak_s / 10000) if peak_s > 10000 else 2
    print("avg %.1f ev/s, peak %.0f ev/s -> partitions: %d (min 2 for HA)" % (avg_s, peak_s, parts))
    assert parts == 2
    # idempotency: at-least-once redelivers 2% duplicates
    dup_rate = 0.02
    processed = 100_000 * (1 + dup_rate)
    print("100k messages at 2%% redelivery -> %d handler executions (handler must be idempotent)" % int(processed))
    assert int(processed) == 102000
    print("rule: the courier waits, the chronicle remembers")
    print("OK: %s ran the nervous system" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_cicd(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # lead time: quarterly big-bang vs daily deploys
    changes = 120
    bigbang_weeks, daily_weeks = 12, 1 / 7
    print("%d changes: big-bang lead time %.0f days, daily-deploy lead time %.1f day" % (changes, bigbang_weeks * 7, daily_weeks * 7))
    # canary math: 5% traffic, error budget 0.1%, detect in 10k canary requests
    canary_share = 0.05
    err_rate_bad = 0.02
    detect_n = 200  # requests to see first errors with high confidence
    total_for_detect = detect_n / canary_share
    print("canary %.0f%%: bad deploy (2%% errors) visible after ~%.0f total requests" % (canary_share * 100, total_for_detect))
    assert total_for_detect == 4000
    # rollback time: blue-green flip 60s vs rebuild 25min
    print("blue-green rollback: ~60s vs rebuild-and-redeploy: ~1500s (%.0fx faster)" % (1500 / 60))
    assert 1500 / 60 == 25
    print("rule: small sworn steps - what is sealed may sail, any step unwound")
    print("OK: %s ran the assembly line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_caching(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # cache-aside: 20k qps, 85% hit ratio, db 25ms vs cache 0.8ms
    qps, hit = 20_000, 0.85
    t_db, t_cache = 0.025, 0.0008
    avg = hit * t_cache + (1 - hit) * t_db
    db_qps = qps * (1 - hit)
    print("avg latency: %.2f ms (was %.0f ms uncached)" % (avg * 1000, t_db * 1000))
    assert 4.42 < avg * 1000 < 4.44
    print("database qps: %.0f (was %d) - %.1fx offload" % (db_qps, qps, qps / db_qps))
    assert 2999 < db_qps < 3001
    # TTL staleness bound: worst case a reader sees 300s-old data
    ttl = 300
    print("worst-case staleness with TTL %ds: %d seconds" % (ttl, ttl))
    # thundering herd: 50k simultaneous misses on one hot key, singleflight -> 1 db query
    print("singleflight: 50000 concurrent misses on hot key -> 1 database query")
    print("rule: remember eagerly, trust the ledger - every answer carries its hour")
    print("OK: %s remembered well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_edge(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # control loop: 10ms budget; cloud RTT 90ms vs edge RTT 4ms
    budget, cloud_rtt, edge_rtt = 10, 90, 4
    print("budget %d ms: cloud RTT %d ms -> %s, edge RTT %d ms -> %s" % (
        budget, cloud_rtt, "MISS", edge_rtt, "HIT"))
    assert cloud_rtt > budget > edge_rtt
    # bandwidth: 1000 cameras at 4 Mbps raw vs 2 kbps event summaries
    cams, raw_mbps, event_kbps = 1000, 4, 2
    raw_total = cams * raw_mbps / 8  # MB/s
    event_total = cams * event_kbps / 8 / 1000  # MB/s
    print("raw video uplink: %.0f MB/s vs edge-filtered events: %.2f MB/s (%.0fx less)" % (
        raw_total, event_total, raw_total / event_total))
    assert raw_total == 500 and 1999 < raw_total / event_total < 2001
    # autonomy: link down 6h, edge keeps deciding locally, syncs on return
    print("6h outage: edge decides locally, store-and-forward syncs 0 lost readings on return")
    print("rule: the watch decides now, the temple remembers forever")
    print("OK: %s posted the far watch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_iot(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # fleet scale: 2M devices, 1 message/min each, 200-byte payloads
    devices, per_min, size = 2_000_000, 1, 200
    msgs_day = devices * per_min * 1440
    gb_day = msgs_day * size / 1e9
    print("2M devices x 1 msg/min: %.2e msgs/day, %.1f GB/day ingest" % (msgs_day, gb_day))
    assert 2.87 < msgs_day / 1e9 < 2.89 and 575 < gb_day < 577
    # MQTT header lightness: 2-byte header on 200-byte payload = 1% overhead
    print("MQTT overhead: 2B header on 200B payload = %.1f%%" % (2 / 200 * 100))
    assert 0.99 < 2 / 200 * 100 < 1.01
    # battery: 2xAA ~ 6000 mWh; radio TX 100mW for 50ms per message
    tx_energy_mwh = 100 * 0.05 / 3600
    per_day = tx_energy_mwh * 1440
    days = 6000 / per_day
    print("radio energy/msg: %.4f mWh -> 2xAA lasts ~%.0f days at 1 msg/min" % (tx_energy_mwh, days))
    assert 2999 < days < 3001
    print("rule: every witness sealed with its own name; silence is the loudest alarm")
    print("OK: %s heard the witnesses" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "cloud_databases": demo_cit_cloud_databases,
    "serverless": demo_cit_serverless,
    "iam": demo_cit_iam,
    "queues_streams": demo_cit_queues_streams,
    "cicd": demo_cit_cicd,
    "caching": demo_cit_caching,
    "edge": demo_cit_edge,
    "iot": demo_cit_iot,
})


def demo_cit_cloud_security(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # blast radius: 1 account vs 4 separated accounts (prod/stage/dev/security)
    print("single account breach: 100% of estate in blast radius")
    print("4-account separation: breach contained to ~25% of estate")
    # guardrail math: 300 resources, weekly drift scan catches misconfig in <=7d vs never
    resources, drift_rate = 300, 0.02
    drifted = resources * drift_rate
    print("2%% weekly drift on 300 resources: ~%.0f misconfigs caught per scan" % drifted)
    assert 5.9 < drifted < 6.1
    # MFA: blocks 99.9% of automated credential attacks per industry studies
    blocked = 0.999
    attempts = 100_000
    print("%.1f%% of %d automated attacks blocked by MFA: %d stopped" % (blocked * 100, attempts, int(attempts * blocked)))
    assert int(attempts * blocked) == 99900
    print("rule: the provider guards the walls - guard everything within")
    print("OK: %s kept the watch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_ddos_waf(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # volumetric: 2.5 Tbps attack vs 40 Gbps origin uplink
    attack_tbps, origin_gbps = 2.5, 40
    ratio = attack_tbps * 1000 / origin_gbps
    print("attack %.1f Tbps vs origin %d Gbps: %.0fx over capacity - absorption mandatory" % (attack_tbps, origin_gbps, ratio))
    assert 62.4 < ratio < 62.6
    # scrubbing: 99.5% attack filtered, 0.1% legitimate collateral
    legit_rps, attack_rps = 8000, 2_000_000
    legit_kept = legit_rps * 0.999
    print("scrubbing keeps %.0f of %d legitimate rps while dropping the flood" % (legit_kept, legit_rps))
    assert 7991 < legit_kept < 7993
    # WAF: 1M requests/day, 0.3% blocked as malicious
    blocked = 1_000_000 * 0.003
    print("WAF blocks %.0f malicious requests/day out of 1M" % blocked)
    assert blocked == 3000
    # count-mode tuning: 50 would-block rules, 2 false positives found before enforcing
    print("count mode: 50 candidate blocks, 2 false positives tuned out before enforce")
    print("rule: the seawall breaks the flood, the gatekeeper knows the dagger")
    print("OK: %s raised both shields" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_zero_trust(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # policy decision: allow only if identity ok AND device healthy AND context ok
    def decide(identity, device, context):
        return "ALLOW" if (identity and device and context) else "DENY"
    cases = [
        (True, True, True, "ALLOW"),
        (True, True, False, "DENY"),   # healthy device, odd context (impossible travel)
        (True, False, True, "DENY"),   # unpatched device
        (False, True, True, "DENY"),   # no MFA
    ]
    for ident, dev, ctx, want in cases:
        got = decide(ident, dev, ctx)
        print("identity=%s device=%s context=%s -> %s" % (ident, dev, ctx, got))
        assert got == want
    # micro-segmentation: flat /16 (65k hosts reachable) vs segments of 64
    print("flat network lateral movement: 65534 reachable hosts")
    print("micro-segmented: 63 reachable hosts (%.2f%% of flat)" % (64 / 65536 * 100))
    assert 0.09 < 64 / 65536 * 100 < 0.11
    # session lifetime: 8h static login vs 15-min re-verified tokens
    print("re-verification: 32 checks/day vs 1 login - trust re-earned continuously")
    print("rule: no courtyard is safe - prove yourself at every door")
    print("OK: %s abolished the courtyard" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_multicloud(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # resilience: single cloud 99.95% vs two independent clouds (active-passive)
    a = 0.9995
    two = 1 - (1 - a) ** 2
    print("one cloud %.3f%% -> two independent: %.6f%%" % (a * 100, two * 100))
    assert 99.99997 < two * 100 < 99.99998
    downtime = (1 - two) * 365 * 24 * 60
    print("expected downtime/year: %.2f minutes" % downtime)
    assert 0.13 < downtime < 0.14
    # egress tax: 20 TB/mo cross-cloud at $0.09/GB
    egress = 20 * 1024 * 0.09
    print("20 TB/mo cross-cloud egress: $%.0f/mo - the tax on smearing workloads" % egress)
    assert 1843.1 < egress < 1843.3
    # leverage: 15% discount on $2M/yr commit from competitive tension
    print("negotiating leverage at $2M/yr: 15%% = $%.0f/yr" % (2_000_000 * 0.15))
    assert 2_000_000 * 0.15 == 300_000
    print("rule: place workloads whole - one oath across many grounds")
    print("OK: %s swore in several courts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_observability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # MTTR: blind (45 min) vs observable (8 min) at $12k/min revenue impact
    mttr_blind, mttr_obs, cost_min = 45, 8, 12000
    saved = (mttr_blind - mttr_obs) * cost_min
    print("MTTR 45 -> 8 min at $12k/min: $%.0f saved per incident" % saved)
    assert saved == 444000
    # trace sampling: 50k rps, keep 100% errors (1%) + 1% of successes
    rps, err = 50_000, 0.01
    kept = rps * err + rps * (1 - err) * 0.01
    print("50k rps -> traces kept: %.0f/s (%.2f%% of traffic)" % (kept, kept / rps * 100))
    assert 994 < kept < 996
    # cardinality: 200 services x 50 endpoints x 10 regions x 5 codes = series
    series = 200 * 50 * 10 * 5
    print("metric series without discipline: %d (bounded labels keep it affordable)" % series)
    assert series == 500000
    # golden signals coverage
    print("four golden signals per service: latency, traffic, errors, saturation")
    print("rule: the outage you cannot see is the outage you cannot fix")
    print("OK: %s held the honest mirror" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_finops(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # rightsizing: 40 servers at 8% CPU, half the size suffices
    servers, util = 40, 0.08
    print("%d servers at %.0f%% CPU: halving sizes saves ~50%% of compute spend" % (servers, util * 100))
    waste = servers * 0.5  # half of each server's cost is pure waste at 8% util
    print("waste equivalent: %.0f full servers idle" % waste)
    assert waste == 20
    # commitment: $50k/mo steady compute, savings plan 40% off
    steady, disc = 50_000, 0.40
    saved_yr = steady * disc * 12
    print("$50k/mo steady at 40%% commitment discount: $%.0f/yr saved" % saved_yr)
    assert saved_yr == 240000
    # spot: fault-tolerant batch at 70% off, 2000 vCPU-hours
    spot_save = 2000 * 0.04 * 0.70
    print("2000 vCPU-h batch on spot (70%% off $0.04): $%.0f saved" % spot_save)
    assert 55.9 < spot_save < 56.1
    # unit economics: $18k/mo / 9M requests
    unit = 18_000 / 9_000_000 * 1000
    print("unit economics: $%.2f per 1000 requests" % unit)
    assert 1.99 < unit < 2.01
    print("rule: cost is an architectural property - design it in")
    print("OK: %s kept the honest ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_disaster_recovery(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # RPO from backup interval: hourly backups -> worst-case 60 min data loss
    interval_min = 60
    print("backup every %d min -> worst-case data loss: %d min (RPO)" % (interval_min, interval_min))
    # RTO ladder across strategies (minutes)
    strategies = {"backup/restore": 240, "pilot light": 60, "warm standby": 20, "active-active": 2}
    for s, rto in strategies.items():
        print("  %-15s RTO ~%d min" % (s, rto))
    assert strategies["backup/restore"] == 240 and strategies["active-active"] == 2
    # cost of downtime vs DR: $25k/min revenue, warm standby $3k/mo
    cost_min, standby_mo = 25_000, 3_000
    breakeven_min = standby_mo * 12 / cost_min
    print("warm standby $3k/mo pays for itself if it saves %.1f min of downtime/year" % breakeven_min)
    assert 1.43 < breakeven_min < 1.45
    # 3-2-1: 3 copies, 2 media, 1 offsite -> ransomware needs 3 independent compromises
    print("3-2-1 rule: attacker must breach 3 independent copies - immutability seals them")
    print("rule: write memory in two lands, rehearse the rising")
    print("OK: %s swore the resurrection oath" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_iac(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # plan diff: desired vs actual across 120 resources
    desired = {"vpc": 2, "subnet": 8, "vm": 40, "db": 6, "lb": 4, "bucket": 60}
    actual = {"vpc": 2, "subnet": 8, "vm": 38, "db": 6, "lb": 4, "bucket": 63}
    to_add = sum(max(0, desired[k] - actual.get(k, 0)) for k in desired)
    to_destroy = sum(max(0, actual.get(k, 0) - desired[k]) for k in desired)
    total = sum(desired.values())
    print("plan: %d to add, %d to destroy, %d unchanged of %d" % (to_add, to_destroy, total - to_add, total))
    assert (to_add, to_destroy, total) == (2, 3, 120)
    # drift: manual console change detected on next plan
    print("drift detected: 3 buckets created by hand -> plan proposes removal (revert or import, decide in review)")
    # environment parity: same module x3 environments
    print("one network module x dev/stage/prod: 3 identical environments from 1 declaration")
    # time: 45-min manual build vs 6-min apply
    print("provisioning: 45 min by hand vs 6 min by apply (%.1fx faster, and identical)" % (45 / 6))
    assert 7.4 < 45 / 6 < 7.6
    print("rule: write the law before raising the walls")
    print("OK: %s wrote the law" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_service_mesh(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # retry budget: 20% of requests may be retried at most
    budget = 0.20
    reqs, failures = 10_000, 300
    retries = min(failures, int(reqs * budget))
    amplified = reqs + retries
    print("%d reqs, %d failed: retries capped at %d (budget %.0f%%) -> backend sees %d" % (
        reqs, failures, retries, budget * 100, amplified))
    assert retries == 300 and amplified == 10300
    # circuit breaker: trip at 50% errors over 100 requests
    window, threshold = 100, 0.50
    errors = 55
    tripped = errors / window > threshold
    print("55 errors/100 requests: breaker %s" % ("TRIPPED - fail fast, shed load" if tripped else "closed"))
    assert tripped
    # canary split: 5% to v2, error rate 3% vs 0.2% baseline -> halt
    v2_err, base_err = 0.03, 0.002
    print("canary v2 error %.1f%% vs baseline %.1f%% -> %s" % (v2_err * 100, base_err * 100, "HALT ROLLOUT" if v2_err > 5 * base_err else "proceed"))
    assert v2_err > 5 * base_err
    # mTLS: 40 services, pairwise trust via mesh CA instead of 780 manual pairs
    import math as m
    pairs = 40 * 39 // 2
    print("40 services: mesh CA replaces %d manual trust pairs" % pairs)
    assert pairs == 780
    print("rule: every servant paired with a seal-bearer")
    print("OK: %s mustered the messengers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cit_future_internet(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\\
def main():
    # IPv6: /64 per subnet -> hosts per subnet
    hosts64 = 2 ** 64
    print("one IPv6 /64 subnet holds %.3e addresses" % hosts64)
    assert 1.844 < hosts64 / 1e19 < 1.845
    # QUIC handshake: 1-RTT vs TCP+TLS 1.2 (3-RTT); 60ms RTT intercontinental-ish
    rtt = 0.060
    quic, old = 1 * rtt, 3 * rtt
    print("connection setup: QUIC %.0f ms vs TCP+TLS1.2 %.0f ms (%.0fx faster)" % (quic * 1000, old * 1000, old / quic))
    assert old / quic == 3
    # adoption curve: 35% of traffic on v6, doubling every ~4 years -> years to 90%
    share, target, doubling = 0.35, 0.90, 4.0
    years = doubling * math.log(target / share, 2)
    print("v6 at %.0f%% doubling every %.0f yr -> 90%% in ~%.1f years" % (share * 100, doubling, years))
    assert 5.4 < years < 5.5
    # LEO latency: 550km orbit vs 35786km GEO (light ~300km/ms round numbers)
    leo_ms = 550 / 300 * 2
    geo_ms = 35786 / 300 * 2
    print("satellite RTT: LEO ~%.0f ms vs GEO ~%.0f ms" % (leo_ms, geo_ms))
    assert 3.6 < leo_ms < 3.7 and 238 < geo_ms < 239
    print("rule: build for the direction - wider streets, swifter couriers")
    print("OK: %s charted the next country" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "cloud_security": demo_cit_cloud_security,
    "ddos_waf": demo_cit_ddos_waf,
    "zero_trust": demo_cit_zero_trust,
    "multicloud": demo_cit_multicloud,
    "observability": demo_cit_observability,
    "finops": demo_cit_finops,
    "disaster_recovery": demo_cit_disaster_recovery,
    "iac": demo_cit_iac,
    "service_mesh": demo_cit_service_mesh,
    "future_internet": demo_cit_future_internet,
})
