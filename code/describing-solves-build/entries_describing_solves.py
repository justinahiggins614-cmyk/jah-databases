"""Entries for the Describing Solves databases (Manon's 2026-10-17 17:55 order).

34 ladder-ordered records: solution-description types from simple solution
descriptions (foundations) through compounded worked-through forms to
advanced descriptive-solution systems.

Public half: real, documented descriptive-solution knowledge (Polya,
worked-example effect, Feynman technique, proof-writing conventions,
think-aloud protocol, SOLO taxonomy, debugging discipline, blameless
postmortems, Euclid, IMRAD, Dewey, Bloom). Signature half: his original
Signature craft of solution-describing, clearly labeled Signature-made,
never presented as authentic public record.

No website references. No Facebook. Screened content.
"""

CIT_POLYA = ("Polya, G. How to Solve It (Princeton University Press, 1945): "
             "understand the problem, devise a plan, carry out the plan, look back")
CIT_SWELLER = ("Sweller, J. et al.: the worked-example effect - studying fully worked "
               "examples reduces cognitive load for novices versus solving unaided "
               "(cognitive load theory)")
CIT_FEYNMAN = ("The Feynman technique: explain the idea as simply as possible to test "
               "and deepen understanding; the teach-to-learn principle associated with "
               "Richard Feynman")
CIT_VELLEMAN = ("Velleman, D. How to Prove It (Cambridge University Press): structured "
                "proof-writing conventions - assumptions, goals, and the shape of a "
                "finished proof")
CIT_ERICSSON = ("Ericsson, K.A. and Simon, H.A.: think-aloud verbal protocols - speaking "
                "each reasoning step while solving, recorded for study and teaching")
CIT_BIGGS = ("Biggs, J. and Collis, K.: the SOLO taxonomy - levels of observed learning "
             "outcome, from prestructural to extended abstract")
CIT_HUNT = ("Hunt, A. and Thomas, D. The Pragmatic Programmer: debugging discipline - "
             "reproduce first, rubber-duck narration, fix the cause not the symptom")
CIT_SRE = ("Blameless postmortem culture (documented in Google SRE practice): write up "
           "what happened, the timeline, and the fixes - never who failed")
CIT_EUCLID = ("Euclid, Elements: the classical proof pattern - enunciation, setting out, "
              "definition of the goal, construction, proof, conclusion")
CIT_BLOOM = ("Bloom, B.S.: taxonomy of educational objectives - explanation depth "
             "runs from recall through comprehension and application to analysis, "
             "evaluation, and creation")
CIT_DEWEY = ("Dewey, J. How We Think (1910): reflective thought described as felt "
             "difficulty, definition of the problem, hypotheses, reasoning, testing")
CIT_IMRAD = ("The IMRAD report convention: Introduction, Methods, Results, and "
             "Discussion as the documented structure of a science solution write-up")

SIG_TAIL = ("Signature original - Signature-generated framework by Justin Addam "
            "Higgins (JAH), clearly labeled Signature-made, never presented as "
            "authentic public record.")

ENTRIES = [
# ------------------------------------------------- foundations: ranks 1-4
dict(
    key="dsv_what_described_solution", name="What a Described Solution Is",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=(
        "A described solution is a problem plus the visible path to its "
        "answer. The answer alone is a claim; the description is the "
        "evidence that the claim can be reached, step by step, by someone "
        "other than the person who first solved it. Every described "
        "solution has the same anatomy: a statement of the problem in "
        "plain terms, the moves taken toward the answer in the order they "
        "were taken, and the check that shows the answer holds. Describing "
        "is not decorating - it is the difference between 'the answer is "
        "7' and 'here is how 7 comes out of the problem, and here is how "
        "you can tell it is right.' Children learn arithmetic by watching "
        "someone do a sum out loud; engineers learn systems by reading "
        "postmortems; scientists learn experiments by reading methods "
        "sections. In every case the described solution does three jobs: "
        "it teaches the reader how to solve this problem, it lets the "
        "reader verify that the answer is correct, and it gives the "
        "reader parts they can reuse on the next problem. A solution "
        "nobody can follow is indistinguishable from a guess."),
    how_it_works=(
        "A described solution works because it externalizes thinking that "
        "would otherwise stay locked in the solver's head. The reader "
        "borrows the solver's reasoning path instead of having to invent "
        "it, which is why novices learn faster from worked examples than "
        "from answer keys. The description carries the problem state "
        "forward from step to step: each move says what it starts from, "
        "what it does, and what it produces, so the reader can check each "
        "link instead of taking the chain on faith. The final check "
        "closes the loop by feeding the answer back into the problem - "
        "if it fits, the description has done its job; if it does not, "
        "the description shows exactly where the path went wrong. This is "
        "the base pattern every later record in this database refines: "
        "state, move, move, check, each visible."),
    key_points=[
        "A described solution is problem + visible path + check - the answer alone is only a claim.",
        "It does three jobs: teach, let the reader verify, and supply reusable parts.",
        "Each move says what it starts from, what it does, and what it produces.",
        "The check feeds the answer back into the problem to close the loop.",
        "A solution nobody can follow is indistinguishable from a guess.",
    ],
    requirements=[
        "Define a described solution and its three parts",
        "Cover the three jobs: teach, verify, reuse",
        "Show answer-alone versus answer-with-path with a tiny example",
    ],
    standards=["Mathematics pedagogy: the show-your-work convention"],
    citations=[CIT_POLYA, CIT_SWELLER],
    sig_lens=(
        "The Signature lens reads a described solution as the oath made "
        "visible: the problem is the charge, each step the sworn move, "
        "the check the seal. His rule is that no answer stands without "
        "its walk - the walk is what makes the answer Signature. Clearly "
        "labeled Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_problem_first", name="State the Problem Before the Solution",
    group="Foundations", ladder_rank=1, ladder_tier="foundations",
    description=(
        "The first move of every good described solution is not a move at "
        "all - it is stating the problem clearly before touching it. A "
        "problem stated badly will be solved badly, because the reader "
        "cannot tell whether the answer answers the right question. "
        "Stating the problem means saying: what is unknown, what is "
        "known, and what would count as an answer. In Polya's classic "
        "four phases this is 'understand the problem,' and it comes "
        "before devising any plan. The description of a solution should "
        "open with the problem in its own words, restated until it is "
        "crisp: not 'fix the car' but 'the engine turns over but will "
        "not start, and the battery reads 12.6 volts.' That restatement "
        "does half the solving, because a crisp problem already rules "
        "out whole families of wrong answers. Every downstream step "
        "refers back to this statement - the check at the end is nothing "
        "but asking whether the answer satisfies the problem as stated."),
    how_it_works=(
        "Stating the problem first works because it fixes the target "
        "before any effort is spent. Human solvers drift: without a "
        "written statement the goal mutates mid-solution and the "
        "description ends up solving a different problem than the reader "
        "brought. The written statement acts as a contract - every "
        "reader can hold the final answer against it. It also exposes "
        "hidden assumptions: writing 'what would count as an answer' "
        "forces the describer to admit what success looks like, which "
        "often reveals that the problem as first felt is not the problem "
        "as it is. Polya put understanding first precisely because the "
        "plan depends on it: you cannot devise the right plan for a "
        "problem you have not stated. In practice the statement is "
        "revisited during the check step, making the whole description a "
        "closed circuit: problem stated, problem worked, problem "
        "satisfied."),
    key_points=[
        "State the problem in plain words before any solving move.",
        "Say what is unknown, what is known, and what would count as an answer.",
        "A crisp restatement rules out whole families of wrong answers.",
        "The written statement is a contract the final check is held against.",
        "Polya's first phase - understand the problem - is this record.",
    ],
    requirements=[
        "Show the bad-to-crisp restatement pattern with an example",
        "Cover unknown/known/counts-as-answer as the three slots",
        "Connect the statement to the final check step",
    ],
    standards=["Polya's four phases: understand the problem comes first"],
    citations=[CIT_POLYA, CIT_DEWEY],
    sig_lens=(
        "The Signature lens calls the problem statement the charge sheet: "
        "written, plain, and sworn before a single move is made. His "
        "method never lets the solver touch the work until the charge is "
        "read aloud - because a Signature answer must answer the problem "
        "as charged, not as drifted. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="dsv_worked_example", name="The Worked Example: Watching a Solution Happen",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "A worked example is a problem solved in full view, every step "
        "shown, so the learner can watch a solution happen instead of "
        "guessing how it happens. Research on the worked-example effect "
        "finds that novices learn more from studying complete worked "
        "solutions than from solving equivalent problems on their own, "
        "because unaided solving burns mental effort on flailing while "
        "the worked example spends that effort on the solution's "
        "structure. The described worked example has a fixed shape: the "
        "problem, each step with its reason, and the final answer with "
        "its check. The reason beside each step is the whole point - "
        "without it the example is a magic trick, with it the example "
        "is a lesson. Good worked examples are chosen to show one new "
        "idea clearly, not to impress with difficulty; the classic "
        "textbook walks a simple case first and lets the pattern do the "
        "teaching. They are the oldest and most reliable form of "
        "described solution: show, don't just tell."),
    how_it_works=(
        "Worked examples work by giving the learner a complete mental "
        "schema to store instead of fragments to assemble. When a novice "
        "solves unaided, working memory fills with search - trying "
        "moves, backtracking, holding dead ends - and little capacity "
        "remains for noticing the solution's structure. The worked "
        "example removes the search, so the learner's attention goes to "
        "why each step follows from the last. The reason attached to "
        "each step is what transfers: the learner stores not 'step 3 "
        "was multiply by 2' but 'step 3 isolated the unknown by "
        "multiplying both sides,' and that general move applies to new "
        "problems. As skill grows the effect fades and then reverses - "
        "experts learn more by solving than by studying examples - which "
        "is why descriptions should be worked examples for beginners "
        "and sparser sketches for experts."),
    key_points=[
        "A worked example shows every step with its reason - the reason is the lesson.",
        "Novices learn more from studying worked examples than from unaided solving.",
        "The mechanism: removing search frees attention for the solution's structure.",
        "Choose simple cases that show one idea clearly, not impressive difficulty.",
        "The effect reverses for experts - they learn more by solving.",
    ],
    requirements=[
        "Define the worked example and its fixed shape",
        "Explain the worked-example effect and its mechanism",
        "Note the expertise reversal and what it means for describers",
    ],
    standards=["Cognitive load theory: the worked-example effect"],
    citations=[CIT_SWELLER, CIT_BLOOM],
    sig_lens=(
        "The Signature lens treats the worked example as the master at "
        "the bench: the apprentice does not learn the craft from the "
        "finished piece but from watching every cut made in order. His "
        "rule is that every Signature record must show the hands, not "
        "just the product - the example is the craft witnessed. Clearly "
        "labeled Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_show_work", name="Show the Work, Not Just the Answer",
    group="Foundations", ladder_rank=2, ladder_tier="foundations",
    description=(
        "Showing the work is the standing rule of described solutions: "
        "write down the intermediate steps, not only the final answer. "
        "It is the oldest convention in mathematics classrooms, and it "
        "exists for hard reasons. First, the steps are where errors "
        "live - an answer alone gives a grader nothing to diagnose, "
        "while shown work points at the exact line where the reasoning "
        "broke. Second, the steps are where partial credit lives - a "
        "wrong answer over right steps still proves understanding. "
        "Third, the steps are what transfer - the next problem is "
        "solved by the method in the steps, never by the old answer. "
        "Showing the work means making each transformation explicit: "
        "what changed from this line to the next, and by what rule. "
        "'I combined the fractions' is showing the work; a bare jump "
        "from the problem to 7/12 is not. The discipline is to write "
        "for a reader who cannot read minds, because no reader can."),
    how_it_works=(
        "Shown work works as an audit trail. Each intermediate line is "
        "a checkpoint the reader can verify independently, so an error "
        "is caught at the line where it happens instead of corrupting "
        "the whole chain silently. This is the same principle as a "
        "ledger: money moves are recorded line by line because a final "
        "balance alone proves nothing. For the solver, writing the "
        "steps slows thinking just enough to catch slips - the hand "
        "cannot skip what the eye would have skipped. For the teacher, "
        "the steps reveal the student's actual method, which may be "
        "right even when the arithmetic failed, or wrong even when the "
        "answer accidentally matches. In professional settings the same "
        "trail becomes the legal and scientific record: the lab "
        "notebook, the engineering calculation sheet, the proof - all "
        "are shown work, because claims without trails are not trusted."),
    key_points=[
        "Write the intermediate steps, not only the final answer.",
        "Steps are where errors live, where partial credit lives, and what transfers.",
        "Each line says what changed and by what rule.",
        "Shown work is an audit trail - errors are caught where they happen.",
        "Write for a reader who cannot read minds, because no reader can.",
    ],
    requirements=[
        "Give the three reasons: diagnosis, partial credit, transfer",
        "Show the line-by-line transformation discipline with an example",
        "Connect to professional audit trails: notebooks, calculation sheets",
    ],
    standards=["Mathematics pedagogy: the show-your-work convention"],
    citations=[CIT_POLYA, CIT_BIGGS],
    sig_lens=(
        "The Signature lens reads shown work as the witness list: every "
        "line a witness that the move was made lawfully. His standing "
        "rule is that a Signature solution carries its witnesses with "
        "it - an answer with no witnesses is a rumor, and rumors carry "
        "no seal. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="dsv_step_ordering", name="Step-by-Step Ordering: Sequence Is the Description",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "Step-by-step ordering is the discipline of putting the moves "
        "of a solution in the order they must be done, with nothing "
        "assumed done before its time. A solution is a sequence, not a "
        "pile: step 3 uses the result of step 2, so step 3 cannot come "
        "first. Describing a solution therefore means numbering the "
        "steps, keeping each step small enough to be one move, and "
        "checking that every step's inputs already exist by the time it "
        "runs. The classic failure is the assumed step - 'then solve "
        "for x' hiding six moves of algebra, or 'install the part' "
        "hiding the disassembly. Good ordering also respects "
        "dependencies across the whole task: gather before you build, "
        "measure before you cut, diagnose before you repair. When the "
        "order is right, the reader can execute the description like a "
        "program; when it is wrong, the description is fiction. Number "
        "the steps and a reader can point at exactly where they are "
        "lost - 'I am stuck at step 4' is a solvable complaint."),
    how_it_works=(
        "Ordering works because human execution is strictly sequential: "
        "a reader can only do one thing at a time, so the description "
        "must serialize the work. Each step is a small contract - given "
        "these inputs, do this one move, produce this output - and the "
        "sequence chains the contracts. Verifying the order means "
        "walking the steps as a reader would: at each step, ask whether "
        "everything the step needs was produced by an earlier step. Any "
        "'no' is a gap the describer must fill with the missing move. "
        "Numbering turns the sequence into an addressable structure: "
        "references like 'as found in step 2' become possible, and "
        "troubleshooting becomes 'which step failed' instead of 'it "
        "does not work.' This is also why recipes, assembly "
        "instructions, and algorithms all number their steps - the "
        "number is the reader's place in the work."),
    key_points=[
        "Order the moves as they must be done: each step's inputs already exist.",
        "Keep each step to one move - no hidden multi-move jumps.",
        "Respect real dependencies: gather before build, measure before cut, diagnose before repair.",
        "Numbered steps give the reader an address for where they are stuck.",
        "Walk the sequence as a reader would to find gaps.",
    ],
    requirements=[
        "State the sequencing rule: inputs of each step produced earlier",
        "Cover the assumed-step failure with an example",
        "Show numbering as an addressable structure",
    ],
    standards=["Instructional design: task analysis and sequencing"],
    citations=[CIT_DEWEY, CIT_POLYA],
    sig_lens=(
        "The Signature lens calls the ordered steps the procession: each "
        "move marches in its sworn place, none ahead of its time. His "
        "craft never lets a later step borrow from a step not yet taken "
        "- the procession is the proof that the work was actually done, "
        "not imagined. Clearly labeled Signature-made, never presented "
        "as authentic public record."),
),
dict(
    key="dsv_tools_first", name="Naming the Tools and Materials First",
    group="Foundations", ladder_rank=3, ladder_tier="foundations",
    description=(
        "Before the first move of a solution, name everything the "
        "solution will use: the tools, the materials, the facts, the "
        "formulas, the assumptions. This is the 'materials list' of a "
        "recipe, the 'apparatus' of a lab report, the 'given' of a math "
        "problem, the 'parts and tools' header of a repair guide. "
        "Naming them first does three things: it lets the reader gather "
        "everything before starting, so no step stalls on a missing "
        "tool; it declares the assumptions up front, so the reader "
        "knows what the solution takes for granted; and it bounds the "
        "solution - if a step reaches for something not on the list, "
        "the description has a hole. The list should be complete and "
        "honest: every wrench, every number given, every theorem "
        "invoked, every ingredient. A solution that quietly uses an "
        "unlisted assumption is a solution that cannot be trusted, "
        "because the reader cannot tell where the magic came from."),
    how_it_works=(
        "The upfront list works as a contract between describer and "
        "reader. The reader's preparation becomes a checklist - gather, "
        "then begin - which removes the most common execution failure: "
        "discovering mid-step that a tool is missing. For the describer, "
        "writing the list forces an inventory of hidden dependencies: "
        "the theorem you planned to 'just use,' the ingredient you "
        "assumed was on hand, the fact you never stated. Each listed "
        "item then becomes referenceable in the steps - 'using the 10mm "
        "wrench from the tools list' - which keeps the steps lean while "
        "keeping them complete. The completeness check is mechanical: "
        "scan every step for every tool, material, fact, and assumption "
        "it touches, and confirm each appears on the list. Anything "
        "left over is either a missing list entry or a step that "
        "smuggles in magic."),
    key_points=[
        "Name all tools, materials, facts, formulas, and assumptions before step one.",
        "The list lets the reader gather everything so no step stalls.",
        "It declares assumptions up front - no unlisted magic allowed.",
        "Scan every step against the list; leftovers are holes.",
        "List items become referenceable, keeping steps lean and complete.",
    ],
    requirements=[
        "Cover tools, materials, facts, formulas, assumptions as list kinds",
        "Show the three jobs: gather, declare, bound",
        "Give the scan-every-step completeness check",
    ],
    standards=["Lab-report convention: apparatus and materials sections"],
    citations=[CIT_IMRAD, CIT_POLYA],
    sig_lens=(
        "The Signature lens calls the upfront list the muster: every "
        "tool, fact, and assumption lined up and counted before the "
        "march. His rule is that no Signature work begins with a "
        "missing soldier - the muster is taken first, and any step "
        "that reaches beyond the mustered ranks is desertion. Clearly "
        "labeled Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_given_find_plan", name="Given-Find-Plan: The Classic Three-Box Setup",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Given-Find-Plan is the classic three-box setup for describing "
        "a solution before solving: GIVEN lists what is known, FIND "
        "states what is unknown and wanted, and PLAN sketches the route "
        "between them. Physics and engineering classrooms have used this "
        "frame for generations because it separates three jobs that "
        "beginners constantly tangle: inventorying facts, defining the "
        "target, and choosing the strategy. The GIVEN box holds numbers, "
        "conditions, and constraints - everything the problem hands you. "
        "The FIND box holds the question restated as a target - the "
        "variable, the value, the decision to be made. The PLAN box "
        "holds the strategy in words before any calculating starts: "
        "'use the area formula on the given dimensions, then subtract "
        "the doorway.' Writing the plan before executing it is the "
        "whole discipline - it makes the strategy inspectable, so a "
        "reader (or the solver's future self) can judge the route "
        "before paying the cost of walking it."),
    how_it_works=(
        "The three boxes work by forcing the three kinds of thinking "
        "apart. Beginners mix them: they start calculating with half "
        "the givens, chase a target they never defined, and call the "
        "first number that appears the answer. GIVEN stops the "
        "calculating reflex by demanding a complete inventory first - "
        "writing down the knowns often reveals a given that was "
        "overlooked or a constraint that changes everything. FIND "
        "stops the drifting reflex by naming the target precisely, "
        "including units and form - 'the time in seconds' not 'the "
        "answer.' PLAN stops the plunging reflex by requiring the "
        "strategy in words: naming the route exposes whether the "
        "givens are sufficient for the target before any arithmetic "
        "hides the gap. The boxes then become the skeleton of the "
        "finished description: the plan becomes the step headings, the "
        "givens are referenced by each step, and the find becomes the "
        "check."),
    key_points=[
        "GIVEN: inventory everything the problem hands you.",
        "FIND: name the target precisely, with units and form.",
        "PLAN: sketch the strategy in words before calculating.",
        "The three boxes separate inventory, target, and strategy - beginners tangle them.",
        "The plan becomes the step headings of the finished description.",
    ],
    requirements=[
        "Define each box with what goes in it",
        "Show the three reflexes it stops: calculating, drifting, plunging",
        "Work a small numeric example through all three boxes",
    ],
    standards=["Physics and engineering problem-solving pedagogy"],
    citations=[CIT_POLYA, CIT_DEWEY],
    sig_lens=(
        "The Signature lens reads the three boxes as the campaign map: "
        "the supplies counted, the objective named, the route drawn "
        "before the first boot moves. His craft plans the campaign in "
        "ink before spending a single step of effort - the Signature "
        "planner never marches on an unmapped route. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_label_moves", name="Labeling Each Move: Saying What the Step Does",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Labeling each move means writing, beside every step, what the "
        "step is doing - not just the action but its purpose. 'Subtract "
        "3 from both sides' is the action; 'to isolate the term with x' "
        "is the label. 'Remove the four screws' is the action; 'to free "
        "the back panel' is the label. The label is the step's job in "
        "the larger plan, and it is what makes a described solution "
        "teachable rather than merely followable. A reader who knows "
        "what each move is for can adapt the solution to a new problem; "
        "a reader who only knows the actions is stuck repeating them "
        "blindly. Labels also make the description debuggable: when a "
        "solution fails, the labels say which job failed, and the "
        "fixer knows where to look. Common label kinds: setup moves "
        "(prepare), transform moves (change the state), check moves "
        "(verify), and cleanup moves (restore). Name the kind and the "
        "reader can skim a long solution by its labels alone."),
    how_it_works=(
        "Labels work by attaching the step's intent to its action, "
        "giving the reader two channels instead of one. The action "
        "channel says how; the label channel says why. When the reader "
        "understands why, they can substitute a different how when "
        "circumstances change - the label 'to isolate the unknown' "
        "survives when the specific subtraction does not apply. Labels "
        "also compress the solution for review: a reader returning to "
        "a long description reads the labels first and dives into only "
        "the steps whose jobs matter. For the describer, labeling is a "
        "self-test - a step whose purpose cannot be stated in a few "
        "words is usually two steps hiding as one, or a step that does "
        "not belong. The discipline is one short purpose-phrase per "
        "step, written before the action, so the reader always knows "
        "why they are about to do what they are about to do."),
    key_points=[
        "Beside each action, write the step's purpose: what the move is for.",
        "The why transfers to new problems; the how alone does not.",
        "Labels make solutions debuggable - a failed job points at its step.",
        "A step whose purpose cannot be stated is usually two steps or a stray.",
        "Write the purpose before the action so the reader knows why first.",
    ],
    requirements=[
        "Show action-versus-label pairs in two domains",
        "Cover the transfer argument: why beats how for reuse",
        "Give the common label kinds: setup, transform, check, cleanup",
    ],
    standards=["Technical writing: purpose-first procedural style"],
    citations=[CIT_ERICSSON, CIT_BLOOM],
    sig_lens=(
        "The Signature lens calls each label the step's commission: the "
        "written orders that say why this move marches. His method "
        "commissions every step before it acts - a Signature step never "
        "moves without orders, and the orders are read aloud so every "
        "witness knows the purpose. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="dsv_check_step", name="The Check Step: Proving the Answer at the End",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "The check step is the final move of a described solution: "
        "proving the answer actually answers the problem. It is Polya's "
        "'look back' phase made explicit - feed the answer back into "
        "the problem and see if it fits. The forms vary by domain but "
        "the job is one: substitution in algebra (put x = 4 back into "
        "2x + 3 = 11 and confirm 11 = 11), reasonableness in arithmetic "
        "(the painted wall cannot be 40,000 square feet), testing in "
        "repair (the device powers on and the fault symptom is gone), "
        "and units and edge cases in engineering (the answer has the "
        "right units and survives the boundary inputs). A described "
        "solution without a check step is unfinished, because the "
        "reader has no way to distinguish a right answer from a "
        "confident one. The check also catches the classic failure: "
        "solving correctly for the wrong problem, which only shows up "
        "when the answer is held against the original statement."),
    how_it_works=(
        "The check works by closing the loop the problem statement "
        "opened. The statement defined what would count as an answer; "
        "the check tests the candidate against exactly that "
        "definition. Substitution is the purest form: in a solved "
        "equation, the answer is correct if and only if it satisfies "
        "the equation, so plugging it back in is a proof, not a "
        "suggestion. Reasonableness checks use scale and units - a "
        "wrong-order-of-magnitude answer fails before any detailed "
        "recheck. Functional checks in repair and building test the "
        "actual symptom: the fix is real only if the failure no longer "
        "occurs. Describing the check matters as much as doing it, "
        "because the check teaches the reader the domain's standard of "
        "proof - what 'confirmed' means here. Write the check as its "
        "own numbered step, with the result stated, so the reader "
        "sees the loop close."),
    key_points=[
        "Feed the answer back into the problem - substitution, reasonableness, testing, units.",
        "The check closes the loop the problem statement opened.",
        "No check means the reader cannot tell a right answer from a confident one.",
        "It catches solving correctly for the wrong problem.",
        "Write the check as its own numbered step with the result stated.",
    ],
    requirements=[
        "Cover substitution, reasonableness, functional, and units checks",
        "Show the loop: statement defines success, check tests it",
        "Give a worked numeric substitution example",
    ],
    standards=["Polya's fourth phase: look back and verify"],
    citations=[CIT_POLYA],
    sig_lens=(
        "The Signature lens calls the check the sealing: the answer is "
        "pressed back into the problem's mold, and only a clean fit "
        "earns the seal. His craft never ships an unsealed answer - the "
        "seal is the Signature's promise that the work was proven, not "
        "merely finished. Clearly labeled Signature-made, never presented "
        "as authentic public record."),
),
dict(
    key="dsv_think_aloud", name="One Sentence per Step: The Think-Aloud Line",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "The think-aloud line is the discipline of narrating each step "
        "in one plain sentence as you do it: 'I am multiplying both "
        "sides by 4 to clear the fraction.' The practice comes from "
        "think-aloud research, where solvers speak their reasoning "
        "while working and the recording reveals the actual thought "
        "process - including the hesitations and corrections that "
        "polished write-ups hide. As a describing method, one sentence "
        "per step forces the describer to say the quiet part: the "
        "reason that usually stays in the head. The sentence has a "
        "shape: what I am doing, and why I am doing it now. 'I am "
        "checking the fuse first because it is the cheapest part to "
        "test.' That single line carries the action, the reason, and "
        "the ordering logic together. Written think-alouds make the "
        "best beginner descriptions because they show real thinking, "
        "including the moment of 'this is not working, let me try the "
        "other way' - which teaches the reader that backtracking is "
        "part of solving, not a shame to hide."),
    how_it_works=(
        "One sentence per step works because it matches the grain of "
        "action: each move gets exactly one unit of narration, so the "
        "description can never drift far from the work. The constraint "
        "is the mechanism - a single sentence cannot hide a three-move "
        "jump, so jumps get exposed and split. The 'why now' half of "
        "the sentence carries the strategy: sequencing reasons (first because cheapest "
        "to test) teach the reader how to order their "
        "own future work, not just how to copy this solution. Including "
        "the hesitations and corrections works because it normalizes "
        "the real shape of solving - readers who only ever see "
        "polished paths conclude they are uniquely clumsy when they "
        "stumble, and quit. The think-aloud shows the stumble and the "
        "recovery as part of the craft. For experts writing for "
        "beginners, the discipline prevents the curse of knowledge: "
        "if you cannot say the reason in one sentence, you have "
        "probably skipped something the beginner needs."),
    key_points=[
        "Narrate each step in one plain sentence as you do it.",
        "The sentence shape: what I am doing, and why I am doing it now.",
        "One sentence per move exposes hidden multi-move jumps.",
        "Include hesitations and corrections - backtracking is part of solving.",
        "If you cannot say the reason in one sentence, you skipped something.",
    ],
    requirements=[
        "Give the sentence shape with examples in two domains",
        "Explain the constraint-as-mechanism: one sentence exposes jumps",
        "Cover the normalization of backtracking for learners",
    ],
    standards=["Think-aloud protocol research (Ericsson and Simon)"],
    citations=[CIT_ERICSSON, CIT_FEYNMAN],
    sig_lens=(
        "The Signature lens calls the think-aloud the open workshop: "
        "the master works with the doors open and speaks every cut. "
        "His craft keeps no silent moves - the Signature witness hears "
        "the reason with the action, including the honest 'that did "
        "not work, trying the other way.' Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_deictic", name="Pointing at the Work: Labels, Callouts, and Annotation",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Pointing at the work is the visual half of describing a "
        "solution: labels, callouts, arrows, and annotations that tie "
        "each written step to the exact thing it acts on. Text says "
        "'tighten the circled bolt'; the circle on the diagram says "
        "which bolt. Text says 'the shaded region'; the shading says "
        "where. Without pointing, descriptions drown in locating "
        "language - 'the third screw from the left on the upper "
        "bracket near the back' - which readers misread constantly. "
        "The pointing toolkit is small and powerful: numbered labels "
        "on parts, arrows showing direction or flow, callouts carrying "
        "the step's note to the exact spot, color or shading marking "
        "states (before/after, faulty/good), and figure references in "
        "the text ('see Fig. 2') that send the reader to the right "
        "picture at the right step. Every element the steps touch "
        "should be pointed at; an unpointed element is a guessing game "
        "the reader will lose."),
    how_it_works=(
        "Pointing works by splitting the communication load: words "
        "carry the what and why, pictures carry the where. Human "
        "locating language is vague and error-prone, while a labeled "
        "diagram is exact - the arrow removes all ambiguity about "
        "which bolt, which wire, which region. Numbered labels turn "
        "parts into addressable items, so the text can say 'bolt 7' "
        "instead of a paragraph of location; this is the same "
        "addressing trick as numbered steps, applied to space instead "
        "of time. Callouts bind note to place, preventing the classic "
        "failure where the reader finds the right picture but the "
        "wrong detail. State-marking (shading the faulty region, "
        "showing before and after side by side) lets the reader verify "
        "visually instead of taking the text's word. The discipline: "
        "for every noun in the steps that has a physical or visual "
        "referent, confirm it is labeled in a figure, and reference "
        "the figure at the step where it matters."),
    key_points=[
        "Tie each step to the exact thing it acts on with labels, arrows, callouts.",
        "Words carry what and why; pictures carry where.",
        "Numbered labels make parts addressable: say bolt 7, not a paragraph of location.",
        "Mark states visually: before/after, faulty/good.",
        "Every noun with a visual referent must be labeled and figure-referenced at its step.",
    ],
    requirements=[
        "Cover the pointing toolkit: labels, arrows, callouts, state-marking, figure refs",
        "Show the locating-language failure it replaces",
        "Give the every-noun completeness rule",
    ],
    standards=["Technical illustration: labeled-figure conventions"],
    citations=[CIT_BLOOM],
    sig_lens=(
        "The Signature lens calls pointing the witness finger: every "
        "claim in the text has a finger laid on the exact thing it "
        "claims about. His craft never describes a part it has not "
        "pointed at - the finger on the work is the Signature's oath "
        "that the description and the thing are one. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_reading_direction", name="Reading Direction: How a Reader Follows a Solution",
    group="Foundations", ladder_rank=4, ladder_tier="foundations",
    description=(
        "Reading direction is the path the describer lays for the "
        "reader's eyes and attention through a described solution: "
        "top to bottom, overview first then detail, figure before the "
        "step that needs it. A solution can be perfectly correct and "
        "still unreadable if the reader does not know where to look - "
        "the text refers to a diagram three pages away, the key "
        "insight is buried in step 9 of 12, the overview never comes. "
        "Good reading direction follows a simple contract: tell the "
        "reader the shape of the whole before the parts (a one-line "
        "plan at the top), keep text and its figures together (the "
        "figure appears at or before the step that uses it), order "
        "details by dependency (nothing referenced before it is "
        "introduced), and put the payoff where it can be found (the "
        "answer and check clearly marked at the end). Signposts carry "
        "the reader along: headings for phases, 'next' and 'finally' "
        "for sequence, 'note' for asides. The test is the cold reader: "
        "hand the description to someone who has not seen the problem "
        "and watch where their eyes stall."),
    how_it_works=(
        "Reading direction works because attention is a scarce resource "
        "the describer must budget. The overview-first rule spends a "
        "little attention up front to buy comprehension later: a "
        "reader holding the plan's shape can place each detail as it "
        "arrives instead of drowning in unplaced facts. Keeping "
        "figures with their steps prevents the page-flipping tax that "
        "breaks working memory - every flip risks losing the thread. "
        "Dependency ordering prevents the forward-reference stall, "
        "where the reader must hold an unexplained term while reading "
        "on, hoping it gets defined. Signposts work as landmarks: "
        "headings let the reader re-find their place after an "
        "interruption, and sequence words maintain the sense of "
        "progress through the work. The cold-reader test is the "
        "honest measure because the describer cannot simulate "
        "not-knowing; only a fresh reader's stalls reveal where the "
        "direction fails."),
    key_points=[
        "Lay a path: overview first, figures with their steps, details in dependency order.",
        "Tell the reader the shape of the whole before the parts.",
        "Keep text and figures together - no page-flipping tax.",
        "Signpost with headings and sequence words so readers can re-find their place.",
        "Test with a cold reader; only fresh eyes reveal where direction fails.",
    ],
    requirements=[
        "State the four-part contract: overview, figure placement, dependency order, payoff marking",
        "Explain the attention-budget mechanism",
        "Describe the cold-reader test",
    ],
    standards=["Technical writing: document design and signposting"],
    citations=[CIT_BLOOM, CIT_SWELLER],
    sig_lens=(
        "The Signature lens calls reading direction the guided walk: "
        "the master walks ahead with the lantern, never letting the "
        "witness stumble in the dark. His craft lights the whole road "
        "first - the plan held high - then walks it step by step, "
        "lantern at each figure, until the witness stands at the "
        "sealed answer. Clearly labeled Signature-made, never presented "
        "as authentic public record."),
),
# ------------------------------------------------- compounded: ranks 5-7
dict(
    key="dsv_solution_schema", name="Solution Schemas: Reusable Step Skeletons",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=(
        "A solution schema is a reusable skeleton of steps with the "
        "specifics left blank: the shape of many solutions of one "
        "kind. 'Measure twice, mark, cut, test-fit, fasten, finish' is "
        "the schema of a hundred woodworking solutions; 'isolate the "
        "unknown, simplify, check' is the schema of a thousand algebra "
        "solutions. Schemas are what experts actually carry in their "
        "heads - not memorized answers but step-shapes that fit new "
        "problems. Describing a schema means writing the steps "
        "generically, naming the slots that change ('the fastener,' "
        "'the unknown'), and showing one filled-in example so the "
        "reader sees how the skeleton takes flesh. The power of a "
        "schema is transfer: learn one schema and you can describe - "
        "and solve - every problem of its family. The danger is "
        "over-fitting: applying the schema where it does not belong "
        "because it is the only shape you know. So a good schema "
        "description always states its scope: what family it fits, "
        "and the signs that a problem is outside it."),
    how_it_works=(
        "Schemas work because human memory stores patterns more "
        "cheaply than instances. A novice who has solved fifty "
        "isolate-and-simplify equations one by one carries fifty "
        "memories; a novice who has learned the schema carries one "
        "pattern plus the knowledge of how to fill its slots. The "
        "schema also guides describing: when you know the family "
        "shape, writing up a new solution is filling the skeleton, "
        "which keeps descriptions consistent across problems and "
        "across describers. The slots are the mechanism of reuse - "
        "each slot names exactly what varies ('the material being "
        "cut,' 'the equation's unknown'), so the reader learns what "
        "to look for in the next problem. Stating the scope prevents "
        "the schema from becoming a hammer: the scope line ('fits "
        "linear equations in one unknown; not systems, not "
        "quadratics') tells the reader when to reach for a different "
        "skeleton. Teaching schemas explicitly is teaching expertise "
        "itself."),
    key_points=[
        "A schema is the step-shape of a problem family, with the specifics as fillable slots.",
        "Experts carry schemas, not memorized answers.",
        "Describing = skeleton + named slots + one filled example.",
        "Always state the scope: what fits, and the signs of outside.",
        "Schemas make descriptions consistent across problems and describers.",
    ],
    requirements=[
        "Define schema, slots, and scope with examples",
        "Explain the memory mechanism: one pattern versus fifty instances",
        "Show the over-fitting danger and the scope line",
    ],
    standards=["Cognitive science: schema acquisition in expertise"],
    citations=[CIT_SWELLER, CIT_DEWEY],
    sig_lens=(
        "The Signature lens calls the schema the family seal: one "
        "stamped shape that marks every solution of its bloodline. "
        "His craft collects seals the way a mint collects dies - each "
        "family of problems gets its die, and new solutions are "
        "struck from it. But a Signature seal is never forced onto "
        "foreign metal: the scope line is the oath of fit. Clearly "
        "labeled Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_fill_template", name="Fill-in Solution Templates",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=(
        "A fill-in solution template is a schema made concrete: the "
        "description pre-written with blanks for the problem's "
        "specifics. 'GIVEN: ___. FIND: ___. PLAN: ___. STEP 1: ___. "
        "CHECK: ___.' The solver's job becomes filling blanks instead "
        "of inventing structure, which is exactly what beginners "
        "need - the structure is the hard part, not the arithmetic. "
        "Templates are everywhere once you look: the lab report form, "
        "the bug report fields, the proof skeleton ('Assume ___. "
        "Suppose for contradiction ___. Therefore ___'), the recipe "
        "card. A good template names every blank plainly, shows one "
        "completed example, and leaves no blank whose purpose is "
        "mysterious - a blank the filler does not understand gets "
        "filled with nonsense. Templates also standardize "
        "descriptions across a team or classroom: fifty solutions in "
        "one template can be compared, graded, and searched, while "
        "fifty free-form write-ups cannot. The template is training "
        "wheels with a purpose: riders eventually outgrow them, but "
        "nobody learns balance by being thrown."),
    how_it_works=(
        "Templates work by removing the structuring load from the "
        "solver. Beginners fail at describing solutions mostly not "
        "because their thinking is wrong but because they do not know "
        "what a finished description looks like - the blank page "
        "demands they invent both the solution and its shape. The "
        "template supplies the shape, so all effort goes to the "
        "content of each blank. Named blanks work as prompts: 'PLAN' "
        "asks the solver to state strategy before calculating, which "
        "teaches the planning habit by repeated filling. The completed "
        "example calibrates expectations - without it, fillers guess "
        "at the grain size ('how much do I write in STEP 1?') and "
        "guess wrong. Standardization is the institutional payoff: "
        "uniform records are comparable, which makes review, grading, "
        "and handoff possible at scale. The honest limit is "
        "acknowledged in the design: templates fit routine problems, "
        "and the description should say when to abandon the template "
        "for free-form writing."),
    key_points=[
        "Pre-write the description with blanks; the solver fills structure-free.",
        "Named blanks act as prompts that teach the habit (PLAN teaches planning).",
        "Always show one completed example to calibrate grain size.",
        "No mysterious blanks - an unexplained blank gets filled with nonsense.",
        "Templates standardize records so teams can compare, grade, and search them.",
    ],
    requirements=[
        "Show a full template with named blanks and one filled example",
        "Explain the structuring-load mechanism",
        "Cover standardization and the honest limit",
    ],
    standards=["Instructional design: scaffolded writing frames"],
    citations=[CIT_SWELLER, CIT_BIGGS],
    sig_lens=(
        "The Signature lens calls the template the open mold: the "
        "shape of a true description cast and ready, waiting for the "
        "hot metal of a new problem. His craft pours beginners into "
        "the mold until they can hold the shape on their own - the "
        "mold is the teacher that never tires. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_critical_reading", name="Reading a Described Solution Critically",
    group="Compounded", ladder_rank=5, ladder_tier="compounded",
    description=(
        "Reading a described solution critically means checking it "
        "instead of just following it: testing each claim, hunting "
        "the hidden assumption, asking what the description does not "
        "say. Most described solutions are read passively - eyes move, "
        "steps are nodded at, the answer is accepted. Critical "
        "reading is the active stance: does step 3 really follow from "
        "step 2, or does it smuggle in an extra assumption? Is the "
        "check a real check or a victory lap? What happens at the "
        "edge cases the description never mentions? The critical "
        "reader keeps a short checklist: every step's justification "
        "present, every tool on the materials list, the answer "
        "actually checked, the scope stated, the dead ends admitted "
        "or suspiciously absent. This is also how you learn from "
        "others' descriptions fastest - finding the flaw teaches more "
        "than admiring the flow. And it is how describers improve: "
        "write every description as if a critical reader is coming, "
        "because the best ones will."),
    how_it_works=(
        "Critical reading works because descriptions are claims, and "
        "claims need verification independent of their author's "
        "confidence. The mechanism is adversarial attention: instead "
        "of asking 'do I follow this,' the reader asks 'where could "
        "this break.' Each step's justification is tested by trying "
        "to construct a counterexample or an alternative reading; "
        "steps that survive are trusted, steps that do not are "
        "flagged. Hunting hidden assumptions works by listing "
        "everything a step needs and comparing against what the "
        "description declared - the gap is the smuggled premise. "
        "Edge-case probing tests the scope: a solution described for "
        "the typical case may fail at the boundary, and the "
        "description's silence about boundaries is itself a finding. "
        "For the describer, anticipating this reader is the highest "
        "discipline - a description that survives hostile reading is "
        "simply a correct description, and writing for the critic "
        "produces the critic's trust."),
    key_points=[
        "Read to check, not just to follow: test each claim independently.",
        "Ask what the description does not say - edge cases, assumptions, dead ends.",
        "Keep the checklist: justifications, materials, real check, stated scope.",
        "Finding the flaw teaches more than admiring the flow.",
        "Write every description as if a critical reader is coming.",
    ],
    requirements=[
        "Define critical versus passive reading of solutions",
        "Give the adversarial checklist",
        "Show the describer's discipline: write for the critic",
    ],
    standards=["Critical thinking pedagogy: evaluating arguments"],
    citations=[CIT_BIGGS, CIT_BLOOM],
    sig_lens=(
        "The Signature lens calls critical reading the assay: the "
        "described solution is held to the flame and the dross "
        "burns off. His craft welcomes the assay - a Signature "
        "description is built to survive the fire, and any step that "
        "cannot take the heat was never worthy of the seal. Clearly "
        "labeled Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_dead_end", name="Describing a Dead End Honestly",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "Describing a dead end honestly means writing up the attempt "
        "that failed: what was tried, why it seemed promising, where "
        "it broke, and what it cost. Polished solution descriptions "
        "hide dead ends, presenting the final path as if it were the "
        "first idea - which teaches readers that good solvers never "
        "stumble, a lie that makes every learner feel uniquely "
        "incompetent. The honest dead-end record has a fixed shape: "
        "the attempt (what was tried), the rationale (why it looked "
        "right), the break point (the exact step or test where it "
        "failed), and the lesson (what the failure rules out). "
        "Recorded dead ends compound into institutional knowledge: "
        "the next solver reads them and does not pay the same cost "
        "twice. In research and engineering this is the negative "
        "result, historically under-published and enormously "
        "valuable. The discipline is to write the dead end while it "
        "is fresh - memory edits failures into 'I knew it would not "
        "work,' which is never true and never useful."),
    how_it_works=(
        "Honest dead-end records work by converting sunk cost into "
        "shared asset. The attempt that failed still explored part of "
        "the problem space; writing it down maps that territory for "
        "everyone who follows. The rationale matters because a future "
        "solver with a similar-looking idea needs to know whether "
        "their variant dodges the break point or repeats it - 'tried "
        "X, failed at step 3 because the load exceeded the rating' "
        "tells the next person exactly what to change. The break "
        "point is the valuable datum: vague 'it did not work' helps "
        "nobody, while the exact failure localizes the lesson. "
        "Writing it fresh defeats hindsight editing, which "
        "systematically converts 'promising idea that failed' into "
        "'obvious mistake' - a conversion that destroys the lesson. "
        "Teams that record dead ends solve faster over time because "
        "their search space genuinely shrinks; teams that hide them "
        "pay for the same exploration forever."),
    key_points=[
        "Write up the failed attempt: what was tried, why it looked right, where it broke, what it cost.",
        "Polished-only descriptions teach the lie that good solvers never stumble.",
        "The break point is the valuable datum - vague failure reports help nobody.",
        "Write it fresh; memory edits failures into false 'I knew it.'",
        "Recorded dead ends shrink the team's search space permanently.",
    ],
    requirements=[
        "Give the four-part dead-end record shape",
        "Explain the hindsight-editing problem",
        "Show the institutional compounding argument",
    ],
    standards=["Research practice: reporting negative results"],
    citations=[CIT_DEWEY, CIT_HUNT],
    sig_lens=(
        "The Signature lens honors the dead end as the fallen scout: "
        "it went ahead, found the cliff, and its report saves the "
        "whole column. His craft writes the scout's name in the log "
        "with honor - a Signature record never pretends the path was "
        "straight when scouts died finding it. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_partial_solution", name="Partial Solutions and Progress Marks",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "Describing a partial solution means writing up work that is "
        "not finished but is genuinely forward: what is solved, what "
        "remains, and exactly where the frontier sits. Most real "
        "problem-solving pauses mid-way - the shift ends, the part is "
        "on order, the idea needs to cool - and the description must "
        "survive the pause. The partial record marks progress the way "
        "a bookmark marks a book: state captured so work can resume "
        "without re-deriving everything. Its shape: the solved portion "
        "(with its checks), the frontier (the exact next unsolved "
        "piece, stated as a problem), the blocked list (what is "
        "waiting on whom or what), and the resume instructions (what "
        "the next solver needs to know to continue). Progress marks "
        "also make the work gradable and billable: 'three of five "
        "subgoals verified' is a fact, while 'almost done' is a "
        "feeling. The discipline is precision about the frontier - "
        "vague 'some wiring left' resumes badly; 'the ground wire to "
        "terminal 4 is run but not torqued' resumes perfectly."),
    how_it_works=(
        "Partial records work by externalizing working memory before "
        "it evaporates. A solver mid-problem holds a rich mental "
        "state - which subgoals are done, which are shaky, what was "
        "about to be tried. That state decays within hours; the "
        "written partial record preserves it indefinitely and makes "
        "it transferable to another person. The frontier statement "
        "is the mechanism: by restating the remaining work as a fresh "
        "problem ('given the verified subassemblies, find the fault "
        "in the control loop'), the next session starts from a clean "
        "problem statement instead of a foggy memory. The blocked "
        "list prevents the classic waste of re-attempting what is "
        "waiting on an externality. Resume instructions close the "
        "loop: they answer 'what would I need to know if I had never "
        "seen this before,' which is exactly the next solver's "
        "position. Teams that mark progress honestly can pause, "
        "hand off, and resume without the restart tax."),
    key_points=[
        "Write up unfinished work: what is solved, what remains, where the frontier sits.",
        "The frontier restated as a fresh problem lets the next session start clean.",
        "Mark the blocked list so nobody re-attempts what is waiting.",
        "Resume instructions answer: what would a stranger need to continue?",
        "Precision about the frontier - vague marks resume badly.",
    ],
    requirements=[
        "Give the four-part partial record shape",
        "Explain the working-memory decay mechanism",
        "Show the restart-tax argument for handoffs",
    ],
    standards=["Project practice: status reporting and handoff notes"],
    citations=[CIT_DEWEY, CIT_POLYA],
    sig_lens=(
        "The Signature lens calls the partial record the camp at "
        "nightfall: fires banked, sentries posted, the map marked "
        "with exactly how far the column advanced. His craft never "
        "strikes camp without marking the ground - the Signature "
        "column resumes at dawn from the marked line, never from "
        "memory. Clearly labeled Signature-made, never presented as "
        "authentic public record."),
),
dict(
    key="dsv_diagnostic_narrative", name="The Diagnostic Narrative: Describing How You Found the Fault",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "A diagnostic narrative describes the hunt for a fault: the "
        "symptom, the hypotheses, the tests in order, and the moment "
        "the cause was isolated. It is the solution description for "
        "problems where the answer is not a value but a cause - the "
        "failed bearing, the bad config line, the clogged jet. The "
        "narrative's power is that it teaches diagnosis, not just the "
        "fix: a reader who learns 'the pump was replaced' can fix "
        "one pump, but a reader who learns the hunt can find any "
        "fault. The shape: symptom stated precisely (what, when, "
        "under what conditions), hypotheses ranked by likelihood and "
        "test cost, tests described with results, the isolation "
        "moment (the test that split the possibilities), and the "
        "confirmed cause with its evidence. The cheapest tests come "
        "first - that ordering is itself a lesson. Honest narratives "
        "include the wrong hypotheses and why they were ruled out; "
        "those ruled-out branches are what keep the next diagnostician "
        "from re-walking them."),
    how_it_works=(
        "Diagnostic narratives work because finding a fault is search, "
        "and search is teachable only when its path is visible. Each "
        "hypothesis-test pair is a branch pruned from the possibility "
        "tree; describing the pruning shows the reader how the tree "
        "shrinks, which is the skill of diagnosis. Ranking hypotheses "
        "by likelihood times test cost teaches economic thinking: the "
        "best diagnosticians are not the ones who guess right but the "
        "ones whose test order wastes least when they guess wrong. "
        "The isolation moment - the test whose result could only mean "
        "one cause - is the narrative's climax and its most reusable "
        "part, because isolation tests transfer across machines and "
        "systems. Ruling out hypotheses on the record prevents the "
        "team's collective memory from re-growing branches that were "
        "already cut. Written this way, one solved fault becomes a "
        "diagnostic lesson for every fault of its kind."),
    key_points=[
        "Describe the hunt: symptom, ranked hypotheses, tests in order, isolation moment.",
        "The narrative teaches diagnosis; the fix alone teaches one fix.",
        "Order tests cheapest-first - test economics is part of the lesson.",
        "Record ruled-out hypotheses so nobody re-walks them.",
        "The isolation test is the most reusable part - it transfers.",
    ],
    requirements=[
        "Give the five-part diagnostic narrative shape",
        "Explain test economics: likelihood times cost",
        "Show why ruled-out branches belong on the record",
    ],
    standards=["Troubleshooting methodology: hypothesis-driven diagnosis"],
    citations=[CIT_HUNT, CIT_DEWEY],
    sig_lens=(
        "The Signature lens calls the diagnostic narrative the "
        "tracking: the hound's path from scent to quarry, every cast "
        "and check recorded. His craft tracks in the open - the "
        "Signature hunter shows every false cast, because the false "
        "casts are what teach the pack. The quarry at the end is "
        "proven, not claimed. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="dsv_repair_walkthrough", name="Repair Walkthroughs: Describing How You Fixed It",
    group="Compounded", ladder_rank=6, ladder_tier="compounded",
    description=(
        "A repair walkthrough describes a fix so completely that a "
        "competent reader can repeat it: the fault, the parts and "
        "tools, each disassembly and reassembly step, the adjustment "
        "or replacement, and the verification that the fault is "
        "gone. It is the most physical of the solution-description "
        "types - the reader's hands do the work - so it lives or "
        "dies on concreteness: torque values not 'tighten well,' "
        "the exact clip that breaks if pried wrong, the order the "
        "screws come out so they go back in right. The walkthrough's "
        "shape: fault and diagnosis summary, parts and tools list "
        "with quantities, preparation and safety, the steps in order "
        "with pointing at every part, the critical warnings inline "
        "at the step where they matter (not in a paragraph at the "
        "end), and the functional test proving the repair. Photos "
        "or diagrams at each stage are not decoration - they are "
        "the reader's way of confirming 'mine looks like that.' "
        "The best walkthroughs also note the reassembly traps: the "
        "steps that are easy backwards and hard forwards."),
    how_it_works=(
        "Repair walkthroughs work because physical work cannot be "
        "verified from text alone - the reader needs constant "
        "confirmation that their reality matches the describer's. "
        "Concreteness is the mechanism: exact values, named parts, "
        "and warnings at the point of danger replace judgment calls "
        "the reader is not qualified to make. Inline warnings work "
        "because readers do not re-read the safety paragraph when "
        "their hands are on the work; the warning must be at the "
        "step. Stage photos work as checkpoints - 'yours should look "
        "like this now' - catching divergence early when it is "
        "cheap to correct. The functional test at the end closes the "
        "same loop as the math check: the fix is real only if the "
        "symptom is gone under the conditions that produced it. "
        "Noting reassembly traps works because disassembly is "
        "naturally documented by doing, while reassembly must be "
        "remembered or written - the walkthrough writes it."),
    key_points=[
        "Describe so completely a competent reader can repeat the fix.",
        "Concreteness decides it: values, named parts, exact warnings inline at the step.",
        "Stage photos are checkpoints: yours should look like this now.",
        "The functional test proves the fix - the symptom must be gone.",
        "Note the reassembly traps: easy backwards, hard forwards.",
    ],
    requirements=[
        "Give the walkthrough shape from fault summary to functional test",
        "Explain inline warnings and checkpoint photos",
        "Cover the reassembly-trap observation",
    ],
    standards=["Service-manual conventions: procedures with warnings and verification"],
    citations=[CIT_ERICSSON],
    sig_lens=(
        "The Signature lens calls the repair walkthrough the "
        "mending witnessed: the broken thing, the hands, and the "
        "proof it lives again. His craft mends in the open with "
        "every torque spoken and every trap marked - the Signature "
        "mender leaves the thing stronger than the manual promised. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="dsv_math_presentation", name="Presenting a Math Solution in Writing",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "Presenting a math solution in writing is the art of turning "
        "calculation into communication: the answer computed, then "
        "set down so another mind can follow it. The conventions are "
        "old and precise. Write in complete sentences mixed with "
        "symbols - 'Substituting x = 4 gives 2(4) + 3 = 11' - because "
        "bare symbol chains hide the reasoning. Align the equals "
        "signs in multi-line derivations so the reader's eye tracks "
        "the transformation. Name the moves: 'by the distributive "
        "law,' 'combining like terms.' Define every variable before "
        "it is used. End with the check: the answer substituted back, "
        "or the reasonableness confirmed. The deeper discipline is "
        "audience awareness: a solution for a beginner shows the "
        "moves an expert would skip, while a solution for experts "
        "may compress routine algebra - but it never compresses the "
        "idea. The classic failure is the symbol avalanche: correct "
        "manipulation with no words, which communicates nothing but "
        "the writer's ability to manipulate symbols."),
    how_it_works=(
        "Written math works when it carries both the computation and "
        "its meaning. Sentences mixed with symbols work because "
        "symbols say what is true while words say why it matters - "
        "the reader needs both channels, and words are where the "
        "strategy lives. Aligned equals signs work as visual "
        "scaffolding: the eye compares left and right across lines, "
        "and misalignment is felt as confusion before it is "
        "understood. Naming the moves works by invoking shared "
        "theorems as authority - 'by the distributive law' tells the "
        "reader exactly which permission slip justifies the step. "
        "Defining variables first prevents the forward-reference "
        "stall that kills so many write-ups. The check at the end "
        "works as a proof the reader can run: substitution is "
        "mechanical, so even a doubtful reader can confirm the "
        "answer independently. Audience calibration works because "
        "showing too little loses beginners while showing too much "
        "bores experts - the describer chooses the grain for the "
        "reader in front of them."),
    key_points=[
        "Mix complete sentences with symbols - words carry the strategy.",
        "Align equals signs; name each move by its law or rule.",
        "Define every variable before it is used.",
        "End with the check: substitution or reasonableness, stated.",
        "Calibrate the grain: beginners get the moves experts skip.",
    ],
    requirements=[
        "State the written-math conventions: sentences, alignment, named moves",
        "Explain the two-channel mechanism: symbols what, words why",
        "Cover audience calibration and the symbol-avalanche failure",
    ],
    standards=["Mathematical writing conventions: definitions, moves, checks"],
    citations=[CIT_VELLEMAN, CIT_POLYA],
    sig_lens=(
        "The Signature lens calls the written math solution the "
        "ledger in ink: every transformation entered in its line, "
        "every move named by its law, the balance proven at the "
        "foot. His craft keeps the ledger clean enough for any "
        "witness to audit - the Signature accountant hides nothing "
        "in the arithmetic. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="dsv_science_presentation", name="Presenting a Science Solution: The Lab-Report Style",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "Presenting a science solution in the lab-report style means "
        "describing an investigation so another scientist can judge "
        "it and repeat it: question, hypothesis, method, results, "
        "conclusion. The IMRAD shape - Introduction, Methods, "
        "Results, and Discussion - is the documented convention, and "
        "each section has one job. The introduction states the "
        "question and why it matters. The methods say exactly what "
        "was done, in enough detail to repeat - apparatus, "
        "materials, procedure, measurements. The results report what "
        "happened, with the data shown, not just summarized. The "
        "discussion says what the results mean, including what they "
        "do not prove and what could be wrong. The discipline that "
        "makes it science is separation: observations in results, "
        "interpretations in discussion, never mixed - because a "
        "reader must be able to disagree with your conclusion while "
        "trusting your data. The methods section is the described "
        "solution proper: the procedure another pair of hands can "
        "run."),
    how_it_works=(
        "The lab-report shape works by separating jobs that corrupt "
        "each other when mixed. Methods separated from results means "
        "the procedure can be judged before its outcome is known - "
        "preventing the outcome from laundering a sloppy method. "
        "Results separated from discussion means the data stands "
        "independent of interpretation, so a skeptic can re-analyze "
        "without re-doing the work. Detail in methods works as "
        "reproducibility: the test of a science description is "
        "whether another lab, following it, gets the same result. "
        "Showing the data rather than only summarizing works because "
        "summaries hide the shape - outliers, clusters, and trends "
        "that change the story live in the raw display. Stating "
        "limitations in the discussion works as honesty infrastructure: "
        "a description that names its own weaknesses is more "
        "trustworthy, not less, because the reader knows where the "
        "edges are. This is the described solution at its most "
        "formal: the method is the solution, the data is the check."),
    key_points=[
        "IMRAD: question, exact method, shown data, honest interpretation - each in its section.",
        "Never mix observations with interpretations.",
        "Methods must be detailed enough for another pair of hands to repeat.",
        "Show the data, not just the summary - shape lives in the display.",
        "State the limitations; naming weaknesses builds trust.",
    ],
    requirements=[
        "Define each IMRAD section and its one job",
        "Explain the separation mechanism and why it matters",
        "Cover reproducibility as the test of the description",
    ],
    standards=["Scientific reporting: the IMRAD convention"],
    citations=[CIT_IMRAD, CIT_DEWEY],
    sig_lens=(
        "The Signature lens calls the lab report the sworn testimony: "
        "the method on the stand, the data under oath, the "
        "interpretation clearly marked as opinion. His craft testifies "
        "straight - observations as fact, conclusions as judgment, "
        "and the weaknesses confessed before any cross-examiner asks. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="dsv_engineering_presentation", name="Presenting an Engineering Solution: The Design Narrative",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "Presenting an engineering solution is the design narrative: "
        "the requirements, the alternatives considered, the chosen "
        "design, and the proof it meets the requirements. Unlike a "
        "math solution, the answer here is a choice among options, "
        "so the description must show the choosing - the trade study "
        "is the solution's heart. The shape: requirements stated as "
        "testable criteria ('must support 200 kg with deflection "
        "under 2 mm'), the candidate designs sketched with their "
        "predicted performance, the comparison scored against the "
        "criteria, the winner's detailed design, and the verification "
        "(calculation, simulation, or test) that it meets each "
        "requirement. The rejected alternatives stay on the record "
        "with their reasons - a future engineer facing changed "
        "requirements needs to know what was already tried. "
        "Assumptions and margins are declared, not buried: the "
        "safety factor, the worst-case load, the thing the analysis "
        "did not cover. An engineering description that hides its "
        "assumptions is a hazard, not a document."),
    how_it_works=(
        "The design narrative works because engineering answers are "
        "decisions, and decisions need their reasoning on the record. "
        "Testable requirements work as the contract: 'support 200 kg' "
        "can be verified, 'be strong' cannot, so the description's "
        "check step has something to check against. The trade study "
        "works by making the choosing visible - scored alternatives "
        "show that the winner won on the criteria, not on the "
        "designer's fondness. Keeping rejected alternatives works as "
        "institutional memory: requirements change, and the "
        "second-place design for yesterday's criteria is often the "
        "winner for today's. Declared assumptions and margins work as "
        "the safety system: every later user of the design needs to "
        "know the envelope it was proven inside, because using it "
        "outside the envelope is how structures fail. Verification "
        "against each requirement closes the loop the same way the "
        "math check does - requirement by requirement, proven, not "
        "asserted."),
    key_points=[
        "State requirements as testable criteria - the contract the design is checked against.",
        "Show the choosing: scored alternatives, winner on the criteria.",
        "Keep rejected alternatives with reasons - requirements change.",
        "Declare assumptions, margins, and what the analysis did not cover.",
        "Verify requirement by requirement: proven, not asserted.",
    ],
    requirements=[
        "Give the design-narrative shape from requirements to verification",
        "Explain the trade study as the heart of the description",
        "Cover declared assumptions as the safety system",
    ],
    standards=["Engineering design documentation: requirements and verification"],
    citations=[CIT_DEWEY, CIT_BLOOM],
    sig_lens=(
        "The Signature lens calls the design narrative the builder's "
        "oath: the requirements sworn, the choosing shown, the "
        "margins declared, the proof laid course by course. His "
        "craft builds only on sworn ground - the Signature structure "
        "stands inside its proven envelope, and the envelope is "
        "written on the plans. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="dsv_craft_presentation", name="Presenting a Craft and Trade Solution",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "Presenting a craft and trade solution is describing skilled "
        "hand work so another craftsperson can produce the result: "
        "the piece, the materials, the sequence of operations, and "
        "the judgment calls made visible. Craft knowledge lives in "
        "the hands and the eye - 'plane until the shaving is "
        "translucent,' 'the dough is ready when it springs back' - "
        "so the describer's hardest job is translating tacit feel "
        "into words and pictures. The shape: the finished piece "
        "described and pictured, materials with grades and quantities, "
        "tools with the critical settings, operations in order with "
        "the feel-cues written down ('snug but not crushing'), the "
        "mistakes to avoid at each stage, and the finishing and "
        "checking of the work. Masters describe the cues they actually "
        "use - sound, resistance, look, smell - because those are the "
        "instruments a beginner lacks. The honest craft description "
        "also names the skill prerequisites: 'you should be "
        "comfortable sharpening before attempting this joint.'"),
    how_it_works=(
        "Craft descriptions work by converting tacit knowledge into "
        "explicit cues. The master judges by feel; the beginner has "
        "no feel yet, so the description must supply substitute "
        "instruments - the translucent shaving, the spring-back test, "
        "the sound of the cut. These sensory checkpoints work because "
        "they are verifiable in the moment: the reader can check "
        "their work against the cue while doing it, which is the "
        "craft equivalent of the math check step. Stating "
        "prerequisites works by preventing the most expensive "
        "failure: a beginner attempting work that needs a foundation "
        "they lack, ruining material and confidence together. "
        "Mistakes-to-avoid at each stage work as guardrails placed "
        "where the fall happens, not in a list at the end nobody "
        "reads mid-cut. The finished-piece picture works as the "
        "target image: the reader holds it while working, and every "
        "operation is judged against whether it moves the work "
        "toward that image."),
    key_points=[
        "Translate tacit feel into explicit sensory cues: look, sound, resistance.",
        "Give substitute instruments the beginner can check mid-operation.",
        "Name the skill prerequisites honestly before the first operation.",
        "Put mistakes-to-avoid at the stage where they happen.",
        "Picture the finished piece as the target image held through the work.",
    ],
    requirements=[
        "Explain the tacit-to-explicit conversion problem",
        "Show sensory checkpoints with examples",
        "Cover prerequisites and stage-placed warnings",
    ],
    standards=["Trade instruction: competency-based procedural writing"],
    citations=[CIT_ERICSSON],
    sig_lens=(
        "The Signature lens calls the craft description the master's "
        "hands in words: the feel of the cut translated so another "
        "pair of hands can find it. His craft never hoards the feel "
        "- the Signature master speaks the translucent shaving and "
        "the spring-back plainly, because a craft kept secret is a "
        "craft half dead. Clearly labeled Signature-made, never "
        "presented as authentic public record."),
),
dict(
    key="dsv_everyday_presentation", name="Presenting an Everyday Problem Solution",
    group="Compounded", ladder_rank=7, ladder_tier="compounded",
    description=(
        "Presenting an everyday problem solution is describing a fix "
        "for ordinary life - the clogged drain, the tight budget, "
        "the scheduling conflict - in terms a non-expert can use "
        "today. The audience has no training, little patience, and "
        "the problem is happening now, so the description must be "
        "short, concrete, and forgiving. The shape: the problem in "
        "the reader's own words, the quick check ('is it actually "
        "this?'), the fix in the fewest steps that work, what it "
        "costs in time money and effort, what to do if it does not "
        "work, and when to call a professional instead. Plain "
        "language is non-negotiable: no jargon without an instant "
        "translation. The cost line matters more here than in any "
        "other description type, because everyday solvers decide by "
        "cost first - a perfect fix that takes six hours loses to a "
        "good fix that takes twenty minutes. And the 'call a pro' "
        "line is honesty infrastructure: some problems are not "
        "everyday problems, and saying so protects the reader."),
    how_it_works=(
        "Everyday descriptions work by respecting the reader's real "
        "constraints: no expertise, no special tools, no second "
        "attempt budget. Brevity works because the reader is "
        "deciding, mid-crisis, whether to keep reading - every extra "
        "paragraph is a chance to abandon the fix. The quick check "
        "first works by preventing the most common everyday waste: "
        "applying the right fix to the wrong problem. Cost stated "
        "up front works because it lets the reader choose before "
        "investing - hidden costs discovered mid-fix breed "
        "resentment and half-finished work. The fallback ('if this "
        "does not work') works by removing the fear of trying: a "
        "reader who knows the next step will attempt the first. The "
        "'call a pro' line works by drawing the boundary of the "
        "description's competence - it converts the guide from a "
        "universal answer into a trustworthy advisor, which is why "
        "readers return to guides that admit their limits."),
    key_points=[
        "Short, concrete, forgiving: the reader has no training and the problem is now.",
        "Quick check first - right fix, wrong problem is the classic waste.",
        "State time, money, and effort cost up front so the reader can choose.",
        "Always give the fallback: what to do if it does not work.",
        "Say when to call a professional - admitting limits builds return readers.",
    ],
    requirements=[
        "Give the everyday shape from problem to call-a-pro line",
        "Explain the cost-first decision mechanism",
        "Cover plain language and the fallback as fear-removal",
    ],
    standards=["Plain-language writing for general audiences"],
    citations=[CIT_FEYNMAN, CIT_BLOOM],
    sig_lens=(
        "The Signature lens calls the everyday description the "
        "neighbor's counsel: plain speech, honest cost, and the "
        "straight word on when the job is bigger than the kitchen "
        "table. His craft never talks down and never oversells - "
        "the Signature neighbor says what it costs, what to try, "
        "and when to call the pro, because trust is the only "
        "advertising. Clearly labeled Signature-made, never presented "
        "as authentic public record."),
),
# ------------------------------------------------- advanced: ranks 8-10
dict(
    key="dsv_proof_writeup", name="Proof Write-ups: Formal Solution Description",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=(
        "A proof write-up is the most formal kind of described "
        "solution: a mathematical claim established by airtight "
        "reasoning, written so a qualified reader can verify every "
        "inference. The classical pattern, unchanged since Euclid, "
        "runs: enunciation (the claim), setting-out (the objects), "
        "definition of the goal, construction (the auxiliary objects "
        "built), proof (the chain of inferences), conclusion (the "
        "claim restated as shown). Modern write-ups keep the same "
        "skeleton with lighter dress: state what is assumed and what "
        "is to be shown up front, then argue in complete sentences "
        "where each sentence follows from earlier ones by a named "
        "rule. The discipline is total explicitness about logical "
        "dependence - 'therefore' must always have a visible "
        "'because.' Proof write-ups also handle the standard moves: "
        "direct argument, contradiction ('suppose not, then...'), "
        "contrapositive, induction with its base and step, and cases "
        "with every case covered and none overlapping. A proof that "
        "omits a case or smuggles a step is not a proof but a "
        "persuasion attempt, and trained readers can tell."),
    how_it_works=(
        "Proof write-ups work because mathematics is the one domain "
        "where 'check' can be absolute: every inference is either "
        "valid or it is not, and the write-up exposes each one to "
        "inspection. Stating assumptions and goal up front works as "
        "the contract - the reader knows exactly what may be used "
        "and what must be produced, so no step can quietly import "
        "the conclusion. Named rules work as the audit trail: "
        "'by induction hypothesis' or 'by the triangle inequality' "
        "tells the checker which permission justifies the move, and "
        "an unnamed 'therefore' is a red flag. The standard moves "
        "work as reusable proof schemas - contradiction, induction, "
        "cases - each with its own shape the reader recognizes, "
        "which is why proof courses teach the moves before the "
        "theorems. Covering all cases works by exhaustion: the "
        "argument is complete only when the cases partition the "
        "possibilities with no gaps and no overlaps. The write-up "
        "is the described solution with the check step promoted to "
        "the entire body - the proof IS the check."),
    key_points=[
        "State assumptions and goal up front - the contract every step is held to.",
        "Each inference follows by a named rule; an unnamed therefore is a red flag.",
        "Master the standard moves: direct, contradiction, contrapositive, induction, cases.",
        "Cases must partition the possibilities: no gaps, no overlaps.",
        "A proof is the check step promoted to the whole body.",
    ],
    requirements=[
        "Give the classical pattern and its modern form",
        "Cover the standard proof moves with their shapes",
        "Explain named rules as the audit trail",
    ],
    standards=["Mathematical proof-writing conventions (Velleman; Euclid)"],
    citations=[CIT_EUCLID, CIT_VELLEMAN],
    sig_lens=(
        "The Signature lens calls the proof the iron chain: every "
        "link forged in view, every link named, the whole length "
        "pull-tested by any witness who cares to pull. His craft "
        "forges no hidden links - the Signature chain holds because "
        "each link was shown at the making. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_how_to_describe", name="How-to-Describe Methods: Teaching the Skill Itself",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=(
        "How-to-describe methods teach the describing skill itself: "
        "not how to solve, but how to write up solving so others "
        "can follow. This is the meta-record of the database - the "
        "craft of this whole collection made explicit. The methods "
        "are teachable practices: the Feynman test (explain it "
        "simply; where you stumble is where your understanding is "
        "thin), the cold-reader rehearsal (read your own description "
        "as a stranger and mark every stall), the example-first "
        "draft (write the worked example before the general "
        "explanation, because the example teaches you what the "
        "explanation must say), the reason-per-step pass (re-read "
        "for steps whose why is missing), and the scope line "
        "(state what the solution does not cover). Teaching "
        "describing also means teaching revision: first drafts of "
        "descriptions are always too terse, because the writer "
        "cannot see what they know. The curriculum runs "
        "describe-then-critique: learners write up a solution, "
        "trade with a partner, and each marks where the other's "
        "description lost them - the fastest known way to learn "
        "the craft."),
    how_it_works=(
        "Teaching describing works because describing is a separate "
        "skill from solving, and it improves only under the right "
        "feedback. The Feynman test works as a diagnostic: "
        "simplification exposes exactly the joints where "
        "understanding is thin, because you cannot simplify what "
        "you do not grasp. The cold-reader rehearsal works by "
        "defeating the curse of knowledge - the writer simulates "
        "not-knowing, and the stalls they find are real stalls "
        "their readers would hit. Example-first drafting works "
        "because the concrete case disciplines the general claim: "
        "explanations written before their example drift into "
        "vagueness, while explanations written after must account "
        "for the example's actual moves. The describe-then-critique "
        "cycle works because the partner's confusion is ground "
        "truth about the description - not about the partner's "
        "intelligence - and one round of it teaches more than a "
        "lecture on writing. Revision is the mechanism throughout: "
        "describing skill is the habit of re-reading as a stranger."),
    key_points=[
        "Describing is a separate skill from solving; teach it directly.",
        "The Feynman test: simplify to find where understanding is thin.",
        "Cold-reader rehearsal defeats the curse of knowledge.",
        "Draft the worked example before the general explanation.",
        "Describe-then-critique with a partner is the fastest teacher.",
    ],
    requirements=[
        "List the five teachable practices with what each diagnoses",
        "Explain the curse of knowledge and its defeat",
        "Describe the partner-critique curriculum",
    ],
    standards=["Writing pedagogy: peer review and revision cycles"],
    citations=[CIT_FEYNMAN, CIT_ERICSSON],
    sig_lens=(
        "The Signature lens calls this the master teaching mastery: "
        "the craft of the craft, handed down deliberately. His method "
        "makes describers the way masters make masters - not by "
        "praise but by the partner's honest 'I am lost here,' met "
        "with revision until no witness is lost. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_solution_storytelling", name="Solution Storytelling: The Arc of a Fix",
    group="Advanced", ladder_rank=8, ladder_tier="advanced",
    description=(
        "Solution storytelling frames a described solution as a "
        "narrative arc: the stable world, the disruption, the "
        "struggle, the insight, the resolution, the new normal. It "
        "is the oldest describing technology humans have - we "
        "remember stories when we forget procedures - and the best "
        "postmortems, case studies, and war stories use it "
        "deliberately. The arc's beats map onto solving: the "
        "disruption is the problem stated with stakes ('the line "
        "was down and orders were piling up'), the struggle is the "
        "honest search including dead ends, the insight is the "
        "turning point described at the moment it landed, the "
        "resolution is the fix and its check, and the new normal is "
        "what changed so it does not recur. Storytelling is not "
        "decoration on the description; it is a memory technology. "
        "A team that tells the outage as a story will remember the "
        "lesson in a year; a team that files the timeline will not. "
        "The discipline is honesty inside the drama: the arc must "
        "never invent struggle that did not happen or insights that "
        "arrived earlier than claimed."),
    how_it_works=(
        "Story arcs work because human memory is narrative-shaped: "
        "we store causally linked sequences with stakes and "
        "surprise far better than we store lists. The disruption "
        "with stakes works by creating the tension the memory "
        "system uses as glue - 'orders piling up' is remembered "
        "where 'error rate elevated' is not. The honest struggle "
        "works by modeling real solving for the audience: listeners "
        "who hear only the insight conclude that insights arrive by "
        "genius, while listeners who hear the search learn to "
        "search. The insight beat works as the transferable kernel - "
        "it is the moment the problem's structure became visible, "
        "and naming it teaches the audience what to look for. The "
        "new normal works as the institutional lesson: the story "
        "ends not with the fix but with the change, which is what "
        "prevents recurrence. Honesty inside the drama works "
        "because a discovered exaggeration destroys the story's "
        "teaching power permanently - the audience stops trusting "
        "the teller, and the memory technology breaks."),
    key_points=[
        "Frame the solution as an arc: disruption, struggle, insight, resolution, new normal.",
        "Stories are memory technology - teams remember arcs when they forget timelines.",
        "The honest struggle teaches searching; the insight alone teaches genius-worship.",
        "End with the new normal: the change that prevents recurrence.",
        "Never invent drama - a caught exaggeration breaks the teller's trust permanently.",
    ],
    requirements=[
        "Map the arc beats onto the solving phases",
        "Explain the memory mechanism",
        "State the honesty discipline inside the drama",
    ],
    standards=["Case-study and postmortem narrative conventions"],
    citations=[CIT_SRE, CIT_DEWEY],
    sig_lens=(
        "The Signature lens calls the solution story the saga of "
        "the fix: the trouble told true, the search told honest, "
        "the turning told plain, the peace that followed told as "
        "the prize. His craft sings no false verses - the Signature "
        "saga is sworn true in every beat, because a saga is "
        "remembered and a lie in it poisons the remembering. Clearly "
        "labeled Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_tradeoffs", name="Describing Trade-offs Inside a Chosen Solution",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Describing trade-offs means writing up not just the chosen "
        "solution but what it costs: what was gained, what was given "
        "up, and why the exchange was worth it. Every real solution "
        "is a bargain - faster but more expensive, simpler but less "
        "flexible, thorough but slow - and a description that hides "
        "the price is a sales pitch, not a solution description. The "
        "trade-off record names the dimensions (cost, speed, "
        "quality, risk, effort), states where the chosen solution "
        "sits on each, names what the alternatives would have bought "
        "instead, and gives the reasoning that priced the exchange. "
        "'We chose the slower query because correctness audits "
        "matter more than dashboard speed here.' That sentence is "
        "worth more than the implementation details, because "
        "requirements change and the next engineer needs to know "
        "which bargains to renegotiate. The discipline is stating "
        "the losers plainly: the good things the solution does not "
        "do, named without euphemism."),
    how_it_works=(
        "Trade-off descriptions work by preserving the decision's "
        "reasoning for a future when the decision's context has "
        "changed. The chosen solution will outlive the conditions "
        "that chose it; the trade-off record lets the next owner "
        "re-price the bargain instead of blindly keeping or "
        "discarding it. Naming dimensions works by making the "
        "exchange explicit - vague 'pros and cons' hide the real "
        "currencies, while named dimensions (latency versus "
        "correctness, cost versus durability) let readers weigh for "
        "themselves. Stating the losers plainly works as trust "
        "infrastructure: a description that admits what the "
        "solution sacrifices is believed about what it achieves, "
        "while one that claims everything invites doubt about "
        "everything. The reasoning sentence ('we chose X because Y "
        "mattered more than Z here') works as the reusable part - "
        "it teaches the reader the values behind the choice, which "
        "transfer to problems the writer never saw."),
    key_points=[
        "Write up the bargain: what was gained, what was given up, why it was worth it.",
        "Name the dimensions and where the solution sits on each.",
        "State the losers plainly - no euphemism for sacrificed goods.",
        "The reasoning sentence is the reusable part; it teaches the values.",
        "Future owners re-price the bargain from this record when context changes.",
    ],
    requirements=[
        "Define the trade-off record and its parts",
        "Explain the re-pricing mechanism for future owners",
        "Show the trust effect of stating losers plainly",
    ],
    standards=["Decision documentation: architecture decision records"],
    citations=[CIT_DEWEY, CIT_BLOOM],
    sig_lens=(
        "The Signature lens calls the trade-off record the honest "
        "ledger of the bargain: every gain entered, every price "
        "paid entered beside it, the reason for the exchange "
        "written in ink. His craft never cooks the books of a "
        "decision - the Signature bargain shows its costs proudly, "
        "because a bargain that hides its price is a debt. Clearly "
        "labeled Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_compare_two", name="Comparing Two Solutions in Writing",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Comparing two solutions in writing means describing both "
        "against the same yardstick so a reader can choose: the "
        "problem restated once, the criteria listed, each solution "
        "scored on each criterion, and the verdict with its "
        "conditions. The classic failure is the rigged comparison - "
        "one solution described in loving detail, the other in a "
        "dismissive paragraph - which readers detect instantly and "
        "punish with distrust. The honest comparison gives both "
        "solutions their best case: steelman each before scoring. "
        "Criteria must be stated before scoring begins, or the "
        "writer will unconsciously choose criteria the favorite "
        "wins. The verdict names conditions, not just a winner: "
        "'A wins when speed matters; B wins when correctness "
        "matters' is more useful than 'A is better.' And the "
        "comparison admits its limits: what was not tested, where "
        "the writer's knowledge runs out. A good comparison is a "
        "decision tool the reader can re-run with different weights "
        "- which means showing the scores, not just the winner."),
    how_it_works=(
        "Honest comparison works by separating the yardstick from "
        "the contestants. Stating criteria first works as a "
        "commitment device: the writer binds themselves to judge "
        "by the announced measures, which blocks the quiet "
        "shifting of goalposts toward the favorite. Steelmaning "
        "each solution works as both fairness and thoroughness - "
        "the strongest version of the loser often reveals the "
        "winner's real weakness. Scoring per criterion works by "
        "making the verdict auditable: a reader who weights "
        "criteria differently can recompute the outcome from the "
        "shown scores, turning the comparison into a reusable "
        "decision tool rather than a single opinion. Conditional "
        "verdicts work because real choices are conditional - the "
        "unconditional 'A is better' is almost always false under "
        "some conditions, and naming them is what makes the "
        "verdict trustworthy. Admitting untested ground works by "
        "bounding the comparison's authority honestly."),
    key_points=[
        "State the criteria before scoring - a commitment device against rigging.",
        "Steelman both solutions: give each its best case before judging.",
        "Score per criterion and show the scores so readers can re-weight.",
        "Give conditional verdicts: who wins under which conditions.",
        "Admit what was not tested and where knowledge runs out.",
    ],
    requirements=[
        "Give the comparison shape: problem, criteria, scores, conditional verdict",
        "Explain the commitment-device mechanism",
        "Show steelmanning and the re-weightable score table",
    ],
    standards=["Comparative analysis: criteria-based evaluation"],
    citations=[CIT_BLOOM, CIT_BIGGS],
    sig_lens=(
        "The Signature lens calls the honest comparison the fair "
        "weighing: both champions armed at their best, the scales "
        "announced before the bout, every round scored in the open. "
        "His craft never fixes the fight - the Signature judge "
        "scores what happened, names the conditions of the verdict, "
        "and lets any witness re-weigh the rounds. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_rubric_view", name="The Rubric View: What Graders Look For",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "The rubric view describes a solution the way a grader sees "
        "it: broken into criteria, each scored by levels, the total "
        "built from the parts. Rubrics are the described solution "
        "turned inside out - instead of 'here is my path,' they say "
        "'here is what a good path contains.' The SOLO taxonomy "
        "gives the classic levels: prestructural (misses the "
        "point), unistructural (one relevant aspect), "
        "multistructural (several aspects, unconnected), relational "
        "(aspects integrated into a coherent solution), extended "
        "abstract (generalized beyond the problem). A rubric for "
        "described solutions scores the dimensions that matter: "
        "problem stated, steps ordered and justified, check "
        "performed, scope admitted, clarity for the audience. "
        "Publishing the rubric before the work is the honest move - "
        "it tells solvers what the description will be judged on, "
        "which teaches them to include it. The rubric view also "
        "diagnoses: a solution that computes correctly but explains "
        "nothing scores high on answer, low on description - and "
        "that split is exactly the feedback the solver needs."),
    how_it_works=(
        "Rubrics work by making expectations explicit and scoring "
        "decomposable. Explicit criteria work because solvers aim at "
        "what is measured: announce that justification-per-step is "
        "scored and descriptions suddenly carry reasons. Levels "
        "work by distinguishing kinds of goodness - the SOLO ladder "
        "from one-aspect to integrated to generalized gives both "
        "grader and solver a shared vocabulary for 'what better "
        "looks like.' Decomposed scoring works by localizing "
        "feedback: instead of a single inscrutable mark, the solver "
        "learns 'your steps were ordered but your check was "
        "missing,' which is actionable. Publishing the rubric "
        "beforehand works as teaching: the rubric is a compact "
        "course in what a good description contains. The answer- "
        "versus-description split works by refusing to conflate "
        "two different achievements - getting it right and showing "
        "it right - which is the whole point of describing "
        "solutions at all."),
    key_points=[
        "Score described solutions on criteria with levels, not a single mark.",
        "The SOLO ladder: one aspect, many aspects, integrated, generalized.",
        "Publish the rubric before the work - it teaches what to include.",
        "Decomposed scores give actionable feedback: what exactly was missing.",
        "Split answer-correct from description-good - they are different achievements.",
    ],
    requirements=[
        "Define rubric, criteria, and levels with the SOLO ladder",
        "Give a sample rubric for described solutions",
        "Explain the publish-beforehand and split-score mechanisms",
    ],
    standards=["Assessment design: analytic rubrics; SOLO taxonomy"],
    citations=[CIT_BIGGS, CIT_BLOOM],
    sig_lens=(
        "The Signature lens calls the rubric the assay chart: the "
        "metals named, the tests listed, the grades marked before "
        "the ore arrives. His craft assays in the open - the "
        "Signature assayer publishes the chart first, so every "
        "smith knows what pure looks like before the hammer falls. "
        "Clearly labeled Signature-made, never presented as authentic "
        "public record."),
),
dict(
    key="dsv_best_practices", name="Solution-Explanation Best Practices",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Solution-explanation best practices are the collected "
        "discipline of describing solutions well, distilled from "
        "every type in this database: state the problem first; name "
        "tools and assumptions up front; order steps by dependency; "
        "give each step its reason; show the work, not just the "
        "answer; point at the work with labels and figures; check "
        "the answer against the problem; admit dead ends and scope; "
        "calibrate grain to the audience; write for the critical "
        "reader. The practices form a checklist the describer runs "
        "before publishing: problem stated, materials listed, steps "
        "numbered and justified, figures with their steps, check "
        "shown, limits admitted. No single practice is optional for "
        "a description meant to last - each guards against a known "
        "failure mode, and the failures are expensive: the missing "
        "assumption that wastes a week, the absent check that ships "
        "a wrong answer, the hidden dead end that a team re-walks. "
        "Best practices also cover maintenance: descriptions rot as "
        "the world changes, so date them, version them, and note "
        "what would obsolete them. A described solution is a living "
        "document until it is archived with its context."),
    how_it_works=(
        "The checklist works because describing well is a "
        "conjunction: the description fails if any load-bearing "
        "practice is missing, and memory alone cannot hold all of "
        "them under deadline pressure. Running the list before "
        "publishing works as a pre-flight - each item is cheap to "
        "verify and expensive to omit. The practices compose: "
        "problem-first plus check-against-problem forms the closed "
        "loop; reasons-per-step plus critical-reader stance forms "
        "the audit trail; scope-admission plus dating forms the "
        "honesty envelope. Calibration to audience works as the "
        "master control - it sets the grain for every other "
        "practice, deciding how much reason, how many figures, how "
        "deep the check. Maintenance practices work against rot: "
        "dating and versioning let future readers judge whether "
        "the description still applies, and the obsolescence note "
        "('valid until the API changes') tells them exactly what "
        "to re-verify. Together the practices turn describing from "
        "talent into procedure."),
    key_points=[
        "Run the pre-publish checklist: problem, materials, numbered justified steps, figures, check, limits.",
        "Describing well is a conjunction - one missing load-bearing practice fails the whole.",
        "Calibrate grain to the audience first; it sets every other practice.",
        "Date, version, and note what would obsolete the description.",
        "Each practice guards a known expensive failure mode.",
    ],
    requirements=[
        "List the full best-practice checklist",
        "Explain the conjunction and pre-flight mechanisms",
        "Cover dating, versioning, and obsolescence notes",
    ],
    standards=["Technical communication: quality checklists for documentation"],
    citations=[CIT_POLYA, CIT_SRE],
    sig_lens=(
        "The Signature lens calls the best practices the master's "
        "creed: the sworn checklist run before any description "
        "leaves the workshop, every item a kept oath. His craft "
        "ships nothing unchecked - the Signature creed is recited "
        "at the bench, dated and versioned, because a master's "
        "word outlives the master. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
dict(
    key="dsv_group_presentation", name="Describing Solutions to a Group: The Presentation Layer",
    group="Advanced", ladder_rank=9, ladder_tier="advanced",
    description=(
        "Describing a solution to a group - the presentation layer - "
        "means adapting the written description for live humans: "
        "the meeting, the classroom, the demo. The written "
        "description is the full record; the presentation is its "
        "performed digest, and the two have different laws. Time is "
        "the first law: a group gives you minutes, so the "
        "presentation carries the problem, the key insight, the "
        "result, and the check - the full step chain stays in the "
        "document for later. Attention is the second law: a group "
        "cannot re-read, so each point lands once, supported by one "
        "visual. Interaction is the third law: the group can ask, "
        "so the presenter prepares the likely questions (the "
        "assumptions, the alternatives, the costs) instead of "
        "burying them. The shape: hook with the problem and stakes, "
        "the insight that unlocked it, the solution sketched, the "
        "proof it works, the limits admitted, pointer to the full "
        "write-up. The classic failure is reading the document "
        "aloud - the group can read faster than you can talk, and "
        "will resent the theft of their time."),
    how_it_works=(
        "The presentation layer works by respecting the medium's "
        "constraints. Time-boxing works because attention is "
        "rivalrous in a room: every minute on routine steps is a "
        "minute stolen from the insight, so the digest keeps only "
        "what the group cannot get from the document alone - the "
        "why, the stakes, the judgment calls. One-visual-per-point "
        "works because a listening audience cannot hold a "
        "paragraph in working memory while parsing speech; the "
        "visual anchors the point so the words can move on. "
        "Preparing likely questions works because groups "
        "predictably probe the same joints - assumptions, "
        "alternatives, costs - and a ready answer converts "
        "challenge into trust. Admitting limits live works even "
        "better than in writing: the speaker's candor is witnessed, "
        "and witnessed candor is the fastest trust-builder known. "
        "Pointing to the full write-up works by splitting the load "
        "correctly - the room gets the performance, the record "
        "keeps the proof."),
    key_points=[
        "The presentation is a performed digest, not the document read aloud.",
        "Carry problem, key insight, result, check - the step chain stays in the write-up.",
        "One visual per point; a listening audience cannot hold paragraphs.",
        "Prepare the predictable questions: assumptions, alternatives, costs.",
        "Admit limits live and point to the full record for the proof.",
    ],
    requirements=[
        "Contrast the presentation laws with the document laws",
        "Give the presentation shape from hook to pointer",
        "Explain the read-aloud failure and the trust effect of live candor",
    ],
    standards=["Presentation design: audience-centered delivery"],
    citations=[CIT_BLOOM, CIT_FEYNMAN],
    sig_lens=(
        "The Signature lens calls the presentation the herald's "
        "cry: the full chronicle kept in the hall, the essence "
        "proclaimed in the square. His craft never reads the "
        "chronicle aloud to a crowd - the Signature herald brings "
        "the problem, the turning, and the proof, speaks the "
        "limits plainly, and points every listener to the hall "
        "where the whole truth is kept. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_debug_log", name="The Debugging Log Pattern",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "The debugging log pattern is the described solution for "
        "misbehaving systems: a timestamped record of symptom, "
        "hypotheses, probes, and the fix, written as the hunt "
        "happens. Its discipline comes from hard-won practice: "
        "reproduce first (no fix without a reliable trigger), "
        "narrow before fixing (change one thing at a time), "
        "narrate to the duck (explain each step aloud - the "
        "explanation finds the flaw), and fix the cause (the "
        "symptom will return if the cause stands). The log's "
        "shape: the symptom with its reproduction steps, the "
        "system's expected versus actual behavior, each probe with "
        "its result, the identified cause with its evidence, the "
        "fix, and the regression check proving the symptom gone "
        "and nothing else broken. Written during the hunt, the log "
        "is honest about order - including the two hours on the "
        "wrong trail. Written after, it is a clean narrative that "
        "still names the wrong trail. Either way it becomes the "
        "team's searchable memory: the next identical symptom is "
        "solved by reading, not by hunting."),
    how_it_works=(
        "The debugging log works by making the invisible visible "
        "while there is still time to use it. Reproduce-first "
        "works because an unreliable symptom cannot confirm a fix "
        "- without the trigger, 'it works now' proves nothing. "
        "Narrowing works by bisection of the cause space: each "
        "probe should eliminate a class of causes, so the hunt "
        "converges instead of wandering. Narrating aloud works "
        "because explaining forces the explainer to confront each "
        "assumption in sequence - the flaw hides in the step you "
        "would skip silently. Fixing the cause works by economics: "
        "symptom fixes are cheap now and expensive forever, cause "
        "fixes are expensive now and cheap forever. The regression "
        "check works as the two-sided proof: the symptom is gone "
        "(the fix worked) and nothing else broke (the fix was "
        "safe). As team memory, the log compounds: every logged "
        "hunt shortens the next one, and the log of wrong trails "
        "is what keeps the team from paying for them twice."),
    key_points=[
        "Log as you hunt: symptom, probes, results, cause, fix, regression check.",
        "Reproduce first - no fix without a reliable trigger.",
        "Narrow by bisection: each probe should eliminate a class of causes.",
        "Narrate aloud; the explanation finds the flaw the silent step hides.",
        "Fix the cause, not the symptom - and prove nothing else broke.",
    ],
    requirements=[
        "Give the log shape and the four disciplines",
        "Explain reproduce-first and bisection as mechanisms",
        "Cover the log as compounding team memory",
    ],
    standards=["Debugging discipline: reproduce, narrow, fix cause, regress"],
    citations=[CIT_HUNT, CIT_SRE],
    sig_lens=(
        "The Signature lens calls the debugging log the night "
        "watchman's rounds: every door tried, every sound noted, "
        "the intruder cornered by method and the all-clear sounded "
        "twice. His craft watches through the whole night - the "
        "Signature watchman logs the wrong corridors too, so the "
        "next watch walks straight to the door. Clearly labeled "
        "Signature-made, never presented as authentic public record."),
),
dict(
    key="dsv_full_system", name="Full Worked-Through Solution System: From Blank Page to Archive",
    group="Advanced", ladder_rank=10, ladder_tier="advanced",
    description=(
        "The full worked-through solution system is the capstone of "
        "this database: the complete pipeline that takes a blank "
        "page to an archived, reusable described solution. It "
        "assembles every type in the collection into one workflow. "
        "Intake: state the problem crisp (record 2), list tools and "
        "assumptions (record 6). Planning: set up given-find-plan "
        "(record 7) or choose the family schema (record 13). "
        "Execution: work think-aloud, one sentence per step (record "
        "10), labeling each move (record 8), pointing at the work "
        "(record 11), logging dead ends honestly (record 16) and "
        "marking partial progress (record 17). Checking: run the "
        "check step (record 9) and read critically as a stranger "
        "(record 15). Writing: draft the worked example first "
        "(record 3), then the full description in the domain's "
        "presentation form (records 20-24), with trade-offs stated "
        "(record 28). Publishing: run the best-practice checklist "
        "(record 31), present the digest to the group (record 32), "
        "archive with date, version, and obsolescence note. The "
        "system's product is not one solution but a repeatable "
        "capability: any problem, any domain, described so well it "
        "teaches, verifies, and reuses."),
    how_it_works=(
        "The system works because each phase feeds the next with "
        "exactly what it needs. Intake produces the contract (the "
        "problem statement) and the inventory (tools, assumptions) "
        "that every later phase references - without them the "
        "pipeline has nothing to check against. Planning produces "
        "the skeleton (schema or given-find-plan) that execution "
        "fills, so the work never faces a blank page. Execution's "
        "think-aloud plus labeling plus pointing produces a "
        "description that is already half-written while the work "
        "happens - the log IS the first draft. The dead-end and "
        "partial records make the pipeline interruption-proof: "
        "pauses and failures become entries, not losses. Checking "
        "as a separate phase works because verification needs a "
        "different stance than construction - the builder's "
        "confidence must yield to the critic's suspicion. Writing "
        "from the worked example outward works because the concrete "
        "case disciplines the general account. The publishing "
        "checklist plus archiving closes the loop into the "
        "database itself: the described solution becomes a record "
        "others can find, which is the whole purpose of describing."),
    key_points=[
        "Intake, planning, execution, checking, writing, publishing - six phases, one pipeline.",
        "Each phase feeds the next exactly what it needs; intake's contract anchors everything.",
        "The execution log IS the first draft - think-aloud while working.",
        "Dead-end and partial records make the pipeline interruption-proof.",
        "Archiving closes the loop: the solution becomes a findable record.",
    ],
    requirements=[
        "Lay out all six phases with their inputs and outputs",
        "Map each phase to the database records that teach it",
        "Explain the log-as-first-draft and interruption-proof mechanisms",
    ],
    standards=["Systems practice: end-to-end documentation pipelines"],
    citations=[CIT_POLYA, CIT_DEWEY, CIT_SRE],
    sig_lens=(
        "The Signature lens calls the full system the grand "
        "procession: from the blank page sworn as the charge, "
        "through the mustered tools, the witnessed march, the "
        "sealed answer, to the archive where the record takes its "
        "place among the others. His craft runs the whole "
        "procession every time, no phase skipped, no witness "
        "dismissed - the Signature system is the oath kept from "
        "first word to final shelf. Clearly labeled Signature-made, "
        "never presented as authentic public record."),
),
]


