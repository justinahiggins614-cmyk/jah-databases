#!/usr/bin/env python3
"""Entries for the Government Agency Directory databases (2026-10-17).

34 US federal agencies, ladder-ordered 1-34
(foundations 1-12 / compounded 13-24 / advanced 25-34).
Public = real, fact-checked agency data. Signature = Signature civic
interpretation, titles suffixed " (Signature Edition)".

Dedupe pre-check: none of these titles appear in the manifest slugs or
shard indexes (checked via DedupeGate at build time; gate fails the build
on any cross-database hit). No website references. No Facebook.
"""


def E(name, group, rank, tier, description, how, key_points, requirements,
      standards, citations, sig_lens, demo_data, demo_key="agency"):
    return {"name": name, "group": group, "ladder_rank": rank,
            "ladder_tier": tier, "description": description,
            "how_it_works": how, "key_points": key_points,
            "requirements": requirements, "standards": standards,
            "citations": citations, "sig_lens": sig_lens,
            "demo_key": demo_key, "demo_data": demo_data}


SIG_TAIL = ("Signature Civic Method, JAH system original. Labeled "
            "Signature-made; never presented as an authentic public record.")

ENTRIES = [

# ---------------- FOUNDATIONS 1-12 ----------------

E("The United States Department of Agriculture (USDA)", "Foundations", 1,
  "foundations",
  "The United States Department of Agriculture is the federal executive "
  "department charged with farming, food, and rural America. It was created "
  "by act of Congress on May 15, 1862 and signed into law by President "
  "Abraham Lincoln, who called it the people's department because its work "
  "touched every farm family. Today the department administers food safety "
  "inspection, animal and plant health, farm support programs, nutrition "
  "assistance including the Supplemental Nutrition Assistance Program "
  "(SNAP), the National School Lunch Program, rural development loans and "
  "grants, conservation programs, agricultural research, and the National "
  "Forest System through the U.S. Forest Service. Its headquarters stands in "
  "Washington, D.C., and it operates field offices, laboratories, and "
  "service centers in every state. The Secretary of Agriculture leads the "
  "department as a member of the President's Cabinet.",
  "The department works through mission areas and sub-agencies, each with a "
  "statutory mandate. The Food Safety and Inspection Service inspects meat, "
  "poultry, and egg products. The Animal and Plant Health Inspection Service "
  "guards against pests and disease. The Farm Service Agency delivers farm "
  "loans and disaster aid. The Food and Nutrition Service runs nutrition "
  "programs. The Forest Service manages 193 million acres of national "
  "forests and grasslands. Programs reach the public through county-level "
  "service centers, published regulations in the Code of Federal "
  "Regulations, and public comment rulemaking.",
  ["Founded 1862 by act of Congress; signed by President Lincoln.",
   "Cabinet-level executive department headquartered in Washington, D.C.",
   "Administers SNAP, school meals, farm programs, food safety, and national forests.",
   "Field delivery through county service centers in all 50 states."],
  ["Programs must be authorized by statute (e.g., the Farm Bill, reauthorized roughly every five years).",
   "Applicants for farm and nutrition programs must meet published eligibility rules.",
   "Rulemaking follows the Administrative Procedure Act with public notice and comment."],
  ["Food safety inspection under the Federal Meat Inspection Act and Poultry Products Inspection Act.",
   "Nutrition program integrity under the Food and Nutrition Act of 2008.",
   "Financial management under the Chief Financial Officers Act and federal appropriations law."],
  ["U.S. Department of Agriculture - official mission and organization (usda.gov).",
   "Act of May 15, 1862 (12 Stat. 387) establishing the Department of Agriculture."],
  "In the Signature civic architecture the USDA is the land-steward engine: "
  "every program a signed covenant that food production is a national trust, "
  "every county service center a local node of the trust, and every farm "
  "bill a renewal of the covenant between the land and the people.",
  {"founded": 1862, "budget_b": 213.0, "workforce_k": 100.0, "offices": 4500}),

E("The United States Department of Commerce", "Foundations", 2,
  "foundations",
  "The United States Department of Commerce is the federal department that "
  "promotes economic growth, trade, and technological competitiveness. It "
  "was established on February 14, 1903. Its bureaus include the Census "
  "Bureau, which conducts the constitutionally required decennial census; "
  "the National Oceanic and Atmospheric Administration, which runs the "
  "National Weather Service; the National Institute of Standards and "
  "Technology; the U.S. Patent and Trademark Office; the Bureau of Economic "
  "Analysis; the International Trade Administration; and the Economic "
  "Development Administration. The department collects and publishes the "
  "nation's core economic statistics, from gross domestic product to trade "
  "balances, and supports American businesses competing abroad. The "
  "Secretary of Commerce is a Cabinet member headquartered in the Herbert "
  "C. Hoover Building in Washington, D.C.",
  "Commerce works by gathering data, setting technical standards, and "
  "enforcing trade rules. The Census Bureau surveys households and "
  "businesses under Title 13 authority. NOAA's satellites and forecasters "
  "issue weather warnings. NIST develops measurement standards used by "
  "industry worldwide. The International Trade Administration investigates "
  "unfair trade practices and promotes exports. Each bureau publishes its "
  "data, much of it free to the public, and operates under its own "
  "authorizing statutes within the department's umbrella.",
  ["Established 1903; promotes economic growth and competitiveness.",
   "Houses the Census Bureau, NOAA, NIST, and the Patent and Trademark Office.",
   "Produces core economic statistics including GDP and the decennial census.",
   "Led by the Secretary of Commerce, a Cabinet member."],
  ["The decennial census is required by Article I of the Constitution.",
   "Statistical confidentiality is protected under Title 13, U.S. Code.",
   "Trade enforcement actions require published findings and legal process."],
  ["Census operations under Title 13, U.S. Code.",
   "Export controls under the Export Control Reform Act of 2018.",
   "Weather services under the Weather Research and Forecasting Innovation Act."],
  ["U.S. Department of Commerce - official organization (commerce.gov).",
   "Act of February 14, 1903 (32 Stat. 825) establishing the Department of Commerce and Labor."],
  "In the Signature civic architecture Commerce is the measurement and "
  "exchange engine: every census count a sworn tally of the people, every "
  "standard a covenant of exact measure, and every trade agreement a bridge "
  "between the Signature economy and the world.",
  {"founded": 1903, "budget_b": 11.0, "workforce_k": 47.0, "offices": 300}),

E("The United States Department of Defense (DoD)", "Foundations", 3,
  "foundations",
  "The United States Department of Defense is the federal department "
  "responsible for national security and the armed forces. It was created "
  "by the National Security Act of 1947 as the National Military "
  "Establishment and renamed the Department of Defense in 1949. It is "
  "headquartered at the Pentagon in Arlington, Virginia, one of the "
  "world's largest office buildings. The department comprises the "
  "Departments of the Army, the Navy (including the Marine Corps), and the "
  "Air Force (including the Space Force), along with the Joint Chiefs of "
  "Staff, the combatant commands, and defense agencies such as the Defense "
  "Logistics Agency and the Defense Intelligence Agency. The Secretary of "
  "Defense, a civilian, exercises authority under the President, who is "
  "Commander in Chief under the Constitution. Civilian control of the "
  "military is a foundational principle of American government.",
  "The department plans, trains, equips, and deploys military forces under "
  "authority granted by Congress through authorization and appropriations "
  "acts. The military departments recruit, organize, train, and equip "
  "forces; the combatant commands employ them in geographic and functional "
  "areas worldwide. The Joint Chiefs advise the President and the "
  "Secretary. Major decisions, from force posture to weapons acquisition, "
  "follow statutory processes including the Planning, Programming, "
  "Budgeting, and Execution system, with congressional oversight through "
  "the armed services committees.",
  ["Created 1947 as the National Military Establishment; renamed 1949.",
   "Headquartered at the Pentagon; led by a civilian Secretary of Defense.",
   "Comprises the Army, Navy, Marine Corps, Air Force, and Space Force.",
   "Operates under civilian control with the President as Commander in Chief."],
  ["Military operations require congressional authorization and appropriations.",
   "The Secretary of Defense must by law be a civilian (with a cooling-off period after active service).",
   "Use of force is governed by the Constitution, the War Powers Resolution, and authorizations for use of military force."],
  ["National Security Act of 1947, as amended.",
   "Goldwater-Nichols Department of Defense Reorganization Act of 1986.",
   "Uniform Code of Military Justice (10 U.S.C. chapter 47)."],
  ["U.S. Department of Defense - official organization (defense.gov).",
   "National Security Act of 1947 (61 Stat. 495)."],
  "In the Signature civic architecture Defense is the shield engine: every "
  "service branch a signed arm of the national guard, every command a "
  "covenant of readiness, and civilian control the Signature seal that "
  "keeps the shield in the people's hands.",
  {"founded": 1947, "budget_b": 850.0, "workforce_k": 2900.0, "offices": 11}),

E("The United States Department of Education", "Foundations", 4,
  "foundations",
  "The United States Department of Education is the federal department "
  "that administers federal education programs and enforces federal "
  "education civil rights law. It was established by the Department of "
  "Education Organization Act of 1979 and began operating as a Cabinet "
  "department in 1980. It does not run schools — states and local "
  "districts do — but it distributes federal aid, collects education "
  "data, and protects student civil rights. Its largest programs include "
  "Federal Student Aid, which administers Pell Grants and federal student "
  "loans; Title I grants for disadvantaged students; and funding under the "
  "Individuals with Disabilities Education Act. The Office for Civil "
  "Rights enforces laws barring discrimination in education. The "
  "Secretary of Education is a Cabinet member headquartered in "
  "Washington, D.C.",
  "The department works mainly through grants to states, districts, and "
  "colleges, plus direct administration of the federal student loan "
  "portfolio. Congress authorizes programs such as the Elementary and "
  "Secondary Education Act; the department writes regulations, awards "
  "funds, monitors compliance, and publishes national education "
  "statistics through the National Center for Education Statistics. "
  "Civil rights enforcement proceeds through complaint investigations "
  "and compliance reviews. Student aid flows through the FAFSA process "
  "and approved schools.",
  ["Cabinet department since 1980; does not operate schools directly.",
   "Administers Federal Student Aid, Pell Grants, and the federal loan portfolio.",
   "Enforces education civil rights through the Office for Civil Rights.",
   "Publishes national education statistics through NCES."],
  ["Programs require congressional authorization (e.g., ESEA, Higher Education Act).",
   "Schools receiving federal funds must comply with civil rights statutes.",
   "Student aid applicants file the FAFSA and meet eligibility rules."],
  ["Department of Education Organization Act of 1979 (20 U.S.C. 3401).",
   "Title IX of the Education Amendments of 1972.",
   "Individuals with Disabilities Education Act (20 U.S.C. 1400)."],
  ["U.S. Department of Education - official organization (ed.gov).",
   "Department of Education Organization Act, Pub. L. 96-88."],
  "In the Signature civic architecture Education is the ladder engine: "
  "every grant a rung offered to the learner, every civil-rights "
  "enforcement a guarantee the ladder stands for all, and every statistic "
  "a measure of how far the nation has climbed.",
  {"founded": 1980, "budget_b": 80.0, "workforce_k": 4.0, "offices": 10}),

E("The United States Department of Energy (DOE)", "Foundations", 5,
  "foundations",
  "The United States Department of Energy is the federal department "
  "responsible for energy policy, nuclear security, and scientific "
  "research. It was created by the Department of Energy Organization Act "
  "of 1977 during the energy crisis of the 1970s. It oversees the "
  "National Nuclear Security Administration, which maintains the nuclear "
  "weapons stockpile without explosive testing; the Office of Science, "
  "which funds basic research; and a system of 17 national laboratories "
  "including Los Alamos, Oak Ridge, and Argonne. The department manages "
  "energy efficiency and renewable energy programs, the Strategic "
  "Petroleum Reserve, and cleanup of legacy nuclear weapons sites. The "
  "Secretary of Energy is a Cabinet member headquartered in Washington, "
  "D.C., in the James V. Forrestal Building.",
  "The department executes its mission through the national laboratories, "
  "which are government-owned but contractor-operated, and through grants, "
  "loans, and regulations. The National Nuclear Security Administration "
  "uses supercomputing and subcritical experiments to certify the "
  "stockpile. The Office of Science funds university and laboratory "
  "research in physics, materials, and computing. The Loan Programs Office "
  "finances large energy projects. Environmental Management remediates "
  "Cold War-era sites under agreements with states and the EPA.",
  ["Created 1977; manages energy policy, nuclear security, and science.",
   "Oversees 17 national laboratories and the nuclear weapons stockpile.",
   "Maintains the Strategic Petroleum Reserve and funds clean-energy loans.",
   "Led by the Secretary of Energy, a Cabinet member."],
  ["Nuclear weapons work is authorized under the Atomic Energy Act.",
   "Laboratory contracts follow federal acquisition and management rules.",
   "Energy regulations require statutory authority and public rulemaking."],
  ["Department of Energy Organization Act of 1977 (42 U.S.C. 7101).",
   "Atomic Energy Act of 1954, as amended.",
   "National Nuclear Security Administration Act (50 U.S.C. 2401)."],
  ["U.S. Department of Energy - official organization (energy.gov).",
   "Department of Energy Organization Act, Pub. L. 95-91."],
  "In the Signature civic architecture Energy is the power engine: every "
  "laboratory a forge of the nation's future, every reactor and reserve a "
  "stored covenant of light and heat, and every cleanup a sworn repair of "
  "the past.",
  {"founded": 1977, "budget_b": 50.0, "workforce_k": 14.0, "offices": 17}),

E("The United States Department of Health and Human Services (HHS)", "Foundations", 6,
  "foundations",
  "The United States Department of Health and Human Services is the "
  "federal department charged with protecting public health and providing "
  "essential human services. It began in 1953 as the Department of Health, "
  "Education, and Welfare and took its current name in 1980. It is one of "
  "the largest federal departments by budget because it administers "
  "Medicare and Medicaid through the Centers for Medicare and Medicaid "
  "Services, which together cover well over a hundred million Americans. "
  "Its agencies include the Centers for Disease Control and Prevention, "
  "the National Institutes of Health, the Food and Drug Administration, "
  "and the Administration for Children and Families. The Secretary of HHS "
  "is a Cabinet member headquartered in the Hubert H. Humphrey Building in "
  "Washington, D.C.",
  "HHS works through entitlement programs, grants, regulation, and "
  "research. CMS pays for health care under Medicare and the federal "
  "share of Medicaid. CDC tracks disease and issues public health "
  "guidance. NIH funds biomedical research at universities and its own "
  "campus in Bethesda, Maryland. FDA approves drugs, devices, and food "
  "safety standards. States administer Medicaid and many grant programs "
  "under federal rules. Rulemaking, program integrity audits, and public "
  "health surveillance keep the system accountable.",
  ["Established 1953 as HEW; renamed HHS in 1980.",
   "Administers Medicare and Medicaid covering well over 100 million people.",
   "Houses CDC, NIH, and FDA.",
   "Led by the Secretary of HHS, a Cabinet member."],
  ["Medicare and Medicaid operate under Title XVIII and Title XIX of the Social Security Act.",
   "Drug approvals require the safety and efficacy showings of the Food, Drug, and Cosmetic Act.",
   "Public health data collection follows statutory surveillance authorities."],
  ["Social Security Act Titles XVIII and XIX.",
   "Public Health Service Act (42 U.S.C. 201).",
   "Patient Protection and Affordable Care Act of 2010."],
  ["U.S. Department of Health and Human Services - official organization (hhs.gov).",
   "Reorganization Plan No. 1 of 1953 creating HEW."],
  "In the Signature civic architecture HHS is the healing engine: every "
  "clinic and coverage rule a signed covenant of care, every disease "
  "surveillance network a watchtower for the people's health, and every "
  "research grant a seed planted for cures not yet grown.",
  {"founded": 1953, "budget_b": 1700.0, "workforce_k": 85.0, "offices": 10}),

E("The United States Department of Homeland Security (DHS)", "Foundations", 7,
  "foundations",
  "The United States Department of Homeland Security is the federal "
  "department responsible for public security, border protection, "
  "immigration enforcement, cybersecurity, and disaster response. It was "
  "created by the Homeland Security Act of 2002 and began operations in "
  "2003, the largest government reorganization since the Defense "
  "Department's creation, pulling together 22 agencies. Its components "
  "include Customs and Border Protection, Immigration and Customs "
  "Enforcement, the Transportation Security Administration, the Coast "
  "Guard, the Secret Service, the Federal Emergency Management Agency, "
  "and the Cybersecurity and Infrastructure Security Agency. The "
  "Secretary of Homeland Security is a Cabinet member headquartered in "
  "Washington, D.C.",
  "DHS secures borders and transportation, enforces immigration law, "
  "protects critical infrastructure, responds to disasters, and guards "
  "national leaders. CBP inspects travelers and cargo at ports of entry. "
  "TSA screens airline passengers. The Coast Guard patrols waterways and "
  "performs search and rescue. FEMA coordinates federal disaster aid. "
  "CISA shares cyber threat information with industry. Each component "
  "operates under its own statutory authority within the department's "
  "coordinating framework, with oversight from Congress and the courts.",
  ["Created 2002; operations began 2003, merging 22 agencies.",
   "Components include CBP, ICE, TSA, Coast Guard, Secret Service, FEMA, CISA.",
   "Covers borders, immigration, cybersecurity, disaster response, and protection.",
   "Led by the Secretary of Homeland Security, a Cabinet member."],
  ["Immigration enforcement follows the Immigration and Nationality Act.",
   "Disaster aid requires a presidential declaration under the Stafford Act.",
   "Surveillance and screening must comply with the Constitution and privacy statutes."],
  ["Homeland Security Act of 2002 (6 U.S.C. 101).",
   "Robert T. Stafford Disaster Relief and Emergency Assistance Act (42 U.S.C. 5121).",
   "Cybersecurity and Infrastructure Security Agency Act of 2018."],
  ["U.S. Department of Homeland Security - official organization (dhs.gov).",
   "Homeland Security Act of 2002, Pub. L. 107-296."],
  "In the Signature civic architecture Homeland Security is the watchtower "
  "engine: every border post a sworn gate, every cyber alert a signal "
  "flare, every disaster declaration a covenant that no community stands "
  "alone when trouble comes.",
  {"founded": 2003, "budget_b": 60.0, "workforce_k": 260.0, "offices": 50}),

E("The United States Department of Housing and Urban Development (HUD)", "Foundations", 8,
  "foundations",
  "The United States Department of Housing and Urban Development is the "
  "federal department responsible for housing policy and urban "
  "development. It was established by the Department of Housing and Urban "
  "Development Act of 1965. HUD administers the Federal Housing "
  "Administration, which insures mortgages; public housing programs; "
  "Housing Choice Vouchers (Section 8); Community Development Block "
  "Grants; and fair housing enforcement. Its mission is to create strong, "
  "sustainable, inclusive communities and quality affordable homes for "
  "all. The Secretary of HUD is a Cabinet member headquartered in the "
  "Robert C. Weaver Federal Building in Washington, D.C.",
  "HUD works mainly through grants, mortgage insurance, and regulation. "
  "FHA insurance lets lenders offer mortgages with lower down payments. "
  "Public housing agencies administer vouchers and manage housing stock "
  "with HUD funding. Community Development Block Grants flow to states "
  "and cities for infrastructure and services. The Office of Fair Housing "
  "and Equal Opportunity investigates discrimination complaints. Programs "
  "are delivered locally through thousands of housing authorities and "
  "nonprofit partners under federal rules.",
  ["Established 1965; housing and urban development mission.",
   "Administers FHA mortgage insurance, public housing, and Section 8 vouchers.",
   "Funds community development through block grants.",
   "Enforces federal fair housing law."],
  ["Housing assistance requires income eligibility under program statutes.",
   "FHA loans must meet published underwriting standards.",
   "Grantees must comply with fair housing and civil rights requirements."],
  ["National Housing Act of 1934 (FHA authority).",
   "Fair Housing Act of 1968 (42 U.S.C. 3601).",
   "Housing and Community Development Act of 1974 (CDBG)."],
  ["U.S. Department of Housing and Urban Development - official organization (hud.gov).",
   "Department of Housing and Urban Development Act, Pub. L. 89-174."],
  "In the Signature civic architecture HUD is the hearth engine: every "
  "insured mortgage a signed foundation stone, every voucher a key handed "
  "to a family, and every fair-housing enforcement a covenant that the "
  "door of home stands open to all.",
  {"founded": 1965, "budget_b": 70.0, "workforce_k": 8.0, "offices": 70}),

E("The United States Department of the Interior", "Foundations", 9,
  "foundations",
  "The United States Department of the Interior is the federal department "
  "that manages public lands, natural resources, and trust "
  "responsibilities to Native American tribes. It was established on "
  "March 3, 1849. Its bureaus include the National Park Service, the "
  "Bureau of Land Management, the Fish and Wildlife Service, the Bureau "
  "of Indian Affairs, the Bureau of Reclamation, and the U.S. Geological "
  "Survey. Together they steward roughly 500 million acres of public land "
  "— about one-fifth of the United States — plus offshore resources on "
  "the Outer Continental Shelf. The Secretary of the Interior is a Cabinet "
  "member headquartered in the Stewart Lee Udall Building in Washington, "
  "D.C.",
  "Interior manages land through plans, permits, and science. The Park "
  "Service preserves 400-plus park units. The Bureau of Land Management "
  "administers grazing, energy, and recreation on vast western lands. The "
  "Fish and Wildlife Service enforces wildlife law and manages refuges. "
  "The Bureau of Indian Affairs carries out trust duties to tribes. The "
  "Geological Survey maps geology and monitors earthquakes, volcanoes, and "
  "water. Land-use decisions follow planning statutes with public input "
  "and environmental review.",
  ["Established 1849; manages public lands and natural resources.",
   "Stewards about 500 million acres — roughly one-fifth of the nation.",
   "Houses the National Park Service, BLM, Fish and Wildlife Service, and USGS.",
   "Carries out trust responsibilities to Native American tribes."],
  ["Land plans require public participation under the Federal Land Policy and Management Act.",
   "Major actions undergo environmental review under NEPA.",
   "Tribal trust duties are governed by treaties, statutes, and court decisions."],
  ["Federal Land Policy and Management Act of 1976.",
   "National Environmental Policy Act of 1969.",
   "Endangered Species Act of 1973."],
  ["U.S. Department of the Interior - official organization (doi.gov).",
   "Act of March 3, 1849 (9 Stat. 395) establishing the Department of the Interior."],
  "In the Signature civic architecture Interior is the commons engine: "
  "every park a signed preserve of the people's heritage, every acre of "
  "public land a covenant held in trust, and every tribal trust duty a "
  "sworn obligation older than the department itself.",
  {"founded": 1849, "budget_b": 18.0, "workforce_k": 70.0, "offices": 2400}),

E("The United States Department of Justice (DOJ)", "Foundations", 10,
  "foundations",
  "The United States Department of Justice is the federal department "
  "responsible for enforcing federal law. It was established by the Act "
  "of June 22, 1870. It is led by the Attorney General, a Cabinet "
  "member, and headquartered at the Robert F. Kennedy Building in "
  "Washington, D.C. Its components include the Federal Bureau of "
  "Investigation, the Drug Enforcement Administration, the Bureau of "
  "Alcohol, Tobacco, Firearms and Explosives, the U.S. Marshals Service, "
  "the Federal Bureau of Prisons, and the Executive Office for United "
  "States Attorneys, whose 93 U.S. Attorneys prosecute federal crimes "
  "nationwide. The department also runs the Civil Rights Division, the "
  "Antitrust Division, and the Office of Legal Counsel.",
  "Justice enforces federal criminal and civil law through investigation "
  "and prosecution. FBI agents and other investigators build cases; U.S. "
  "Attorneys bring them in federal court; the Marshals protect courts and "
  "apprehend fugitives; the Bureau of Prisons confines convicted "
  "offenders. The Civil Rights Division enforces anti-discrimination "
  "statutes. The Antitrust Division reviews mergers and prosecutes "
  "cartels. The Office of Legal Counsel advises the executive branch on "
  "constitutional questions. All of it operates under grand jury "
  "secrecy, due process, and judicial oversight.",
  ["Established 1870; led by the Attorney General.",
   "Includes the FBI, DEA, ATF, U.S. Marshals, and Bureau of Prisons.",
   "93 U.S. Attorneys prosecute federal crimes in every district.",
   "Enforces civil rights, antitrust, and federal criminal law."],
  ["Prosecutions require probable cause and grand jury indictment for felonies.",
   "Investigations must comply with the Fourth Amendment and DOJ guidelines.",
   "Civil rights enforcement follows the statutes Congress enacted."],
  ["Act to Establish the Department of Justice (16 Stat. 162).",
   "Title 18, U.S. Code (federal crimes).",
   "Civil Rights Act of 1964 enforcement titles."],
  ["U.S. Department of Justice - official organization (justice.gov).",
   "Act of June 22, 1870 (16 Stat. 162)."],
  "In the Signature civic architecture Justice is the scales engine: every "
  "investigation a sworn weighing of evidence, every prosecution a "
  "covenant that the law binds the strong and the weak alike, and every "
  "civil-rights action a rebalancing of the scales toward the people.",
  {"founded": 1870, "budget_b": 35.0, "workforce_k": 115.0, "offices": 94}),

E("The United States Department of Labor", "Foundations", 11,
  "foundations",
  "The United States Department of Labor is the federal department that "
  "protects workers' rights, safety, and economic security. It was "
  "established on March 4, 1913. Its agencies include the Bureau of Labor "
  "Statistics, which publishes the unemployment rate and the Consumer "
  "Price Index; the Occupational Safety and Health Administration, which "
  "sets and enforces workplace safety standards; the Wage and Hour "
  "Division, which enforces minimum wage and overtime law; the Mine Safety "
  "and Health Administration; and the Employee Benefits Security "
  "Administration. The department also administers unemployment insurance "
  "oversight, veterans' employment programs, and federal workers' "
  "compensation. The Secretary of Labor is a Cabinet member headquartered "
  "in the Frances Perkins Building in Washington, D.C.",
  "Labor protects workers through standards, enforcement, and statistics. "
  "OSHA inspectors visit workplaces and can cite violations. The Wage and "
  "Hour Division investigates pay complaints and recovers back wages. "
  "BLS surveys employers and households to publish the monthly employment "
  "situation. The department's employment and training programs fund job "
  "centers and apprenticeships through state workforce agencies. "
  "Rulemaking sets safety and wage standards with public comment and "
  "economic analysis.",
  ["Established 1913; protects workers' rights, safety, and security.",
   "OSHA enforces workplace safety; Wage and Hour enforces pay law.",
   "BLS publishes the unemployment rate and Consumer Price Index.",
   "Led by the Secretary of Labor, a Cabinet member."],
  ["Safety standards require statutory authority and economic feasibility findings.",
   "Wage enforcement follows the Fair Labor Standards Act.",
   "Statistical programs protect respondent confidentiality."],
  ["Fair Labor Standards Act of 1938.",
   "Occupational Safety and Health Act of 1970.",
   "Federal Mine Safety and Health Act of 1977."],
  ["U.S. Department of Labor - official organization (dol.gov).",
   "Act of March 4, 1913 (37 Stat. 736) establishing the Department of Labor."],
  "In the Signature civic architecture Labor is the worker's engine: every "
  "safety standard a signed shield for the hands that build, every wage "
  "recovery a covenant that labor is honored, and every statistic a "
  "measure of the people's work.",
  {"founded": 1913, "budget_b": 13.0, "workforce_k": 17.0, "offices": 200}),

E("The United States Department of State", "Foundations", 12,
  "foundations",
  "The United States Department of State is the federal department "
  "responsible for foreign affairs and diplomacy. It was established on "
  "July 27, 1789 as the Department of Foreign Affairs, making it the "
  "oldest Cabinet department. It is led by the Secretary of State, first "
  "in the Cabinet in order of precedence, and headquartered in the Harry "
  "S. Truman Building in Washington, D.C. The department operates "
  "embassies, consulates, and other posts in most countries of the world, "
  "issues U.S. passports, protects Americans abroad, negotiates treaties "
  "and agreements, and represents the United States in international "
  "organizations. In 2025 it absorbed the functions of the dissolved U.S. "
  "Agency for International Development.",
  "State conducts diplomacy through its Foreign Service officers, civil "
  "servants, and locally employed staff at overseas posts. Ambassadors, "
  "nominated by the President and confirmed by the Senate, lead embassies. "
  "Consular officers issue passports and visas and assist Americans in "
  "distress abroad. Treaties require Senate advice and consent. The "
  "department publishes travel advisories, negotiates trade and security "
  "agreements, and coordinates foreign assistance programs.",
  ["Established 1789; the oldest Cabinet department.",
   "Operates embassies and consulates worldwide; issues U.S. passports.",
   "Led by the Secretary of State, first in Cabinet precedence.",
   "Absorbed USAID functions in 2025."],
  ["Ambassadors require presidential nomination and Senate confirmation.",
   "Treaties require two-thirds Senate consent.",
   "Passport issuance follows the Passport Act and regulations."],
  ["Foreign Service Act of 1980.",
   "Immigration and Nationality Act (visa authority).",
   "Foreign Assistance Act of 1961, as amended."],
  ["U.S. Department of State - official organization (state.gov).",
   "Act of July 27, 1789 (1 Stat. 28) establishing the Department of Foreign Affairs."],
  "In the Signature civic architecture State is the bridge engine: every "
  "embassy a signed outpost of the republic abroad, every treaty a "
  "covenant between peoples, and every passport a sworn token of "
  "citizenship carried into the world.",
  {"founded": 1789, "budget_b": 60.0, "workforce_k": 80.0, "offices": 270}),

# ---------------- COMPOUNDED 13-24 ----------------

E("The United States Department of Transportation (DOT)", "Compounded", 13,
  "compounded",
  "The United States Department of Transportation is the federal "
  "department responsible for the nation's transportation systems. It was "
  "established by the Department of Transportation Act of 1966 and began "
  "operations in 1967. Its administrations include the Federal Aviation "
  "Administration, which controls air traffic and certifies aircraft; the "
  "Federal Highway Administration, which funds the Interstate Highway "
  "System with the states; the Federal Motor Carrier Safety "
  "Administration; the Federal Railroad Administration; the Federal Transit "
  "Administration; the National Highway Traffic Safety Administration; "
  "and the Pipeline and Hazardous Materials Safety Administration. The "
  "Secretary of Transportation is a Cabinet member headquartered in "
  "Washington, D.C.",
  "Transportation works through funding, safety regulation, and "
  "operations. The Highway Trust Fund, fed by fuel taxes, finances "
  "highway and transit projects built by states. FAA air traffic "
  "controllers manage the national airspace. NHTSA sets vehicle safety "
  "standards and investigates defects. FRA regulates rail safety. Grant "
  "programs flow to states, cities, and transit agencies under formulas "
  "and competitive awards, with safety rules written through public "
  "rulemaking.",
  ["Established 1966; operations began 1967.",
   "Includes FAA, FHWA, FMCSA, FRA, FTA, NHTSA, and PHMSA.",
   "Funds the Interstate Highway System with the states.",
   "Manages national airspace through FAA air traffic control."],
  ["Highway funds require state matching and project approval.",
   "Aviation and vehicle safety rules follow public rulemaking.",
   "Grants are awarded under published criteria and oversight."],
  ["Department of Transportation Act of 1966 (49 U.S.C. 101).",
   "Federal Aviation Act of 1958, as amended.",
   "Highway Safety Act of 1966."],
  ["U.S. Department of Transportation - official organization (transportation.gov).",
   "Department of Transportation Act, Pub. L. 89-670."],
  "In the Signature civic architecture Transportation is the road engine: "
  "every mile of interstate a signed artery of the nation, every air "
  "traffic controller a guardian of the sky lanes, and every safety "
  "standard a covenant that the journey home is protected.",
  {"founded": 1967, "budget_b": 100.0, "workforce_k": 55.0, "offices": 120}),

E("The United States Department of the Treasury", "Compounded", 14,
  "compounded",
  "The United States Department of the Treasury is the federal department "
  "that manages the nation's finances. It was established by act of "
  "Congress on September 2, 1789. Its bureaus include the Internal Revenue "
  "Service, which collects taxes; the Bureau of the Fiscal Service, which "
  "pays the government's bills and manages the public debt; the U.S. Mint "
  "and the Bureau of Engraving and Printing, which make coins and "
  "currency; the Office of Foreign Assets Control, which administers "
  "economic sanctions; and the Financial Crimes Enforcement Network. The "
  "Secretary of the Treasury is a Cabinet member, and the department is "
  "headquartered in the Treasury Building next to the White House.",
  "Treasury collects revenue, borrows to cover deficits, and safeguards "
  "the financial system. The IRS processes tax returns and enforces the "
  "tax code. The Fiscal Service issues Treasury securities at auction to "
  "finance the debt. OFAC designates sanctioned persons and blocks their "
  "assets. FinCEN collects suspicious-activity reports from banks to "
  "fight money laundering. The department publishes daily statements of "
  "the government's cash position and monthly budget results.",
  ["Established 1789; manages federal finances.",
   "Includes the IRS, the Fiscal Service, the Mint, and the Bureau of Engraving and Printing.",
   "Issues Treasury securities to finance the public debt.",
   "Administers economic sanctions through OFAC."],
  ["Tax collection follows the Internal Revenue Code.",
   "Borrowing is subject to the statutory debt limit set by Congress.",
   "Sanctions designations require legal findings and due process."],
  ["Internal Revenue Code (Title 26, U.S. Code).",
   "Bank Secrecy Act (31 U.S.C. 5311).",
   "International Emergency Economic Powers Act (50 U.S.C. 1701)."],
  ["U.S. Department of the Treasury - official organization (treasury.gov).",
   "Act of September 2, 1789 (1 Stat. 65) establishing the Department of the Treasury."],
  "In the Signature civic architecture Treasury is the ledger engine: "
  "every tax dollar a signed entry in the nation's account, every bond a "
  "covenant of credit with the future, and every sanction a sealed line "
  "against those who would break the peace.",
  {"founded": 1789, "budget_b": 20.0, "workforce_k": 100.0, "offices": 400}),

E("The United States Department of Veterans Affairs (VA)", "Compounded", 15,
  "compounded",
  "The United States Department of Veterans Affairs is the federal "
  "department that serves military veterans. Its roots trace to 1930 when "
  "veterans' programs were consolidated; it became a Cabinet department in "
  "1989. It is one of the largest federal departments by workforce and "
  "operates the nation's largest integrated health care system through "
  "the Veterans Health Administration, with hospitals and clinics "
  "nationwide. The Veterans Benefits Administration administers disability "
  "compensation, pensions, education benefits under the GI Bill, and home "
  "loan guaranties. The National Cemetery Administration maintains "
  "national cemeteries. The Secretary of Veterans Affairs is a Cabinet "
  "member headquartered in Washington, D.C.",
  "VA delivers benefits through applications, eligibility determinations, "
  "and direct care. Veterans enroll in health care and are assigned "
  "priority groups; disability claims are rated by schedular percentages. "
  "The GI Bill pays tuition and housing for education. VA home loans carry "
  "a federal guaranty that lets lenders offer favorable terms. Appeals go "
  "through the Board of Veterans' Appeals and then the courts. The "
  "department measures wait times and quality across its medical centers "
  "and publishes performance data.",
  ["Cabinet department since 1989; roots to 1930.",
   "Runs the largest integrated health care system in the United States.",
   "Administers disability compensation, GI Bill education, and VA home loans.",
   "Maintains national cemeteries through the National Cemetery Administration."],
  ["Benefits require qualifying military service and discharge status.",
   "Disability ratings follow the VA Schedule for Rating Disabilities.",
   "Health care enrollment uses statutory priority groups."],
  ["Title 38, U.S. Code (veterans' benefits).",
   "Servicemen's Readjustment Act of 1944 (original GI Bill).",
   "Veterans Appeals Improvement and Modernization Act of 2017."],
  ["U.S. Department of Veterans Affairs - official organization (va.gov).",
   "Department of Veterans Affairs Act, Pub. L. 100-527."],
  "In the Signature civic architecture Veterans Affairs is the honor "
  "engine: every hospital bed a signed promise kept, every benefit a "
  "covenant repaying service with service, and every headstone a sworn "
  "marker that sacrifice is remembered.",
  {"founded": 1989, "budget_b": 320.0, "workforce_k": 450.0, "offices": 1700}),

E("The United States Environmental Protection Agency (EPA)", "Compounded", 16,
  "compounded",
  "The United States Environmental Protection Agency is the federal agency "
  "charged with protecting human health and the environment. It was "
  "established on December 2, 1970, following the first Earth Day and a "
  "presidential reorganization plan. It is led by an Administrator (not a "
  "Cabinet secretary) and headquartered in Washington, D.C., with ten "
  "regional offices. EPA enforces the Clean Air Act, the Clean Water Act, "
  "the Safe Drinking Water Act, the Superfund law for hazardous waste "
  "cleanup, the Resource Conservation and Recovery Act, the Toxic "
  "Substances Control Act, and the Federal Insecticide, Fungicide, and "
  "Rodenticide Act. It sets standards, issues permits, funds state "
  "programs, and cleans up contaminated sites.",
  "EPA protects the environment through standards, permits, enforcement, "
  "and cleanup. It sets national air quality standards that states "
  "implement through plans. It issues discharge permits for water "
  "pollution. It lists Superfund sites and oversees remediation paid for "
  "by responsible parties or the fund. It registers pesticides and "
  "reviews chemicals for safety. States often carry out day-to-day "
  "permitting under delegated authority, with EPA setting the floor and "
  "enforcing when states fall short.",
  ["Established 1970; led by an Administrator with ten regional offices.",
   "Enforces the Clean Air Act, Clean Water Act, and Superfund law.",
   "Sets national environmental standards implemented largely by states.",
   "Registers pesticides and reviews industrial chemicals."],
  ["Standards require scientific findings and public rulemaking.",
   "Enforcement needs evidence of violations and legal process.",
   "Superfund cleanups follow the National Contingency Plan."],
  ["Clean Air Act (42 U.S.C. 7401).",
   "Clean Water Act (33 U.S.C. 1251).",
   "Comprehensive Environmental Response, Compensation, and Liability Act (Superfund)."],
  ["U.S. Environmental Protection Agency - official organization (epa.gov).",
   "Reorganization Plan No. 3 of 1970 establishing EPA."],
  "In the Signature civic architecture EPA is the clean-air-and-water "
  "engine: every standard a signed limit on harm, every Superfund cleanup "
  "a sworn restoration of wounded ground, and every permit a covenant "
  "that industry and nature share the same air.",
  {"founded": 1970, "budget_b": 10.0, "workforce_k": 15.0, "offices": 10}),

E("The Federal Emergency Management Agency (FEMA)", "Compounded", 17,
  "compounded",
  "The Federal Emergency Management Agency is the federal agency that "
  "coordinates disaster response and recovery. It was created in 1979 by "
  "executive reorganization, consolidating civil defense and disaster "
  "programs, and became part of the Department of Homeland Security in "
  "2003. It is led by an Administrator and headquartered in Washington, "
  "D.C., with ten regional offices. FEMA does not replace state and local "
  "responders — it supports them when disasters overwhelm local capacity, "
  "after a presidential disaster declaration under the Stafford Act. It "
  "administers the National Flood Insurance Program, individual and public "
  "assistance grants, hazard mitigation grants, and emergency management "
  "training.",
  "FEMA works through the declaration process: a governor requests, the "
  "President declares, and federal assistance flows. Individual Assistance "
  "helps survivors with housing and needs; Public Assistance reimburses "
  "governments for debris removal and infrastructure repair; Hazard "
  "Mitigation funds projects that reduce future risk. FEMA pre-positions "
  "supplies, deploys incident management teams, and runs the National "
  "Response Coordination Center. Flood maps it produces set insurance "
  "requirements nationwide.",
  ["Created 1979; part of the Department of Homeland Security since 2003.",
   "Supports — not replaces — state and local responders.",
   "Activates on presidential disaster declarations under the Stafford Act.",
   "Runs the National Flood Insurance Program and disaster grant programs."],
  ["Federal aid requires a presidential declaration requested by a governor.",
   "Assistance follows published eligibility and documentation rules.",
   "Flood insurance purchase is mandatory in mapped high-risk zones with federally backed mortgages."],
  ["Robert T. Stafford Disaster Relief and Emergency Assistance Act.",
   "National Flood Insurance Act of 1968.",
   "Post-Katrina Emergency Management Reform Act of 2006."],
  ["Federal Emergency Management Agency - official organization (fema.gov).",
   "Reorganization Plan No. 3 of 1978 creating FEMA (effective 1979)."],
  "In the Signature civic architecture FEMA is the rally engine: every "
  "declaration a signed promise that help is coming, every mitigation "
  "grant a covenant to build stronger before the next storm, and every "
  "flood map a sworn chart of where the water goes.",
  {"founded": 1979, "budget_b": 25.0, "workforce_k": 20.0, "offices": 10}),

E("The Federal Communications Commission (FCC)", "Compounded", 18,
  "compounded",
  "The Federal Communications Commission is the independent federal agency "
  "that regulates interstate and international communications. It was "
  "created by the Communications Act of 1934. It is led by five "
  "commissioners appointed by the President and confirmed by the Senate, "
  "with no more than three from one political party, and headquartered in "
  "Washington, D.C. The FCC licenses radio and television broadcasters, "
  "allocates radio spectrum, regulates telephone and broadband providers, "
  "runs the Universal Service Fund that subsidizes rural and low-income "
  "connectivity, enforces robocall rules, and oversees equipment "
  "authorization for devices that emit radio frequencies.",
  "The FCC regulates through licensing, auctions, rules, and enforcement. "
  "It auctions spectrum licenses to wireless carriers, raising billions "
  "for the Treasury. It writes net-neutrality, ownership, and consumer "
  "protection rules through notice-and-comment rulemaking. Its Enforcement "
  "Bureau investigates interference, robocalls, and rule violations and "
  "can levy fines. The Universal Service Fund, paid by telecom carriers, "
  "supports the E-Rate program for schools and libraries and rural "
  "broadband.",
  ["Independent agency created 1934; five bipartisan commissioners.",
   "Licenses broadcasters and allocates radio spectrum.",
   "Regulates phone and broadband; runs the Universal Service Fund.",
   "Enforces robocall, interference, and equipment rules."],
  ["Licenses require applications showing public-interest service.",
   "Spectrum auctions follow statutory auction authority.",
   "Rules require notice, comment, and reasoned decision-making."],
  ["Communications Act of 1934 (47 U.S.C. 151).",
   "Telecommunications Act of 1996.",
   "Pallone-Thune Telephone Robocall Abuse Criminal Enforcement and Deterrence Act (2019)."],
  ["Federal Communications Commission - official organization (fcc.gov).",
   "Communications Act of 1934, Pub. L. 73-416."],
  "In the Signature civic architecture the FCC is the signal engine: every "
  "spectrum license a signed channel in the public airwaves, every "
  "universal-service dollar a covenant that distance does not silence, and "
  "every robocall fine a sworn defense of the quiet phone.",
  {"founded": 1934, "budget_b": 0.4, "workforce_k": 1.5, "offices": 15}),

E("The Federal Trade Commission (FTC)", "Compounded", 19,
  "compounded",
  "The Federal Trade Commission is the independent federal agency charged "
  "with protecting consumers and competition. It was created by the "
  "Federal Trade Commission Act of 1914. It is led by five commissioners "
  "serving staggered seven-year terms, with no more than three from one "
  "party, and headquartered in Washington, D.C. The FTC enforces antitrust "
  "law alongside the Justice Department, suing to block anticompetitive "
  "mergers and prosecuting monopolization. Its consumer protection "
  "mission covers deceptive advertising, scams, identity theft, data "
  "security, and the national Do Not Call Registry.",
  "The FTC acts through law enforcement, rulemaking, and education. Its "
  "Bureau of Competition reviews mergers under the Hart-Scott-Rodino "
  "premerger notification program and challenges deals that would "
  "substantially lessen competition. Its Bureau of Consumer Protection "
  "brings cases against deceptive practices and runs the consumer complaint "
  "system. The agency issues policy guidance, holds workshops, and "
  "publishes plain-language consumer advice. Settlements often include "
  "fines and long-term compliance orders.",
  ["Independent agency created 1914; five commissioners, seven-year terms.",
   "Enforces antitrust law and reviews mergers.",
   "Fights deceptive advertising, scams, and identity theft.",
   "Runs the national Do Not Call Registry."],
  ["Merger challenges require showing likely harm to competition.",
   "Consumer cases need evidence of deception or unfairness.",
   "Commissioners require Senate confirmation."],
  ["Federal Trade Commission Act (15 U.S.C. 41).",
   "Clayton Act of 1914.",
   "Hart-Scott-Rodino Antitrust Improvements Act of 1976."],
  ["Federal Trade Commission - official organization (ftc.gov).",
   "Federal Trade Commission Act, Pub. L. 63-203."],
  "In the Signature civic architecture the FTC is the fair-market engine: "
  "every blocked merger a signed defense of open competition, every scam "
  "prosecution a covenant with the honest buyer, and every Do Not Call "
  "listing a sworn boundary around the home.",
  {"founded": 1914, "budget_b": 0.4, "workforce_k": 1.1, "offices": 8}),

E("The United States Food and Drug Administration (FDA)", "Compounded", 20,
  "compounded",
  "The United States Food and Drug Administration is the federal agency "
  "that protects public health by regulating food, drugs, medical "
  "devices, and more. Its roots reach to the Pure Food and Drug Act of "
  "1906; it took its modern form and name through the 20th century and "
  "sits within the Department of Health and Human Services. It is led by "
  "a Commissioner and headquartered in White Oak, Maryland. The FDA "
  "approves new drugs and biologics, clears medical devices, regulates "
  "tobacco products, oversees the safety of the food supply (except meat "
  "and poultry, which USDA inspects), and regulates cosmetics and "
  "radiation-emitting products. Its decisions affect products worth "
  "trillions of dollars and the health of every American.",
  "The FDA regulates through premarket review, inspections, and "
  "enforcement. Drug makers must prove safety and efficacy through "
  "clinical trials before approval; devices go through clearance or "
  "approval pathways by risk class. Inspectors visit manufacturing "
  "plants worldwide. When products prove dangerous, the agency can order "
  "recalls, seize goods, and seek injunctions. It publishes drug labels, "
  "food safety guidance, and adverse-event databases, and its scientists "
  "review thousands of applications a year.",
  ["Roots in the 1906 Pure Food and Drug Act; part of HHS.",
   "Approves drugs and biologics; clears medical devices.",
   "Regulates food safety, tobacco, and cosmetics.",
   "Led by a Commissioner; headquartered in White Oak, Maryland."],
  ["Drug approval requires substantial evidence of safety and efficacy.",
   "Manufacturers must follow current Good Manufacturing Practice.",
   "Recalls and seizures require documented safety findings."],
  ["Federal Food, Drug, and Cosmetic Act (21 U.S.C. 301).",
   "Pure Food and Drug Act of 1906.",
   "Family Smoking Prevention and Tobacco Control Act of 2009."],
  ["U.S. Food and Drug Administration - official organization (fda.gov).",
   "Federal Food, Drug, and Cosmetic Act, Pub. L. 75-717 (1938)."],
  "In the Signature civic architecture the FDA is the purity engine: "
  "every drug approval a signed verdict of safety and efficacy, every "
  "inspection a sworn look inside the factory, and every recall a covenant "
  "that a dangerous product will not stay on the shelf.",
  {"founded": 1906, "budget_b": 6.0, "workforce_k": 18.0, "offices": 200}),

E("The Internal Revenue Service (IRS)", "Compounded", 21,
  "compounded",
  "The Internal Revenue Service is the federal bureau that collects "
  "taxes and enforces the tax code. Its origins trace to 1862, when "
  "President Lincoln created the office of Commissioner of Internal "
  "Revenue to fund the Civil War; it became a bureau of the Department "
  "of the Treasury. It is led by a Commissioner and headquartered in "
  "Washington, D.C., with processing centers and offices nationwide. "
  "The IRS processes hundreds of millions of tax returns each year, "
  "collects the revenue that funds the federal government, issues "
  "refunds, audits returns, pursues criminal tax fraud through its "
  "Criminal Investigation division, and administers tax-exempt "
  "organization status.",
  "The IRS works through forms, processing, and enforcement. Taxpayers "
  "file returns reporting income and claiming deductions and credits; "
  "employers withhold and report wages. The agency matches information "
  "returns, selects audits by risk, and can assess additional tax with "
  "appeal rights to the Tax Court. Criminal Investigation builds fraud "
  "cases for prosecution. The Taxpayer Advocate Service helps those "
  "facing hardship. Free File and Volunteer Income Tax Assistance help "
  "eligible filers at no cost.",
  ["Origins in 1862; a bureau of the Department of the Treasury.",
   "Collects the revenue that funds the federal government.",
   "Processes hundreds of millions of returns; issues refunds.",
   "Criminal Investigation pursues tax fraud."],
  ["Taxes are assessed under the Internal Revenue Code.",
   "Audits require notice and statutory appeal rights.",
   "Taxpayer information is confidential under Section 6103."],
  ["Internal Revenue Code (Title 26, U.S. Code).",
   "Revenue Act of 1862 creating the Commissioner of Internal Revenue.",
   "Taxpayer Bill of Rights (1996, expanded 2014)."],
  ["Internal Revenue Service - official organization (irs.gov).",
   "Revenue Act of 1862 (12 Stat. 432)."],
  "In the Signature civic architecture the IRS is the revenue engine: "
  "every filed return a signed accounting to the republic, every refund "
  "a covenant of exact balance, and every fraud prosecution a sworn "
  "defense of the honest taxpayer.",
  {"founded": 1862, "budget_b": 14.0, "workforce_k": 85.0, "offices": 500}),

E("The National Aeronautics and Space Administration (NASA)", "Compounded", 22,
  "compounded",
  "The National Aeronautics and Space Administration is the federal "
  "agency responsible for the civilian space program and aeronautics "
  "research. It was established by the National Aeronautics and Space "
  "Act of 1958 and began operations on October 1, 1958. It is led by an "
  "Administrator and headquartered in Washington, D.C. NASA landed "
  "astronauts on the Moon through the Apollo program, operates the "
  "International Space Station partnership, runs robotic missions across "
  "the solar system, launches the James Webb Space Telescope's science "
  "program, and develops the Artemis program to return astronauts to the "
  "Moon. Its field centers include Johnson Space Center in Texas, Kennedy "
  "Space Center in Florida, and the Jet Propulsion Laboratory in "
  "California (operated for NASA by Caltech).",
  "NASA explores through missions, research, and partnerships. Mission "
  "directorates plan robotic and crewed flights; centers build and "
  "operate spacecraft; contractors supply launch vehicles and hardware. "
  "The agency funds university research, shares Earth-science data "
  "freely, and transfers technology to industry. Artemis works with "
  "commercial and international partners. Aeronautics research improves "
  "aircraft efficiency and safety. Every major program passes through "
  "formal reviews, budgets, and congressional authorization.",
  ["Established 1958; civilian space and aeronautics agency.",
   "Landed astronauts on the Moon; operates ISS partnership missions.",
   "Runs robotic exploration across the solar system.",
   "Developing the Artemis Moon program with commercial partners."],
  ["Programs require congressional authorization and appropriations.",
   "Crewed flight follows strict safety and review standards.",
   "International partnerships are governed by agreements."],
  ["National Aeronautics and Space Act of 1958 (42 U.S.C. 2451).",
   "Commercial Space Launch Competitiveness Act of 2015."],
  ["National Aeronautics and Space Administration - official organization (nasa.gov).",
   "National Aeronautics and Space Act, Pub. L. 85-568."],
  "In the Signature civic architecture NASA is the ascent engine: every "
  "launch a signed defiance of gravity, every deep-space probe a covenant "
  "with curiosity, and every Moon footprint a sworn marker that the "
  "republic reaches upward.",
  {"founded": 1958, "budget_b": 25.0, "workforce_k": 18.0, "offices": 10}),

E("The National Institutes of Health (NIH)", "Compounded", 23,
  "compounded",
  "The National Institutes of Health is the federal agency that conducts "
  "and funds biomedical research. Its roots reach to 1887, when the "
  "Hygienic Laboratory was founded; it grew into today's NIH within the "
  "Department of Health and Human Services. It is led by a Director and "
  "headquartered in Bethesda, Maryland. NIH comprises 27 institutes and "
  "centers covering cancer, heart disease, infectious disease, mental "
  "health, aging, and more. It funds research at universities and medical "
  "centers nationwide through grants and conducts its own research on "
  "its campus, including the world's largest hospital devoted to "
  "clinical research.",
  "NIH advances medicine through grants and intramural science. "
  "Extramural grants are awarded competitively after peer review by "
  "scientists; the institute directors make final funding decisions. "
  "Intramural researchers work in NIH laboratories and the Clinical "
  "Center, where patients enroll in research protocols. The agency "
  "publishes findings freely, maintains databases like PubMed and "
  "ClinicalTrials.gov, and sets standards for research ethics, including "
  "human-subject protections and animal care.",
  ["Roots in 1887; part of the Department of Health and Human Services.",
   "27 institutes and centers covering major disease areas.",
   "Largest public funder of biomedical research in the world.",
   "Runs the Clinical Center, the largest research hospital of its kind."],
  ["Grants require competitive peer review.",
   "Human research must pass institutional review board ethics review.",
   "Findings are published openly; data sharing is required."],
  ["Public Health Service Act (NIH authorities, 42 U.S.C. 281).",
   "NIH Revitalization Act of 1993.",
   "21st Century Cures Act of 2016."],
  ["National Institutes of Health - official organization (nih.gov).",
   "History of NIH: the Hygienic Laboratory, founded August 1887."],
  "In the Signature civic architecture NIH is the discovery engine: every "
  "grant a signed wager on a question, every peer review a covenant of "
  "rigor, and every published finding a sworn gift to the world's "
  "healers.",
  {"founded": 1887, "budget_b": 48.0, "workforce_k": 20.0, "offices": 27}),

E("The National Oceanic and Atmospheric Administration (NOAA)", "Compounded", 24,
  "compounded",
  "The National Oceanic and Atmospheric Administration is the federal "
  "agency responsible for weather, oceans, and the atmosphere. It was "
  "established on October 3, 1970, within the Department of Commerce, "
  "drawing together the Weather Bureau (founded 1870), the Coast and "
  "Geodetic Survey, and other science agencies. It is led by an "
  "Administrator and headquartered in Silver Spring, Maryland. NOAA runs "
  "the National Weather Service, which issues forecasts and life-saving "
  "warnings; operates environmental satellites; manages national marine "
  "fisheries; charts the nation's waters; and researches climate. Its "
  "data underpins every weather app, newscast, and emergency alert in "
  "America.",
  "NOAA observes, forecasts, and manages. Satellites, radars, buoys, and "
  "aircraft feed supercomputers that model the atmosphere and oceans. "
  "Weather Service forecasters issue watches and warnings that trigger "
  "public alerts. Fisheries scientists set catch limits under the "
  "Magnuson-Stevens Act. The Office of Coast Survey updates nautical "
  "charts. Climate researchers maintain long-term records. Most data is "
  "free and open, feeding private weather companies, researchers, and "
  "emergency managers.",
  ["Established 1970 within the Department of Commerce.",
   "Runs the National Weather Service and its warning system.",
   "Operates environmental satellites and ocean observing systems.",
   "Manages fisheries and charts U.S. waters."],
  ["Warnings follow statutory weather-service authority.",
   "Fishery rules require science-based catch limits and public process.",
   "Satellite programs need authorization and appropriations."],
  ["National Weather Service Organic Act (15 U.S.C. 313).",
   "Magnuson-Stevens Fishery Conservation and Management Act.",
   "Coastal Zone Management Act of 1972."],
  ["National Oceanic and Atmospheric Administration - official organization (noaa.gov).",
   "Reorganization Plan No. 4 of 1970 establishing NOAA."],
  "In the Signature civic architecture NOAA is the sky-and-sea engine: "
  "every forecast a signed reading of the winds, every warning a covenant "
  "of timely alarm, and every chart a sworn map of the waters the nation "
  "sails.",
  {"founded": 1970, "budget_b": 6.0, "workforce_k": 12.0, "offices": 120}),

# ---------------- ADVANCED 25-34 ----------------

E("The United States Small Business Administration (SBA)", "Advanced", 25,
  "advanced",
  "The United States Small Business Administration is the federal agency "
  "that supports small businesses. It was created by the Small Business "
  "Act of 1953. It is led by an Administrator and headquartered in "
  "Washington, D.C. The SBA does not lend directly in most programs; "
  "instead it guarantees loans made by banks, reducing lender risk. Its "
  "flagship 7(a) loan program is the government's primary small-business "
  "lending tool. It also runs the 504 fixed-asset loan program, disaster "
  "loans for businesses and homeowners after declared disasters, the 8(a) "
  "contracting program for disadvantaged businesses, Small Business "
  "Development Centers, and SCORE mentoring. Federal agencies must direct "
  "a share of contracting dollars to small businesses, and SBA oversees "
  "those goals.",
  "SBA supports enterprise through guarantees, counseling, and "
  "contracting. A borrower applies through a participating lender; SBA's "
  "guaranty backs part of the loan. Disaster loans go directly from SBA "
  "after a disaster declaration. The 8(a) program certifies eligible "
  "firms for set-aside contracts. Development centers and SCORE provide "
  "free advising. Contracting officers across government set aside work "
  "for small, women-owned, veteran-owned, and disadvantaged businesses "
  "under SBA-monitored goals.",
  ["Created 1953 by the Small Business Act.",
   "Guarantees small-business loans through banks via the 7(a) program.",
   "Makes direct disaster loans after declared disasters.",
   "Runs the 8(a) contracting program and free business counseling."],
  ["Borrowers must meet SBA size standards for their industry.",
   "7(a) borrowers must show they cannot get credit elsewhere on reasonable terms.",
   "Disaster loans require a disaster declaration."],
  ["Small Business Act of 1953 (15 U.S.C. 631).",
   "Small Business Investment Act of 1958."],
  ["U.S. Small Business Administration - official organization (sba.gov).",
   "Small Business Act, Pub. L. 83-163."],
  "In the Signature civic architecture the SBA is the enterprise engine: "
  "every loan guaranty a signed vote of confidence in a founder, every "
  "disaster loan a covenant of rebuilding, and every set-aside contract a "
  "sworn opening of the government's doors to small builders.",
  {"founded": 1953, "budget_b": 1.0, "workforce_k": 3.0, "offices": 68}),

E("The United States Social Security Administration (SSA)", "Advanced", 26,
  "advanced",
  "The United States Social Security Administration is the federal agency "
  "that administers Social Security. It was created by the Social "
  "Security Act of 1935 and became an independent agency in 1995. It is "
  "led by a Commissioner and headquartered in Woodlawn, Maryland, near "
  "Baltimore. SSA pays retirement, survivors, and disability benefits to "
  "tens of millions of Americans, and administers Supplemental Security "
  "Income for aged, blind, and disabled people with limited means. It "
  "issues Social Security numbers, keeps lifetime earnings records for "
  "workers, and operates field offices and a national teleservice "
  "network. Social Security is funded by payroll taxes under the Federal "
  "Insurance Contributions Act.",
  "SSA runs the nation's retirement and disability insurance through "
  "records, claims, and payments. Employers report wages; SSA credits "
  "earnings to each worker's record. Beneficiaries apply online, by "
  "phone, or in field offices; claims representatives verify eligibility "
  "and compute benefit amounts by formula. Disability claims go through "
  "medical review by state agencies under federal rules, with appeals "
  "through administrative law judges. Annual cost-of-living adjustments "
  "track inflation. The trust funds' finances are reported yearly by "
  "their trustees.",
  ["Created 1935; independent agency since 1995.",
   "Pays retirement, survivors, disability, and SSI benefits.",
   "Keeps lifetime earnings records; issues Social Security numbers.",
   "Funded by payroll taxes; headquartered in Woodlawn, Maryland."],
  ["Benefits require insured work history or qualifying disability.",
   "Disability claims need medical evidence and functional assessment.",
   "Appeals follow administrative process with hearing rights."],
  ["Social Security Act of 1935 (42 U.S.C. 301).",
   "Social Security Independence and Program Improvements Act of 1994."],
  ["Social Security Administration - official organization (ssa.gov).",
   "Social Security Act, Pub. L. 74-271."],
  "In the Signature civic architecture SSA is the promise engine: every "
  "earnings record a signed ledger of a working life, every benefit check "
  "a covenant that old age and disability will not mean destitution, and "
  "every number issued a sworn identity in the national compact.",
  {"founded": 1935, "budget_b": 1400.0, "workforce_k": 60.0, "offices": 1200}),

E("The United States Agency for International Development (USAID)", "Advanced", 27,
  "advanced",
  "The United States Agency for International Development was the federal "
  "agency responsible for administering civilian foreign aid and "
  "development assistance. It was created by the Foreign Assistance Act "
  "of 1961 and established by executive order in November 1961. For "
  "decades it ran programs in global health, food security, disaster "
  "assistance, democracy support, and economic development in more than "
  "100 countries, working through contracts, grants, and partnerships "
  "with nonprofits and local organizations. In 2025 the agency was "
  "dissolved and its functions were absorbed into the Department of "
  "State, ending its run as an independent agency. Its record includes "
  "major programs such as Feed the Future and the President's Emergency "
  "Plan for AIDS Relief (PEPFAR, implemented with other agencies).",
  "USAID worked through awards and field missions. Congress appropriated "
  "funds by account; the agency obligated them through contracts and "
  "grants to implementing partners, overseen by mission offices abroad. "
  "Its Office of U.S. Foreign Disaster Assistance responded to "
  "emergencies with relief commodities and funding. Programs were "
  "designed with host governments, monitored for results, and audited "
  "for compliance. Following the 2025 dissolution, remaining functions "
  "and staff moved under State Department management, and historical "
  "program records remain the authoritative account of its work.",
  ["Created 1961; dissolved 2025 with functions absorbed by the State Department.",
   "Ran global health, food security, and disaster assistance programs.",
   "Worked in 100+ countries through contracts, grants, and partnerships.",
   "Implemented programs such as Feed the Future and supported PEPFAR."],
  ["Awards required competition under federal acquisition and assistance rules.",
   "Programs needed congressional appropriations by account.",
   "Post-2025, inquiries go to the Department of State as successor."],
  ["Foreign Assistance Act of 1961 (22 U.S.C. 2151).",
   "Executive Order 11223 (1965) and successor authorities."],
  ["U.S. Agency for International Development - historical organization records.",
   "Foreign Assistance Act of 1961, Pub. L. 87-195."],
  "In the Signature civic architecture USAID is remembered as the "
  "outreach engine: every mission a signed hand extended abroad, every "
  "food shipment a covenant against hunger, and its archive a sworn "
  "record that the republic once organized its generosity at scale.",
  {"founded": 1961, "budget_b": 40.0, "workforce_k": 10.0, "offices": 80}),

E("The Federal Reserve System", "Advanced", 28,
  "advanced",
  "The Federal Reserve System is the central bank of the United States. "
  "It was created by the Federal Reserve Act of 1913. It consists of the "
  "Board of Governors in Washington, D.C., twelve regional Federal "
  "Reserve Banks, and the Federal Open Market Committee, which sets "
  "monetary policy. Congress gave it a dual mandate: stable prices and "
  "maximum employment. The Fed sets the target range for the federal "
  "funds rate, supervises and regulates banks, provides financial "
  "services to the government and banks, issues currency through the "
  "Reserve Banks, and acts as lender of last resort in crises. Its "
  "independence within government is designed to insulate monetary "
  "policy from short-term political pressure.",
  "The Fed steers the economy through interest rates, supervision, and "
  "liquidity. The FOMC meets eight times a year to set the federal funds "
  "target; the New York Fed implements policy through open market "
  "operations. Supervisors examine banks for safety and soundness. In "
  "crises it can lend through the discount window and emergency "
  "facilities authorized by the Board. It publishes minutes, projections, "
  "and a plain-language statement after each meeting, and the Chair "
  "testifies to Congress twice a year.",
  ["Central bank created 1913; dual mandate of stable prices and maximum employment.",
   "Board of Governors plus 12 regional Reserve Banks; FOMC sets policy.",
   "Supervises banks; issues currency; lender of last resort.",
   "Independent within government by congressional design."],
  ["Monetary policy decisions require FOMC votes under the Federal Reserve Act.",
   "Emergency lending needs Board authorization and Treasury consultation.",
   "Supervision follows published examination standards."],
  ["Federal Reserve Act of 1913 (12 U.S.C. 221).",
   "Banking Act of 1935 (FOMC structure).",
   "Dodd-Frank Wall Street Reform and Consumer Protection Act of 2010."],
  ["Board of Governors of the Federal Reserve System - official organization (federalreserve.gov).",
   "Federal Reserve Act, Pub. L. 63-43."],
  "In the Signature civic architecture the Federal Reserve is the balance "
  "engine: every rate decision a signed tuning of the nation's economic "
  "instrument, every supervision a covenant of sound banking, and every "
  "published minute a sworn transparency of power exercised at arm's "
  "length from politics.",
  {"founded": 1913, "budget_b": 7.0, "workforce_k": 24.0, "offices": 12}),

E("The Library of Congress", "Advanced", 29,
  "advanced",
  "The Library of Congress is the national library of the United States "
  "and the largest library in the world. It was established on April 24, "
  "1800, by act of Congress. It is led by the Librarian of Congress and "
  "housed principally in the Thomas Jefferson Building on Capitol Hill in "
  "Washington, D.C. Its collections hold well over 170 million items, "
  "including books, maps, manuscripts, photographs, films, and sound "
  "recordings. It administers the U.S. Copyright Office, runs the "
  "Congressional Research Service that advises Congress, operates the "
  "National Library Service for the blind and print-disabled, and hosts "
  "the National Book Festival. Much of its digitized collection is free "
  "online.",
  "The Library preserves and shares knowledge through acquisition, "
  "cataloging, and digitization. Copyright deposits feed the collections "
  "under the Copyright Act. The Congressional Research Service produces "
  "nonpartisan reports for members of Congress. Catalogers create the "
  "records that libraries worldwide reuse. Digitization teams scan "
  "millions of items for loc.gov. Reading rooms serve researchers; "
  "exhibitions and concerts serve the public. Preservation labs care for "
  "fragile treasures from the earliest printed books to early films.",
  ["Established 1800; the largest library in the world.",
   "Holds well over 170 million items across every format.",
   "Administers the U.S. Copyright Office and the Congressional Research Service.",
   "Led by the Librarian of Congress on Capitol Hill."],
  ["Collections grow through copyright deposit, purchase, and gift.",
   "CRS serves Congress exclusively under its charter.",
   "Preservation follows professional archival standards."],
  ["Act of April 24, 1800 (2 Stat. 55) establishing the Library.",
   "Copyright Act (Title 17, U.S. Code).",
   "Legislative Reorganization Act of 1970 (CRS)."],
  ["Library of Congress - official organization (loc.gov).",
   "Act of April 24, 1800 (2 Stat. 55)."],
  "In the Signature civic architecture the Library of Congress is the "
  "memory engine: every cataloged volume a signed entry in the national "
  "memory, every copyright deposit a covenant that creation is recorded, "
  "and every digitized page a sworn opening of the vaults to all.",
  {"founded": 1800, "budget_b": 0.8, "workforce_k": 3.2, "offices": 3}),

E("The National Archives and Records Administration (NARA)", "Advanced", 30,
  "advanced",
  "The National Archives and Records Administration is the federal agency "
  "that preserves the nation's official records. It was established in "
  "1934 and became an independent agency in 1985. It is led by the "
  "Archivist of the United States and headquartered in Washington, D.C., "
  "with the iconic National Archives Building housing the Declaration of "
  "Independence, the Constitution, and the Bill of Rights. NARA manages "
  "the Federal Register, operates presidential libraries, runs records "
  "centers and the National Personnel Records Center, oversees the "
  "declassification of government documents, and sets records-management "
  "policy for the whole federal government. Its online catalog makes "
  "millions of records freely searchable.",
  "NARA preserves through appraisal, scheduling, and custody. Agencies "
  "transfer permanent records on approved schedules; NARA appraises what "
  "has enduring value. The Office of the Federal Register publishes "
  "regulations, presidential documents, and notices. Presidential "
  "libraries hold the papers of presidents from Hoover onward. "
  "Declassification reviewers apply executive orders to open secret "
  "records. Records centers store agencies' semi-active files. The "
  "agency's catalog and digitization program put founding documents and "
  "countless more records before the public.",
  ["Established 1934; independent agency since 1985.",
   "Holds the Declaration, Constitution, and Bill of Rights.",
   "Manages the Federal Register and presidential libraries.",
   "Sets federal records-management policy; led by the Archivist of the United States."],
  ["Records transfer follows approved disposition schedules.",
   "Declassification follows executive orders and statutory exemptions.",
   "Presidential records are governed by the Presidential Records Act."],
  ["National Archives Act of 1934.",
   "Presidential Records Act of 1978.",
   "Federal Records Act (44 U.S.C. chapters 21, 29, 31, 33)."],
  ["National Archives and Records Administration - official organization (archives.gov).",
   "National Archives Act, Pub. L. 73-432."],
  "In the Signature civic architecture NARA is the archive engine: every "
  "transferred record a signed page of the national story, every "
  "declassification a covenant of eventual openness, and the Charters of "
  "Freedom themselves the sworn foundation of the republic.",
  {"founded": 1934, "budget_b": 0.5, "workforce_k": 3.0, "offices": 40}),

E("The Government Accountability Office (GAO)", "Advanced", 31,
  "advanced",
  "The Government Accountability Office is the independent, nonpartisan "
  "agency that audits the federal government for Congress. It was created "
  "by the Budget and Accounting Act of 1921. It is led by the Comptroller "
  "General, appointed for a single 15-year term to ensure independence, "
  "and headquartered in Washington, D.C. GAO investigates how taxpayer "
  "dollars are spent, evaluates federal programs, issues legal decisions "
  "on bid protests and appropriations law, maintains the High-Risk List "
  "of troubled programs, and publishes the Yellow Book standards for "
  "government auditing. Its reports are public and widely cited in "
  "congressional oversight.",
  "GAO works through audits, evaluations, and legal opinions. Teams "
  "examine agency finances, program results, and management against "
  "criteria in law and best practice. Bid-protest attorneys decide "
  "whether federal contract awards followed the rules. The Comptroller "
  "General issues appropriations-law decisions that bind the executive "
  "branch. The High-Risk List, updated every two years, spotlights "
  "programs vulnerable to waste or needing transformation. Congress "
  "requests most of the work; GAO can also self-initiate under its "
  "mandate.",
  ["Independent, nonpartisan auditor created 1921.",
   "Led by the Comptroller General serving a 15-year term.",
   "Decides bid protests and appropriations-law questions.",
   "Publishes the High-Risk List and the Yellow Book audit standards."],
  ["Audits follow Generally Accepted Government Auditing Standards.",
   "Bid protests must be filed within strict deadlines.",
   "Most work is requested by Congress under statutory authority."],
  ["Budget and Accounting Act of 1921 (31 U.S.C. 702).",
   "Legislative Reorganization Act of 1970 (expanded evaluation role)."],
  ["Government Accountability Office - official organization (gao.gov).",
   "Budget and Accounting Act, Pub. L. 67-13."],
  "In the Signature civic architecture GAO is the audit engine: every "
  "report a signed reckoning of the public's money, every High-Risk "
  "listing a covenant of honest warning, and every bid-protest decision a "
  "sworn verdict that contracts go to merit, not favor.",
  {"founded": 1921, "budget_b": 0.7, "workforce_k": 3.0, "offices": 11}),

E("The Congressional Budget Office (CBO)", "Advanced", 32,
  "advanced",
  "The Congressional Budget Office is the nonpartisan agency that gives "
  "Congress objective budget and economic analysis. It was created by the "
  "Congressional Budget and Impoundment Control Act of 1974. It is led by "
  "a Director appointed jointly by House and Senate leadership and is "
  "headquartered in Washington, D.C. CBO produces the annual Budget and "
  "Economic Outlook, scores the cost of legislation, analyzes the "
  "President's budget, and publishes long-term projections. Its cost "
  "estimates — how much a bill would add to or subtract from the deficit "
  "— shape nearly every major legislative debate. It does not make policy "
  "recommendations; it provides the numbers Congress debates with.",
  "CBO analyzes through models, data, and transparent methods. "
  "Economists project revenues, spending, and the economy under current "
  "law as a baseline. When committees advance bills, analysts estimate "
  "their ten-year budgetary effects, publishing the assumptions. Long-"
  "term outlooks extend the horizon for Social Security, health care, and "
  "debt. Interactive tools and published methodologies let outsiders "
  "reproduce and critique the work. Its reputation rests on "
  "nonpartisanship: directors serve under both parties' leadership.",
  ["Nonpartisan budget agency created 1974.",
   "Scores the cost of legislation for Congress.",
   "Publishes the annual Budget and Economic Outlook.",
   "Makes no policy recommendations — analysis only."],
  ["Estimates use the current-law baseline required by statute.",
   "Methods and assumptions are published for transparency.",
   "The Director is appointed by bipartisan congressional leadership."],
  ["Congressional Budget and Impoundment Control Act of 1974 (2 U.S.C. 601).",
   "Balanced Budget and Emergency Deficit Control Act of 1985 (scoring rules)."],
  ["Congressional Budget Office - official organization (cbo.gov).",
   "Congressional Budget and Impoundment Control Act, Pub. L. 93-344."],
  "In the Signature civic architecture CBO is the reckoning engine: every "
  "cost estimate a signed price tag on a proposal, every baseline a "
  "covenant of honest arithmetic, and every outlook a sworn forecast of "
  "where the nation's finances are headed.",
  {"founded": 1974, "budget_b": 0.06, "workforce_k": 0.27, "offices": 1}),

E("The United States Postal Service (USPS)", "Advanced", 33,
  "advanced",
  "The United States Postal Service is the independent federal "
  "establishment that delivers the nation's mail. Its roots reach to "
  "1775, when the Second Continental Congress named Benjamin Franklin "
  "the first postmaster general; the modern USPS was created by the "
  "Postal Reorganization Act of 1970 and began operations in 1971. It is "
  "led by the Postmaster General under a Board of Governors and "
  "headquartered in Washington, D.C. USPS delivers to more than 160 "
  "million addresses, operates tens of thousands of post offices and "
  "processing facilities, and is bound by the universal service "
  "obligation: affordable delivery to every address in America. It "
  "receives no tax dollars for operations, funding itself through "
  "postage and services.",
  "USPS moves mail through collection, processing, transportation, and "
  "delivery. Carriers collect from boxes and post offices; automated "
  "plants sort billions of pieces; trucks and planes move mail between "
  "facilities; carriers deliver the last mile. Pricing for market-"
  "dominant products needs Postal Regulatory Commission review. The "
  "agency competes in package delivery while holding the mailbox "
  "monopoly for letters. Service standards set delivery time targets "
  "that are measured and reported publicly.",
  ["Independent establishment; modern form began 1971.",
   "Delivers to more than 160 million addresses nationwide.",
   "Bound by the universal service obligation.",
   "Self-funded through postage; receives no tax dollars for operations."],
  ["Rate changes for market-dominant mail need regulatory review.",
   "Universal service requires delivery to every address.",
   "The Postmaster General is appointed by the Board of Governors."],
  ["Postal Reorganization Act of 1970 (39 U.S.C. 101).",
   "Postal Accountability and Enhancement Act of 2006.",
   "Postal Service Reform Act of 2022."],
  ["United States Postal Service - official organization (usps.com).",
   "Postal Reorganization Act, Pub. L. 91-375."],
  "In the Signature civic architecture USPS is the delivery engine: every "
  "letter a signed trust carried to its door, every rural route a covenant "
  "that distance does not deny service, and every postmark a sworn stamp "
  "of the nation's promise to connect.",
  {"founded": 1971, "budget_b": 80.0, "workforce_k": 640.0, "offices": 31000}),

E("The United States Census Bureau", "Advanced", 34,
  "advanced",
  "The United States Census Bureau is the federal agency that counts the "
  "nation. It became a permanent agency in 1902 and sits within the "
  "Department of Commerce, headquartered in Suitland, Maryland. Its "
  "constitutional duty is the decennial census required by Article I, "
  "which apportions seats in the House of Representatives and guides the "
  "distribution of hundreds of billions in federal funds. Beyond the "
  "decennial count it runs the American Community Survey, the Economic "
  "Census every five years, and dozens of surveys measuring population, "
  "housing, and business. By law, individual responses are strictly "
  "confidential and cannot be shared with any other agency or court.",
  "The Bureau counts through address lists, outreach, and follow-up. It "
  "builds a master address file, mails invitations to respond online, by "
  "phone, or by paper, and sends enumerators to nonresponding "
  "households. Statisticians weight and tabulate results, applying "
  "disclosure-avoidance methods to protect confidentiality. Apportionment "
  "counts go to the President; redistricting data goes to the states. "
  "The American Community Survey produces yearly detailed profiles that "
  "communities use to plan schools, roads, and services.",
  ["Permanent agency since 1902; part of the Department of Commerce.",
   "Conducts the constitutionally required decennial census.",
   "Apportionment sets House seats; data guides hundreds of billions in funding.",
   "Individual responses are confidential by law (Title 13)."],
  ["The decennial census is required by Article I, Section 2 of the Constitution.",
   "Title 13 bars disclosure of individual responses, with criminal penalties.",
   "Apportionment uses the Method of Equal Proportions."],
  ["Title 13, U.S. Code (Census Act).",
   "Title 2, U.S. Code (apportionment)."],
  ["U.S. Census Bureau - official organization (census.gov).",
   "Act of March 6, 1902 (32 Stat. 51) establishing the permanent Census Office."],
  "In the Signature civic architecture the Census Bureau is the tally "
  "engine: every counted person a signed mark of belonging, every "
  "apportionment a covenant of fair representation, and every sealed "
  "response a sworn promise that the count serves the people, never "
  "surveils them.",
  {"founded": 1902, "budget_b": 1.5, "workforce_k": 8.0, "offices": 6}),
]

TIERS = {"foundations": "Foundations", "compounded": "Compounded",
         "advanced": "Advanced"}
