# 2. data-type domains (41). Exact source-section -> domain slug map.
GROUP_DOMAIN = {
    "Absolute Mathematical & Ontological Constants": "ontological-constants-data-types",
    "Advanced Autonomous Agent & Cognitive Architectures": "agent-architectures-data-types",
    "Agriculture, Environmental Science & Ecology": "agriculture-ecology-data-types",
    "Artisanal Soap Formulations, Packaging & Batch Processing": "soap-formulation-data-types",
    "Astronomy, Aerospace & Defense": "aerospace-defense-data-types",
    "Causality, Temporal & Destiny Control Primitives": "temporal-control-data-types",
    "Core Computer Science & Database Architecture": "database-architecture-data-types",
    "Cosmological Simulation & Reality Architecture": "cosmological-simulation-data-types",
    "E-Commerce, Retail & Consumer": "retail-ecommerce-data-types",
    "Education & Academic Administration": "education-academic-data-types",
    "Embedded Systems, Micro-Runtimes & Firmware": "embedded-firmware-data-types",
    "Energy, Utilities & Smart Infrastructure": "energy-utilities-data-types",
    "Enterprise, HR & Legal Operations": "enterprise-hr-legal-data-types",
    "Entertainment, Media Production & Arts": "entertainment-arts-data-types",
    "Everyday Hardware & Substrate Fabrication": "hardware-fabrication-data-types",
    "Finance, Banking & Fintech": "fintech-data-types",
    "Gaming & Simulation": "gaming-simulation-data-types",
    "Geospatial, Mapping & Environmental": "geospatial-environmental-data-types",
    "Government, Demographics & Public Records": "government-demographics-data-types",
    "Healthcare & Clinical Informatics": "healthcare-clinical-data-types",
    "Historical & Specialized Computer Science Engine Primitives": "cs-engine-primitives-data-types",
    "Hospitality, Travel & Event Management": "hospitality-travel-data-types",
    "IT, Cybersecurity & DevOps": "cybersecurity-devops-data-types",
    "Insurance, Legal & Regulatory Compliance": "insurance-compliance-data-types",
    "Manufacturing, Robotics & Industrial Automation": "manufacturing-robotics-data-types",
    "Metaphysical, Noospheric & Consciousness Matrices": "noospheric-matrices-data-types",
    "Neuromorphic, Biological & Substrate Computing": "neuromorphic-computing-data-types",
    "Optical, Holographic & Nanophotonic Storage": "holographic-storage-data-types",
    "Post-Quantum Cryptography & Advanced Privacy": "post-quantum-crypto-data-types",
    "Public Safety, Law Enforcement & Forensics": "public-safety-forensics-data-types",
    "Real Estate, Urban Planning & Construction": "real-estate-construction-data-types",
    "Real-Time Communications, Broadcasting & Entertainment Production": "broadcast-communications-data-types",
    "Scientific, Engineering & Physics": "scientific-engineering-data-types",
    "Social Media, Communications & Media": "media-communications-data-types",
    "Static Web Applications, Networks & Distributed Deployment": "static-web-apps-data-types",
    "Supply Chain, Logistics & Transport": "supply-chain-logistics-data-types",
    "Telecom, Networking & Web Infrastructure": "telecom-network-data-types",
    "Topological, Geometric & Advanced Mathematical Spaces": "topological-math-data-types",
    "Trans-Dimensional, Brane & Hyper-Spatial Topology": "brane-topology-data-types",
    "Transportation, Maritime & Aviation": "transport-maritime-aviation-data-types",
    "Woodworking, Finishing & Surface Restoration": "woodworking-finishing-data-types",
}

#!/usr/bin/env python3
"""New-database definitions for Phase-Q."""
import json, os
from qentries import load_all

def _dbs():
    dbprod = [e for e in load_all([]) if e["family"] == "dbprod"]
    dtype = [e for e in load_all([]) if e["family"] == "dtype"]
    out = []
    # 1. production databases (200 entries)
    out.append({
        "slug": "production-databases",
        "name": "The Production Databases Database",
        "kind": "database product record",
        "prefix": "JAH-PDB-",
        "ai": "JAH Production Database Archivist",
        "role": "production database archivist — real-world production-grade database systems",
        "desc": "Real-world production-grade database systems — distributed SQL, document stores, graph engines, time-series, vector, and NewSQL platforms.",
        "fields": ["distributed-sql", "document", "graph", "time-series", "vector", "newsql", "key-value", "wide-column"],
        "family": "dbprod",
    })
    def dom_of(e):
        return GROUP_DOMAIN.get(e["group"])
    by_dom = {}
    unmapped = set()
    for e in dtype:
        dom = dom_of(e)
        if dom: by_dom.setdefault(dom, []).append(e)
        else: unmapped.add(e["group"])
    if unmapped:
        print("UNMAPPED dtype groups:", sorted(unmapped))
    assert len(by_dom) == 41, "expected 41 domains, got %d" % len(by_dom)
    domains = sorted(by_dom)
    DTYPE_PREFIX = {
        "ontological-constants-data-types": "JAH-ONC-",
        "agent-architectures-data-types": "JAH-AAG-",
        "agriculture-ecology-data-types": "JAH-AGD-",
        "soap-formulation-data-types": "JAH-SFD-",
        "aerospace-defense-data-types": "JAH-ASD-",
        "temporal-control-data-types": "JAH-TCD-",
        "database-architecture-data-types": "JAH-DBD-",
        "cosmological-simulation-data-types": "JAH-CSD-",
        "retail-ecommerce-data-types": "JAH-RTD-",
        "education-academic-data-types": "JAH-EDD-",
        "embedded-firmware-data-types": "JAH-EMD-",
        "energy-utilities-data-types": "JAH-END-",
        "enterprise-hr-legal-data-types": "JAH-EHD-",
        "entertainment-arts-data-types": "JAH-EAD-",
        "hardware-fabrication-data-types": "JAH-HFD-",
        "fintech-data-types": "JAH-FND-",
        "gaming-simulation-data-types": "JAH-GSD-",
        "geospatial-environmental-data-types": "JAH-GED-",
        "government-demographics-data-types": "JAH-GVD-",
        "healthcare-clinical-data-types": "JAH-HCD-",
        "cs-engine-primitives-data-types": "JAH-CED-",
        "hospitality-travel-data-types": "JAH-HTD-",
        "cybersecurity-devops-data-types": "JAH-CYD-",
        "insurance-compliance-data-types": "JAH-IND-",
        "manufacturing-robotics-data-types": "JAH-MRD-",
        "noospheric-matrices-data-types": "JAH-NMD-",
        "neuromorphic-computing-data-types": "JAH-NCD-",
        "holographic-storage-data-types": "JAH-HSD-",
        "post-quantum-crypto-data-types": "JAH-PQD-",
        "public-safety-forensics-data-types": "JAH-PSD-",
        "real-estate-construction-data-types": "JAH-RCD-",
        "broadcast-communications-data-types": "JAH-BCD-",
        "scientific-engineering-data-types": "JAH-SCD-",
        "media-communications-data-types": "JAH-MCD-",
        "static-web-apps-data-types": "JAH-SWD-",
        "supply-chain-logistics-data-types": "JAH-SLD-",
        "telecom-network-data-types": "JAH-TND-",
        "topological-math-data-types": "JAH-TMD-",
        "brane-topology-data-types": "JAH-BTD-",
        "transport-maritime-aviation-data-types": "JAH-TAD-",
        "woodworking-finishing-data-types": "JAH-WFD-",
    }
    assert set(DTYPE_PREFIX) == set(domains), "prefix map mismatch"
    for d in domains:
        slug = d
        label = " ".join(w.capitalize() for w in d.replace("-data-types", "").split("-"))
        out.append({
            "slug": slug,
            "name": "The %s Data Types Database" % label,
            "kind": "data type record",
            "prefix": DTYPE_PREFIX[d],
            "ai": "JAH %s Data Archivist" % label,
            "role": "%s data type archivist" % label.lower(),
            "desc": "Data types, record schemas, and interchange formats for %s systems." % label.lower(),
            "fields": ["schemas", "identifiers", "measurements", "events", "interchange"],
            "family": "dtype",
            "domain": d,
        })
    # 3. bizarre software (leftovers)
    out.append({
        "slug": "bizarre-software",
        "name": "The Bizarre Software Database",
        "kind": "software record",
        "prefix": "JAH-BIZ-",
        "ai": "JAH Bizarre Software Archivist",
        "role": "bizarre and avant-garde software archivist",
        "desc": "Bizarre, avant-garde, and cutting-edge software — unusual utilities, experimental apps, and novel system tools.",
        "fields": ["utilities", "experiments", "novelties", "system-tools", "research"],
        "family": "bizarre",
    })
    # 4. taxonomy section overflow DBs
    for slug, label, secname in [
        ("software-labs-taxonomy", "Software Labs", "LABS"),
        ("core-engine-taxonomy", "Core and Engine", "CORE & ENGINE"),
        ("storage-repository-taxonomy", "Storage and Repository", "STORAGE & REPOSITORY"),
        ("network-interconnect-taxonomy", "Network and Interconnect", "NETWORK & INTERCONNECTIVITY"),
        ("hardware-fabrication-taxonomy", "Hardware and Fabrication", "HARDWARE, FABRICATION & PHYSICAL"),
    ]:
        out.append({
            "slug": slug,
            "name": "The %s Taxonomy Database" % label,
            "kind": "taxonomy term record",
            "prefix": "JAH-" + "".join(w[0].upper() for w in slug.split("-")[:3]) + "-",
            "ai": "JAH %s Taxonomist" % label,
            "role": "%s taxonomy archivist" % label.lower(),
            "desc": "Taxonomy terms for %s — execution environments, categories, and classification vocabulary." % label.lower(),
            "fields": ["terms", "categories", "environments", "vocabulary"],
            "family": "taxon",
            "section": secname,
        })
    return out

NEW_DBS = _dbs()
BY_SLUG = {d["slug"]: d for d in NEW_DBS}

def with_signatures(dbs):
    out = []
    for d in dbs:
        out.append(d)
        s = dict(d)
        s["slug"] = d["slug"] + "-signature"
        s["name"] = d["name"] + " — Signature Edition"
        s["prefix"] = d["prefix"][:-1] + "S-"
        s["ai"] = d["ai"] + " (Signature)"
        s["signature"] = True
        out.append(s)
    return out

ALL_NEW = with_signatures(NEW_DBS)

if __name__ == "__main__":
    print(len(NEW_DBS), "new public DBs ->", len(ALL_NEW), "with signatures")
    prefixes = [d["prefix"] for d in ALL_NEW]
    assert len(set(prefixes)) == len(prefixes), "prefix collision: " + str([p for p in prefixes if prefixes.count(p) > 1])
    print("prefixes unique OK")
    for d in NEW_DBS:
        print(" ", d["slug"], d["prefix"])
