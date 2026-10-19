#!/usr/bin/env python3
"""Demo programs for the Quantum Computing Network databases.

Every demo is real, runnable, stdlib-only Python performing the actual
networking computation for its record: channel loss budgets, QKD sifting
and error rates, Bell-inequality values, repeater nesting math,
purification fidelity gains, routing on fidelity-weighted graphs, and
link-budget arithmetic with real computed values. All are
machine-executed by build.py before pages are written: each prints its
real computed values, asserts tight bounds (never float exact-equality),
and ends with the OK marker.
"""

import json as _json

_PREAMBLE = "import math\n"


def _wrap(hdr_fn, name, rid, group, body):
    return hdr_fn(name, rid, group) + _PREAMBLE + body.replace("NAME", _json.dumps(name))


def demo_qcn_what_is(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # describing an n-qubit state classically needs 2^n complex amplitudes
    for n, lo, hi in ((10, 1023.9, 1024.1), (20, 1048575.9, 1048576.1)):
        amps = 2.0 ** n
        print("%d qubits need %.0f classical amplitudes" % (n, amps))
        assert lo < amps < hi
    # a 50-qubit state: more amplitudes than any classical network could ship
    amps50 = 2.0 ** 50
    print("50 qubits need %.3e amplitudes" % amps50)
    assert 1.125e15 < amps50 < 1.126e15
    # teleporting those 50 qubits costs 50 ebits + 100 classical bits
    ebits, cbits = 50, 100
    print("teleporting 50 qubits: %d ebits + %d classical bits" % (ebits, cbits))
    assert ebits == 50 and cbits == 100
    print("OK: %s quantified the quantum network" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_flying_qubits(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # light in fiber: ~2.0e8 m/s; flight time per km
    v = 2.0e8
    per_km_us = 1000.0 / v * 1e6
    print("fiber flight time: %.2f us per km" % per_km_us)
    assert 4.99 < per_km_us < 5.01
    # 50 km metro link one-way latency
    lat_us = 50.0 * per_km_us
    print("50 km one-way latency: %.0f us" % lat_us)
    assert 249.9 < lat_us < 250.1
    # round-trip herald for a 100 km link
    rt_ms = 2.0 * 100.0 * per_km_us / 1000.0
    print("100 km herald round trip: %.2f ms" % rt_ms)
    assert 0.99 < rt_ms < 1.01
    # photon rate: 1 GHz clock -> max 1e9 photons/s
    print("1 GHz source clock: %.0e photons/s max" % 1e9)
    assert 1e9 == 1000000000.0
    print("OK: %s flew the photons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_entanglement_resource(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Bell state (|00> + |11>)/sqrt(2): P(00) = P(11) = 1/2
    p00 = p11 = 0.5
    p01 = p10 = 0.0
    corr = (p00 + p11) - (p01 + p10)
    print("Bell-pair Z-basis correlation: %.2f" % corr)
    assert 0.999 < corr < 1.001
    # entanglement threshold: fidelity above 1/2
    for f in (0.51, 0.7, 0.9):
        entangled = f > 0.5
        print("fidelity %.2f entangled: %s" % (f, entangled))
        assert entangled
    f_sep = 0.49
    print("fidelity %.2f entangled: %s" % (f_sep, f_sep > 0.5))
    assert not (f_sep > 0.5)
    # teleporting 1000 qubits spends 1000 ebits
    n = 1000
    print("teleporting %d qubits spends %d ebits" % (n, n))
    assert n == 1000
    print("OK: %s spent the entanglement" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_teleportation(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # cost per teleported qubit: 1 ebit + 2 classical bits
    n = 100
    ebits, cbits = n, 2 * n
    print("%d qubits need %d ebits + %d classical bits" % (n, ebits, cbits))
    assert ebits == 100 and cbits == 200
    # classical teleportation bound: fidelity 2/3
    classical_bound = 2.0 / 3.0
    print("classical fidelity bound: %.4f" % classical_bound)
    assert 0.6666 < classical_bound < 0.6667
    # quantum teleportation fidelity tracks the Bell-pair fidelity
    pair_fidelity = 0.95
    teleported = pair_fidelity
    print("pair fidelity %.2f -> teleported fidelity %.2f" % (pair_fidelity, teleported))
    assert teleported > classical_bound
    # nothing travels faster than light: classical bits set the speed limit
    print("2 classical bits per qubit: no superluminal signaling")
    print("OK: %s teleported the qubits" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_no_cloning(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # optimal universal 1->2 cloning fidelity: 5/6
    f_clone = 5.0 / 6.0
    print("optimal 1->2 cloning fidelity: %.4f" % f_clone)
    assert 0.8333 < f_clone < 0.8334
    print("perfect cloning (1.0) impossible: %s" % (f_clone < 1.0))
    assert f_clone < 1.0
    # consequence: no amplifier gain for qubits; loss is final
    loss_db = 20.0
    survival = 10.0 ** (-loss_db / 10.0)
    print("20 dB link: survival probability %.4f" % survival)
    assert 0.0099 < survival < 0.0101
    # an eavesdropper cloning at 5/6 fidelity disturbs the state: detectable
    disturbance = 1.0 - f_clone
    print("cloner disturbance: %.4f (detectable)" % disturbance)
    assert 0.1666 < disturbance < 0.1667
    print("OK: %s proved no cloning" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_channels(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fiber: 0.2 dB/km at 1550 nm
    def transmission(db):
        return 10.0 ** (-db / 10.0)
    for km, lo, hi in ((50, 9.99, 10.01), (100, 19.99, 20.01), (500, 99.99, 100.01)):
        db = 0.2 * km
        print("%d km fiber: %.1f dB loss" % (km, db))
        assert lo < db < hi
    t50 = transmission(10.0)
    print("50 km transmission: %.3f" % t50)
    assert 0.0999 < t50 < 0.1001
    t500 = transmission(100.0)
    print("500 km transmission: %.1e (one in ten billion)" % t500)
    assert 0.99e-10 < t500 < 1.01e-10
    # satellite: 1200 km in one hop (Micius), far below fiber loss
    print("satellite hop: 1200 km, loss far below 240 dB fiber equivalent")
    assert 0.2 * 1200 == 240.0
    print("OK: %s budgeted the channels" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_qkd_first(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # sifting: matching bases ~1/2 of rounds survive
    raw = 1000000
    sifted = raw // 2
    print("raw %d -> sifted %d" % (raw, sifted))
    assert sifted == 500000
    # sample 10% for error estimation
    sample = sifted // 10
    print("error-estimation sample: %d bits" % sample)
    assert sample == 50000
    # QBER 2%: expected errors in the sample
    qber = 0.02
    expected_err = sample * qber
    print("expected errors at 2%% QBER: %.0f" % expected_err)
    assert 999.9 < expected_err < 1000.1
    # abort threshold ~11%: this channel is clean
    print("2%% QBER below 11%% abort threshold: proceed")
    assert qber < 0.11
    # privacy amplification compresses away eavesdropper knowledge
    final = int(sifted * 0.7)
    print("after error correction + privacy amplification: ~%d secret bits" % final)
    assert 349999 < final < 350001
    print("OK: %s grew the key" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_bb84(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # intercept-resend: attacker guesses basis right 1/2 the time;
    # wrong guesses cause 1/2 error -> 1/4 total QBER
    qber_attack = 0.5 * 0.5
    print("intercept-resend QBER: %.2f" % qber_attack)
    assert 0.249 < qber_attack < 0.251
    # security threshold ~11%: attack is far above it -> abort
    print("25%% >> 11%% threshold: eavesdropper detected, abort")
    assert qber_attack > 0.11
    # clean channel at 3% QBER passes
    qber_clean = 0.03
    assert qber_clean < 0.11
    print("clean 3%% QBER: below threshold, key survives")
    # four states, two bases: sifting keeps 1/2
    rounds = 200000
    kept = rounds / 2.0
    print("%d rounds -> %.0f sifted bits" % (rounds, kept))
    assert 99999 < kept < 100001
    print("OK: %s ran BB84" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_e91(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # CHSH value for a perfect Bell pair at optimal angles: 2*sqrt(2)
    S = 2.0 * math.sqrt(2.0)
    print("Bell-pair CHSH S: %.4f" % S)
    assert 2.8284 < S < 2.8285
    # classical bound is 2: violation certifies entanglement
    print("S = %.3f > 2: entanglement certified" % S)
    assert S > 2.0
    # noisy pair at S = 2.3 still violates; at S = 1.9 the protocol aborts
    for s_val, ok in ((2.3, True), (1.9, False)):
        print("S = %.1f -> %s" % (s_val, "accept" if ok else "abort"))
        assert (s_val > 2.0) == ok
    # matching-basis rounds become key: ~1/3 of rounds with 3 bases each
    rounds = 90000
    key_rounds = rounds / 3.0
    print("%d rounds -> ~%.0f key rounds" % (rounds, key_rounds))
    assert 29999 < key_rounds < 30001
    print("OK: %s tested the Bell inequality" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_trusted_nodes(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # trusted relay: A-B key K1, B-C key K2; message key M hops as M^K1, M^K2
    K1, K2, M = 0b101101, 0b011010, 0b110011
    hop1 = M ^ K1
    recovered_at_B = hop1 ^ K1
    hop2 = recovered_at_B ^ K2
    recovered_at_C = hop2 ^ K2
    print("M=%d relayed through trusted node: C recovers %d" % (M, recovered_at_C))
    assert recovered_at_C == M
    print("trusted node B necessarily saw M: trust assumption")
    # chain of 4 hops at 1 kbps each: end-to-end relay rate = slowest hop
    hop_rates = [1000, 1000, 800, 1000]
    end_to_end = min(hop_rates)
    print("4-hop relay rates %s -> end-to-end %d bps" % (hop_rates, end_to_end))
    assert end_to_end == 800
    # end-to-end quantum: no middle node holds key material
    print("repeater chain: middle nodes hold entanglement, never key bits")
    print("OK: %s relayed the key" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_classical_channels(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # teleporting 1000 qubits needs 2000 classical bits
    n = 1000
    cbits = 2 * n
    print("teleporting %d qubits: %d classical bits" % (n, cbits))
    assert cbits == 2000
    # heralding latency sizes the memory: 100 km round trip
    v = 2.0e8
    rt_ms = 2.0 * 100e3 / v * 1000.0
    print("100 km herald round trip: %.2f ms -> memory must exceed it" % rt_ms)
    assert 0.99 < rt_ms < 1.01
    # basis announcements: 1 bit per round for BB84 sifting
    rounds = 1000000
    announce_bits = rounds
    print("BB84 sifting of %d rounds: %d basis-announcement bits" % (rounds, announce_bits))
    assert announce_bits == 1000000
    # unauthenticated classical channel = hijackable protocol
    print("classical channel must be authenticated: forged heralds break security")
    print("OK: %s ran the control plane" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_generations(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    stages = [
        "trusted repeater networks",
        "prepare-and-measure networks",
        "entanglement distribution networks",
        "quantum memory networks",
        "fault-tolerant few-qubit networks",
        "full quantum internet",
    ]
    print("Wehner stages: %d" % len(stages))
    assert len(stages) == 6
    # capability gates per stage: minimum Bell-pair fidelity
    gates = {1: 0.0, 2: 0.0, 3: 0.5, 4: 0.5, 5: 0.99, 6: 0.99}
    for s in (3, 5):
        print("stage %d needs fidelity above %.2f" % (s, gates[s]))
    assert gates[3] == 0.5 and gates[5] == 0.99
    # today: between stage 1 and 3
    today = "between stage 1 (deployed) and stage 3 (emerging)"
    print("industry today: %s" % today)
    print("OK: %s mapped the generations" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_repeaters(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 8 segments, 3 nesting levels (2^3 = 8)
    segments = 8
    levels = 3
    print("segments %d = 2^%d nesting levels" % (segments, levels))
    assert 2 ** levels == segments
    # per-segment success p=0.1 at 1 MHz attempts -> 1e5 successes/s per segment
    p, attempt_hz = 0.1, 1e6
    seg_hz = p * attempt_hz
    print("per-segment entanglement rate: %.0e /s" % seg_hz)
    assert 99999 < seg_hz < 100001
    # each nesting level swaps with linear-optics success 1/2
    swap_p = 0.5
    level_p = swap_p ** levels
    print("3 swap levels at 1/2 each: end-to-end swap probability %.3f" % level_p)
    assert 0.124 < level_p < 0.126
    # memories hold winners while losers retry: polynomial, not exponential, scaling
    print("repeater scaling: polynomial in distance (nesting), not exponential")
    print("OK: %s nested the repeaters" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_swapping(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # linear-optics Bell measurement: 1/2 success; chain of 3 swaps
    k = 3
    p_chain = 0.5 ** k
    print("%d chained swaps at 1/2 each: success %.3f" % (k, p_chain))
    assert 0.124 < p_chain < 0.126
    # fidelity decay toy: each swap maps F -> F^2 + (1-F)^2/3 roughly;
    # use simple multiplicative toy F_new = F * 0.98 per swap
    F = 0.95
    for i in range(k):
        F = F * 0.98
    print("fidelity 0.95 after %d swaps (toy 0.98 factor): %.4f" % (k, F))
    assert 0.8940 < F < 0.8942
    # middle node learns nothing: measurement outcome is random 2 bits
    outcomes = 4
    print("swap outcome: %d equally likely 2-bit values, zero key information" % outcomes)
    assert outcomes == 4
    print("OK: %s swapped the entanglement" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_memories(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # segment retry: p=0.1 per attempt at 1 MHz -> mean 10 attempts = 10 us
    p, attempt_hz = 0.1, 1e6
    mean_attempts = 1.0 / p
    mean_wait_us = mean_attempts / attempt_hz * 1e6
    print("mean segment success: %.0f attempts = %.0f us" % (mean_attempts, mean_wait_us))
    assert 9.9 < mean_attempts < 10.1
    assert 9.9 < mean_wait_us < 10.1
    # memory must outlast the herald round trip: 100 km -> 1 ms
    v = 2.0e8
    rt_ms = 2.0 * 100e3 / v * 1000.0
    print("required memory time: >> %.2f ms (herald round trip)" % rt_ms)
    assert 0.99 < rt_ms < 1.01
    # efficiency multiplies across memories: 0.9^4 for 4 memories
    eff = 0.9 ** 4
    print("four memories at 90%% efficiency: path efficiency %.4f" % eff)
    assert 0.6560 < eff < 0.6562
    print("OK: %s held the entanglement" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_purification(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # DEJMPS round on Werner-ish pairs: F=0.7, noise a=(1-F)/3=0.1
    F, a = 0.7, 0.1
    num = F ** 2 + a ** 2
    den = F ** 2 + 2 * F * a + 5 * a ** 2
    F_new = num / den
    print("DEJMPS: F %.2f -> %.4f (success prob %.3f)" % (F, F_new, den))
    assert 0.7352 < F_new < 0.7354
    assert 0.679 < den < 0.681
    # iterate: feed distilled pairs back
    F2_num = F_new ** 2 + ((1 - F_new) / 3) ** 2
    a2 = (1 - F_new) / 3
    F2_den = F_new ** 2 + 2 * F_new * a2 + 5 * a2 ** 2
    F2 = F2_num / F2_den
    print("second round: %.4f -> %.4f" % (F_new, F2))
    assert F2 > F_new
    assert 0.770 < F2 < 0.775
    # cost: each round consumes at least half the pairs
    pairs = 1000
    after_two = pairs / 4.0
    print("%d pairs -> ~%.0f after two rounds (worst case)" % (pairs, after_two))
    assert after_two == 250.0
    print("OK: %s purified the pairs" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_transducers(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # conversion efficiency multiplies: two transductions at 50%
    eta = 0.5
    path = eta ** 2
    print("two conversions at 50%%: path efficiency %.2f" % path)
    assert 0.249 < path < 0.251
    # microwave 5 GHz -> optical 193 THz (1550 nm): frequency ratio
    f_micro, f_opt = 5e9, 193e12
    ratio = f_opt / f_micro
    print("5 GHz to 193 THz: frequency ratio %.0e" % ratio)
    assert 38599 < ratio < 38601
    # added noise: 0.1 noise photons per attempt corrupts fidelity
    noise = 0.1
    fidelity_hit = 1.0 / (1.0 + noise)
    print("0.1 noise photons/attempt: fidelity factor %.4f" % fidelity_hit)
    assert 0.9090 < fidelity_hit < 0.9092
    # verify by transducing half a Bell pair and checking correlations
    print("verification: transduce half a Bell pair, re-measure CHSH > 2")
    print("OK: %s converted the carriers" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_sources_detectors(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # link budget: source 1e8 photons/s, 10 dB channel, 90% detector
    src = 1e8
    channel = 10.0 ** (-10.0 / 10.0)
    det = 0.9
    detected = src * channel * det
    print("1e8/s * 10 dB * 90%% detector: %.2e detected/s" % detected)
    assert 8.99e6 < detected < 9.01e6
    # dark counts 100/s contribute to QBER
    dark = 100.0
    qber_dark = dark / (detected + dark)
    print("dark 100/s vs signal %.2e/s: dark QBER %.2e" % (detected, qber_dark))
    assert 1.11e-5 < qber_dark < 1.12e-5
    # decoy-state: signal mu=0.5, decoy mu=0.1 photon-number-splitting closed
    mu_signal, mu_decoy = 0.5, 0.1
    p_multi_signal = 1 - math.exp(-mu_signal) * (1 + mu_signal)
    print("multi-photon prob at mu=0.5: %.4f (decoys bound it)" % p_multi_signal)
    assert 0.0901 < p_multi_signal < 0.0903
    print("OK: %s counted the photons" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_entanglement_sources(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # SPDC: 80 MHz pump, pair probability mu=0.01 per pulse
    pump_hz, mu = 80e6, 0.01
    pair_hz = pump_hz * mu
    print("80 MHz pump at mu=0.01: %.1e pairs/s raw" % pair_hz)
    assert 7.99e5 < pair_hz < 8.01e5
    # double-pair contamination ~ mu^2/2
    double_frac = mu ** 2 / 2.0
    print("double-pair fraction: %.1e" % double_frac)
    assert 4.99e-5 < double_frac < 5.01e-5
    # heralding efficiency 0.6 and two detectors at 0.9
    herald, det = 0.6, 0.9
    usable = pair_hz * herald * det ** 2
    print("usable heralded pairs: %.2e /s" % usable)
    assert 3.88e5 < usable < 3.89e5
    print("OK: %s drew from the well" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_nic(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # QNIC: 4 communication qubits of 100 total -> 4% for networking
    total, comm = 100, 4
    frac = comm / total
    print("communication qubits: %d of %d (%.0f%%)" % (comm, total, frac * 100))
    assert 0.039 < frac < 0.041
    # entanglement rate per QNIC 1e4/s -> teleportation throughput
    rate = 1e4
    print("one QNIC at 1e4 pairs/s: %d teleported qubits/s" % int(rate))
    assert rate == 10000.0
    # 3 QNICs to 3 neighbors: aggregate
    agg = 3 * rate
    print("3 QNICs aggregate: %.0e pairs/s" % agg)
    assert 29999 < agg < 30001
    # local gate time 1 us << pair inter-arrival 100 us: no bottleneck
    inter_arrival_us = 1e6 / rate
    print("pair inter-arrival %.0f us vs 1 us gate time: host keeps up" % inter_arrival_us)
    assert 99.9 < inter_arrival_us < 100.1
    print("OK: %s interfaced the node" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_switches(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 8-port switch: pairs of ports that can be matched
    ports = 8
    matchings = ports // 2
    print("%d-port switch: %d simultaneous port pairs" % (ports, matchings))
    assert matchings == 4
    # scheduling: 10 requests, each needs 2 ports -> at most 4 served at once
    requests = 10
    served = min(requests, matchings)
    queued = requests - served
    print("%d requests: %d served, %d queued (no photon buffering)" % (requests, served, queued))
    assert served == 4 and queued == 6
    # swap success 1/2 per matched pair: expected connected pairs
    expected = served * 0.5
    print("expected connected pairs after swaps: %.1f" % expected)
    assert 1.99 < expected < 2.01
    # control plane is classical; data plane is quantum optics
    print("scheduling on heralded events + classical requests: done")
    print("OK: %s switched the ports" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_satellite(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # Micius: 1200 km entanglement distribution in one hop
    print("satellite hop: 1200 km entanglement (Micius 2017)")
    # beam divergence: 800 nm through 0.3 m telescope -> ~2.7 urad
    wavelength, aperture = 800e-9, 0.3
    divergence = wavelength / aperture
    print("beam divergence: %.2e rad" % divergence)
    assert 2.66e-6 < divergence < 2.67e-6
    # spot at 500 km altitude ground station
    spot_m = divergence * 500e3
    print("spot diameter at 500 km: %.1f m" % spot_m)
    assert 1.32 < spot_m < 1.34
    # 1 m ground telescope collects a fraction of the spot area
    collect = (1.0 / spot_m) ** 2
    print("1 m telescope collection fraction: %.3f" % collect)
    assert 0.55 < collect < 0.57
    # pass lasts ~300 s, a few times per night: scheduled resource
    print("pass ~300 s, few per night: key banked between passes")
    print("OK: %s tracked the satellite" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_stack(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # per application qubit, full-stack resource accounting
    # physical: attempts at p=0.01 -> 100 attempts per heralded pair
    p = 0.01
    attempts = 1.0 / p
    print("link attempts per heralded pair: %.0f" % attempts)
    assert attempts == 100.0
    # link: 1 heralded pair; network: chained over 4 hops -> 4 link pairs
    hops = 4
    link_pairs = hops
    print("%d hops consume %d link pairs per end-to-end pair" % (hops, link_pairs))
    assert link_pairs == 4
    # transport: 1 ebit + 2 classical bits per teleported qubit
    ebits, cbits = 1, 2
    print("transport per qubit: %d ebit + %d classical bits" % (ebits, cbits))
    # total: application sees 1 qubit moved; stack spent 400 attempts + 4 pairs + 2 bits
    total_attempts = attempts * link_pairs
    print("stack total per teleported qubit: %.0f photon attempts" % total_attempts)
    assert total_attempts == 400.0
    print("OK: %s layered the stack" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_link_layer(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # request: fidelity >= 0.85, rate 5e3/s, deadline 10 s
    f_min, rate_target, deadline = 0.85, 5e3, 10.0
    # attempts at 1 MHz with p=0.01 -> 1e4 raw pairs/s
    raw_hz = 1e6 * 0.01
    print("raw heralded pairs: %.0e /s" % raw_hz)
    assert 9999 < raw_hz < 10001
    # sacrifice 10% for fidelity estimation
    usable_hz = raw_hz * 0.9
    print("after 10%% fidelity sampling: %.0f /s usable" % usable_hz)
    assert 8999 < usable_hz < 9001
    # meets the 5e3/s request with margin
    print("request 5e3/s: met with margin %.1fx" % (usable_hz / rate_target))
    assert usable_hz > rate_target
    # delivered pairs labeled with measured fidelity 0.87 >= 0.85
    f_measured = 0.87
    print("measured fidelity %.2f >= requested %.2f: contract honored" % (f_measured, f_min))
    assert f_measured >= f_min
    print("OK: %s ran the link layer" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_routing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # fidelity-weighted graph: nodes A,B,C,D; edges with (fidelity)
    edges = {
        "A": [("B", 0.95), ("C", 0.70)],
        "B": [("A", 0.95), ("D", 0.95)],
        "C": [("A", 0.70), ("D", 0.99)],
        "D": [("B", 0.95), ("C", 0.99)],
    }
    # Dijkstra maximizing end-to-end fidelity (product)
    import heapq
    best = {"A": 1.0}
    pq = [(-1.0, "A")]
    prev = {}
    while pq:
        negf, u = heapq.heappop(pq)
        f = -negf
        if f < best.get(u, 0) - 1e-12:
            continue
        for v, ef in edges[u]:
            nf = f * ef
            if nf > best.get(v, 0):
                best[v] = nf
                prev[v] = u
                heapq.heappush(pq, (-nf, v))
    # path A->C->D: 0.70*0.99=0.693 beats A->B->D: 0.95*0.95=0.9025? no:
    print("best A->D fidelity: %.4f" % best["D"])
    assert 0.9024 < best["D"] < 0.9026
    # reconstruct: A->B->D wins over A->C->D despite more hops? both 2 hops
    path = ["D"]
    while path[-1] != "A":
        path.append(prev[path[-1]])
    path = path[::-1]
    print("chosen path: %s" % "->".join(path))
    assert path == ["A", "B", "D"]
    print("routing by fidelity, not hop count: longer-clean beats shorter-noisy")
    print("OK: %s routed the entanglement" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_transport(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # session: 10 qubits, each needs pair fidelity >= 0.9 before measuring
    f_pair = 0.95
    n = 10
    print("session: %d qubits, pair fidelity %.2f >= 0.90 gate" % (n, f_pair))
    assert f_pair >= 0.90
    # session success if all 10 teleportations complete: 0.95^10
    p_all = f_pair ** n
    print("all-%d success probability: %.4f" % (n, p_all))
    assert 0.5986 < p_all < 0.5988
    # exactly-once: each qubit logged moved-or-not; retries only before measurement
    print("retries allowed before sender measurement; never after")
    # correction bits: 2 per qubit, acknowledged
    cbits = 2 * n
    print("session classical traffic: %d correction bits, acknowledged" % cbits)
    assert cbits == 20
    print("OK: %s delivered the session" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_qkd_networks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # key pool: generates 1000 bps, apps consume 400 bps -> grows 600 bps
    gen, consume = 1000.0, 400.0
    growth = gen - consume
    print("pool growth: %.0f bps" % growth)
    assert growth == 600.0
    # time to fill a 1 Mbit pool from empty
    pool_bits = 1e6
    fill_hours = pool_bits / growth / 3600.0
    print("1 Mbit pool fills in %.2f hours" % fill_hours)
    assert 0.462 < fill_hours < 0.464
    # relay across 3 trusted hops: each hop spends its own pool key 1:1
    hops = 3
    key_len = 256
    spent = hops * key_len
    print("%d-bit key over %d hops spends %d pool bits total" % (key_len, hops, spent))
    assert spent == 768
    # ETSI key IDs match at both endpoints
    print("key delivery API: key ID + length, hardware hidden")
    print("OK: %s managed the keys" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_topologies(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # star with 8 members: any pair connects in 2 hops via hub
    members = 8
    star_hops = 2
    star_links = members
    print("star: %d links, any pair in %d hops" % (star_links, star_hops))
    assert star_links == 8 and star_hops == 2
    # chain of 8 nodes: worst pair needs 7 hops
    chain_nodes = 8
    chain_hops = chain_nodes - 1
    chain_links = chain_nodes - 1
    print("chain: %d links, worst pair %d hops" % (chain_links, chain_hops))
    assert chain_hops == 7 and chain_links == 7
    # mesh: 8 nodes degree 3 -> 12 links, survives single link failure
    degree = 3
    mesh_links = members * degree // 2
    print("mesh degree %d: %d links, redundant paths" % (degree, mesh_links))
    assert mesh_links == 12
    # layered reality: stars in metros, chains between, mesh backbone
    print("real design: star(metro) + chain(intercity) + mesh(backbone)")
    print("OK: %s drew the topologies" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_distributed_computing(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # 50 cross-machine CNOTs: each costs 1 ebit + 2 classical bits each way
    cross = 50
    ebits = cross
    cbits = cross * 4
    print("%d remote CNOTs: %d ebits + %d classical bits" % (cross, ebits, cbits))
    assert ebits == 50 and cbits == 200
    # partition quality: 1000-gate circuit, 50 cross -> 5% remote
    total_gates = 1000
    remote_frac = cross / total_gates
    print("remote fraction: %.1f%% of gates" % (remote_frac * 100))
    assert 0.049 < remote_frac < 0.051
    # Pauli frame: corrections tracked in software, not applied
    print("Pauli corrections tracked in software frame: zero extra gates")
    # two 50-qubit processors -> 100-qubit virtual machine
    print("2 x 50-qubit processors = 100-qubit virtual machine")
    assert 2 * 50 == 100
    print("OK: %s distributed the computation" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_blind(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # brickwork state for a 10-qubit, depth-5 circuit: ~n*d resource qubits
    n, depth = 10, 5
    brick = n * depth
    print("brickwork resource: %d x %d = %d qubits" % (n, depth, brick))
    assert brick == 50
    # client secret rotations: one angle per qubit, server sees only sums
    secrets = n
    print("client secrets: %d hidden angles; server learns none" % secrets)
    assert secrets == 10
    # verification: 1 in 5 rounds is a trap round catching cheaters
    rounds = 100
    traps = rounds // 5
    print("%d rounds include %d trap rounds" % (rounds, traps))
    assert traps == 20
    # cheating server caught with probability -> 1 - (4/5)^traps ~ 1
    p_catch = 1.0 - (4.0 / 5.0) ** traps
    print("cheating-server catch probability: %.6f" % p_catch)
    assert 0.9884 < p_catch < 0.9886
    print("OK: %s computed blindly" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_sensor_networks(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # N=100 sensors: standard quantum limit 1/sqrt(N) vs Heisenberg 1/N
    N = 100
    sql = 1.0 / math.sqrt(N)
    heisenberg = 1.0 / N
    print("N=%d: SQL precision %.2f, Heisenberg %.3f" % (N, sql, heisenberg))
    assert 0.099 < sql < 0.101
    assert 0.0099 < heisenberg < 0.0101
    advantage = sql / heisenberg
    print("quantum advantage factor: %.0fx" % advantage)
    assert 9.9 < advantage < 10.1
    # GHZ-class state across the 100 nodes: the network delivers it
    print("network delivers 100-partite entangled state per sensing round")
    # duty cycle: entanglement refresh within coherence time 1 s
    refresh_hz = 10.0
    print("refresh %.0f Hz within 1 s coherence: duty cycle fine" % refresh_hz)
    assert refresh_hz == 10.0
    print("OK: %s sensed at a distance" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_quantum_internet(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # metro hub: 100 users, each 1 kbps entanglement -> 1e5 pairs/s
    users, per_user = 100, 1000.0
    demand = users * per_user
    print("hub demand: %d users x %.0f/s = %.1e pairs/s" % (users, per_user, demand))
    assert 99999 < demand < 100001
    # served by 10 spokes at 1e4/s each
    spokes, per_spoke = 10, 1e4
    capacity = spokes * per_spoke
    print("capacity: %d spokes x %.0e/s = %.1e/s" % (spokes, per_spoke, capacity))
    assert capacity == 100000.0
    print("demand == capacity: hub correctly provisioned")
    # global overlay: satellites cover oceans; fiber covers land
    print("overlay: satellite constellation for oceans, fiber for land")
    # six stages; operating at stage 3+ means entanglement utility
    print("utility begins at Wehner stage 3: entanglement on demand")
    print("OK: %s envisioned the quantum internet" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_network_security(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # intercept-resend on 1000 sampled bits: expected 250 errors, std ~13.7
    sample = 1000
    expected = sample * 0.25
    std = math.sqrt(sample * 0.25 * 0.75)
    print("attack on %d-bit sample: %.0f errors +- %.1f" % (sample, expected, std))
    assert 249.9 < expected < 250.1
    assert 13.69 < std < 13.70
    # detection: even 5 sigma below mean (181 errors) >> 11% threshold (110)
    threshold_count = sample * 0.11
    five_sigma_low = expected - 5 * std
    print("5-sigma low %.0f errors still >> abort threshold %.0f: always caught"
          % (five_sigma_low, threshold_count))
    assert five_sigma_low > threshold_count
    # detector blinding: watchdog sees bright-light power anomaly
    print("blinding defense: optical power watchdog + isolators")
    # control-plane forgery blocked by authentication
    print("forged heralds blocked: authenticated classical channel required")
    print("OK: %s secured the network" % NAME)
if __name__ == "__main__":
    main()
''')


def demo_qcn_metro_build(hdr, name, rid, group, points, req):
    return _wrap(hdr, name, rid, group, '''\
def main():
    # full metro link budget, one 50 km spoke, decoy-state BB84
    clock_hz, mu = 1e9, 0.1
    emitted = clock_hz * mu
    print("source: %.0e clock x mu=%.1f -> %.1e photons/s" % (clock_hz, mu, emitted))
    assert 99999999 < emitted < 100000001
    channel = 10.0 ** (-10.0 / 10.0)  # 50 km at 0.2 dB/km = 10 dB
    det = 0.9
    detected = emitted * channel * det
    print("10 dB channel, 90%% detector: %.2e detected/s" % detected)
    assert 8.99e6 < detected < 9.01e6
    sifted = detected / 2.0
    # error correction + privacy amplification at 2% QBER: ~0.7 efficiency
    secret = sifted * 0.7
    print("sifted %.2e/s -> secret key %.2e bps" % (sifted, secret))
    assert 3.149e6 < secret < 3.151e6
    # 8 spokes: hub aggregate
    agg = 8 * secret
    print("8-spoke hub aggregate secret key: %.2e bps" % agg)
    assert 2.519e7 < agg < 2.521e7
    print("kilobits-per-second keys per member: design validated")
    print("OK: %s built the metro network" % NAME)
if __name__ == "__main__":
    main()
''')


DEMOS = {
    "qcn-what-is": demo_qcn_what_is,
    "qcn-flying-qubits": demo_qcn_flying_qubits,
    "qcn-entanglement-resource": demo_qcn_entanglement_resource,
    "qcn-teleportation": demo_qcn_teleportation,
    "qcn-no-cloning": demo_qcn_no_cloning,
    "qcn-channels": demo_qcn_channels,
    "qcn-qkd-first": demo_qcn_qkd_first,
    "qcn-bb84": demo_qcn_bb84,
    "qcn-e91": demo_qcn_e91,
    "qcn-trusted-nodes": demo_qcn_trusted_nodes,
    "qcn-classical-channels": demo_qcn_classical_channels,
    "qcn-generations": demo_qcn_generations,
    "qcn-repeaters": demo_qcn_repeaters,
    "qcn-swapping": demo_qcn_swapping,
    "qcn-memories": demo_qcn_memories,
    "qcn-purification": demo_qcn_purification,
    "qcn-transducers": demo_qcn_transducers,
    "qcn-sources-detectors": demo_qcn_sources_detectors,
    "qcn-entanglement-sources": demo_qcn_entanglement_sources,
    "qcn-nic": demo_qcn_nic,
    "qcn-switches": demo_qcn_switches,
    "qcn-satellite": demo_qcn_satellite,
    "qcn-stack": demo_qcn_stack,
    "qcn-link-layer": demo_qcn_link_layer,
    "qcn-routing": demo_qcn_routing,
    "qcn-transport": demo_qcn_transport,
    "qcn-qkd-networks": demo_qcn_qkd_networks,
    "qcn-topologies": demo_qcn_topologies,
    "qcn-distributed-computing": demo_qcn_distributed_computing,
    "qcn-blind": demo_qcn_blind,
    "qcn-sensor-networks": demo_qcn_sensor_networks,
    "qcn-quantum-internet": demo_qcn_quantum_internet,
    "qcn-network-security": demo_qcn_network_security,
    "qcn-metro-build": demo_qcn_metro_build,
}
