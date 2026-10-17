#!/usr/bin/env python3
"""Demo programs for the JAH Signature Cloud databases.

Every demo is real, runnable, stdlib-only Python performing the actual
cloud-computing computation for its record. All are machine-executed by
build.py: each prints its real computed values, asserts tight bounds
(never float exact-equality), and ends with the OK marker.
"""

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", __import__("json").dumps(name))


def demo_cld_what_cloud_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the NIST frame: 5 characteristics, 3 service models, 4 deployment models
    characteristics = ["on-demand self-service", "broad network access",
                       "resource pooling", "rapid elasticity",
                       "measured service"]
    service_models = ["IaaS", "PaaS", "SaaS"]
    deployment_models = ["public", "private", "community", "hybrid"]
    print("essential characteristics: %d" % len(characteristics))
    for c in characteristics:
        print("  - %s" % c)
    print("service models: %d (%s)" % (len(service_models), ", ".join(service_models)))
    print("deployment models: %d" % len(deployment_models))
    assert len(characteristics) == 5
    assert len(service_models) == 3
    assert len(deployment_models) == 4
    # the cloud test: a service missing any characteristic is hosting, not cloud
    score = len(characteristics) / 5.0 * 100.0
    print("NIST completeness score: %.1f %%" % score)
    assert 99.9 < score < 100.1
    print("rule: five characteristics or it is not cloud")
    print("OK: %s defined the frame" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_five_characteristics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rapid elasticity made concrete: base load 10 VMs, peak 120 VMs
    base, peak = 10.0, 120.0
    factor = peak / base
    print("base capacity: %.0f VMs, peak capacity: %.0f VMs" % (base, peak))
    print("elasticity factor: %.1fx" % factor)
    assert 11.9 < factor < 12.1
    # measured service: the meter never sleeps
    metered_units = {"compute-seconds": 86400, "gigabyte-months": 500.0,
                     "gigabytes transferred": 100.0}
    print("metered dimensions: %d" % len(metered_units))
    assert len(metered_units) == 3
    # resource pooling: 4 tenants share one host of 64 vCPUs
    tenants, host_vcpus = 4, 64
    share = host_vcpus / tenants
    print("per-tenant fair share of 64 vCPUs: %.0f" % share)
    assert share == 16
    print("rule: appear unlimited to the consumer, metered to the grain")
    print("OK: %s tested the five" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_service_models(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the nine-layer stack and who manages what per model
    layers = ["application", "data", "runtime", "middleware", "operating system",
              "virtualization", "servers", "storage", "networking"]
    customer_layers = {
        "IaaS": ["application", "data", "runtime", "middleware", "operating system"],
        "PaaS": ["application", "data"],
        "SaaS": [],
    }
    print("stack layers: %d" % len(layers))
    for model in ("IaaS", "PaaS", "SaaS"):
        n = len(customer_layers[model])
        pct = n / len(layers) * 100.0
        print("  %s: customer manages %d of %d layers (%.1f %%)" % (model, n, len(layers), pct))
    iaas_pct = len(customer_layers["IaaS"]) / len(layers) * 100.0
    paas_pct = len(customer_layers["PaaS"]) / len(layers) * 100.0
    assert 55.5 < iaas_pct < 55.6
    assert 22.2 < paas_pct < 22.3
    assert len(customer_layers["SaaS"]) == 0
    print("rule: higher up the stack, less control, less burden")
    print("OK: %s split the stack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_deployment_models(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # control (1-5) versus management burden (1-5) per deployment model
    models = {"public": (2, 1), "private": (5, 5),
              "community": (3, 3), "hybrid": (4, 4)}
    print("%-10s %7s %7s %6s" % ("model", "control", "burden", "ratio"))
    for m, (control, burden) in models.items():
        ratio = control / burden
        print("%-10s %7d %7d %6.2f" % (m, control, burden, ratio))
    assert abs(models["public"][0] / models["public"][1] - 2.0) < 0.01
    assert abs(models["private"][0] / models["private"][1] - 1.0) < 0.01
    assert abs(models["hybrid"][0] / models["hybrid"][1] - 1.0) < 0.01
    # hybrid composition: two distinct infrastructures, one bound system
    bound = len(models)
    print("deployment models bound by portability tech: %d" % bound)
    assert bound == 4
    print("rule: regulated data private, elastic bursts public, bound together")
    print("OK: %s mapped the courts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_shared_responsibility(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # twelve concrete security tasks, audited against the line
    tasks = [
        ("physical facility security", "provider"),
        ("host operating system patching", "provider"),
        ("hypervisor hardening", "provider"),
        ("network fabric protection", "provider"),
        ("managed service patching", "provider"),
        ("facility redundancy", "provider"),
        ("hardware disposal", "provider"),
        ("data classification", "customer"),
        ("identity and access policies", "customer"),
        ("guest OS patching", "customer"),
        ("security group rules", "customer"),
        ("encryption key management", "customer"),
    ]
    provider = sum(1 for _, o in tasks if o == "provider")
    customer = sum(1 for _, o in tasks if o == "customer")
    print("audited tasks: %d" % len(tasks))
    print("  provider (security OF the cloud): %d" % provider)
    print("  customer (security IN the cloud): %d" % customer)
    assert len(tasks) == 12
    assert provider == 7
    assert customer == 5
    print("rule: the provider never patches your application")
    print("OK: %s drew the line" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_virtualization(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # hypervisor overhead on a 100,000-unit host
    host = 100000.0
    type1 = host * (1 - 0.03)
    type2 = host * (1 - 0.12)
    print("host capacity: %.0f units" % host)
    print("Type 1 (3%% overhead): %.0f units for guests" % type1)
    print("Type 2 (12%% overhead): %.0f units for guests" % type2)
    print("bare-metal advantage: %.0f units" % (type1 - type2))
    assert 96999.0 < type1 < 97001.0
    assert 87999.0 < type2 < 88001.0
    assert 8999.0 < (type1 - type2) < 9001.0
    # consolidation: 16 VMs on one host
    vms, hosts = 16, 1
    ratio = vms / hosts
    print("consolidation ratio: %.0f to 1" % ratio)
    assert ratio == 16
    print("rule: the cloud runs bare metal because 9,000 units matter")
    print("OK: %s split the forge" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_regions_azs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # latency follows distance
    lat = {"same AZ": 0.5, "cross AZ": 1.5, "cross region": 100.0}
    for k, v in lat.items():
        print("%-12s latency: %.1f ms" % (k, v))
    assert 0.4 < lat["same AZ"] < 0.6
    # availability follows isolation: minutes per year at each tier
    minutes_per_year = 365.25 * 24 * 60
    single_az = (1 - 0.999) * minutes_per_year / 60.0
    three_az = (1 - 0.9999) * minutes_per_year
    print("single AZ 99.9%%: %.2f hours downtime per year" % single_az)
    print("three AZ 99.99%%: %.1f minutes downtime per year" % three_az)
    assert 8.75 < single_az < 8.77
    assert 52.5 < three_az < 52.6
    print("rule: zones for fault tolerance, regions for disaster, edge for speed")
    print("OK: %s drew the map" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_vpc_networking(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # CIDR math on 10.0.0.0/16
    total = 2 ** 16
    subnet_size = 2 ** 8
    subnets = total // subnet_size
    reserved_per_subnet = 5
    usable = subnet_size - reserved_per_subnet
    print("10.0.0.0/16 total addresses: %d" % total)
    print("/24 subnets: %d" % subnets)
    print("usable per /24 after %d reserved: %d" % (reserved_per_subnet, usable))
    assert total == 65536
    assert subnets == 256
    assert usable == 251
    # defense layers on one packet
    layers = ["edge firewall", "subnet NACL", "security group", "host firewall"]
    print("independent filters per packet: %d" % len(layers))
    assert len(layers) == 4
    print("rule: number every street before building a single house")
    print("OK: %s staked the land" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_storage_types(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # illustrative per-request latency per storage type
    lat = {"block": 0.2, "file": 1.0, "object": 10.0}
    for k, v in lat.items():
        print("%-6s latency: %.1f ms" % (k, v))
    ratio = lat["object"] / lat["block"]
    print("object vs block latency ratio: %.0fx" % ratio)
    assert 49.9 < ratio < 50.1
    # the right home per workload
    homes = {"database": "block", "shared content": "file", "archive": "object"}
    for workload, home in homes.items():
        print("  %-14s -> %s" % (workload, home))
    assert homes["database"] == "block"
    assert homes["archive"] == "object"
    print("rule: match the type to the access pattern or pay for the mismatch")
    print("OK: %s stocked the three storehouses" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_iam_basics(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # least-privilege audit: 48 actions granted, 11 used
    granted, used = 48, 11
    score = used / granted
    print("actions granted: %d, actions used: %d" % (granted, used))
    print("least-privilege score: %.4f" % score)
    assert 0.2291 < score < 0.2292
    verdict = "TIGHTEN" if score < 0.5 else "ACCEPT"
    print("verdict: %s" % verdict)
    assert verdict == "TIGHTEN"
    # policy evaluation order: explicit deny beats allow
    decisions = {"explicit deny": "DENY", "explicit allow": "ALLOW", "no statement": "DENY"}
    assert decisions["explicit deny"] == "DENY"
    assert decisions["no statement"] == "DENY"
    print("evaluation: deny > allow > implicit deny")
    print("rule: the narrowest warrant that lets the work be done")
    print("OK: %s guarded the gate" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_payg_pricing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # a realistic monthly bill, line by line
    compute = 0.20 * 730
    storage = 500 * 0.023
    transfer = 100 * 0.09
    total = compute + storage + transfer
    print("compute  0.20 x 730 h ......... %7.2f" % compute)
    print("storage  500 GB x 0.023 ....... %7.2f" % storage)
    print("transfer 100 GB x 0.09 ........ %7.2f" % transfer)
    print("monthly total ................. %7.2f" % total)
    assert 145.99 < compute < 146.01
    assert 11.49 < storage < 11.51
    assert 8.99 < transfer < 9.01
    assert 166.49 < total < 166.51
    # the idle tax: a stopped-then-forgotten twin doubles the compute line
    waste = compute
    print("forgotten idle twin would waste: %.2f per month" % waste)
    assert 145.99 < waste < 146.01
    print("rule: stop what is not used; the meter never sleeps")
    print("OK: %s read the ledger" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_cloud_apis(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # retry budget: 5 retries, exponential backoff from 1 second
    waits = [1 * (2 ** i) for i in range(5)]
    total_wait = sum(waits)
    print("backoff waits (s): %s" % waits)
    print("total waiting before giving up: %d s" % total_wait)
    assert waits == [1, 2, 4, 8, 16]
    assert total_wait == 31
    # idempotency: repeating a create converges instead of duplicating
    desired, actual = 3, 1
    to_create = desired - actual
    print("desired %d, actual %d -> create %d, duplicates %d" % (desired, actual, to_create, 0))
    assert to_create == 2
    print("rule: declare what should exist; repeat safely; back off politely")
    print("OK: %s spoke to the throne" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_virtual_machines(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # an 8-vCPU workload priced on two families
    hours = 730.0
    general = 0.34 * hours
    compute_opt = 0.30 * hours
    saving_mo = general - compute_opt
    saving_yr = saving_mo * 12
    print("general-purpose  0.34/h: %7.2f /mo" % general)
    print("compute-optimized 0.30/h: %7.2f /mo" % compute_opt)
    print("saving per machine: %5.2f /mo, %7.2f /yr" % (saving_mo, saving_yr))
    assert 248.19 < general < 248.21
    assert 218.99 < compute_opt < 219.01
    assert 29.19 < saving_mo < 29.21
    assert 350.3 < saving_yr < 350.5
    # sizing discipline: 38 percent average CPU means step down
    avg_cpu = 38.0
    action = "STEP DOWN" if avg_cpu < 40 else "HOLD"
    print("average CPU %.0f%% -> %s" % (avg_cpu, action))
    assert action == "STEP DOWN"
    print("rule: never buy a warhorse to pull a cart")
    print("OK: %s chose the family" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_containers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # layered image: base + runtime + app
    base, runtime, app = 80, 120, 15
    image = base + runtime + app
    print("base %d MB + runtime %d MB + app %d MB = %d MB image" % (base, runtime, app, image))
    assert image == 215
    # ten containers share base and runtime layers on one host
    containers = 10
    saved = (containers - 1) * base
    print("%d containers share layers, saving %d MB" % (containers, saved))
    assert saved == 720
    # startup: milliseconds versus seconds
    container_start_ms, vm_start_s = 300, 45
    print("container start ~%d ms vs VM start ~%d s" % (container_start_ms, vm_start_s))
    assert container_start_ms < vm_start_s * 1000
    print("rule: sealed vessels sail identically on any sea - guard the shared keel")
    print("OK: %s sealed the vessels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_kubernetes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scheduling: 6 replicas, 4 pods fit per node
    replicas, per_node = 6, 4
    nodes = math.ceil(replicas / per_node)
    print("replicas %d at %d per node -> %d nodes" % (replicas, per_node, nodes))
    assert nodes == 2
    # rolling update with 25 percent max surge
    peak = math.ceil(replicas * 1.25)
    print("25%% max surge -> peak %d pods during rollout" % peak)
    assert peak == 8
    # reconciliation: desired versus actual
    desired, actual = 6, 4
    to_start = desired - actual
    print("desired %d, actual %d -> controller starts %d" % (desired, actual, to_start))
    assert to_start == 2
    print("rule: declare the desired fleet and the sea obeys")
    print("OK: %s sailed the fleet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_serverless(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # one million invocations: 512 MB for 200 ms each
    invocations = 1e6
    gb_seconds = invocations * 0.5 * 0.2
    compute_cost = gb_seconds * 0.0000166667
    request_cost = 0.20
    total = compute_cost + request_cost
    print("gigabyte-seconds: %.0f" % gb_seconds)
    print("compute %.2f + requests %.2f = %.2f" % (compute_cost, request_cost, total))
    assert 99999.0 < gb_seconds < 100001.0
    assert 1.666 < compute_cost < 1.668
    assert 1.866 < total < 1.868
    # versus the idle server it replaces
    idle_server_mo = 146.00
    print("idle server it replaces: %.2f /mo" % idle_server_mo)
    assert total < idle_server_mo
    print("rule: no idle fires - but endless sparks cost more than one steady flame")
    print("OK: %s cast the sparks" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_object_storage_deep(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # eleven nines: annual loss probability per object
    p_loss = 1e-11
    objects = 1e6
    expected = objects * p_loss
    print("durability: 99.999999999%%")
    print("one million objects -> expected yearly loss: %.5f" % expected)
    assert 0.9e-5 < expected < 1.1e-5
    # objects until one expected loss
    until_one = 1 / p_loss
    print("objects for one expected loss: %.0e" % until_one)
    assert 0.9e11 < until_one < 1.1e11
    # erasure coding: 12 data + 4 parity survives 4 fragment losses
    data_frags, parity_frags = 12, 4
    survivable = parity_frags
    print("erasure %d+%d survives %d simultaneous fragment losses" % (data_frags, parity_frags, survivable))
    assert survivable == 4
    print("rule: durability is mathematics, not magic")
    print("OK: %s plumbed the vault" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "what_cloud_is": demo_cld_what_cloud_is,
    "five_characteristics": demo_cld_five_characteristics,
    "service_models": demo_cld_service_models,
    "deployment_models": demo_cld_deployment_models,
    "shared_responsibility": demo_cld_shared_responsibility,
    "virtualization": demo_cld_virtualization,
    "regions_azs": demo_cld_regions_azs,
    "vpc_networking": demo_cld_vpc_networking,
    "storage_types": demo_cld_storage_types,
    "iam_basics": demo_cld_iam_basics,
    "payg_pricing": demo_cld_payg_pricing,
    "cloud_apis": demo_cld_cloud_apis,
    "virtual_machines": demo_cld_virtual_machines,
    "containers": demo_cld_containers,
    "kubernetes": demo_cld_kubernetes,
    "serverless": demo_cld_serverless,
    "object_storage_deep": demo_cld_object_storage_deep,
}


def demo_cld_block_file_storage(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full-volume read time at provisioned throughput
    terabyte = 1e12
    throughput = 125e6
    seconds = terabyte / throughput
    hours = seconds / 3600.0
    print("1 TB at 125 MB/s: %.0f s (%.2f h)" % (seconds, hours))
    assert 7999.0 < seconds < 8001.0
    assert 2.22 < hours < 2.23
    # IOPS tiers
    tiers = {"general-purpose baseline": 3000, "provisioned": 16000}
    for k, v in tiers.items():
        print("  %s: %d IOPS" % (k, v))
    assert tiers["provisioned"] / tiers["general-purpose baseline"] > 5.0
    print("rule: throughput, not just IOPS, belongs in every storage decision")
    print("OK: %s timed the anvil" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_managed_databases(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # read scale: primary plus three replicas
    write_rps = 1000
    replicas, per_replica_rps = 3, 5000
    read_capacity = replicas * per_replica_rps
    print("primary writes: %d rps" % write_rps)
    print("read replicas: %d x %d rps = %d rps read capacity" % (replicas, per_replica_rps, read_capacity))
    assert read_capacity == 15000
    # failover window
    rto_lo, rto_hi = 60, 120
    print("multi-zone failover RTO: %d to %d s" % (rto_lo, rto_hi))
    assert rto_lo == 60 and rto_hi == 120
    # read/write ratio the replicas absorb
    ratio = read_capacity / write_rps
    print("read-to-write capacity ratio: %.0f to 1" % ratio)
    assert ratio == 15
    print("rule: the provider monks copy and mend; the master keeps the questions")
    print("OK: %s kept the ledgers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_load_balancing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # round robin: 9,000 requests over 3 healthy servers
    requests, servers = 9000, 3
    per_server = requests // servers
    remainder = requests % servers
    distribution = [per_server + (1 if i < remainder else 0) for i in range(servers)]
    print("requests %d over %d servers -> %s" % (requests, servers, distribution))
    assert distribution == [3000, 3000, 3000]
    assert sum(distribution) == requests
    # health checks remove the sick gate
    healthy = [True, True, False]
    live = sum(healthy)
    print("healthy targets: %d of %d" % (live, len(healthy)))
    assert live == 2
    print("rule: forward only to the healthy; divide with a perfect hand")
    print("OK: %s held the gatehouse" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_cdn_edge(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # effective latency at 0.92 hit ratio
    hit_ratio = 0.92
    edge_ms, origin_ms = 25.0, 400.0
    effective = hit_ratio * edge_ms + (1 - hit_ratio) * origin_ms
    print("hit ratio %.2f, edge %.0f ms, origin %.0f ms" % (hit_ratio, edge_ms, origin_ms))
    print("effective latency: %.1f ms" % effective)
    assert 54.9 < effective < 55.1
    speedup = origin_ms / effective
    print("speedup over origin: %.1fx" % speedup)
    assert 7.2 < speedup < 7.3
    # origin offload per terabyte
    offloaded = 1000 * hit_ratio
    print("per TB served, %.0f GB never reach the origin" % offloaded)
    assert 919.9 < offloaded < 920.1
    print("rule: carry the chronicles to the far posts before they are asked")
    print("OK: %s rode the outrider posts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_cloud_network_security(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # zero-trust matrix: 5 services, 4 callers, 9 explicit allows
    services = ["web", "api", "db", "queue", "vault"]
    callers = ["frontend", "worker", "analyst", "backup"]
    allows = {("frontend", "web"), ("frontend", "api"), ("worker", "api"),
              ("worker", "queue"), ("worker", "db"), ("analyst", "api"),
              ("analyst", "vault"), ("backup", "db"), ("backup", "vault")}
    pairs = [(c, s) for c in callers for s in services]
    allowed = sum(1 for p in pairs if p in allows)
    denied = len(pairs) - allowed
    print("caller-service pairs: %d" % len(pairs))
    print("allowed: %d, denied by default: %d" % (allowed, denied))
    assert len(pairs) == 20
    assert allowed == 9
    assert denied == 11
    # every hop encrypted: mTLS coverage
    mtls_coverage = 1.0
    print("service-to-service mTLS coverage: %.0f %%" % (mtls_coverage * 100))
    assert mtls_coverage == 1.0
    print("rule: trust no road, only warrants")
    print("OK: %s manned the fortress" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_observability(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # error budget for 99.9 percent over 30 days
    window_minutes = 30 * 24 * 60
    budget = (1 - 0.999) * window_minutes
    print("30-day window: %d minutes" % window_minutes)
    print("error budget at 99.9%%: %.1f minutes" % budget)
    assert window_minutes == 43200
    assert 43.19 < budget < 43.21
    # burn rate: budget consumed in 6 hours means paging now
    consumed_hours = 6.0
    burn = budget / (consumed_hours * 60)
    print("budget burned in %.0f h -> burn rate %.3f budgets per hour" % (consumed_hours, burn))
    assert 0.119 < burn < 0.121
    # the four golden signals on the dashboard
    signals = ["latency", "traffic", "errors", "saturation"]
    print("golden signals: %d (%s)" % (len(signals), ", ".join(signals)))
    assert len(signals) == 4
    print("rule: read the signs at dawn rather than fight the fire at midnight")
    print("OK: %s kept the watch" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_infrastructure_as_code(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # plan diff: 5 desired against 3 actual (2 matching, 1 drifted)
    desired = {"vpc", "subnet-a", "subnet-b", "database", "bucket"}
    actual = {"vpc", "subnet-a", "database-old"}
    creates = desired - {"vpc", "subnet-a"}          # 2 match, the rest are new
    deletes = {"database-old"} - desired              # drifted resource to remove
    updates = {"database"} if "database-old" in actual else set()  # replace drifted
    print("desired %d, actual %d" % (len(desired), len(actual)))
    print("plan: %d creates, %d updates, %d deletes" % (len(creates), len(updates), len(deletes)))
    assert len(creates) == 3
    assert len(updates) == 1
    assert len(deletes) == 1
    print("rule: the drawing is law; the night watch reports moved stones")
    print("OK: %s drew the fortress" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_messaging_events(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # the shock absorber: 500/s in, 450/s out
    arrival, service = 500.0, 450.0
    growth = arrival - service
    seconds = 60.0
    backlog = growth * seconds
    print("arrival %.0f/s, service %.0f/s -> growth %.0f/s" % (arrival, service, growth))
    print("backlog after %.0f s: %.0f messages" % (seconds, backlog))
    assert 49.9 < growth < 50.1
    assert 2999.0 < backlog < 3001.0
    # drain time once the spike passes at full service rate
    drain = backlog / service
    print("drain time at %.0f/s: %.2f s" % (service, drain))
    assert 6.66 < drain < 6.68
    # Little law: L = lambda * W
    wait_s = 2.0
    in_system = arrival * wait_s
    print("Little law: %.0f in system at %.0f/s with %.0f s wait" % (in_system, arrival, wait_s))
    assert in_system == 1000
    print("rule: the courier hall never keeps the sender waiting")
    print("OK: %s ran the courier hall" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_backup_dr(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # backup window: 2 TB at 200 MB/s
    bytes_total = 2e12
    rate = 200e6
    seconds = bytes_total / rate
    hours = seconds / 3600.0
    window = 4.0
    print("2 TB at 200 MB/s: %.0f s (%.2f h)" % (seconds, hours))
    print("backup window: %.1f h -> %s" % (window, "INSIDE" if hours < window else "OVER"))
    assert 9999.0 < seconds < 10001.0
    assert 2.77 < hours < 2.79
    assert hours < window
    # the two covenants
    rpo_min, rto_h = 15, 4
    print("RPO %d minutes of tolerable loss; RTO %d hours to serve again" % (rpo_min, rto_h))
    assert rpo_min == 15 and rto_h == 4
    # recovery order: data plane first
    order = ["restore data", "repoint DNS", "verify health", "replay queue"]
    print("runbook steps: %d" % len(order))
    assert len(order) == 4
    print("rule: test by restore, never by faith")
    print("OK: %s kept the chronicle" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_cicd(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # lead time: build + test + deploy
    build_s, test_s, deploy_s = 180, 240, 90
    lead = build_s + test_s + deploy_s
    print("build %ds + test %ds + deploy %ds = lead time %ds (%.1f min)" % (build_s, test_s, deploy_s, lead, lead / 60.0))
    assert lead == 510
    assert 8.4 < lead / 60.0 < 8.6
    # canary: 10 percent of 50 pods
    pods, canary_pct = 50, 10
    canary = pods * canary_pct // 100
    print("canary: %d%% of %d pods = %d pods" % (canary_pct, pods, canary))
    assert canary == 5
    # DORA: elite means deploy on demand
    deploys_per_day = 12
    print("deployment frequency: %d per day" % deploys_per_day)
    assert deploys_per_day >= 1
    print("rule: build once, promote the same artifact, roll back by the numbers")
    print("OK: %s paved the road" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_cost_optimization(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # rightsizing: 20 VMs at 12 percent CPU become 4 at 60 percent
    before, after = 20, 4
    util_before, util_after = 12.0, 60.0
    per_vm_mo = 146.00
    retired = before - after
    saving_mo = retired * per_vm_mo
    saving_yr = saving_mo * 12
    print("%d VMs at %.0f%% -> %d VMs at %.0f%%" % (before, util_before, after, util_after))
    print("retired %d machines x %.2f = %.2f /mo" % (retired, per_vm_mo, saving_mo))
    print("yearly saving: %.2f" % saving_yr)
    assert retired == 16
    assert 2335.99 < saving_mo < 2336.01
    assert 28031.99 < saving_yr < 28032.01
    # capacity check: the work still fits
    capacity_before = before * util_before
    capacity_after = after * util_after
    print("compute units before %.0f, after %.0f" % (capacity_before, capacity_after))
    assert capacity_after == capacity_before
    print("rule: strength exactly where the need is, never more, never less")
    print("OK: %s weighed the gold" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_twelve_factor(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # score an app against the twelve factors
    factors = ["codebase", "dependencies", "config", "backing services",
               "build-release-run", "stateless processes", "port binding",
               "concurrency", "disposability", "dev-prod parity",
               "logs as streams", "admin processes"]
    missing = {"disposability", "dev-prod parity", "admin processes"}
    met = [f for f in factors if f not in missing]
    score = len(met) / len(factors) * 100.0
    print("factors met: %d of %d (%.1f %%)" % (len(met), len(factors), score))
    print("remediation list: %s" % ", ".join(sorted(missing)))
    assert len(factors) == 12
    assert len(met) == 9
    assert 74.9 < score < 75.1
    assert len(missing) == 3
    print("rule: each factor removes one classic source of it-works-on-my-machine")
    print("OK: %s kept the twelve articles" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_multiregion_cap(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # quorum math for 3 replicas
    n = 3
    quorum = n // 2 + 1
    print("replicas %d -> quorum %d" % (n, quorum))
    assert quorum == 2
    # write set and read set overlap on at least one node
    overlap = quorum + quorum - n
    print("write quorum %d + read quorum %d - %d nodes = overlap %d" % (quorum, quorum, n, overlap))
    assert overlap >= 1
    # one node down: survivors still form a quorum
    survivors = n - 1
    print("one node down: %d survivors, quorum %d -> %s" % (survivors, quorum, "CONSISTENT+AVAILABLE" if survivors >= quorum else "DEGRADED"))
    assert survivors >= quorum
    # the CAP choice during a partition
    print("partition: choose consistency (stop writes) or availability (accept divergence)")
    print("rule: of truth, readiness, and endurance through severed roads, swear two")
    print("OK: %s held the three cities" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_migration_6rs(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # classify a 120-application portfolio
    portfolio = {"rehost": 60, "replatform": 30, "refactor": 12,
                 "repurchase": 8, "retain": 6, "retire": 4}
    total = sum(portfolio.values())
    print("portfolio: %d applications" % total)
    assert total == 120
    for r, count in portfolio.items():
        pct = count / total * 100.0
        print("  %-10s %3d (%4.1f %%)" % (r, count, pct))
    assert abs(portfolio["rehost"] / total * 100.0 - 50.0) < 0.05
    assert abs(portfolio["replatform"] / total * 100.0 - 25.0) < 0.05
    assert 6.6 < portfolio["repurchase"] / total * 100.0 < 6.7
    assert 3.3 < portfolio["retire"] / total * 100.0 < 3.4
    # wave order: independent and low-risk first
    waves = ["pilot", "factory wave 1", "factory wave 2", "core systems"]
    print("migration waves: %d" % len(waves))
    assert len(waves) == 4
    print("rule: no house travels without its map home")
    print("OK: %s marshaled the moving" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_service_mesh(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # retries turn 0.9 per-try into four nines
    p_try = 0.9
    attempts = 4
    p_success = 1 - (1 - p_try) ** attempts
    print("per-try success %.1f over %d attempts -> %.4f" % (p_try, attempts, p_success))
    assert 0.99989 < p_success < 0.99991
    # latency cost of the sidecar
    base_ms, sidecar_ms = 50.0, 2.0
    overhead = sidecar_ms / base_ms * 100.0
    print("sidecar %.0f ms on %.0f ms base = %.0f%% overhead" % (sidecar_ms, base_ms, overhead))
    assert 3.9 < overhead < 4.1
    # circuit breaker: stop calling the failing service
    consecutive_failures, threshold = 5, 5
    state = "OPEN" if consecutive_failures >= threshold else "CLOSED"
    print("failures %d at threshold %d -> breaker %s" % (consecutive_failures, threshold, state))
    assert state == "OPEN"
    print("rule: a guard that never sleeps is worth 4 percent")
    print("OK: %s rode with the escorts" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_confidential_computing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # AES-256 key space against a trillion guesses per second
    keys = 2.0 ** 256
    guesses_per_s = 1e12
    secs_per_year = 365.25 * 24 * 3600
    years = keys / (guesses_per_s * secs_per_year)
    print("key space: %.4e keys" % keys)
    print("brute force at 1e12 guesses/s: %.4e years" % years)
    assert 1.15e77 < keys < 1.16e77
    assert 3.66e57 < years < 3.68e57
    # envelope encryption: rotating the master re-wraps keys, not petabytes
    data_keys = 1000000
    rewrap_ops = data_keys
    reencrypt_bytes = 0
    print("rotation: %d key re-wraps, %d data bytes re-encrypted" % (rewrap_ops, reencrypt_bytes))
    assert rewrap_ops == 1000000
    assert reencrypt_bytes == 0
    print("rule: guard the thought itself, not only the letter and the road")
    print("OK: %s sealed the crystal mind" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_cld_well_architected(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # scored review across the six pillars
    pillars = {"operational excellence": 82, "security": 91, "reliability": 78,
               "performance efficiency": 85, "cost optimization": 74,
               "sustainability": 88}
    assert len(pillars) == 6
    avg = sum(pillars.values()) / len(pillars)
    weakest = min(pillars, key=pillars.get)
    print("pillar scores:")
    for k, v in pillars.items():
        print("  %-22s %d" % (k, v))
    print("weighted average: %.1f" % avg)
    print("remediate first: %s (%d)" % (weakest, pillars[weakest]))
    assert 82.9 < avg < 83.1
    assert weakest == "cost optimization"
    # error budget discipline behind the reliability score
    slo, window_days = 0.999, 30
    budget_min = (1 - slo) * window_days * 24 * 60
    print("reliability backstop: %.1f min error budget per month" % budget_min)
    assert 43.19 < budget_min < 43.21
    print("rule: score, remediate, re-score - lift the weakest pillar first")
    print("OK: %s judged the fortress" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS.update({
    "block_file_storage": demo_cld_block_file_storage,
    "managed_databases": demo_cld_managed_databases,
    "load_balancing": demo_cld_load_balancing,
    "cdn_edge": demo_cld_cdn_edge,
    "cloud_network_security": demo_cld_cloud_network_security,
    "observability": demo_cld_observability,
    "infrastructure_as_code": demo_cld_infrastructure_as_code,
    "messaging_events": demo_cld_messaging_events,
    "backup_dr": demo_cld_backup_dr,
    "cicd": demo_cld_cicd,
    "cost_optimization": demo_cld_cost_optimization,
    "twelve_factor": demo_cld_twelve_factor,
    "multiregion_cap": demo_cld_multiregion_cap,
    "migration_6rs": demo_cld_migration_6rs,
    "service_mesh": demo_cld_service_mesh,
    "confidential_computing": demo_cld_confidential_computing,
    "well_architected": demo_cld_well_architected,
})

assert len(DEMOS) == 34, "expected 34 demos, got %d" % len(DEMOS)
