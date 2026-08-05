# -*- coding: utf-8 -*-
# Adds/updates the Gun Plain / Cooper / Oshtemo / Richland / Dorr / Dexter Twp / Wayland / Otsego
# cluster (Kalamazoo + Allegan + Washtenaw Counties) researched 2026-08-05.
import io

path = "index.html"
with io.open(path, "r", encoding="utf-8") as f:
    src = f.read()

# ------------------------------------------------------------------
# 1. Bump LAST_UPDATED
# ------------------------------------------------------------------
old_date = 'const LAST_UPDATED = "2026-08-04"; // format: YYYY-MM-DD — set this by hand on every data update'
new_date = 'const LAST_UPDATED = "2026-08-05"; // format: YYYY-MM-DD — set this by hand on every data update'
assert old_date in src, "LAST_UPDATED anchor not found"
src = src.replace(old_date, new_date, 1)

# ------------------------------------------------------------------
# 2. Update existing Oshtemo Township entry (id 137)
# ------------------------------------------------------------------
old_oshtemo = '''      {
        id: 137,
        municipality: "Oshtemo Township",
        county: "Kalamazoo",
        type: "Township",
        lat: 42.2828,
        lng: -85.6797,
        planner_name: "Jodi Stefforia",
        planner_title: "Planning Director",
        firm: "In-House (City Staff)",
        employment_type: "In-House",
        status: "active",
        cwa_flag: false,
        cwa_alumni: false,
        data_center_case: true,
        data_center_notes: "Solar, wind, and BESS ordinances actively being drafted January 2026 with 400-foot setbacks from residential properties. Township taking proactive regulatory approach to renewable energy siting — one of first Michigan townships to comprehensively address all three energy types simultaneously.",
        notes: "West Kalamazoo County township with rapid residential growth. In-house planning staff. Drafting comprehensive solar/wind/BESS ordinances Jan 2026 with 400-ft setbacks — proactive energy policy leader in Southwest Michigan. | jstefforia@oshtemo.org, 269-216-5232. Colten Hutson (ZA) and Leeanna Harris also on staff.",
        work_history: null,
        sources: ["Oshtemo Township planning documents", "Solar/wind/BESS ordinance drafting Jan 2026"]
      },'''

new_oshtemo = '''      {
        id: 137,
        municipality: "Oshtemo Township",
        county: "Kalamazoo",
        type: "Township",
        lat: 42.2828,
        lng: -85.6797,
        planner_name: "Jodi Stefforia",
        planner_title: "Planning Director",
        firm: "In-House (City Staff)",
        employment_type: "In-House",
        status: "active",
        cwa_flag: false,
        cwa_alumni: false,
        data_center_case: true,
        data_center_notes: "UPDATED 2026-08-05: BESS developer identified — NewEdge Renewable Power, 260 MW facility on leased ag land near W Main St/S Van Kal St (Oshtemo/Almena border); not a formal application yet, just a lease + informal PC presentations (Aug/Oct 2025). Board paused BESS 5-2 Nov 11, 2025 (12-month, expires ~Nov 25, 2026); a 27-page draft BESS ordinance still not public as of early Aug 2026, first public draft targeted for the Aug 13, 2026 PC meeting. Separate 1-year data center moratorium moved through readings starting ~Mar 10, 2026 (no known applicant at the time — Supervisor Cheri Bell). A NEW 6-month large-scale solar moratorium had its first reading in mid-2026, second reading Aug 11, 2026. Oshtemo is part of a multi-township coalition challenging the MPSC's PA 233 authority to override local zoning for utility-scale BESS/solar/wind — now petitioned to the MI Supreme Court.",
        notes: "West Kalamazoo County township with rapid residential growth. In-house planning staff (Jodi Stefforia, Planning Director; Colten Hutson, ZA; Leeanna Harris) drives the BESS/data-center/solar ordinance work — NOT PCI or CWA (no connection to either found). Oshtemo separately hired Progressive Companies (planner Jason Ball, Sara Moring-Hilt) for an unrelated general zoning-ordinance rewrite (PC updates Jun 25 & Jul 23, 2026) — worth not conflating the two efforts. UPDATED 2026-08-05: active recall campaign (recalloshtemo.org, organizer Katherine/Katie Schneider, who also leads BESS opposition with Donita/Gary DeBruin) targeting Trustees Neil Sikora, Zak Ford, Kristin Cole, plus Supervisor Cheri Bell and Clerk Dusty Farmer — signature drive fell short for Nov 2026 ballot, next window Nov 2028. | jstefforia@oshtemo.org, 269-216-5232.",
        work_history: null,
        sources: ["Oshtemo Township planning documents", "WWMT — https://wwmt.com/news/local/oshtemo-township-battery-storage-system-vote-pause-board-residents-concern-environment-safety-renewable-energy-kalamazoo-county-west-michigan", "WWMT — https://wwmt.com/news/local/oshtemo-township-residents-organize-against-battery-storage-facility-plans-newedge-public-service-commission-wwmt", "Public Media Network — https://publicmedianet.org/news/community/oshtemo-township-board-advances-energy-ordinance-timeline-adopts-first-reading-of-solar-moratorium/", "Ballotpedia recall — https://ballotpedia.org/Town_board_recall,_Oshtemo_Township,_Michigan_(2025-2026)", "recalloshtemo.org"]
      },'''

assert old_oshtemo in src, "old Oshtemo block not found"
assert src.count(old_oshtemo) == 1, "Oshtemo block not unique"
src = src.replace(old_oshtemo, new_oshtemo)

# ------------------------------------------------------------------
# 3. Update existing Dexter Township entry (id 342)
# ------------------------------------------------------------------
old_dexter_twp = '''      {
        id: 342,
        municipality: "Dexter Township",
        county: "Washtenaw",
        type: "Township",
        lat: 42.4,
        lng: -83.87,
        planner_name: "Megan Masson-Minock (consultant) / Fletcher Reyher (in-house Director)",
        planner_title: "Consultant Planner / Director of Planning and Zoning",
        firm: "Carlisle/Wortman Associates",
        employment_type: "Contracted",
        status: "active",
        cwa_flag: true,
        cwa_alumni: false,
        data_center_case: true,
        data_center_notes: "Planning Commission has been actively drafting a dedicated Data Center Ordinance through 2025-2026 addressing siting, noise, and Master Plan compatibility.",
        notes: "Hybrid arrangement: CWA consultant plus in-house Director. (Firm listed as: Carlisle/Wortman Associates, Inc..)",
        work_history: null,
        sources: ["https://www.dextertownshipmi.gov/planning-commission/"]
      },'''

new_dexter_twp = '''      {
        id: 342,
        municipality: "Dexter Township",
        county: "Washtenaw",
        type: "Township",
        lat: 42.4,
        lng: -83.87,
        planner_name: "Megan Masson-Minock / Grayson Moore (consultants) / Fletcher Reyher, AICP (in-house Director)",
        planner_title: "Consultant Planners (CWA) / Director of Planning and Zoning",
        firm: "Carlisle/Wortman Associates",
        employment_type: "Contracted",
        status: "active",
        cwa_flag: true,
        cwa_alumni: false,
        data_center_case: true,
        data_center_notes: "UPDATED 2026-08-05: CWA contract CONFIRMED via Mar 18, 2025 Board consent-agenda item — Benjamin Carlisle signed for CWA; Megan Masson-Minock and Grayson Moore named as assigned consultants; $3,000/mo retainer w/ 5% annual escalation, $70-150/hr additional, term through Mar 31, 2028. Board imposed a 180-day data-center-permit moratorium effective Feb 17, 2026 (expires ~mid-Aug 2026 — imminent as of this writing, extension status unconfirmed). CWA's Apr 20, 2026 memo transmitted a 'reference framework' draft (65 dBA flat noise, 200/50 ft setbacks, PUE 1.3, 25% renewable) essentially identical in shape to CWA's other openers (Scio, Lenox). The May 5, 2026 revised memo — explicitly 'modified from Pittsfield Township' — tightened standards substantially (50/40 dBA day/night, 400/200 ft setbacks, PUE 1.2, 90% renewable, no nuclear, 500-ft residential buffer) — same Pittsfield-lineage propagation pattern seen at Dexter (city, separately) and Scio Township. A competing Washington Twp 'High-Energy-Intensive Development' template was submitted for comparison May 18, 2026 but not adopted. No developer/applicant on file anywhere — purely preemptive, matching Scio's pattern (Supervisor Kerry there: 'not been approached'). Still in discussion phase as of Jun 23, 2026 PC meeting — no public hearing, PC recommendation, or Board vote yet. MPRC member Joseph Spiegel (Jun 17, 2026 packet) disputed a '30-40 residents oppose' framing and requested a survey — real opposition size contested/likely larger.",
        notes: "Hybrid arrangement: CWA consultant plus in-house Director (Fletcher Reyher, AICP — unconfirmed whether Reyher is CWA-employed or independent township staff). Same CWA planner (Megan Masson-Minock) who drafted Berkley's zoning rewrite and co-handles Dundee Village and Sharon Township — see [[project-cwa-ordinance-pattern-comparison]] in P.A.C.T. project memory. (Firm listed as: Carlisle/Wortman Associates, Inc..)",
        work_history: null,
        sources: ["https://www.dextertownshipmi.gov/planning-commission/", "Dexter Twp PC Packet 04-28-2026 — https://www.dextertownshipmi.gov/wp-content/uploads/04-28-2026-PC-Packet-2.pdf", "Dexter Twp PC Packet 05-12-2026 (May 5 CWA memo) — https://www.dextertownshipmi.gov/wp-content/uploads/PC-Packet-05-12-2026.pdf", "Dexter Twp PC Packet 05-26-2026 — https://www.dextertownshipmi.gov/wp-content/uploads/PC-Packet-05-26-2026.pdf", "Dexter Twp MPRC Packet 06-17-2026 — https://www.dextertownshipmi.gov/wp-content/uploads/06-17-2026-MPRC-Packet.pdf", "Dexter Twp Board Packet 03-18-2025 (CWA contract) — https://www.dextertownshipmi.gov/wp-content/uploads/03182025-Regular-Packet-2.pdf", "Sun Times News — https://thesuntimesnews.com/dexter-township-and-the-complexity-of-data-centers/"]
      },'''

assert old_dexter_twp in src, "old Dexter Township block not found"
assert src.count(old_dexter_twp) == 1, "Dexter Township block not unique"
src = src.replace(old_dexter_twp, new_dexter_twp)

# ------------------------------------------------------------------
# 4. Insert 6 brand-new municipality entries before the closing "];"
# ------------------------------------------------------------------
anchor = '''        sources: ["The Daily News, March 16, 2026 — https://www.thedailynews.cc/articles/breaking-news-majority-of-sand-lake-village-council-resigns-along-with-finance-director-planning-commission-members/"]
      }
    ];'''
assert anchor in src, "insertion anchor (end of MUNICIPALITIES array) not found"
assert src.count(anchor) == 1, "insertion anchor not unique"

new_entries = '''        sources: ["The Daily News, March 16, 2026 — https://www.thedailynews.cc/articles/breaking-news-majority-of-sand-lake-village-council-resigns-along-with-finance-director-planning-commission-members/"]
      },
      {
        id: 453,
        municipality: "Gun Plain Charter Township",
        county: "Allegan",
        type: "Township",
        lat: 42.4442,
        lng: -85.6386,
        planner_name: "Lori Castello / \\"Mike\\" (staff, unconfirmed surname)",
        planner_title: "Planner/Zoning Administrator (PCI)",
        firm: "PCImi",
        employment_type: "Contracted",
        status: "active",
        cwa_flag: false,
        cwa_alumni: false,
        data_center_case: true,
        data_center_notes: "NEW 2026-08-05: BESS developer = Heron Energy Storage, LLC — Special Land Use/site plan for a BESS facility on Riverview Dr (Parcel #03-08-034-021-51), submitted Feb 2026, still under review (tabled repeatedly for missing decommissioning/financial-guarantee/emergency-access info) as of Jun 2026. Board requested a 6-month BESS moratorium (with authority to expand) approved by PC Jun 17, 2026. Separately, Data Center moratorium Ordinance 193 was passed Apr 2026 and EXTENDED TO ONE YEAR by May 20, 2026 (heavy public opposition at that hearing — fire safety, water use ~300M gal/day cited by a resident, bald eagle nest, property values). An Ad Hoc Data Center Ordinance Committee was formed Jun 17, 2026: Township Board members VanDenBerg & Albertson-Stowell, 2 PC members (TBD), 3 Citizens Coalition members (Ally Riston-Komroy, Lisa Mulder, Brad Seekman), 2 alternates (Robert Petric, Wendy Pedrolini). U-M's Dr. Sarah Mills (co-author of the Feb 2026 statewide data-center guidebook, already tracked as Auerbach/CWA's MAP webinar co-instructor) is noted in the May 20, 2026 PC minutes as holding an Aug 31, 2026 meeting IN DORR TOWNSHIP for township officials on data center ordinances — this specific meeting could not be independently corroborated outside the Gun Plain minutes (worth confirming directly). Coldwater Township (Branch Co.) — Michigan's one operational BESS site — invited Gun Plain's board to visit its facility (Jun 2026).",
        notes: "Contracted planning/zoning firm is Professional Code Inspections of Michigan, Inc. (PCI, pcimi.com) — 'Lori from PCI' referenced directly in Feb 18 & Jun 17, 2026 PC minutes (Mo's own downloaded copies). PCI ALSO serves Dorr, Otsego, and Wayland Townships (all in this same Allegan Co. cluster) plus 20+ other West Michigan municipalities out of its Dorr office — a parallel single-firm-across-multiple-townships pattern to the CWA/Auerbach pattern already tracked in Washtenaw/Wayne County. PC members: Robert Bennett (Chair), Paul Sullivan (Vice Chair), Diane Webber (Secretary), Dana Albertson-Stowell, Kelly McHugh, Wayne Novick, Bill Shannon. 'Mike' referenced alongside Lori in PC minutes is likely additional PCI staff (possibly Mike Burns, PCI's Plumbing/Mechanical Inspector, per PCI's Dorr staff roster) — surname not directly confirmed in Gun Plain's own minutes.",
        work_history: null,
        sources: ["Gun Plain Charter Township PC Minutes, Nov 19 2025 – Jun 17 2026 (Mo's direct downloads)", "gunplain.org — https://www.gunplain.org/resolution-2026-8-to-extend-the-temporary-moratorium-on-data-centers-from-ordinance-193/", "gunplain.org — https://www.gunplain.org/resolution-2026-9-to-impose-a-temporary-moratorium-on-future-battery-energy-storage-systems-bess/", "pcimi.com — https://www.pcimi.com/dorr/"]
      },
      {
        id: 454,
        municipality: "Cooper Charter Township",
        county: "Kalamazoo",
        type: "Township",
        lat: 42.345,
        lng: -85.57,
        planner_name: "Julie Johnston",
        planner_title: "Planning/Zoning Administrator (in-house)",
        firm: "In-House (City Staff)",
        employment_type: "In-House",
        status: "active",
        cwa_flag: false,
        cwa_alumni: false,
        data_center_case: true,
        data_center_notes: "NEW 2026-08-05: Township Board adopted Ordinance No. 283 (Jul 13, 2026) adding a general 'Moratorium on Emerging Land Uses' enabling clause (§120.95, up to 18 months total), then invoked it same day via Resolution 26-338 to impose a 6-month (extendable) moratorium specifically on Data Centers — no developer/applicant named anywhere, purely preemptive. A companion Resolution 26-337 imposes an unrelated subdivision/site-condo moratorium. Not yet picked up by regional press (WWMT/MLive/Fox17/Public Media Network) as of Aug 2026 — flew under the radar. A 'Final Master Plan' dated Jun 15, 2026 was adopted just ~4 weeks before the data-center moratorium; the moratorium's own text says its purpose is to allow time to amend that plan/zoning ordinance 'concerning data centers,' implying the brand-new plan doesn't yet address them. Referenced in Gun Plain Twp's Jan 21, 2026 PC minutes: 'Martin Township and Cooper Township are working on their Master Plans.'",
        notes: "No outside planning consultant identified — appears to be entirely in-house (Julie Johnston, Planning/Zoning Administrator). No connection found to CWA or PCI. Township attorney: Michael Homier, Foster Swift Collins & Smith P.C. PC minutes/agendas on the township website are stale (nothing posted past 2023), so PC-level deliberation ahead of the Jul 13, 2026 Board vote isn't publicly documented — worth a FOIA/records request.",
        work_history: null,
        sources: ["Ordinance 283 — https://www.coopertwp.org/wp-content/uploads/2026/07/Adopted-Ordinance-283-Moratorium-on-Emerging-Land-Uses.pdf", "Resolution 26-338 notice — https://www.coopertwp.org/wp-content/uploads/2026/07/Notice-of-Adoption-re-Resolution-26-338-Imposing-Temporary-Moratorium-on-Data-Centers.pdf", "Cooper Township Boards and Committees — https://www.coopertwp.org/boards-and-committees/", "Gun Plain Twp PC Minutes, Jan 21 2026 (Mo's direct download)"]
      },
      {
        id: 455,
        municipality: "Richland Charter Township",
        county: "Kalamazoo",
        type: "Township",
        lat: 42.3667,
        lng: -85.4614,
        planner_name: "Bradley S. Kotrba, AICP / Toby Hayes, AICP",
        planner_title: "Township Planning Consultant & Zoning Administrator",
        firm: "Williams & Works",
        employment_type: "Contracted",
        status: "active",
        cwa_flag: false,
        cwa_alumni: false,
        data_center_case: false,
        data_center_notes: "NEW 2026-08-05: Richland has NOT had a distinct data-center or BESS proposal, docket item, or moratorium — its only large-scale-energy matter is Consumers Energy's 'Liberty Farms Solar Energy Center' (~2,200 acres, 220 MW solar, NOT battery storage), which drew large, overwhelmingly-opposed multi-session public hearings concluding May 28, 2026 at Gull Lake Middle School. No final PC decision reported as of Aug 5, 2026 — Supervisor Bear Priest estimated 3-4 months' further deliberation from late May (i.e. roughly Aug-Sept 2026). NOTE: a separate data-center fight exists in Kalamazoo County's Pavilion Township (Franklin Partners LLC) — a DIFFERENT township, not Richland; don't conflate them.",
        notes: "Contracted firm is Williams & Works (Grand Rapids), NOT CWA or PCI — Bradley Kotrba and Toby Hayes both confirmed via township memos/LinkedIn. Docket for the solar case: richlandtwp.net/boards___officials/liberty_farms_solar_application.php. Unverified lead: a 'Richland Preservation Action Group' Facebook page appears tied to solar-opposition messaging but content couldn't be independently confirmed (page blocked automated access).",
        work_history: null,
        sources: ["Richland Twp Liberty Farms Solar docket — https://www.richlandtwp.net/boards___officials/liberty_farms_solar_application.php", "Richland Twp PC Packet 3-25-26 — https://cms2.revize.com/revize/richlandtwpkc/PC%20Packet%20A%203-25-26.pdf", "WMUK, May 28 2026 — https://www.wmuk.org/wmuk-news/2026-05-28/richland-residents-boo-chant-and-say-no-to-solar-during-final-liberty-farms-hearing", "Fox17 regional roundup — https://www.fox17online.com/news/local-news/kzoo-bc/kalamazoo/kalamazoo-area-communities-work-to-address-potential-large-scale-energy-storage-projects-in-the-region"]
      },
      {
        id: 456,
        municipality: "Dorr Township",
        county: "Allegan",
        type: "Township",
        lat: 42.7178,
        lng: -85.7942,
        planner_name: "Kirk Scharphorn Jr. / Jason Derry / Lori Castello",
        planner_title: "Zoning Administrator / Planner (PCI — functions as township's building dept. & zoning office)",
        firm: "PCImi",
        employment_type: "Contracted",
        status: "active",
        cwa_flag: false,
        cwa_alumni: false,
        data_center_case: true,
        data_center_notes: "MAJOR ACTIVE CASE, NEW 2026-08-05: Microsoft purchased ~272 acres off 144th Ave (near US-131) in 2024 for $48M+, ~128 acres for the data center footprint, plus an adjacent ~144-acre 'Microsoft West' parcel — one of several concurrent MI Microsoft sites (Gaines Twp ~414 ac 'South Campus', Lowell Twp ~235 ac 'Valley Three', the latter paused after opposition). Site is already zoned commercial/industrial, so NO rezoning is required and the project can proceed 'by right' — meaning no formal PC hearing has happened yet and none is required to start. Baxtel lists status as 'land bank,' planned year 2028 — no construction timeline confirmed. Heavy pre-application resident opposition since Dec 2025 (Facebook group 'Dorr Township MI – We the People,' ~100-person Jan 31 2026 meeting w/ state Reps. Jim DeSana & Joseph Fox, industrial hygienist Kristen Meghan Kelly; Microsoft held its own community workshop Feb 5, 2026). SEPARATELY, PC began preliminary BESS-ordinance discussion Feb 17, 2026 (Chair Dan Beute) — no BESS developer named, draft going to Township Attorney next, residents perceive it as connected to the Microsoft project though township frames it as a distinct, proactive item. Lakeshore Advantage (Holland-based regional economic-development org) is the one named partner organization beyond Microsoft itself. No Dykema Gossett or other cross-case law-firm connection found.",
        notes: "PCI (Professional Code Inspections of Michigan, pcimi.com) is confirmed on Dorr Township's own website as the contracted provider for permits, inspections, AND zoning questions — i.e., functionally the township's zoning administrator/building department, not merely a firm with an office located there. PCI's Dorr office serves 23+ West Michigan municipalities incl. Gun Plain, Otsego, and Wayland Townships in this same cluster (pcimi.com/dorr/) — worth treating as a parallel single-firm-across-multiple-townships pattern alongside the CWA/Auerbach pattern tracked elsewhere. No direct evidence found (yet) that PCI has personally reviewed the Microsoft site plan or is drafting the BESS ordinance language (that's going to the Township Attorney) — flagged as an inference, not confirmed.",
        work_history: null,
        sources: ["Dorr Twp Planning & Zoning page — https://www.dorrtownshipmi.gov/Departments/Planning-Zoning", "PCI Dorr ZA contact — https://www.pcimi.com/contact/dorr-township-za/", "WWMT — https://wwmt.com/news/local/dorr-township-planning-commission-discussion-battery-energy-storage-system-bess-residents-concerns-data-center-wwmt", "Data Center Dynamics — https://www.datacenterdynamics.com/en/news/microsoft-plans-data-centers-in-dorr-and-lowell-townships-applies-for-property-rezoning-in-gaines-townships/", "Baxtel — https://baxtel.com/data-center/microsoft-dorr-1", "Wilcox Newspapers — https://wilcoxnewspapers.com/data-center-opposition-continues-in-dorr-township/"]
      },
      {
        id: 457,
        municipality: "Wayland Township",
        county: "Allegan",
        type: "Township",
        lat: 42.6764,
        lng: -85.6367,
        planner_name: "Rebecca Harvey (PC consultant, firm unconfirmed) / Kirk Scharphorn Jr. (PCI, Zoning Administrator)",
        planner_title: "Township Zoning Consultant / Zoning Administrator",
        firm: "PCImi",
        employment_type: "Contracted",
        status: "active",
        cwa_flag: false,
        cwa_alumni: false,
        data_center_case: true,
        data_center_notes: "NEW 2026-08-05: Very active 2026 docket. Apr 8, 2026: Supervisor Roger VanVolkinburg asked the PC to begin drafting a data-center ordinance; a BESS draft was already awaiting Township Attorney language. Jun 10, 2026: PC discussed a 1-year data center moratorium (consultant Rebecca Harvey warned outright exclusion risks 'exclusionary zoning' liability) and reviewed the BESS ordinance; hearings set for July. Jul 8, 2026 (7-0 votes): ADOPTED a 12-month data center moratorium AND new BESS ordinance sections (Sec. 3.50 off-site BESS, Sec. 3.51 on-site BESS, amended Sec. 13.03) — minutes note the BESS ordinance was 'modeled after other communities' ordinances,' plausibly including neighboring Gun Plain/Oshtemo drafts. No BESS or data-center developer named — both efforts are preemptive, explicitly prompted by residents citing the Microsoft/Dorr Twp fight and Gaines Township data-center activity nearby. Separately, Wayland has an active, contentious SOLAR case: Blazing Star Solar LLC (Apex Clean Energy subsidiary), 125 MW on 13 parcels — approved 4-3 with conditions (50 dBA sound cap, decommissioning agreement) Jun 10, 2026, Findings of Fact approved Jul 8, 2026.",
        notes: "PCI (Professional Code Inspections of Michigan) is Wayland's contracted building/zoning firm — Kirk Scharphorn Jr. named as Zoning Administrator on the township's own site; PCI's Dorr-office roster also lists Lori Castello (Planner/ZA) and Mike Burns (Plumbing/Mechanical Inspector) — the same 'Lori' and likely the same 'Mike' referenced in Gun Plain Twp's PC minutes, confirming PCI staff cover both townships. HOWEVER the PC's actual day-to-day planning consultant of record in 2026 minutes is Rebecca Harvey ('Township Zoning Consultant') — her firm affiliation (PCI vs. independent) is UNCONFIRMED; commissioners separately email PCI directly for hearing-notice publication, so PCI retains at least an administrative role. A client testimonial on pcimi.com from 'Roger VanVolkinburg — Wayland Township Supervisor' corroborates the PCI relationship generally.",
        work_history: null,
        sources: ["Wayland Twp PC Minutes, Apr 8 2026 — https://waytwp.org/wp-content/uploads/2026/04/4-8-26-Draft.pdf", "Wayland Twp PC Minutes, Jun 10 2026 — https://waytwp.org/wp-content/uploads/2026/07/6-10-26.pdf", "Wayland Twp PC Minutes, Jul 8 2026 — https://waytwp.org/wp-content/uploads/2026/07/7-8-26-draft.pdf", "Wayland Twp Zoning & Planning page — https://waytwp.org/departments/zoning/", "PCI Dorr office roster — https://www.pcimi.com/dorr/", "Blazing Star Solar — https://www.blazingstarsolar.com/"]
      },
      {
        id: 458,
        municipality: "Otsego Township",
        county: "Allegan",
        type: "Township",
        lat: 42.4595,
        lng: -85.702,
        planner_name: "Brad Ade (PC Chair) — planning/zoning administered by PCI",
        planner_title: "Planning Commission Chair / Contracted Zoning Administration (PCI)",
        firm: "PCImi",
        employment_type: "Contracted",
        status: "active",
        cwa_flag: false,
        cwa_alumni: false,
        data_center_case: false,
        data_center_notes: "NEW 2026-08-05: No pending data-center or BESS application, moratorium, or ordinance yet — but explicitly queued up as next work: the Feb 9, 2026 Township Board minutes record PC Chair Brad Ade telling the board that once the 2026 Master Plan update is complete, the PC intends to work on 'updating/realigning Ordinances for renewable energy/battery storage, gravel mining, renewable energy, and data centers' — a direct, proactive signal almost certainly responding to next-door Gun Plain's Heron Energy Storage BESS fight and Dorr Township's Microsoft data-center fight. Current zoning ordinance on file is still the 2019 book with no BESS/data-center category. Master Plan public workshop held Feb 11, 2026.",
        notes: "Otsego Township's own site confirms Professional Code Inspections of Michigan, Inc. (PCI, pcimi.com) as its contracted building/planning/zoning provider — PCI's Dorr office explicitly lists Otsego Township among its 23+ served municipalities, alongside Gun Plain and Dorr Townships in this same cluster (plus Wayland). No CWA connection found. Local officials: PC Chair Brad Ade (pcchair@otsegotownship.org), Secretary Jeff Polonowski; Supervisor Michael Gudith, Clerk Jen Colin.",
        work_history: null,
        sources: ["Otsego Twp Building, Planning & Zoning — https://www.otsegotownship.org/building-planning-and-zoning/", "Otsego Twp Board Minutes, Feb 9 2026 — https://www.otsegotownship.org/wp-content/uploads/2026/03/Twp-Board-Meeting-Minutes-February-2026.docx.pdf", "PCI Dorr office service list — https://www.pcimi.com/dorr/"]
      }
    ];'''

src = src.replace(anchor, new_entries)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(src)

print("patched OK, new size", len(src))
