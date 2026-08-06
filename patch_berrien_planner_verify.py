# -*- coding: utf-8 -*-
# Verification pass, 2026-08-05 (pass 4, same project): Mo supplied two rounds of
# AI-assisted research on Berrien County "Unknown planner" townships. Each claim
# was checked against its cited primary source before being written in. Two of
# three "Wightman" claims did NOT survive verification (Watervliet traced to a
# mismatched citation for a different township entirely; St. Joseph Charter's
# own 2024 draft master plan has no Wightman credit). Confirmed facts below.
#
# Approach: extract each municipality's block by id (robust to exact escaping),
# do targeted field replacements within that block only, splice back.
import io
import re

path = "index.html"
with io.open(path, "r", encoding="utf-8") as f:
    src = f.read()

def get_block(id_):
    marker = "        id: %d,\n" % id_
    start = src.index(marker)
    # block runs from the "      {" line before marker to the matching "      },ህ" or "      }\n    ];"
    open_brace = src.rindex("      {\n", 0, start)
    end_close1 = src.find("\n      },\n", start)
    end_close2 = src.find("\n      }\n    ];", start)
    if end_close2 != -1 and (end_close1 == -1 or end_close2 < end_close1):
        end = end_close2 + len("\n      }")
    else:
        end = end_close1 + len("\n      }")
    return open_brace, end, src[open_brace:end]

def replace_block(id_, transform, label):
    global src
    start, end, block = get_block(id_)
    new_block = transform(block)
    assert new_block != block, "%s: transform made no change" % label
    src = src[:start] + new_block + src[end:]
    print("done:", label)

def set_field(block, field, new_value_js_string_literal):
    """Replace the value of `field: "...",` (single-line) within block."""
    pattern = re.compile(r'(' + re.escape(field) + r':\s*)"(?:[^"\\]|\\.)*"(,?)', re.S)
    m = pattern.search(block)
    assert m, "field %s not found in block" % field
    return block[:m.start()] + field + ": " + new_value_js_string_literal + m.group(2) + block[m.end():]

def jsstr(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

# ------------------------------------------------------------------
# 0. Add "Williams & Works" to FIRMS dictionary
# ------------------------------------------------------------------
old_firms = '  "Mihelich & Associates":       { color: "#be185d", short: "Mihelich" },'
assert src.count(old_firms) == 1
new_firms = old_firms + '\n  "Williams & Works":            { color: "#15803d", short: "W&W" },'
src = src.replace(old_firms, new_firms, 1)
print("done: FIRMS: add Williams & Works")

# ------------------------------------------------------------------
# 1. Niles Charter Township (id 491) — CONFIRMED
# ------------------------------------------------------------------
def t491(b):
    b = set_field(b, "planner_name", jsstr("Denise Kasprzak (in-house ZA) / Williams & Works (Planner of Record)"))
    b = set_field(b, "planner_title", jsstr("Zoning Administrator (in-house) / Planner of Record (contracted)"))
    b = set_field(b, "firm", jsstr("Williams & Works"))
    b = set_field(b, "employment_type", jsstr("Contracted + In-House"))
    b = set_field(b, "data_center_notes", jsstr("No data center/BESS/moratorium activity found this pulse-check pass (2026-08-05)."))
    b = set_field(b, "notes", jsstr(
        "CONFIRMED 2026-08-05 (verification pass, Mo-supplied lead): nilestwpmi.gov/departments/contact_zoning_dept.php directly names "
        "\"Denise Kasprzak (Zoning Administrator)\" as in-house staff contact AND states \"Planner of Record - Williams & Works, Grand Rapids, MI\" "
        "— the earlier \"nilestownship.org bad-cert\" note was the wrong domain; the real site is nilestwpmi.gov. This is Niles Charter TOWNSHIP, "
        "distinct from the City of Niles."))
    b = re.sub(r'sources:\s*\[[^\]]*\]', 'sources: ' + repr(["nilestwpmi.gov/departments/contact_zoning_dept.php", "en.wikipedia.org/wiki/Niles_Charter_Township,_Michigan"]).replace("'", '"'), b)
    return b
replace_block(491, t491, "491 Niles Charter Township")

# ------------------------------------------------------------------
# 2. Lake Charter Township (id 489) — CONFIRMED (firm only; individual name unconfirmed)
# ------------------------------------------------------------------
def t489(b):
    b = set_field(b, "planner_name", jsstr("Unknown (in-house) / Williams & Works (contracted, Master Plan)"))
    b = set_field(b, "planner_title", jsstr("Planning consultant for 2024 Master Plan"))
    b = set_field(b, "firm", jsstr("Williams & Works"))
    b = set_field(b, "employment_type", jsstr("Contracted"))
    b = set_field(b, "notes", jsstr(
        "CONFIRMED 2026-08-05 (verification pass, Mo-supplied lead): the township's own 2024 Master Plan (lakechartertownship.squarespace.com, "
        "PC-approved) carries the acknowledgement \"Prepared with assistance from WILLIAMS & WORKS\" — directly confirming the contracted-consultant "
        "relationship. A separately-cited PC-minutes PDF naming a Richard Kubsch (ZA) and William Geukes (PC Chair) could NOT be independently "
        "verified this pass (the fetched file returned unreadable/empty) — not asserted as fact, flagged for a direct follow-up read. IMPORTANT "
        "DISAMBIGUATION — Lake Charter Township, Berrien County (near Bridgman, on Lake Michigan; confirmed address 3220 Shawnee Rd, Bridgman, MI "
        "49106) must not be confused with plain \"Lake Township\" entities in other Michigan counties — a domain guess (laketwp.org) resolved to the "
        "Benzie County Lake Township during earlier research, and lake-township.org is yet another distinct entity, neither is this one."))
    b = re.sub(r'sources:\s*\[[^\]]*\]', 'sources: ' + repr(["lakechartertownship.squarespace.com (2024 Master Plan, PC-approved, Acknowledgements page)", "en.wikipedia.org/wiki/Lake_Charter_Township,_Michigan"]).replace("'", '"'), b)
    return b
replace_block(489, t489, "489 Lake Charter Township")

# ------------------------------------------------------------------
# 3. Buchanan Township (id 484) — CONFIRMED (citizen-chaired PC, no staff planner)
# ------------------------------------------------------------------
def t484(b):
    b = set_field(b, "data_center_notes", jsstr("No data center/BESS/moratorium activity found this pulse-check pass (2026-08-05)."))
    b = set_field(b, "notes", jsstr(
        "CONFIRMED 2026-08-05 (verification pass, Mo-supplied lead): buchanantownship.net (the real domain — buchanantownship.org, tried earlier, "
        "was the wrong/inaccessible one) names Dennis Wentworth as Planning Commission Chairman, Kimberly Scarpone as Vice Chairman, Gerald DiPietro "
        "as Secretary. This is a citizen-chaired PC, not a staff planner/ZA — no dedicated zoning administrator or contracted firm was found. "
        "Buchanan Charter Township is legally distinct from the City of Buchanan, a separate incorporated home-rule city located within/adjacent "
        "to the township."))
    b = re.sub(r'sources:\s*\[[^\]]*\]', 'sources: ' + repr(["buchanantownship.net/planning-commission/", "en.wikipedia.org/wiki/Buchanan_Township,_Michigan"]).replace("'", '"'), b)
    return b
replace_block(484, t484, "484 Buchanan Township")

# ------------------------------------------------------------------
# 4. Galien Township (id 487) — CONFIRMED (Supervisor, not a planner role)
# ------------------------------------------------------------------
def t487(b):
    b = set_field(b, "notes", jsstr(
        "PULSE-CHECK 2026-08-05, updated in verification pass same day (Mo-supplied lead): Tim Richter confirmed directly as Township Supervisor "
        "(galientownship.org/government/township-board), overseeing the township generally. No dedicated staff zoning administrator found; "
        "Planning Commission is chaired by Richard \"Rusty\" Riley (a citizen chair, not staff), with Ed Carpenter (Building Inspector) and Bob "
        "Middlebrook (Code Officer) handling enforcement. Galien Township is distinct from the Village of Galien, a separate incorporated "
        "municipality within it."))
    b = re.sub(r'sources:\s*\[[^\]]*\]', 'sources: ' + repr(["www.galientownship.org", "www.galientownship.org/info-forms/ordinances", "www.galientownship.org/government/planning-commission", "www.galientownship.org/government/township-board"]).replace("'", '"'), b)
    return b
replace_block(487, t487, "487 Galien Township")

# ------------------------------------------------------------------
# 5. St. Joseph Charter Township (id 495) — CONFIRMED Manager; Wightman NOT confirmed
# ------------------------------------------------------------------
def t495(b):
    b = set_field(b, "planner_name", jsstr("Tim Fenderbosch"))
    b = set_field(b, "planner_title", jsstr("Township Manager"))
    b = set_field(b, "firm", jsstr("In-House (City Staff)"))
    b = set_field(b, "employment_type", jsstr("In-House"))
    b = set_field(b, "data_center_notes", jsstr("No data center/BESS/moratorium activity found this pulse-check pass (2026-08-05)."))
    b = set_field(b, "notes", jsstr(
        "CONFIRMED 2026-08-05 (verification pass, Mo-supplied lead): Tim Fenderbosch confirmed as Township Manager (independently corroborated "
        "via ZoomInfo staff listing). This ALSO resolves the earlier domain confusion — sjct.org IS the real official site for this township "
        "(confirmed via its own 2024 draft Master Plan document), not the Indiana mix-up flagged before. A separate claim that Wightman "
        "(engineering/planning firm) \"partnered\" with this township on its master plan did NOT survive a direct check: the township's own "
        "2024.02.22 draft Master Plan has no acknowledgements or prepared-by section crediting Wightman or any consulting firm — only local "
        "officials' signatures (Roger Seely, Patrice Rose, Ben Baker, Denise Cook). Not treating the Wightman claim as confirmed. IMPORTANT "
        "DISAMBIGUATION — this is St. Joseph Charter TOWNSHIP, Berrien County, MI, distinct from (a) the City of St. Joseph and (b) St. Joseph "
        "COUNTY, Michigan. A domain lead (stjosephtwp.com) is an unrelated St. Joseph Township in Allen County, Indiana — do not use that site "
        "as a source for this entry."))
    b = re.sub(r'sources:\s*\[[^\]]*\]', 'sources: ' + repr(["sjct.org", "sjct.org/files/2024.02.22-Draft-2024-Master-Plan.pdf", "ZoomInfo — Tim Fenderbosch, Manager at St Joseph Charter Township", "Berrien County township directory — https://www.berriencounty.org/QuickLinks.aspx?CID=123"]).replace("'", '"'), b)
    return b
replace_block(495, t495, "495 St. Joseph Charter Township")

# ------------------------------------------------------------------
# 6. Bertrand Township (id 483) — PARTIAL confirmation, title unstated; flag name collision
# ------------------------------------------------------------------
def t483(b):
    b = set_field(b, "planner_name", jsstr("Eileen Glick (unconfirmed title)"))
    b = set_field(b, "planner_title", jsstr("Contact for planning questions — exact title not stated on source page"))
    b = set_field(b, "data_center_notes", jsstr(
        "Not confirmed — the township does have a real website (bertrandtwpmi.gov, found in verification pass), but no ordinance/docket review "
        "was completed this pass. Treat as a weak negative, not a confirmed one."))
    b = set_field(b, "notes", jsstr(
        "CONFIRMED (partial) 2026-08-05 (verification pass, Mo-supplied lead): bertrandtwpmi.gov/planning names Eileen Glick as the contact "
        "(\"reach out to Eileen Glick at (269) 591-7982 with any questions\") but does not state her title on that page — not asserting "
        "\"Zoning Administrator\" without a title confirmation. NOTABLE CROSS-CHECK: this is the same name as the confirmed Zoning Administrator "
        "at Milton Township, Cass County (id 524) — a different county, not adjacent. Could be the same contracted individual serving both, or "
        "a coincidence; flagged, not asserted either way. The earlier \"no township website found\" note was wrong — bertrandtwpmi.gov is real "
        "and accessible; lat/lng (Dayton community approximation) not yet corrected to a confirmed hall address. Bertrand Township borders "
        "Indiana (South Bend area)."))
    b = re.sub(r'sources:\s*\[[^\]]*\]', 'sources: ' + repr(["bertrandtwpmi.gov/planning", "en.wikipedia.org/wiki/Bertrand_Township,_Michigan"]).replace("'", '"'), b)
    return b
replace_block(483, t483, "483 Bertrand Township")

# ------------------------------------------------------------------
# 7. Sodus Township (id 496) — DEBUNKED lead re: Kevin Kolb
# ------------------------------------------------------------------
def t496(b):
    b = set_field(b, "notes", jsstr(
        "PULSE-CHECK 2026-08-05. No zoning administrator named on the site's Planning & Zoning or News pages. East-central Berrien County, near "
        "Watervliet. Lat/lng is an approximation; Wikipedia's article on this township carries no coordinates. DEBUNKED 2026-08-05 (verification "
        "pass): a Mo-supplied lead claimed a \"Kevin Kolb, Planning Commission secretary\" citing a SWMPC-hosted PDF (sodus111411.pdf) — that "
        "document is actually the township's 2008 Zoning Ordinance and contains no mention of that name anywhere. Not added to the record."))
    return b
replace_block(496, t496, "496 Sodus Township")

# ------------------------------------------------------------------
# 8. Watervliet Charter Township (id 498) — DEBUNKED Wightman lead (wrong citation)
# ------------------------------------------------------------------
def t498(b):
    b = set_field(b, "notes", jsstr(
        "PULSE-CHECK 2026-08-05. This would be Watervliet Charter TOWNSHIP, distinct from the City of Watervliet, a separate incorporated city "
        "surrounded by the township (also not to be confused with Watervliet, New York). Lat/lng is a rough estimate, not independently geocoded. "
        "Recommend a direct browser visit to wctwp.org. DEBUNKED 2026-08-05 (verification pass): a Mo-supplied lead claimed Wightman was "
        "\"retained by Watervliet Charter Township for ongoing planning commission assistance,\" citing an eagletownshipmi.gov PC packet PDF as "
        "its source — that document is actually Eagle Township's own Planning Commission agenda and does not mention Watervliet, Wightman, or "
        "Berrien County anywhere. The citation was simply wrong; treating the Wightman/Watervliet connection as unconfirmed, not as a lead worth "
        "chasing further absent a real source."))
    return b
replace_block(498, t498, "498 Watervliet Charter Township")

# ------------------------------------------------------------------
# 9. Berrien Township (id 482) — reported-not-confirmed Rogien/O'Dell; confirmed Wightman park project
# ------------------------------------------------------------------
def t482(b):
    b = set_field(b, "notes", jsstr(
        "PULSE-CHECK 2026-08-05. UPDATED same day (verification pass, Mo-supplied lead): a lead reported Ross Rogien (Building Inspector/Zoning "
        "Administrator — also confirmed elsewhere on this map at Bainbridge Twp id 480 and Pipestone Twp id 493, so plausible he covers a third "
        "township) and Karen O'Dell (Planning Commission Chair) for this township, citing berrientownship.org — that domain blocks all automated "
        "fetching (robots.txt), so this could NOT be independently verified this pass. Reported, not confirmed; not changing planner_name until "
        "directly verified. SEPARATELY CONFIRMED: Wightman (Benton Harbor-based engineering/planning firm) lists a real completed project for "
        "this township on its own portfolio site — Range Line Park (gowightman.com/projects/range-line-park) — narrower park-planning/"
        "infrastructure work, not general zoning or master-plan consulting, so not set as the township's primary firm. \"Berrien Township\" "
        "(around Berrien Center) is distinct from Berrien Springs (village), Berrien County itself, and any \"Berrien Charter Township\" naming "
        "(does not exist as a separate entity)."))
    return b
replace_block(482, t482, "482 Berrien Township")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(src)

print("PATCH COMPLETE. New file size:", len(src))
