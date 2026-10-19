#!/usr/bin/env python3
"""Engineer project records: 34 real public projects + 34 Signature concepts."""

ENGINEER_PUBLIC = [
 dict(name="Hoover Dam", group="Dams", location="Black Canyon, Colorado River, Nevada/Arizona, USA",
  dates="1931-1936", figures="U.S. Bureau of Reclamation; Six Companies, Inc.",
  history=("Hoover Dam was the signature public work of the Great Depression: authorized by the "
   "Boulder Canyon Project Act of 1928, built 1931-1936 by Six Companies, Inc. with up to 5,200 "
   "workers on site. It tamed the Colorado River, impounding Lake Mead - the largest reservoir in "
   "the United States - and proved America could build at continental scale."),
  how_it_works=("A concrete gravity-arch dam: its 726-foot height and curved axis push water pressure "
   "into the canyon walls as well as down into the foundation. Water drops through penstocks to "
   "powerhouse turbines (now about 2,080 MW capacity), and the reservoir stores two years of river "
   "flow for the Southwest."),
  specs=[("Height","726 ft"),("Crest length","1,244 ft"),("Concrete","3.25 million cubic yards"),
   ("Reservoir","Lake Mead, 28.9 million acre-feet"),("Power","about 2,080 MW")],
  materials=["Mass concrete","Steel penstocks","Turbines and generators","Foundation grouting"],
  codes=["USBR design standards","FERC dam safety"],
  citations=["U.S. Bureau of Reclamation project records","Encyclopaedia Britannica"],
  structures=[("Dam Crest",1244,45),("Spillway",500,80),("Powerhouse",400,120),("Intake Towers",100,60)]),
 dict(name="Panama Canal", group="Waterways", location="Isthmus of Panama",
  dates="1904-1914 (U.S. construction); expansion 2007-2016", figures="U.S. Isthmian Canal Commission; George Goethals",
  history=("The Panama Canal - 51 miles linking the Atlantic and Pacific - was the moonshot of the "
   "early 1900s. France's 1880s attempt failed catastrophically; the United States succeeded "
   "1904-1914 by conquering yellow fever (William Gorgas' sanitation campaign) and choosing a "
   "lock canal over a sea-level cut. The 2016 expansion added neo-Panamax locks."),
  how_it_works=("Ships climb 85 feet to Gatun Lake through three lock chambers, cross the continental "
   "divide via the Gaillard Cut, and descend through the Pedro Miguel and Miraflores locks. Each "
   "lockage uses about 52 million gallons of water; the new locks recycle it in water-saving "
   "basins."),
  specs=[("Length","51 miles"),("Lift","85 ft to Gatun Lake"),("Original locks","Gatun, Pedro Miguel, Miraflores"),
   ("Neo-Panamax locks","Agua Clara, Cocoli (2016)"),("Transit time","8-10 hours")],
  materials=["Mass concrete locks","Steel miter gates","Towing locomotives","Dredged channels"],
  codes=["Panama Canal Authority regulations","PIANC guidelines"],
  citations=["Panama Canal Authority","Encyclopaedia Britannica"],
  structures=[("Gatun Locks",1000,110),("Gaillard Cut",3000,300),("Miraflores Locks",1000,110),("Gatun Lake",2000,1500)]),
 dict(name="Golden Gate Bridge", group="Bridges", location="San Francisco, California, USA",
  dates="1933-1937", figures="Joseph Strauss (chief engineer); Charles Alton Ellis (design)",
  history=("The Golden Gate Bridge - 1.7 miles across the strait in International Orange - opened "
   "in 1937 as the longest suspension span in the world. Chief engineer Joseph Strauss drove it "
   "through a decade of opposition; designer Charles Ellis did the structural mathematics. It "
   "remains the defining American bridge."),
  how_it_works=("Two main cables (each 7,650 feet, 27,572 wires) drape over 746-foot towers; 250 "
   "pairs of suspender ropes hang the 90-foot-wide deck. The deck's stiffening truss resists wind - "
   "a lesson learned industry-wide after Tacoma Narrows."),
  specs=[("Total length","8,981 ft (1.7 mi)"),("Main span","4,200 ft"),("Tower height","746 ft"),
   ("Cable wire","80,000 miles total"),("Color","International Orange")],
  materials=["Steel main cables","Steel towers","Concrete anchorages","Steel deck truss"],
  codes=["AASHTO (retroactive)","California seismic retrofit standards"],
  citations=["Golden Gate Bridge District records","Encyclopaedia Britannica"],
  structures=[("Main Span",4200,90),("South Tower",746,60),("North Anchorage",200,150),("Approach",1500,90)]),
 dict(name="Brooklyn Bridge", group="Bridges", location="New York City, USA",
  dates="1869-1883", figures="John Augustus Roebling; Washington Roebling; Emily Roebling",
  history=("The Brooklyn Bridge - the first steel-wire suspension bridge - opened in 1883 after 14 "
   "years of heroic construction. John Roebling died before it began; his son Washington was "
   "crippled by caisson disease; his wife Emily effectively directed completion. Its Gothic stone "
   "towers remain New York's great monument."),
  how_it_works=("Four main cables of steel wire (not iron - the first major use) span 1,595.5 feet "
   "between masonry towers; diagonal stays add stiffness. Caissons - pressurized wooden boxes - "
   "let workers dig the tower foundations underwater, at the cost of the bends."),
  specs=[("Main span","1,595.5 ft"),("Total length","5,989 ft"),("Tower height","276.5 ft"),
   ("Cable wire","14,000 miles"),("Opened","May 24, 1883")],
  materials=["Steel-wire cables","Granite/limestone towers","Wooden caissons","Steel deck"],
  codes=["Historic landmark standards","NYC DOT bridge inspection"],
  citations=["NYC Municipal Archives","Encyclopaedia Britannica"],
  structures=[("Main Span",1596,85),("Manhattan Tower",277,80),("Brooklyn Tower",277,80),("Approach",2000,85)]),
 dict(name="Channel Tunnel", group="Tunnels", location="Folkestone, UK - Coquelles, France",
  dates="1988-1994", figures="TransManche Link consortium",
  history=("The Channel Tunnel - 31.4 miles, the world's longest undersea tunnel section - opened "
   "in 1994 after six years of boring from both shores. Eleven tunnel boring machines met "
   "beneath the Channel; the British and French crews broke through within centimeters of plan."),
  how_it_works=("Two running tunnels (one track each) plus a central service tunnel, cross-connected "
   "every 375 meters. Shuttle trains carry cars and trucks; high-speed passenger trains run "
   "through. The service tunnel provides evacuation and ventilation."),
  specs=[("Total length","31.4 mi"),("Undersea section","23.5 mi"),("Depth","up to 250 ft below seabed"),
   ("TBMs","11"),("Opened","1994")],
  materials=["Tunnel boring machines","Segmental concrete lining","Rail systems","Shuttle trains"],
  codes=["Intergovernmental Commission safety","NFPA 130 principles"],
  citations=["Eurotunnel/LeShuttle records","Encyclopaedia Britannica"],
  structures=[("Running Tunnel A",150000,25),("Running Tunnel B",150000,25),("Service Tunnel",150000,16),("Terminal UK",2000,800)]),
 dict(name="Burj Khalifa", group="Buildings", location="Dubai, UAE",
  dates="2004-2010", figures="Skidmore, Owings & Merrill; Adrian Smith (design)",
  history=("The Burj Khalifa - 2,717 feet, 163 floors - opened in 2010 as the tallest structure "
   "ever built. SOM's buttressed-core design spirals a Y-shaped plan upward, each wing buttressing "
   "the others. It redefined what a skyscraper could be."),
  how_it_works=("A hexagonal central core buttressed by three wings - the 'buttressed core' - resists "
   "wind through shape, not mass: the stepped, spiraling form confuses wind vortices. A 192-pile "
   "foundation goes 164 feet into the ground."),
  specs=[("Height","2,717 ft"),("Floors","163"),("Concrete","330,000 cubic meters"),
   ("Foundation","192 piles, 164 ft deep"),("Opened","2010")],
  materials=["Reinforced concrete core","Aluminum/glass cladding","192 foundation piles","High-speed elevators"],
  codes=["Dubai building code","ASCE 7 wind","Performance-based fire design"],
  citations=["SOM project records","Encyclopaedia Britannica"],
  structures=[("Tower Footprint",200,200),("Podium",400,300),("Plaza",600,400),("Foundation Piles",200,200)]),
 dict(name="Eiffel Tower", group="Buildings", location="Paris, France",
  dates="1887-1889", figures="Gustave Eiffel; Maurice Koechlin; Emile Nouguier",
  history=("Built for the 1889 World's Fair, the Eiffel Tower - 330 meters of wrought iron - was "
   "the tallest structure on earth for 41 years. Parisians hated it, then adopted it; it was "
   "nearly demolished in 1909 before radio antennas saved it."),
  how_it_works=("Four lattice piers curve inward to a single tower - the curve follows the wind-load "
   "diagram, so the iron is exactly where the forces are. 18,038 pieces, 2.5 million rivets, all "
   "assembled with no on-site welding."),
  specs=[("Height","330 m (1,083 ft)"),("Iron","7,300 tonnes"),("Rivets","2.5 million"),
   ("Pieces","18,038"),("Built","1887-1889")],
  materials=["Wrought iron","Rivets","Paint (60 tonnes per coat)"],
  codes=["French historic monument standards"],
  citations=["Societe d'Exploitation de la Tour Eiffel","Encyclopaedia Britannica"],
  structures=[("Base 125m sq",410,410),("First Floor",200,200),("Second Floor",120,120),("Summit",60,60)]),
 dict(name="Empire State Building", group="Buildings", location="New York City, USA",
  dates="1930-1931", figures="Shreve, Lamb & Harmon; Starrett Brothers (builders)",
  history=("The Empire State Building rose in 13 months during the Depression - 102 stories, 1,454 "
   "feet to the tip - and held the world's-tallest title for 40 years. Its construction speed "
   "(a floor a day at peak) remains legendary."),
  how_it_works=("A steel frame riveted at speed, clad in Indiana limestone; the mooring mast (built "
   "for dirigibles, never used) gives the silhouette. Setbacks follow the 1916 zoning law - the "
   "law literally shaped the tower."),
  specs=[("Height","1,454 ft to tip"),("Stories","102"),("Steel","57,000 tons"),
   ("Built","13 months"),("Opened","1931")],
  materials=["Structural steel","Indiana limestone","Aluminum spandrels"],
  codes=["NYC 1930s building code","Landmark preservation"],
  citations=["Empire State Realty Trust","Encyclopaedia Britannica"],
  structures=[("Tower Footprint",200,200),("Fifth Ave Base",400,200),("Mast",60,60),("Lobby",150,80)]),
 dict(name="Transcontinental Railroad", group="Transport", location="United States (Omaha to Sacramento)",
  dates="1863-1869", figures="Central Pacific; Union Pacific; Theodore Judah",
  history=("Completed May 10, 1869 at Promontory, Utah, the transcontinental railroad bound America "
   "together: the Central Pacific built east over the Sierra Nevada (largely with Chinese labor), "
   "the Union Pacific built west across the plains. Travel time coast to coast fell from months "
   "to days."),
  how_it_works=("Two railroads built toward each other on the 1862 Pacific Railroad Act's land grants "
   "and bonds; the Sierra crossing required 15 tunnels and 37 miles of snow sheds. Standard gauge "
   "(4 ft 8.5 in) let cars run through."),
  specs=[("Length","1,912 miles"),("Completed","May 10, 1869"),("Sierra tunnels","15"),
   ("Workforce","up to 20,000"),("Gauge","standard 4 ft 8.5 in")],
  materials=["Iron/steel rail","Wood ties","Blasting powder","Snow sheds"],
  codes=["Pacific Railroad Acts 1862/1864"],
  citations=["National Park Service (Golden Spike)","Encyclopaedia Britannica"],
  structures=[("Sierra Crossing",5000,200),("Promontory Point",500,500),("Snow Sheds",3000,40),("Trestles",1000,60)]),
 dict(name="Interstate Highway System", group="Transport", location="United States",
  dates="1956-present", figures="President Dwight Eisenhower; Federal-Aid Highway Act of 1956",
  history=("Authorized in 1956, the Interstate Highway System - about 48,000 miles - is the largest "
   "public works project in American history. Eisenhower sold it on defense and commerce; it "
   "remade the country's geography, suburbs, and freight."),
  how_it_works=("Limited-access freeways on federal standards: 12-foot lanes, full control of access, "
   "design speeds of 70 mph. The Highway Trust Fund (fuel taxes) paid 90 percent of construction; "
   "states own and maintain the roads."),
  specs=[("Mileage","about 48,000 mi"),("Authorized","1956"),("Federal share","90%"),
   ("Design speed","70 mph"),("Lanes","12 ft standard")],
  materials=["Concrete/asphalt pavement","Bridges","Interchanges","Signage"],
  codes=["AASHTO Green Book","FHWA standards","MUTCD"],
  citations=["Federal Highway Administration","Encyclopaedia Britannica"],
  structures=[("Typical Section",200,120),("Interchange",1400,1400),("Bridge Span",500,80),("Rest Area",600,300)]),
 dict(name="Saturn V / Apollo", group="Space", location="Kennedy Space Center, Florida, USA",
  dates="1961-1972 (Apollo); Saturn V 1967-1973", figures="Wernher von Braun; NASA Marshall Space Flight Center",
  history=("The Saturn V - 363 feet, 7.5 million pounds of thrust - carried Apollo to the Moon: 12 "
   "astronauts walked on the lunar surface 1969-1972. It remains the most powerful rocket ever "
   "flown successfully, built by 400,000 workers across America."),
  how_it_works=("Three stages: the S-IC first stage (five F-1 engines) lifts off the pad; the S-II "
   "pushes toward orbit; the S-IVB restarts to send Apollo to the Moon. Staging discards dead "
   "weight - the rocket equation made flesh."),
  specs=[("Height","363 ft"),("Thrust","7.5 million lbf"),("Moon landings","6 (1969-1972)"),
   ("Astronauts on Moon","12"),("Launches","13, all successful")],
  materials=["F-1 and J-2 engines","Aluminum stages","Launch complex 39"],
  codes=["NASA human-rating standards"],
  citations=["NASA history records","Encyclopaedia Britannica"],
  structures=[("Launch Pad 39A",800,600),("VAB",700,500),("Crawlerway",5000,80),("Saturn V",363,60)]),
 dict(name="International Space Station", group="Space", location="Low Earth orbit, about 420 km",
  dates="1998-present", figures="NASA, Roscosmos, ESA, JAXA, CSA",
  history=("The International Space Station - first module launched 1998 - is the largest structure "
   "ever put in space: 15 nations, a million pounds, continuously crewed since 2000. It proved "
   "rival space agencies could build and operate one machine together."),
  how_it_works=("Pressurized modules connected in orbit; the integrated truss carries solar arrays "
   "(up to 120 kW) and radiators; visiting vehicles dock at multiple ports. It orbits every 90 "
   "minutes at 17,500 mph, reboosted against atmospheric drag."),
  specs=[("Mass","about 1 million lb"),("Orbit","about 420 km"),("Crewed since","November 2000"),
   ("Partner nations","15"),("Power","up to 120 kW")],
  materials=["Pressurized modules","Integrated truss","Solar arrays","Docking adapters"],
  codes=["NASA/partner safety standards"],
  citations=["NASA ISS records","Encyclopaedia Britannica"],
  structures=[("Truss 356ft",356,30),("US Segment",200,60),("Russian Segment",150,50),("Solar Arrays",240,120)]),
 dict(name="Three Gorges Dam", group="Dams", location="Yangtze River, Hubei, China",
  dates="1994-2012", figures="China Yangtze Power",
  history=("The Three Gorges Dam - the world's largest power station at 22,500 MW - was built "
   "1994-2012 across the Yangtze. Its reservoir displaced over a million people and submerged "
   "towns; its flood control and power transformed China's grid. Scale beyond precedent, "
   "controversy to match."),
  how_it_works=("A concrete gravity dam 607 feet high and 7,661 feet long; 32 main turbines plus "
   "underground units; a five-stage ship lock and ship lift pass vessels around it. Flood storage "
   "in the reservoir protects the downstream plain."),
  specs=[("Height","607 ft"),("Length","7,661 ft"),("Capacity","22,500 MW"),
   ("Concrete","27.2 million cubic meters"),("Resettled","over 1 million people")],
  materials=["Mass concrete","32+ turbines","Ship locks","Ship lift"],
  codes=["Chinese dam standards"],
  citations=["China Yangtze Power records","Encyclopaedia Britannica"],
  structures=[("Dam Axis",7661,100),("Ship Locks",1500,150),("Powerhouse",2000,200),("Spillway",1000,150)]),
 dict(name="Itaipu Dam", group="Dams", location="Parana River, Brazil/Paraguay",
  dates="1975-1991", figures="Itaipu Binacional",
  history=("Itaipu - 14,000 MW shared by Brazil and Paraguay - was the world's largest power "
   "station from 1984 until Three Gorges. Built 1975-1991 by a binational entity, it showed two "
   "nations could share one river's power."),
  how_it_works=("A concrete gravity dam with spillway and powerhouse; 20 generating units (18 main "
   "plus 2 auxiliary). Paraguay uses little of its half and sells most to Brazil - the dam is "
   "diplomacy in concrete."),
  specs=[("Capacity","14,000 MW"),("Units","20"),("Dam length","7,919 m total structures"),
   ("Built","1975-1991"),("Shared","Brazil/Paraguay")],
  materials=["Mass concrete","20 generating units","Spillway gates"],
  codes=["Brazilian/Paraguayan dam standards"],
  citations=["Itaipu Binacional records","Encyclopaedia Britannica"],
  structures=[("Dam Axis",4000,100),("Powerhouse",1000,150),("Spillway",800,120),("Reservoir",5000,2000)]),
 dict(name="Millau Viaduct", group="Bridges", location="Tarn Valley, France",
  dates="2001-2004", figures="Norman Foster (architect); Michel Virlogeux (engineer)",
  history=("The Millau Viaduct - tallest bridge in the world, mast tops 1,125 feet above the Tarn - "
   "opened in 2004 carrying the A75 across southern France. Foster and Virlogeux's cable-stayed "
   "design made infrastructure into sculpture."),
  how_it_works=("Seven pylons carry a 1.5-mile steel deck via cable stays; the deck was launched "
   "from both ends (incremental launching) to avoid falsework in the deep valley. The masts split "
   "into two legs above the deck for the stays."),
  specs=[("Mast height","1,125 ft above valley"),("Length","8,071 ft"),("Pylons","7"),
   ("Deck launching","incremental"),("Opened","2004")],
  materials=["Steel deck","Concrete pylons","Cable stays"],
  codes=["French bridge standards","Eurocodes"],
  citations=["Compagnie Eiffage records","Encyclopaedia Britannica"],
  structures=[("Viaduct 8071ft",8071,90),("Tallest Pylon",1125,60),("Valley Floor",3000,1500),("Approach",2000,90)]),
 dict(name="Akashi Kaikyo Bridge", group="Bridges", location="Kobe-Awaji, Japan",
  dates="1988-1998", figures="Honshu-Shikoku Bridge Authority",
  history=("The Akashi Kaikyo Bridge - main span 6,532 feet, the longest suspension span in the "
   "world - opened in 1998. Mid-construction, the 1995 Kobe earthquake moved the towers 3 feet "
   "apart; engineers simply lengthened the span and carried on."),
  how_it_works=("Two-hinged stiffening truss deck hung from twin main cables; the towers stand in "
   "deep, fast water on massive caisson foundations. Designed for 8.5-magnitude earthquakes and "
   "150-mph winds."),
  specs=[("Main span","6,532 ft"),("Total length","12,831 ft"),("Tower height","928 ft"),
   ("Opened","1998"),("Earthquake","survived Kobe 1995 mid-build")],
  materials=["Twin main cables","Steel towers","Caisson foundations","Truss deck"],
  codes=["Honshu-Shikoku standards","Japanese seismic code"],
  citations=["Honshu-Shikoku Bridge Expressway records","Encyclopaedia Britannica"],
  structures=[("Main Span",6532,100),("Towers",928,80),("Anchorages",300,200),("Approaches",3000,100)]),
 dict(name="London Underground", group="Transport", location="London, UK",
  dates="1863-present", figures="Metropolitan Railway",
  history=("The Metropolitan Railway opened in 1863 - the world's first underground railway, steam "
   "trains in cut-and-cover tunnels. The deep-level Tube (1890, electric) followed; the system "
   "now runs 11 lines and carries billions. Every metro on earth descends from it."),
  how_it_works=("Cut-and-cover built the first lines (dig, roof, cover); shield tunneling bored the "
   "deep Tube lines. Electric traction replaced steam by 1905; the deep tunnels' small diameter "
   "is why Tube trains are famously cramped."),
  specs=[("Opened","1863"),("Lines","11"),("First deep line","1890"),("Ridership","billions per year")],
  materials=["Cut-and-cover boxes","Shield tunnels","Electric rolling stock"],
  codes=["UK rail standards","London Underground engineering standards"],
  citations=["Transport for London archives","Encyclopaedia Britannica"],
  structures=[("Cut-Cover Box",200,40),("Tube Tunnel",200,15),("Station Box",400,80),("Depot",800,400)]),
 dict(name="Suez Canal", group="Waterways", location="Egypt (Port Said to Suez)",
  dates="1859-1869", figures="Ferdinand de Lesseps; Suez Canal Company",
  history=("The Suez Canal - 120 miles through desert, no locks (sea level throughout) - opened in "
   "1869 and cut the Europe-Asia voyage by thousands of miles. Dug largely by forced Egyptian "
   "labor under de Lesseps' company, it remains one of the world's great trade arteries."),
  how_it_works=("A sea-level canal: ships transit in convoy with no locks to slow them. The 2015 "
   "expansion added a parallel channel for two-way traffic in much of the canal."),
  specs=[("Length","120 miles"),("Locks","none (sea level)"),("Opened","1869"),
   ("Expansion","2015 new channel"),("Transit","about 12-16 hours")],
  materials=["Dredged channel","Bypass channels","Port facilities"],
  codes=["Suez Canal Authority rules"],
  citations=["Suez Canal Authority","Encyclopaedia Britannica"],
  structures=[("Canal 120mi",3000,300),("Bypass Channel",1500,300),("Port Said",1000,800),("Suez Port",1000,800)]),
 dict(name="Grand Coulee Dam", group="Dams", location="Columbia River, Washington, USA",
  dates="1933-1942", figures="U.S. Bureau of Reclamation",
  history=("Grand Coulee - 550 feet high, the largest concrete structure in America when built - "
   "was the Columbia Basin Project's heart: irrigation for the desert, power for the wartime "
   "Northwest (its electricity smelted the aluminum for WWII aircraft)."),
  how_it_works=("A concrete gravity dam across the Columbia; the Third Powerplant (1970s) added "
   "capacity to 6,809 MW. Pump-generators lift water to Banks Lake for irrigation - the dam "
   "waters as well as powers."),
  specs=[("Height","550 ft"),("Crest","5,223 ft"),("Capacity","6,809 MW"),
   ("Concrete","12 million cubic yards"),("Built","1933-1942")],
  materials=["Mass concrete","Pump-generators","Turbines","Irrigation canals"],
  codes=["USBR standards","FERC dam safety"],
  citations=["U.S. Bureau of Reclamation records","Encyclopaedia Britannica"],
  structures=[("Dam Axis",5223,100),("Powerhouse",1500,200),("Pump Plant",500,150),("Banks Lake",3000,1500)]),
 dict(name="Sydney Opera House", group="Buildings", location="Sydney, Australia",
  dates="1959-1973", figures="Jorn Utzon (architect); Ove Arup (engineer)",
  history=("The Sydney Opera House - Utzon's shells on Bennelong Point - opened in 1973 after 14 "
   "years of heroic engineering. Arup's team solved the shells with spherical geometry: every "
   "shell segment cut from one sphere, tiled in a million white tiles."),
  how_it_works=("The 'shells' are precast concrete ribs from a single 246-foot-radius sphere, "
   "post-tensioned and clad in glossy white tiles. The podium holds the halls; the shells are "
   "pure roof - structure as sculpture."),
  specs=[("Shell radius","246 ft"),("Tiles","over 1 million"),("Halls","multiple venues"),
   ("Opened","1973"),("UNESCO","World Heritage 2007")],
  materials=["Precast concrete ribs","Ceramic tiles","Glass walls","Post-tensioning"],
  codes=["Australian standards","UNESCO heritage management"],
  citations=["Sydney Opera House Trust","Encyclopaedia Britannica"],
  structures=[("Podium",600,400),("Shell Group",300,200),("Concert Hall",200,150),("Forecourt",400,300)]),
 dict(name="The Pentagon", group="Buildings", location="Arlington, Virginia, USA",
  dates="1941-1943", figures="George Edwin Bergstrom (architect)",
  history=("The Pentagon - 6.5 million square feet, the world's largest office building by floor "
   "area - was built in 16 months during WWII to house the War Department. Its five rings and "
   "five-sided plan put any office within a 7-minute walk of any other."),
  how_it_works=("Five concentric pentagonal rings around a 5-acre courtyard; 17.5 miles of "
   "corridors. The low, spread form was a wartime choice: harder to bomb effectively than a "
   "tower, fast to build in reinforced concrete."),
  specs=[("Floor area","6.5 million sq ft"),("Rings","5"),("Corridors","17.5 miles"),
   ("Built","16 months"),("Completed","1943")],
  materials=["Reinforced concrete","Limestone facade","Steel windows"],
  codes=["Wartime expedited standards","DoD force protection (later)"],
  citations=["U.S. Department of Defense","Encyclopaedia Britannica"],
  structures=[("Ring E",1500,1500),("Courtyard",500,500),("Rings A-D",1200,1200),("Parking",2000,1000)]),
 dict(name="Aswan High Dam", group="Dams", location="Nile River, Egypt",
  dates="1960-1970", figures="Soviet-Egyptian cooperation",
  history=("The Aswan High Dam - completed 1970 with Soviet assistance - created Lake Nasser and "
   "ended the Nile's annual flood. It electrified Egypt and enabled year-round irrigation, at the "
   "cost of the Nubian homeland (rescued temples, including Abu Simbel, were moved stone by "
   "stone)."),
  how_it_works=("A rockfill embankment dam 364 feet high; the reservoir stores the flood for "
   "controlled release; 12 turbines generate 2,100 MW. Sediment that once fertilized fields now "
   "settles in the lake - farmers use fertilizer instead."),
  specs=[("Height","364 ft"),("Crest","12,562 ft"),("Reservoir","Lake Nasser"),
   ("Capacity","2,100 MW"),("Completed","1970")],
  materials=["Rockfill embankment","Clay core","12 turbines"],
  codes=["Egyptian dam standards"],
  citations=["Encyclopaedia Britannica","Nile Basin records"],
  structures=[("Dam Axis",12562,150),("Powerhouse",800,150),("Spillway",1000,200),("Lake Nasser",8000,3000)]),
 dict(name="Oresund Bridge", group="Bridges", location="Copenhagen, Denmark - Malmo, Sweden",
  dates="1995-2000", figures="Oresundskonsortiet",
  history=("The Oresund Bridge (2000) is a bridge-tunnel hybrid: 5 miles of cable-stayed bridge, "
   "an artificial island, then 2.5 miles of immersed tunnel - because planes from Copenhagen "
   "airport needed the airspace. It fused Denmark and Sweden into one metro region."),
  how_it_works=("Cable-stayed bridge spans the navigation channel; the roadway dives onto Peberholm "
   "(artificial island) and continues through the Drogden immersed-tube tunnel. Rail runs below "
   "road on the bridge, beside it in the tunnel."),
  specs=[("Bridge","5 miles"),("Tunnel","2.5 miles"),("Main span","1,608 ft"),
   ("Opened","2000"),("Modes","road + rail")],
  materials=["Cable-stayed steel","Immersed tube segments","Artificial island"],
  codes=["Danish/Swedish standards","Eurocodes"],
  citations=["Oresundsbron records","Encyclopaedia Britannica"],
  structures=[("Bridge 5mi",2500,120),("Peberholm Island",1500,800),("Tunnel 2.5mi",1300,80),("Main Span",1608,100)]),
 dict(name="Gotthard Base Tunnel", group="Tunnels", location="Swiss Alps, Switzerland",
  dates="1999-2016", figures="AlpTransit Gotthard",
  history=("The Gotthard Base Tunnel - 35.5 miles, the world's longest rail tunnel - opened in 2016 "
   "after 17 years of boring through the Alps. It flattened the historic Gotthard route: freight "
   "trains now run level beneath the mountains instead of climbing over them."),
  how_it_works=("Two single-track bores with cross-passages; the flat alignment (max 8 per mille "
   "grade) lets heavy freight run at speed. Multifunction stations inside the tunnel allow "
   "overtaking and emergency response underground."),
  specs=[("Length","35.5 mi"),("Bores","2"),("Max grade","8 per mille"),
   ("Excavated rock","28 million tons"),("Opened","2016")],
  materials=["4 TBMs","Segmental lining","Rail systems","Multifunction stations"],
  codes=["Swiss rail standards","NFPA 130 principles"],
  citations=["AlpTransit Gotthard records","Encyclopaedia Britannica"],
  structures=[("Bore East",180000,30),("Bore West",180000,30),("Multifunction Station",2000,100),("Portal North",1500,500)]),
 dict(name="Palm Jumeirah", group="Land Reclamation", location="Dubai, UAE",
  dates="2001-2006 (reclamation)", figures="Nakheel",
  history=("Palm Jumeirah - the palm-shaped artificial island visible from space - was dredged "
   "2001-2006 from 94 million cubic meters of sand and 7 million tons of rock. No concrete or "
   "steel in the breakwater: rock placed by GPS to Dutch engineering."),
  how_it_works=("Rainbowing dredgers sprayed sand into the palm shape; vibro-compaction densified "
   "it; a crescent breakwater of placed rock shelters the island. GPS-guided placement held "
   "tolerances on a structure kilometers across."),
  specs=[("Sand","94 million cubic meters"),("Rock","7 million tons"),
   ("Breakwater","crescent, 11 km"),("Built","2001-2006")],
  materials=["Dredged sand","Placed rock","Vibro-compaction"],
  codes=["Dutch breakwater engineering practice"],
  citations=["Nakheel records","Encyclopaedia Britannica"],
  structures=[("Palm Trunk",2000,400),("Fronds",3000,2500),("Crescent",11000,400),("Causeway",1500,200)]),
 dict(name="Hong Kong-Zhuhai-Macau Bridge", group="Bridges", location="Pearl River Delta, China",
  dates="2009-2018", figures="HZMB Authority",
  history=("The Hong Kong-Zhuhai-Macau Bridge - 34 miles, the world's longest sea crossing - opened "
   "in 2018: bridges, artificial islands, and a 4-mile undersea tunnel threading the Pearl River "
   "Delta's shipping lanes and airport airspace."),
  how_it_works=("Three cable-stayed bridges span the navigation channels; the roadway dives through "
   "an immersed-tube tunnel (33 segments, each 600,000 tons) between two artificial islands. "
   "Designed for 120 years and super-typhoons."),
  specs=[("Length","34 miles"),("Tunnel","4.2 miles immersed"),("Design life","120 years"),
   ("Opened","2018")],
  materials=["Cable-stayed bridges","Immersed tube segments","Artificial islands"],
  codes=["Chinese bridge standards"],
  citations=["HZMB Authority records","Encyclopaedia Britannica"],
  structures=[("Bridge Sections",25000,120),("Tunnel 4.2mi",22000,80),("Island West",1500,800),("Island East",1500,800)]),
 dict(name="Taipei 101", group="Buildings", location="Taipei, Taiwan",
  dates="1999-2004", figures="C.Y. Lee (architect); Thornton Tomasetti (engineer)",
  history=("Taipei 101 - 1,671 feet, world's tallest 2004-2010 - wears its engineering outside: a "
   "660-ton tuned mass damper ball hangs visibly in the tower, swaying against typhoons and "
   "earthquakes. The pagoda-like stacking is structure and symbol."),
  how_it_works=("A braced core with outriggers every 8 floors; the 660-tonne steel damper - the "
   "world's largest - counter-sways in wind and quakes. Foundations: 380 piles into bedrock."),
  specs=[("Height","1,671 ft"),("Floors","101"),("Damper","660 tonnes"),
   ("Piles","380"),("Tallest","2004-2010")],
  materials=["Braced steel core","660-ton damper","380 piles","Double-pane facade"],
  codes=["Taiwan seismic code","Performance-based design"],
  citations=["Taipei 101 records","Encyclopaedia Britannica"],
  structures=[("Tower Footprint",200,200),("Damper Zone",60,60),("Podium",400,300),("Foundation",300,300)]),
 dict(name="One World Trade Center", group="Buildings", location="New York City, USA",
  dates="2006-2014", figures="Skidmore, Owings & Merrill; David Childs",
  history=("One World Trade Center - 1,776 feet, the symbolic height - rose 2006-2014 on the "
   "World Trade Center site. Its tapering, chamfered form and redundant structure answer the "
   "site's history with engineering: among the most secure tall buildings ever built."),
  how_it_works=("A concrete core with redundant steel moment frame; the tapered form sheds wind; "
   "the base is a blast-resistant concrete podium. Stair pressurization, hardened elevators, and "
   "redundant systems exceed code throughout."),
  specs=[("Height","1,776 ft (symbolic)"),("Stories","104"),("Built","2006-2014"),
   ("Structure","redundant core+frame")],
  materials=["Concrete core","Steel moment frame","Blast-resistant podium","Prismatic glass"],
  codes=["NYC Building Code","NYPD security standards","Progressive-collapse design"],
  citations=["Port Authority records","Encyclopaedia Britannica"],
  structures=[("Tower Footprint",200,200),("Podium",300,300),("Plaza",500,400),("Memorial",400,300)]),
 dict(name="Denver International Airport", group="Transport", location="Denver, Colorado, USA",
  dates="1989-1995", figures="Fentress Architects (terminal)",
  history=("Denver International Airport opened in 1995 with the most famous terminal roof ever "
   "built: Teflon-coated fiberglass tents echoing the Rockies. Beneath it runs one of the "
   "world's largest automated baggage systems - famously troubled at opening, later fixed."),
  how_it_works=("The Jeppesen Terminal's tensile membrane roof spans on masts and cables - fabric "
   "as structure. Six runways (the longest commercial runway in North America at 16,000 feet) "
   "handle the high-altitude thin air."),
  specs=[("Roof","tensile membrane, 15 acres"),("Runways","6"),("Longest runway","16,000 ft"),
   ("Opened","1995"),("Land","53 sq mi")],
  materials=["PTFE fiberglass membrane","Steel masts and cables","Concrete runways"],
  codes=["FAA AC 150","IBC assembly"],
  citations=["Denver International Airport records","Encyclopaedia Britannica"],
  structures=[("Terminal",1200,300),("Concourse A",1000,120),("Runway 16R",16000,200),("Airfield",8000,5000)]),
 dict(name="Falkirk Wheel", group="Waterways", location="Falkirk, Scotland, UK",
  dates="2000-2002", figures="British Waterways; Tony Kettle (architect)",
  history=("The Falkirk Wheel (2002) - the world's only rotating boat lift - reconnects the Forth "
   "and Clyde and Union canals across a 115-foot height difference. Two gondolas counterbalance "
   "perfectly: Archimedes' principle means a full gondola weighs the same as an empty one."),
  how_it_works=("Two 300-tonne gondolas rotate 180 degrees; because displaced water equals boat "
   "weight, the wheel is always balanced - 22.5 kW motors do the work of lifting 600 tonnes. "
   "The aqueduct delivers boats from the high canal."),
  specs=[("Lift","115 ft"),("Gondolas","2 x 300 tonnes"),("Power","22.5 kW"),
   ("Rotation","180 degrees"),("Opened","2002")],
  materials=["Steel wheel structure","Gondolas","Aqueduct","Gear ring"],
  codes=["British Waterways standards"],
  citations=["Scottish Canals records","Encyclopaedia Britannica"],
  structures=[("Wheel 115ft",120,120),("Aqueduct",300,40),("Visitor Center",100,60),("Basin",200,150)]),
 dict(name="Thames Barrier", group="Flood Defense", location="London, UK",
  dates="1974-1982", figures="Rendel, Palmer and Tritton",
  history=("The Thames Barrier - ten steel gates across the river at Woolwich - has protected "
   "London from storm surges since 1982. Each gate rotates up from the riverbed; the stainless "
   "cowls are a London landmark. It was designed for the floods of the future - and the future "
   "arrived, with closures rising yearly."),
  how_it_works=("Ten 61-meter spans; the gates rest flat on the riverbed sills and rotate up to "
   "block surge tides. Six are navigable; four close the shallows. Closure takes about 90 "
   "minutes from decision to sealed river."),
  specs=[("Spans","10"),("Span width","61 m"),("Gate rotation","90 degrees"),
   ("Completed","1982"),("Closures","rising yearly")],
  materials=["Steel gates","Stainless cowls","Concrete piers","Hydraulic machinery"],
  codes=["UK flood defense standards"],
  citations=["Environment Agency records","Encyclopaedia Britannica"],
  structures=[("Barrier 520m",1700,150),("Piers",100,80),("Control Building",80,40),("River Reach",3000,600)]),
 dict(name="Delta Works", group="Flood Defense", location="Zeeland, Netherlands",
  dates="1953-1997", figures="Rijkswaterstaat; Delta Commission",
  history=("After the 1953 North Sea flood killed 1,835 Dutch, the Netherlands built the Delta "
   "Works: dams, sluices, and the Oosterscheldekering - a 5.6-mile storm-surge barrier with "
   "movable gates, the largest of its kind. The American Society of Civil Engineers called it a "
   "wonder of the modern world."),
  how_it_works=("Estuaries were dammed except where ecology demanded openness - there, surge barriers "
   "with gates stay open for tides and close for storms. The Oosterscheldekering's 62 steel gates "
   "slide between concrete piers."),
  specs=[("Barrier length","5.6 miles"),("Gates","62 steel"),("Flood","1953, 1,835 dead"),
   ("Built","1953-1997"),("ASCE","wonder of the modern world")],
  materials=["62 steel gates","Concrete piers","Dams and sluices"],
  codes=["Dutch Delta Act standards"],
  citations=["Rijkswaterstaat records","Encyclopaedia Britannica"],
  structures=[("Oosterscheldekering",9000,200),("Gates",500,100),("Dams",5000,150),("Estuary",8000,3000)]),
 dict(name="Large Hadron Collider", group="Research", location="CERN, Swiss-French border",
  dates="1998-2008", figures="CERN",
  history=("The Large Hadron Collider - a 17-mile ring 100 meters underground - is the largest "
   "machine ever built. First beam 2008, first collisions 2009, Higgs boson discovered 2012. "
   "Its 1,232 superconducting dipole magnets run colder than deep space."),
  how_it_works=("Proton beams circulate in opposite directions through superconducting magnets at "
   "1.9 Kelvin, steered and focused around the ring; at four detectors they collide at nearly "
   "light speed. The tunnel reuses the earlier LEP ring."),
  specs=[("Ring","17 miles"),("Dipoles","1,232 superconducting"),("Temperature","1.9 K"),
   ("First beam","2008"),("Higgs","2012")],
  materials=["Superconducting magnets","Cryogenics","Detectors (ATLAS, CMS...)"],
  codes=["CERN safety standards"],
  citations=["CERN records","Encyclopaedia Britannica"],
  structures=[("Ring 17mi",8000,8000),("ATLAS Cavern",200,150),("CMS Cavern",200,150),("Surface Sites",1000,800)]),
 dict(name="Tokaido Shinkansen", group="Transport", location="Tokyo-Osaka, Japan",
  dates="1959-1964", figures="Japanese National Railways; Hideo Shima",
  history=("The Tokaido Shinkansen opened in 1964 - the world's first high-speed railway, Tokyo to "
   "Osaka at 130 mph. Hideo Shima's team built a dedicated standard-gauge line (Japan's old "
   "network was narrow gauge) and proved high-speed rail's economics; billions of passengers "
   "have ridden since without a fatal accident."),
  how_it_works=("Dedicated standard-gauge track with gentle curves and grades; 25 kV AC "
   "electrification; ATC signaling (no lineside signals at speed); earthquake detection that "
   "stops trains before the shaking arrives."),
  specs=[("Length","320 miles"),("Opened","1964"),("Speed","130 mph (original)"),
   ("Fatalities","zero passenger fatalities"),("Power","25 kV AC")],
  materials=["Standard-gauge track","25 kV catenary","Shinkansen trainsets","ATC signaling"],
  codes=["Japanese rail standards"],
  citations=["JR Central records","Encyclopaedia Britannica"],
  structures=[("Tokyo Station",800,400),("Viaduct Section",2000,60),("Osaka Station",800,400),("Depot",1500,800)]),
]

ENGINEER_SIGNATURE = [
 dict(name="Signature Sky Arcology", group="Habitats",
  concept=("A self-contained vertical city for 50,000 residents: housing, farms, factories, and "
   "civic life stacked in one walkable megastructure, so the ground below returns to forest. The "
   "Signature answer to sprawl is not denser sprawl - it is the city as a single building that "
   "treads lightly."),
  specs=[("Population","50,000"),("Height","1,600 ft"),("Footprint","12 acres"),
   ("Food","40% grown in-structure"),("Energy","net-positive")],
  history=("Signature original concept - arcology lineage from Paolo Soleri's 1960s work, rebuilt "
   "from first principles for repairable structure and daylight."),
  how_it_works=("Mixed-use vertical zoning: industry at the base (heavy, serviced by rail), civic "
   "and commercial in the middle ring, housing in the daylit upper two-thirds, sky farms at the "
   "crown. Gravity-fed water, stack-effect ventilation, and district energy close the loops."),
  materials=["Mass timber + steel hybrid","Unitized curtain wall","District energy plant","Sky-farm systems"],
  phases=["Phase 1: foundation and base industry (years 1-3)","Phase 2: middle civic ring (years 3-5)",
   "Phase 3: housing tiers (years 4-7)","Phase 4: crown farms and commissioning (years 7-8)"],
  structures=[("Tower 1600ft",400,400),("Base Industry",600,400),("Civic Ring",500,300),("Crown Farms",400,200)]),
 dict(name="Signature Ocean Platform City", group="Habitats",
  concept=("A floating modular city for 20,000 people on stabilized platforms: breakwater ring, "
   "residential pontoons, and an industrial core - seasteading rebuilt as civic engineering with "
   "real utilities, not a libertarian stunt."),
  specs=[("Population","20,000"),("Platforms","modular 200x200 ft"),("Breakwater","floating ring"),
   ("Power","offshore wind + solar"),("Water","desalination")],
  history=("Signature original concept - floating-city lineage from 1970s seasteading proposals, "
   "re-engineered for storm survival and municipal services."),
  how_it_works=("Semi-submersible stabilized platforms linked by flexible bridges; the breakwater "
   "ring attenuates waves; ballast and mooring handle storms. Desalination, waste treatment, and "
   "power are district systems on dedicated utility platforms."),
  materials=["Marine concrete pontoons","Flexible bridge links","Desalination plant","Offshore wind"],
  phases=["Phase 1: breakwater ring and moorings (years 1-2)","Phase 2: utility platforms (years 2-3)",
   "Phase 3: residential pontoons (years 3-5)","Phase 4: civic core (years 5-6)"],
  structures=[("Breakwater Ring",2000,2000),("Utility Platform",400,400),("Residential Pontoon",200,200),("Civic Core",300,300)]),
 dict(name="Signature Desert Solar Belt", group="Energy",
  concept=("A continental solar belt across arid lands: gigawatt-scale PV with co-located "
   "desalination, green-hydrogen electrolysis, and HVDC export - the desert as a power station "
   "that also makes water and fuel."),
  specs=[("Capacity","100 GW target"),("PV area","thousands of sq km"),("Co-products","water, hydrogen"),
   ("Export","HVDC interconnects")],
  history=("Signature original concept - desert-solar lineage from the DESERTEC proposals, rebuilt "
   "with co-located water and fuel so the belt serves its neighbors first."),
  how_it_works=("Single-axis tracker PV in modular blocks; daytime surplus runs reverse-osmosis "
   "desalination and electrolyzers; HVDC lines export firm power. Panel washing uses a fraction "
   "of the desalinated output - the plant waters itself."),
  materials=["PV modules","Trackers","Electrolyzers","RO desalination","HVDC converters"],
  phases=["Phase 1: pilot 1 GW + desalination (years 1-3)","Phase 2: 10 GW + hydrogen (years 3-6)",
   "Phase 3: 100 GW belt + HVDC (years 6-15)"],
  structures=[("PV Block",2000,1000),("Desalination",400,300),("Hydrogen Plant",500,400),("HVDC Station",300,200)]),
 dict(name="Signature Vertical Farm Tower", group="Habitats",
  concept=("A 40-story crop tower producing the vegetables of 1,000 acres on one acre: stacked "
   "hydroponic floors, LED suns tuned per crop, and the building's own waste streams feeding "
   "nutrients back. Farming as architecture."),
  specs=[("Footprint","1 acre"),("Equivalent farmland","1,000 acres"),("Water use","95% less"),
   ("Lighting","tuned LED per crop")],
  history=("Signature original concept - vertical-farm lineage from Dickson Despommier's 2000s "
   "work, engineered for energy honesty: only crops that beat field economics go in the tower."),
  how_it_works=("Crops stacked 30-plus high in hydroponic racks; LED recipes per growth stage; "
   "transpiration water recaptured; the tower's data center waste heat warms the root zones. Only "
   "leafy greens, herbs, and berries - wheat stays in fields."),
  materials=["Hydroponic racks","Tuned LED arrays","Climate envelope","Water recapture","Nutrient systems"],
  phases=["Phase 1: pilot 5 floors (year 1)","Phase 2: full tower (years 2-3)","Phase 3: distribution hub (year 3)"],
  structures=[("Tower 400ft",150,150),("Rack Floors",120,120),("Water Plant",80,60),("Distribution",100,80)]),
 dict(name="Signature Maglev Spine", group="Transport",
  concept=("A 500-mph maglev spine linking the continent's great cities: elevated guideway, "
   "non-contact levitation, city-center stations. The airplane's speed with the train's "
   "punctuality - and a fraction of the energy per seat."),
  specs=[("Speed","500 mph design"),("Guideway","elevated, grade-separated"),("Stations","city centers"),
   ("Energy","per seat-mile below air")],
  history=("Signature original concept - maglev lineage from German Transrapid and Japanese Linimo, "
   "re-planned as a continental spine rather than a showcase line."),
  how_it_works=("Electromagnetic levitation and guidance on an elevated concrete guideway; linear "
   "motors in the guideway propel the train - no onboard engine. City-center stations on viaduct "
   "keep the network in the middle of demand."),
  materials=["Guideway beams","Levitation magnets","Linear motors","Station viaducts"],
  phases=["Phase 1: first city pair (years 1-8)","Phase 2: spine completion (years 8-16)","Phase 3: branches (years 16-25)"],
  structures=[("Guideway 500mi",3000,60),("Station",600,200),("Maintenance Base",800,500),("Viaduct Span",300,60)]),
 dict(name="Signature Lunar Habitat Module", group="Space",
  concept=("A build-ready lunar surface habitat: regolith-shielded pressure modules, closed-loop "
   "life support, and ISRU (in-situ resource utilization) interfaces - designed so the second "
   "mission builds with Moon dirt, not Earth cargo."),
  specs=[("Crew","6"),("Shielding","regolith, 2m+"),("Life support","98% closed loop"),
   ("Power","fission + solar")],
  history=("Signature original concept - lunar-base lineage from 1980s NASA studies, re-engineered "
   "around regolith shielding and ISRU from mission two."),
  how_it_works=("Inflatable or rigid pressure modules buried under regolith for radiation and "
   "micrometeorite shielding; closed-loop water and air; a fission surface power unit for the "
   "lunar night; ISRU pilot plant making oxygen from regolith."),
  materials=["Pressure modules","Regolith shielding","Closed-loop ECLSS","Fission power unit","ISRU plant"],
  phases=["Phase 1: robotic site prep (mission 1)","Phase 2: crewed modules (missions 2-3)",
   "Phase 3: ISRU and expansion (missions 4+)"],
  structures=[("Habitat Cluster",200,150),("Power Unit",100,100),("ISRU Plant",150,120),("Landing Zone",500,500)]),
 dict(name="Signature Orbital Ring Dock", group="Space",
  concept=("A construction dock in low Earth orbit: the shipyard where deep-space vehicles are "
   "assembled from Earth-launched modules - because the rocket equation punishes launching "
   "finished starships from the ground."),
  specs=[("Orbit","LEO, 400 km"),("Dock length","500 m truss"),("Assembly","modular vehicles"),
   ("Crew","rotating 50")],
  history=("Signature original concept - orbital-infrastructure lineage from 1970s space "
   "industrialization studies, scoped as a build-ready dock design."),
  how_it_works=("A 500-meter truss with docking ports, robotic arms, and propellant depot; modules "
   "launch separately and mate at the dock; finished vehicles depart for the Moon, Mars, and "
   "beyond. The dock never lands - it is pure infrastructure."),
  materials=["Truss structure","Docking adapters","Robotic arms","Propellant depot","Habitation module"],
  phases=["Phase 1: core truss and power (launches 1-10)","Phase 2: arms and depot (launches 11-20)",
   "Phase 3: full operations (launch 21+)"],
  structures=[("Truss 500m",500,30),("Docking Hub",80,80),("Propellant Depot",120,60),("Hab Module",60,40)]),
 dict(name="Signature Tidal Lagoon Array", group="Energy",
  concept=("Coastal tidal lagoons generating predictable power: impound the tide behind a low "
   "breakwater, run it through bulb turbines both ways. The Moon's schedule is the most reliable "
   "power forecast on earth."),
  specs=[("Tidal range","8m+ sites"),("Turbines","bidirectional bulb"),("Predictability","100%"),
   ("Co-benefits","flood defense, mariculture")],
  history=("Signature original concept - tidal-range lineage from La Rance (1966), re-imagined as "
   "multi-use lagoons: power, flood defense, and aquaculture in one structure."),
  how_it_works=("A breakwater ring impounds a coastal lagoon; turbines generate on both ebb and "
   "flood; the lagoon doubles as a storm-surge barrier and a sheltered mariculture zone. Power "
   "is forecast years ahead - the grid's dream."),
  materials=["Breakwater","Bulb turbines","Sluices","Mariculture systems"],
  phases=["Phase 1: pilot lagoon (years 1-5)","Phase 2: array of 5 (years 5-12)","Phase 3: grid integration (year 12+)"],
  structures=[("Lagoon",3000,2000),("Turbine House",400,150),("Breakwater",4000,100),("Mariculture",1000,800)]),
 dict(name="Signature Geothermal City Grid", group="Energy",
  concept=("A city heated and powered from below: deep geothermal wells feeding a district grid - "
   "baseload renewable energy with a footprint of acres, not miles. Where the geology allows, "
   "nothing beats it."),
  specs=[("Depth","3-5 km wells"),("Output","baseload electric + heat"),("Footprint","acres"),
   ("District","heating + cooling")],
  history=("Signature original concept - geothermal-district lineage from Iceland's century of "
   "practice, engineered for sedimentary-basin cities with enhanced geothermal."),
  how_it_works=("Deep wells tap hot rock; binary-cycle plants generate electricity; waste heat feeds "
   "a district heating/cooling loop under the streets. One well field serves the whole downtown - "
   "the power plant is invisible."),
  materials=["Deep wells","Binary plants","District piping","Heat exchangers"],
  phases=["Phase 1: exploration wells (years 1-2)","Phase 2: plant + downtown loop (years 2-5)",
   "Phase 3: city-wide grid (years 5-10)"],
  structures=[("Well Field",800,600),("Power Plant",300,200),("District Loop",3000,60),("Peaking Station",150,100)]),
 dict(name="Signature Skybridge Network", group="Transport",
  concept=("A second-story pedestrian city: climate-controlled skybridges linking towers into a "
   "walkable network above the traffic - Minneapolis skyways and Calgary Plus-15 rebuilt as a "
   "planned system, not an accident."),
  how_it_works=("Enclosed bridges at the second/third floor connect every major building; the "
   "network is heated, cooled, and accessible; street level returns to transit, bikes, and "
   "green. Winter cities become walkable year-round."),
  specs=[("Level","+2/+3 floors"),("Climate","conditioned"),("Access","step-free everywhere"),
   ("Coverage","downtown core")],
  history=("Signature original concept - skyway lineage from Minneapolis (1960s) and Calgary, "
   "planned as one network with civic design standards."),
  materials=["Enclosed bridge spans","Tower connection nodes","Wayfinding systems","Accessibility lifts"],
  phases=["Phase 1: core loop (years 1-3)","Phase 2: district branches (years 3-6)","Phase 3: full network (years 6-10)"],
  structures=[("Bridge Span",300,20),("Connection Node",60,60),("Core Loop",2000,1500),("Branch",1000,20)]),
 dict(name="Signature Amphibious Housing District", group="Habitats",
  concept=("A flood-plain neighborhood that floats: houses on amphibious foundations rest on the "
   "ground normally and rise with floodwater on guide piles - Dutch innovation scaled to a whole "
   "district with shared utilities on flexible connections."),
  specs=[("Lift","up to 12 ft"),("Guides","steel piles"),("Utilities","flexible connections"),
   ("Normal state","grounded houses")],
  history=("Signature original concept - amphibious-housing lineage from Dutch Maasbommel "
   "prototypes, engineered as district infrastructure with utility resilience."),
  how_it_works=("Each house sits on a buoyant foundation within vertical guide piles; floodwater "
   "lifts the house, guides keep it positioned; utilities connect through flexible umbilicals. "
   "When water recedes, houses settle home."),
  materials=["Buoyant foundations","Guide piles","Flexible utility umbilicals","Flood-proof materials"],
  phases=["Phase 1: pilot street (years 1-2)","Phase 2: district build (years 2-5)","Phase 3: utility hardening (years 5-6)"],
  structures=[("House Plot",80,60),("Guide Piles",40,40),("Utility Spine",800,20),("Community Dock",200,60)]),
 dict(name="Signature Carbon-Capture Tower", group="Energy",
  concept=("A direct-air-capture tower integrated into the city: fans, sorbent contactors, and "
   "mineralization in one vertical plant that eats the skyline's own emissions - carbon removal "
   "as civic infrastructure."),
  specs=[("Capture","100,000 tCO2/yr per tower"),("Energy","dedicated clean power"),
   ("Storage","mineralization"),("Footprint","city block")],
  history=("Signature original concept - DAC lineage from 2000s research, packaged as urban "
   "infrastructure co-located with the emissions it offsets."),
  how_it_works=("Giant fans draw air through solid-sorbent contactors; low-grade heat regenerates "
   "the sorbent; captured CO2 mineralizes into building aggregate - the tower literally builds "
   "the city from the sky."),
  materials=["Contactor arrays","Sorbent systems","Mineralization plant","Heat integration"],
  phases=["Phase 1: pilot tower (years 1-3)","Phase 2: 10-tower district (years 3-7)","Phase 3: city scale (years 7-12)"],
  structures=[("Tower 300ft",200,200),("Contactor Banks",300,150),("Mineralization",200,150),("Aggregate Yard",300,200)]),
 dict(name="Signature Hyperloop Corridor", group="Transport",
  concept=("A sealed-tube corridor for 700-mph pods: vacuum-reduced tubes on pylons, linear "
   "propulsion, city-pair service. The engineering is specified end-to-end - tube, pods, "
   "stations, safety - as one build-ready package."),
  specs=[("Speed","700 mph design"),("Tube","low-pressure steel"),("Pods","28 passengers"),
   ("Headway","minutes")],
  history=("Signature original concept - vactrain lineage from 1970s Rand studies through the "
   "2010s hyperloop proposals, engineered conservatively: proven subsystems only."),
  how_it_works=("Steel tubes at 1/1000 atmosphere on concrete pylons; pods levitate and propel by "
   "linear motors; stations are airlocks with pod maintenance. Emergency egress and re- "
   "pressurization are designed in, not added later."),
  materials=["Steel tube sections","Concrete pylons","Linear motors","Airlock stations","Pod fleet"],
  phases=["Phase 1: test track (years 1-4)","Phase 2: first corridor (years 4-10)","Phase 3: network (years 10-20)"],
  structures=[("Tube 300mi",2000,40),("Station Airlock",400,150),("Pylon Line",2000,20),("Maintenance",600,400)]),
 dict(name="Signature Stratospheric Relay Platform", group="Space",
  concept=("A solar airship stationed at 65,000 feet as a communications and observation relay: "
   "above weather, below orbit - the stratosphere's sweet spot for persistent coverage of a "
   "region."),
  specs=[("Altitude","65,000 ft"),("Endurance","months"),("Payload","comms + sensors"),
   ("Coverage","regional")],
  history=("Signature original concept - HAPS lineage from 1990s Helios and modern Airbus Zephyr, "
   "specified as a build-ready relay platform."),
  how_it_works=("A solar-powered airship holds station in the stratospheric winds; photovoltaic "
   "skin charges batteries for the night; payload relays communications and imagery to the "
   "region below. Launch, station-keep, recover, refurbish - an aircraft's lifecycle."),
  materials=["Envelope","PV skin","Batteries","Payload module","Ground station"],
  phases=["Phase 1: prototype flights (years 1-3)","Phase 2: operational relay (years 3-5)","Phase 3: constellation (years 5-8)"],
  structures=[("Airship 300ft",300,80),("Ground Station",200,150),("Hangar",400,200),("Payload Bay",60,40)]),
 dict(name="Signature Deep-Sea Research Station", group="Research",
  concept=("A permanent crewed station on the continental shelf at 500 meters: saturation habitat, "
   "moon pool, and ROV hangar - the ocean's equivalent of the space station, built from proven "
   "saturation-diving and subsea technology."),
  specs=[("Depth","500 m"),("Crew","12"),("Endurance","months"),("Access","DSV + ROV")],
  history=("Signature original concept - undersea-habitat lineage from Cousteau's Conshelf (1960s), "
   "rebuilt with modern saturation and ROV practice."),
  how_it_works=("A pressure hull on the seabed at saturation depth; divers work from the moon pool "
   "at ambient pressure; ROVs extend reach; a surface support ship handles logistics. Power and "
   "data via umbilical; life support closes the loops."),
  materials=["Pressure hull","Saturation systems","Moon pool","ROV hangar","Umbilical"],
  phases=["Phase 1: uncrewed test (years 1-3)","Phase 2: crewed station (years 3-6)","Phase 3: science program (year 6+)"],
  structures=[("Habitat Hull",120,40),("Moon Pool",40,40),("ROV Hangar",60,40),("Support Ship",300,60)]),
 dict(name="Signature Mountain Tunnel City", group="Habitats",
  concept=("A city inside the mountain: excavated caverns for housing, industry, and farms beneath "
   "a national park - the surface stays wild while the city lives in engineered rock with "
   "daylight piped in. The Norwegian and Swiss bunkers, rebuilt as a city."),
  specs=[("Population","30,000"),("Cover","200m+ rock"),("Daylight","heliostat piped"),
   ("Climate","geothermal stable")],
  history=("Signature original concept - underground-city lineage from Cold War bunkers and "
   "Coober Pedy, designed as a complete city, not a shelter."),
  how_it_works=("Parallel caverns for districts, cross-connected; heliostats and light pipes bring "
   "daylight deep; the rock's thermal mass stabilizes climate; a single hardened portal cluster "
   "handles all access. Excavation is drill-and-blast and TBM at city scale."),
  materials=["Cavern linings","Heliostat arrays","Light pipes","Ventilation","District systems"],
  phases=["Phase 1: access tunnels and first cavern (years 1-5)","Phase 2: districts (years 5-12)","Phase 3: full city (years 12-20)"],
  structures=[("Main Cavern",2000,300),("District Cavern",1500,250),("Portal Cluster",500,300),("Heliostat Field",800,600)]),
 dict(name="Signature River Restoration Weir System", group="Water",
  concept=("A river restored by engineered weirs: rock-arch rapids replacing drowned dams - "
   "fish passage, whitewater, floodplain reconnection, and hydropower in one structure. The dam "
   "comes down; the river comes back, better instrumented."),
  specs=[("Drop","staged rapids"),("Fish passage","100%"),("Power","low-head hydro"),
   ("Floodplain","reconnected")],
  history=("Signature original concept - dam-removal lineage from 2000s river restoration, "
   "engineered as a replacement system, not just demolition."),
  how_it_works=("The dam is replaced by a series of rock weirs forming rapids; fish swim the "
   "rapids; kayakers play them; low-head turbines in the weirs generate power; the floodplain "
   "reconnects at high water. Sensors monitor fish, flow, and water quality."),
  materials=["Rock weirs","Low-head turbines","Fish monitoring","Floodplain earthworks"],
  phases=["Phase 1: pilot reach (years 1-3)","Phase 2: dam replacement (years 3-6)","Phase 3: monitoring (year 6+)"],
  structures=[("Weir Series",1500,200),("Turbine Bays",200,80),("Floodplain",2000,800),("Monitoring",100,60)]),
 dict(name="Signature Sky Garden Viaduct", group="Transport",
  concept=("A rail viaduct that is also a park: trains run below, a linear garden runs on top - "
   "the High Line's idea applied to new infrastructure from day one, so the viaduct gives back "
   "more public space than it takes."),
  specs=[("Deck","dual: rail + park"),("Park width","30 ft"),("Length","corridor scale"),
   ("Access","every half mile")],
  history=("Signature original concept - linear-park lineage from New York's High Line (2009), "
   "designed into new viaducts rather than retrofitted."),
  how_it_works=("A concrete rail viaduct carries tracks; its roof deck - engineered for soil, "
   "drainage, and trees - carries a public linear park with ramps every half mile. The park "
   "cools the corridor and pays the viaduct's social license."),
  materials=["Viaduct structure","Park deck system","Soil and planting","Drainage","Access ramps"],
  phases=["Phase 1: viaduct + park pilot (years 1-4)","Phase 2: corridor build (years 4-9)"],
  structures=[("Viaduct 5mi",2500,60),("Park Deck",2500,40),("Access Ramp",200,40),("Station",400,150)]),
 dict(name="Signature Modular Hospital Ship", group="Habitats",
  concept=("A hospital ship built from modules: a converted hull (or newbuild) carrying containerized "
   "operating theaters, wards, and labs - disaster and remote-area surgery that sails to the "
   "patient."),
  specs=[("Beds","500"),("ORs","12 modular"),("Speed","18 knots"),("Endurance","60 days")],
  history=("Signature original concept - hospital-ship lineage from the Mercy-class, re-imagined "
   "modular: containerized medical units that swap by crane."),
  how_it_works=("Standard hull with a modular medical deck: OR, ICU, ward, and lab modules in "
   "container frames, craned aboard per mission; helicopter deck; the ship's utilities (power, "
   "water, medical gas) plug into every module slot."),
  materials=["Hull","Medical modules","Helicopter deck","Utility plug-in systems"],
  phases=["Phase 1: hull + core modules (years 1-3)","Phase 2: full module set (years 3-4)","Phase 3: operations (year 4+)"],
  structures=[("Hull 800ft",800,100),("Medical Deck",600,90),("Helo Deck",150,150),("Module Yard",400,200)]),
 dict(name="Signature Disaster-Relief Rapid Shelter", group="Habitats",
  concept=("A shelter that deploys in hours: flat-packed insulated panels, tool-free assembly by "
   "unskilled crews, rated for the climate it's sent to - the tent's replacement, engineered "
   "like a product."),
  specs=[("Deploy","4 hours, 6 people"),("Rating","per climate zone"),("Life","5 years"),
   ("Pack","flat, 40 per container")],
  history=("Signature original concept - emergency-shelter lineage from UNHCR tents, engineered as "
   "a real product with climate variants."),
  how_it_works=("Insulated composite panels pin together without tools; the floor is the shipping "
   "pallet; a stove jack, solar vent, and water catchment are standard. Variants for hot, cold, "
   "and wet climates share the same joint system."),
  materials=["Composite panels","Pallet floors","Solar vents","Stove jacks"],
  phases=["Phase 1: prototype + field test (year 1)","Phase 2: production (year 2)","Phase 3: stockpile (year 3)"],
  structures=[("Shelter 200sqft",20,14),("Panel Stack",8,6),("Container 40 units",40,8),("Camp Layout",400,300)]),
 dict(name="Signature Desert Greenhouse Belt", group="Habitats",
  concept=("Seawater greenhouses in the desert: evaporative cooling grows crops where nothing grew, "
   "and the process distills fresh water as a byproduct. The Sahara Forest Project's idea, "
   "engineered as a build-ready belt."),
  specs=[("Cooling","seawater evaporative"),("Water","net producer"),("Crops","vegetables, forage"),
   ("Power","solar")],
  history=("Signature original concept - seawater-greenhouse lineage from 1990s Tenerife pilots and "
   "the Jordan Sahara Forest project, scaled as a belt."),
  how_it_works=("Seawater trickles over front evaporator pads, cooling and humidifying incoming air; "
   "crops grow in the cool humid house; at the back, condensers recover fresh water. Solar powers "
   "pumps and fans."),
  materials=["Greenhouse structures","Evaporator pads","Condensers","Solar arrays","Hydroponics"],
  phases=["Phase 1: pilot hectares (years 1-2)","Phase 2: belt build (years 2-6)"],
  structures=[("Greenhouse Block",500,300),("Seawater Intake",200,100),("Solar Field",400,300),("Packhouse",150,100)]),
 dict(name="Signature Floating Solar Island", group="Energy",
  concept=("Solar on water: floating PV on reservoirs and coastal lagoons - no land use, cooler "
   "panels (higher output), and reduced evaporation. The island is moored, cabled, and serviced "
   "like a small offshore platform."),
  specs=[("Capacity","100 MW per island"),("Cooling","+5-10% output"),("Evaporation","-70%"),
   ("Mooring","catenary")],
  history=("Signature original concept - floating-PV lineage from 2000s Japanese and Korean pilots, "
   "engineered as standardized islands."),
  how_it_works=("HDPE float platforms carry tilted PV; the water cools the panels; mooring handles "
   "wind and waves; subsea cable lands power ashore. Anchoring and O&M access are the marine "
   "engineering."),
  materials=["Float platforms","PV modules","Mooring systems","Subsea cable","O&M boats"],
  phases=["Phase 1: pilot island (years 1-2)","Phase 2: 10 islands (years 2-5)"],
  structures=[("Island",800,600),("Mooring Field",1200,1000),("Cable Landing",200,100),("O&M Dock",150,60)]),
 dict(name="Signature Underground Freight Tube", group="Transport",
  concept=("Freight in tubes beneath the city: automated electric capsules moving parcels and "
   "pallets under congested streets - the pneumatic tube's great-grandchild, sized for the "
   "e-commerce age."),
  specs=[("Capsule","pallet-scale"),("Speed","60 mph"),("Network","hub and spoke"),
   ("Power","electric")],
  history=("Signature original concept - freight-pipeline lineage from 19th-century pneumatic tubes, "
   "rebuilt at pallet scale with modern automation."),
  how_it_works=("A bored tunnel network with linear-motor capsules; hubs at warehouses and district "
   "depots; capsules route automatically like packets. Surface trucks handle only the last mile."),
  materials=["Tunnel bores","Linear motors","Capsule fleet","Hub terminals"],
  phases=["Phase 1: pilot pair (years 1-4)","Phase 2: city network (years 4-10)"],
  structures=[("Tunnel 10mi",1500,25),("Hub Terminal",400,300),("Capsule",12,8),("Portal",100,60)]),
 dict(name="Signature Smart Levee System", group="Water",
  concept=("A levee that thinks: instrumented embankments with fiber-optic strain sensing, "
   "automated floodgates, and a digital twin that predicts failure before it happens - the "
   "Mississippi's levees rebuilt as a sensing machine."),
  specs=[("Sensing","fiber per mile"),("Gates","automated"),("Twin","real-time model"),
   ("Warning","hours ahead")],
  history=("Signature original concept - smart-infrastructure lineage from 2010s sensor "
   "deployments, specified as a complete levee system."),
  how_it_works=("Distributed fiber senses strain, seepage, and temperature along every mile; "
   "automated gates and pumps respond to the digital twin's forecasts; the system warns hours "
   "before a human inspector could see trouble."),
  materials=["Levee embankments","Fiber sensing","Automated gates","Digital twin","Pumps"],
  phases=["Phase 1: pilot reach (years 1-3)","Phase 2: system build (years 3-8)"],
  structures=[("Levee Mile",5280,60),("Gate Structure",100,60),("Pump Station",80,60),("Control Center",100,80)]),
 dict(name="Signature Elevated Forest Walkway City", group="Habitats",
  concept=("A city in the canopy: elevated walkways and treehouse districts threaded through a "
   "protected forest - housing, schools, and workshops at canopy level, the forest floor "
   "untouched below. Ecotourism's walkways, grown into a town."),
  specs=[("Level","canopy, 60-100 ft"),("Footprint","forest intact"),("Access","walkway network"),
   ("Structures","treehouse")],
  history=("Signature original concept - canopy-walkway lineage from ecotourism parks, designed as "
   "permanent habitation with forest ecology as the client."),
  how_it_works=("Tension walkways span between engineered treehouse platforms; buildings hang light "
   "on the forest - helical piles, no clear-cutting; the ground stays wild. Canopy-level living "
   "with the forest as the neighborhood."),
  materials=["Walkway spans","Treehouse platforms","Helical piles","Canopy utilities"],
  phases=["Phase 1: pilot cluster (years 1-3)","Phase 2: district (years 3-7)"],
  structures=[("Walkway Mile",5280,12),("Platform Cluster",200,150),("Commons Deck",100,80),("Ground Preserve",2000,1500)]),
 dict(name="Signature Polar Research Dome", group="Research",
  concept=("A year-round polar research station under one geodesic dome: labs, habitation, and "
   "vehicle bays in a climate-controlled village - the Antarctic station rebuilt so scientists "
   "walk to work in shirtsleeves at minus 60 outside."),
  specs=[("Dome","200 ft span"),("Crew","100"),("Temp inside","65F year-round"),
   ("Power","wind + nuclear battery")],
  history=("Signature original concept - polar-station lineage from Amundsen-Scott South Pole "
   "station, re-imagined as a single domed village."),
  how_it_works=("A geodesic dome on a raised foundation encloses the station village; snow "
   "management (the dome sheds it) and elevated structures handle drift; wind turbines and a "
   "microreactor power the science through the polar night."),
  materials=["Geodesic dome","Elevated modules","Wind turbines","Microreactor","Snow management"],
  phases=["Phase 1: summer construction (seasons 1-3)","Phase 2: winter commissioning (season 4)"],
  structures=[("Dome 200ft",200,200),("Lab Modules",150,100),("Power Plant",100,80),("Vehicle Bay",120,80)]),
 dict(name="Signature Volcano Geothermal Plant", group="Energy",
  concept=("Power from the volcano's edge: wells drilled into high-temperature fields beside "
   "active volcanoes, built to survive eruptions - Iceland's practice taken to the most extreme "
   "geology on earth."),
  specs=[("Resource","300C+ fields"),("Wells","directional, cased"),("Output","100 MW+"),
   ("Hazard","eruption-rated")],
  history=("Signature original concept - volcanic-geothermal lineage from Iceland's Krafla and "
   "Hellisheidi plants, engineered for eruption exposure."),
  how_it_works=("Directional wells tap superheated zones; the plant is sited and armored for lava, "
   "ash, and gas; wellheads can be sacrificed - the field survives even if a pad doesn't. "
   "Corrosion-resistant alloys throughout."),
  materials=["High-temp wells","Corrosion alloys","Armored plant","Gas handling"],
  phases=["Phase 1: exploration (years 1-3)","Phase 2: plant (years 3-6)"],
  structures=[("Well Pads",400,300),("Power Plant",300,200),("Steam Field",800,600),("Control Bunker",100,80)]),
 dict(name="Signature Wave-Energy Breakwater", group="Energy",
  concept=("A breakwater that pays for itself: wave-energy converters built into harbor protection - "
   "the port gets calm water, the grid gets power, and the structure earns its keep twice."),
  specs=[("Converters","overtopping or flap"),("Power","per km of breakwater"),
   ("Protection","harbor-grade"),("Life","50 years")],
  history=("Signature original concept - wave-energy lineage from 2000s pilot devices, integrated "
   "into breakwaters so the civil structure carries the economics."),
  how_it_works=("The breakwater's seaward face carries overtopping reservoirs or oscillating flaps; "
   "waves pump water or drive hydraulics; the harbor behind stays calm. Maintenance from the "
   "breakwater crest - no offshore vessels needed."),
  materials=["Breakwater caissons","Wave converters","Hydraulics","Grid connection"],
  phases=["Phase 1: pilot section (years 1-4)","Phase 2: full breakwater (years 4-8)"],
  structures=[("Breakwater 2km",6500,100),("Converter Bays",500,80),("Crest Road",6500,30),("Substation",100,80)]),
 dict(name="Signature Sky Farm Ziggurat", group="Habitats",
  concept=("A stepped pyramid of farms: each terrace a different crop zone, the whole ziggurat a "
   "vertical watershed - rain captured at the crown irrigates every level by gravity. Ancient "
   "form, modern agronomy."),
  specs=[("Terraces","12 levels"),("Water","gravity-fed"),("Crops","zoned by level"),
   ("Footprint","city block")],
  history=("Signature original concept - terrace-farming lineage from Incan and Ifugao terraces, "
   "stacked as a single engineered structure."),
  how_it_works=("Twelve terraced levels step back to a crown cistern; captured rain and recycled "
   "water feed down by gravity; each terrace's microclimate suits its crop - rice at the wet "
   "base, herbs at the windy crown."),
  materials=["Terrace structure","Crown cistern","Gravity irrigation","Crop zones"],
  phases=["Phase 1: base terraces (years 1-2)","Phase 2: full ziggurat (years 2-4)"],
  structures=[("Ziggurat 200ft",300,300),("Terraces",250,250),("Crown Cistern",80,80),("Base Market",200,150)]),
 dict(name="Signature Community Microgrid Hub", group="Energy",
  concept=("The neighborhood power plant: a community microgrid hub with solar, batteries, and "
   "backup generation that islands gracefully when the grid fails - resilience as a shared "
   "utility, not a private generator."),
  specs=[("Capacity","5 MW / 20 MWh"),("Island time","72 hours"),("Members","2,000 homes"),
   ("Solar","rooftop aggregated")],
  history=("Signature original concept - microgrid lineage from post-Sandy New Jersey and "
   "California PSPS responses, packaged as a replicable hub."),
  how_it_works=("Rooftop solar aggregated across the neighborhood feeds a central battery hall; the "
   "hub islands automatically on grid failure; critical loads (clinic, grocery, water pumps) get "
   "priority circuits. Members buy resilience by subscription."),
  materials=["Battery hall","Solar aggregation","Island switchgear","Priority circuits"],
  phases=["Phase 1: hub + critical loads (year 1)","Phase 2: full membership (years 2-3)"],
  structures=[("Hub Building",120,80),("Battery Hall",80,60),("Solar Canopy",200,150),("Critical Loads",300,200)]),
 dict(name="Signature Elevated Transit Podway", group="Transport",
  concept=("Personal rapid transit, finally built right: small automated pods on a lightweight "
   "elevated guideway, stations every half mile, no waiting - the Morgantown PRT (1975, still "
   "running) scaled to a city network."),
  specs=[("Pods","4 passengers"),("Headway","seconds"),("Guideway","lightweight elevated"),
   ("Stations","every 0.5 mi")],
  history=("Signature original concept - PRT lineage from Morgantown's 1975 system, re-engineered "
   "with modern automation and a real network plan."),
  how_it_works=("Four-passenger pods run on demand on a slim elevated guideway; offline stations let "
   "express pods bypass; the guideway is light enough for tight urban corridors. You board "
   "immediately - the pod waits for you, not vice versa."),
  materials=["Guideway beams","Pod fleet","Offline stations","Control system"],
  phases=["Phase 1: pilot loop (years 1-4)","Phase 2: city network (years 4-10)"],
  structures=[("Guideway 10mi",1500,25),("Station",120,60),("Pod",12,7),("Maintenance",300,200)]),
 dict(name="Signature Rewilding Corridor Bridges", group="Research",
  concept=("Wildlife crossings at continental scale: a network of vegetated overpasses reconnecting "
   "fragmented habitats - the Banff crossings proven over 25 years, scaled into a system that "
   "lets migration routes function again."),
  specs=[("Width","150 ft vegetated"),("Spacing","per migration data"),("Monitoring","camera + DNA"),
   ("Target","apex species")],
  history=("Signature original concept - wildlife-crossing lineage from Banff's 1990s overpasses, "
   "planned as a continental network from migration science."),
  how_it_works=("Wide vegetated bridges span highways at documented crossing points; fencing funnels "
   "animals to the bridges; cameras and eDNA monitor use; the network is managed adaptively - "
   "crossings move as herds shift."),
  materials=["Bridge structures","Native vegetation","Fencing","Monitoring systems"],
  phases=["Phase 1: priority crossings (years 1-3)","Phase 2: network build (years 3-10)"],
  structures=[("Crossing",200,180),("Fencing Mile",5280,10),("Monitoring",60,40),("Corridor",5000,500)]),
 dict(name="Signature Atmospheric Water Farm", group="Water",
  concept=("Water from air at scale: arrays of atmospheric water generators - condensation and "
   "sorption - producing drinking water where there is no aquifer. The dehumidifier, engineered "
   "as infrastructure."),
  specs=[("Output","10,000 L/day per array"),("Energy","solar"),("Humidity","works at 20%+ RH"),
   ("Quality","mineralized")],
  history=("Signature original concept - AWG lineage from military and off-grid units, scaled as "
   "a municipal water source."),
  how_it_works=("Sorption materials pull water from air even at low humidity; solar heat releases "
   "it; condensation collects it; mineralization makes it taste like spring water. Arrays scale "
   "linearly - water by the acre."),
  materials=["Sorption arrays","Solar thermal","Condensation","Mineralization","Storage"],
  phases=["Phase 1: pilot array (year 1)","Phase 2: municipal scale (years 2-4)"],
  structures=[("Array Field",400,300),("Solar Thermal",300,200),("Storage Tanks",150,100),("Distribution",200,150)]),
 dict(name="Signature Orbital Solar Farm", group="Space",
  concept=("Power from orbit: a kilometer-scale photovoltaic array beaming energy to Earth via "
   "microwaves - the 1968 Peter Glaser concept, specified with modern PV, phased-array "
   "transmission, and robotic assembly."),
  specs=[("Array","1 km class"),("Beaming","microwave, retrodirective"),("Ground","rectenna farm"),
   ("Output","GW class")],
  history=("Signature original concept - space-solar lineage from Glaser's 1968 NASA study, "
   "re-specified with current PV and assembly robotics."),
  how_it_works=("A vast PV array in geostationary orbit collects constant sunlight; phased-array "
   "antennas beam microwaves to a ground rectenna; a pilot signal guarantees the beam can't "
   "wander. Robotic assembly builds the array from launched modules."),
  materials=["PV array","Phased-array transmitter","Rectenna","Assembly robots"],
  phases=["Phase 1: pilot beaming demo (years 1-5)","Phase 2: MW pilot plant (years 5-12)","Phase 3: GW farm (years 12-25)"],
  structures=[("Array 1km",1000,1000),("Transmitter",300,300),("Rectenna 5km",5000,5000),("Assembly Dock",400,200)]),
]
