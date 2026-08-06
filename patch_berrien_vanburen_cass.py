# -*- coding: utf-8 -*-
# Berrien / Van Buren / Cass County townships sweep, 2026-08-05 (pass 3, same project).
# Adds 53 new municipalities (ids 480-532) + enriches 2 existing Berrien entries
# (Benton Charter Twp id 246, Lincoln Charter Twp id 247) with new data-center findings.
# Also adds 4 new FIRMS entries: Horizon Planning, Michigan Township Services,
# Zoning Solutions, Mihelich & Associates.
import io
import json

path = "index.html"
with io.open(path, "r", encoding="utf-8") as f:
    src = f.read()

# ------------------------------------------------------------------
# 0. Add 4 new FIRMS entries
#    NOTE: renamed "Horizon Community Planning" -> "Horizon Planning" to match
#    the actually-confirmed branding (domain horizon-planning.com; consultant
#    David Jirousek, AICP, serves Almena/Antwerp/Paw Paw Townships).
# ------------------------------------------------------------------
old_firms_anchor = '  "Fresh Coast Planning":        { color: "#4d7c0f", short: "FCP" },\n  "Cassin Planning Group":       { color: "#6D4C41", short: "Cassin" },'
new_firms_anchor = '''  "Fresh Coast Planning":        { color: "#4d7c0f", short: "FCP" },
  "Horizon Planning":            { color: "#c026d3", short: "Horizon" },
  "Michigan Township Services":  { color: "#0e7490", short: "MTS" },
  "Zoning Solutions":            { color: "#a16207", short: "ZoneSol" },
  "Mihelich & Associates":       { color: "#be185d", short: "Mihelich" },
  "Cassin Planning Group":       { color: "#6D4C41", short: "Cassin" },'''
assert old_firms_anchor in src, "FIRMS anchor not found"
src = src.replace(old_firms_anchor, new_firms_anchor, 1)
print("Step 0 done: 4 new FIRMS entries added")

# ------------------------------------------------------------------
# 1. Enrich Benton Charter Township (id 246)
# ------------------------------------------------------------------
old_246_planner_title = '        planner_title: "Planning & Zoning Consultant",'
new_246_planner_title = '        planner_title: "Planning & Zoning Consultant (contracted individually, not a named firm)",'
assert src.count(old_246_planner_title) == 1, "246 planner_title not unique"
src = src.replace(old_246_planner_title, new_246_planner_title)

old_246_dc_notes_tail = '''Project may re-emerge if state tax legislation passes.",'''
new_246_dc_notes_tail = '''Project may re-emerge if state tax legislation passes. PULSE-CHECK UPDATE 2026-08-05: could not find any 2025 or 2026 status update confirming the project is dead, revived, or that a local moratorium was adopted — the most recent Planning Commission minutes reviewed (Jan-Apr 2026) don't mention it. Status remains genuinely stale/unresolved, not confirmed dead.",'''
assert old_246_dc_notes_tail in src, "246 dc_notes tail not found"
assert src.count(old_246_dc_notes_tail) == 1, "246 dc_notes tail not unique"
src = src.replace(old_246_dc_notes_tail, new_246_dc_notes_tail)

old_246_notes = '        notes: "No named planner identified — Building dept staff only (Deeann Scalf admin, Bennett/O\'Toole inspectors). The $3B stalled data center is the largest potential energy-planning case in Berrien County. Contact: bentonchartertwp.org or 269-925-0500. | Confirmed in 2025-2026 PC minutes. Engaged Jan 2026 for Master Plan + zoning rewrite ($20k cap). Firm unknown - may be sole practitioner. Data center: ~$3B AI company proposal on ~280 acres at Yore Ave; stalled (water capacity + opposition).",'
new_246_notes = '        notes: "PULSE-CHECK UPDATE 2026-08-05: Rebecca Harvey confirmed still current per the Jan 12, 2026 PC minutes (quoted $12,000 for a zoning ordinance review, $4,000 for master plan work; minutes note she \\"wrote the Master Plan\\"). She reads as an independent contracted consultant engaged project-by-project, not W-2 township staff, and no firm/company name is associated with her — worth noting she is the SAME Rebecca Harvey later corrected to McKenna Associates at Wayland Township (Allegan Co., id 457) in this project\'s Kalamazoo/Allegan cluster pass; unconfirmed whether this is the same person or a name coincidence, flagged for a cross-check. Building dept staff (Deeann Scalf admin, Bennett/O\'Toole inspectors) handle permitting separately. The $3B stalled data center is the largest potential energy-planning case in Berrien County. Contact: bentonchartertwp.org or 269-925-0500.",'
assert old_246_notes in src, "246 notes not found"
assert src.count(old_246_notes) == 1, "246 notes not unique"
src = src.replace(old_246_notes, new_246_notes)
print("Step 1 done: Benton Charter Township (246) enriched")

# ------------------------------------------------------------------
# 2. Enrich Lincoln Charter Township (id 247) — NEW moratorium finding
# ------------------------------------------------------------------
old_247_dc_notes = '        data_center_notes: "Active utility-scale solar proposals triggered adoption of new solar energy systems ordinance November 2025. Developer name(s) not publicly disclosed. Lake Michigan shoreline location. Michigan PA 233 context: township adopted ordinance proactively to maintain local input before MPSC override authority applies to 50+ MW projects.",'
new_247_dc_notes = '        data_center_notes: "Active utility-scale solar proposals triggered adoption of new solar energy systems ordinance November 2025. Developer name(s) not publicly disclosed. Lake Michigan shoreline location. Michigan PA 233 context: township adopted ordinance proactively to maintain local input before MPSC override authority applies to 50+ MW projects. NEW 2026-08-05 PULSE-CHECK FINDING: per WSBT (South Bend/Michiana) reporting dated June 11, 2026, the Township Board separately adopted a 10-month moratorium on NEW data centers, giving the Planning Commission time to study impacts on water, noise, electrical consumption, and surrounding communities before any project can proceed. The underlying board resolution/ordinance document itself was not independently retrieved this pass (sourced to the news report, not primary minutes) — worth pulling the actual text for the file.",'
assert old_247_dc_notes in src, "247 dc_notes not found"
assert src.count(old_247_dc_notes) == 1, "247 dc_notes not unique"
src = src.replace(old_247_dc_notes, new_247_dc_notes)

old_247_notes = '        notes: "Jim Pheifer, ICC Certified Building Official (primary contact for zoning/planning per township website, 269-429-1589, 2055 W. John Beers Rd, Stevensville). Jackie Yearous handles building admin/rental inspections. Glenn Youngstedt is Township Supervisor. Solar ordinance Nov 2025 — active developer proposals in township.",'
new_247_notes = '        notes: "Jim Pheifer, ICC Certified Building Official (primary contact for zoning/planning per township website, 269-429-1589, 2055 W. John Beers Rd, Stevensville). Jackie Yearous handles building admin/rental inspections. Glenn Youngstedt is Township Supervisor. Solar ordinance Nov 2025 — active developer proposals in township. PULSE-CHECK UPDATE 2026-08-05: Pheifer could not be independently re-confirmed this pass (site access issues on Planning Commission/Board of Trustees pages) — not disputing the entry, just flagging it wasn\'t re-verified.",'
assert old_247_notes in src, "247 notes not found"
assert src.count(old_247_notes) == 1, "247 notes not unique"
src = src.replace(old_247_notes, new_247_notes)

old_247_sources = '        sources: ["lctberrien.org", "WSJM Nov 13 2025 solar ordinance", "Herald Palladium solar ordinance article"]'
new_247_sources = '        sources: ["lctberrien.org", "WSJM Nov 13 2025 solar ordinance", "Herald Palladium solar ordinance article", "WSBT, Jun 11 2026 — https://wsbt.com/news/local/lincoln-township-trustees-agree-to-moratorium-on-data-centers-state-water-noise-electrical-consumption-impacts-communities-built-lincoln-township-michigan"]'
assert old_247_sources in src, "247 sources not found"
assert src.count(old_247_sources) == 1, "247 sources not unique"
src = src.replace(old_247_sources, new_247_sources)
print("Step 2 done: Lincoln Charter Township (247) enriched")

# ------------------------------------------------------------------
# 3. Insert 53 new municipalities (ids 480-532)
# ------------------------------------------------------------------

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def entry(id_, municipality, county, type_, lat, lng, planner_name, planner_title,
          firm, employment_type, dc_case, dc_notes, notes, sources):
    src_list = ", ".join('"%s"' % esc(s) for s in sources)
    return '''      {{
        id: {id_},
        municipality: "{municipality}",
        county: "{county}",
        type: "{type_}",
        lat: {lat},
        lng: {lng},
        planner_name: "{planner_name}",
        planner_title: "{planner_title}",
        firm: "{firm}",
        employment_type: "{employment_type}",
        status: "active",
        cwa_flag: false,
        cwa_alumni: false,
        data_center_case: {dc_case},
        data_center_notes: "{dc_notes}",
        notes: "{notes}",
        work_history: null,
        sources: [{src_list}]
      }}'''.format(
        id_=id_, municipality=esc(municipality), county=esc(county), type_=esc(type_),
        lat=lat, lng=lng, planner_name=esc(planner_name), planner_title=esc(planner_title),
        firm=esc(firm), employment_type=esc(employment_type),
        dc_case=("true" if dc_case else "false"), dc_notes=esc(dc_notes), notes=esc(notes),
        src_list=src_list,
    )

NF = "No data center/BESS/moratorium activity found this pulse-check pass (2026-08-05)."

municipalities = [
    # ---------------- BERRIEN COUNTY (480-499) ----------------
    dict(id_=480, municipality="Bainbridge Township", county="Berrien", type_="Township",
         lat=42.19, lng=-86.25, planner_name="Ross Rogien", planner_title="Building-Zoning Inspector",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Reviewed full 42-ordinance list and ZBA page — no solar, BESS, or data-center items.",
         notes="PULSE-CHECK 2026-08-05. Ross Rogien also serves as Zoning Administrator at neighboring Pipestone Township (id 493) — plausible he covers both as a shared/contracted individual; both townships' own sites list him without a firm name.",
         sources=["bainbridgetownship.org", "bainbridgetownship.org/ordinances", "en.wikipedia.org/wiki/Bainbridge_Township,_Berrien_County,_Michigan"]),

    dict(id_=481, municipality="Baroda Township", county="Berrien", type_="Township",
         lat=41.945, lng=-86.488, planner_name="Ryan Keough", planner_title="Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes="No data-center or BESS activity found. NOTABLE CONTEXT (not counted as a DC/BESS case per project convention, solar-only): Baroda has adopted TWO utility-scale-solar moratorium ordinances — Ordinance #42 (Jan 2024) and Ordinance #43 (Jan 2026, appears to be a renewal/extension) — worth rechecking if it later expands to cover BESS/data centers.",
         notes="PULSE-CHECK 2026-08-05. Ryan Keough (or a closely related \"T. Ryan Keough\") is also listed as Zoning Administrator at neighboring Oronoko Charter Township (id 492) — likely the same person serving multiple townships as a contracted individual, though both sites present him as in-house staff. Baroda Township split off from Lake Township in 1923; distinct from the Village of Baroda within it.",
         sources=["barodatownship.org", "barodatownship.org/baroda-township-ordinances/", "en.wikipedia.org/wiki/Baroda_Township,_Michigan"]),

    dict(id_=482, municipality="Berrien Township", county="Berrien", type_="Township",
         lat=41.9497, lng=-86.2886, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Township's site is a minimal single-page presence with no zoning/planning staff listed and no news section — treat this negative as lower-confidence.",
         notes="PULSE-CHECK 2026-08-05. No named planner/zoning administrator could be found on the township's own thin website. \"Berrien Township\" (around Berrien Center) is distinct from Berrien Springs (village), Berrien County itself, and any \"Berrien Charter Township\" naming (does not exist as a separate entity).",
         sources=["www.berrientownship.com", "en.wikipedia.org/wiki/Berrien_Township,_Michigan"]),

    dict(id_=483, municipality="Bertrand Township", county="Berrien", type_="Township",
         lat=41.798, lng=-86.439, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="Not confirmed — no official township website could be located this pass, so no ordinance/docket review was possible. Treat as a weak negative, not a confirmed one.",
         notes="PULSE-CHECK 2026-08-05. No official township website found; lat/lng is an approximation using the unincorporated community of Dayton within the township, NOT a confirmed township-hall location. Bertrand Township borders Indiana (South Bend area). Recommend a direct clerk phone call to establish current planning/zoning contact.",
         sources=["en.wikipedia.org/wiki/Bertrand_Township,_Michigan"]),

    dict(id_=484, municipality="Buchanan Township", county="Berrien", type_="Township",
         lat=41.83, lng=-86.36, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="Not confirmed — the township's site (buchanantownship.org) is JavaScript-rendered and its content could not be extracted with available research tools this pass. Treat as a weak negative given lack of access.",
         notes="PULSE-CHECK 2026-08-05. Buchanan Charter Township is legally distinct from the City of Buchanan, a separate incorporated home-rule city located within/adjacent to the township — do not conflate the two governments. Lat/lng is an approximation (township surrounds the City); recommend a follow-up visit to buchanantownship.org directly in a browser.",
         sources=["buchanantownship.org", "en.wikipedia.org/wiki/Buchanan_Township,_Michigan"]),

    dict(id_=485, municipality="Chikaming Township", county="Berrien", type_="Township",
         lat=41.865, lng=-86.636, planner_name="Kelly Largent", planner_title="Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes="UNRESOLVED — an earlier pass in this project flagged an ACTIVE 1-year data-center moratorium said to have been approved May 14, 2026, but this pulse-check recheck (homepage, Building & Zoning page, and minutes-index level only, not full PDF minutes) could not corroborate that claim. Not marked as a confirmed case pending direct verification against primary board/PC minutes — recommend pulling the actual May 2026 minutes before relying on this.",
         notes="PULSE-CHECK 2026-08-05. Building inspections are contracted out to SafeBuilt Building Service, but zoning administration itself is in-house per Kelly Largent. Chikaming Township includes Harbert, Sawyer, Lakeside, and the Shorewood-Tower Hills-Harbert CDP; Union Pier is split between Chikaming and New Buffalo Township — don't attribute all of Union Pier to Chikaming alone.",
         sources=["www.chikamingtownship.org", "www.chikamingtownship.org/staff-directory", "www.chikamingtownship.org/building-zoning", "en.wikipedia.org/wiki/Chikaming_Township,_Michigan"]),

    dict(id_=486, municipality="Coloma Charter Township", county="Berrien", type_="Charter Township",
         lat=42.185, lng=-86.31, planner_name="Kevin Kutscher", planner_title="Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Reviewed News & Announcements and Building Department pages; full Municode ordinance text wasn't directly searchable, so not fully exhaustive.",
         notes="PULSE-CHECK 2026-08-05. Jim Fulton is the (also in-house) Building Inspector. Coloma Charter Township surrounds but is legally distinct from the City of Coloma, which has its own separate government.",
         sources=["www.colomatownship.org", "www.colomatownship.org/building-department", "en.wikipedia.org/wiki/Coloma_Charter_Township,_Michigan"]),

    dict(id_=487, municipality="Galien Township", county="Berrien", type_="Township",
         lat=41.797, lng=-86.492, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Reviewed full ordinance list (Ordinances 2-26, including a marijuana-facility moratorium) and the Planning Commission page — no solar, BESS, or data-center items found.",
         notes="PULSE-CHECK 2026-08-05. No dedicated staff zoning administrator found; Planning Commission is chaired by Richard \\\"Rusty\\\" Riley (a citizen chair, not staff), with Ed Carpenter (Building Inspector) and Bob Middlebrook (Code Officer) handling enforcement. Galien Township is distinct from the Village of Galien, a separate incorporated municipality within it.",
         sources=["www.galientownship.org", "www.galientownship.org/info-forms/ordinances", "www.galientownship.org/government/planning-commission"]),

    dict(id_=488, municipality="Hagar Township", county="Berrien", type_="Township",
         lat=42.107, lng=-86.394, planner_name="Mark Toncray", planner_title="Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Reviewed the Zoning department page in full; the township's separate ordinance-hosting site could not be accessed (SSL error), so not fully exhaustive.",
         notes="PULSE-CHECK 2026-08-05. Hagar Township includes the unincorporated community of Lake Michigan Beach (\\\"Hagar Shores\\\"). Mailing address uses Benton Harbor/Riverside ZIP codes, which can cause confusion with the separate City of Benton Harbor.",
         sources=["www.hagartownship.gov", "hagartownship.gov/departments/zoning.php", "en.wikipedia.org/wiki/Hagar_Township,_Michigan"]),

    dict(id_=489, municipality="Lake Charter Township", county="Berrien", type_="Charter Township",
         lat=41.968, lng=-86.543, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="Not confirmed — no official township website could be located this pass. Notable context (not a new proposal): the township already hosts the Donald C. Cook Nuclear Plant, making it a plausible watch-list site for future large-scale energy siting activity even absent a confirmed active docket item today.",
         notes="PULSE-CHECK 2026-08-05. IMPORTANT DISAMBIGUATION — Lake Charter Township, Berrien County (near Bridgman, on Lake Michigan) must not be confused with plain \\\"Lake Township\\\" entities in other Michigan counties (Benzie, Huron, Roscommon, Newaygo, Missaukee, Isabella). A domain guess (laketwp.org) resolved to the Benzie County Lake Township during research — a real, documented mix-up risk.",
         sources=["en.wikipedia.org/wiki/Lake_Charter_Township,_Michigan"]),

    dict(id_=490, municipality="New Buffalo Township", county="Berrien", type_="Township",
         lat=41.80, lng=-86.74, planner_name="Estelle Brinkman", planner_title="Building Dept. Administrator & Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Building & Zoning and Planning Commission pages checked; a full local-news sweep wasn't completed, so treat as \"no activity in sources checked\" rather than fully exhaustive.",
         notes="PULSE-CHECK 2026-08-05. This is New Buffalo TOWNSHIP, distinct from the City of New Buffalo, a separate incorporated home-rule city within/adjacent to the township — do not conflate the two governments.",
         sources=["newbuffalotownship.org", "newbuffalotownship.org/departments/building-and-zoning-department", "newbuffalotownship.org/departments/planning-commission"]),

    dict(id_=491, municipality="Niles Charter Township", county="Berrien", type_="Charter Township",
         lat=41.81667, lng=-86.26667, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="Not confirmed — the township's likely site (nilestownship.org) presents an invalid/mismatched TLS certificate and could not be verified as authentic this pass; no dedicated news search was completed either.",
         notes="PULSE-CHECK 2026-08-05. This is Niles Charter TOWNSHIP, distinct from the City of Niles, a separate incorporated city surrounded by (but independent of) the township. Recommend verifying nilestownship.org's certificate/ownership directly before relying on it.",
         sources=["en.wikipedia.org/wiki/Niles_Charter_Township,_Michigan"]),

    dict(id_=492, municipality="Oronoko Charter Township", county="Berrien", type_="Charter Township",
         lat=41.95, lng=-86.36667, planner_name="T. Ryan Keough", planner_title="Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Homepage (features a 2023 Master Plan and a Rental Safety Verification Program, unrelated to energy siting) and Building & Zoning page checked; full local-news sweep not completed.",
         notes="PULSE-CHECK 2026-08-05. \\\"T. Ryan Keough\\\" here closely matches \\\"Ryan Keough,\\\" Zoning Administrator at neighboring Baroda Township (id 481) — likely the same contracted individual serving both townships, flagged for cross-check. Sometimes referred to informally as just \\\"Oronoko Township\\\"; contains the unincorporated village of Berrien Springs.",
         sources=["oronokotownship.org", "oronokotownship.org (Building & Zoning)", "en.wikipedia.org/wiki/Oronoko_Charter_Township,_Michigan"]),

    dict(id_=493, municipality="Pipestone Township", county="Berrien", type_="Township",
         lat=42.03111, lng=-86.29083, planner_name="Ross Rogien", planner_title="Zoning Administrator (also Building Inspector)",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=True,
         dc_notes="ACTIVE, CONFIRMED 2026-08-05: Pipestone Township adopted Ordinance No. 2026-1, \\\"An Ordinance to Enact a Temporary Moratorium on Data Centers,\\\" on July 8, 2026 (posted via a linked document on the township's own site). No BESS-specific proposal found; specific substantive provisions beyond the moratorium's existence/adoption date not independently confirmed this pass.",
         notes="PULSE-CHECK 2026-08-05. Ross Rogien is also listed as Building-Zoning Inspector at neighboring Bainbridge Township (id 480) — plausibly the same contracted individual serving both (the two townships share a fire department). Agricultural community on Berrien's eastern side.",
         sources=["pipestonetownship.org", "en.wikipedia.org/wiki/Pipestone_Township,_Michigan"]),

    dict(id_=494, municipality="Royalton Township", county="Berrien", type_="Township",
         lat=42.04319, lng=-86.43332, planner_name="Tony Riegel", planner_title="Building Official / Zoning Administrator / Planner",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Zoning, Building Safety, and Planning Commission pages checked; full local-news sweep not completed.",
         notes="PULSE-CHECK 2026-08-05. Township hall at 980 Miners Road, St. Joseph, MI — situated on the St. Joseph River in Berrien's \\\"fruitbelt.\\\"",
         sources=["royaltontownship.org", "royaltontownship.org/zoning/", "royaltontownship.org/building-safety/"]),

    dict(id_=495, municipality="St. Joseph Charter Township", county="Berrien", type_="Charter Township",
         lat=42.08, lng=-86.44, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="Not confirmed — the township's own site (sjctwp.org) could not be verified this pass due to access/robots restrictions.",
         notes="PULSE-CHECK 2026-08-05. IMPORTANT DISAMBIGUATION — this is St. Joseph Charter TOWNSHIP, Berrien County, MI, distinct from (a) the City of St. Joseph (separate incorporated city on Lake Michigan) and (b) St. Joseph COUNTY, Michigan (a different county to the east). A domain lead (stjosephtwp.com) turned out to be an unrelated St. Joseph Township in Allen County, Indiana — a confirmed, documented mix-up risk; do not use that site as a source for this entry. Lat/lng is a rough estimate for the St. Joseph, MI area, not independently geocoded.",
         sources=["Berrien County township directory — https://www.berriencounty.org/QuickLinks.aspx?CID=123"]),

    dict(id_=496, municipality="Sodus Township", county="Berrien", type_="Township",
         lat=42.05, lng=-86.24, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Planning & Zoning page and Township News page checked directly on the township's own site.",
         notes="PULSE-CHECK 2026-08-05. No zoning administrator named on the site's Planning & Zoning or News pages. East-central Berrien County, near Watervliet. Lat/lng is an approximation; Wikipedia's article on this township carries no coordinates.",
         sources=["sodustwp.org", "www.sodustwp.org/copy-of-planning-and-zoning", "www.sodustwp.org/township-news"]),

    dict(id_=497, municipality="Three Oaks Township", county="Berrien", type_="Township",
         lat=41.80, lng=-86.61, planner_name="Ed Carpenter", planner_title="Building & Mechanical Inspector / Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Planning Commission and Inspections pages checked; full local-news sweep not completed.",
         notes="PULSE-CHECK 2026-08-05. Ed Carpenter is also named as Building Inspector at Galien Township (id 487) — plausibly the same contracted individual serving multiple townships. Three Oaks TOWNSHIP is distinct from the Village of Three Oaks, a separate incorporated village located within it.",
         sources=["threeoakstownship.org", "www.threeoakstownship.org/inspections/", "www.threeoakstownship.org/planning-commission/"]),

    dict(id_=498, municipality="Watervliet Charter Township", county="Berrien", type_="Charter Township",
         lat=42.19, lng=-86.29, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="Not confirmed — the township's likely domain (wctwp.org) exists but blocks all automated access via robots.txt, so content could not be verified this pass.",
         notes="PULSE-CHECK 2026-08-05. This would be Watervliet Charter TOWNSHIP, distinct from the City of Watervliet, a separate incorporated city surrounded by the township (also not to be confused with Watervliet, New York). Lat/lng is a rough estimate, not independently geocoded. Recommend a direct browser visit to wctwp.org.",
         sources=["wctwp.org (existence only, content unverified)"]),

    dict(id_=499, municipality="Weesaw Township", county="Berrien", type_="Township",
         lat=41.86, lng=-86.52333, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="Not confirmed — no township website or dedicated news coverage found to check against.",
         notes="PULSE-CHECK 2026-08-05. CONFIRMED ACROSS TWO INDEPENDENT RESEARCH PASSES: Weesaw Township appears to have no independent township website (extensive domain-name guessing across both passes found nothing resolving). Recommend a direct clerk phone call via the Berrien County directory to establish current planning/zoning contact — this is the one township in this batch where \\\"no findings\\\" most likely reflects a real access gap rather than genuinely nothing going on.",
         sources=["en.wikipedia.org/wiki/Weesaw_Township,_Michigan", "Berrien County township directory — https://www.berriencounty.org/QuickLinks.aspx?CID=123"]),

    # ---------------- VAN BUREN COUNTY (500-517) ----------------
    dict(id_=500, municipality="Almena Township", county="Van Buren", type_="Township",
         lat=42.26476, lng=-85.82529, planner_name="David Jirousek, AICP", planner_title="Land Use / Zoning Consultant",
         firm="Horizon Planning", employment_type="Contracted", dc_case=False,
         dc_notes=NF + " Homepage, officials, planning, and building/zoning pages checked directly on the township's own site.",
         notes="PULSE-CHECK 2026-08-05. Firm confirmed via a closely-matching listing at neighboring Antwerp Township (id 501), where the same consultant, David Jirousek, is named with the firm \\\"Horizon Planning\\\" explicitly — treat as the same firm serving both townships (and also Paw Paw Township, id 513).",
         sources=["almenatownship.gov", "almenatownship.gov/officials.php", "almenatownship.gov/planning.php"]),

    dict(id_=501, municipality="Antwerp Township", county="Van Buren", type_="Township",
         lat=42.20948, lng=-85.78445, planner_name="David Jirousek", planner_title="Zoning and Planning Administrator",
         firm="Horizon Planning", employment_type="Contracted", dc_case=False,
         dc_notes=NF + " Homepage, Contact, and Planning Commission pages checked directly on the township's own site.",
         notes="PULSE-CHECK 2026-08-05. Township hall: 24821 Front Avenue, Mattawan, MI 49071. Jirousek also confirmed serving Almena (id 500) and Paw Paw (id 513) Townships under the same Horizon Planning firm.",
         sources=["antwerptownshipmi.gov", "antwerptownshipmi.gov/contact-us/", "antwerptownshipmi.gov/government/planning-commission-2/"]),

    dict(id_=502, municipality="Arlington Township", county="Van Buren", type_="Township",
         lat=42.31, lng=-86.11, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Homepage, ordinances, and zoning pages checked; site has minimal content overall (meeting minutes and ordinances only, no staff directory with names).",
         notes="PULSE-CHECK 2026-08-05. IMPORTANT — there is a separate, unrelated Arlington Charter Township in Tuscola County, Michigan; confirm any secondary sourcing is about Van Buren County's Arlington Township. Township hall address: 52022 34th Ave, Bangor, MI 49013 (low-precision lat/lng).",
         sources=["www.arlingtontownship.com", "www.arlingtontownship.com/zoning"]),

    dict(id_=503, municipality="Bangor Township", county="Van Buren", type_="Township",
         lat=42.28833, lng=-86.17, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Reviewed the township's information page hosted on the Van Buren County site (no standalone township site exists). Code enforcement is handled by a Van Buren County Sheriff's Deputy, not a named zoning administrator.",
         notes="PULSE-CHECK 2026-08-05. Confirmed no standalone township website — all information is hosted on vanburencountymi.gov. IMPORTANT DISAMBIGUATION — there is a much larger, more prominent Bangor Charter Township in Bay County, Michigan (near Bay City); confirm any secondary sourcing is about Van Buren County's Bangor Township, not Bay County's.",
         sources=["vanburencountymi.gov/government/municipalities/townships/bangor-township/", "en.wikipedia.org/wiki/Bangor_Township,_Van_Buren_County,_Michigan"]),

    dict(id_=504, municipality="Bloomingdale Township", county="Van Buren", type_="Township",
         lat=42.3825, lng=-85.94028, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Reviewed the township's information page hosted on the Van Buren County site (no standalone township site exists); staff directory lists Supervisor/Clerk/Treasurer/Trustees/Assessor but no zoning administrator by name.",
         notes="PULSE-CHECK 2026-08-05. Confirmed no standalone township website — all information is hosted on vanburencountymi.gov. The incorporated Village of Bloomingdale sits within/adjacent to the township and is a separate governmental entity — do not conflate village records with township records.",
         sources=["vanburencountymi.gov/government/municipalities/townships/bloomingdale-township/", "en.wikipedia.org/wiki/Bloomingdale_Township,_Michigan"]),

    dict(id_=505, municipality="Columbia Township (Van Buren Co.)", county="Van Buren", type_="Township",
         lat=42.4042, lng=-86.07308, planner_name="Unknown", planner_title="Zoning Administrator (role named, individual not published)",
         firm="Michigan Township Services", employment_type="Contracted", dc_case=False,
         dc_notes="UNRESOLVED — an earlier pass in this project flagged a Vesper Energy \\\"Gypsum Peak Energy Storage\\\" BESS project and an unconfirmed single-source claim that this township joined a 70+ municipality lawsuit against the MPSC over PA 233 enforcement. This pulse-check recheck could NOT substantiate either claim: the township's own site has no mention of either; Vesper Energy's own official projects page does not list a \\\"Gypsum Peak\\\" project among its named projects (Gaucho Solar, Hornet Solar, Juniper Creek Energy Storage, Bradford Solar, Axton Solar); and the MPSC's own site has no mention either. Not marked as a confirmed case — recommend a direct records request to the township or an MPSC E-Dockets search before relying on this claim.",
         notes="PULSE-CHECK 2026-08-05. IMPORTANT DISAMBIGUATION — there is a distinct, better-known Columbia Township in Jackson County, Michigan (Clarklake/Vandercook Lake area), which is more active in state energy-siting news; any general search hit for \\\"Columbia Township, Michigan\\\" PA 233/lawsuit news needs to be checked carefully to confirm it's actually about Van Buren County's Columbia Township and not Jackson County's — high risk of mix-up, especially for the still-unconfirmed lawsuit claim.",
         sources=["www.columbiatwp.com", "vesperenergy.com/projects", "www.michigan.gov/mpsc"]),

    dict(id_=506, municipality="Covert Township", county="Van Buren", type_="Township",
         lat=42.29365, lng=-86.26225, planner_name="Kelly Largent", planner_title="Zoning Official",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Homepage and Building & Zoning page checked; references the township's 2026 Master Plan & Coastal Management Plan, but no energy-siting content found within the fetched material.",
         notes="PULSE-CHECK 2026-08-05. Kelly Largent here shares a name with the confirmed Zoning Administrator at Chikaming Township, Berrien County (id 485) — the two townships are not adjacent, so treat as an unconfirmed possible name coincidence or a genuinely shared contracted individual; flagged for cross-check, not asserted as fact.",
         sources=["www.coverttwp.com", "coverttwp.com/building-zoning/"]),

    dict(id_=507, municipality="Decatur Township", county="Van Buren", type_="Township",
         lat=42.1081, lng=-85.97446, planner_name="OJ Hamilton", planner_title="Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Homepage and township-officials page checked; the zoning ordinance document library (General Commercial, Light Industrial, Manufacturing, Signs chapters) was not individually opened, so not fully exhaustive.",
         notes="PULSE-CHECK 2026-08-05. The incorporated Village of Decatur is a separate governmental entity within/adjacent to the township — do not conflate. Also note unrelated \\\"Decatur Township\\\" entities exist in other states (e.g., Indiana).",
         sources=["decaturtownshipmi.org", "decaturtownshipmi.org/township-officials/", "decaturtownshipmi.org/zoning/"]),

    dict(id_=508, municipality="Geneva Township", county="Van Buren", type_="Township",
         lat=42.37333, lng=-86.1825, planner_name="Unknown", planner_title="Unknown",
         firm="Michigan Township Services", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Reviewed the township's own site and the Van Buren County directory/information pages.",
         notes="PULSE-CHECK 2026-08-05. Michigan Township Services is confirmed for building/electrical inspection at Geneva; a dedicated zoning-administrator individual/role was not explicitly named in available material, so employment type for planning specifically is not fully confirmed (leans Contracted given MTS's confirmed inspection role).",
         sources=["www.genevatwpvbcmi.gov", "vanburencountymi.gov/government/municipalities/townships/geneva-township/"]),

    dict(id_=509, municipality="Hamilton Township (Van Buren Co.)", county="Van Buren", type_="Township",
         lat=42.11, lng=-86.02, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Reviewed the township's Planning Commission page and the Decatur & Hamilton Joint Future Land Use Plan page. Only planning-related item found is the joint master-planning effort with Decatur Township and the Village of Decatur.",
         notes="PULSE-CHECK 2026-08-05. IMPORTANT DISAMBIGUATION — there is a separate, unrelated Hamilton Township in Allegan County, Michigan (near the Village of Hamilton, zip 49419), already on this map. This entry is confirmed as the Van Buren County township via Van Buren County's own government site (hall address 52333 Territorial Road W, Decatur, MI 49045); no standalone township domain was found — information is hosted on vanburencountymi.gov.",
         sources=["vanburencountymi.gov/government/municipalities/townships/hamilton-township/", "vanburencountymi.gov/363/Hamilton-Township-Planning-Commission"]),

    dict(id_=510, municipality="Hartford Township", county="Van Buren", type_="Township",
         lat=42.20, lng=-86.16, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="No utility-scale data center or BESS activity found. Only energy-adjacent item found is Ordinance No. 49, a \\\"Residential Solar Company License Application and Inspection Ordinance\\\" — a residential contractor-licensing ordinance, not a utility-scale siting item.",
         notes="PULSE-CHECK 2026-08-05. No named zoning administrator found on the Ordinances or Officials pages. Lat/lng is an approximation using the City of Hartford vicinity (no hall street address found).",
         sources=["www.hartfordtownship.org", "www.hartfordtownship.org/officials", "www.hartfordtownship.org/ordinances"]),

    dict(id_=511, municipality="Keeler Township", county="Van Buren", type_="Township",
         lat=42.19, lng=-86.10, planner_name="Ryan Laylin", planner_title="Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Official homepage checked; a dedicated notices subpage could not be located/loaded to confirm further.",
         notes="PULSE-CHECK 2026-08-05. Holds weekly office hours at township hall alongside Building Inspector Scott Saunders. NOTE: a \\\"Ryan Laylin\\\" is also confirmed this pass as Interim Zoning Administrator at Silver Creek Township, Cass County (id 530) — plausibly the same individual serving both townships as a contracted/shared official; flagged for cross-check.",
         sources=["keelertownshipmi.gov", "www.keelertownship.org"]),

    dict(id_=512, municipality="Lawrence Township", county="Van Buren", type_="Township",
         lat=42.21, lng=-86.05, planner_name="Christopher (Chris) Mihelich", planner_title="Zoning Administrator",
         firm="Mihelich & Associates", employment_type="Contracted", dc_case=False,
         dc_notes=NF + " Zoning Department page and homepage checked directly.",
         notes="PULSE-CHECK 2026-08-05. Firm name \\\"Mihelich & Associates, LLC\\\" appears on the township homepage's business-hours listing; the dedicated Zoning Department page lists him without repeating the firm name, so the firm affiliation is not 100% double-confirmed across both pages. Building permits/inspections for the township are separately handled by SAFEbuilt, a distinct contracted building-department firm.",
         sources=["www.lawrence-township.org", "www.lawrence-township.org/dept-committees/zoning-department/"]),

    dict(id_=513, municipality="Paw Paw Township", county="Van Buren", type_="Township",
         lat=42.22, lng=-85.89, planner_name="David Jirousek", planner_title="Township Planner",
         firm="Horizon Planning", employment_type="Contracted", dc_case=False,
         dc_notes=NF + " Public Notices, Planning Commission, and Ordinances pages checked. The one recent zoning-amendment notice found (Aug 19, 2025 hearing) concerned mini/self-storage and indoor recreation land-use definitions — unrelated to data centers or battery storage.",
         notes="PULSE-CHECK 2026-08-05. David Jirousek, AICP of Horizon Planning (horizon-planning.com) also confirmed serving Almena (id 500) and Antwerp (id 501) Townships. Building permits/inspections separately handled by SAFEbuilt, a contracted building-department firm distinct from the planning role.",
         sources=["pawpawtownshipmi.gov", "pawpawtownshipmi.gov/planning-commission/", "pawpawtownshipmi.gov/public-notices/"]),

    dict(id_=514, municipality="Pine Grove Township", county="Van Buren", type_="Township",
         lat=42.34, lng=-85.90, planner_name="Bear Priest", planner_title="Zoning Administrator",
         firm="Unknown", employment_type="In-House", dc_case=True,
         dc_notes="ACTIVE, CONFIRMED 2026-08-05: Pine Grove Township adopted Ordinance No. 06-03-2026, a \\\"Temporary Data Center Moratorium,\\\" on June 3, 2026, effective 30 days after publication. It imposes a six-month moratorium on data-center development specifically (not BESS or solar) \\\"to study potential public health, safety, and welfare concerns,\\\" extendable by Board resolution, and expires early if a permanent data-center ordinance is adopted first. A Planning Commission public hearing was separately scheduled for 7/20/26, plausibly related to drafting that permanent ordinance (not independently confirmed).",
         notes="PULSE-CHECK 2026-08-05. Bear Priest also confirmed this project as Supervisor at Richland Charter Township, Kalamazoo County (a different individual role at a different township, from an earlier pass in this project) — worth a light cross-check in case of a shared name vs. the same very-active individual. No consulting firm named; listed with a personal cell number on the township site.",
         sources=["pinegrovetownshipmi.gov", "pinegrovetownshipmi.gov/notice-of-ordinance-adoption-temporary-data-center-moratorium/", "pinegrovetownshipmi.gov/planning-commission/"]),

    dict(id_=515, municipality="Porter Township (Van Buren Co.)", county="Van Buren", type_="Township",
         lat=42.10, lng=-85.83, planner_name="Bob Angle", planner_title="Zoning Administrator (also a Planning Commission member)",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Planning Commission, Directory, and Minutes pages checked; full ordinance text is hosted externally on Municode and wasn't fully searchable, so treat as a lighter-confidence negative.",
         notes="PULSE-CHECK 2026-08-05. IMPORTANT DISAMBIGUATION — there is a separate, unrelated Porter Township in adjacent Cass County, MI (id 529 on this map), directly bordering this one. This entry is confirmed via portertwpvbco.gov, whose homepage explicitly states \\\"PORTER TOWNSHIP, VAN BUREN COUNTY, MICHIGAN.\\\"",
         sources=["portertwpvbco.gov", "portertwpvbco.gov/planning-commission/", "portertwpvbco.gov/minutes-2/"]),

    dict(id_=516, municipality="South Haven Charter Township", county="Van Buren", type_="Charter Township",
         lat=42.37, lng=-86.27, planner_name="Tasha Smalley", planner_title="Zoning Administrator",
         firm="Michigan Township Services", employment_type="Contracted", dc_case=False,
         dc_notes=NF + " Zoning Ordinances, Forms & Permits, and Board & Committee pages checked. Recent site-plan reviews noted (Blue Star Highway, 73rd St, Hidden Ponds properties) appear to be standard/local-scale projects, not utility-scale energy or industrial siting.",
         notes="PULSE-CHECK 2026-08-05. Confirmed official name is \\\"South Haven Charter Township,\\\" distinct from the incorporated City of South Haven, which it surrounds.",
         sources=["southhaventwp.com", "southhaventwp.com/zoning-ordinances/", "southhaventwp.com/about/board-committee/"]),

    dict(id_=517, municipality="Waverly Township", county="Van Buren", type_="Township",
         lat=42.27, lng=-85.87, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Homepage, Planning & Zoning Commission page, and Building & Zoning page checked (staff-name fields on these pages were unpopulated placeholder elements at time of check).",
         notes="PULSE-CHECK 2026-08-05. No named planner/zoning administrator currently published on the township's own site.",
         sources=["waverlytownship-vbcmi.gov", "waverlytownship-vbcmi.gov/planningcommission", "waverlytownship-vbcmi.gov/building"]),

    # ---------------- CASS COUNTY (518-532) ----------------
    dict(id_=518, municipality="Calvin Township", county="Cass", type_="Township",
         lat=41.846361, lng=-85.928325, planner_name="Matthew Jorgensen", planner_title="Zoning Administrator",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Ordinances and Reports pages checked directly.",
         notes="PULSE-CHECK 2026-08-05. Jorgensen has a separate direct line (269-386-1110) from the main township office number, suggesting a possibly-contracted arrangement, but in-house-vs-contracted status could not be confirmed either way.",
         sources=["calvintownship.org", "calvintownship.org/ordinances", "calvintownship.org/reports"]),

    dict(id_=519, municipality="Howard Township", county="Cass", type_="Township",
         lat=41.851291, lng=-86.175614, planner_name="Linda McGregor", planner_title="Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Zoning and Ordinances pages checked directly.",
         notes="PULSE-CHECK 2026-08-05. Site identifies itself as \\\"Howard Charter Township\\\"; confirmed as the same Cass County township via address/ZIP match against Wikipedia's Cass County township list.",
         sources=["howardtwp.org", "howardtwp.org/zoning", "howardtwp.org/ordinances"]),

    dict(id_=520, municipality="Jefferson Township", county="Cass", type_="Township",
         lat=41.854371, lng=-86.04391, planner_name="Unknown", planner_title="Zoning Inspector (name not published)",
         firm="Unknown", employment_type="Unknown", dc_case=True,
         dc_notes="ACTIVE, CONFIRMED 2026-08-05 — explicitly covers BOTH data centers AND BESS: the township's own site lists a \\\"Data Center & Battery Energy Storage System Moratorium Ordinance,\\\" adopted May 21, 2026 as Resolution and Ordinance 2026-6 (per May 21, 2026 board minutes: \\\"Resolution and Ordinance 2026-6 passed unanimously\\\"). It's a one-year temporary moratorium citing potential negative impacts on permitted land uses and threats to public health, safety, and welfare, extendable by board resolution. This is the clearest dual data-center-AND-BESS ordinance found in this entire county sweep.",
         notes="PULSE-CHECK 2026-08-05. No individual Zoning Inspector name is published on the township's own site — only the role/title.",
         sources=["www.jeffersontownshiponline.org", "www.jeffersontownshiponline.org (May 21, 2026 board minutes PDF)"]),

    dict(id_=521, municipality="LaGrange Township", county="Cass", type_="Township",
         lat=41.911694, lng=-86.045879, planner_name="Steven Allen", planner_title="Zoning Administrator",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Ordinances page checked; lists only 5 ordinances (Cass County ORV, Noxious Weed 1-2022, Knox Box 5-2022, Short-term Rentals 2024-1, Zoning Amendment 5-2011) — none touching data centers/BESS. Site itself notes this list \\\"is not comprehensive,\\\" so unlisted activity can't be fully ruled out.",
         notes="PULSE-CHECK 2026-08-05. Township site lists two different addresses (a mailing address and a separately-stated hall address) that did not resolve to the same point in geocoding — flagged in case they map to genuinely different locations.",
         sources=["lagrangetownshipmi.com", "lagrangetownshipmi.com/ordinances"]),

    dict(id_=522, municipality="Marcellus Township", county="Cass", type_="Township",
         lat=42.026924, lng=-85.820579, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="No dedicated ordinances page with data-center/BESS content was found (only a Cass County ORV Ordinance reference); minutes page lists 2025-2026 PDFs but their full text wasn't reviewable this pass — not a high-confidence negative.",
         notes="PULSE-CHECK 2026-08-05. No named zoning administrator found; the site directs zoning inquiries to Clerk Darcie L. Plummer rather than a dedicated planning staffer.",
         sources=["www.marcellustwpmi.org", "www.marcellustwpmi.org/minutes"]),

    dict(id_=523, municipality="Mason Township", county="Cass", type_="Township",
         lat=41.776267, lng=-85.897831, planner_name="Chelsa Greathouse", planner_title="Zoning Administrator",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Reviewed 13 listed township ordinances/documents — none touching data centers/BESS.",
         notes="PULSE-CHECK 2026-08-05. An earlier pass in this project flagged a possible \\\"Zoning Solutions LLC\\\" firm as Ordinance Enforcement Officer here — this pulse-check recheck could NOT confirm that firm name anywhere on the official township site; the site names only Chelsa Greathouse as Zoning Administrator (personal Gmail contact, limited Tuesday 6-8pm office hours \\\"and by appointment,\\\" suggesting a possibly part-time/contracted arrangement, though this is inference, not confirmed). Treat the \\\"Zoning Solutions LLC\\\" claim as unconfirmed pending direct township contact.",
         sources=["www.masontownship.org", "www.masontownship.org/zoning-ordinances/"]),

    dict(id_=524, municipality="Milton Township", county="Cass", type_="Township",
         lat=41.777679, lng=-86.195002, planner_name="Eileen Glick", planner_title="Zoning Administrator",
         firm="In-House (City Staff)", employment_type="In-House", dc_case=False,
         dc_notes=NF + " Reviewed the 17-item Civil Ordinances list (includes a Medical Marijuana Moratorium Ordinance) — no data-center, BESS, or solar ordinances found.",
         notes="PULSE-CHECK 2026-08-05. In-house status is inferred from a township-domain email address (zoning@miltontwpmi.gov) and listing alongside other department heads, not an explicit site statement. Confirmed distinct from a same-named \\\"Milton Township\\\" in Antrim County, MI, which surfaced as a wrong-township lead during domain research (the correct site is miltontwpmi.gov).",
         sources=["miltontwpmi.gov", "miltontwpmi.gov/?page_id=72", "miltontwpmi.gov/?page_id=276"]),

    dict(id_=525, municipality="Newberg Township", county="Cass", type_="Township",
         lat=41.925877, lng=-85.819222, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=True,
         dc_notes="ACTIVE, CONFIRMED 2026-08-05: the township's ordinances page lists a \\\"Data Center Ordinance No. 2026-02\\\" and a \\\"Data Center Resolution No. 2026-09,\\\" both dated May 2026, alongside a new Mass Gathering Ordinance and a Solar Panel Ordinance from the same period. The PDFs were scanned images and not machine-readable, so exact adopted text (and whether BESS is explicitly covered) could not be verified. SEPARATE OPEN QUESTION: a \\\"Special Meeting Planning Commission Ordinance\\\" notice was posted for a July 23, 2026 public hearing; the notice text only says the meeting concerns \\\"Newberg Twp. Planning Commission Ordinance\\\" without stating a specific subject. Its connection to the May 2026 Data Center Ordinance/Resolution is plausible (same era of land-use activity) but NOT CONFIRMED — direct contact with the township clerk is needed. This is a DIFFERENT township's DC measure from Jefferson Township's (id 520) DC & BESS moratorium — don't conflate the two May 2026 actions.",
         notes="PULSE-CHECK 2026-08-05. No named Zoning Administrator found on the site. Hall/tax-payment address: 13020 Born St, Jones, MI 49061 (a separate 58391 M-40, Jones, MI address is listed for FedEx/UPS deliveries only).",
         sources=["newbergtwp.com/ordinances/", "newbergtwp.com/special-meeting-planning-commission-ordinance/", "newbergtwp.com (Data Center Ordinance No. 2026-02 PDF)", "newbergtwp.com (Data Center Resolution No. 2026-09 PDF)"]),

    dict(id_=526, municipality="Ontwa Township", county="Cass", type_="Township",
         lat=41.80, lng=-86.08, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="UNRESOLVED — the township's own Ordinances page lists a document titled \\\"Resolution to Adopt a Temporary Non-Zoning Moratorium,\\\" but the PDF itself could not be read (not machine-readable via available tools this pass), so its subject matter is NOT CONFIRMED — it may or may not relate to data centers/BESS/solar. Flagged for manual follow-up (open the PDF directly) rather than assumed either way.",
         notes="PULSE-CHECK 2026-08-05. Edwardsburg, MI area; lat/lng is an approximate geocode, not from an official source.",
         sources=["www.ontwatwp.org", "www.ontwatwp.org/ordinances"]),

    dict(id_=527, municipality="Penn Township", county="Cass", type_="Township",
         lat=41.91, lng=-85.99, planner_name="Unknown", planner_title="No staff zoning administrator — volunteer Planning & Zoning Commission (Chair Carl Sparks)",
         firm="Unknown", employment_type="Unknown", dc_case=True,
         dc_notes="ACTIVE, CONFIRMED 2026-08-05 via official board minutes: on May 11, 2026 the Board of Trustees adopted a 30-day moratorium on data-center decisions (4-1 vote) \\\"to allow time to write up a proper legal moratorium,\\\" after board members noted an earlier moratorium had been \\\"legally deficient.\\\" On May 21, 2026, the Board adopted a Temporary One-Year Moratorium on Data Centers and directed the Planning Commission to prepare formal zoning text amendments with outside legal counsel. No mention of BESS specifically.",
         notes="PULSE-CHECK 2026-08-05. Township runs on a volunteer Planning & Zoning Commission model (Carl Sparks, Shadrick Yoder, Craig Danzy, Nicholas Dussel) plus a separate Zoning Board chaired by Je Green — no staff administrator or contracted firm is named on the site. Hall address: 60717 S Main Street, Vandalia, MI.",
         sources=["penntwpmi.org", "penntwpmi.org (May 11, 2026 board minutes PDF)", "penntwpmi.org (May 21, 2026 special board minutes PDF)"]),

    dict(id_=528, municipality="Pokagon Township", county="Cass", type_="Township",
         lat=41.93, lng=-86.09, planner_name="Joseph True", planner_title="Zoning Administrator & Blight Enforcement Officer",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes=NF + " Planning & Zoning page and Ordinances section checked; site currently lists only a Zoning Ordinance (rev. 6/2019) and Master Plan.",
         notes="PULSE-CHECK 2026-08-05. Contact info given as direct township office hours (Mondays 5-7:30pm), suggesting a likely In-House/part-time township officer rather than an outside consulting firm — not explicitly confirmed either way.",
         sources=["pokagontownshipmi.gov", "pokagontownshipmi.gov/planning-zoning"]),

    dict(id_=529, municipality="Porter Township (Cass Co.)", county="Cass", type_="Township",
         lat=41.783, lng=-85.867, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="UNRESOLVED — an earlier pass in this project flagged a possible data-center moratorium confirmed as of ~July 15, 2026, but TWO separate research passes this session could not locate an official website for this township (extensive domain-guessing across both attempts either failed to resolve or hit unrelated same-named townships in other states — including Porter Township, Delaware County, Ohio). Not marked as a confirmed case given the total inability to verify — recommend a direct phone call to Cass County (casscountymi.org lists this as one of its 15 townships but does not expose a working direct link) or the township clerk before relying on the prior claim.",
         notes="PULSE-CHECK 2026-08-05. IMPORTANT DISAMBIGUATION — this is Porter Township, CASS COUNTY, Michigan (southeast Cass County, communities of Union, Williamsville, Zimmysville; pop. ~3,750 per 2020 census), distinct from Porter Township, Van Buren County, MI (id 515 on this map, directly bordering this one) and from Porter Township, Delaware County, Ohio (a false lead hit during domain research — portertwp.org). Lat/lng uses Union, MI as a geographic-center proxy, not a confirmed township-hall location.",
         sources=["www.casscountymi.org", "en.wikipedia.org/wiki/Porter_Township,_Cass_County,_Michigan"]),

    dict(id_=530, municipality="Silver Creek Township", county="Cass", type_="Township",
         lat=41.90, lng=-86.06, planner_name="Ryan Laylin (in-house Interim Zoning Administrator); McKenna Associates (contracted planning consultant)",
         planner_title="Interim Zoning Administrator / Planning Commission consultant",
         firm="McKenna Associates", employment_type="Contracted", dc_case=True,
         dc_notes="ACTIVE, CONFIRMED 2026-08-05 via official Planning Commission minutes (meeting held May 27, 2026, filed under a \\\"May draft\\\" label): \\\"Ben Schilling read Resolution No. 2026-003 Data Center Moratorium aloud,\\\" and the Commission \\\"requested input and guidance from McKenna regarding appropriate language\\\" for the moratorium. No mention of BESS specifically. A previously-cited planner name, \\\"Paige Smith,\\\" could NOT be independently confirmed in any document reviewed this pass — Ryan Laylin is the individual actually named in available minutes/site material as Interim Zoning Administrator, working alongside McKenna Associates as outside planning consultant.",
         notes="PULSE-CHECK 2026-08-05. \\\"Ryan Laylin\\\" is also confirmed this pass as Zoning Administrator at Keeler Township, Van Buren County (id 511) — plausibly the same individual serving both townships as a contracted/shared official; flagged for cross-check, not asserted as fact. Near Sister Lakes/Dowagiac.",
         sources=["www.silvercreektwpmi.gov", "silvercreektwpmi.gov/planning-commission/", "silvercreektwpmi.gov (May 27, 2026 PC minutes PDF, Resolution No. 2026-003)"]),

    dict(id_=531, municipality="Volinia Township", county="Cass", type_="Township",
         lat=41.95, lng=-85.85, planner_name="Unknown", planner_title="Unknown",
         firm="Unknown", employment_type="Unknown", dc_case=False,
         dc_notes="Not confirmed — no activity could be checked.",
         notes="PULSE-CHECK 2026-08-05. CONFIRMED ACROSS TWO INDEPENDENT RESEARCH PASSES: the township's website (voliniatownship.gov) is inaccessible, returning an HTTP 403 error on every attempt (including a direct fetch and a Wayback Machine lookup attempt, itself rate-limited). No alternate county or news source could be located to substitute. Recommend a direct clerk phone call via the Cass County directory to establish current planning/zoning contact — like Weesaw Township (Berrien, id 499), this \\\"no findings\\\" most likely reflects a real access gap rather than genuinely nothing going on. Lat/lng is an approximate geographic center near the Jones/Marcellus area, not from an official source.",
         sources=["www.voliniatownship.gov (inaccessible, HTTP 403 — cited to document the access failure)", "en.wikipedia.org/wiki/Volinia_Township,_Michigan", "Cass County township directory — https://www.casscountymi.org/QuickLinks.aspx?CID=1037"]),

    dict(id_=532, municipality="Wayne Township (Cass Co.)", county="Cass", type_="Township",
         lat=42.00, lng=-85.93, planner_name="Unknown", planner_title="Unknown (only named staff contact, Judy Fusko, handles property-cleanup bidding, not planning/zoning)",
         firm="Unknown", employment_type="Unknown", dc_case=True,
         dc_notes="ACTIVE DISCUSSION, CONFIRMED 2026-08-05 via official June 1, 2026 board meeting minutes: a resident, Julie Dye, \\\"asked if the township is considering a moratorium concerning Data Centers.\\\" Supervisor Davis responded that adopting a moratorium starts a one-year countdown before regulations can be enacted, and the township prefers to wait until concrete development proposals materialize before triggering that timeline. No moratorium has been adopted — this is an early-stage, preemptive discussion only, no developer/applicant named.",
         notes="PULSE-CHECK 2026-08-05. Hall address: 53950 Glenwood Road, Dowagiac, MI 49047. Confirmed distinct from Wayne Township, Marion County, Indiana, which surfaced as a wrong-township lead during domain research.",
         sources=["www.waynetwpmi.org", "www.waynetwpmi.org/minutes", "waynetwpmi.org (June 1, 2026 board minutes PDF)"]),
]

assert len(municipalities) == 53, "expected 53 new municipalities, got %d" % len(municipalities)
ids = [m["id_"] for m in municipalities]
assert ids == list(range(480, 533)), "id sequence mismatch: %r" % ids

entries_js = ",\n".join(entry(**m) for m in municipalities)

old_tail = '''        sources: ["City of Wayland Business/Planning & Zoning — https://www.cityofwayland.org/business/planning-zoning/", "City of Wayland Current Projects — https://www.cityofwayland.org/current-projects/"]
      }
    ];'''
new_tail = '''        sources: ["City of Wayland Business/Planning & Zoning — https://www.cityofwayland.org/business/planning-zoning/", "City of Wayland Current Projects — https://www.cityofwayland.org/current-projects/"]
      },
''' + entries_js + '''
    ];'''
assert old_tail in src, "array-closing anchor not found"
assert src.count(old_tail) == 1, "array-closing anchor not unique"
src = src.replace(old_tail, new_tail)
print("Step 3 done: inserted %d new municipality entries (ids 480-532)" % len(municipalities))

with io.open(path, "w", encoding="utf-8") as f:
    f.write(src)

print("PATCH COMPLETE. New file size:", len(src))
