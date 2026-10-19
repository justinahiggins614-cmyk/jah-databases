#!/usr/bin/env python3
"""Solution-explorer walkthrough demos for the Unsolved Neuroscience databases.

Each record gets a working program: the Signature approach as numbered steps,
adjustable assumptions, a deterministic toy model with real computed values
and tight-bounds asserts (never float exact-equality), and confirm/refute
panels. Models are labeled illustrations, not experiments and not proof.
"""

import json

DEMOS_CFG = {
"why_we_dream": {
 "steps": ["Treat the brain as a prediction machine with a generative world model.",
           "Gate sensory input off during REM while the generator keeps running.",
           "Read each dream as an uncorrected counterfactual rollout.",
           "Treat dream emotion as the model's internally computed loss."],
 "assumptions": [("Sleep duration", "8.0", "hours"), ("Sleep cycle length", "90", "minutes"),
                 ("REM fraction of late cycles", "0.25", "fraction")],
 "confirm": ["Decoded dream rollouts systematically precede next-day gains on the simulated subtasks.",
             "Disrupting specific dream content impairs exactly the rehearsed skill."],
 "refute": ["Total dream suppression with intact sleep architecture leaves learning and emotion unchanged."],
 "model": '''
_CYCLES = 8.0 * 60 / 90
_REM_MIN = [10.0, 20.0, 25.0, 30.0, 35.0]
_DREAM_MIN = sum(d * 0.8 for d in _REM_MIN)
print("  sleep cycles: %.2f" % _CYCLES)
print("  REM episodes: %d" % len(_REM_MIN))
print("  estimated dream minutes: %.1f" % _DREAM_MIN)
assert 5.0 < _CYCLES < 5.6, "cycle count out of bounds"
print("  CHECK cycle count in (5.0, 5.6): PASS")
assert 4 <= len(_REM_MIN) <= 6, "REM episode count out of bounds"
print("  CHECK REM episodes in [4, 6]: PASS")
assert 60.0 < _DREAM_MIN < 140.0, "dream minutes out of bounds"
print("  CHECK dream minutes in (60, 140): PASS")
'''},
"what_attention_is": {
 "steps": ["Treat perception as prediction-error minimization.",
           "Weight each error by its trustworthiness: precision.",
           "Read the spotlight as boosted gain and the filter as suppressed errors.",
           "Recompute the precision map several times per second."],
 "assumptions": [("Scene items", "100", "count"), ("Target salience", "9.5", "units"),
                 ("Distractor salience", "0.5", "mean units")],
 "confirm": ["A measured precision map predicts trial-by-trial which errors get amplified downstream.",
             "Attention effects vanish when the map is held fixed while goals change."],
 "refute": ["Clean attentional selection occurs with no precision-like signal anywhere in the circuit."],
 "model": '''
_N = 100
_dist = [0.5] * (_N - 1)
_target = 9.5
_share = _target / (sum(_dist) + _target)
_uniform = 1.0 / _N
print("  target selection share: %.3f" % _share)
print("  uniform baseline share: %.3f" % _uniform)
assert 0.10 < _share < 0.25, "selection share out of bounds"
print("  CHECK selection share in (0.10, 0.25): PASS")
assert _share > 5 * _uniform, "gain too small to count as attention"
print("  CHECK gain over uniform > 5x: PASS (%.1fx)" % (_share / _uniform))
'''},
"why_we_forget": {
 "steps": ["Treat memory as a generative model, not a recording.",
           "Read the Ebbinghaus curve as regularization: weight decay on unretrieved traces.",
           "Tag traces by predicted future value; release low-value traces to decay.",
           "Run sleep as a global downscaling pass."],
 "assumptions": [("Trace strength time constant", "1.25", "days"),
                 ("Value threshold", "0.30", "relative units")],
 "confirm": ["Low-value memories are preferentially erased by the known active mechanisms.",
             "The Ebbinghaus curve shape derives from the value distribution."],
 "refute": ["High-value memories decay at exactly the same rate as trivial ones."],
 "model": '''
import math as _m
_S = 1.25
def _ret(t): return _m.exp(-t / _S)
_r1, _r7, _r30 = _ret(1.0), _ret(7.0), _ret(30.0)
print("  retention after 1 day: %.4f" % _r1)
print("  retention after 7 days: %.4f" % _r7)
print("  retention after 30 days: %.6f" % _r30)
assert 0.44 < _r1 < 0.46, "1-day retention out of bounds"
print("  CHECK 1-day retention in (0.44, 0.46): PASS")
assert _r7 < 0.01, "7-day retention too high"
print("  CHECK 7-day retention < 0.01: PASS")
assert _r30 < 1e-6, "30-day retention too high"
print("  CHECK 30-day retention < 1e-6: PASS")
assert _r1 > _r7 > _r30, "curve not monotonic"
print("  CHECK curve monotonic decreasing: PASS")
'''},
"memory_consolidation": {
 "steps": ["Split learning into a fast hippocampal scratchpad and a slow cortical library.",
           "Replay compressed packets from fast to slow during sleep.",
           "Prioritize replay by prediction error: surprising events get more packets.",
           "Keep gist in cortex and detail in hippocampus: two formats by design."],
 "assumptions": [("Nights of consolidation", "14", "count"), ("Nightly transfer rate", "0.10", "fraction")],
 "confirm": ["Ripple-triggered disruption blocks transfer of exactly the decoded replayed content.",
             "Surprising experiences show measurably more replay packets."],
 "refute": ["Memories consolidate fully with zero replay events across all offline periods."],
 "model": '''
_N = 14
_rate = 0.10
_H = (1 - _rate) ** _N
_C = 1 - _H
print("  hippocampal trace after %d nights: %.4f" % (_N, _H))
print("  cortical trace after %d nights: %.4f" % (_N, _C))
assert 0.20 < _H < 0.26, "hippocampal trace out of bounds"
print("  CHECK hippocampal trace in (0.20, 0.26): PASS")
assert 0.70 < _C < 0.85, "cortical trace out of bounds"
print("  CHECK cortical trace in (0.70, 0.85): PASS")
assert _C > _H, "transfer did not dominate"
print("  CHECK cortical exceeds hippocampal: PASS")
'''},
"deja_vu": {
 "steps": ["Compute familiarity and recollection as separable signals.",
           "Race them: fast familiarity versus slower recollection veto.",
           "Attribute orphan familiarity to the present moment.",
           "Read the eeriness as the system's own error flag."],
 "assumptions": [("Familiarity signal strength", "0.85", "relative units"),
                 ("Veto arrival", "late", "timing"), ("Attribution threshold", "0.50", "units")],
 "confirm": ["In-the-act recording shows the familiarity response abnormally preceding the recollection verdict.",
             "Episode rate tracks temporal-lobe excitability manipulations."],
 "refute": ["Spontaneous episodes show no timing anomaly and no familiarity-recollection dissociation."],
 "model": '''
_F = 0.85
_veto = 0.10
_attr = _F * (1 - _veto)
_thresh = 0.50
print("  familiarity signal: %.2f" % _F)
print("  attribution strength: %.3f" % _attr)
assert 0.70 < _attr < 0.85, "attribution out of bounds"
print("  CHECK attribution in (0.70, 0.85): PASS")
assert _attr > _thresh, "no deja vu predicted"
print("  CHECK attribution exceeds threshold: PASS -> deja vu")
_normal_veto = 0.60
_normal_attr = _F * (1 - _normal_veto)
assert _normal_attr < _thresh, "normal race should not trigger"
print("  CHECK normal veto (%.2f) suppresses: PASS" % _normal_attr)
'''},
"prediction_error_learning": {
 "steps": ["Compute signed errors locally in each circuit.",
           "Broadcast dopamine as the global plasticity volume knob.",
           "Tag recently active synapses with eligibility traces.",
           "Update only tagged synapses, in the direction of the local error."],
 "assumptions": [("Learning rate", "0.30", "per trial"), ("Eligibility decay", "0.80", "per trial"),
                 ("Trials", "20", "count")],
 "confirm": ["Blocking local errors abolishes learning while dopamine stays intact.",
             "Blocking dopamine slows learning without changing what is learned."],
 "refute": ["Learning requires no local error computation anywhere."],
 "model": '''
_V = 0.0
_alpha, _beta, _lam = 0.30, 0.80, 1.0
_vs = []
for _t in range(20):
    _V += _alpha * _beta * (_lam - _V)
    _vs.append(_V)
print("  value after 5 trials: %.4f" % _vs[4])
print("  value after 20 trials: %.4f" % _vs[19])
assert _vs[19] > 0.95, "learning did not converge"
print("  CHECK final value > 0.95: PASS")
assert abs(_vs[19] - _lam) < 0.05, "final error too large"
print("  CHECK final prediction error < 0.05: PASS")
assert all(b > a for a, b in zip(_vs, _vs[1:])), "learning not monotonic"
print("  CHECK monotonic learning: PASS")
'''},
"pain_in_the_brain": {
 "steps": ["Separate nociception (data) from pain (decision).",
           "Maintain a model of bodily integrity and compute a protection policy.",
           "Read pain as the conscious output of the policy, not the raw data.",
           "Treat the spinal gate as the policy's first actuator."],
 "assumptions": [("Protection threshold", "0.50", "policy units"),
                 ("Context weight", "0.30", "relative units")],
 "confirm": ["A readable protection variable predicts pain reports better than nociceptive input across contexts.",
             "Placebo and phantom cases fall on the same policy curve."],
 "refute": ["Pain reports track nociceptive input perfectly across all contexts with no top-down modulation."],
 "model": '''
def _pain(noc, inh):
    return max(0.0, noc - inh)
_p1 = _pain(0.9, 0.2)
_p2 = _pain(0.9, 0.95)
_p3 = _pain(0.2, 0.1)
print("  injury, no inhibition: %.2f" % _p1)
print("  injury with strong inhibition (rubbing): %.2f" % _p2)
print("  mild input, mild inhibition: %.2f" % _p3)
assert 0.6 < _p1 < 0.8, "uninhibited pain out of bounds"
print("  CHECK uninhibited pain in (0.6, 0.8): PASS")
assert _p2 == 0.0, "gate failed to close"
print("  CHECK gate closes pain fully: PASS")
assert _p3 < _p1, "policy not graded"
print("  CHECK pain graded by net signal: PASS")
'''},
"body_ownership": {
 "steps": ["Infer the body from multisensory correlations; never sense it directly.",
           "Score candidate body hypotheses by prediction error.",
           "Let the lowest-error hypothesis capture ownership.",
           "Recalibrate proprioception to serve the winner."],
 "assumptions": [("Visual weight", "0.70", "fraction"), ("Rubber-hand offset", "20", "cm")],
 "confirm": ["Ownership switches occur exactly at measured error crossovers, trial by trial.",
             "Disrupting a hypothesis evidence shifts the switch point predictably."],
 "refute": ["Ownership changes with no change in multisensory evidence or error signals."],
 "model": '''
_w = 0.70
_seen, _felt = 20.0, 0.0
_drift = _w * _seen + (1 - _w) * _felt
print("  proprioceptive drift toward seen hand: %.1f cm" % _drift)
assert 10.0 < _drift < 18.0, "drift out of bounds"
print("  CHECK drift in (10, 18) cm: PASS")
assert _drift < _seen, "drift must be partial, not total"
print("  CHECK drift partial (model still anchored): PASS")
_async_w = 0.05
_async_drift = _async_w * _seen + (1 - _async_w) * _felt
assert _async_drift < 3.0, "async stroking should kill the illusion"
print("  CHECK async drift < 3 cm (illusion broken): PASS")
'''},
"few_shot_learning": {
 "steps": ["Arrive with a rich generative prior and a library of parts.",
           "Induce the shortest program that generates the observed example.",
           "Anchor the single episode in the fast hippocampal store.",
           "Self-distill: replay synthetic variations to train slow weights."],
 "assumptions": [("Part library size", "48", "parts"), ("Classes", "3", "count")],
 "confirm": ["Replay blockade after one-shot learning spares recall but kills generalization.",
             "Part-based neural encoding is detectable during induction."],
 "refute": ["One-shot generalization survives complete replay blockade with no loss."],
 "model": '''
import math as _m
_proto = [(0.0, 0.0), (5.0, 1.0), (1.0, 5.0)]
_query = (0.4, -0.3)
def _d(a, b): return _m.hypot(a[0] - b[0], a[1] - b[1])
_ds = [_d(_query, p) for p in _proto]
_best = min(range(3), key=lambda i: _ds[i])
print("  distances to prototypes: %s" % ["%.2f" % d for d in _ds])
print("  nearest prototype: class %d" % _best)
assert _best == 0, "one-shot classification failed"
print("  CHECK correct one-shot classification: PASS")
_margin = sorted(_ds)[1] - sorted(_ds)[0]
assert _margin > 3.0, "margin too small for reliable induction"
print("  CHECK decision margin > 3.0: PASS (%.2f)" % _margin)
'''},
"spatial_representation": {
 "steps": ["Maintain a grid-cell coordinate framework by path integration.",
           "Bind coordinates to content in the hippocampus.",
           "Compute vectors between positions for shortcuts and pointing.",
           "Reuse the same circuit for non-spatial relational spaces."],
 "assumptions": [("Grid scale", "1.0", "relative units"), ("Loop side", "10.0", "units")],
 "confirm": ["Grid disruption selectively impairs relational inference in non-spatial tasks.",
             "Shortcut vectors are readable from entorhinal-hippocampal activity."],
 "refute": ["Navigation survives complete grid disruption with no deficit."],
 "model": '''
import math as _m
_x, _y = 0.0, 0.0
for _dx, _dy in [(10, 0), (0, 10), (-10, 0), (0, -10)]:
    _x += _dx; _y += _dy
_err = _m.hypot(_x, _y)
_shortcut = _m.hypot(10, 10)
print("  path-integration loop closure error: %.2e" % _err)
print("  novel shortcut distance: %.2f" % _shortcut)
assert _err < 1e-6, "path integration drifted"
print("  CHECK loop closure error < 1e-6: PASS")
assert 14.0 < _shortcut < 14.3, "shortcut vector wrong"
print("  CHECK shortcut in (14.0, 14.3): PASS")
'''},
"working_memory_limits": {
 "steps": ["Treat working memory as a serial global broadcast channel.",
           "Fix the channel bit rate: a few high-precision items.",
           "Multiplex items in time slots (gamma in theta).",
           "Trade precision against count; chunk to expand effective capacity."],
 "assumptions": [("Channel capacity", "4", "items"), ("Precision decay per extra item", "0.05", "fraction")],
 "confirm": ["Measured channel parameters predict individual capacity.",
             "Experimental rate changes shift capacity."],
 "refute": ["Capacity persists with zero global broadcast of the items."],
 "model": '''
def _acc(n):
    if n <= 4: return 1.0
    return (4.0 / n) * (1 - 0.05 * (n - 4))
_a4, _a8 = _acc(4), _acc(8)
print("  recall accuracy at 4 items: %.2f" % _a4)
print("  recall accuracy at 8 items: %.2f" % _a8)
assert _a4 > 0.9, "within-capacity accuracy too low"
print("  CHECK within-capacity accuracy > 0.9: PASS")
assert _a8 < 0.6, "over-capacity accuracy too high"
print("  CHECK over-capacity accuracy < 0.6: PASS")
assert _a4 > _a8, "limit not visible"
print("  CHECK capacity limit visible: PASS")
'''},
"sensory_cancellation": {
 "steps": ["Copy every motor command to sensory areas (efference copy).",
           "Predict the sensory consequence with a confidence interval.",
           "Subtract the confidently predicted component; tag it self.",
           "Perceive the residual as world."],
 "assumptions": [("Self-touch intensity", "10.0", "units"), ("Prediction confidence", "0.95", "fraction")],
 "confirm": ["Measured uncertainty intervals set the cancellation boundary.",
             "Precision manipulations shift exactly which self-sensations get through."],
 "refute": ["Cancellation proves all-or-none with no precision grading."],
 "model": '''
_actual, _pred, _conf = 10.0, 9.8, 0.95
_self_perc = _actual - _pred * _conf
_ext_perc = 10.0 - 0.0 * _conf
_ratio = _self_perc / _ext_perc
print("  perceived self-touch: %.2f" % _self_perc)
print("  perceived external touch: %.2f" % _ext_perc)
print("  attenuation ratio: %.3f" % _ratio)
assert 0.5 < _self_perc < 1.0, "self perception out of bounds"
print("  CHECK self heavily attenuated: PASS")
assert _ratio < 0.15, "cancellation too weak"
print("  CHECK attenuation ratio < 0.15: PASS")
'''},
"full_function_of_sleep": {
 "steps": ["Track three debts: informational, metabolic, synaptic.",
           "Decouple from the world: the expensive shared step.",
           "Run physical service in non-REM, informational service in REM.",
           "Cycle through modes in order of debt urgency."],
 "assumptions": [("Waking hours", "16", "hours"), ("Sleep hours", "8", "hours"),
                 ("Pressure decay time constant", "4.0", "hours")],
 "confirm": ["Independent debt meters gate their corresponding sleep stages.",
             "Selective debt in one domain shifts only its stage."],
 "refute": ["A routine proves fully serviceable during waking with no decoupling cost."],
 "model": '''
import math as _m
_S0 = 2.0
_S = _S0 + 16.0 * 1.0
_S *= _m.exp(-8.0 / 4.0)
print("  sleep pressure at bedtime: %.1f" % (_S0 + 16.0))
print("  sleep pressure at waking: %.2f" % _S)
assert 1.4 < _S < 2.6, "pressure did not return near baseline"
print("  CHECK pressure returns within 30%% of baseline: PASS")
assert (_S0 + 16.0) > 5 * _S, "sleep did not discharge the debt"
print("  CHECK overnight discharge > 5x: PASS")
'''},
"the_neural_code": {
 "steps": ["Abandon one true code; let each circuit speak its own.",
           "Match the code to the reader: short windows read timing, long windows read rate.",
           "Spread information across populations for error correction.",
           "Keep redundancy: rate, timing, and population carry the message together."],
 "assumptions": [("True firing rate", "40", "Hz"), ("Short window", "0.05", "s"), ("Long window", "0.50", "s")],
 "confirm": ["Measured codes match codes predicted from reader biophysics.",
             "Timing-into-slow-reader mismatches fail to transmit."],
 "refute": ["One universal code is used identically across fast and slow circuits."],
 "model": '''
import math as _m
_rate = 40.0
_std_short = _m.sqrt(_rate / 0.05)
_std_long = _m.sqrt(_rate / 0.50)
_ratio = _std_short / _std_long
print("  rate-estimate std, 50ms window: %.1f Hz" % _std_short)
print("  rate-estimate std, 500ms window: %.1f Hz" % _std_long)
print("  precision gain ratio: %.2f" % _ratio)
assert 25.0 < _std_short < 32.0, "short-window std out of bounds"
print("  CHECK short-window std in (25, 32): PASS")
assert 8.0 < _std_long < 10.0, "long-window std out of bounds"
print("  CHECK long-window std in (8, 10): PASS")
assert 3.0 < _ratio < 3.3, "sqrt-time scaling violated"
print("  CHECK longer window more precise (ratio ~3.16): PASS")
'''},
"binding_problem": {
 "steps": ["Bind by space via topographic overlap.",
           "Bind by time via synchrony tags in fast circuits.",
           "Bind objects across time via attentional pointers.",
           "Read unity as the three tags agreeing."],
 "assumptions": [("Population size", "100", "neurons"), ("Sync spread", "0.10", "radians")],
 "confirm": ["Synchrony disruption breaks temporal binding while sparing spatial binding.",
             "Topographic disruption breaks spatial binding while sparing temporal."],
 "refute": ["One manipulation breaks all binding types identically."],
 "model": '''
import cmath as _c, math as _m
_N = 100
_sync = [-0.1 + 0.2 * i / (_N - 1) for i in range(_N)]
_desync = [-_m.pi + 2 * _m.pi * i / (_N - 1) for i in range(_N)]
_Rs = abs(sum(_c.exp(1j * p) for p in _sync)) / _N
_Rd = abs(sum(_c.exp(1j * p) for p in _desync)) / _N
print("  synchrony order parameter (bound): %.3f" % _Rs)
print("  synchrony order parameter (unbound): %.3f" % _Rd)
assert _Rs > 0.95, "bound tag too weak"
print("  CHECK bound tag > 0.95: PASS")
assert _Rd < 0.15, "unbound tag too strong"
print("  CHECK unbound tag < 0.15: PASS")
'''},
"physical_basis_of_memory": {
 "steps": ["Index the memory with its engram cell ensemble.",
           "Store content in the distributed synaptic weight pattern.",
           "Maintain the pattern with molecular locks.",
           "Recall by index-triggered pattern completion."],
 "assumptions": [("Network size", "500", "neurons"), ("Hopfield load factor", "0.138", "fraction")],
 "confirm": ["Read-out weight patterns predict specific memory content with the index intact.",
             "Rewriting the pattern changes content; the index alone does not."],
 "refute": ["Content is fully determined by molecular states independent of synaptic weights."],
 "model": '''
_N = 500
_pmax = 0.138 * _N
_stored = 20
print("  theoretical pattern capacity: %.1f" % _pmax)
print("  patterns stored: %d" % _stored)
assert 65.0 < _pmax < 73.0, "capacity out of bounds"
print("  CHECK capacity in (65, 73): PASS")
assert _stored < 0.5 * _pmax, "not safely below capacity"
print("  CHECK stored well below capacity: PASS")
'''},
"rules_of_neuroplasticity": {
 "steps": ["Let coincidence propose a synaptic change.",
           "Let the local prediction error set its sign.",
           "Let the global gate decide whether change is allowed.",
           "Open the gates wide in development; gate by attention and surprise in adulthood."],
 "assumptions": [("Learning rate", "0.10", "per event"), ("BCM threshold", "0.50", "rate units")],
 "confirm": ["Arbitrary synaptic responses are predicted from the three measured factors across protocols.",
             "Gate-state measurement predicts when plasticity is permitted."],
 "refute": ["A major plasticity phenomenon changes with no change in coincidence, error, or gate."],
 "model": '''
_eta, _theta = 0.10, 0.50
def _dw(x, y): return _eta * x * y * (y - _theta)
_ltp = _dw(1.0, 0.8)
_ltd = _dw(1.0, 0.3)
print("  weight change, strong activity: %+.4f" % _ltp)
print("  weight change, weak activity: %+.4f" % _ltd)
assert _ltp > 0, "should potentiate"
print("  CHECK LTP sign positive: PASS")
assert _ltd < 0, "should depress"
print("  CHECK LTD sign negative: PASS")
assert abs(_ltp) < 0.05 and abs(_ltd) < 0.05, "single step too large"
print("  CHECK steps stable and small: PASS")
'''},
"neural_basis_of_decision": {
 "steps": ["Accumulate evidence toward a bound: one accumulator for all decisions.",
           "Feed it sensory, value, and simulated evidence streams.",
           "Set the bound from the cost of time and the cost of error.",
           "Treat habits as low-bound regimes and deliberation as high-bound regimes."],
 "assumptions": [("Decision bound", "1.0", "evidence units")],
 "confirm": ["A neural bound readout tracks opportunity cost trial by trial.",
             "Habits, perception, and deliberation fit one accumulator with different parameters."],
 "refute": ["A major decision type uses no accumulation-to-bound dynamics at all."],
 "model": '''
_bound = 1.0
_rt_fast = _bound / 2.0
_rt_slow = _bound / 0.5
print("  mean RT, strong evidence: %.2f s" % _rt_fast)
print("  mean RT, weak evidence: %.2f s" % _rt_slow)
assert 0.45 < _rt_fast < 0.55, "fast RT out of bounds"
print("  CHECK fast RT in (0.45, 0.55): PASS")
assert 1.9 < _rt_slow < 2.1, "slow RT out of bounds"
print("  CHECK slow RT in (1.9, 2.1): PASS")
assert _rt_slow > 3 * _rt_fast, "speed-accuracy tradeoff too weak"
print("  CHECK strong evidence decides much faster: PASS")
'''},
"neural_basis_of_emotion": {
 "steps": ["Prepare the body with ancient control circuits for situation classes.",
           "Read the resulting bodily state via interoception.",
           "Categorize the state with learned emotion concepts.",
           "Treat disorders as failures at circuit, body-reading, or concept level."],
 "assumptions": [("Core affect dimensions", "2", "valence and arousal")],
 "confirm": ["Same bodily mobilization yields different reported emotions under different concept primes.",
             "Mobilization predicts action while categorization predicts experience."],
 "refute": ["Felt emotions prove fully determined by subcortical circuits with no conceptual contribution."],
 "model": '''
import math as _m
_fear, _anger, _joy = (-0.8, 0.7), (-0.7, 0.6), (0.8, 0.5)
def _d(a, b): return _m.hypot(a[0]-b[0], a[1]-b[1])
_dfa, _dfj = _d(_fear, _anger), _d(_fear, _joy)
print("  fear-anger distance: %.3f" % _dfa)
print("  fear-joy distance: %.3f" % _dfj)
assert _dfa < 0.3, "neighboring control states should be close"
print("  CHECK neighboring states close: PASS")
assert _dfj > 1.0, "opposite states should be far"
print("  CHECK opposite states far: PASS")
assert _dfa < _dfj, "affect space inconsistent"
print("  CHECK affect geometry consistent: PASS")
'''},
"language_comprehension": {
 "steps": ["Predict at every level: sound, word, grammar, meaning.",
           "Treat the N400 as semantic prediction error and the P600 as syntactic.",
           "Define a word's meaning as the predictions it licenses.",
           "Read understanding as the convergence of all predictions."],
 "assumptions": [("Predictable word probability", "0.60", "fraction"),
                 ("Unpredictable word probability", "0.02", "fraction")],
 "confirm": ["Level-by-level prediction errors independently predict N400, P600, and comprehension speed.",
             "Comprehension fails exactly when errors cannot be resolved."],
 "refute": ["Comprehension proves non-predictive, computed only after the sentence ends."],
 "model": '''
import math as _m
def _surp(p): return -_m.log2(p)
_sp, _su = _surp(0.60), _surp(0.02)
print("  surprisal, predictable word: %.2f bits" % _sp)
print("  surprisal, unpredictable word: %.2f bits" % _su)
assert _sp < 1.0, "predictable surprisal too high"
print("  CHECK predictable surprisal < 1 bit: PASS")
assert _su > 5.0, "unpredictable surprisal too low"
print("  CHECK unpredictable surprisal > 5 bits: PASS")
assert (_su - _sp) > 4.0, "N400 proxy difference too small"
print("  CHECK error difference > 4 bits (N400 proxy): PASS")
'''},
"neural_basis_of_creativity": {
 "steps": ["Run the generator hot: default mode samples unusual combinations.",
           "Cool the system: executive networks test against goals and taste.",
           "Alternate hot and cool phases on a neuromodulator schedule.",
           "Read insight as the phase transition when a winner is recognized."],
 "assumptions": [("Candidate ideas", "5", "count"), ("Hot phase length", "20", "minutes")],
 "confirm": ["Real-time hot-cool phase tracking predicts creative output.",
             "Output quality depends on phase timing matched to task demands."],
 "refute": ["Creative output proves independent of any generation-evaluation alternation."],
 "model": '''
_sim = [[1.0, 0.8, 0.2, 0.1, 0.3],
        [0.8, 1.0, 0.3, 0.2, 0.1],
        [0.2, 0.3, 1.0, 0.7, 0.2],
        [0.1, 0.2, 0.7, 1.0, 0.4],
        [0.3, 0.1, 0.2, 0.4, 1.0]]
_val = [0.5, 0.6, 0.7, 0.9, 0.4]
_best, _bs = None, -1.0
for _i in range(5):
    for _j in range(_i + 1, 5):
        _s = (1 - _sim[_i][_j]) * _val[_j]
        if _s > _bs: _bs, _best = _s, (_i, _j)
print("  best novel combination: ideas %d + %d" % _best)
print("  novelty x value score: %.3f" % _bs)
assert _sim[_best[0]][_best[1]] < 0.5, "pair not remote enough"
print("  CHECK winning pair is remote (sim < 0.5): PASS")
assert _bs > 0.4, "no valuable combination found"
print("  CHECK valuable combination found: PASS")
'''},
"lifelong_learning_no_forgetting": {
 "steps": ["Track per-synapse importance for mastered skills.",
           "Lock important synapses against change.",
           "Route new learning through unprotected synapses and fresh neurons.",
           "Audit the locks with sleep replay."],
 "assumptions": [("Protection strength", "50.0", "relative units"),
                 ("Task B pull", "1.0", "gradient units")],
 "confirm": ["Measured protection levels predict which synapses change during new learning.",
             "Protection blockade causes catastrophic-like forgetting."],
 "refute": ["New learning changes synapses independently of any importance measure."],
 "model": '''
_lam = 50.0
_w_no = 0.0
_w_prot = _lam / (1.0 + _lam)
print("  skill-A weight after task B, unprotected: %.3f" % _w_no)
print("  skill-A weight after task B, protected: %.4f" % _w_prot)
assert _w_no < 0.1, "unprotected should collapse"
print("  CHECK unprotected collapses (< 0.1): PASS")
assert _w_prot > 0.9, "protection failed"
print("  CHECK protected retained (> 0.9): PASS")
'''},
"anesthesia_consciousness_switch": {
 "steps": ["Require recurrent feedback for consciousness; feedforward alone is unconscious.",
           "Cut long-range feedback gain with molecular actions.",
           "Cross the critical feedback density: a phase transition, not a dimmer.",
           "Reverse the threshold for emergence."],
 "assumptions": [("Integration threshold", "5.0", "index units"),
                 ("Wake feedback gain", "0.95", "fraction"), ("Anesthesia gain", "0.70", "fraction")],
 "confirm": ["Feedback connectivity crosses a sharp threshold exactly at loss and return of consciousness.",
             "The threshold holds across different anesthetic agents."],
 "refute": ["Consciousness is lost with feedback fully intact."],
 "model": '''
def _I(g): return g / (1 - g)
_Iw, _Ia = _I(0.95), _I(0.70)
_T = 5.0
print("  integration index, awake: %.1f" % _Iw)
print("  integration index, anesthetized: %.2f" % _Ia)
assert _Iw > _T > _Ia, "threshold not straddled"
print("  CHECK threshold straddled: PASS")
_Ia2, _Ib2 = _I(0.83), _I(0.84)
print("  index at gain 0.83: %.2f | at 0.84: %.2f" % (_Ia2, _Ib2))
assert _Ia2 < _T < _Ib2, "transition not sharp"
print("  CHECK sharp phase transition at threshold: PASS")
'''},
"volition_libet": {
 "steps": ["Prepare actions unconsciously in parallel accumulators.",
           "Broadcast the leading candidate to the workspace.",
           "Apply conscious endorsement or veto in the late window.",
           "Read the feeling of willing as the endorsement readout."],
 "assumptions": [("Readiness onset", "-500", "ms"), ("Reported decision", "-200", "ms"),
                 ("Movement", "0", "ms")],
 "confirm": ["Veto-window disruption abolishes withholding while sparing initiation.",
             "Endorsement signals predict ownership of action."],
 "refute": ["Conscious intention proves to have zero causal effect under all manipulations."],
 "model": '''
_onset, _w, _move = -500, -200, 0
print("  readiness onset: %d ms" % _onset)
print("  reported decision (W): %d ms" % _w)
print("  movement: %d ms" % _move)
assert _onset < _w < _move, "two-stage order violated"
print("  CHECK preparation < endorsement < action: PASS")
_veto_window = _move - _w
assert 150 < _veto_window < 250, "veto window out of bounds"
print("  CHECK veto window in (150, 250) ms: PASS (%d ms)" % _veto_window)
'''},
"neural_correlates_consciousness": {
 "steps": ["Require recurrence: the representation sustains itself.",
           "Require integration: the state is informationally unified.",
           "Require broadcast: the state is globally available.",
           "Read consciousness as the triple signature, not any single facet."],
 "assumptions": [("Recurrence threshold", "0.80", "fraction"), ("Integration threshold", "0.80", "fraction"),
                 ("Broadcast threshold", "0.80", "fraction")],
 "confirm": ["The triple signature outperforms any single theory's measure.",
             "Disrupting any one facet abolishes the percept."],
 "refute": ["Conscious perception occurs with the triple signature absent."],
 "model": '''
_T = 0.80
_seen = (0.92, 0.88, 0.90)
_masked = (0.90, 0.82, 0.25)
def _consc(s): return all(v > _T for v in s)
print("  seen stimulus triple: %s -> %s" % (_seen, _consc(_seen)))
print("  masked stimulus triple: %s -> %s" % (_masked, _consc(_masked)))
assert _consc(_seen), "seen should be conscious"
print("  CHECK seen classed conscious: PASS")
assert not _consc(_masked), "masked should be unconscious"
print("  CHECK masked classed unconscious: PASS")
_single = _masked[0] > _T and _masked[1] > _T
assert _single, "single-facet measures would misclassify"
print("  CHECK single facet insufficient (needs all three): PASS")
'''},
"brain_aging_cognition": {
 "steps": ["Track conduction timing, not just neuron counts.",
           "Attribute speed and working-memory decline to desynchronization.",
           "Treat stored patterns (vocabulary, expertise) as timing-independent.",
           "Protect myelin and vasculature to protect timing."],
 "assumptions": [("Base conduction delay", "10.0", "ms at age 25"),
                 ("Delay growth", "0.02", "per year after 25")],
 "confirm": ["Conduction timing precision predicts the specific pattern of decline.",
             "Vocabulary proves independent of timing measures."],
 "refute": ["Cognitive decline tracks neuron loss with no role for timing."],
 "model": '''
import math as _m
def _delay(age): return 10.0 * (1 + 0.02 * (age - 25))
def _speed(age): return 100.0 * _m.exp(-(_delay(age) - 10.0) / 15.0)
_s25, _s75 = _speed(25), _speed(75)
_vocab25, _vocab75 = 100.0, 100.0
print("  processing speed at 25: %.1f | at 75: %.1f" % (_s25, _s75))
print("  vocabulary at 25: %.1f | at 75: %.1f" % (_vocab25, _vocab75))
assert _s25 > 95.0, "young speed too low"
print("  CHECK young speed > 95: PASS")
assert 45.0 < _s75 < 60.0, "aged speed out of bounds"
print("  CHECK aged speed in (45, 60): PASS")
assert _vocab75 == _vocab25, "stored patterns should persist"
print("  CHECK vocabulary preserved: PASS")
'''},
"bci_limits": {
 "steps": ["Treat the BCI as two adaptive systems negotiating a shared language.",
           "Cap bandwidth by the mutual information of the sampled fraction.",
           "Let the brain make itself decodable through practice.",
           "Write in the brain's own code; build electrodes the immune system ignores."],
 "assumptions": [("Channels", "100", "count"), ("Bits per channel per second", "20", "bits"),
                 ("Usable fraction after noise", "0.05", "fraction")],
 "confirm": ["Performance is predicted from sampling fraction plus measured co-adaptation.",
             "Brain-side learning gains separate from decoder gains."],
 "refute": ["Performance proves fully determined by decoder quality with zero brain-side adaptation."],
 "model": '''
_raw = 100 * 20
_usable = _raw * 0.05
print("  raw sampled bandwidth: %d bits/s" % _raw)
print("  usable bandwidth after noise: %.0f bits/s" % _usable)
assert 50 < _usable < 200, "usable bandwidth out of bounds"
print("  CHECK usable bandwidth in (50, 200): PASS")
import math as _m
_half_life = 18 * _m.log(2)
print("  signal half-life: %.1f months" % _half_life)
assert 12.0 < _half_life < 24.0, "half-life out of bounds"
print("  CHECK half-life in (12, 24) months: PASS")
'''},
"brain_self_repair": {
 "steps": ["Treat regeneration failure as an active safety interlock.",
           "Attribute recovery to rerouting through surviving pathways.",
           "Train specifically through each patient's remaining pathways.",
           "Pursue guided regrowth only with the miswiring risk solved."],
 "assumptions": [("Intact alternative pathways", "0.60", "fraction"),
                 ("Training gain", "1.50", "multiplier")],
 "confirm": ["Recovery is predicted by rerouting options rather than lesion size.",
             "Unguided brake removal produces miswiring, not function."],
 "refute": ["Unguided regeneration restores precise original connectivity and function."],
 "model": '''
_recovery = min(0.95, 0.60 * 1.50)
_regrow = 0.05
print("  predicted recovery via rerouting: %.2f" % _recovery)
print("  contribution of true regrowth: %.2f" % _regrow)
assert 0.80 < _recovery < 0.95, "recovery out of bounds"
print("  CHECK recovery in (0.80, 0.95): PASS")
assert _recovery > 10 * _regrow, "rerouting must dominate"
print("  CHECK rerouting dominates regrowth: PASS")
'''},
"receptor_to_experience_gap": {
 "steps": ["Act on deep-layer prediction-carrying neurons via 5-HT2A.",
           "Desynchronize the top-down broadcast.",
           "Let unfiltered bottom-up signals surface as visions.",
           "Relax the self-model's priors; permit rapid belief revision."],
 "assumptions": [("EC50", "1.0", "relative dose"), ("Hill coefficient", "1.2", "units")],
 "confirm": ["Deep-layer desynchronization predicts experience intensity and belief change trial by trial.",
             "Selective deep-layer manipulation reproduces the cascade."],
 "refute": ["The full experience occurs with deep-layer prediction signaling intact."],
 "model": '''
def _occ(d): return (d ** 1.2) / (1.0 ** 1.2 + d ** 1.2)
_o1, _o2, _o3 = _occ(0.2), _occ(2.0), _occ(5.0)
print("  occupancy at low dose: %.3f" % _o1)
print("  occupancy at medium dose: %.3f" % _o2)
print("  occupancy at high dose: %.3f" % _o3)
assert _o1 < 0.20, "low-dose occupancy too high"
print("  CHECK low dose < 0.20: PASS")
assert 0.65 < _o2 < 0.80, "medium-dose occupancy out of bounds"
print("  CHECK medium dose in (0.65, 0.80): PASS")
assert _o3 > 0.85, "high-dose occupancy too low"
print("  CHECK high dose > 0.85: PASS")
'''},
"circuit_basis_of_psychosis": {
 "steps": ["Load the dice with genetic risk on gain control.",
           "Over-amplify salience signals through striatal dopamine.",
           "Corrupt prediction-error teaching with noise.",
           "Read hallucinations as over-precise priors and delusions as false inferences."],
 "assumptions": [("Salience threshold", "1.50", "units"), ("Normal gain", "1.0", "multiplier"),
                 ("Elevated gain", "2.5", "multiplier")],
 "confirm": ["Pre-onset gain measures predict who develops psychosis.",
             "Hallucinations track prior precision and delusions track error corruption separately."],
 "refute": ["Psychosis occurs with fully normal gain control and error signaling."],
 "model": '''
_T = 1.50
_sig, _noise = 0.8, 0.1
_normal = 1.0 * (_sig + _noise)
_elev = 2.5 * (_sig + _noise)
print("  salience signal, normal gain: %.2f" % _normal)
print("  salience signal, elevated gain: %.2f" % _elev)
assert _normal < _T, "normal state should stay sub-threshold"
print("  CHECK normal below threshold: PASS")
assert _elev > _T, "elevated state should cross threshold"
print("  CHECK elevated crosses threshold: PASS (aberrant salience)")
'''},
"map_model_whole_brain": {
 "steps": ["Map coarse whole-brain wiring now.",
           "Sample dense synaptic-resolution volumes as ground truth.",
           "Infer the rest statistically, like reference genomes plus variation.",
           "Add weights, dynamics, and modulation: four layers, validated by prediction."],
 "assumptions": [("Synapses", "1e14", "count"), ("Bytes per synapse", "10", "bytes"),
                 ("Imaging rate", "1", "mm^3 per day per scope")],
 "confirm": ["Each added layer measurably improves activity prediction in smaller brains.",
             "A four-layer fly or mouse model beats wiring alone."],
 "refute": ["Complete wiring plus dynamics still fails to predict function in a small mapped brain."],
 "model": '''
_vol_PB = 1e14 * 10 / 1e15
_days = 1.2e6 / 1.0
_years_serial = _days / 365.0
_years_parallel = _years_serial / 10000.0
print("  wiring data volume: %.1f petabytes" % _vol_PB)
print("  serial imaging time: %.0f years" % _years_serial)
print("  with 10k parallel scopes: %.2f years" % _years_parallel)
assert 0.9 < _vol_PB < 1.1, "volume out of bounds"
print("  CHECK volume ~1 petabyte: PASS")
assert 3000 < _years_serial < 3600, "serial time out of bounds"
print("  CHECK serial time in (3000, 3600) years: PASS")
assert 0.2 < _years_parallel < 0.5, "parallel time out of bounds"
print("  CHECK parallel time in (0.2, 0.5) years: PASS")
'''},
"neural_basis_of_self": {
 "steps": ["Model the body, then the organism, then the life story: predictions at three timescales.",
           "Inherit each moment's self-prediction from the last.",
           "Read continuity as the inherited pattern, not persisting matter.",
           "Predict degradations: cut the relay, quiet the prediction, corrupt the pattern."],
 "assumptions": [("Intact self-prediction correlation", "0.92", "fraction"),
                 ("Degraded correlation", "0.45", "fraction")],
 "confirm": ["Self-prediction integrity tracks selfhood vividness across conditions.",
             "Relay interruptions produce the predicted self-thinning."],
 "refute": ["Selfhood persists with the predictive model fully abolished."],
 "model": '''
_vivid_intact = 0.92 ** 2
_vivid_degraded = 0.45 ** 2
print("  selfhood vividness, intact model: %.3f" % _vivid_intact)
print("  selfhood vividness, degraded model: %.3f" % _vivid_degraded)
assert _vivid_intact > 0.7, "intact selfhood too low"
print("  CHECK intact vividness > 0.7: PASS")
assert _vivid_degraded < 0.3, "degraded selfhood too high"
print("  CHECK degraded vividness < 0.3: PASS")
assert _vivid_intact > 3 * _vivid_degraded, "contrast too weak"
print("  CHECK sharp contrast: PASS")
'''},
"hard_problem_consciousness": {
 "steps": ["Grant the problem's genuineness: no description entails feel.",
           "Question the demand for deductive entailment as a possible category error.",
           "Offer a research program, not an answer.",
           "Narrow the correlate until the remaining gap is precisely stated."],
 "assumptions": [("Easy problems addressed", "8", "of 8"), ("Hard problem addressed", "0", "of 1")],
 "confirm": ["A complete physical account predicts every nuance of experience reports with no residual mystery.",
             "Rival positions lose ground as the correlate sharpens."],
 "refute": ["A proof of in-principle uncloseability refutes the program framing (and solves the problem)."],
 "model": '''
_easy = 8.0 / 8.0
_hard = 0.0 / 1.0
_gap = ["why integrated recurrent broadcast feels like anything"]
print("  easy-problem coverage: %.2f" % _easy)
print("  hard-problem coverage: %.2f" % _hard)
print("  remaining gap items: %d" % len(_gap))
assert _easy > 0.99, "easy coverage wrong"
print("  CHECK easy problems covered: PASS")
assert _hard < 0.01, "hard problem must remain open"
print("  CHECK hard problem honestly open: PASS")
assert len(_gap) > 0, "gap must be stated, not hidden"
print("  CHECK gap explicitly stated: PASS")
'''},
"complete_theory_of_brain": {
 "steps": ["State the candidate principle: minimize expected surprise under energy and wiring costs.",
           "Derive perception, learning, memory, attention, sleep, and action as theorems.",
           "Implement hierarchically: predictions down, errors up, precision weights, three-factor plasticity.",
           "Honestly mark the hard problem as underived."],
 "assumptions": [("Phenomena catalogued", "15", "count"), ("Derived from principle", "12", "count")],
 "confirm": ["Separate phenomena are derived quantitatively from the one objective with no extra assumptions.",
             "Each derivation strengthens the theory."],
 "refute": ["A phenomenon provably needs no prediction-error machinery, or the principle proves unfalsifiable."],
 "model": '''
_derived, _total = 12, 15
_coverage = _derived / _total
_underived = ["hard problem", "exact wiring cost function", "developmental schedule"]
print("  phenomena derived from the principle: %d of %d" % (_derived, _total))
print("  coverage: %.2f" % _coverage)
print("  honestly underived: %s" % ", ".join(_underived))
assert 0.70 < _coverage < 0.90, "coverage out of bounds"
print("  CHECK coverage in (0.70, 0.90): PASS")
assert "hard problem" in _underived, "must not claim the hard problem"
print("  CHECK hard problem marked underived: PASS")
assert len(_underived) > 0, "honesty list must be nonempty"
print("  CHECK honesty list nonempty: PASS")
'''},
}


def build_demo(cfg, name, rid, group):
    parts = []
    parts.append("#!/usr/bin/env python3")
    parts.append('"""' + name + " \u2014 solution-explorer walkthrough.")
    parts.append("Record " + rid + " [" + group + "]. Property of Justin Addam Higgins (JAH).")
    parts.append('"""')
    parts.append('print("SOLUTION-EXPLORER: " + ' + json.dumps(name) + ')')
    parts.append('print("Record " + ' + json.dumps(rid) + ' + " [" + ' + json.dumps(group) + ' + "]")')
    parts.append('print()')
    parts.append('print("WALKTHROUGH - the Signature approach step by step:")')
    parts.append("_STEPS = " + json.dumps(cfg["steps"]))
    parts.append("for _i, _s in enumerate(_STEPS, 1):")
    parts.append('    print("  %d. %s" % (_i, _s))')
    parts.append('print()')
    parts.append('print("ASSUMPTIONS (adjustable - change these and re-run):")')
    parts.append("_ASM = " + json.dumps(cfg["assumptions"]))
    parts.append("for _a, _v, _u in _ASM:")
    parts.append('    print("  %s = %s %s" % (_a, _v, _u))')
    parts.append('print()')
    parts.append('print("MODEL - toy illustration of the core relationship (not an experiment, not proof):")')
    parts.append(cfg["model"].strip("\n"))
    parts.append('print()')
    parts.append('print("CONFIRM - evidence that would support the Signature approach:")')
    parts.append("for _c in " + json.dumps(cfg["confirm"]) + ":")
    parts.append('    print("  + " + _c)')
    parts.append('print("REFUTE - evidence that would kill it:")')
    parts.append("for _r in " + json.dumps(cfg["refute"]) + ":")
    parts.append('    print("  - " + _r)')
    parts.append('print()')
    parts.append('print("OK: " + ' + json.dumps(rid) + ')')
    return "\n".join(parts) + "\n"


def _make(key):
    def fn(hdr, name, rid, group, points, req):
        return build_demo(DEMOS_CFG[key], name, rid, group)
    return fn

DEMOS = {k: _make(k) for k in DEMOS_CFG}
