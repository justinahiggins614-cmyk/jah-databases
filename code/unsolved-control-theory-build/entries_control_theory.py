#!/usr/bin/env python3
"""Entries for The Unsolved Control Theory Database (unsolved-control-theory) and its
Signature half (unsolved-control-theory-signature).

34 famous unsolved problems in control theory, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USCT- / JAH-USCTS- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "control-theory",
 "disp": "control theory",
 "name": "The Unsolved Control Theory Database",
 "sig_name": "The Unsolved Control Theory Signature Database",
 "prefix": "JAH-USCT-",
 "sig_prefix": "JAH-USCTS-",
 "ai": "JAH Unsolved Control Theory Archivist",
 "tagline": ("Thirty-four famous open problems in control theory, from PID tuning to the unified theory of "
             "control: real, fact-checked, each with its full story and a clearly labeled Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of control theory: "
                 "Signature-generated proposed solutions with assumptions declared, confirm and refute conditions "
                 "stated, and limits honestly marked. Clearly labeled Signature-made, never established science."),
 "pub_line": ("Public records - 34 famous open problems in control theory, real and fact-checked: PID tuning, "
              "controllability, observability, state estimation, LQR design, pole placement, stability margins, "
              "time delays, actuator saturation, disturbance rejection, and tracking - every record carrying the "
              "problem statement, background, why it matters, key points, requirements, standards, citations, "
              "and a working solution-explorer demonstration, organized in the Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "control theory problems approached as a covenant between the known and the unknown, each carrying "
              "the full Signature-generated proposed solution with its assumptions declared, its confirm and "
              "refute conditions stated, and its limits honestly marked. Clearly labeled Signature-made, never "
              "presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (PID tuning, controllability, "
                 "observability, state estimation, LQR design, pole placement, stability margins, time delays, "
                 "saturation, disturbance rejection, tracking) -> Compounded (robust control, H-infinity, mu "
                 "synthesis, adaptive control, model predictive control, nonlinear control, feedback "
                 "linearization, sliding mode, Lyapunov design, passivity, hybrid systems, switched systems) -> "
                 "Advanced (distributed control, decentralized control, networked control, multi-agent consensus, "
                 "formation control, cyber-physical security, learning-based control, RL safety, data-driven "
                 "control, quantum control, unified control theory)."),
 "search_ph": ("Search PID, controllability, robust control, MPC, adaptive control, consensus, reinforcement "
               "learning..."),
 "chat_ph": "Ask about the great open problems of control theory...",
 "greet_pub": ("I am the JAH Unsolved Control Theory Archivist. Ask me about the great open problems of control "
               "theory - from PID tuning, controllability, and state estimation through robust and adaptive "
               "control, to consensus, learning-based control, and the unified theory."),
 "greet_sig": ("I am the JAH Unsolved Control Theory Archivist (Signature). Ask me about the Signature proposed "
               "solutions to the great open problems of control theory - every approach labeled as a proposal, "
               "never established science."),
 "role_pub": ("unsolved control theory archivist - the great open problems of control theory, from PID tuning, "
              "controllability, and state estimation through robust and adaptive control, to consensus, "
              "learning-based control, and the unified theory; teaches progressively along the ladder from "
              "foundations through compounded to advanced; answers from many angles - definition, example, "
              "analogy, application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved control theory archivist - Signature editions: his original Signature solution method "
              "applied to the 34 great open problems of control theory, each carrying the full "
              "Signature-generated proposed solution, clearly labeled Signature-made and never presented as "
              "established science; teaches progressively along the ladder from foundations through compounded "
              "to advanced; answers from many angles - definition, example, analogy, application, history, "
              "math - using only archive data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved control theory studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Ogata, Modern Control Engineering; Khalil, Nonlinear Systems).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "ct-pid",
 "name": "The PID Tuning Problem",
 "group": "Classical Control",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "PID controls most industrial loops - but how can the three gains be tuned optimally for unknown or changing plants?",
 "background": "The PID-tuning problem - Ziegler-Nichols (1942) to modern optimization - persists because the plants are unknown, nonlinear, and time-varying: the tuning rules assume models the plants violate; the auto-tuners (relay, adaptive) work partially; and the performance-robustness tradeoff has no universal optimum. The most-used controller is tuned by rules of thumb. The industry's workhorse is tuned by heuristics.",
 "why_it_matters": "PID runs industry. The heuristic tuning is the performance left on the table.",
 "sig_lens": "The Signature lens reads PID as the workhorse: the protocol must tune it systematically - model-free optimization with robustness guarantees.",
 "sig_solution": LABEL + " Assumptions: (1) plants unknown, nonlinear, time-varying; (2) rules assume violated models. Reasoning path: tune data-driven - model-free optimization with robustness constraints. Proposed mechanism: a workhorse protocol with data-driven PID optimization, robustness-constrained tuning, and auto-tuner standardization. Confirm: the tuned loops outperform rules-of-thumb. Kill: the plants defeat data-driven tuning. Does NOT claim: the optimal PID - it tunes systematically.",
 "pointer": "The Signature system's proposed approach tunes PID data-driven with robustness constraints; the companion Signature Edition record specifies the workhorse protocol.",
 "key_points": [
  "PID controls most industrial loops.",
  "Ziegler-Nichols (1942) still used.",
  "Plants unknown, nonlinear, time-varying.",
  "Auto-tuners work partially.",
 ],
 "requirements": [
  "Data-driven PID optimization.",
  "Robustness-constrained tuning.",
  "Auto-tuner standardization.",
 ],
 "citations": [
  "Ziegler JG, Nichols NB (1942) Optimum settings for automatic controllers. Trans. ASME 64.",
 ],
 "demo": {"zeta": 0.7, "wn": 2.0},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "ct-controllability",
 "name": "The Controllability Problem",
 "group": "State Space",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Can the system be steered anywhere - and if the controllability test passes barely, is the system really controllable in practice?",
 "background": "The controllability problem - Kalman's rank test is binary, but the practical controllability (the control energy needed) varies enormously: the controllability Gramian's smallest eigenvalue measures the hardest direction; the actuator placement (where to put the inputs) is the design question; and the large-scale systems' controllability is computationally hard. The binary test passes; the energy bill may be infinite.",
 "why_it_matters": "Controllability decides actuator placement and design feasibility. The binary test hides the energy cost.",
 "sig_lens": "The Signature lens reads controllability as the steering: the protocol must price the steering (Gramian energy) - and place the wheel (actuators) optimally.",
 "sig_solution": LABEL + " Assumptions: (1) rank test binary; (2) control energy varies enormously. Reasoning path: quantify and optimize - Gramian-based energy metrics with actuator-placement optimization. Proposed mechanism: a steering protocol with controllability-energy quantification, optimal actuator placement, and large-scale approximations. Confirm: the placed actuators control efficiently. Kill: the optimization proves intractable. Does NOT claim: the systems controllable cheaply - it prices the steering.",
 "pointer": "The Signature system's proposed approach quantifies controllability energy and optimizes actuator placement; the companion Signature Edition record specifies the steering protocol.",
 "key_points": [
  "Kalman rank test: binary controllability.",
  "Gramian eigenvalues measure control energy.",
  "Actuator placement is the design question.",
  "Large-scale controllability computationally hard.",
 ],
 "requirements": [
  "Controllability-energy quantification.",
  "Optimal actuator placement.",
  "Large-scale approximations.",
 ],
 "citations": [
  "Kalman RE (1960) On the general theory of control systems. Proc. IFAC Congress.",
 ],
 "demo": {"zeta": 0.5, "wn": 3.0},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "ct-observability",
 "name": "The Observability Problem",
 "group": "State Space",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Can the internal state be inferred from outputs - and where should sensors go for the best state reconstruction?",
 "background": "The observability problem - the dual of controllability - has the same binary-vs-quantitative gap: the observability Gramian measures the reconstruction quality; the sensor placement (dual of actuator placement) is the design question; and the nonlinear observability (Lie-algebraic rank conditions) is harder. The sensors are placed; their information is half-measured.",
 "why_it_matters": "Observability decides sensor placement. The binary test hides the reconstruction quality.",
 "sig_lens": "The Signature lens reads observability as the seeing: the protocol must measure the sight (Gramian) - and place the eyes (sensors) optimally.",
 "sig_solution": LABEL + " Assumptions: (1) binary test hides quality; (2) nonlinear observability harder. Reasoning path: quantify and place - observability-Gramian metrics with optimal sensor placement. Proposed mechanism: a seeing protocol with observability-quality quantification, optimal sensor placement, and nonlinear observability methods. Confirm: the placed sensors reconstruct well. Kill: the nonlinear case defeats. Does NOT claim: the states observable cheaply - it measures the sight.",
 "pointer": "The Signature system's proposed approach quantifies observability and optimizes sensor placement; the companion Signature Edition record specifies the seeing protocol.",
 "key_points": [
  "Observability: dual of controllability.",
  "Gramian measures reconstruction quality.",
  "Sensor placement the design question.",
  "Nonlinear observability Lie-algebraic.",
 ],
 "requirements": [
  "Observability-quality quantification.",
  "Optimal sensor placement.",
  "Nonlinear observability methods.",
 ],
 "citations": [
  "Hermann R, Krener AJ (1977) Nonlinear controllability and observability. IEEE Trans. Automatic Control 22.",
 ],
 "demo": {"zeta": 0.9, "wn": 1.5},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "ct-estimation",
 "name": "The State Estimation Problem",
 "group": "State Space",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Estimating hidden states from noisy measurements - but how can the estimator be optimal when the models are wrong and the noise is non-Gaussian?",
 "background": "The estimation problem - Kalman filter optimal for linear-Gaussian, extended/unscented/particle filters for the rest - faces the model-mismatch reality: the process models are approximate, the noise is non-Gaussian, and the tuning (covariances) is heuristic. The robust filters (H-infinity) trade optimality for robustness. The estimator is optimal - for the wrong model.",
 "why_it_matters": "State estimation feeds every feedback loop. The wrong-model optimality is the loop's hidden error.",
 "sig_lens": "The Signature lens reads estimation as the guessing: the protocol must guess robustly - for the approximate model, not the ideal one.",
 "sig_solution": LABEL + " Assumptions: (1) models approximate; noise non-Gaussian; (2) tuning heuristic. Reasoning path: estimate robustly - robust/adaptive filters with covariance learning. Proposed mechanism: a guessing protocol with robust filter designs, adaptive covariance estimation, and model-mismatch quantification. Confirm: the robust estimators outperform. Kill: the mismatch defeats. Does NOT claim: the optimal estimator - it guesses robustly.",
 "pointer": "The Signature system's proposed approach builds robust adaptive state estimators; the companion Signature Edition record specifies the guessing protocol.",
 "key_points": [
  "Kalman optimal for linear-Gaussian only.",
  "EKF/UKF/particle filters for nonlinear.",
  "Process models approximate; noise non-Gaussian.",
  "Covariance tuning heuristic.",
 ],
 "requirements": [
  "Robust filter designs.",
  "Adaptive covariance estimation.",
  "Model-mismatch quantification.",
 ],
 "citations": [
  "Kalman RE (1960) A new approach to linear filtering and prediction problems. Trans. ASME 82.",
 ],
 "demo": {"zeta": 0.6, "wn": 2.5},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "ct-lqr",
 "name": "The LQR Design Problem",
 "group": "Optimal Control",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "LQR gives optimal state feedback - but how should the Q and R weights be chosen when the tradeoff is the real design decision?",
 "background": "The LQR problem - the Riccati solution is elegant, but the Q/R weight selection is the design: the weights encode the state-vs-effort tradeoff that the designer must choose; the Bryson's-rule heuristics guide; and the robustness (LQR's guaranteed margins) is the comfort. The optimal control is optimal - for the chosen weights.",
 "why_it_matters": "LQR is the optimal-control workhorse. The weight choice - the design - is heuristic.",
 "sig_lens": "The Signature lens reads LQR as the optimal answer to the chosen question: the protocol must choose the question (weights) systematically - from the specifications.",
 "sig_solution": LABEL + " Assumptions: (1) Riccati solution elegant; (2) weights encode the design tradeoff. Reasoning path: select weights from specifications - inverse-optimal and multi-objective methods. Proposed mechanism: a question protocol with specification-driven weight selection, Pareto-frontier tradeoff exploration, and robustness verification. Confirm: the selected weights meet specs. Kill: the tradeoff stays heuristic. Does NOT claim: the optimal weights - it chooses the question systematically.",
 "pointer": "The Signature system's proposed approach selects LQR weights from specifications; the companion Signature Edition record specifies the question protocol.",
 "key_points": [
  "LQR: Riccati-based optimal state feedback.",
  "Q/R weights encode state-vs-effort tradeoff.",
  "Bryson's rule: heuristic guidance.",
  "Guaranteed stability margins.",
 ],
 "requirements": [
  "Specification-driven weight selection.",
  "Pareto tradeoff exploration.",
  "Robustness verification.",
 ],
 "citations": [
  "Anderson BDO, Moore JB (1990) Optimal Control: Linear Quadratic Methods. Prentice Hall.",
 ],
 "demo": {"zeta": 0.8, "wn": 2.0},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "ct-pole-placement",
 "name": "The Pole Placement Problem",
 "group": "State Space",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Placing closed-loop poles sets the response - but which pole locations are achievable under actuator limits and robustness needs?",
 "background": "The pole-placement problem - Ackermann's formula places poles arbitrarily (for controllable systems), but the achievable performance is limited: the actuator saturation bounds the speed; the robustness (sensitivity to the placed locations) degrades for aggressive placements; and the zero dynamics constrain. The poles are placed; the limits are the design.",
 "why_it_matters": "Pole placement is the direct performance design. The ignored limits are the aggressive designs' fragility.",
 "sig_lens": "The Signature lens reads pole placement as the seating chart: the protocol must seat the poles where the actuators can serve them - and the robustness can tolerate.",
 "sig_solution": LABEL + " Assumptions: (1) arbitrary placement mathematically; (2) saturation and robustness limit. Reasoning path: place feasibly - constrained pole-region design with robustness metrics. Proposed mechanism: a seating protocol with feasible-region pole placement, robustness-constrained selection, and saturation-aware design. Confirm: the placed poles perform robustly. Kill: the feasible region too small. Does NOT claim: the arbitrary poles - it seats feasibly.",
 "pointer": "The Signature system's proposed approach places poles in feasible robust regions; the companion Signature Edition record specifies the seating protocol.",
 "key_points": [
  "Ackermann: arbitrary placement for controllable systems.",
  "Actuator saturation bounds achievable speed.",
  "Aggressive placements fragile.",
  "Zero dynamics constrain.",
 ],
 "requirements": [
  "Feasible-region pole placement.",
  "Robustness-constrained selection.",
  "Saturation-aware design.",
 ],
 "citations": [
  "Ackermann J (1972) Der Entwurf linearer Regelungssysteme im Zustandsraum. Regelungstechnik 20.",
 ],
 "demo": {"zeta": 1.0, "wn": 1.8},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "ct-margins",
 "name": "The Stability Margin Problem",
 "group": "Classical Control",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Gain and phase margins measure robustness - but are the classical margins sufficient for modern multivariable systems?",
 "background": "The margins problem - gain/phase margins are SISO concepts; the multivariable systems need the disk margins, the structured singular value - is the robustness-measure gap: the classical margins are still the industry standard; the modern measures are the theory standard. The gap is the certified-vs-practical robustness.",
 "why_it_matters": "Stability margins certify robustness. The SISO measures on MIMO systems are the false comfort.",
 "sig_lens": "The Signature lens reads margins as the safety buffer: the protocol must measure the buffer correctly - multivariable, not SISO - for the real system.",
 "sig_solution": LABEL + " Assumptions: (1) classical margins SISO; (2) modern measures underused. Reasoning path: certify multivariable - disk margins and mu-analysis in practice. Proposed mechanism: a buffer protocol with multivariable margin computation, industry-standard modern measures, and margin-based design. Confirm: the certified systems robust. Kill: the modern measures stay theoretical. Does NOT claim: the margins sufficient - it measures the buffer correctly.",
 "pointer": "The Signature system's proposed approach certifies multivariable stability margins; the companion Signature Edition record specifies the buffer protocol.",
 "key_points": [
  "Gain/phase margins: SISO concepts.",
  "MIMO needs disk margins, structured singular value.",
  "Classical margins industry standard.",
  "Modern measures theory standard.",
 ],
 "requirements": [
  "Multivariable margin computation.",
  "Modern-measure industry adoption.",
  "Margin-based design procedures.",
 ],
 "citations": [
  "Skogestad S, Postlethwaite I (2005) Multivariable Feedback Control. Wiley.",
 ],
 "demo": {"zeta": 0.4, "wn": 3.5},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "ct-delay",
 "name": "The Time Delay Problem",
 "group": "Classical Control",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Time delays destabilize loops - but how can delay systems be controlled when the delay is unknown or time-varying?",
 "background": "The delay problem - the Smith predictor compensates known delays; the unknown/varying delays need adaptive/robust methods - is the process-control reality: the delays are everywhere (transport, computation); the predictor's model-mismatch destabilizes; and the delay-margin is the robustness measure. The compensated delay is the fragile compensation.",
 "why_it_matters": "Delays are everywhere in process control. The fragile compensation is the destabilization risk.",
 "sig_lens": "The Signature lens reads delays as the echo: the protocol must predict the echo (predictor) - robustly, for the uncertain delay.",
 "sig_solution": LABEL + " Assumptions: (1) Smith predictor needs known delay; (2) mismatch destabilizes. Reasoning path: compensate robustly - delay-adaptive predictors with delay-margin guarantees. Proposed mechanism: an echo protocol with delay-estimation-adaptive predictors, delay-margin robustness analysis, and predictor-mismatch monitoring. Confirm: the compensated loops stable. Kill: the varying delays defeat. Does NOT claim: the delays compensated - it predicts the echo robustly.",
 "pointer": "The Signature system's proposed approach compensates time delays adaptively with margin guarantees; the companion Signature Edition record specifies the echo protocol.",
 "key_points": [
  "Smith predictor compensates known delays.",
  "Unknown/varying delays need adaptation.",
  "Model mismatch destabilizes predictors.",
  "Delay margin the robustness measure.",
 ],
 "requirements": [
  "Delay-adaptive predictors.",
  "Delay-margin analysis.",
  "Mismatch monitoring.",
 ],
 "citations": [
  "Smith OJ (1959) A controller to overcome dead time. ISA Journal 6.",
 ],
 "demo": {"zeta": 0.7, "wn": 1.2},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "ct-saturation",
 "name": "The Actuator Saturation Problem",
 "group": "Classical Control",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Actuators saturate - but how can the controller handle limits without windup and instability?",
 "background": "The saturation problem - integral windup, the directionality, the nested saturations - has the anti-windup fixes (conditioning, clamping) but the multivariable saturation (directionality: the saturated direction matters) is harder; the MPC handles constraints naturally (its advantage). The limited actuator is the linear design's unmodeled nonlinearity.",
 "why_it_matters": "Every actuator saturates. The unmodeled limits are the linear designs' instability.",
 "sig_lens": "The Signature lens reads saturation as the limited muscle: the protocol must respect the limits - anti-windup plus constraint-aware design.",
 "sig_solution": LABEL + " Assumptions: (1) anti-windup fixes SISO; (2) multivariable directionality harder. Reasoning path: respect limits - anti-windup plus constraint-aware (MPC-like) design. Proposed mechanism: a muscle protocol with anti-windup standardization, multivariable saturation handling, and constraint-aware control design. Confirm: the limited systems stable. Kill: the limits defeat linear designs. Does NOT claim: the saturation solved - it respects the muscle.",
 "pointer": "The Signature system's proposed approach handles actuator saturation with anti-windup and constraint-aware design; the companion Signature Edition record specifies the muscle protocol.",
 "key_points": [
  "Integral windup from saturation.",
  "Anti-windup: conditioning, clamping.",
  "Multivariable directionality harder.",
  "MPC handles constraints naturally.",
 ],
 "requirements": [
  "Anti-windup standardization.",
  "Multivariable saturation methods.",
  "Constraint-aware design.",
 ],
 "citations": [
  "Kothare MV et al. (1994) A unified framework for the study of anti-windup designs. Automatica 30.",
 ],
 "demo": {"zeta": 0.9, "wn": 2.8},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "ct-disturbance",
 "name": "The Disturbance Rejection Problem",
 "group": "Classical Control",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Disturbances perturb every loop - but how can unknown disturbances be rejected without knowing their models?",
 "background": "The disturbance problem - the internal model principle (reject what you model), the unknown-disturbance observers (ESO: extended state observer) - is the regulation challenge: the ADRC (active disturbance rejection) estimates and cancels the total disturbance; the performance-robustness tradeoff persists. The rejected disturbance is the estimated one.",
 "why_it_matters": "Disturbance rejection is control's main job. The estimated disturbances are the rejection's limit.",
 "sig_lens": "The Signature lens reads disturbances as the headwind: the protocol must feel the wind (estimate) - and lean into it (cancel) - without knowing its source.",
 "sig_solution": LABEL + " Assumptions: (1) internal model needs the disturbance model; (2) ESO estimates the total. Reasoning path: reject actively - disturbance-observer-based control with robustness. Proposed mechanism: a headwind protocol with disturbance-observer designs, ADRC deployment, and rejection-robustness analysis. Confirm: the disturbances rejected. Kill: the estimation lags the disturbance. Does NOT claim: the disturbances all rejected - it leans into the wind.",
 "pointer": "The Signature system's proposed approach rejects disturbances with observer-based active control; the companion Signature Edition record specifies the headwind protocol.",
 "key_points": [
  "Internal model principle: model to reject.",
  "ESO estimates the total disturbance.",
  "ADRC: estimate and cancel.",
  "Performance-robustness tradeoff.",
 ],
 "requirements": [
  "Disturbance-observer designs.",
  "ADRC deployment.",
  "Rejection-robustness analysis.",
 ],
 "citations": [
  "Han J (2009) From PID to active disturbance rejection control. IEEE Trans. Industrial Electronics 56.",
 ],
 "demo": {"zeta": 0.6, "wn": 3.2},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "ct-tracking",
 "name": "The Tracking Problem",
 "group": "Classical Control",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Following reference commands - but how can perfect tracking be achieved when the plant has non-minimum-phase zeros or delays?",
 "background": "The tracking problem - the fundamental limits (Bode's integral, the non-minimum-phase undershoot) - is the performance ceiling: the RHP zeros force the undershoot-vs-speed tradeoff; the delays limit the bandwidth; and the feedforward (model-inverse) helps where the model is known. The tracked reference is the limited one.",
 "why_it_matters": "Tracking is the servo's job. The fundamental limits are the performance ceiling.",
 "sig_lens": "The Signature lens reads tracking as the chase: the protocol must know the speed limit (RHP zeros, delays) - and chase optimally within it.",
 "sig_solution": LABEL + " Assumptions: (1) RHP zeros force tradeoffs; (2) feedforward helps where modeled. Reasoning path: track optimally - limit-aware feedforward/feedback with the tradeoffs explicit. Proposed mechanism: a chase protocol with fundamental-limit-aware design, model-based feedforward, and tradeoff-explicit specifications. Confirm: the tracking optimal within limits. Kill: the limits too restrictive. Does NOT claim: the perfect tracking - it chases within the speed limit.",
 "pointer": "The Signature system's proposed approach tracks within fundamental limits using feedforward; the companion Signature Edition record specifies the chase protocol.",
 "key_points": [
  "Bode integral: fundamental sensitivity limits.",
  "RHP zeros force undershoot-vs-speed tradeoff.",
  "Delays limit achievable bandwidth.",
  "Feedforward inverts the model where known.",
 ],
 "requirements": [
  "Limit-aware tracking design.",
  "Model-based feedforward.",
  "Explicit tradeoff specifications.",
 ],
 "citations": [
  "Bode HW (1945) Network Analysis and Feedback Amplifier Design. Van Nostrand.",
 ],
 "demo": {"zeta": 0.75, "wn": 2.2},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "ct-robust",
 "name": "The Robust Control Problem",
 "group": "Robust Control",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Models are always wrong - but how can controllers guarantee performance for all plants in an uncertainty set?",
 "background": "The robust-control problem - the small-gain theorem, the uncertainty modeling (multiplicative, coprime-factor) - is the guarantee challenge: the uncertainty sets are the designer's choice (conservative or risky); the robust-performance (not just stability) is harder; and the conservatism (guaranteeing for the worst case) costs performance. The guaranteed controller is the conservative one.",
 "why_it_matters": "Robustness is the controller's guarantee. The conservative guarantee is the performance cost.",
 "sig_lens": "The Signature lens reads robustness as the guarantee: the protocol must model the uncertainty honestly - and pay only the necessary conservatism.",
 "sig_solution": LABEL + " Assumptions: (1) uncertainty sets designer's choice; (2) conservatism costs performance. Reasoning path: guarantee efficiently - data-driven uncertainty sets with less-conservative robust design. Proposed mechanism: a guarantee protocol with uncertainty-set identification, less-conservative robust synthesis, and performance-robustness tradeoff optimization. Confirm: the guarantees hold with less cost. Kill: the uncertainty unmodelable. Does NOT claim: the perfect robustness - it guarantees efficiently.",
 "pointer": "The Signature system's proposed approach synthesizes robust controllers from data-driven uncertainty; the companion Signature Edition record specifies the guarantee protocol.",
 "key_points": [
  "Small-gain theorem: robustness foundation.",
  "Uncertainty sets: multiplicative, coprime-factor.",
  "Robust performance harder than robust stability.",
  "Conservatism costs performance.",
 ],
 "requirements": [
  "Data-driven uncertainty-set identification.",
  "Less-conservative robust synthesis.",
  "Tradeoff optimization.",
 ],
 "citations": [
  "Zhou K et al. (1996) Robust and Optimal Control. Prentice Hall.",
 ],
 "demo": {"zeta": 0.65, "wn": 2.6},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "ct-hinf",
 "name": "The H Infinity Problem",
 "group": "Robust Control",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "H-infinity optimizes worst-case performance - but how can the conservatism be reduced and the designs made practical?",
 "background": "The H-infinity problem - the Riccati/LMI solutions are elegant, but the worst-case optimization is conservative; the mixed H2/H-infinity trades average for worst-case; and the controller order (high) needs reduction. The practical H-infinity is the reduced-conservatism one.",
 "why_it_matters": "H-infinity is the robust-synthesis standard. Its conservatism is the practicality gap.",
 "sig_lens": "The Signature lens reads H-infinity as the worst-case optimizer: the protocol must tame the pessimism - mixed objectives, reduced order - for practice.",
 "sig_solution": LABEL + " Assumptions: (1) worst-case conservative; (2) high-order controllers. Reasoning path: practicalize - mixed H2/H-infinity with order reduction. Proposed mechanism: a pessimism protocol with mixed-objective synthesis, controller-order reduction, and application-tuned H-infinity. Confirm: the practical designs perform. Kill: the conservatism irreducible. Does NOT claim: the conservatism gone - it tames the pessimism.",
 "pointer": "The Signature system's proposed approach practicalizes H-infinity with mixed objectives; the companion Signature Edition record specifies the pessimism protocol.",
 "key_points": [
  "H-infinity: worst-case performance optimization.",
  "Riccati/LMI solutions elegant.",
  "Conservatism from worst-case focus.",
  "High-order controllers need reduction.",
 ],
 "requirements": [
  "Mixed H2/H-infinity synthesis.",
  "Controller-order reduction.",
  "Application-tuned designs.",
 ],
 "citations": [
  "Doyle JC et al. (1989) State-space solutions to standard H2 and H-infinity control problems. IEEE Trans. AC 34.",
 ],
 "demo": {"zeta": 0.55, "wn": 3.8},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "ct-mu",
 "name": "The Mu Synthesis Problem",
 "group": "Robust Control",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Structured uncertainty needs mu-synthesis - but how can the D-K iteration's conservatism and convergence be handled?",
 "background": "The mu problem - the structured singular value is NP-hard to compute; the D-K iteration approximates - is the structured-robustness challenge: the D-scales approximate; the iteration may not converge; and the resulting controllers are high-order. The structured guarantee is the approximated one.",
 "why_it_matters": "Mu-synthesis is the structured-robustness tool. Its approximations are the guarantee's fine print.",
 "sig_lens": "The Signature lens reads mu as the structured guarantee: the protocol must compute it reliably - and converge the iteration.",
 "sig_solution": LABEL + " Assumptions: (1) mu NP-hard; D-K approximates; (2) convergence not guaranteed. Reasoning path: compute reliably - improved mu bounds with convergent synthesis. Proposed mechanism: a structured protocol with mu-bound computation advances, convergent D-K variants, and order-reduced mu controllers. Confirm: the guarantees reliable. Kill: the NP-hardness bites. Does NOT claim: the mu computed exactly - it guarantees reliably.",
 "pointer": "The Signature system's proposed approach makes mu-synthesis convergent and reliable; the companion Signature Edition record specifies the structured protocol.",
 "key_points": [
  "Structured singular value: NP-hard.",
  "D-K iteration approximates.",
  "Convergence not guaranteed.",
  "High-order resulting controllers.",
 ],
 "requirements": [
  "Improved mu-bound computation.",
  "Convergent synthesis variants.",
  "Order-reduced mu controllers.",
 ],
 "citations": [
  "Packard A, Doyle J (1993) The complex structured singular value. Automatica 29.",
 ],
 "demo": {"zeta": 0.85, "wn": 1.6},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "ct-adaptive",
 "name": "The Adaptive Control Problem",
 "group": "Adaptive Control",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Adapting to unknown plants - but how can adaptation be stable, robust, and fast without bursting?",
 "background": "The adaptive problem - the bursting (parameter drift), the robustness (unmodeled dynamics destabilize), the persistent-excitation need - is the adaptation trilemma: the MRAC and self-tuning regulators adapt; the robust-adaptive (sigma-modification, projection) fixes the drift; and the excitation condition is the convergence price. The adapting controller is the cautious one.",
 "why_it_matters": "Adaptive control handles unknown plants. The bursting and fragility are the adaptation's risks.",
 "sig_lens": "The Signature lens reads adaptation as the learning: the protocol must learn stably - robust to the unmodeled, excited enough to converge.",
 "sig_solution": LABEL + " Assumptions: (1) bursting from parameter drift; (2) excitation needed. Reasoning path: adapt robustly - robust modifications with excitation management. Proposed mechanism: a learning protocol with robust-adaptive laws, excitation-condition monitoring, and transient-performance guarantees. Confirm: the adaptation stable and fast. Kill: the unmodeled dynamics defeat. Does NOT claim: the adaptation perfect - it learns cautiously.",
 "pointer": "The Signature system's proposed approach adapts robustly with excitation management; the companion Signature Edition record specifies the learning protocol.",
 "key_points": [
  "Bursting: parameter drift instability.",
  "Unmodeled dynamics destabilize adaptive loops.",
  "Persistent excitation needed for convergence.",
  "Robust modifications (sigma, projection) fix drift.",
 ],
 "requirements": [
  "Robust adaptive laws.",
  "Excitation monitoring.",
  "Transient-performance guarantees.",
 ],
 "citations": [
  "Astrom KJ, Wittenmark B (2008) Adaptive Control. Dover.",
 ],
 "demo": {"zeta": 0.7, "wn": 2.4},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "ct-mpc",
 "name": "The Model Predictive Control Problem",
 "group": "Predictive Control",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "MPC handles constraints optimally - but how can stability be guaranteed and the computation made real-time?",
 "background": "The MPC problem - the stability (terminal costs/constraints), the feasibility (recursive), the computation (QP at each step) - is the industry-standard challenge: the theory guarantees with terminal ingredients; the practice needs the speed (explicit MPC, fast solvers); and the nonlinear MPC is the frontier. The constrained optimum is the computed one.",
 "why_it_matters": "MPC is the advanced-control industry standard. Its guarantees and speed are the deployment's needs.",
 "sig_lens": "The Signature lens reads MPC as the looking-ahead: the protocol must guarantee the lookahead (stability) - and compute it in time.",
 "sig_solution": LABEL + " Assumptions: (1) terminal ingredients guarantee; (2) computation the bottleneck. Reasoning path: guarantee and accelerate - stabilizing MPC formulations with fast solvers. Proposed mechanism: a lookahead protocol with stability-guaranteed MPC designs, real-time solver development, and nonlinear-MPC advances. Confirm: the MPC stable and real-time. Kill: the computation never suffices. Does NOT claim: the MPC always feasible - it looks ahead reliably.",
 "pointer": "The Signature system's proposed approach guarantees MPC stability with real-time solvers; the companion Signature Edition record specifies the lookahead protocol.",
 "key_points": [
  "Terminal costs/constraints guarantee stability.",
  "Recursive feasibility required.",
  "QP solved each step: computation bottleneck.",
  "Nonlinear MPC the frontier.",
 ],
 "requirements": [
  "Stability-guaranteed formulations.",
  "Real-time solver development.",
  "Nonlinear MPC methods.",
 ],
 "citations": [
  "Mayne DQ et al. (2000) Constrained model predictive control: stability and optimality. Automatica 36.",
 ],
 "demo": {"zeta": 0.8, "wn": 3.0},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "ct-nonlinear",
 "name": "The Nonlinear Control Problem",
 "group": "Nonlinear Control",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Most systems are nonlinear - but how can general nonlinear systems be controlled when no universal method exists?",
 "background": "The nonlinear problem - no universal synthesis (unlike linear) - has the toolset: feedback linearization, backstepping, sliding mode, passivity - each for classes; the region-of-attraction estimation (SOS programming); and the global stabilization (hard in general). The nonlinear systems are the rule; the methods are the cases.",
 "why_it_matters": "Real systems are nonlinear. The case-by-case methods are the generality gap.",
 "sig_lens": "The Signature lens reads nonlinear control as the many terrains: the protocol must map each terrain (method per class) - and certify the safe region.",
 "sig_solution": LABEL + " Assumptions: (1) no universal method; (2) region-of-attraction hard. Reasoning path: classify and certify - method-per-class with SOS-certified regions. Proposed mechanism: a terrains protocol with class-specific synthesis, SOS region-of-attraction certification, and global methods where available. Confirm: the certified regions cover operation. Kill: the generality stays out of reach. Does NOT claim: the nonlinear problem solved - it maps the terrains.",
 "pointer": "The Signature system's proposed approach certifies nonlinear control regions with SOS methods; the companion Signature Edition record specifies the terrains protocol.",
 "key_points": [
  "No universal nonlinear synthesis.",
  "Feedback linearization, backstepping, sliding mode: class methods.",
  "Region-of-attraction via SOS programming.",
  "Global stabilization hard generally.",
 ],
 "requirements": [
  "Class-specific synthesis methods.",
  "SOS region certification.",
  "Global methods where available.",
 ],
 "citations": [
  "Khalil HK (2002) Nonlinear Systems. Prentice Hall.",
 ],
 "demo": {"zeta": 0.5, "wn": 4.0},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "ct-feedback-lin",
 "name": "The Feedback Linearization Problem",
 "group": "Nonlinear Control",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Canceling nonlinearities by feedback - but what happens to the internal (zero) dynamics, and how robust is the cancellation?",
 "background": "The feedback-linearization problem - the exact cancellation needs the exact model; the zero dynamics (unobservable after linearization) must be stable (minimum-phase); and the robustness (cancellation errors) is the fragility - is the method's fine print: the beautiful linearization is the fragile one.",
 "why_it_matters": "Feedback linearization is the elegant nonlinear method. Its fragility is the elegance's price.",
 "sig_lens": "The Signature lens reads feedback linearization as the exact trick: the protocol must check the hidden dynamics (zero) - and robustify the trick.",
 "sig_solution": LABEL + " Assumptions: (1) exact cancellation needs exact model; (2) zero dynamics must be stable. Reasoning path: linearize robustly - approximate/adaptive linearization with zero-dynamics checks. Proposed mechanism: a trick protocol with zero-dynamics stability verification, robust/adaptive linearization, and fragility quantification. Confirm: the linearized systems robust. Kill: the zero dynamics unstable. Does NOT claim: the nonlinearities canceled - it checks the trick.",
 "pointer": "The Signature system's proposed approach robustifies feedback linearization with zero-dynamics checks; the companion Signature Edition record specifies the trick protocol.",
 "key_points": [
  "Exact cancellation needs exact model.",
  "Zero dynamics must be minimum-phase.",
  "Cancellation errors fragility.",
  "Beautiful but fragile method.",
 ],
 "requirements": [
  "Zero-dynamics stability verification.",
  "Robust/adaptive linearization.",
  "Fragility quantification.",
 ],
 "citations": [
  "Isidori A (1995) Nonlinear Control Systems. Springer.",
 ],
 "demo": {"zeta": 0.9, "wn": 2.0},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "ct-sliding-mode",
 "name": "The Sliding Mode Problem",
 "group": "Nonlinear Control",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Sliding-mode control is robust - but how can the chattering (high-frequency switching) be eliminated without losing robustness?",
 "background": "The sliding-mode problem - the discontinuous control's chattering wears actuators; the boundary-layer smoothing trades robustness; the higher-order sliding modes (super-twisting) reduce chattering - is the robustness-chattering tradeoff: the invariant sliding surface is the robustness; the switching is the wear.",
 "why_it_matters": "Sliding mode is the robust nonlinear method. The chattering is the robustness' wear.",
 "sig_lens": "The Signature lens reads sliding mode as the firm grip: the protocol must grip firmly (robust) - without shaking (chattering).",
 "sig_solution": LABEL + " Assumptions: (1) discontinuity causes chattering; (2) smoothing trades robustness. Reasoning path: slide smoothly - higher-order sliding modes with chattering analysis. Proposed mechanism: a grip protocol with higher-order sliding-mode designs, chattering-robustness tradeoff optimization, and actuator-aware implementation. Confirm: the robust sliding without chattering. Kill: the tradeoff irreducible. Does NOT claim: the chattering gone - it grips without shaking.",
 "pointer": "The Signature system's proposed approach eliminates sliding-mode chattering with higher-order methods; the companion Signature Edition record specifies the grip protocol.",
 "key_points": [
  "Discontinuous control: robust, chattering.",
  "Boundary layer smooths, loses robustness.",
  "Higher-order (super-twisting) reduces chattering.",
  "Chattering wears actuators.",
 ],
 "requirements": [
  "Higher-order sliding-mode designs.",
  "Chattering-robustness optimization.",
  "Actuator-aware implementation.",
 ],
 "citations": [
  "Utkin VI (1977) Variable structure systems with sliding modes. IEEE Trans. AC 22.",
 ],
 "demo": {"zeta": 0.6, "wn": 4.5},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "ct-lyapunov",
 "name": "The Lyapunov Design Problem",
 "group": "Nonlinear Control",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Lyapunov functions certify stability - but how can they be found systematically for design, not just analysis?",
 "background": "The Lyapunov problem - finding the function is the art; the SOS programming automates for polynomial systems; the control-Lyapunov functions (CLFs) guide design (Sontag's formula) - is the synthesis gap: the analysis is easier than the design; the CLF existence is the stabilizability. The certificate is the design's guide.",
 "why_it_matters": "Lyapunov functions are the stability certificates. The design-use gap is the certificate's unused power.",
 "sig_lens": "The Signature lens reads Lyapunov as the certificate: the protocol must issue it by construction (CLF) - not just verify after.",
 "sig_solution": LABEL + " Assumptions: (1) finding Lyapunov the art; (2) SOS automates polynomially. Reasoning path: design via CLF - SOS-based CLF synthesis with Sontag-type formulas. Proposed mechanism: a certificate protocol with CLF synthesis methods, SOS automation, and design-certification integration. Confirm: the designed systems certified. Kill: the CLFs unfindable. Does NOT claim: the Lyapunov always found - it issues by construction.",
 "pointer": "The Signature system's proposed approach synthesizes control-Lyapunov functions for design; the companion Signature Edition record specifies the certificate protocol.",
 "key_points": [
  "Lyapunov functions certify stability.",
  "Finding them: the art.",
  "SOS programming automates (polynomial).",
  "CLFs guide design (Sontag).",
 ],
 "requirements": [
  "CLF synthesis methods.",
  "SOS automation.",
  "Design-certification integration.",
 ],
 "citations": [
  "Sontag ED (1989) A universal construction of Artstein's theorem. Systems & Control Letters 13.",
 ],
 "demo": {"zeta": 0.75, "wn": 1.4},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "ct-passivity",
 "name": "The Passivity Problem",
 "group": "Nonlinear Control",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Passive systems interconnect stably - but how can passivity be enforced or exploited for general systems?",
 "background": "The passivity problem - the passivity theorem (feedback interconnection of passive systems stable); the passivation (making systems passive via feedback); the physical intuition (energy) - is the compositional-stability tool: the robotics and networked systems use it; the non-passive systems need the transformation. The energy intuition is the stability's physics.",
 "why_it_matters": "Passivity gives compositional stability guarantees. The unenforced passivity is the interconnection's risk.",
 "sig_lens": "The Signature lens reads passivity as the energy honesty: the protocol must keep the energy books (storage functions) - and interconnect only the honest.",
 "sig_solution": LABEL + " Assumptions: (1) passive interconnections stable; (2) passivation via feedback. Reasoning path: enforce and exploit - passivation designs with energy-based interconnection. Proposed mechanism: an honesty protocol with passivation feedback designs, energy-based stability certificates, and compositional interconnection rules. Confirm: the interconnected systems stable. Kill: the passivation infeasible. Does NOT claim: the systems all passive - it keeps the energy books.",
 "pointer": "The Signature system's proposed approach enforces passivity for compositional stability; the companion Signature Edition record specifies the honesty protocol.",
 "key_points": [
  "Passivity theorem: passive interconnections stable.",
  "Passivation via feedback.",
  "Energy/storage-function intuition.",
  "Robotics and networks use it.",
 ],
 "requirements": [
  "Passivation feedback designs.",
  "Energy-based certificates.",
  "Compositional interconnection rules.",
 ],
 "citations": [
  "van der Schaft AJ (2000) L2-Gain and Passivity Techniques in Nonlinear Control. Springer.",
 ],
 "demo": {"zeta": 1.0, "wn": 2.6},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "ct-hybrid",
 "name": "The Hybrid Systems Problem",
 "group": "Nonlinear Control",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Systems mixing continuous and discrete dynamics - but how can hybrid systems be modeled, analyzed, and controlled?",
 "background": "The hybrid problem - the bouncing ball, the thermostat, the walking robot - needs the hybrid formalism (Goebel-Sanfelice-Teel); the Zeno behavior (infinite switches in finite time); and the stability (hybrid Lyapunov) - is the mixed-dynamics challenge: the formalisms compete; the tools are young.",
 "why_it_matters": "Cyber-physical systems are hybrid. The young tools are the mixed dynamics' gap.",
 "sig_lens": "The Signature lens reads hybrid systems as the mixed dance: the protocol must choreograph both rhythms (flows and jumps) - without the infinite stutter (Zeno).",
 "sig_solution": LABEL + " Assumptions: (1) formalisms compete; (2) Zeno the pathology. Reasoning path: model and control hybridly - GST formalism with Zeno-free design. Proposed mechanism: a dance protocol with hybrid modeling standards, Zeno-free controller design, and hybrid stability certification. Confirm: the hybrid systems controlled. Kill: the formalisms never unify. Does NOT claim: the hybrid problem solved - it choreographs the dance.",
 "pointer": "The Signature system's proposed approach models and controls hybrid systems Zeno-free; the companion Signature Edition record specifies the dance protocol.",
 "key_points": [
  "Mixed continuous/discrete dynamics.",
  "Goebel-Sanfelice-Teel formalism.",
  "Zeno: infinite switches, finite time.",
  "Hybrid Lyapunov stability.",
 ],
 "requirements": [
  "Hybrid modeling standards.",
  "Zeno-free design.",
  "Hybrid stability certification.",
 ],
 "citations": [
  "Goebel R et al. (2012) Hybrid Dynamical Systems. Princeton.",
 ],
 "demo": {"zeta": 0.5, "wn": 5.0},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "ct-switched",
 "name": "The Switched Systems Problem",
 "group": "Nonlinear Control",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Switching between controllers or plants - but how can stability be guaranteed under arbitrary or controlled switching?",
 "background": "The switched problem - the arbitrary switching needs a common Lyapunov; the slow switching (dwell time) relaxes; the controlled switching (supervisory) is the design - is the multi-mode challenge: the stable subsystems can make an unstable switched system; the dwell-time bounds the switching speed.",
 "why_it_matters": "Multi-mode systems switch. The unstable switching of stable parts is the surprise.",
 "sig_lens": "The Signature lens reads switching as the gear changes: the protocol must shift smoothly (dwell time) - or prove the gears mesh (common Lyapunov).",
 "sig_solution": LABEL + " Assumptions: (1) stable parts, unstable switching possible; (2) dwell time bounds. Reasoning path: switch safely - common-Lyapunov or dwell-time-guaranteed switching. Proposed mechanism: a gears protocol with switching-stability certification, dwell-time design, and supervisory switching logic. Confirm: the switched systems stable. Kill: the switching too fast. Does NOT claim: the switching always safe - it shifts smoothly.",
 "pointer": "The Signature system's proposed approach guarantees switched-system stability; the companion Signature Edition record specifies the gears protocol.",
 "key_points": [
  "Stable subsystems, unstable switching possible.",
  "Common Lyapunov for arbitrary switching.",
  "Dwell time bounds switching speed.",
  "Supervisory control designs the switching.",
 ],
 "requirements": [
  "Switching-stability certification.",
  "Dwell-time design.",
  "Supervisory switching logic.",
 ],
 "citations": [
  "Liberzon D (2003) Switching in Systems and Control. Birkhauser.",
 ],
 "demo": {"zeta": 0.68, "wn": 3.4},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "ct-distributed",
 "name": "The Distributed Control Problem",
 "group": "Large Scale",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Controlling spatially distributed systems (PDEs) - but how can the infinite-dimensional systems be controlled with finite actuators?",
 "background": "The distributed problem - the PDE control (heat, wave, fluid equations); the late-lumping vs early-lumping; the boundary control - is the infinite-dimensional challenge: the theory (semigroups) is elegant; the practice (discretize-then-design) is approximate; and the fluid control (Navier-Stokes) is the hard case.",
 "why_it_matters": "Distributed systems (reactors, structures, fluids) are infinite-dimensional. The approximate practice is the control gap.",
 "sig_lens": "The Signature lens reads distributed control as the infinite orchestra: the protocol must conduct with finite batons (actuators) - placing them where the music needs.",
 "sig_solution": LABEL + " Assumptions: (1) theory elegant; practice approximate; (2) fluids the hard case. Reasoning path: control with placed actuators - optimal actuator placement with PDE-aware design. Proposed mechanism: an orchestra protocol with PDE control designs, actuator-placement optimization, and late-lumping methods. Confirm: the distributed systems controlled. Kill: the fluids defeat. Does NOT claim: the PDEs tamed - it conducts with finite batons.",
 "pointer": "The Signature system's proposed approach controls distributed systems with optimized actuator placement; the companion Signature Edition record specifies the orchestra protocol.",
 "key_points": [
  "PDE control: heat, wave, fluids.",
  "Late vs early lumping debated.",
  "Boundary control the practical case.",
  "Navier-Stokes control hard.",
 ],
 "requirements": [
  "PDE-aware control design.",
  "Optimal actuator placement.",
  "Late-lumping methods.",
 ],
 "citations": [
  "Curtain RF, Zwart H (1995) An Introduction to Infinite-Dimensional Linear Systems Theory. Springer.",
 ],
 "demo": {"zeta": 0.72, "wn": 2.8},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "ct-decentralized",
 "name": "The Decentralized Control Problem",
 "group": "Large Scale",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Large systems need local controllers - but how can decentralized control be stabilized when the subsystems interact?",
 "background": "The decentralized problem - the fixed modes (unstabilizable by decentralized control); the overlapping decompositions; the LMI methods - is the large-scale challenge: the interactions destabilize the locally-stable; the fixed modes are the structural barrier.",
 "why_it_matters": "Power grids and process plants are decentralized. The interaction destabilization is the scale risk.",
 "sig_lens": "The Signature lens reads decentralization as the local rule: the protocol must let each district govern - while keeping the federation stable.",
 "sig_solution": LABEL + " Assumptions: (1) interactions destabilize; (2) fixed modes structural. Reasoning path: decentralize safely - fixed-mode-free designs with interaction-robust local control. Proposed mechanism: a federation protocol with decentralized stabilizability checks, interaction-robust local designs, and overlapping-decomposition methods. Confirm: the decentralized systems stable. Kill: the fixed modes block. Does NOT claim: the decentralization always safe - it federates carefully.",
 "pointer": "The Signature system's proposed approach stabilizes decentralized control against interactions; the companion Signature Edition record specifies the federation protocol.",
 "key_points": [
  "Fixed modes: decentralized-unstabilizable.",
  "Interactions destabilize locally-stable.",
  "Overlapping decompositions help.",
  "LMI methods for decentralized design.",
 ],
 "requirements": [
  "Decentralized stabilizability checks.",
  "Interaction-robust local designs.",
  "Overlapping decomposition methods.",
 ],
 "citations": [
  "Siljak DD (1991) Decentralized Control of Complex Systems. Academic Press.",
 ],
 "demo": {"zeta": 0.6, "wn": 3.6},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "ct-networked",
 "name": "The Networked Control Problem",
 "group": "Large Scale",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Control over networks faces delays and dropouts - but how can stability be guaranteed when the network misbehaves?",
 "background": "The networked problem - the packet dropouts, the time-varying delays, the quantization - needs the network-aware control: the dropout models (Bernoulli, Markov); the event-triggered control (communicate when needed); and the co-design (control + network). The misbehaving network is the loop's adversary.",
 "why_it_matters": "Networked control runs factories and vehicles. The misbehaving network is the loop's risk.",
 "sig_lens": "The Signature lens reads networked control as the remote operation: the protocol must operate through the static (dropouts, delays) - efficiently.",
 "sig_solution": LABEL + " Assumptions: (1) dropouts/delays/quantization; (2) event-triggering saves communication. Reasoning path: control network-aware - dropout-robust designs with event-triggered efficiency. Proposed mechanism: a remote protocol with network-aware controller synthesis, event-triggered communication, and control-network co-design. Confirm: the networked loops stable. Kill: the network too hostile. Does NOT claim: the network tamed - it operates through static.",
 "pointer": "The Signature system's proposed approach controls over networks with dropout robustness; the companion Signature Edition record specifies the remote protocol.",
 "key_points": [
  "Packet dropouts and varying delays.",
  "Quantization in feedback.",
  "Event-triggered control saves communication.",
  "Control-network co-design emerging.",
 ],
 "requirements": [
  "Dropout-robust controller synthesis.",
  "Event-triggered communication.",
  "Control-network co-design.",
 ],
 "citations": [
  "Hespanha JP et al. (2007) A survey of recent results in networked control systems. Proc. IEEE 95.",
 ],
 "demo": {"zeta": 0.78, "wn": 1.9},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "ct-consensus",
 "name": "The Multi Agent Consensus Problem",
 "group": "Large Scale",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Agents must agree distributively - but how can consensus be fast, robust, and secure against faulty agents?",
 "background": "The consensus problem - the Laplacian dynamics, the convergence speed (algebraic connectivity), the Byzantine agents - is the distributed-coordination core: the switching topologies, the quantized communication, and the adversarial agents each challenge. The agreeing agents are the coordinated swarm.",
 "why_it_matters": "Consensus coordinates swarms, grids, and blockchains. The faulty agents are the agreement's traitors.",
 "sig_lens": "The Signature lens reads consensus as the agreement: the protocol must make the agents agree - fast - despite the traitors.",
 "sig_solution": LABEL + " Assumptions: (1) convergence speed graph-dependent; (2) Byzantine agents the threat. Reasoning path: agree robustly - fast consensus with Byzantine-resilient protocols. Proposed mechanism: an agreement protocol with topology-optimized consensus, Byzantine-resilient algorithms, and convergence-speed guarantees. Confirm: the agents agree fast and safely. Kill: the adversaries win. Does NOT claim: the consensus always - it agrees despite traitors.",
 "pointer": "The Signature system's proposed approach makes multi-agent consensus fast and Byzantine-resilient; the companion Signature Edition record specifies the agreement protocol.",
 "key_points": [
  "Laplacian dynamics drive consensus.",
  "Algebraic connectivity sets speed.",
  "Switching/quantized communication challenges.",
  "Byzantine agents the adversarial threat.",
 ],
 "requirements": [
  "Topology-optimized consensus.",
  "Byzantine-resilient algorithms.",
  "Convergence-speed guarantees.",
 ],
 "citations": [
  "Olfati-Saber R et al. (2007) Consensus and cooperation in networked multi-agent systems. Proc. IEEE 95.",
 ],
 "demo": {"zeta": 0.66, "wn": 2.9},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "ct-formation",
 "name": "The Formation Control Problem",
 "group": "Large Scale",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Robot swarms must hold formations - but how can the formation be maintained distributively with limited sensing?",
 "background": "The formation problem - the displacement/rigidity approaches, the bearing-only control, the collision avoidance - is the swarm-coordination challenge: the rigidity theory certifies the shape; the distributed implementation needs the local sensing; and the moving formations (flocking) add the dynamics.",
 "why_it_matters": "Drone swarms and satellite constellations need formations. The distributed maintenance is the swarm's skill.",
 "sig_lens": "The Signature lens reads formations as the flock: the protocol must keep the shape - with each bird watching only its neighbors.",
 "sig_solution": LABEL + " Assumptions: (1) rigidity certifies shape; (2) local sensing the constraint. Reasoning path: hold distributively - rigidity-based control with bearing-only sensing. Proposed mechanism: a flock protocol with rigidity-certified formation designs, distributed bearing control, and collision-avoidance integration. Confirm: the formations hold. Kill: the sensing too limited. Does NOT claim: the formations always - it flocks with local eyes.",
 "pointer": "The Signature system's proposed approach holds robot formations with distributed rigidity control; the companion Signature Edition record specifies the flock protocol.",
 "key_points": [
  "Rigidity theory certifies formation shape.",
  "Displacement vs bearing approaches.",
  "Bearing-only sensing practical.",
  "Collision avoidance the added need.",
 ],
 "requirements": [
  "Rigidity-certified formation designs.",
  "Distributed bearing control.",
  "Collision-avoidance integration.",
 ],
 "citations": [
  "Anderson BDO et al. (2008) Rigid graph control architectures. IEEE Control Systems Magazine 28.",
 ],
 "demo": {"zeta": 0.82, "wn": 2.3},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "ct-cps-security",
 "name": "The Cyber Physical Security Problem",
 "group": "Large Scale",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Control systems face cyberattacks - but how can the physical process be protected when the attacker is in the loop?",
 "background": "The CPS-security problem - Stuxnet's lesson, the false-data-injection attacks, the replay attacks - needs the attack-aware control: the detection (residue-based, physics-based), the resilient estimation, and the secure control. The attacked loop is the new normal.",
 "why_it_matters": "Infrastructure control systems are attacked. The in-the-loop attacker is the physical risk.",
 "sig_lens": "The Signature lens reads CPS security as the guarded plant: the protocol must detect the intruder (physics-based) - and keep the process safe.",
 "sig_solution": LABEL + " Assumptions: (1) attackers in the loop; (2) detection physics-based. Reasoning path: defend physically - attack detection plus resilient control. Proposed mechanism: a guarded protocol with physics-based attack detection, resilient estimation/control, and security-aware architecture. Confirm: the plants survive attacks. Kill: the attackers adapt faster. Does NOT claim: the systems unhackable - it guards the plant.",
 "pointer": "The Signature system's proposed approach defends control systems with physics-based attack detection; the companion Signature Edition record specifies the guarded protocol.",
 "key_points": [
  "Stuxnet: the cyber-physical attack template.",
  "False-data-injection and replay attacks.",
  "Physics-based detection methods.",
  "Resilient estimation and control.",
 ],
 "requirements": [
  "Physics-based attack detection.",
  "Resilient estimation/control.",
  "Security-aware architectures.",
 ],
 "citations": [
  "Cardenas AA et al. (2008) Research challenges for the security of control systems. HotSec.",
 ],
 "demo": {"zeta": 0.58, "wn": 4.2},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "ct-learning",
 "name": "The Learning Based Control Problem",
 "group": "Learning",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Machine learning controls systems - but how can the learned controllers be certified stable and safe?",
 "background": "The learning-control problem - the neural controllers' opacity, the stability certification (neural Lyapunov), the safe learning - is the AI-control frontier: the learned policies perform; their guarantees lag; and the verification (formal methods for NN controllers) is young.",
 "why_it_matters": "Learned controllers outperform classical. The missing certificates are the deployment barrier.",
 "sig_lens": "The Signature lens reads learning control as the talented apprentice: the protocol must certify the apprentice (stability) - before the solo flight.",
 "sig_solution": LABEL + " Assumptions: (1) learned policies perform; (2) guarantees lag. Reasoning path: certify the learning - neural Lyapunov certificates with formal verification. Proposed mechanism: an apprentice protocol with stability-certified learning, neural-certificate synthesis, and formal NN-controller verification. Confirm: the certified controllers deploy. Kill: the certification stays out of reach. Does NOT claim: the learning certified - it trains the apprentice safely.",
 "pointer": "The Signature system's proposed approach certifies learning-based controllers with neural certificates; the companion Signature Edition record specifies the apprentice protocol.",
 "key_points": [
  "Neural controllers: high performance.",
  "Stability certification (neural Lyapunov) young.",
  "Safe learning the requirement.",
  "Formal NN verification developing.",
 ],
 "requirements": [
  "Stability-certified learning methods.",
  "Neural-certificate synthesis.",
  "Formal controller verification.",
 ],
 "citations": [
  "Brunke L et al. (2022) Safe learning in robotics. Annual Review Control, Robotics, Autonomous Systems 5.",
 ],
 "demo": {"zeta": 0.71, "wn": 2.7},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "ct-rl-safety",
 "name": "The Reinforcement Learning Safety Problem",
 "group": "Learning",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "RL explores dangerously - but how can reinforcement learning be safe during training and deployment?",
 "background": "The RL-safety problem - the exploration's constraint violations, the sim-to-real gap, the safe exploration - needs the constrained MDPs, the shielding (safety filters), and the Lyapunov-safe RL: the learning is powerful; its safety is half-built.",
 "why_it_matters": "RL will control physical systems. The unsafe exploration is the training risk.",
 "sig_lens": "The Signature lens reads RL safety as the training wheels: the protocol must keep them on (shielding) - until the rider is proven.",
 "sig_solution": LABEL + " Assumptions: (1) exploration violates constraints; (2) sim-to-real gaps. Reasoning path: learn safely - shielding plus constrained RL with safety certificates. Proposed mechanism: a wheels protocol with safety-shielded RL, constrained-MDP formulations, and sim-to-real safety transfer. Confirm: the RL safe in training and deployment. Kill: the safety unguaranteeable. Does NOT claim: the RL safe - it keeps the wheels on.",
 "pointer": "The Signature system's proposed approach shields reinforcement learning with safety certificates; the companion Signature Edition record specifies the wheels protocol.",
 "key_points": [
  "Exploration violates safety constraints.",
  "Constrained MDPs formalize safety.",
  "Shielding (safety filters) protects.",
  "Sim-to-real gap the transfer risk.",
 ],
 "requirements": [
  "Safety-shielded RL algorithms.",
  "Constrained-MDP formulations.",
  "Sim-to-real safety transfer.",
 ],
 "citations": [
  "Garcia J, Fernandez F (2015) A comprehensive survey on safe reinforcement learning. JMLR 16.",
 ],
 "demo": {"zeta": 0.63, "wn": 3.1},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "ct-data-driven",
 "name": "The Data Driven Control Problem",
 "group": "Learning",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Controlling directly from data without models - but when is the data informative enough, and what are the guarantees?",
 "background": "The data-driven problem - Willems' fundamental lemma (data as model), the data-enabled predictive control (DeePC) - is the model-free frontier: the informativity (persistency of excitation), the noise handling, and the guarantees (still developing) are the questions. The data replaces the model; its sufficiency is the open check.",
 "why_it_matters": "Data-driven control skips the modeling step. The informativity check is the model-free guarantee.",
 "sig_lens": "The Signature lens reads data-driven control as the mapless navigation: the protocol must check the landmarks (data informativity) - before sailing.",
 "sig_solution": LABEL + " Assumptions: (1) Willems' lemma: data as model; (2) informativity the check. Reasoning path: sail on checked data - informativity-verified DeePC with noise-robust guarantees. Proposed mechanism: a mapless protocol with data-informativity verification, noise-robust data-driven control, and guarantee development. Confirm: the data-driven controllers certified. Kill: the informativity uncheckable. Does NOT claim: the data sufficient - it checks the landmarks.",
 "pointer": "The Signature system's proposed approach verifies data informativity for model-free control; the companion Signature Edition record specifies the mapless protocol.",
 "key_points": [
  "Willems' fundamental lemma: data as model.",
  "DeePC: data-enabled predictive control.",
  "Persistency of excitation = informativity.",
  "Noise handling and guarantees developing.",
 ],
 "requirements": [
  "Data-informativity verification.",
  "Noise-robust data-driven methods.",
  "Guarantee development.",
 ],
 "citations": [
  "Willems JC et al. (2005) A note on persistency of excitation. Systems & Control Letters 54.",
 ],
 "demo": {"zeta": 0.77, "wn": 2.1},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "ct-quantum",
 "name": "The Quantum Control Problem",
 "group": "Learning",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Controlling quantum systems - but how can the fragile quantum states be steered despite decoherence and measurement backaction?",
 "background": "The quantum-control problem - the unitary control (pulses), the measurement-based feedback (backaction), the decoherence (the enemy) - is the quantum-technology enabler: the optimal pulse design (GRAPE), the error correction as control, and the scalability are the frontiers. The fragile states are the controlled ones.",
 "why_it_matters": "Quantum control enables quantum computing and sensing. The decoherence battle is the technology's war.",
 "sig_lens": "The Signature lens reads quantum control as the fragile steering: the protocol must steer fast (before decoherence) - and correct the errors.",
 "sig_solution": LABEL + " Assumptions: (1) decoherence the enemy; (2) measurement disturbs. Reasoning path: steer fast and correct - optimal pulse design with error-corrected feedback. Proposed mechanism: a fragile protocol with optimal quantum-pulse synthesis, measurement-feedback control, and decoherence-mitigation. Confirm: the quantum states controlled. Kill: the decoherence wins. Does NOT claim: the quantum tamed - it steers the fragile.",
 "pointer": "The Signature system's proposed approach steers quantum systems with optimal pulses and error correction; the companion Signature Edition record specifies the fragile protocol.",
 "key_points": [
  "Unitary control via shaped pulses (GRAPE).",
  "Measurement backaction complicates feedback.",
  "Decoherence the central enemy.",
  "Error correction as quantum control.",
 ],
 "requirements": [
  "Optimal quantum-pulse synthesis.",
  "Measurement-feedback control.",
  "Decoherence-mitigation methods.",
 ],
 "citations": [
  "D'Alessandro D (2007) Introduction to Quantum Control and Dynamics. CRC Press.",
 ],
 "demo": {"zeta": 0.69, "wn": 3.3},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "ct-unified",
 "name": "The Unified Control Theory Problem",
 "group": "Learning",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Classical, robust, nonlinear, learning-based control are separate - but can control theory be unified as one science of feedback?",
 "background": "The unified-control problem - one framework from PID to RL - is the field's synthesis: the paradigms (frequency-domain, state-space, optimization, learning) are separate cultures; the unifications (behavioral approach, dissipativity) are partial. The feedback's science is one; its theory is many.",
 "why_it_matters": "The fragmented theory misses the connections. The unification is the science's maturity.",
 "sig_lens": "The Signature lens reads control as the one art of feedback: the protocol must unite it - from PID's intuition to RL's learning - in the coherent science.",
 "sig_solution": LABEL + " Assumptions: (1) paradigms separate cultures; (2) partial unifications exist. Reasoning path: unify via behavior - the behavioral/dissipativity frameworks extended to learning. Proposed mechanism: an art protocol with unifying theoretical frameworks, paradigm-bridging methods, and unified control education. Confirm: the unified theory connects and predicts. Kill: the paradigms resist. Does NOT claim: control unified - it practices the one art.",
 "pointer": "The Signature system's proposed approach unifies control paradigms via behavioral frameworks; the companion Signature Edition record specifies the art protocol.",
 "key_points": [
  "Paradigms: classical, robust, nonlinear, learning.",
  "Behavioral approach unifies partially.",
  "Dissipativity connects across paradigms.",
  "The feedback science is one; theory many.",
 ],
 "requirements": [
  "Unifying theoretical frameworks.",
  "Paradigm-bridging methods.",
  "Unified control education.",
 ],
 "citations": [
  "Willems JC (2007) The behavioral approach to open and interconnected systems. IEEE Control Systems Magazine 27.",
 ],
 "demo": {"zeta": 0.73, "wn": 2.5},
},
]
