#!/usr/bin/env python3
"""Topics + config for the geological-subsurface-data pair. Property of Justin Addam Higgins (JAH)."""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

CFG = {
    "slug": "geological-subsurface-data",
    "name_pub": "The Geological Subsurface Data Database",
    "name_sig": "Signature Geological Subsurface Data Database",
    "tagline_pub": ("Geological subsurface data from the ground up: borehole logs, strata "
                    "columns, geophysical surveys, 3D geological models, and subsurface "
                    "stewardship - every record carrying the full entry taught progressively "
                    "along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of geological subsurface data: "
                    "the same real subsurface knowledge carried forward, plus Signature-built "
                    "modeling pipelines, survey frameworks, and data systems original to this "
                    "system."),
    "record_kind": "geological subsurface data record",
    "record_kind_plural": "geological subsurface data records",
    "prefix_pub": "JAH-SUBG-", "prefix_sig": "JAH-SUBGS-",
    "ai_pub": "JAH Geological Subsurface Data Archivist",
    "ai_sig": "JAH Signature Geological Subsurface Data Creator",
    "role_pub": ("geological subsurface data archivist - teaching boreholes, strata, geophysical "
                 "surveys, 3D models, and data stewardship; answers from many angles - "
                 "definition, example, process, interpretation, stewardship - using only archive "
                 "data from this system"),
    "role_sig": ("Signature creator of geological subsurface data systems - designing modeling "
                 "pipelines, survey frameworks, and data systems as original Signature works; "
                 "answers from many angles using only archive data from this system"),
    "search_ph": "Search boreholes, strata, surveys, 3D models, geophysics...",
    "chat_ph": "Ask about geological subsurface data...",
    "greet_pub": ("I am the JAH Geological Subsurface Data Archivist. Ask me about borehole "
                  "logs, strata columns, geophysical surveys, and 3D geological models."),
    "greet_sig": ("I am the JAH Signature Geological Subsurface Data Creator. Ask me about "
                  "Signature-built subsurface data systems."),
    "gen_blurb": ("Generate clearly-labeled geological subsurface studies. Seeded archive "
                  "records are the authoritative entries."),
    "about_archive": ("Seeded geological subsurface data records, marching toward one million "
                      "records. Presented in teaching-ladder order: foundations, compounded, "
                      "advanced."),
    "demo_kind": "subsurface-demo",
    "demo_title": "Geological Subsurface Demo",
    "health": False,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Geological Subsurface Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "column":
        return fill(
            "layers = @@LAYERS@@\n"
            "print('Stratigraphic column (top to bottom):')\n"
            "total = 0.0\n"
            "for L in layers:\n"
            "    total += L['thick']\n"
            "    bar = '#' * max(1, int(L['thick']))\n"
            "    print(' %6.1fm %-22s %s' % (L['thick'], L['unit'], bar))\n"
            "print('Total logged thickness: %.1f m' % total)\n",
            {"LAYERS": p["layers"]})
    if v == "logstat":
        return fill(
            "readings = @@READINGS@@\n"
            "n = len(readings)\n"
            "mean = sum(readings) / n\n"
            "var = sum((x - mean) ** 2 for x in readings) / n\n"
            "print('Borehole log statistics:')\n"
            "print(' Samples:', n)\n"
            "print(' Min: %.2f  Max: %.2f  Mean: %.2f' % (min(readings), max(readings), mean))\n"
            "print(' Std dev: %.2f' % var ** 0.5)\n",
            {"READINGS": p["readings"]})
    if v == "volume":
        return fill(
            "nx, ny, nz = @@DIMS@@\ncell = @@CELL@@\n"
            "fill = @@FILL@@\n"
            "cells = nx * ny * nz\n"
            "rock = int(cells * fill)\n"
            "vol = rock * (cell ** 3)\n"
            "print('3D model grid: %d x %d x %d = %d cells' % (nx, ny, nz, cells))\n"
            "print('Rock-filled cells: %d (%.1f%%)' % (rock, 100.0 * fill))\n"
            "print('Rock volume: %.1f cubic units' % vol)\n",
            {"DIMS": p["dims"], "CELL": p["cell"], "FILL": p["fill"]})
    if v == "survey":
        return fill(
            "stations = @@STATIONS@@\n"
            "vals = [s['value'] for s in stations]\n"
            "n = len(vals)\n"
            "mean = sum(vals) / n\n"
            "print('Geophysical survey line: %d stations' % n)\n"
            "print(' Mean: %.2f  Range: %.2f - %.2f' % (mean, min(vals), max(vals)))\n"
            "anom = [s for s in stations if abs(s['value'] - mean) > @@TOL@@]\n"
            "print(' Anomalous stations (>%.1f from mean): %d' % (@@TOL@@, len(anom)))\n"
            "for s in anom:\n"
            "    print('  station %s: %.2f' % (s['id'], s['value']))\n",
            {"STATIONS": p["stations"], "TOL": p["tol"]})
    if v == "correlate":
        return fill(
            "holes = @@HOLES@@\n"
            "print('Borehole correlation:')\n"
            "units = {}\n"
            "for h in holes:\n"
            "    print(' ' + h['id'] + ':', ', '.join(u['unit'] for u in h['units']))\n"
            "    for u in h['units']:\n"
            "        units.setdefault(u['unit'], []).append(h['id'])\n"
            "print('Units traced across holes:')\n"
            "for u, hs in units.items():\n"
            "    if len(hs) > 1:\n"
            "        print(' %s: %s' % (u, ', '.join(hs)))\n",
            {"HOLES": p["holes"]})
    raise ValueError("unknown demo variant " + v)


TOPICS = [
dict(title="What Geological Subsurface Data Is", tier=F,
 desc_pub=("Geological subsurface data describes what lies beneath the Earth's surface: "
  "borehole logs (direct observations from drilled holes), geophysical surveys (indirect "
  "measurements - seismic, gravity, magnetic, electrical), and the 3D models built by "
  "combining them.\n"
  "It underpins groundwater management, construction, mining, energy, carbon storage, and "
  "hazard assessment. Subsurface data is expensive to acquire - every meter drilled costs - "
  "so archives that preserve and share it multiply its value."),
 desc_sig=("The Signature system treats subsurface data as a permanent public asset: every "
  "borehole and survey archived with lineage, so no meter drilled is ever wasted."),
 how_pub=("Data comes from drilling (cuttings, cores, wireline logs), surface geophysics, and "
  "existing archives. Geologists interpret measurements into stratigraphy and structure, "
  "then build 2D/3D models. Archives preserve raw data plus interpretations."),
 how_sig=("Signature archive-first practice ensures every subsurface measurement is "
  "preserved with its interpretation lineage."),
 keys=["Boreholes: direct observation",
  "Geophysics: indirect measurement",
  "3D models combine both",
  "Groundwater, construction, mining, energy, hazards",
  "Drilling is expensive; archives multiply value",
  "Raw data + interpretations preserved"],
 reqs=["Drilling and survey capability",
  "Geological interpretation",
  "Data archiving"],
 stds=["Geological data standards (public, e.g., GeoSciML)"],
 cites=["U.S. Geological Survey — public resources (public)",
  "British Geological Survey — public data (public)"],
 demo=("column", {"layers": [
   {"unit": "Topsoil", "thick": 1.5}, {"unit": "Sand", "thick": 8.0},
   {"unit": "Clay", "thick": 12.0}, {"unit": "Sandstone", "thick": 25.0},
   {"unit": "Shale", "thick": 18.0}, {"unit": "Limestone", "thick": 30.0}]})),

dict(title="Rock Types and the Rock Cycle", tier=F,
 desc_pub=("Rocks sort into three families: igneous (cooled magma - granite, basalt), "
  "sedimentary (compacted sediments - sandstone, shale, limestone), and metamorphic "
  "(transformed by heat/pressure - marble, slate). The rock cycle transforms each into the "
  "others over geologic time.\n"
  "Subsurface work mostly meets sedimentary rocks - layered, porous, hosting water, oil, and "
  "gas - plus the igneous basement below and metamorphic terrains in old shields."),
 desc_sig=("Signature rock-property catalogs attach typical physical properties to each rock "
  "family, so modelers start from informed defaults."),
 how_pub=("Geologists identify rocks from cuttings, cores, and outcrops - texture, "
  "mineralogy, fossils - and classify per standard schemes. Properties (porosity, "
  "permeability, strength) are measured or estimated from the type."),
 how_sig=("Signature property catalogs give modelers informed starting values per rock "
  "type."),
 keys=["Igneous, sedimentary, metamorphic",
  "Rock cycle transforms over time",
  "Sedimentary: layered, porous, hosts fluids",
  "Identify via texture, mineralogy, fossils",
  "Properties follow from type",
  "Standard classification schemes"],
 reqs=["Rock identification skill",
  "Classification references",
  "Property measurement"],
 stds=["Geological classification standards (public)"],
 cites=["U.S. Geological Survey — rock classification (public)"],
 demo=("column", {"layers": [
   {"unit": "Granite (igneous)", "thick": 50.0},
   {"unit": "Sandstone (sedimentary)", "thick": 20.0},
   {"unit": "Marble (metamorphic)", "thick": 15.0}]})),

dict(title="Stratigraphy Basics", tier=F,
 desc_pub=("Stratigraphy is the study of layered rocks: superposition (younger layers overlie "
  "older), original horizontality, and fossil succession for dating. Strata columns depict "
  "the layer stack at a location - thickness, rock type, age.\n"
  "Correlating columns between boreholes reveals the subsurface architecture: which layers "
  "continue, pinch out, or fault-offset. Stratigraphy is the grammar of subsurface "
  "description."),
 desc_sig=("Signature stratigraphic frameworks standardize unit naming and correlation "
  "workflows, so columns from different campaigns speak the same language."),
 how_pub=("Geologists log layers in each borehole, describe lithology and fossils, assign "
  "ages, and correlate marker beds between holes. Fences of correlated columns build the "
  "3D picture."),
 how_sig=("Signature standardized unit naming makes multi-campaign correlation reliable."),
 keys=["Superposition, horizontality, fossil succession",
  "Strata columns: the layer stack",
  "Correlation reveals architecture",
  "Marker beds link boreholes",
  "Stratigraphy is subsurface grammar",
  "Fences build the 3D picture"],
 reqs=["Borehole logging",
  "Fossil/lithology identification",
  "Correlation skill"],
 stds=["Stratigraphic nomenclature codes (public, e.g., NACSN)"],
 cites=["U.S. Geological Survey — stratigraphy (public)"],
 demo=("correlate", {"holes": [
   {"id": "BH-01", "units": [{"unit": "Sand"}, {"unit": "Clay marker"}, {"unit": "Sandstone"}]},
   {"id": "BH-02", "units": [{"unit": "Sand"}, {"unit": "Clay marker"}, {"unit": "Shale"}]},
   {"id": "BH-03", "units": [{"unit": "Clay marker"}, {"unit": "Sandstone"}]}]})),

dict(title="What a Borehole Is", tier=F,
 desc_pub=("A borehole is a drilled hole into the subsurface - for water, investigation, "
  "minerals, or energy. Drilling methods: rotary (fast, deep), auger (shallow soils), "
  "percussion/cable-tool, and sonic (excellent core recovery).\n"
  "Every borehole is a precious direct observation: location, depth, method, and the "
  "materials encountered are logged meticulously, because drilling it again costs as much "
  "as the first time."),
 desc_sig=("Signature borehole records capture method, location, and observations in "
  "standardized digital logs at the rig, so nothing is lost to paper."),
 how_pub=("Drillers advance the hole with the suitable method, collect cuttings or core at "
  "intervals, and geologists log lithology, water strikes, and drilling behavior. The hole "
  "is completed (cased, screened) or sealed per regulations."),
 how_sig=("Signature rig-side digital logging preserves observations at capture."),
 keys=["Drilled holes for water, investigation, minerals, energy",
  "Rotary, auger, percussion, sonic methods",
  "Direct observation - precious and costly",
  "Log location, depth, method, materials",
  "Cuttings or core at intervals",
  "Complete or seal per regulations"],
 reqs=["Drilling contractor",
  "Geological logging",
  "Regulatory compliance"],
 stds=["Drilling and logging standards (public, e.g., ASTM)"],
 cites=["U.S. Geological Survey — drilling (public)"],
 demo=("column", {"layers": [
   {"unit": "Fill", "thick": 2.0}, {"unit": "Gravel aquifer", "thick": 10.0},
   {"unit": "Till", "thick": 22.0}, {"unit": "Bedrock", "thick": 40.0}]})),

dict(title="Reading a Borehole Log", tier=F,
 desc_pub=("A borehole log is the organized record of a hole: depth-indexed descriptions of "
  "materials, water strikes, drilling notes, and wireline measurements. Reading one means "
  "tracking the story downward - depositional environments changing, aquifers appearing, "
  "bedrock arriving.\n"
  "Standard log headers record who, where, when, how: location coordinates, elevation "
  "datum, drilling method, dates. Without headers, a log is just scribbles."),
 desc_sig=("Signature log readers parse standardized digital logs into queryable databases, "
  "making thousands of logs searchable at once."),
 how_pub=("Readers check headers first (location, datum, method), then scan depth-indexed "
  "lithology for aquifers, confining layers, and bedrock. Water strikes and drilling notes "
  "flag hydrologic significance. Wireline curves refine the story."),
 how_sig=("Signature queryable log databases make regional analysis possible."),
 keys=["Depth-indexed materials, water, notes, measurements",
  "Read the story downward",
  "Headers: who, where, when, how",
  "Track aquifers and confining layers",
  "Water strikes flag hydrology",
  "Wireline refines the story"],
 reqs=["Standardized log format",
  "Header completeness",
  "Lithology interpretation skill"],
 stds=["Borehole log standards (public)"],
 cites=["U.S. Geological Survey — borehole logs (public)"],
 demo=("logstat", {"readings": [45.2, 47.8, 46.1, 52.3, 51.7, 48.9, 46.5, 53.1, 52.8, 47.2]})),

dict(title="Sedimentary Layers", tier=F,
 desc_pub=("Sedimentary layers form as sediments accumulate and lithify: sand becomes "
  "sandstone, mud becomes shale, shells become limestone. Grain size, sorting, and fossils "
  "record the depositional environment - river, beach, deep sea.\n"
  "Layer properties decide use: sands and gravels transmit water (aquifers); clays block it "
  "(aquitards); thick salt or shale can seal storage reservoirs. Reading layers predicts "
  "behavior."),
 desc_sig=("Signature depositional models link layer descriptions to predicted properties, "
  "so each logged layer carries behavior expectations."),
 how_pub=("Geologists describe grain size, sorting, and structures in cores and cuttings, "
  "interpret environments, and assign hydrogeologic roles (aquifer/aquitard). Porosity and "
  "permeability are measured or estimated."),
 how_sig=("Signature environment-to-property models make descriptions predictive."),
 keys=["Sediments accumulate and lithify",
  "Grain size records environment",
  "Sands: aquifers; clays: aquitards",
  "Salt/shale: seals",
  "Reading layers predicts behavior",
  "Measure porosity, permeability"],
 reqs=["Sediment description skill",
  "Environmental interpretation",
  "Property measurement"],
 stds=["Sedimentary description standards (public)"],
 cites=["Society for Sedimentary Geology — public resources (public)"],
 demo=("column", {"layers": [
   {"unit": "Beach sand", "thick": 6.0}, {"unit": "Marine clay (aquitard)", "thick": 14.0},
   {"unit": "River gravel (aquifer)", "thick": 9.0}, {"unit": "Deep-sea shale", "thick": 35.0}]})),

dict(title="Groundwater Basics", tier=F,
 desc_pub=("Groundwater fills pore spaces below the water table: aquifers (transmit water "
  "usefully), aquitards (block flow), wells (access points). Flow follows topography and "
  "pressure - from recharge areas to springs, streams, and wells.\n"
  "Sustainability rule: pump no more than recharge replenishes, or water levels fall. "
  "Contamination spreads with flow - protecting recharge areas protects wells."),
 desc_sig=("Signature groundwater data systems link borehole, water-level, and quality "
  "records, so aquifers are managed from complete information."),
 how_pub=("Hydrogeologists map aquifers from boreholes, monitor water levels in wells, test "
  "pumping to measure properties, and model flow. Management sets pumping limits from "
  "recharge estimates; protection zones guard recharge areas."),
 how_sig=("Signature linked water records make aquifer management information-complete."),
 keys=["Aquifers transmit; aquitards block",
  "Flow follows topography and pressure",
  "Pump no more than recharge",
  "Contamination spreads with flow",
  "Monitor levels in wells",
  "Protect recharge areas"],
 reqs=["Aquifer mapping",
  "Water-level monitoring",
  "Pumping tests"],
 stds=["Hydrogeology standards (public)"],
 cites=["U.S. Geological Survey — groundwater (public)"],
 demo=("logstat", {"readings": [12.1, 12.3, 11.9, 12.5, 12.2, 11.8, 12.4, 12.0, 12.6, 12.2]})),

dict(title="Maps of the Subsurface", tier=F,
 desc_pub=("Subsurface maps show what drilling reveals: structure contour maps (elevation of a "
  "buried surface), isopach maps (layer thickness), and cross-sections (vertical slices along "
  "a line). Together they communicate 3D geology on 2D paper.\n"
  "Map literacy: contours close around highs and lows, thickness maps guide resource "
  "estimates, cross-sections show the layer cake with faults and folds. Every map needs "
  "scale, datum, and data-point locations."),
 desc_sig=("Signature map products generate from the same 3D model as the database, so maps "
  "and models can never disagree."),
 how_pub=("Geologists compile borehole picks onto maps, contour by hand or software, draw "
  "cross-sections honoring all data, and document sources and uncertainty. Digital maps "
  "live in GIS with the underlying data."),
 how_sig=("Signature model-derived maps guarantee map-model consistency."),
 keys=["Structure contours: buried surface elevation",
  "Isopach: layer thickness",
  "Cross-sections: vertical slices",
  "Contours close around highs/lows",
  "Scale, datum, data points required",
  "Digital maps in GIS"],
 reqs=["Borehole pick compilation",
  "Contouring skill/software",
  "GIS capability"],
 stds=["Geologic mapping standards (public)"],
 cites=["U.S. Geological Survey — mapping (public)"],
 demo=("survey", {"stations": [
   {"id": "S1", "value": 100.0}, {"id": "S2", "value": 102.5}, {"id": "S3", "value": 98.0},
   {"id": "S4", "value": 101.0}, {"id": "S5", "value": 135.0}, {"id": "S6", "value": 99.5}], "tol": 15.0})),

dict(title="Depth and Elevation Datums", tier=F,
 desc_pub=("Subsurface depths are meaningless without datums: depths below ground surface "
  "vs elevations above sea level. Ground surface varies - a layer 10 m deep on a hill may "
  "sit higher than one 5 m deep in a valley.\n"
  "Standard practice: record both depth and elevation (ground elevation minus depth), note "
  "the elevation datum (NAVD88 or local), and survey borehole locations precisely. Datum "
  "errors have ruined projects."),
 desc_sig=("Signature datum management validates every record's datum metadata on ingest, "
  "rejecting ambiguous elevations before they corrupt models."),
 how_pub=("Surveyors establish ground elevations at each borehole, loggers record depths "
  "from a fixed reference (kelly bushing, ground), and databases store both with datum "
  "metadata. Conversions are explicit, never assumed."),
 how_sig=("Signature ingest validation catches datum ambiguity at the door."),
 keys=["Depth vs elevation: different things",
  "Record both depth and elevation",
  "Note the elevation datum",
  "Survey locations precisely",
  "Datum errors ruin projects",
  "Conversions explicit, never assumed"],
 reqs=["Surveyed elevations",
  "Datum documentation",
  "Reference discipline"],
 stds=["Geodetic datum standards (public)"],
 cites=["National Geodetic Survey (public)"],
 demo=("logstat", {"readings": [102.5, 103.1, 102.8, 103.5, 102.9, 103.2, 102.7, 103.0]})),

dict(title="Fossils and Dating Layers", tier=F,
 desc_pub=("Fossils date sedimentary layers: index fossils (widespread, short-lived species) "
  "pin a layer's age; assemblages refine it. Superposition orders the stack; fossils "
  "calibrate it to geologic time.\n"
  "Absolute dating (radiometric) anchors the scale where suitable minerals exist. Together, "
  "relative and absolute dating build the geologic time framework every correlation uses."),
 desc_sig=("Signature biostratigraphic databases link fossil occurrences to the time scale, "
  "so age assignments are traceable to evidence."),
 how_pub=("Paleontologists identify fossils from cuttings and cores, assign biozones, and "
  "correlate to the geologic time scale. Radiometric dates anchor key horizons. Age models "
  "document uncertainty."),
 how_sig=("Signature traceable age assignments link every date to its fossil evidence."),
 keys=["Index fossils pin ages",
  "Assemblages refine",
  "Superposition orders; fossils calibrate",
  "Radiometric anchors where possible",
  "Geologic time scale framework",
  "Document uncertainty"],
 reqs=["Paleontological identification",
  "Time scale reference",
  "Uncertainty documentation"],
 stds=["Geologic Time Scale (public, ICS)"],
 cites=["International Commission on Stratigraphy (public)"],
 demo=("column", {"layers": [
   {"unit": "Sandstone (Jurassic)", "thick": 40.0},
   {"unit": "Shale (Cretaceous)", "thick": 60.0},
   {"unit": "Limestone (Tertiary)", "thick": 25.0}]})),

dict(title="Porosity and Permeability", tier=F,
 desc_pub=("Porosity is the fraction of rock that is pore space (stores fluids); permeability "
  "is how well pores connect (transmits fluids). High porosity without permeability (shale) "
  "stores but won't yield; both high (clean sand) makes aquifers and reservoirs.\n"
  "Measured on cores in labs and estimated from wireline logs in holes. These two properties "
  "decide groundwater, oil, gas, and storage potential."),
 desc_sig=("Signature petrophysical databases compile porosity-permeability relationships per "
  "rock type, so estimates start from measured analogues."),
 how_pub=("Labs measure core porosity/permeability; log analysts derive them from wireline "
  "curves; modelers populate 3D grids honoring both. Relationships are rock-type specific - "
  "never borrow blindly."),
 how_sig=("Signature analogue databases ground property estimates in measurements."),
 keys=["Porosity: storage fraction",
  "Permeability: flow connectivity",
  "Shale: stores, won't yield",
  "Clean sand: aquifer/reservoir",
  "Measured on cores; estimated from logs",
  "Rock-type-specific relationships"],
 reqs=["Core analysis",
  "Wireline interpretation",
  "Property modeling"],
 stds=["Petrophysical measurement standards (public, e.g., API)"],
 cites=["Society of Petrophysicists — public resources (public)"],
 demo=("logstat", {"readings": [0.22, 0.25, 0.21, 0.28, 0.24, 0.19, 0.26, 0.23, 0.27, 0.20]})),

# ---------------- Compounded (12) ----------------
dict(title="Wireline Logging", tier=C,
 desc_pub=("Wireline logging lowers instruments into boreholes to measure formation properties "
  "in place: gamma ray (shale vs sand), resistivity (fluids), sonic (porosity), density, "
  "neutron, and caliper (hole size). Curves vs depth reveal lithology and fluids.\n"
  "Interpretation is pattern recognition: clean sands show low gamma + high resistivity "
  "(hydrocarbons) or low resistivity (water). Logs calibrate to cores where available."),
 desc_sig=("Signature log-interpretation workflows standardize curve QC and multi-log "
  "analysis, so interpretations are reproducible."),
 how_pub=("Loggers run tool strings after drilling, QC curves for tool problems, and "
  "interpreters pick lithology and fluid contacts from curve patterns. Results feed "
  "correlation and modeling."),
 how_sig=("Signature standardized QC makes log interpretations reproducible."),
 keys=["Gamma, resistivity, sonic, density, neutron, caliper",
  "Curves vs depth reveal lithology/fluids",
  "Pattern recognition",
  "Calibrate to cores",
  "QC curves first",
  "Feed correlation and modeling"],
 reqs=["Wireline tools",
  "Curve QC",
  "Interpretation expertise"],
 stds=["Wireline logging standards (public)"],
 cites=["Society of Petrophysicists (public)"],
 demo=("logstat", {"readings": [75.0, 78.5, 32.0, 35.5, 80.0, 76.5, 30.0, 33.5, 79.0, 77.0]})),

dict(title="Seismic Survey Basics", tier=C,
 desc_pub=("Seismic surveys image the subsurface with sound: sources (vibroseis, airguns) send "
  "waves down; receivers record reflections off layer boundaries. Processing turns "
  "recordings into images of structure - anticlines, faults, stratigraphy.\n"
  "2D lines give cross-sections; 3D surveys give volumes. Resolution vs depth trades: "
  "higher frequencies see detail shallow; lower frequencies penetrate deep."),
 desc_sig=("Signature seismic data management preserves field data through processing "
  "versions, so interpretations stay linked to raw recordings."),
 how_pub=("Crews lay out sources and receivers, acquire with QC, and processors apply "
  "statics, velocity analysis, migration. Interpreters pick horizons and faults on the "
  "migrated volumes."),
 how_sig=("Signature versioned processing preserves the raw-to-interpretation chain."),
 keys=["Sound waves image layer boundaries",
  "Sources: vibroseis, airguns",
  "2D lines; 3D volumes",
  "Resolution vs depth trade-off",
  "Processing: statics, velocity, migration",
  "Interpret horizons and faults"],
 reqs=["Seismic acquisition",
  "Processing capability",
  "Interpretation expertise"],
 stds=["Seismic data standards (public, e.g., SEG-Y)"],
 cites=["Society of Exploration Geophysicists (public)"],
 demo=("survey", {"stations": [
   {"id": "T1", "value": 1.2}, {"id": "T2", "value": 1.5}, {"id": "T3", "value": 4.8},
   {"id": "T4", "value": 1.3}, {"id": "T5", "value": 1.1}, {"id": "T6", "value": 5.2}], "tol": 2.0})),

dict(title="Gravity and Magnetic Surveys", tier=C,
 desc_pub=("Gravity surveys map density variations - salt domes, ore bodies, basins - with "
  "gravimeters; magnetic surveys map magnetic minerals - igneous intrusions, faults, "
  "archaeological features - with magnetometers.\n"
  "Both are fast, cheap reconnaissance: they find anomalies worth detailed follow-up, not "
  "definitive answers. Corrections (terrain, latitude, diurnal) precede interpretation."),
 desc_sig=("Signature potential-field workflows standardize corrections and anomaly "
  "ranking, so reconnaissance is systematic."),
 how_pub=("Surveyors collect gridded or airborne data, apply corrections, and interpret "
  "anomalies against geology. Targets feed seismic or drilling programs."),
 how_sig=("Signature standardized anomaly ranking prioritizes follow-up objectively."),
 keys=["Gravity: density variations",
  "Magnetics: magnetic minerals",
  "Fast cheap reconnaissance",
  "Find anomalies, not answers",
  "Corrections before interpretation",
  "Feed detailed follow-up"],
 reqs=["Gravimeter/magnetometer surveys",
  "Correction processing",
  "Anomaly interpretation"],
 stds=["Potential-field survey standards (public)"],
 cites=["Society of Exploration Geophysicists (public)"],
 demo=("survey", {"stations": [
   {"id": "G1", "value": 9.81}, {"id": "G2", "value": 9.80}, {"id": "G3", "value": 9.75},
   {"id": "G4", "value": 9.81}, {"id": "G5", "value": 9.82}], "tol": 0.03})),

dict(title="Electrical Resistivity Surveys", tier=C,
 desc_pub=("Resistivity surveys inject current and measure voltage to map subsurface "
  "electrical properties: clays conduct, sands resist, water chemistry shifts values. "
  "Arrays (Wenner, Schlumberger) trade depth for resolution.\n"
  "Applications: groundwater (fresh vs saline), contamination plumes, archaeology, "
  "engineering site investigation. Inversion turns measurements into 2D/3D resistivity "
  "images."),
 desc_sig=("Signature resistivity workflows standardize array choice and inversion "
  "parameters, making surveys comparable."),
 how_pub=("Crews deploy electrode arrays, acquire systematically, and invert data to "
  "resistivity sections. Interpretation ties resistivity patterns to geology with borehole "
  "control."),
 how_sig=("Signature standardized inversion keeps surveys comparable across sites."),
 keys=["Current in, voltage measured",
  "Clays conduct; sands resist",
  "Arrays trade depth/resolution",
  "Groundwater, contamination, archaeology",
  "Inversion creates resistivity images",
  "Borehole control grounds interpretation"],
 reqs=["Resistivity equipment",
  "Inversion software",
  "Borehole calibration"],
 stds=["Resistivity survey practices (public literature)"],
 cites=["Society of Exploration Geophysicists (public)"],
 demo=("survey", {"stations": [
   {"id": "E1", "value": 120.0}, {"id": "E2", "value": 95.0}, {"id": "E3", "value": 15.0},
   {"id": "E4", "value": 110.0}, {"id": "E5", "value": 105.0}], "tol": 60.0})),

dict(title="Ground-Penetrating Radar", tier=C,
 desc_pub=("Ground-penetrating radar (GPR) sends radio pulses and records reflections from "
  "buried objects and layers: utilities, voids, graves, shallow stratigraphy. High "
  "resolution, shallow penetration (meters, less in clay).\n"
  "Clay and salt water kill GPR signals - know the site's suitability first. Interpretation "
  "reads reflection patterns: hyperbolas mark point objects like pipes."),
 desc_sig=("Signature GPR practice pairs suitability assessment with standardized "
  "acquisition, so surveys are only run where they can work."),
 how_pub=("Assess suitability (soil, water), acquire grids with positioning, process "
  "(gain, migration), and interpret reflections. Mark utilities on the surface for "
  "excavation safety."),
 how_sig=("Signature suitability-first practice prevents doomed surveys."),
 keys=["Radio pulses; shallow, high-resolution",
  "Utilities, voids, stratigraphy",
  "Clay/salt water kill signals",
  "Check suitability first",
  "Hyperbolas mark point objects",
  "Mark finds for excavation safety"],
 reqs=["GPR system",
  "Suitability assessment",
  "Positioning"],
 stds=["GPR practice standards (public, e.g., ASTM D6432)"],
 cites=["ASTM International — D6432 (public)"],
 demo=("survey", {"stations": [
   {"id": "R1", "value": 0.5}, {"id": "R2", "value": 0.6}, {"id": "R3", "value": 3.8},
   {"id": "R4", "value": 0.55}, {"id": "R5", "value": 0.5}], "tol": 2.0})),

dict(title="Borehole Correlation", tier=C,
 desc_pub=("Borehole correlation links equivalent layers between holes using marker beds "
  "(distinctive layers), fossil zones, and log signatures. Correlated fences reveal "
  "structure: folds, faults, pinch-outs.\n"
  "Pitfalls: similar-looking layers of different ages, fault-repeated sections, and "
  "lateral facies changes. Multiple independent markers beat single-marker correlation."),
 desc_sig=("Signature correlation workbenches track marker confidence per pick, so fences "
  "carry their uncertainty explicitly."),
 how_pub=("Geologists pick markers in each hole, correlate on cross-sections, check with "
  "independent evidence (fossils, logs), and build fences. Uncertain correlations are "
  "flagged, not hidden."),
 how_sig=("Signature confidence-tracked picks make correlation uncertainty visible."),
 keys=["Link equivalent layers between holes",
  "Marker beds, fossil zones, log signatures",
  "Reveal folds, faults, pinch-outs",
  "Beware look-alike layers",
  "Multiple markers beat one",
  "Flag uncertain correlations"],
 reqs=["Marker identification",
  "Cross-section construction",
  "Independent verification"],
 stds=["Correlation practices (public literature)"],
 cites=["American Association of Petroleum Geologists (public)"],
 demo=("correlate", {"holes": [
   {"id": "BH-10", "units": [{"unit": "Top sand"}, {"unit": "Bentonite marker"}, {"unit": "Lower sand"}]},
   {"id": "BH-11", "units": [{"unit": "Top sand"}, {"unit": "Bentonite marker"}, {"unit": "Shale"}]},
   {"id": "BH-12", "units": [{"unit": "Top sand"}, {"unit": "Bentonite marker"}, {"unit": "Lower sand"}]}]})),

dict(title="Faults and Folds", tier=C,
 desc_pub=("Faults are fractures with displacement - normal (extension), reverse/thrust "
  "(compression), strike-slip (lateral). Folds are bent layers - anticlines (arch up), "
  "synclines (sag down). Both shape subsurface architecture profoundly.\n"
  "In data: faults offset markers between boreholes and break seismic reflectors; folds "
  "show as repeating dips. Faults can seal (trap fluids) or leak (pathways) - characterizing "
  "them matters for resources and hazards."),
 desc_sig=("Signature structural frameworks model faults as first-class objects with seal "
  "analysis, so structure directly informs fluid decisions."),
 how_pub=("Geologists map offsets in boreholes and seismic, classify fault/fold types, and "
  "assess seal vs leak behavior from juxtaposition and gouge properties. Models honor all "
  "structural data."),
 how_sig=("Signature fault-as-object modeling links structure to fluid behavior."),
 keys=["Faults: displaced fractures; folds: bent layers",
  "Normal, reverse, strike-slip; anticline, syncline",
  "Offset markers and reflectors",
  "Faults seal or leak",
  "Shape architecture profoundly",
  "Characterize for resources and hazards"],
 reqs=["Structural interpretation",
  "Offset mapping",
  "Seal analysis"],
 stds=["Structural geology practices (public literature)"],
 cites=["American Association of Petroleum Geologists (public)"],
 demo=("column", {"layers": [
   {"unit": "Sandstone", "thick": 20.0}, {"unit": "FAULT", "thick": 2.0},
   {"unit": "Sandstone (repeated)", "thick": 20.0}, {"unit": "Shale", "thick": 15.0}]})),

dict(title="Aquifer Characterization", tier=C,
 desc_pub=("Aquifer characterization quantifies groundwater systems: geometry from boreholes "
  "and geophysics, properties from pumping tests (transmissivity, storativity), recharge from "
  "water budgets, and quality from sampling.\n"
  "Pumping tests are the gold standard for properties: pump a well, watch neighbors "
  "respond, analyze the curves. Models built on characterization guide sustainable "
  "management."),
 desc_sig=("Signature aquifer records unify geometry, properties, and monitoring in single "
  "characterizations, so management sees the whole system."),
 how_pub=("Hydrogeologists compile borehole and geophysical geometry, run pumping tests, "
  "monitor levels and quality, and build numerical models. Characterization updates as new "
  "data arrives."),
 how_sig=("Signature unified aquifer records keep characterization current."),
 keys=["Geometry, properties, recharge, quality",
  "Pumping tests: the gold standard",
  "Transmissivity, storativity",
  "Models guide management",
  "Monitor levels and quality",
  "Update with new data"],
 reqs=["Pumping test capability",
  "Monitoring network",
  "Modeling software"],
 stds=["Aquifer testing standards (public, e.g., ASTM)"],
 cites=["U.S. Geological Survey — aquifer studies (public)"],
 demo=("logstat", {"readings": [250.0, 265.0, 240.0, 270.0, 255.0, 248.0, 262.0, 258.0]})),

dict(title="Site Investigation for Construction", tier=C,
 desc_pub=("Construction site investigation de-risks building: boreholes on a grid, in-situ "
  "tests (SPT, CPT), lab tests on samples (strength, compressibility), and groundwater "
  "assessment. Findings feed foundation design.\n"
  "Standards scale investigation to project risk: a house needs a few holes; a dam needs "
  "campaigns. Surprises (soft clay, voids, contamination) found early are cheap; found "
  "during construction, ruinous."),
 desc_sig=("Signature investigation planning scales borehole grids and testing to project "
  "risk with documented rationale, so investigation is proportional."),
 how_pub=("Engineers scope investigations per standards, drill and test, lab-test samples, "
  "assess groundwater, and write interpretive reports with design recommendations. "
  "Contamination screening runs in parallel."),
 how_sig=("Signature risk-scaled scoping makes investigation proportional and defensible."),
 keys=["Boreholes, SPT/CPT, lab tests, groundwater",
  "Feed foundation design",
  "Scale to project risk",
  "Early surprises cheap; late ruinous",
  "Interpretive reports with recommendations",
  "Screen contamination"],
 reqs=["Geotechnical drilling",
  "In-situ and lab testing",
  "Interpretive reporting"],
 stds=["Site investigation standards (public, e.g., Eurocode 7)"],
 cites=["British Geological Survey — engineering geology (public)"],
 demo=("logstat", {"readings": [15.0, 18.0, 12.0, 45.0, 50.0, 20.0, 16.0, 48.0]})),

dict(title="Contamination Assessment", tier=C,
 desc_pub=("Contamination assessment finds and delineates subsurface pollution: phased "
  "approach - desktop study, intrusive investigation (soil/groundwater sampling), risk "
  "assessment, remediation design. Source-pathway-receptor thinking focuses effort.\n"
  "Sampling QA/QC is critical: proper wells, decontaminated equipment, chain of custody. "
  "Plume maps guide remediation; monitoring proves it works."),
 desc_sig=("Signature contamination records link source history, plume data, and remediation "
  "performance in single case files, so liability and cleanup share one truth."),
 how_pub=("Investigators research site history, sample soil and groundwater systematically, "
  "assess risks to receptors, delineate plumes, and design remediation. Long-term "
  "monitoring verifies cleanup."),
 how_sig=("Signature unified case files keep contamination knowledge intact across "
  "decades."),
 keys=["Phased: desktop, intrusive, risk, remediation",
  "Source-pathway-receptor",
  "Sampling QA/QC critical",
  "Plume maps guide cleanup",
  "Monitoring proves remediation",
  "Chain of custody"],
 reqs=["Site history research",
  "Sampling with QA/QC",
  "Risk assessment"],
 stds=["Contaminated land standards (public, e.g., ASTM E1527)"],
 cites=["U.S. Environmental Protection Agency — cleanup (public)"],
 demo=("survey", {"stations": [
   {"id": "W1", "value": 5.0}, {"id": "W2", "value": 8.0}, {"id": "W3", "value": 120.0},
   {"id": "W4", "value": 95.0}, {"id": "W5", "value": 6.0}], "tol": 50.0})),

dict(title="Geothermal Data", tier=C,
 desc_pub=("Geothermal data maps Earth's heat: temperature gradients from boreholes, heat "
  "flow measurements, geochemical thermometers (silica, cation ratios), and resistivity "
  "surveys finding hot fluids.\n"
  "Exploration funnels from regional heat-flow to targeted drilling. Temperature logs in "
  "existing boreholes are cheap reconnaissance - every deep hole is a thermometer."),
 desc_sig=("Signature geothermal databases aggregate temperature data across borehole "
  "campaigns, turning scattered measurements into regional heat maps."),
 how_pub=("Explorers compile heat-flow data, run geochemistry and geophysics, drill "
  "slimholes then production wells, and log temperatures. Resource models estimate "
  "capacity and sustainability."),
 how_sig=("Signature aggregated temperature data reveals regional patterns."),
 keys=["Temperature gradients; heat flow",
  "Geochemical thermometers",
  "Resistivity finds hot fluids",
  "Regional to targeted funnel",
  "Deep holes are thermometers",
  "Model capacity and sustainability"],
 reqs=["Temperature logging",
  "Geochemical analysis",
  "Resource modeling"],
 stds=["Geothermal exploration practices (public literature)"],
 cites=["International Geothermal Association (public)"],
 demo=("logstat", {"readings": [25.0, 32.0, 41.0, 55.0, 68.0, 84.0, 97.0, 110.0]})),

dict(title="Mineral Exploration Data", tier=C,
 desc_pub=("Mineral exploration data hunts ore: geological mapping, geochemical sampling "
  "(soils, stream sediments), geophysics (magnetics, EM for conductors like massive "
  "sulfides), and drilling with assay.\n"
  "The funnel narrows from continent to drill target: each stage's data justifies the next "
  "stage's cost. Assay databases with QA/QC (standards, duplicates, blanks) underpin "
  "resource estimates."),
 desc_sig=("Signature exploration data systems track the prospect funnel with stage-gate "
  "decisions, so spending follows evidence."),
 how_pub=("Explorers map and sample regionally, follow up anomalies with detailed surveys, "
  "drill targets, assay with QA/QC, and estimate resources per reporting codes (JORC, "
  "NI 43-101). Data rooms preserve everything."),
 how_sig=("Signature stage-gated funnels make exploration spending evidence-driven."),
 keys=["Mapping, geochemistry, geophysics, drilling, assay",
  "Funnel: continent to drill target",
  "EM finds conductive sulfides",
  "Assay QA/QC: standards, duplicates, blanks",
  "Resource codes: JORC, NI 43-101",
  "Each stage justifies the next"],
 reqs=["Exploration program design",
  "Assay QA/QC",
  "Resource reporting codes"],
 stds=["JORC Code, NI 43-101 (public)"],
 cites=["Society of Economic Geologists (public)"],
 demo=("survey", {"stations": [
   {"id": "M1", "value": 0.02}, {"id": "M2", "value": 0.03}, {"id": "M3", "value": 2.5},
   {"id": "M4", "value": 0.02}, {"id": "M5", "value": 1.8}], "tol": 1.0})),

# ---------------- Advanced (11) ----------------
dict(title="3D Geological Modeling", tier=A,
 desc_pub=("3D geological modeling builds volumetric earth models from boreholes, maps, and "
  "seismic: surfaces for each horizon, fault networks, and property grids (porosity, "
  "permeability) between them. Software (open-source GemPy to commercial suites) "
  "interpolates between data.\n"
  "Models are interpretations, not truth: uncertainty grows away from data. Good practice "
  "documents assumptions, honors all data, and updates as new boreholes arrive."),
 desc_sig=("Signature 3D modeling practice versions models with their input data, so every "
  "model is reproducible from its inputs."),
 how_pub=("Modelers compile all data, build structural frameworks (horizons + faults), "
  "populate properties geostatistically, validate against held-out data, and document "
  "assumptions and uncertainty. Models update with new data."),
 how_sig=("Signature versioned models make subsurface interpretation reproducible."),
 keys=["Volumetric models from boreholes, maps, seismic",
  "Horizons, faults, property grids",
  "Interpolate between data",
  "Uncertainty grows from data",
  "Honor all data; document assumptions",
  "Update with new boreholes"],
 reqs=["3D modeling software",
  "Compiled input data",
  "Uncertainty documentation"],
 stds=["3D modeling practices (public literature)"],
 cites=["American Association of Petroleum Geologists (public)"],
 demo=("volume", {"dims": [50, 40, 20], "cell": 10.0, "fill": 0.85})),

dict(title="Seismic Interpretation", tier=A,
 desc_pub=("Seismic interpretation turns reflection data into geology: picking horizons "
  "(continuous reflectors = layer boundaries), mapping faults (disrupted reflectors), and "
  "extracting attributes (amplitude, frequency) that hint at fluids or lithology.\n"
  "Well ties calibrate: synthetic seismograms from borehole logs link reflections to "
  "known geology. Interpretation iterates with modeling - each informs the other."),
 desc_sig=("Signature interpretation workflows version picks with their seismic vintages, "
  "so reinterpretation is traceable."),
 how_pub=("Interpreters tie wells with synthetics, pick horizons and faults on 2D/3D "
  "volumes, extract attributes, and depth-convert with velocity models. Peer review "
  "challenges picks before they enter models."),
 how_sig=("Signature versioned picks make reinterpretation traceable."),
 keys=["Horizons: layer boundaries",
  "Faults: disrupted reflectors",
  "Attributes hint fluids/lithology",
  "Well ties calibrate",
  "Depth-convert with velocities",
  "Peer-review picks"],
 reqs=["Seismic volumes",
  "Well-tie capability",
  "Interpretation software"],
 stds=["Seismic interpretation practices (public literature)"],
 cites=["Society of Exploration Geophysicists (public)"],
 demo=("survey", {"stations": [
   {"id": "H1", "value": 2.1}, {"id": "H2", "value": 2.3}, {"id": "H3", "value": 2.2},
   {"id": "H4", "value": 3.9}, {"id": "H5", "value": 2.0}], "tol": 1.0})),

dict(title="Geostatistics and Interpolation", tier=A,
 desc_pub=("Geostatistics interpolates sparse subsurface data: kriging weights nearby "
  "measurements by spatial correlation (variograms), producing best estimates plus "
  "uncertainty maps. Simulation generates multiple equally-likely realizations.\n"
  "The variogram is the key: it quantifies how similarity decays with distance, per "
  "property and direction. Honest uncertainty maps guide where to drill next."),
 desc_sig=("Signature geostatistical practice standardizes variogram modeling with "
  "cross-validation, so interpolations are defensible."),
 how_pub=("Analysts compute experimental variograms, fit models, krige grids, and validate "
  "with cross-validation. Simulations quantify uncertainty; drilling targets fill the "
  "highest-uncertainty high-value areas."),
 how_sig=("Signature cross-validated variograms make interpolations defensible."),
 keys=["Kriging: weighted spatial interpolation",
  "Variograms quantify spatial correlation",
  "Estimates plus uncertainty maps",
  "Simulation: multiple realizations",
  "Uncertainty guides drilling",
  "Cross-validate"],
 reqs=["Geostatistical software",
  "Variogram modeling skill",
  "Validation discipline"],
 stds=["Geostatistical practices (public literature)"],
 cites=["International Association for Mathematical Geosciences (public)"],
 demo=("logstat", {"readings": [10.0, 12.0, 11.0, 15.0, 14.0, 13.0, 16.0, 12.5, 11.5, 14.5]})),

dict(title="Carbon Storage Site Characterization", tier=A,
 desc_pub=("Carbon storage characterization proves CO2 can be stored safely: a porous reservoir "
  "(sandstone) beneath a sealing caprock (shale/salt), mapped in 3D, with injectivity "
  "tested, faults assessed for leakage risk, and monitoring designed.\n"
  "Regulations demand containment assurance: baseline surveys, plume modeling, and "
  "long-term monitoring. Characterization data also serves hydrogen storage and "
  "geothermal - the subsurface skills transfer."),
 desc_sig=("Signature storage-site records unify geology, injectivity, and monitoring in "
  "single characterizations, so containment cases are complete."),
 how_pub=("Teams map reservoir and seal in 3D, test injectivity, model plume migration, "
  "assess well and fault leakage risks, and design monitoring (seismic, pressure, "
  "geochemistry). Regulators review containment cases."),
 how_sig=("Signature unified containment cases make storage permitting evidence-based."),
 keys=["Porous reservoir under sealing caprock",
  "3D-mapped, injectivity-tested",
  "Fault leakage risk assessed",
  "Plume modeling",
  "Baseline + long-term monitoring",
  "Skills transfer to hydrogen/geothermal"],
 reqs=["3D characterization",
  "Injectivity testing",
  "Monitoring design"],
 stds=["Storage assessment standards (public, e.g., ISO 27914)"],
 cites=["International Energy Agency — CCS (public)"],
 demo=("volume", {"dims": [100, 80, 10], "cell": 25.0, "fill": 0.7})),

dict(title="Induced Seismicity Monitoring", tier=A,
 desc_pub=("Induced seismicity - earthquakes triggered by injection, extraction, or "
  "reservoirs - is monitored with seismometer networks: detecting tiny events, locating "
  "them, and relating them to operations. Traffic-light protocols pause injection when "
  "magnitudes exceed thresholds.\n"
  "Baseline monitoring before operations distinguishes natural from induced events. "
  "Transparent data sharing builds public trust where operations meet communities."),
 desc_sig=("Signature induced-seismicity practice pairs real-time monitoring with public "
  "data dashboards, so communities see what operators see."),
 how_pub=("Operators install baselines, monitor continuously, locate events in near-real "
  "time, and apply traffic-light protocols. Data is shared with regulators and the "
  "public; operations adapt to seismic response."),
 how_sig=("Signature public dashboards make induced-seismicity monitoring transparent."),
 keys=["Injection/extraction can trigger quakes",
  "Seismometer networks detect and locate",
  "Traffic-light protocols",
  "Baseline before operations",
  "Distinguish natural from induced",
  "Transparent data builds trust"],
 reqs=["Seismic monitoring network",
  "Real-time location",
  "Traffic-light procedures"],
 stds=["Induced seismicity protocols (public literature)"],
 cites=["U.S. Geological Survey — induced seismicity (public)"],
 demo=("survey", {"stations": [
   {"id": "Q1", "value": 0.5}, {"id": "Q2", "value": 0.8}, {"id": "Q3", "value": 2.5},
   {"id": "Q4", "value": 0.6}, {"id": "Q5", "value": 0.4}], "tol": 1.5})),

dict(title="Subsurface Data Standards", tier=A,
 desc_pub=("Subsurface data standards make data shareable: GeoSciML (geological features), "
  "RESQML (3D reservoir models), WITSML (drilling data), and GroundWaterML - all with "
  "defined schemas and vocabularies.\n"
  "Adoption is uneven but growing: regulators increasingly require standard submissions, "
  "and standards unlock multi-source modeling. The alternative - bespoke formats per "
  "project - wastes the industry's data."),
 desc_sig=("Signature standards adoption validates every dataset against the relevant "
  "schema on ingest, so shared data is actually interoperable."),
 how_pub=("Organizations map internal formats to standards, validate submissions, and "
  "publish via standard services. Regulators specify required standards; archives "
  "enforce them."),
 how_sig=("Signature ingest validation makes interoperability real, not aspirational."),
 keys=["GeoSciML, RESQML, WITSML, GroundWaterML",
  "Defined schemas and vocabularies",
  "Regulators require standard submissions",
  "Unlock multi-source modeling",
  "Bespoke formats waste data",
  "Validate on ingest"],
 reqs=["Standard mappings",
  "Validation tooling",
  "Publication services"],
 stds=["GeoSciML, RESQML, WITSML (public standards)"],
 cites=["Energistics — standards (public)",
  "Open Geospatial Consortium (public)"],
 demo=("correlate", {"holes": [
   {"id": "STD-1", "units": [{"unit": "Unit A (GeoSciML)"}, {"unit": "Unit B (GeoSciML)"}]},
   {"id": "STD-2", "units": [{"unit": "Unit A (GeoSciML)"}, {"unit": "Unit C (GeoSciML)"}]}]})),

dict(title="Borehole Data Management", tier=A,
 desc_pub=("Borehole data management preserves drilling's value: standardized digital logs, "
  "validated coordinates and datums, linked documents (driller notes, photos, lab "
  "results), versioned interpretations, and open publication.\n"
  "National borehole databases (BGS, USGS) prove the model: decades of holes queryable in "
  "one place, each new project building on all previous drilling instead of starting "
  "blind."),
 desc_sig=("Signature borehole management treats every hole as a permanent data asset with "
  "complete lineage, so the archive compounds in value."),
 how_pub=("Organizations standardize logging formats, validate on ingest, link all "
  "associated documents, version interpretations separately from raw data, and publish to "
  "national databases where they exist."),
 how_sig=("Signature asset-grade borehole records compound the archive's value."),
 keys=["Standardized digital logs",
  "Validated coordinates and datums",
  "Linked documents and photos",
  "Versioned interpretations",
  "Open publication",
  "Build on previous drilling"],
 reqs=["Logging standards",
  "Ingest validation",
  "Publication pipeline"],
 stds=["Borehole data standards (public)"],
 cites=["British Geological Survey — borehole data (public)",
  "U.S. Geological Survey (public)"],
 demo=("logstat", {"readings": [100.0, 150.0, 200.0, 175.0, 225.0, 190.0, 210.0, 165.0]})),

dict(title="Uncertainty in Subsurface Models", tier=A,
 desc_pub=("Subsurface models are uncertain: sparse data, ambiguous interpretations, and "
  "property variability. Honest practice quantifies it - multiple realizations, sensitivity "
  "analysis, and explicit confidence statements.\n"
  "Decisions use uncertainty: drill the high-value high-uncertainty target; design "
  "foundations for the worst credible case. Hiding uncertainty is the professional "
  "failure; communicating it is the skill."),
 desc_sig=("Signature uncertainty practice requires every model to ship with quantified "
  "uncertainty and decision guidance, so users never mistake models for truth."),
 how_pub=("Modelers generate multiple realizations, test sensitivity to key assumptions, "
  "and document confidence per area. Decision-makers receive uncertainty-aware "
  "recommendations, not single answers."),
 how_sig=("Signature uncertainty-shipped models keep decisions honest."),
 keys=["Sparse data, ambiguous interpretation",
  "Quantify: realizations, sensitivity",
  "Explicit confidence statements",
  "Decisions use uncertainty",
  "Hiding it is the failure",
  "Communicating it is the skill"],
 reqs=["Uncertainty quantification",
  "Sensitivity analysis",
  "Decision communication"],
 stds=["Uncertainty practices (public literature)"],
 cites=["Society of Petroleum Engineers (public)"],
 demo=("volume", {"dims": [30, 30, 15], "cell": 20.0, "fill": 0.6})),

dict(title="Legacy Data Rescue", tier=A,
 desc_pub=("Legacy data rescue saves subsurface knowledge from decay: scanning paper logs, "
  "digitizing with QC, georeferencing old locations, and validating against modern data. "
  "Millions of paper logs hold irreplaceable observations - wells long sealed, outcrops "
  "long built over.\n"
  "Prioritize by value and risk: data in active development areas, deteriorating media, "
  "and unique observations first. Rescued data enters modern databases with provenance "
  "noting its journey."),
 desc_sig=("Signature rescue operations run digitization pipelines with provenance "
  "tracking, so rescued data carries its history transparently."),
 how_pub=("Programs inventory paper holdings, prioritize by value/risk, scan and digitize "
  "with double-key QC, georeference, and ingest into databases with rescue provenance. "
  "Originals are preserved archivally."),
 how_sig=("Signature provenance-tracked rescue keeps history transparent."),
 keys=["Paper logs decay; knowledge is irreplaceable",
  "Scan, digitize, georeference, validate",
  "Prioritize by value and risk",
  "Double-key QC",
  "Provenance notes the journey",
  "Preserve originals archivally"],
 reqs=["Paper holdings inventory",
  "Digitization pipeline",
  "Georeferencing"],
 stds=["Digitization best practices (public)"],
 cites=["British Geological Survey — data rescue (public)"],
 demo=("logstat", {"readings": [50.0, 52.0, 48.0, 51.0, 49.0, 53.0, 50.5, 51.5]})),

dict(title="Subsurface Data Ethics and Access", tier=A,
 desc_pub=("Subsurface data ethics balances openness with legitimate restriction: public "
  "borehole data serves science and planning; proprietary exploration data earns its "
  "confidentiality period; sacred-site and security-sensitive locations need protection.\n"
  "Best practice: open by default with defined embargoes, clear licensing, and respect "
  "for indigenous data sovereignty. Data collected with public money should serve the "
  "public."),
 desc_sig=("Signature data policy implements tiered access - open, embargoed, restricted - "
  "with machine-readable licenses, so sharing is the default and restriction is "
  "justified."),
 how_pub=("Organizations set data policies with embargo periods, publish open data with "
  "licenses, protect sensitive locations, and honor indigenous sovereignty. Publicly "
  "funded data goes public."),
 how_sig=("Signature tiered access makes openness the default."),
 keys=["Openness vs legitimate restriction",
  "Public data serves science",
  "Confidentiality periods for exploration",
  "Protect sensitive locations",
  "Indigenous data sovereignty",
  "Public money, public data"],
 reqs=["Data policy",
  "Embargo management",
  "Licensing"],
 stds=["Open data principles (public)",
  "CARE principles for indigenous data (public)"],
 cites=["Global Indigenous Data Alliance — CARE (public)"],
 demo=("correlate", {"holes": [
   {"id": "OPEN-1", "units": [{"unit": "Sand"}, {"unit": "Clay"}]},
   {"id": "EMBARGO-2", "units": [{"unit": "Sand"}, {"unit": "Shale"}]}]})),

dict(title="The Future of Subsurface Data", tier=A,
 desc_pub=("Subsurface data's future: ubiquitous sensing (fiber-optic DAS turning cables "
  "into seismometers), machine learning accelerating interpretation, digital twins of "
  "reservoirs and cities, and open data commons compounding knowledge.\n"
  "The through-line is seeing clearly underground: better data, better models, better "
  "decisions about water, energy, storage, and hazards. This database's Signature edition "
  "prototypes the knowledge core that future needs."),
 desc_sig=("The Signature future-state is a subsurface operating system: all boreholes, "
  "surveys, and models in one living archive with AI-assisted interpretation - serving "
  "water, energy, storage, and hazard decisions. This database is a prototype of that "
  "system's knowledge core."),
 how_pub=("The field deploys distributed sensing, validates ML interpretation tools, "
  "builds city-scale digital twins, and opens data commons. Standards mature; "
  "stewardship professionalizes."),
 how_sig=("Signature's operating-system vision makes subsurface knowledge cumulative."),
 keys=["Fiber-optic sensing everywhere",
  "ML accelerates interpretation",
  "Digital twins of reservoirs and cities",
  "Open data commons",
  "Through-line: seeing clearly underground",
  "Stewardship professionalizes"],
 reqs=["Distributed sensing",
  "ML validation",
  "Open commons infrastructure"],
 stds=["Emerging subsurface data standards (public literature)"],
 cites=["Society of Exploration Geophysicists (public)",
  "American Geophysical Union (public)"],
 demo=("volume", {"dims": [200, 200, 50], "cell": 5.0, "fill": 0.9})),
]
