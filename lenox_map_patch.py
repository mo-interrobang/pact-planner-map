# -*- coding: utf-8 -*-
path = "index.html"
with open(path, encoding='utf-8') as f:
    content = f.read()

old_notes = "notes: \"CWA named on township website; Stephen Cassin confirmed as CWA planning consultant for Lenox Township. Township hall: 63775 Gratiot Ave, Lenox MI 48050. Township's domain migrated lenoxtwp.org -> lenox-mi.gov in 2026. Resident opposition hub: lenoxdatacenterinfo.org.\","
assert old_notes in content, "old_notes anchor not found"
new_notes = "notes: \"CORRECTED 2026-08-04 (evening): CWA planner is Shana Lengyel, confirmed via the March 23, 2026 PC minutes (prior attribution to Stephen Cassin was wrong). Township hall: 63775 Gratiot Ave, Lenox MI 48050. Township's domain migrated lenoxtwp.org -> lenox-mi.gov in 2026. Resident opposition hub: lenoxdatacenterinfo.org.\","
content = content.replace(old_notes, new_notes, 1)

old_dc_tail = "CWA/Stephen Cassin's specific role in drafting the ordinance text is NOT YET directly confirmed — the March 23 and June 2, 2026 PC minutes (most likely to contain the template language) could not be fetched (lenox-mi.gov blocks automated access) — worth a direct pull. See PACT-Vault Documents/CWA-Ordinance-Pattern-Comparison and People/Ben Carlisle.\","
assert old_dc_tail in content, "old_dc_tail anchor not found"
new_dc_tail = "RESOLVED 2026-08-04 (evening): CWA's drafting role is CONFIRMED — the March 23, 2026 PC minutes (Mo downloaded directly) show planner Shana Lengyel, 'with Carlisle Wortman Associates, the new Planner for Lenox,' presenting and walking the Commission through both draft ordinances (I-94 Development District rezoning + standalone Data Center ordinance, Sec. 719.157). Corrects prior misattribution to Stephen Cassin. Also from that meeting: noise cap referenced at a flat 65 dB at the property line (matches CWA's usual opening-bid pattern seen at Scio); a proposed 1,350 ft residential setback defended as needing to be 'defendable' / not exclusionary zoning; and — the clearest resident-driven win — data centers were moved from Permitted-by-Right to Special Land Use (discretionary review) status at a commissioner's push. See PACT-Vault Documents/CWA-Ordinance-Pattern-Comparison and People/Ben Carlisle.\","
content = content.replace(old_dc_tail, new_dc_tail, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("patched OK")
