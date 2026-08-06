# -*- coding: utf-8 -*-
# Verification pass, 2026-08-05 (pass 5, same project): Mo supplied a third round
# of AI-assisted research, this time on Van Buren County "Unknown planner"
# townships. Same approach as the Berrien verification pass — check every claim
# against its cited primary source before writing it in. Two more claims did
# NOT survive (Bloomingdale's supervisor name is simply wrong; Columbia Twp's
# citation resolves to the WRONG Columbia Township — Jackson County, not Van
# Buren — the exact mix-up already flagged in this entry's own notes).
import io
import re

path = "index.html"
with io.open(path, "r", encoding="utf-8") as f:
    src = f.read()

def get_block(id_):
    marker = "        id: %d,\n" % id_
    start = src.index(marker)
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
    pattern = re.compile(r'(' + re.escape(field) + r':\s*)"(?:[^"\\]|\\.)*"(,?)', re.S)
    m = pattern.search(block)
    assert m, "field %s not found in block" % field
    return block[:m.start()] + field + ": " + new_value_js_string_literal + m.group(2) + block[m.end():]

def jsstr(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def set_sources(block, sources_list):
    return re.sub(r'sources:\s*\[[^\]]*\]', 'sources: ' + repr(sources_list).replace("'", '"'), block)

# ------------------------------------------------------------------
# 1. Arlington Township (id 502) — CONFIRMED: Ryan Laylin + Peggy Douglas.
#    McKenna claim DEBUNKED — Master Plan actually credits SWMPC assistance.
# ------------------------------------------------------------------
def t502(b):
    b = set_field(b, "planner_name", jsstr("Ryan Laylin"))
    b = set_field(b, "planner_title", jsstr("Zoning Administrator & Ordinance Enforcement Officer"))
    b = set_field(b, "firm", jsstr("In-House (City Staff)"))
    b = set_field(b, "employment_type", jsstr("In-House"))
    b = set_field(b, "data_center_notes", jsstr("No data center/BESS/moratorium activity found this pulse-check pass (2026-08-05)."))
    b = set_field(b, "notes", jsstr(
        "CONFIRMED 2026-08-05 (verification pass, Mo-supplied lead): arlingtontownship.com/contact-info/ directly names Ryan Laylin as Zoning "
        "Administrator & Ordinance Enforcement Officer and Peggy Douglas as Planning Commission Chairperson. This is now the THIRD township on "
        "this map with a Ryan Laylin in a zoning role — also Keeler Township (id 511) and, less certainly, Silver Creek Township, Cass County "
        "(id 530) — a real pattern of one contracted/shared individual across at least Arlington and Keeler (both Van Buren), worth a light "
        "confirmation call. A separate claim that McKenna Associates is Arlington's \"designated professional planning consulting firm\" did NOT "
        "survive a direct check: the township's own 2024 Master Plan draft states \"This Plan was prepared by the Arlington Township Planning "
        "Commission (Matt Butler, Ron Klein, Tina Loomis, Bill Handlang, Donna Bell) with assistance from the Southwest Michigan Planning "
        "Commission\" — McKenna is not mentioned anywhere in it. Not treating the McKenna claim as confirmed; SWMPC assisted with the Master Plan "
        "specifically, day-to-day zoning is in-house via Laylin. IMPORTANT — there is a separate, unrelated Arlington Charter Township in Tuscola "
        "County, Michigan."))
    b = set_sources(b, ["arlingtontownship.com/contact-info/", "arlingtontownship.com/wp-content/uploads/2024/09/Arlington-Twp-Master-Plan-Draft-2024-1.pdf", "en.wikipedia.org/wiki/Arlington_Township,_Van_Buren_County,_Michigan"])
    return b
replace_block(502, t502, "502 Arlington Township")

# ------------------------------------------------------------------
# 2. Bangor Township (id 503) — CONFIRMED: Mike Sullins, Supervisor
# ------------------------------------------------------------------
def t503(b):
    b = set_field(b, "notes", jsstr(
        "PULSE-CHECK 2026-08-05, updated in verification pass same day (Mo-supplied lead): Mike Sullins confirmed directly as Township Supervisor "
        "(vanburencountymi.gov directory). A supplementary claim that the township \"rescinded its independent planning committee ordinance to "
        "handle land-use rules directly via the board\" was not independently checked against the ordinances page this pass — plausible given no "
        "standalone Planning Commission was found in earlier research, but not confirmed as stated; treat as a reasonable inference, not a verified "
        "fact. Confirmed no standalone township website — all information is hosted on vanburencountymi.gov. IMPORTANT DISAMBIGUATION — there is a "
        "much larger, more prominent Bangor Charter Township in Bay County, Michigan (near Bay City); confirm any secondary sourcing is about Van "
        "Buren County's Bangor Township, not Bay County's."))
    return b
replace_block(503, t503, "503 Bangor Township")

# ------------------------------------------------------------------
# 3. Bloomingdale Township (id 504) — CORRECTION: supervisor is Matthew
#    Ashbrook, NOT "Bernie Scholten" as claimed — that name doesn't
#    independently corroborate anywhere (Ballotpedia + county directory
#    both confirm Ashbrook).
# ------------------------------------------------------------------
def t504(b):
    b = set_field(b, "notes", jsstr(
        "PULSE-CHECK 2026-08-05. Confirmed no standalone township website — all information is hosted on vanburencountymi.gov. The incorporated "
        "Village of Bloomingdale sits within/adjacent to the township and is a separate governmental entity — do not conflate village records with "
        "township records. CORRECTION 2026-08-05 (verification pass): a Mo-supplied lead named the Supervisor as \"Bernie Scholten\" — this does "
        "NOT corroborate against any source checked. The actual confirmed Supervisor is Matthew L. Ashbrook (Ballotpedia candidate page + the "
        "township's own Van Buren County directory listing both independently confirm this; Ashbrook also appears as a current Van Buren County "
        "Farm Bureau board member under the same township). Not using \"Bernie Scholten\" anywhere in this record — likely simply incorrect, "
        "possibly from a stale or unrelated source."))
    return b
replace_block(504, t504, "504 Bloomingdale Township")

# ------------------------------------------------------------------
# 4. Columbia Township, Van Buren Co. (id 505) — the newly-cited domain for
#    a "Kevin Reszka, Supervisor" claim turned out to be the WRONG Columbia
#    Township (Jackson County) — the exact disambiguation risk this entry
#    already warns about. Not confirming Reszka; adding a note about this
#    specific new instance of the mix-up.
# ------------------------------------------------------------------
def t505(b):
    old_notes_marker = 'high risk of mix-up, especially for the still-unconfirmed lawsuit claim.'
    assert old_notes_marker in b
    addition = (' NEW INSTANCE OF THIS EXACT MIX-UP, 2026-08-05 (verification pass): a Mo-supplied lead claimed a \\"Kevin Reszka, Township '
        'Supervisor\\" overseeing this township\'s Planning Commission — the domain used to reach that claim (twp.columbia.mi.us) was directly '
        'checked and is CONFIRMED to be Columbia Charter Township, Jackson County, MI (Brooklyn, MI 49230; Clerk Cathy Hulburt), not Van Buren '
        'County\'s Columbia Township. Not treating the Kevin Reszka claim as confirmed for this entry.')
    b = b.replace(old_notes_marker, old_notes_marker + addition)
    return b
replace_block(505, t505, "505 Columbia Township (Van Buren Co.)")

# ------------------------------------------------------------------
# 5. Hartford Township (id 510) — Jim Lechenet claim did NOT survive
# ------------------------------------------------------------------
def t510(b):
    b = set_field(b, "notes", jsstr(
        "PULSE-CHECK 2026-08-05. No named zoning administrator found on the Ordinances or Officials pages. Lat/lng is an approximation using the "
        "City of Hartford vicinity (no hall street address found). CHECKED 2026-08-05 (verification pass): a Mo-supplied lead named \"Jim "
        "Lechenet\" as Zoning Administrator, citing hartfordmichigan.com (a different domain than hartfordtownship.org, already the source used "
        "here) and an energyzoning.org-hosted ordinance PDF. The energyzoning.org document was checked directly — it names the Zoning Administrator "
        "role generically (\"appointed by the Zoning Commission\") but does not name Jim Lechenet or anyone else. Not confirmed; leaving planner_name "
        "as Unknown."))
    return b
replace_block(510, t510, "510 Hartford Township")

# ------------------------------------------------------------------
# 6. Waverly Township (id 517) — Tasha Smalley / MTS claim not found on
#    the specific page checked
# ------------------------------------------------------------------
def t517(b):
    b = set_field(b, "notes", jsstr(
        "PULSE-CHECK 2026-08-05. No named planner/zoning administrator currently published on the township's own site. CHECKED 2026-08-05 "
        "(verification pass): a Mo-supplied lead claimed Tasha Smalley (already confirmed elsewhere on this map as South Haven Charter Township's "
        "Zoning Administrator via Michigan Township Services, id 516) also covers Waverly Township through MTS — plausible given MTS's confirmed "
        "multi-township footprint in this county, but neither her name nor Michigan Township Services appears on waverlytownship-vbcmi.gov/building, "
        "the page cited. Not confirmed; leaving planner_name as Unknown pending a direct check of the township's Zoning (rather than Building) page."))
    return b
replace_block(517, t517, "517 Waverly Township")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(src)

print("PATCH COMPLETE. New file size:", len(src))
