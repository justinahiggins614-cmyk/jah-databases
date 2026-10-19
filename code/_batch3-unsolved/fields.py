#!/usr/bin/env python3
"""Field configuration table for unsolved batch 3 (15 fields).
Prefixes verified free against data/manifest.json id_prefix values (exact + substring), 2026-10-17.
"""

FIELDS = [
 dict(slug="unsolved-surgery", short="surgery",
      name_pub="The Unsolved Surgery Database", name_sig="The Unsolved Surgery Signature Database",
      prefix_pub="JAH-USSU-", prefix_sig="JAH-USSUS-",
      tagline_pub=("Thirty-four of surgery's greatest unsolved problems - preventing anastomotic leaks, "
       "scarless healing, nerve regeneration, organ preservation, real-time tumor margins - each a fact-checked "
       "public record, each explored through a labeled Signature-generated proposed solution, taught in ladder "
       "order from the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science, never medical advice."),
      search_ph="Search anastomotic leak, adhesions, nerve regeneration, organ preservation, tumor margins, surgical site infection...",
      chat_ph="Ask about unsolved surgery...",
      greet_pub=("I am the JAH Unsolved Surgery Archivist. Ask me about the great unsolved problems of surgery - from "
       "anastomotic leaks, adhesions, and wound healing through nerve regeneration, organ preservation, and tumor "
       "margins - each with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in surgery (standard references: Sabiston Textbook of Surgery; Schwartz's Principles of "
       "Surgery; Cochrane systematic reviews; landmark trials cited per record).")),
 dict(slug="unsolved-nursing", short="nursing",
      name_pub="The Unsolved Nursing Database", name_sig="The Unsolved Nursing Signature Database",
      prefix_pub="JAH-USNU-", prefix_sig="JAH-USNUS-",
      tagline_pub=("Thirty-four of nursing science's greatest unsolved problems - predicting patient deterioration, "
       "pressure injury prevention, alarm fatigue, nurse burnout, failure to rescue - each a fact-checked public "
       "record, each explored through a labeled Signature-generated proposed solution, taught in ladder order from "
       "the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science, never clinical advice."),
      search_ph="Search failure to rescue, alarm fatigue, pressure injury, nurse burnout, staffing ratios, handoffs...",
      chat_ph="Ask about unsolved nursing...",
      greet_pub=("I am the JAH Unsolved Nursing Archivist. Ask me about the great unsolved problems of nursing science - from "
       "patient deterioration, pressure injuries, and alarm fatigue through burnout, staffing, and rescue - each with what "
       "is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in nursing science (standard references: Agency for Healthcare Research and Quality; "
       "American Nurses Association; Cochrane systematic reviews; landmark studies cited per record).")),
 dict(slug="unsolved-dentistry", short="dentistry",
      name_pub="The Unsolved Dentistry Database", name_sig="The Unsolved Dentistry Signature Database",
      prefix_pub="JAH-USDE-", prefix_sig="JAH-USDES-",
      tagline_pub=("Thirty-four of dentistry's greatest unsolved problems - stopping caries completely, regenerating "
       "periodontal tissue, whole-tooth regeneration, peri-implantitis, TMD etiology - each a fact-checked public "
       "record, each explored through a labeled Signature-generated proposed solution, taught in ladder order from "
       "the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science, never dental advice."),
      search_ph="Search dental caries, periodontal regeneration, tooth regeneration, peri-implantitis, TMD, pulp...",
      chat_ph="Ask about unsolved dentistry...",
      greet_pub=("I am the JAH Unsolved Dentistry Archivist. Ask me about the great unsolved problems of dentistry - from "
       "caries, periodontal disease, and pulp regeneration through whole-tooth regeneration and peri-implantitis - each "
       "with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in dentistry (standard references: Journal of Dental Research; American Dental "
       "Association; Cochrane Oral Health reviews; landmark studies cited per record).")),
 dict(slug="unsolved-veterinary-medicine", short="veterinary medicine",
      name_pub="The Unsolved Veterinary Medicine Database", name_sig="The Unsolved Veterinary Medicine Signature Database",
      prefix_pub="JAH-USVM-", prefix_sig="JAH-USVMS-",
      tagline_pub=("Thirty-four of veterinary medicine's greatest unsolved problems - feline kidney disease, equine "
       "laminitis, African swine fever, zoonotic spillover prediction, wildlife disease - each a fact-checked public "
       "record, each explored through a labeled Signature-generated proposed solution, taught in ladder order from "
       "the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science, never veterinary advice."),
      search_ph="Search feline kidney disease, laminitis, African swine fever, zoonotic spillover, mastitis, colic...",
      chat_ph="Ask about unsolved veterinary medicine...",
      greet_pub=("I am the JAH Unsolved Veterinary Medicine Archivist. Ask me about the great unsolved problems of "
       "veterinary medicine - from feline kidney disease, laminitis, and mastitis through spillover prediction and "
       "wildlife disease - each with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in veterinary medicine (standard references: Journal of the American Veterinary Medical "
       "Association; OIE/World Organisation for Animal Health; landmark studies cited per record).")),
 dict(slug="unsolved-psychiatry", short="psychiatry",
      name_pub="The Unsolved Psychiatry Database", name_sig="The Unsolved Psychiatry Signature Database",
      prefix_pub="JAH-USPY-", prefix_sig="JAH-USPYS-",
      tagline_pub=("Thirty-four of psychiatry's greatest unsolved problems - what causes schizophrenia and depression, "
       "treatment resistance, suicide prediction, valid biomarkers, rapid antidepressants - each a fact-checked public "
       "record, each explored through a labeled Signature-generated proposed solution, taught in ladder order from "
       "the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science, never medical advice."),
      search_ph="Search schizophrenia, treatment-resistant depression, biomarkers, ketamine, suicide prediction...",
      chat_ph="Ask about unsolved psychiatry...",
      greet_pub=("I am the JAH Unsolved Psychiatry Archivist. Ask me about the great unsolved problems of psychiatry - from "
       "schizophrenia, depression, and bipolar disorder through biomarkers, rapid antidepressants, and suicide "
       "prediction - each with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in psychiatry (standard references: American Journal of Psychiatry; JAMA Psychiatry; "
       "NIMH; landmark studies cited per record).")),
 dict(slug="unsolved-nutrition", short="nutrition",
      name_pub="The Unsolved Nutrition Database", name_sig="The Unsolved Nutrition Signature Database",
      prefix_pub="JAH-USNT-", prefix_sig="JAH-USNTS-",
      tagline_pub=("Thirty-four of nutrition science's greatest unsolved problems - why diets work for some and not "
       "others, ultra-processed foods, the microbiome's causal role, personalized nutrition - each a fact-checked "
       "public record, each explored through a labeled Signature-generated proposed solution, taught in ladder order "
       "from the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science, never dietary advice."),
      search_ph="Search ultra-processed foods, microbiome, personalized nutrition, obesity, saturated fat, fiber...",
      chat_ph="Ask about unsolved nutrition...",
      greet_pub=("I am the JAH Unsolved Nutrition Archivist. Ask me about the great unsolved problems of nutrition - from "
       "diet variability, ultra-processed foods, and the microbiome through personalized nutrition and obesity - each "
       "with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in nutrition science (standard references: American Journal of Clinical Nutrition; "
       "Cochrane systematic reviews; landmark trials cited per record).")),
 dict(slug="unsolved-radiology", short="radiology",
      name_pub="The Unsolved Radiology Database", name_sig="The Unsolved Radiology Signature Database",
      prefix_pub="JAH-USRA-", prefix_sig="JAH-USRAS-",
      tagline_pub=("Thirty-four of radiology's greatest unsolved problems - overdiagnosis in screening, AI validation, "
       "radiation risk at low doses, incidentalomas, early cancer detection - each a fact-checked public record, each "
       "explored through a labeled Signature-generated proposed solution, taught in ladder order from the approachable "
       "to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science, never medical advice."),
      search_ph="Search overdiagnosis, AI validation, low-dose radiation, incidentalomas, radiomics, contrast safety...",
      chat_ph="Ask about unsolved radiology...",
      greet_pub=("I am the JAH Unsolved Radiology Archivist. Ask me about the great unsolved problems of radiology - from "
       "overdiagnosis, incidentalomas, and radiation risk through AI validation and early cancer detection - each with "
       "what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in radiology (standard references: Radiology; American College of Radiology "
       "appropriateness criteria; landmark studies cited per record).")),
 dict(slug="unsolved-immunology", short="immunology",
      name_pub="The Unsolved Immunology Database", name_sig="The Unsolved Immunology Signature Database",
      prefix_pub="JAH-USIM-", prefix_sig="JAH-USIMS-",
      tagline_pub=("Thirty-four of immunology's greatest unsolved problems - why allergies are rising, autoimmune "
       "triggers, the HIV vaccine challenge, CAR-T for solid tumors, transplant tolerance - each a fact-checked public "
       "record, each explored through a labeled Signature-generated proposed solution, taught in ladder order from "
       "the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science, never medical advice."),
      search_ph="Search allergies, autoimmunity, HIV vaccine, CAR-T, transplant tolerance, trained immunity...",
      chat_ph="Ask about unsolved immunology...",
      greet_pub=("I am the JAH Unsolved Immunology Archivist. Ask me about the great unsolved problems of immunology - from "
       "allergies, autoimmunity, and trained immunity through the HIV vaccine, CAR-T, and transplant tolerance - each "
       "with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in immunology (standard references: Nature Reviews Immunology; Annual Review of "
       "Immunology; landmark studies cited per record).")),
 dict(slug="unsolved-epidemiology", short="epidemiology",
      name_pub="The Unsolved Epidemiology Database", name_sig="The Unsolved Epidemiology Signature Database",
      prefix_pub="JAH-USEP-", prefix_sig="JAH-USEPS-",
      tagline_pub=("Thirty-four of epidemiology's greatest unsolved problems - predicting pandemics, spillover "
       "forecasting, causal inference from observational data, superspreading, eradication's next targets - each a "
       "fact-checked public record, each explored through a labeled Signature-generated proposed solution, taught in "
       "ladder order from the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science, never public-health directives."),
      search_ph="Search pandemic prediction, spillover, causal inference, superspreading, herd immunity, eradication...",
      chat_ph="Ask about unsolved epidemiology...",
      greet_pub=("I am the JAH Unsolved Epidemiology Archivist. Ask me about the great unsolved problems of epidemiology - "
       "from pandemic prediction, spillover, and superspreading through causal inference and eradication - each with "
       "what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in epidemiology (standard references: American Journal of Epidemiology; WHO; landmark "
       "studies cited per record).")),
 dict(slug="unsolved-aerospace-engineering", short="aerospace engineering",
      name_pub="The Unsolved Aerospace Engineering Database", name_sig="The Unsolved Aerospace Engineering Signature Database",
      prefix_pub="JAH-USAE-", prefix_sig="JAH-USAES-",
      tagline_pub=("Thirty-four of aerospace engineering's greatest unsolved problems - the turbulence closure problem, "
       "hypersonic flight, scramjet operation, orbital debris remediation, Mars entry - each a fact-checked public "
       "record, each explored through a labeled Signature-generated proposed solution, taught in ladder order from "
       "the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science."),
      search_ph="Search turbulence closure, scramjet, hypersonics, orbital debris, Mars entry, electric aviation...",
      chat_ph="Ask about unsolved aerospace engineering...",
      greet_pub=("I am the JAH Unsolved Aerospace Engineering Archivist. Ask me about the great unsolved problems of "
       "aerospace engineering - from turbulence, hypersonics, and scramjets through debris remediation and Mars entry - "
       "each with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in aerospace engineering (standard references: AIAA Journal; NASA technical reports; "
       "landmark studies cited per record).")),
 dict(slug="unsolved-biomedical-engineering", short="biomedical engineering",
      name_pub="The Unsolved Biomedical Engineering Database", name_sig="The Unsolved Biomedical Engineering Signature Database",
      prefix_pub="JAH-USBM-", prefix_sig="JAH-USBMS-",
      tagline_pub=("Thirty-four of biomedical engineering's greatest unsolved problems - the foreign body response, "
       "bioartificial organs, chronic neural interfaces, closed-loop artificial pancreas, engineered tissues - each a "
       "fact-checked public record, each explored through a labeled Signature-generated proposed solution, taught in "
       "ladder order from the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science, never medical advice."),
      search_ph="Search foreign body response, bioartificial organs, neural interfaces, artificial pancreas, biosensors...",
      chat_ph="Ask about unsolved biomedical engineering...",
      greet_pub=("I am the JAH Unsolved Biomedical Engineering Archivist. Ask me about the great unsolved problems of "
       "biomedical engineering - from biocompatibility, biofilms, and biosensors through bioartificial organs and neural "
       "interfaces - each with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in biomedical engineering (standard references: Nature Biomedical Engineering; IEEE "
       "Transactions on Biomedical Engineering; landmark studies cited per record).")),
 dict(slug="unsolved-software-engineering", short="software engineering",
      name_pub="The Unsolved Software Engineering Database", name_sig="The Unsolved Software Engineering Signature Database",
      prefix_pub="JAH-USSE-", prefix_sig="JAH-USSES-",
      tagline_pub=("Thirty-four of software engineering's greatest unsolved problems - proving correctness at scale, "
       "the oracle problem, accurate estimation, technical debt measurement, AI-generated code safety - each a "
       "fact-checked public record, each explored through a labeled Signature-generated proposed solution, taught in "
       "ladder order from the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science."),
      search_ph="Search program correctness, oracle problem, estimation, technical debt, formal verification, AI code...",
      chat_ph="Ask about unsolved software engineering...",
      greet_pub=("I am the JAH Unsolved Software Engineering Archivist. Ask me about the great unsolved problems of software "
       "engineering - from correctness proofs, the oracle problem, and estimation through formal verification and AI "
       "code safety - each with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in software engineering (standard references: IEEE Transactions on Software Engineering; "
       "ACM Computing Surveys; landmark studies cited per record).")),
 dict(slug="unsolved-materials-science", short="materials science",
      name_pub="The Unsolved Materials Science Database", name_sig="The Unsolved Materials Science Signature Database",
      prefix_pub="JAH-USMT-", prefix_sig="JAH-USMTS-",
      tagline_pub=("Thirty-four of materials science's greatest unsolved problems - the glass transition, "
       "room-temperature superconductivity, solid-state battery dendrites, corrosion prediction, materials by design - "
       "each a fact-checked public record, each explored through a labeled Signature-generated proposed solution, "
       "taught in ladder order from the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science."),
      search_ph="Search glass transition, room-temperature superconductivity, dendrites, corrosion, high-entropy alloys...",
      chat_ph="Ask about unsolved materials science...",
      greet_pub=("I am the JAH Unsolved Materials Science Archivist. Ask me about the great unsolved problems of materials "
       "science - from the glass transition, superconductivity, and dendrites through corrosion and materials by design - "
       "each with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in materials science (standard references: Nature Materials; MRS Bulletin; landmark "
       "studies cited per record).")),
 dict(slug="unsolved-nanotechnology", short="nanotechnology",
      name_pub="The Unsolved Nanotechnology Database", name_sig="The Unsolved Nanotechnology Signature Database",
      prefix_pub="JAH-USNA-", prefix_sig="JAH-USNAS-",
      tagline_pub=("Thirty-four of nanotechnology's greatest unsolved problems - nanotoxicology prediction, the protein "
       "corona, atomic precision manufacturing, targeted delivery efficiency, molecular assemblers - each a fact-checked "
       "public record, each explored through a labeled Signature-generated proposed solution, taught in ladder order "
       "from the approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science."),
      search_ph="Search nanotoxicology, protein corona, atomic precision, targeted delivery, molecular assemblers...",
      chat_ph="Ask about unsolved nanotechnology...",
      greet_pub=("I am the JAH Unsolved Nanotechnology Archivist. Ask me about the great unsolved problems of "
       "nanotechnology - from nanotoxicology, the protein corona, and targeted delivery through atomic precision "
       "manufacturing - each with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in nanotechnology (standard references: Nature Nanotechnology; ACS Nano; landmark "
       "studies cited per record).")),
 dict(slug="unsolved-robotics", short="robotics",
      name_pub="The Unsolved Robotics Database", name_sig="The Unsolved Robotics Signature Database",
      prefix_pub="JAH-USRO-", prefix_sig="JAH-USROS-",
      tagline_pub=("Thirty-four of robotics' greatest unsolved problems - Moravec's paradox, general grasping, the "
       "sim-to-real gap, human-level dexterity, lifelong learning, safe humanoids - each a fact-checked public record, "
       "each explored through a labeled Signature-generated proposed solution, taught in ladder order from the "
       "approachable to the profound."),
      tagline_sig=("The same thirty-four unsolved problems through the Signature lens: every record carries the full "
       "Signature-generated proposed solution approach - assumptions, reasoning path, proposed mechanism, what would "
       "confirm or kill it, and what it does not claim. Clearly labeled Signature-made proposals, never established "
       "science."),
      search_ph="Search Moravec paradox, grasping, sim-to-real gap, dexterity, lifelong learning, humanoids...",
      chat_ph="Ask about unsolved robotics...",
      greet_pub=("I am the JAH Unsolved Robotics Archivist. Ask me about the great unsolved problems of robotics - from "
       "Moravec's paradox, grasping, and the sim-to-real gap through dexterity, lifelong learning, and safe humanoids - "
       "each with what is known, why it matters, and the Signature system's labeled proposed solution approach."),
      cit=("Unsolved problems in robotics (standard references: Science Robotics; IEEE Transactions on Robotics; "
       "landmark studies cited per record).")),
]
