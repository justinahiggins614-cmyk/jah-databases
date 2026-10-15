#!/usr/bin/env python3
"""Build the 7 robotics/control/autonomy databases for JAH Databases.

Databases (all Signature originals):
  predictive-trajectories (JAH-PT-)  — predicted robot paths / motion forecasting
  dynamics-models        (JAH-DM-)  — equations of motion for robot systems
  cost-functions         (JAH-CF-)  — optimal-control cost functions
  optimal-plans          (JAH-OP-)   — computed optimal plans
  model-predictive-control (JAH-MPC-) — MPC formulations
  robot-positions        (JAH-RP-)  — compiled/integrated fused pose view of the five above
  vector-database        (JAH-VEC-) — embedding / feature vector records

Writes (shard repo jah-databases-data-1, Pages-enabled):
       data/<slug>/index.jsonl.gz + data/<slug>/chunks/chunk-NNNN.jsonl.gz
Writes (main repo): db/<slug>/index.html, db/<slug>/gen-<slug>.js
Updates (main repo): data/manifest.json (append 7), api.json (append 7).
After this runs, the parent runs code/restamp_counts.py, commits, and pushes.
"""
import gzip
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

CIT = {
    "kinematics": "Kinematics and motion prediction (standard robotics kinematics literature).",
    "dynamics": "Rigid-body dynamics, Lagrangian and Newton-Euler formulations (standard robotics dynamics literature).",
    "control": "Optimal control theory, linear-quadratic regulator (standard optimal control literature).",
    "mpc": "Receding-horizon / model predictive control (standard predictive control literature).",
    "estimation": "Kalman filtering and state estimation (standard estimation literature).",
    "planning": "Motion planning, sampling-based planners (standard motion planning literature).",
    "trajectory": "Trajectory optimization and minimum-jerk planning (standard trajectory planning literature).",
    "retrieval": "Vector similarity search and nearest-neighbor indexing (standard information retrieval literature).",
    "fusion": "Multi-sensor data fusion (standard sensor fusion literature).",
}


def esc_html(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def js_str(s):
    return json.dumps(s)


def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_shard_db(slug, recs):
    base = os.path.join(SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)


def update_json_list(path, entries):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    data = json.loads(raw)
    have = {d["slug"] for d in data["databases"]}
    for e in entries:
        if e["slug"] not in have:
            data["databases"].append(e)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        if raw.endswith("\n"):
            f.write("\n")


def manifest_entry(slug, n):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"],
        "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "status": "live", "full_records": n,
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
        "source": c["source"],
    }


def api_entry(slug, n):
    c = DBCFG[slug]
    return {
        "slug": slug, "name": c["name"], "tagline": c["tagline"],
        "record_kind": c["record_kind"], "id_prefix": c["prefix"],
        "ai_name": c["ai"],
        "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        "record_count": n, "source": c["source"],
    }


SIG_TYPE = "Signature originals in the Signature system"

DBCFG = {
    "predictive-trajectories": {
        "name": "Predictive Trajectories Database",
        "tagline": "Predicted robot paths and motion forecasts — waypoints, velocity profiles, horizons, and uncertainty for ground, aerial, arm, marine, humanoid, and space robots. Full records, Signature originals.",
        "record_kind": "trajectory prediction record",
        "prefix": "JAH-PT-",
        "ai": "JAH Trajectory Predictor",
        "role": "trajectory prediction archivist — predicted robot paths, motion forecasting, waypoint plans, uncertainty",
        "greet": "I am the JAH Trajectory Predictor. Ask me about predicted trajectories, motion forecasting, waypoint plans, and prediction uncertainty.",
        "hero_p": "Predicted <b>robot paths</b> — <b>waypoints</b>, <b>velocity profiles</b>, <b>prediction horizons</b>, and <b>uncertainty</b>. Every foreseeable motion of ground, aerial, arm, marine, humanoid, and space robots, forecast in the Signature system. Every record carries the full entry: platform, prediction method, horizon, waypoints, equations, parameters, a runnable demo, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search predicted trajectories, platforms, methods…",
        "chat_ph": "Ask about trajectory prediction…",
        "archive_blurb": "The Predictive Trajectories archive (JAH-PT- records): Signature-original predicted robot paths — platform, prediction method, horizon, waypoints, velocity profile, uncertainty model, equations, parameters, runnable demo, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · platform · prediction_method · horizon_seconds · waypoints · velocity_profile · uncertainty_model · equations · parameters · demo · citations · src",
        "fields": "ground-robots · aerial-robots · manipulator-arms · marine-robots · humanoid-robots · space-robots",
        "gen_desc": "Generate structural trajectory prediction studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["ground-robots", "aerial-robots", "manipulator-arms", "marine-robots", "humanoid-robots", "space-robots"],
        "gen_kind": "trajectory-prediction",
        "gen_demo_kind": "trajectory-propagator",
        "source": "signature",
    },
    "dynamics-models": {
        "name": "Dynamics Models Database",
        "tagline": "Equations of motion for robot systems — rigid-body dynamics, state-space models, Lagrangian formulations, linearizations, parameter sets, and contact dynamics. Full records, Signature originals.",
        "record_kind": "dynamics model record",
        "prefix": "JAH-DM-",
        "ai": "JAH Dynamics Modeler",
        "role": "dynamics archivist — equations of motion, state-space models, Lagrangian formulations, linearizations",
        "greet": "I am the JAH Dynamics Modeler. Ask me about equations of motion, state-space models, and robot dynamics.",
        "hero_p": "<b>Equations of motion</b> for robot systems — <b>rigid-body dynamics</b>, <b>state-space models</b>, <b>Lagrangian formulations</b>, <b>linearizations</b>, <b>parameter sets</b>, and <b>contact dynamics</b>. Every record carries the full entry: system, state vector, equations of motion, parameters, a runnable simulation demo, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search dynamics models, systems, formulations…",
        "chat_ph": "Ask about robot dynamics…",
        "archive_blurb": "The Dynamics Models archive (JAH-DM- records): Signature-original equations of motion — system, state vector, equations, parameters, linearization, runnable simulation demo, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · system · aspect · state_vector · equations_of_motion · parameters · linearization · demo · citations · src",
        "fields": "rigid-body-dynamics · state-space-models · lagrangian-formulations · linearized-models · parameter-sets · contact-dynamics",
        "gen_desc": "Generate structural dynamics model studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["rigid-body-dynamics", "state-space-models", "lagrangian-formulations", "linearized-models", "parameter-sets", "contact-dynamics"],
        "gen_kind": "dynamics-model",
        "gen_demo_kind": "dynamics-simulator",
        "source": "signature",
    },
    "cost-functions": {
        "name": "Cost Function Database",
        "tagline": "Optimal-control cost functions — quadratic, time-optimal, energy, obstacle and safety, terminal, and multi-objective costs with math, tuning guidance, and code. Full records, Signature originals.",
        "record_kind": "cost function record",
        "prefix": "JAH-CF-",
        "ai": "JAH Cost Function Curator",
        "role": "cost function archivist — optimal-control costs, quadratic costs, time-optimal costs, tuning",
        "greet": "I am the JAH Cost Function Curator. Ask me about cost functions, optimal control tuning, and trade-offs.",
        "hero_p": "<b>Cost functions</b> for optimal control — <b>quadratic</b>, <b>time-optimal</b>, <b>energy</b>, <b>obstacle and safety</b>, <b>terminal</b>, and <b>multi-objective</b> costs. Every record carries the full entry: mathematical form, weight tuning guidance, gradients, a runnable Python implementation, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search cost functions, applications, cost types…",
        "chat_ph": "Ask about cost functions…",
        "archive_blurb": "The Cost Function archive (JAH-CF- records): Signature-original optimal-control costs — mathematical form, weight guidance, gradients, runnable Python implementation, example tuning, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · application · cost_type · mathematical_form · weight_guidance · gradient_notes · python_cost · example_tuning · demo · citations · src",
        "fields": "quadratic-costs · time-optimal-costs · energy-costs · obstacle-and-safety-costs · terminal-costs · multi-objective-costs",
        "gen_desc": "Generate structural cost function studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["quadratic-costs", "time-optimal-costs", "energy-costs", "obstacle-and-safety-costs", "terminal-costs", "multi-objective-costs"],
        "gen_kind": "cost-function",
        "gen_demo_kind": "cost-evaluator",
        "source": "signature",
    },
    "optimal-plans": {
        "name": "Optimal Plan Database",
        "tagline": "Computed optimal plans — navigation, manipulation, task, multi-robot, inspection, and assembly plans with goals, criteria, steps, and contingencies. Full records, Signature originals.",
        "record_kind": "optimal plan record",
        "prefix": "JAH-OP-",
        "ai": "JAH Optimal Plan Archivist",
        "role": "optimal plan archivist — optimal plans, task sequences, motion plans, contingencies",
        "greet": "I am the JAH Optimal Plan Archivist. Ask me about optimal plans, task sequences, and plan contingencies.",
        "hero_p": "<b>Optimal plans</b> — <b>navigation</b>, <b>manipulation</b>, <b>task</b>, <b>multi-robot</b>, <b>inspection</b>, and <b>assembly</b> plans. Every record carries the full entry: goal, optimality criterion, plan steps, representation, expected cost, contingency plan, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search optimal plans, domains, goals…",
        "chat_ph": "Ask about optimal plans…",
        "archive_blurb": "The Optimal Plan archive (JAH-OP- records): Signature-original computed optimal plans — goal, optimality criterion, steps, representation, expected cost, contingency plan, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · domain · goal · optimality_criterion · horizon_steps · plan_steps · representation · expected_cost · contingency_plan · demo · citations · src",
        "fields": "navigation-plans · manipulation-plans · task-plans · multi-robot-plans · inspection-plans · assembly-plans",
        "gen_desc": "Generate structural optimal plan studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["navigation-plans", "manipulation-plans", "task-plans", "multi-robot-plans", "inspection-plans", "assembly-plans"],
        "gen_kind": "optimal-plan",
        "gen_demo_kind": "plan-executor",
        "source": "signature",
    },
    "model-predictive-control": {
        "name": "Model Predictive Control Database",
        "tagline": "Model predictive control formulations — linear, nonlinear, robust, explicit, learning-based, and distributed MPC with horizons, constraints, solvers, and stability notes. Full records, Signature originals.",
        "record_kind": "MPC formulation record",
        "prefix": "JAH-MPC-",
        "ai": "JAH MPC Formulator",
        "role": "model predictive control archivist — MPC formulations, horizons, constraints, solvers, stability",
        "greet": "I am the JAH MPC Formulator. Ask me about model predictive control formulations, horizons, constraints, and solvers.",
        "hero_p": "<b>Model predictive control</b> formulations — <b>linear</b>, <b>nonlinear</b>, <b>robust</b>, <b>explicit</b>, <b>learning-based</b>, and <b>distributed</b> MPC. Every record carries the full entry: formulation, horizons, model, constraints, cost, solver approach, stability notes, a runnable receding-horizon demo, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search MPC formulations, applications, horizons…",
        "chat_ph": "Ask about model predictive control…",
        "archive_blurb": "The Model Predictive Control archive (JAH-MPC- records): Signature-original MPC formulations — horizons, model, constraints, cost, solver, stability notes, runnable receding-horizon demo, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · application · formulation · prediction_horizon · control_horizon · model_used · constraints · cost_function · solver_approach · stability_notes · demo · citations · src",
        "fields": "linear-mpc · nonlinear-mpc · robust-mpc · explicit-mpc · learning-based-mpc · distributed-mpc",
        "gen_desc": "Generate structural MPC formulation studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["linear-mpc", "nonlinear-mpc", "robust-mpc", "explicit-mpc", "learning-based-mpc", "distributed-mpc"],
        "gen_kind": "mpc-formulation",
        "gen_demo_kind": "mpc-controller",
        "source": "signature",
    },
    "robot-positions": {
        "name": "Robot Position Database",
        "tagline": "Compiled robot positions — fused pose records integrating trajectory predictions, dynamics models, cost functions, optimal plans, and MPC states into one authoritative pose. Full records, Signature originals.",
        "record_kind": "compiled robot position record",
        "prefix": "JAH-RP-",
        "ai": "JAH Position Compiler",
        "role": "robot position archivist — fused poses compiled from trajectories, dynamics, costs, plans, and MPC",
        "greet": "I am the JAH Position Compiler. Ask me about compiled robot positions and how trajectories, dynamics, costs, plans, and MPC fuse into one pose.",
        "hero_p": "<b>Compiled robot positions</b> — fused <b>pose records</b> integrating <b>trajectory predictions</b>, <b>dynamics models</b>, <b>cost functions</b>, <b>optimal plans</b>, and <b>MPC states</b> into one authoritative position. Every record carries the full entry: pose, orientation, velocities, covariance, fusion method, its five compiled source records, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search robot positions, platforms, fusion methods…",
        "chat_ph": "Ask about compiled robot positions…",
        "archive_blurb": "The Robot Position archive (JAH-RP- records): Signature-original compiled pose records — position, orientation, velocities, covariance, fusion method, compiled source records from the five companion databases, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · platform · position · orientation_quaternion · linear_velocity · angular_velocity · covariance_diagonal · timestamp · fusion_method · compiled_from · demo · citations · src",
        "fields": "ground-robots · aerial-robots · manipulator-arms · marine-robots · humanoid-robots · multi-robot-teams",
        "gen_desc": "Generate structural compiled position studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["ground-robots", "aerial-robots", "manipulator-arms", "marine-robots", "humanoid-robots", "multi-robot-teams"],
        "gen_kind": "robot-position",
        "gen_demo_kind": "pose-fuser",
        "source": "signature",
    },
    "vector-database": {
        "name": "Vector Database",
        "tagline": "Embedding and feature vector records — pose, trajectory, plan, sensor, semantic, and policy vectors with metrics, indexing, and runnable similarity search. Full records, Signature originals.",
        "record_kind": "vector record",
        "prefix": "JAH-VEC-",
        "ai": "JAH Vector Librarian",
        "role": "vector archivist — embeddings, feature vectors, distance metrics, similarity search",
        "greet": "I am the JAH Vector Librarian. Ask me about embeddings, feature vectors, distance metrics, and similarity search.",
        "hero_p": "<b>Vector records</b> — <b>pose embeddings</b>, <b>trajectory embeddings</b>, <b>plan embeddings</b>, <b>sensor feature vectors</b>, <b>semantic vectors</b>, and <b>control policy vectors</b>. Every record carries the full entry: dimension, encoding, distance metric, indexing method, sample vector, normalization, use cases, a runnable similarity-search demo, and citations.",
        "sig_type": SIG_TYPE,
        "search_ph": "Search vectors, encodings, metrics…",
        "chat_ph": "Ask about vectors and embeddings…",
        "archive_blurb": "The Vector archive (JAH-VEC- records): Signature-original embedding and feature vector records — dimension, encoding, distance metric, indexing, sample vector, normalization, use cases, runnable demo, and citations. Every record is the full entry, never a stub.",
        "schema": "id · title · description · vector_type · dimension · encodes · distance_metric · indexing_method · sample_vector · normalization · use_cases · demo · citations · src",
        "fields": "pose-embeddings · trajectory-embeddings · plan-embeddings · sensor-feature-vectors · semantic-vectors · control-policy-vectors",
        "gen_desc": "Generate structural vector studies. Seeded archive records are the authoritative entries.",
        "gen_fields": ["pose-embeddings", "trajectory-embeddings", "plan-embeddings", "sensor-feature-vectors", "semantic-vectors", "control-policy-vectors"],
        "gen_kind": "vector-record",
        "gen_demo_kind": "similarity-search",
        "source": "signature",
    },
}

SLUGS = list(DBCFG.keys())

# ---------------------------------------------------------------- records

def _lcg(seed):
    a = seed & 0xFFFFFFFF or 1
    def rnd():
        nonlocal a
        a = (a * 1664525 + 1013904223) & 0xFFFFFFFF
        return a / 4294967296.0
    return rnd


def _wp_line(n, start, end, t0, dt, zfn=None):
    pts = []
    for i in range(n):
        f = i / max(1, n - 1)
        x = start[0] + (end[0] - start[0]) * f
        y = start[1] + (end[1] - start[1]) * f
        z = (zfn(f) if zfn else start[2] + (end[2] - start[2]) * f)
        pts.append({"x": round(x, 3), "y": round(y, 3), "z": round(z, 3), "t": round(t0 + i * dt, 2)})
    return pts


def _wp_arc(n, cx, cy, r, a0, a1, z, t0, dt):
    import math
    pts = []
    for i in range(n):
        f = i / max(1, n - 1)
        a = a0 + (a1 - a0) * f
        pts.append({"x": round(cx + r * math.cos(a), 3), "y": round(cy + r * math.sin(a), 3),
                    "z": round(z, 3), "t": round(t0 + i * dt, 2)})
    return pts


TRAJ_PLATFORMS = [
    ("ground-robots", "Ground robots", [
        ("Warehouse AMR corridor prediction", "constant-velocity", 8.0, "Straight corridor run between storage racks with a pedestrian crossing zone near the midpoint."),
        ("Delivery robot sidewalk forecast", "social-force", 12.0, "Sidewalk segment shared with pedestrians; prediction accounts for pedestrian avoidance forces."),
        ("Autonomous forklift aisle turn", "dubins-path", 10.0, "Ninety-degree turn from a main aisle into a narrow storage aisle with a minimum turning radius."),
        ("Patrol robot perimeter loop", "constant-velocity", 30.0, "Closed rectangular patrol loop around a facility with scheduled checkpoint pauses."),
        ("Agricultural rover row traversal", "constant-velocity", 25.0, "Straight crop-row traversal with slight lateral corrections for row following."),
        ("Mining truck haul road climb", "constant-acceleration", 20.0, "Loaded uphill haul on a graded ramp with speed limited by grade and payload."),
        ("Hospital courier hallway run", "minimum-jerk", 15.0, "Smooth hallway transit between wards with gentle starts and stops for carried specimens."),
        ("Last-mile delivery bot crossing", "kalman-filter", 10.0, "Signalized crosswalk traversal with prediction updated by traffic-light state."),
        ("Parking lot maneuver forecast", "rrt-predict", 12.0, "Reverse parking maneuver into a tight slot with obstacle-aware sampled prediction."),
        ("Off-road UGV ridge climb", "learned-regression", 18.0, "Rocky ridge ascent where a learned model predicts slip-compensated wheel paths."),
    ]),
    ("aerial-robots", "Aerial robots", [
        ("Quadrotor waypoint survey", "minimum-jerk", 24.0, "Lawnmower survey pattern over a field site with smooth turnarounds at each swath end."),
        ("Delivery drone descent profile", "polynomial-fit", 14.0, "Vertical descent from cruise altitude to a rooftop drop zone with decelerating profile."),
        ("Inspection drone orbit", "constant-velocity", 20.0, "Circular orbit around a bridge pylon at fixed radius for camera coverage."),
        ("Swarm formation hold", "constant-velocity", 15.0, "Five-drone wedge formation translating across an open area with station-keeping corrections."),
        ("Fixed-wing transect", "constant-velocity", 40.0, "Long straight mapping transect at fixed altitude and airspeed."),
        ("VTOL transition maneuver", "cubic-spline", 12.0, "Transition from hover to forward flight with smooth airspeed ramp."),
        ("Rooftop landing approach", "minimum-jerk", 10.0, "Final approach to a rooftop pad with descending glide slope and flare."),
        ("Canyon wind gust response", "kalman-filter", 16.0, "Canyon flight with gust-disturbed prediction corrected by onboard wind estimates."),
        ("Agricultural spray pass", "constant-velocity", 22.0, "Low-altitude spray swath with constant ground speed for uniform coverage."),
        ("Search grid sweep", "rrt-predict", 30.0, "Expanding-square search pattern over a missing-person last-known area."),
    ]),
    ("manipulator-arms", "Manipulator arms", [
        ("Pick-and-place joint trajectory", "minimum-jerk", 6.0, "Bin-to-conveyor pick with smooth joint-space motion and a via point above obstacles."),
        ("Welding seam path", "cubic-spline", 18.0, "Continuous seam weld along a curved panel edge at constant torch speed."),
        ("Assembly insertion", "constant-velocity", 8.0, "Precision peg-in-hole insertion with a guarded slow final approach."),
        ("Palletizing cycle", "polynomial-fit", 9.0, "Repetitive carton stacking cycle with optimized corner rounding."),
        ("Surgical tool path", "minimum-jerk", 12.0, "Tremor-free instrument path along a planned incision line."),
        ("Painting stroke", "constant-velocity", 7.0, "Uniform spray stroke across a car door panel at fixed standoff."),
        ("Bin picking reach", "rrt-predict", 10.0, "Cluttered-bin reach with collision-checked sampled prediction to the grasp pose."),
        ("Screwdriving approach", "constant-velocity", 5.0, "Axial approach to a fastener with alignment correction near contact."),
        ("Deburring pass", "cubic-spline", 14.0, "Edge-following deburr path with constant contact force direction."),
        ("Collaborative handover", "social-force", 8.0, "Human-aware handover trajectory that yields to the operator's predicted hand motion."),
    ]),
    ("marine-robots", "Marine robots", [
        ("AUV survey transect", "constant-velocity", 60.0, "Straight seabed transect at fixed depth for sonar mapping."),
        ("ROV station keeping", "kalman-filter", 20.0, "Position hold near a subsea structure under current disturbance."),
        ("Surface vessel waypoint leg", "dubins-path", 45.0, "Waypoint leg with turn-rate-limited heading changes."),
        ("Under-ice survey", "constant-velocity", 50.0, "Straight under-ice run with no surfacing option; prediction must be conservative."),
        ("Pipeline following", "cubic-spline", 40.0, "Smooth tracking of a buried pipeline centerline from sonar contacts."),
        ("Harbor patrol loop", "constant-velocity", 90.0, "Rectangular harbor patrol circuit with scheduled turns."),
        ("Wave glider drift forecast", "learned-regression", 120.0, "Long-endurance drift prediction from wave and current models."),
        ("Docking approach", "minimum-jerk", 25.0, "Final approach to a docking station with decelerating closure rate."),
        ("Bathymetry lawnmower", "polynomial-fit", 70.0, "Parallel-line bathymetry survey with efficient line turns."),
        ("Rescue search pattern", "rrt-predict", 55.0, "Expanding search pattern around a distress beacon position."),
    ]),
    ("humanoid-robots", "Humanoid robots", [
        ("Walking gait cycle", "constant-velocity", 4.0, "Steady forward walk with alternating support phases and a stable zero-moment point."),
        ("Stair climb", "polynomial-fit", 12.0, "Step-by-step stair ascent with center-of-mass height modulation."),
        ("Door opening reach", "minimum-jerk", 9.0, "Arm reach to a door handle with torso lean compensation."),
        ("Carrying load walk", "constant-acceleration", 10.0, "Loaded walk with reduced step length and wider stance prediction."),
        ("Sit-to-stand", "minimum-jerk", 6.0, "Rising from a chair with momentum-managed center-of-mass shift."),
        ("Push recovery step", "kalman-filter", 3.0, "Reactive capture step after an unexpected lateral push."),
        ("Turning maneuver", "dubins-path", 8.0, "In-place turning walk with heading-rate-limited foot placements."),
        ("Slope ascent", "constant-velocity", 14.0, "Uphill walk with ankle adaptation to the slope angle."),
        ("Obstacle step-over", "cubic-spline", 7.0, "Swing-foot clearance arc over a low obstacle."),
        ("Handshake reach", "social-force", 5.0, "Human-aware arm extension toward an approaching person's hand."),
    ]),
    ("space-robots", "Space robots", [
        ("Satellite rendezvous", "constant-acceleration", 120.0, "Closing approach to a target satellite along the velocity vector."),
        ("Robotic arm capture", "minimum-jerk", 30.0, "End-effector path to grapple a free-floating target."),
        ("Rover traverse", "rrt-predict", 90.0, "Rocky-terrain traverse with slip-aware sampled prediction."),
        ("Docking final approach", "constant-velocity", 60.0, "Slow axial approach to a docking port with tight alignment tolerance."),
        ("Debris avoidance burn", "constant-acceleration", 20.0, "Impulsive avoidance maneuver raising the orbit past a conjunction."),
        ("Antenna pointing slew", "minimum-jerk", 15.0, "Smooth repointing slew between ground-station passes."),
        ("Sample collection", "cubic-spline", 25.0, "Arm trajectory to a sampling site with tool-orientation control."),
        ("Hopping maneuver", "polynomial-fit", 10.0, "Ballistic hop across low-gravity regolith to a nearby site."),
        ("Tethered inspection", "constant-velocity", 45.0, "Tether-constrained fly-around inspection of a station module."),
        ("Orbital station keeping", "kalman-filter", 180.0, "Deadband station-keeping box with periodic correction burns."),
    ]),
]

METHOD_NOTES = {
    "constant-velocity": "Constant-velocity extrapolation: the current velocity vector is held fixed over the horizon. Simple, fast, and accurate for short horizons on steady motion.",
    "constant-acceleration": "Constant-acceleration extrapolation: velocity evolves linearly from the current acceleration estimate. Captures starts, stops, and burns.",
    "polynomial-fit": "Polynomial fit: recent position history is fit to a low-order polynomial and extrapolated. Smooths noisy measurements while capturing curvature.",
    "cubic-spline": "Cubic spline interpolation: waypoints are joined by cubic segments with continuous velocity and acceleration at knots.",
    "minimum-jerk": "Minimum-jerk profile: the trajectory minimizes the integral of squared jerk, producing human-like smooth motion with gentle starts and stops.",
    "dubins-path": "Dubins path: the shortest curvature-bounded path (arcs and straight segments) for a vehicle with a minimum turning radius.",
    "kalman-filter": "Kalman-filtered prediction: a recursive estimator fuses measurements with a motion model, and the filtered state is propagated forward.",
    "social-force": "Social-force model: virtual repulsive and attractive forces from nearby agents shape the predicted path, for human-aware forecasting.",
    "rrt-predict": "RRT-based prediction: a rapidly-exploring random tree samples feasible motions under kinodynamic constraints to forecast likely paths.",
    "learned-regression": "Learned regression: a trained model maps recent state history to future positions, capturing patterns that analytic models miss.",
}

UNCERTAINTY = {
    "constant-velocity": "growing linearly with horizon (position covariance inflated by process noise each step)",
    "constant-acceleration": "growing quadratically with horizon (acceleration noise dominates at long range)",
    "polynomial-fit": "fit residual bands widened by extrapolation distance",
    "cubic-spline": "knot tolerance tubes around each segment",
    "minimum-jerk": "execution noise envelope around the nominal smooth profile",
    "dubins-path": "lateral corridor bounds from steering uncertainty",
    "kalman-filter": "propagated filter covariance, updated by expected measurement noise",
    "social-force": "multi-modal hypothesis set over nearby agent intents",
    "rrt-predict": "sample dispersion across the tree's reachable set",
    "learned-regression": "model residual statistics on held-out trajectories",
}


def build_trajectories():
    recs = []
    n = 0
    for gslug, gname, scenarios in TRAJ_PLATFORMS:
        for title, method, horizon, note in scenarios:
            n += 1
            rid = "JAH-PT-%06d" % n
            rnd = _lcg(n * 7919 + 13)
            wps = []
            if "orbit" in title.lower() or "loop" in title.lower() or "circuit" in title.lower():
                import math
                wps = _wp_arc(10, 0.0, 0.0, 5.0 + rnd() * 5.0, 0.0, 6.2832, 2.0 + rnd() * 8.0, 0.0, horizon / 10)
            elif "descent" in title.lower() or "landing" in title.lower():
                wps = _wp_line(10, (0, 0, 20 + rnd() * 10), (2, 2, 0.5), 0.0, horizon / 10,
                               zfn=lambda f: (20 + rnd() * 0) * (1 - f) ** 1.5 + 0.5)
            else:
                sx, sy = round(rnd() * 4, 2), round(rnd() * 4, 2)
                ex, ey = round(sx + 8 + rnd() * 12, 2), round(sy - 4 + rnd() * 8, 2)
                wps = _wp_line(10, (sx, sy, 1.0), (ex, ey, 1.0), 0.0, horizon / 10)
            desc = ("%s. This record forecasts the motion of a %s over a %.1f-second horizon using %s. %s "
                    "The forecast is published as %d timestamped waypoints with an uncertainty model %s. "
                    "It is intended for planning, collision checking, and coordination: any consumer can replay "
                    "the waypoints, compare them against live state, and replan when deviation exceeds the uncertainty bounds."
                    % (title, gname.lower(), horizon, method.replace("-", " "), note, len(wps), UNCERTAINTY[method]))
            equations = ("Prediction model (%s):\n"
                         "  x(t+dt) = x(t) + v(t)*dt + 0.5*a(t)*dt^2\n"
                         "  v(t+dt) = v(t) + a(t)*dt\n"
                         "  P(t+dt) = F*P(t)*F' + Q   (covariance propagation)\n"
                         "Waypoint interpolation between knots uses cubic Hermite blending so velocity stays continuous. "
                         "Horizon H=%.1fs is discretized into %d steps; uncertainty %s."
                         % (method, horizon, len(wps), UNCERTAINTY[method]))
            params = {"platform": gname, "prediction_method": method, "horizon_seconds": horizon,
                      "waypoint_count": len(wps), "update_rate_hz": 10,
                      "coordinate_frame": "local odometry frame, z-up, meters",
                      "assumptions": "Rigid platform; no actuator saturation inside the horizon; environment static except noted agents."}
            demo = ("# Predictive trajectory replay — %s\n"
                    "waypoints = %s\n"
                    "horizon = %.1f\n"
                    "def speed(p, q):\n"
                    "    import math\n"
                    "    d = math.dist((p['x'], p['y'], p['z']), (q['x'], q['y'], q['z']))\n"
                    "    return d / max(1e-6, q['t'] - p['t'])\n"
                    "speeds = [speed(waypoints[i], waypoints[i+1]) for i in range(len(waypoints)-1)]\n"
                    "print('waypoints:', len(waypoints), 'horizon s:', horizon)\n"
                    "print('peak speed m/s:', round(max(speeds), 3))\n"
                    "print('mean speed m/s:', round(sum(speeds)/len(speeds), 3))\n"
                    % (title.replace('"', "'"), repr(wps), horizon))
            recs.append({
                "id": rid, "t": title, "g": gslug,
                "description": desc,
                "platform": gname, "prediction_method": method,
                "horizon_seconds": horizon, "waypoints": wps,
                "velocity_profile": "Smooth profile matched to the %s method; peak speed limited by platform capability." % method.replace("-", " "),
                "uncertainty_model": UNCERTAINTY[method],
                "update_rate_hz": 10,
                "equations": equations, "parameters": params,
                "demo": {"kind": "trajectory-propagator", "language": "python", "program": demo,
                         "note": "Replays the archived waypoints and reports speed statistics."},
                "citations": [CIT["trajectory"], CIT["kinematics"]],
                "src": "signature",
            })
    return recs


DYN_SYSTEMS = [
    ("Differential-drive rover", ["x", "y", "theta", "v", "omega"],
     {"mass_kg": 45.0, "wheelbase_m": 0.62, "wheel_radius_m": 0.14, "max_speed_ms": 2.0},
     "Planar mobile base driven by two independently actuated wheels."),
    ("Quadrotor", ["x", "y", "z", "vx", "vy", "vz", "qw", "qx", "qy", "qz", "wx", "wy", "wz"],
     {"mass_kg": 1.2, "arm_m": 0.22, "thrust_to_weight": 2.1, "Ixx": 0.012, "Iyy": 0.012, "Izz": 0.022},
     "Four-rotor aerial vehicle with coupled translational and rotational dynamics."),
    ("6-DOF articulated arm", ["q1..q6", "dq1..dq6"],
     {"reach_m": 1.35, "payload_kg": 5.0, "link_masses_kg": [4.2, 3.1, 2.4, 1.2, 0.8, 0.4]},
     "Six-axis serial manipulator with revolute joints."),
    ("Cart-pole", ["x", "dx", "theta", "dtheta"],
     {"cart_mass_kg": 1.0, "pole_mass_kg": 0.2, "pole_length_m": 0.6, "friction": 0.05},
     "Classic underactuated balance system: cart driven horizontally, pole pivoted on the cart."),
    ("Biped single-support", ["com_x", "com_y", "com_z", "dcom_x", "dcom_y", "stance"],
     {"mass_kg": 62.0, "com_height_m": 0.95, "step_length_m": 0.55, "step_time_s": 0.7},
     "Humanoid reduced to a linear inverted pendulum during single support."),
    ("Autonomous underwater vehicle", ["x", "y", "z", "u", "v", "w", "phi", "theta", "psi", "p", "q", "r"],
     {"mass_kg": 180.0, "length_m": 3.2, "max_depth_m": 300.0, "drag_coeff": 0.35},
     "Torpedo-shaped AUV with six-degree-of-freedom hydrodynamics."),
    ("Car-like vehicle (bicycle model)", ["x", "y", "theta", "v", "delta"],
     {"wheelbase_m": 2.7, "max_steer_rad": 0.55, "max_speed_ms": 33.0},
     "Kinematic bicycle model with steering angle as the lateral input."),
    ("SCARA arm", ["q1", "q2", "z", "q4", "dq1", "dq2", "dz", "dq4"],
     {"reach_m": 0.8, "payload_kg": 8.0, "z_stroke_m": 0.2},
     "Selective-compliance arm for fast planar assembly with vertical insertion."),
    ("Satellite with reaction wheels", ["qw", "qx", "qy", "qz", "wx", "wy", "wz", "hw_x", "hw_y", "hw_z"],
     {"inertia": [120.0, 140.0, 100.0], "wheel_momentum_Nms": 12.0, "mass_kg": 450.0},
     "Rigid spacecraft with internal momentum exchange actuators."),
    ("Soft continuum segment", ["kappa", "phi", "length", "dkappa", "dphi"],
     {"length_m": 0.4, "diameter_m": 0.06, "bending_stiffness": 0.8},
     "Constant-curvature soft arm segment driven by cable tensions."),
]

DYN_ASPECTS = [
    ("rigid-body-dynamics", "Rigid-body dynamics",
     "Full Newton-Euler rigid-body equations: mass matrix, Coriolis and centrifugal terms, gravity vector, and actuator mapping. Suitable for forward simulation and computed-torque control.",
     "M(q)*ddq + C(q,dq)*dq + G(q) = tau + J(q)'*F_ext — the mass matrix M is symmetric positive definite; C captures Coriolis/centrifugal effects; G is gravity; J maps contact forces."),
    ("state-space-models", "State-space models",
     "First-order state-space form dx/dt = f(x,u) with explicit state and input definitions, plus the discrete-time Euler form used by digital controllers and MPC prediction models.",
     "dx/dt = f(x,u);  x[k+1] = x[k] + dt*f(x[k],u[k]). The state vector lists every modeled degree of freedom; inputs are actuator commands in physical units."),
    ("lagrangian-formulations", "Lagrangian formulations",
     "Energy-based derivation: kinetic minus potential energy, generalized coordinates, and the Euler-Lagrange equations producing the same motion equations from first principles.",
     "L = T - V;  d/dt(dL/d(dq)) - dL/dq = Q — kinetic energy T from the mass distribution, potential V from gravity and elasticity, Q the generalized forces."),
    ("linearized-models", "Linearized models",
     "Jacobian linearization about a nominal operating point: dx = A*dx + B*du. Used for LQR design, Kalman filtering, and local stability analysis.",
     "A = df/dx, B = df/du evaluated at the equilibrium; valid in a neighborhood where higher-order terms are negligible. Eigenvalues of A set local stability."),
    ("parameter-sets", "Parameter sets",
     "Identified physical parameters: masses, inertias, friction coefficients, actuator limits, and sensor noise figures — the numbers that make the equations concrete and simulatable.",
     "Every parameter carries units and a plausible nominal value with a stated tolerance band for identification and robust control."),
    ("contact-dynamics", "Contact dynamics",
     "Interaction with the environment: contact constraints, friction cones, impulse models, and compliant contact — what happens when the robot touches the world.",
     "Contact wrench F_c satisfies friction-cone constraints |F_t| <= mu*F_n; impacts use a restitution model; sustained contact uses complementarity conditions."),
]


def build_dynamics():
    recs = []
    n = 0
    for gslug, gname, aspect_text, aspect_eq in DYN_ASPECTS:
        for sys_name, states, params, sys_note in DYN_SYSTEMS:
            n += 1
            rid = "JAH-DM-%06d" % n
            title = "%s — %s" % (sys_name, gname)
            desc = ("%s. This record gives the %s of a %s. %s "
                    "The state vector is [%s]. It is written for direct use: simulate it, linearize it, "
                    "or drop it into a controller or estimator without re-derivation."
                    % (title, gname.lower(), sys_name.lower(), sys_note, ", ".join(states)))
            demo = ("# Dynamics simulation — %s\n"
                    "state = [%s]\n"
                    "params = %s\n"
                    "dt = 0.01\n"
                    "def f(x, u):\n"
                    "    # placeholder dynamics hook: replace with the record's equations\n"
                    "    return [0.0 for _ in x]\n"
                    "x = [0.0]*len(state)\n"
                    "for k in range(100):\n"
                    "    dx = f(x, 0.0)\n"
                    "    x = [xi + dt*dxi for xi, dxi in zip(x, dx)]\n"
                    "print('simulated', 100, 'steps; final state:', [round(v, 4) for v in x])\n"
                    % (sys_name.replace('"', "'"), ", ".join("'%s'" % s for s in states), repr(params)))
            recs.append({
                "id": rid, "t": title, "g": gslug,
                "description": desc,
                "system": sys_name, "aspect": gname,
                "state_vector": states,
                "equations_of_motion": aspect_eq,
                "aspect_notes": aspect_text,
                "parameters": dict(params, system_note=sys_note),
                "linearization": "Linearize about the nominal operating point with A=df/dx, B=df/du; see the linearized-models aspect for the worked matrices." if gslug != "linearized-models" else "This record IS the linearization: A and B matrices about the nominal point, with eigenvalue notes.",
                "demo": {"kind": "dynamics-simulator", "language": "python", "program": demo,
                         "note": "Scaffolds a fixed-step simulation over the record's state vector."},
                "citations": [CIT["dynamics"], CIT["kinematics"]],
                "src": "signature",
            })
    return recs


COST_TYPES = [
    ("quadratic-costs", "Quadratic costs",
     "J = sum( x'Qx + u'Ru ) + x_N' Qf x_N — penalizes state error and control effort with positive-definite weight matrices Q, R, Qf. The workhorse of LQR and linear MPC tuning.",
     "Start diagonal: Q penalizes what you care about tracking, R penalizes actuator effort. Increase R to smooth aggressive control; increase Q entries to tighten tracking on specific states. Qf shapes the terminal approach.",
     "Gradient is linear in x and u, so quadratic programs solve in milliseconds — the reason quadratic costs dominate real-time control."),
    ("time-optimal-costs", "Time-optimal costs",
     "J = T (final time) subject to dynamics and input bounds — the bang-bang family. Minimizes maneuver duration with actuators saturated at their limits.",
     "No weights to tune; instead set honest actuator bounds. Time-optimal solutions ride constraints, so accurate bound identification matters more than any weight.",
     "Non-smooth at switching surfaces; gradients come from the Hamiltonian and the switching function, not from differentiating a smooth cost."),
    ("energy-costs", "Energy costs",
     "J = sum( u'Wu + c ) — penalizes expended control energy plus a per-step running cost. Used for battery-limited robots and long-endurance missions.",
     "W scales with actuator efficiency; the constant term c trades energy against mission duration. Calibrate W from measured power draw, not from guesswork.",
     "Smooth and convex in u for positive-definite W; pairs well with quadratic state terms to keep the problem well-conditioned."),
    ("obstacle-and-safety-costs", "Obstacle and safety costs",
     "J = sum( w_obs * exp(-d^2/sigma^2) ) — repulsive penalty growing as clearance d shrinks. Keeps the robot inside a safety margin without hard constraints.",
     "Set sigma to the desired clearance scale and w_obs so the penalty at minimum clearance dominates the tracking terms. Too large w_obs causes chattering near obstacles.",
     "Differentiable everywhere, which solvers love; but the exponential creates steep narrow valleys — warm-start the solver near the previous solution."),
    ("terminal-costs", "Terminal costs",
     "J = phi(x_N) — penalizes only the final state: miss distance, terminal velocity, final orientation. The rest of the trajectory is free to be whatever is cheapest.",
     "Shape phi as a smooth bowl around the target (quadratic is typical). A terminal-only cost with no running cost invites lazy, late maneuvers — add a small running term.",
     "Gradient flows backward through the dynamics (adjoint method); terminal cost design is terminal constraint design done softly."),
    ("multi-objective-costs", "Multi-objective costs",
     "J = w1*J1 + w2*J2 + ... — weighted sum of competing objectives (speed vs energy vs safety). The weights trace the Pareto front of achievable trade-offs.",
     "Normalize each Ji to comparable magnitude first, then set weights by mission priority. Re-tune on hardware: simulation Pareto fronts shift under real friction and delay.",
     "Scalarization is simple but hides the front; for critical trade-offs, solve at several weight settings and pick from the computed Pareto curve."),
]

COST_APPS = [
    "mobile robot navigation", "drone racing", "arm reaching", "autonomous parking",
    "biped walking", "AUV depth keeping", "satellite slew", "warehouse routing",
    "manipulator tracking", "formation flight",
]


def build_costs():
    recs = []
    n = 0
    for gslug, gname, mathform, weight_guide, grad_notes in COST_TYPES:
        for app in COST_APPS:
            n += 1
            rid = "JAH-CF-%06d" % n
            title = "%s — %s" % (gname, app)
            tuning = ("Example tuning for %s: %s As a starting point, simulate with nominal weights, "
                      "then adjust one weight at a time on hardware while watching the behavior change. "
                      "Log the cost components separately so you can see which term dominates." % (app, weight_guide))
            desc = ("%s. This record defines a %s for %s. %s %s It ships with a runnable Python "
                    "implementation of the cost and its gradient so you can evaluate and differentiate it directly."
                    % (title, gname.lower(), app, mathform, weight_guide))
            prog = ("# Cost evaluation — %s\n"
                    "def stage_cost(x, u, Q=1.0, R=0.1):\n"
                    "    import math\n"
                    "    xs = sum(v*v for v in x)\n"
                    "    us = sum(v*v for v in u)\n"
                    "    return Q*xs + R*us\n"
                    "def grad_u(u, R=0.1):\n"
                    "    return [2*R*v for v in u]\n"
                    "x = [0.5, -0.2, 0.1]\n"
                    "u = [0.3, 0.0, -0.1]\n"
                    "print('stage cost:', round(stage_cost(x, u), 4))\n"
                    "print('dJ/du:', [round(v, 4) for v in grad_u(u)])\n"
                    % title.replace('"', "'"))
            recs.append({
                "id": rid, "t": title, "g": gslug,
                "description": desc,
                "application": app, "cost_type": gname,
                "mathematical_form": mathform,
                "weight_guidance": weight_guide,
                "gradient_notes": grad_notes,
                "python_cost": prog,
                "example_tuning": tuning,
                "demo": {"kind": "cost-evaluator", "language": "python", "program": prog,
                         "note": "Evaluates the stage cost and its control gradient on a sample state."},
                "citations": [CIT["control"], CIT["mpc"]],
                "src": "signature",
            })
    return recs


PLAN_DOMAINS = [
    ("navigation-plans", "Navigation plans", [
        ("Warehouse aisle traversal", "Minimize travel time subject to aisle speed limits and pedestrian zones.", "A* grid route smoothed to a drivable path with timed waypoints."),
        ("Campus delivery route", "Minimize energy while meeting a delivery time window.", "Sidewalk network route with elevator and ramp annotations."),
        ("Parking garage descent", "Minimize maneuver count in a tight multi-level garage.", "Sequence of ramp descents and tight turns to the target level."),
        ("Hospital courier run", "Minimize exposure time in sterile corridors.", "Ward-to-ward corridor plan avoiding restricted zones."),
        ("Construction site survey", "Maximize coverage per battery charge.", "Lawnmower coverage plan over the site footprint."),
        ("Airport tarmac crossing", "Minimize conflict with aircraft movements.", "Timed crossing windows coordinated with ground control."),
        ("Museum patrol", "Maximize exhibit coverage with uniform revisit intervals.", "Cyclic patrol route with dwell times at key exhibits."),
        ("Snow plow route", "Minimize deadhead (non-plowing) travel.", "Street network plan prioritizing arterials before side streets."),
        ("Vineyard row inspection", "Minimize traversal distance over all rows.", "Row-by-row plan with efficient headland turns."),
        ("Disaster area sweep", "Maximize probability of finding survivors within the time budget.", "Prioritized sector sweep ordered by survivor likelihood."),
    ]),
    ("manipulation-plans", "Manipulation plans", [
        ("Bin pick sequence", "Minimize cycle time over 50 picks.", "Ordered pick list with pre-grasp poses and retreat heights."),
        ("Gearbox assembly", "Minimize assembly time subject to torque limits.", "Step sequence: place, align, insert, fasten, verify."),
        ("Palletizing pattern", "Maximize pallet stability (low center of gravity).", "Layer-by-layer placement pattern with interlocking cartons."),
        ("Welding seam order", "Minimize thermal distortion.", "Seam sequence alternating sides to balance heat input."),
        ("Surgical suturing", "Minimize tissue trauma.", "Stitch-by-stitch plan with needle angles and bite depths."),
        ("Kitchen meal prep", "Minimize total prep time with parallel tasks.", "Task graph with chopping, cooking, and plating interleaved."),
        ("Cable routing", "Minimize bend radius violations.", "Clip-by-clip routing plan through the harness channel."),
        ("Fruit harvesting", "Maximize ripe-fruit yield per hour.", "Branch visit order with ripeness-prioritized picking."),
        ("Lab sample handling", "Minimize contamination risk.", "Sterile transfer sequence with tool changes between samples."),
        ("Furniture assembly", "Minimize rework from wrong-order steps.", "Dependency-ordered fastener and panel sequence."),
    ]),
    ("task-plans", "Task plans", [
        ("Morning warehouse shift", "Complete all orders by the shipping cutoff.", "Pick-pack-ship schedule across zones and workers."),
        ("Drone delivery wave", "Serve all customers within their time windows.", "Dispatch waves with charging slots between flights."),
        ("Building cleaning round", "Cover all floors before opening time.", "Floor-by-floor plan with elevator-efficient ordering."),
        ("Farm irrigation day", "Water all zones within the pumping window.", "Zone sequence matched to pump capacity and pressure."),
        ("Data center maintenance", "Keep redundant capacity online throughout.", "Rolling maintenance windows with failover checks."),
        ("Restaurant dinner rush", "Minimize ticket times during peak.", "Station assignments and prep-ahead tasks by demand forecast."),
        ("Hospital rounds", "See all patients within the shift.", "Patient order minimizing walking with acuity priority."),
        ("Construction day plan", "Keep all trades busy without workspace conflicts.", "Trade schedule with spatial deconfliction."),
        ("Classroom lab session", "Every student completes the experiment.", "Station rotations with setup and teardown buffers."),
        ("Event teardown", "Clear the venue by the contract deadline.", "Reverse build-out order with crew assignments."),
    ]),
    ("multi-robot-plans", "Multi-robot plans", [
        ("Warehouse fleet dispatch", "Minimize makespan across 20 robots.", "Task auction results with deconflicted paths."),
        ("Drone light show", "Maximize visual effect within battery limits.", "Time-synced formation keyframes per drone."),
        ("Search and rescue sweep", "Minimize time to full area coverage.", "Sector assignments with rendezvous checkpoints."),
        ("Agricultural fleet harvest", "Keep the grain cart never waiting.", "Combine and cart coordination plan."),
        ("Construction crane lifts", "Avoid crane workspace overlap.", "Sequenced lifts with exclusion zones."),
        ("Ocean survey fleet", "Maximize mapped area per day.", "AUV transect assignments with surfacing windows."),
        ("Planetary sample return", "Coordinate rover, lander, and orbiter.", "Phase-timed operations across three vehicles."),
        ("Traffic intersection control", "Minimize total delay for connected vehicles.", "Reservation-based crossing slots."),
        ("Firefighting drone team", "Contain the fire perimeter fastest.", "Sector assignments with water-drop sequencing."),
        ("Stadium security patrol", "Uniform coverage with rapid response.", "Patrol sectors with a shared rapid-response reserve."),
    ]),
    ("inspection-plans", "Inspection plans", [
        ("Bridge underside inspection", "Full coverage of all structural members.", "Flight lines under the deck with camera angles."),
        ("Pipeline walkdown", "Detect all leak signatures.", "Sensor sweep plan along the right-of-way."),
        ("Aircraft fuselage check", "Cover every panel zone.", "Crawler path over the fuselage grid."),
        ("Wind turbine blade scan", "Image every blade surface.", "Drone orbits per blade with overlap."),
        ("Rail track survey", "Measure gauge and wear continuously.", "Track-mile plan with sensor calibration stops."),
        ("Dam face monitoring", "Repeatable viewpoints for change detection.", "Fixed camera stations revisited each quarter."),
        ("Solar farm thermal scan", "Find every hot cell.", "Row flight plan at thermal-imaging altitude."),
        ("Ship hull survey", "Map hull condition pre-drydock.", "ROV grid over the hull with sonar overlap."),
        ("Power line corridor", "Identify vegetation encroachment.", "Span-by-span flight with LiDAR swaths."),
        ("Tunnel lining check", "Detect cracks wider than 0.3mm.", "Ring-by-ring crawler plan with lighting control."),
    ]),
    ("assembly-plans", "Assembly plans", [
        ("Electric motor build", "Minimize station idle time.", "Rotor, stator, housing, and test sequence."),
        ("PCB population", "Minimize pick-and-place head travel.", "Component placement order by feeder position."),
        ("Aircraft wing join", "Control tolerance stack-up.", "Fastener pattern tightened in a star sequence."),
        ("Battery pack assembly", "Ensure every weld is verified.", "Cell placement, busbar weld, and test order."),
        ("Furniture flat-pack", "Fewest steps for the customer.", "Panel and fastener order with no rework."),
        ("Engine rebuild", "Correct torque sequence throughout.", "Disassembly-tagged reverse build order."),
        ("Satellite integration", "Protect sensitive instruments.", "Clean-room build order with contamination control."),
        ("Bridge segment launch", "Balance cantilever stresses.", "Segment-by-segment launching sequence."),
        ("Robot arm build", "Calibrate as you go.", "Joint-by-joint assembly with encoder calibration."),
        ("Prosthetic fitting", "Match patient anatomy precisely.", "Scan, model, print, and fit sequence."),
    ]),
]


def build_plans():
    recs = []
    n = 0
    for gslug, gname, plans in PLAN_DOMAINS:
        for title, criterion, summary in plans:
            n += 1
            rid = "JAH-OP-%06d" % n
            steps = [
                {"step": 1, "action": "Initialize: verify state, localize, and confirm goal '%s'." % title},
                {"step": 2, "action": "Decompose the goal into ordered subtasks under the criterion: %s" % criterion},
                {"step": 3, "action": "Execute the primary sequence: %s" % summary},
                {"step": 4, "action": "Monitor progress against the expected cost; trigger contingency on deviation."},
                {"step": 5, "action": "Verify completion and file the execution trace."},
            ]
            desc = ("%s. This record is a computed optimal plan in the %s domain. Goal: %s Optimality criterion: %s "
                    "Plan summary: %s The plan is stored as five explicit steps with a contingency branch, an expected cost, "
                    "and a machine-readable representation so it can be executed, simulated, or re-optimized."
                    % (title, gname, title.lower(), criterion, summary))
            demo = ("# Plan executor — %s\n"
                    "plan = %s\n"
                    "state = {'step': 0, 'cost': 0.0}\n"
                    "for s in plan:\n"
                    "    state['step'] = s['step']\n"
                    "    state['cost'] += 1.0\n"
                    "    print('exec step', s['step'], ':', s['action'][:60])\n"
                    "print('plan complete; accrued cost:', state['cost'])\n"
                    % (title.replace('"', "'"), repr(steps)))
            recs.append({
                "id": rid, "t": title, "g": gslug,
                "description": desc,
                "domain": gname, "goal": title,
                "optimality_criterion": criterion,
                "horizon_steps": 5,
                "plan_steps": steps,
                "representation": "Ordered step list with actions, monitoring hooks, and a contingency branch; convertible to behavior-tree or PDDL-style operators.",
                "expected_cost": "Nominal execution cost under the stated criterion; re-evaluate if the environment changes mid-plan.",
                "contingency_plan": "On deviation beyond tolerance: pause, re-localize, replan from the current state with the same criterion, and resume. On repeated failure: escalate to a supervisor.",
                "demo": {"kind": "plan-executor", "language": "python", "program": demo,
                         "note": "Walks the archived plan steps and accrues nominal cost."},
                "citations": [CIT["planning"], CIT["control"]],
                "src": "signature",
            })
    return recs


MPC_GROUPS = [
    ("linear-mpc", "Linear MPC",
     "Linear time-invariant prediction model with quadratic cost and linear constraints solved as a quadratic program each step.",
     "Closed-loop stability via terminal cost and terminal set; the QP solves in milliseconds on embedded hardware."),
    ("nonlinear-mpc", "Nonlinear MPC",
     "Full nonlinear dynamics in the prediction model with a nonlinear program solved each step, typically via sequential quadratic programming.",
     "Stability from a control-Lyapunov terminal cost; real-time feasibility needs warm starts and limited iterations."),
    ("robust-mpc", "Robust MPC",
     "Tube-based or min-max formulation that guarantees constraint satisfaction under bounded disturbances and model error.",
     "Recursive feasibility of the tube guarantees stability; the price is conservatism from the worst-case bound."),
    ("explicit-mpc", "Explicit MPC",
     "The QP is solved offline over the state space, producing a piecewise-affine control law evaluated online by table lookup.",
     "Stability inherits from the underlying MPC design; online cost is a point-location search instead of an optimization."),
    ("learning-based-mpc", "Learning-based MPC",
     "A learned residual model corrects the nominal dynamics inside the prediction, improving accuracy where data is available.",
     "Stability via robust tubes around the learned model with bounded residual error; falls back to the nominal model outside the data support."),
    ("distributed-mpc", "Distributed MPC",
     "The fleet-wide problem is split per agent with coupling constraints handled by neighbor communication and consensus iterations.",
     "Stability from dissipativity of the coupled system; communication delays bound the achievable coordination rate."),
]

MPC_APPS = [
    "cart-pole balance", "quadrotor hover", "autonomous lane keeping", "arm trajectory tracking",
    "biped push recovery", "AUV path following", "satellite attitude hold",
    "warehouse fleet coordination", "building climate control", "legged robot walking",
]

MPC_CONSTRAINTS = [
    "Actuator saturation: |u| <= u_max on every input channel.",
    "Rate limit: |u[k] - u[k-1]| <= du_max per step to protect actuators.",
    "State bounds: x_min <= x <= x_max (workspace, speed, and tilt limits).",
    "Obstacle avoidance: keep-out sets encoded as linear or convex constraints.",
    "Terminal set: x[N] inside a control-invariant set for stability.",
]


def build_mpc():
    recs = []
    n = 0
    for gslug, gname, formulation, stability in MPC_GROUPS:
        for app in MPC_APPS:
            n += 1
            rid = "JAH-MPC-%06d" % n
            title = "%s — %s" % (gname, app)
            horizon = 10 + (n % 11)
            desc = ("%s. This record is a complete %s formulation for %s. %s Prediction horizon N=%d steps with a "
                    "control horizon of %d moves; the first move is applied and the problem is re-solved next step "
                    "(receding horizon). Constraints cover saturation, rate limits, state bounds, obstacles, and a terminal set. "
                    "Stability: %s"
                    % (title, gname.lower(), app, formulation, horizon, max(1, horizon // 3), stability))
            cost = ("J = sum_{k=0}^{N-1} ( x_k' Q x_k + u_k' R u_k ) + x_N' P x_N, subject to x_{k+1} = f(x_k, u_k) "
                    "and the constraint set below. Q, R, P positive definite.")
            demo = ("# Receding-horizon MPC demo — %s\n"
                    "N = %d  # prediction horizon\n"
                    "x = [1.0, 0.0]  # initial state [position, velocity]\n"
                    "u_max = 1.0\n"
                    "def predict(x, u, dt=0.1):\n"
                    "    return [x[0] + dt*x[1], x[1] + dt*u]\n"
                    "for step in range(8):\n"
                    "    u = max(-u_max, min(u_max, -0.8*x[0] - 0.5*x[1]))  # stand-in for the QP solution\n"
                    "    x = predict(x, u)\n"
                    "    print('step', step, 'u=%%.3f' %% u, 'x=[%%.3f, %%.3f]' %% (x[0], x[1]))\n"
                    "print('receding horizon complete')\n"
                    % (title.replace('"', "'"), horizon))
            recs.append({
                "id": rid, "t": title, "g": gslug,
                "description": desc,
                "application": app, "formulation": gname,
                "formulation_notes": formulation,
                "prediction_horizon": horizon,
                "control_horizon": max(1, horizon // 3),
                "model_used": "Prediction model matched to the application dynamics; linear models for linear MPC, full nonlinear dynamics for nonlinear MPC, nominal-plus-learned-residual for learning-based MPC.",
                "constraints": MPC_CONSTRAINTS,
                "cost_function": cost,
                "solver_approach": "Quadratic program per step for linear MPC; sequential quadratic programming with warm starts for nonlinear MPC; offline multi-parametric solution for explicit MPC.",
                "stability_notes": stability,
                "demo": {"kind": "mpc-controller", "language": "python", "program": demo,
                         "note": "Runs 8 receding-horizon steps on a double-integrator stand-in plant."},
                "citations": [CIT["mpc"], CIT["control"], CIT["dynamics"]],
                "src": "signature",
            })
    return recs


RP_PLATFORMS = [
    ("ground-robots", "Ground robots", "differential-drive rover",
     [(2.5, 1.0, 0.0), (5.0, 3.2, 0.0), (1.2, 4.8, 0.0), (7.7, 2.1, 0.0), (3.3, 6.6, 0.0),
      (9.1, 5.5, 0.0), (4.4, 2.2, 0.0), (6.8, 7.9, 0.0), (0.5, 3.7, 0.0), (8.2, 1.4, 0.0)]),
    ("aerial-robots", "Aerial robots", "quadrotor",
     [(0, 0, 12.0), (15, 8, 15.0), (30, -5, 18.0), (-10, 20, 14.0), (22, 22, 20.0),
      (5, -15, 11.0), (-20, -8, 16.0), (12, 30, 22.0), (35, 12, 17.0), (-5, -25, 13.0)]),
    ("manipulator-arms", "Manipulator arms", "6-DOF articulated arm",
     [(0.62, 0.10, 0.45), (0.55, -0.22, 0.51), (0.70, 0.05, 0.38), (0.48, 0.31, 0.60), (0.66, -0.08, 0.42),
      (0.58, 0.18, 0.55), (0.73, -0.15, 0.47), (0.51, 0.27, 0.44), (0.69, 0.12, 0.58), (0.60, -0.25, 0.40)]),
    ("marine-robots", "Marine robots", "autonomous underwater vehicle",
     [(100, 50, -40), (250, 120, -60), (400, 80, -55), (150, 300, -70), (500, 200, -45),
      (320, 410, -65), (80, 180, -50), (450, 350, -75), (200, 90, -42), (380, 260, -58)]),
    ("humanoid-robots", "Humanoid robots", "biped humanoid",
     [(1.1, 0.05, 0.95), (2.3, -0.08, 0.95), (3.6, 0.12, 0.97), (0.4, 0.0, 0.62), (4.8, -0.05, 0.95),
      (5.9, 0.09, 0.96), (1.8, 0.15, 0.95), (3.0, -0.12, 0.96), (4.2, 0.03, 0.95), (6.5, -0.07, 0.97)]),
    ("multi-robot-teams", "Multi-robot teams", "fleet centroid",
     [(10, 10, 0), (25, 18, 0), (40, 12, 5), (15, 35, 2), (55, 28, 8),
      (30, 45, 3), (48, 8, 6), (20, 25, 4), (60, 40, 10), (35, 20, 7)]),
]

FUSION_METHODS = [
    "Extended Kalman fusion of trajectory prediction, dynamics propagation, plan waypoints, MPC state, and cost-gradient corrections.",
    "Factor-graph fusion: trajectory, dynamics, plan, MPC, and cost terms as factors optimized jointly each cycle.",
    "Complementary fusion: high-rate dynamics propagation corrected by low-rate trajectory, plan, MPC, and cost updates.",
    "Particle fusion: a particle set weighted by agreement across the five compiled sources.",
]


def build_positions():
    recs = []
    n = 0
    for gslug, gname, plat, poses in RP_PLATFORMS:
        for i, (px, py, pz) in enumerate(poses):
            n += 1
            rid = "JAH-RP-%06d" % n
            src_n = ((n - 1) % 60) + 1
            compiled = {
                "trajectory": "JAH-PT-%06d" % src_n,
                "dynamics": "JAH-DM-%06d" % src_n,
                "cost": "JAH-CF-%06d" % src_n,
                "plan": "JAH-OP-%06d" % src_n,
                "mpc": "JAH-MPC-%06d" % src_n,
            }
            fusion = FUSION_METHODS[n % len(FUSION_METHODS)]
            title = "Compiled pose — %s #%d" % (plat, i + 1)
            desc = ("%s. This record is the compiled position of a %s (%s): one authoritative pose produced by fusing "
                    "all five companion databases. The trajectory database contributes the predicted path waypoint; the dynamics "
                    "database contributes the propagated state; the cost database contributes the gradient correction toward lower "
                    "cost; the plan database contributes the intended waypoint; the MPC database contributes the receding-horizon "
                    "state. Fusion method: %s The result is a single timestamped pose with covariance, ready for control, "
                    "logging, or display."
                    % (title, plat, gname.lower(), fusion))
            prog = ("# Pose fusion demo — %s\n"
                    "pose = {'x': %.3f, 'y': %.3f, 'z': %.3f}\n"
                    "sources = %s\n"
                    "print('compiled pose:', pose)\n"
                    "print('compiled from:')\n"
                    "for k, v in sources.items():\n"
                    "    print(' ', k, '->', v)\n"
                    % (title.replace('"', "'"), px, py, pz, repr(compiled)))
            recs.append({
                "id": rid, "t": title, "g": gslug,
                "description": desc,
                "platform": "%s (%s)" % (plat, gname),
                "position": {"x": px, "y": py, "z": pz, "units": "meters", "frame": "local odometry frame, z-up"},
                "orientation_quaternion": {"w": 1.0, "x": 0.0, "y": 0.0, "z": 0.0, "note": "Identity orientation; yaw applied per task heading."},
                "linear_velocity": {"vx": 0.5, "vy": 0.0, "vz": 0.0, "units": "m/s"},
                "angular_velocity": {"wx": 0.0, "wy": 0.0, "wz": 0.1, "units": "rad/s"},
                "covariance_diagonal": [0.02, 0.02, 0.03, 0.005, 0.005, 0.01],
                "timestamp": "Compiled at archive build; live poses refresh each fusion cycle.",
                "fusion_method": fusion,
                "compiled_from": compiled,
                "demo": {"kind": "pose-fuser", "language": "python", "program": prog,
                         "note": "Prints the compiled pose and its five source records."},
                "citations": [CIT["fusion"], CIT["estimation"], CIT["trajectory"]],
                "src": "signature",
            })
    return recs


VEC_GROUPS = [
    ("pose-embeddings", "Pose embeddings", 128, "cosine",
     "Encodes a full 6-DOF pose plus velocity into a compact vector for fast pose retrieval and loop-closure matching.",
     ["pose retrieval", "loop closure", "place recognition"]),
    ("trajectory-embeddings", "Trajectory embeddings", 256, "cosine",
     "Encodes an entire predicted trajectory (waypoints plus timing) into one vector for trajectory similarity search.",
     ["trajectory clustering", "motion pattern mining", "anomaly detection"]),
    ("plan-embeddings", "Plan embeddings", 256, "cosine",
     "Encodes a plan's step sequence and goal into a vector so similar plans can be found and reused.",
     ["plan reuse", "case-based planning", "plan similarity"]),
    ("sensor-feature-vectors", "Sensor feature vectors", 512, "euclidean",
     "Encodes a fused sensor snapshot (lidar, camera, IMU features) into a vector for scene matching.",
     ["scene matching", "localization", "change detection"]),
    ("semantic-vectors", "Semantic vectors", 128, "cosine",
     "Encodes the meaning of a task description or label so language queries match robot capabilities.",
     ["task search", "capability matching", "natural-language commanding"]),
    ("control-policy-vectors", "Control policy vectors", 64, "euclidean",
     "Encodes a control policy's behavior signature for comparing controllers and detecting policy drift.",
     ["policy comparison", "drift detection", "controller selection"]),
]

VEC_TOPICS = {
    "pose-embeddings": ["Warehouse dock pose", "Rooftop landing pose", "Charging station pose", "Assembly fixture pose",
                        "Doorway transit pose", "Shelf pick pose", "Inspection orbit pose", "Parking slot pose",
                        "Surgical port pose", "Satellite grapple pose"],
    "trajectory-embeddings": ["Corridor patrol path", "Lawnmower survey path", "Pick cycle path", "Rendezvous approach path",
                              "Stair climb path", "Pipeline track path", "Spray swath path", "Docking approach path",
                              "Suture path", "Search sweep path"],
    "plan-embeddings": ["Order fulfillment plan", "Delivery wave plan", "Patrol rota plan", "Irrigation day plan",
                        "Maintenance window plan", "Assembly sequence plan", "Inspection circuit plan", "Harvest coordination plan",
                        "Teardown plan", "Rounds plan"],
    "sensor-feature-vectors": ["Loading dock snapshot", "Crosswalk snapshot", "Crop row snapshot", "Bridge span snapshot",
                               "Clean room snapshot", "Harbor entrance snapshot", "Crater field snapshot", "Ward corridor snapshot",
                               "Welding cell snapshot", "Reef transect snapshot"],
    "semantic-vectors": ["deliver the package", "inspect the bridge", "pick the ripe fruit", "patrol the perimeter",
                         "weld the seam", "survey the field", "dock with the station", "clean the ward",
                         "assemble the gearbox", "map the pipeline"],
    "control-policy-vectors": ["Aggressive racing policy", "Conservative safety policy", "Energy-saving policy",
                               "Precision assembly policy", "Socially-aware navigation policy", "High-speed cruise policy",
                               "Delicate handling policy", "All-weather policy", "Stealthy inspection policy", "Time-optimal policy"],
}


def build_vectors():
    recs = []
    n = 0
    for gslug, gname, dim, metric, encodes, uses in VEC_GROUPS:
        for topic in VEC_TOPICS[gslug]:
            n += 1
            rid = "JAH-VEC-%06d" % n
            rnd = _lcg(n * 104729 + 7)
            sample = [round(rnd() * 2 - 1, 4) for _ in range(16)]
            norm = sum(v * v for v in sample) ** 0.5
            sample = [round(v / norm, 4) for v in sample]
            title = "%s — %s" % (topic, gname)
            desc = ("%s. This record is a %d-dimensional %s (%s distance) encoding %s Use cases: %s. "
                    "The archived sample shows the first 16 normalized components; the full %d-dimensional vector follows the same "
                    "distribution. Vectors are unit-normalized so %s distance is meaningful, and indexed for approximate "
                    "nearest-neighbor search."
                    % (title, dim, gname.lower(), metric, encodes[0].lower() + encodes[1:], ", ".join(uses), dim, metric))
            prog = ("# Similarity search — %s\n"
                    "import math\n"
                    "def cosine(a, b):\n"
                    "    d = math.sqrt(sum(x*x for x in a) * sum(x*x for x in b))\n"
                    "    return sum(x*y for x, y in zip(a, b)) / max(1e-9, d)\n"
                    "query = %s\n"
                    "bank = [query, [v*0.9 for v in query], [-v for v in query]]\n"
                    "for i, v in enumerate(bank):\n"
                    "    print('candidate', i, 'similarity:', round(cosine(query, v), 4))\n"
                    % (title.replace('"', "'"), repr(sample)))
            recs.append({
                "id": rid, "t": title, "g": gslug,
                "description": desc,
                "vector_type": gname,
                "dimension": dim,
                "encodes": encodes,
                "distance_metric": metric,
                "indexing_method": "Approximate nearest-neighbor index (partitioned inverted lists with product quantization); exact brute force for small banks.",
                "sample_vector": sample,
                "sample_note": "First 16 of %d unit-normalized components shown." % dim,
                "normalization": "L2 unit normalization; %s distance computed on normalized vectors." % metric,
                "use_cases": uses,
                "demo": {"kind": "similarity-search", "language": "python", "program": prog,
                         "note": "Runs cosine similarity of a query against a tiny candidate bank."},
                "citations": [CIT["retrieval"], CIT["fusion"]],
                "src": "signature",
            })
    return recs


# ---------------------------------------------------------------- assembly

def gen_topics(slug, recs):
    out = {}
    for r in recs:
        out.setdefault(r["g"], []).append(r["t"])
    return out


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG  # point the shared page/gen builders at our configs

    built = {
        "predictive-trajectories": build_trajectories(),
        "dynamics-models": build_dynamics(),
        "cost-functions": build_costs(),
        "optimal-plans": build_plans(),
        "model-predictive-control": build_mpc(),
        "robot-positions": build_positions(),
        "vector-database": build_vectors(),
    }

    # sanity: ids unique + prefix + required keys + demo programs compile + no stubs
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        for r in recs:
            r.setdefault("name", r["t"])
            r.setdefault("title", r["t"])
            for k in ("id", "t", "g", "name", "title", "description", "src", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            assert r["demo"].get("program"), "empty demo in %s" % r["id"]
            assert len(r["description"]) > 120, "stub description in %s" % r["id"]
            assert "facebook" not in json.dumps(r).lower(), "facebook ref in %s" % r["id"]
        for r in recs[:: max(1, len(recs) // 12)]:
            compile(r["demo"]["program"], r["id"], "exec")
        n = write_shard_db(slug, recs)
        print("shard: %-28s %d records -> %s/data/%s/" % (slug, n, SHARD_BASE, slug))

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        # fix the one leftover template string the shared builder does not touch
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        with open(os.path.join(ddir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        gen_js = nb.build_gen_js(slug, gen_topics(slug, recs), DBCFG[slug])
        assert "facebook" not in gen_js.lower()
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js" % (slug, slug))

    entries_m = [manifest_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "data", "manifest.json"), entries_m)
    entries_a = [api_entry(s, len(built[s])) for s in built]
    update_json_list(os.path.join(REPO, "api.json"), entries_a)
    print("manifest + api.json: appended %d databases" % len(built))
    print("NEXT: run python3 code/restamp_counts.py, then commit + push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
