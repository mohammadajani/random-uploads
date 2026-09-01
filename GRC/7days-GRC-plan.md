# 7-Day GRC Learning Plan (Governance, Risk & Compliance)

  

GRC is less about tools and more about **frameworks, judgment, and documentation**. Since you already know CIA triad, RBAC, and PTES from your TCS iON coursework, you can move fast through Day 1–2 and spend more time on the risk assessment and compliance days — that's where GRC actually differs from pure technical security.

  

Plan on ~3–4 focused hours/day. Each day ends with a small deliverable so you build an actual portfolio piece, not just notes.

  

---

  

## Day 1 — Foundations: What GRC Actually Is

  

**Learn:**

- The three pillars separately: Governance (direction/policy), Risk Management (identify/assess/treat), Compliance (adherence to laws/standards)

- Core vocabulary: asset, threat, vulnerability, likelihood, impact, inherent risk vs residual risk, risk appetite vs risk tolerance, control (preventive/detective/corrective), risk owner

- How GRC differs from — and feeds into — SOC/pentest/red team work (a pentest finding becomes a risk register entry, not just a report line)

  

**Resources:**

- TryHackMe path: *Governance, Risk and Compliance* — free-tier rooms exist, includes the well-regarded **"Governance & Regulation"** room

- YouTube: search "GRC Intro TryHackMe" and "GRC vs Cybersecurity vs Audit explained" for quick primers

- NIST Glossary (nist.gov/glossary) — bookmark this, you'll use it all week

  

**Deliverable:** A one-page glossary of 15 GRC terms in your own words.

  

---

  

## Day 2 — Governance

  

**Learn:**

- Information security governance structure: Board → CISO → Security team (the "three lines of defense" model: operations, risk/compliance oversight, internal audit)

- Policy hierarchy: Policy → Standard → Procedure → Guideline (know the difference — it's a common interview question)

- Governance frameworks at a high level: **COBIT** (IT governance), **ISO/IEC 27001** (ISMS — ties governance to risk to controls)

  

**Resources:**

- ISACA COBIT overview (isaca.org) — free intro material

- ISO 27001 free summary/poster PDFs from certification bodies (search "ISO 27001 Annex A controls list 2022") — the 2022 revision has 93 controls across 4 themes (Organizational, People, Physical, Technological)

- Coursera: *Packt — GRC Fundamentals* (audit for free, ~6 hrs, covers governance roles + framework selection)

  

**Deliverable:** Draft a one-page mock "Acceptable Use Policy" for a fictional small company — practice writing in policy language.

  

---

  

## Day 3 — Risk Management Fundamentals

  

**Learn:**

- The risk management lifecycle: Identify → Assess → Treat → Monitor → Report

- Qualitative vs quantitative risk assessment (Likelihood × Impact matrix vs **FAIR** model's dollar-value loss exposure)

- Risk treatment options: Accept, Avoid, Transfer (insurance/outsourcing), Mitigate

- Frameworks: **NIST SP 800-30** (risk assessment guide, free PDF), **ISO 31000** (general risk management), **FAIR** (Factor Analysis of Information Risk)

  

**Resources:**

- NIST SP 800-30 Rev 1 — free PDF on csrc.nist.gov, the single best primer on qualitative risk assessment methodology

- FAIR Institute (fairinstitute.org) — free "FAIR Fundamentals" material

- TryHackMe: "Pentesting Fundamentals" → look specifically at rooms tagged Risk/Governance for a risk-scoring exercise

  

**Deliverable:** Build a simple 5×5 Likelihood/Impact risk matrix in a spreadsheet.

  

---

  

## Day 4 — Compliance & Regulatory Frameworks

  

**Learn:**

- Global frameworks: **NIST CSF 2.0**, **SOC 2**, **PCI DSS**, **GDPR**, **HIPAA**

- India-specific (important for your context):

  - **DPDP Act 2023** + **DPDP Rules 2025** (notified Nov 14, 2025, phased compliance rollout, full enforcement from May 2027, penalties up to ₹250 crore) — India's GDPR-equivalent

  - **CERT-In directions** (incident reporting timelines, log retention)

  - **RBI/SEBI guidelines** if you're interested in fintech GRC roles

- How to read a control mapping (e.g., mapping ISO 27001 Annex A controls to NIST CSF functions)

  

**Resources:**

- NIST CSF 2.0 (nist.gov/cyberframework) — free, the most-referenced framework globally

- MeitY / CERT-In official site (cert-in.org.in) for actual directive text

- Search "DPDP Act 2023 compliance checklist" for practical breakdowns of Data Fiduciary obligations

  

**Deliverable:** Pick one framework (e.g. ISO 27001) and map 5 of its controls to what NIST CSF category they'd fall under.

  

---

  

## Day 5 — Practical Risk Assessment (Hands-On)

  

**Learn:**

- How to build and maintain a **risk register** (columns: asset, threat, vulnerability, likelihood, impact, inherent risk score, existing controls, residual risk, treatment, owner, due date)

- Asset classification (public/internal/confidential/restricted)

- Business Impact Analysis (BIA) basics — RTO/RPO concepts

- Third-party/vendor risk assessment basics

  

**Resources:**

- Free risk register templates — search "NIST risk register template xlsx" or "ISO 27001 risk register template"

- TryHackMe "Governance & Regulation" room walkthrough (if you get stuck, several write-ups exist on Medium)

  

**Deliverable:** Build a risk register with 10 realistic entries for a small org (e.g. a startup running AWS + a customer database) — this is a genuinely useful portfolio artifact for interviews.

  

---

  

## Day 6 — Audit, Controls Testing & GRC Tools

  

**Learn:**

- Internal vs external audit process; control testing: design effectiveness vs operating effectiveness

- Evidence collection basics, audit findings/reporting language

- KPI vs KRI (Key Risk Indicator) — how GRC teams report to leadership

- GRC platforms landscape (know these exist, don't need hands-on for all): ServiceNow GRC, Archer, Vanta, Drata, Scrut (India-based, DPDP-focused)

  

**Resources:**

- Vanta/Drata blogs — both publish genuinely good free educational content on control testing and audit prep

- ISACA free resources on audit fundamentals (isaca.org)

  

**Deliverable:** Write a one-paragraph mock audit finding for one control in your Day 5 risk register (state the gap, evidence, and recommendation — this is exact audit-report language).

  

---

  

## Day 7 — Advanced: Integration + Career Path

  

**Learn:**

- How to bridge technical findings into GRC language — take one of your own past pentest/CTF findings and reframe it as a risk register entry with likelihood/impact scoring (this is a strong differentiator: most GRC-only people can't do this, most technical people don't bother)

- Certification roadmap:

  - **Entry:** ISC2 CGRC (formerly CAP), CompTIA Security+ (if not already done)

  - **Mid:** ISACA CRISC (risk-focused), ISACA CISA (audit-focused)

  - **Senior:** ISACA CISM, ISO 27001 Lead Implementer/Lead Auditor

- Given your OSCP priority already noted, CRISC or ISO 27001 Lead Implementer would pair well later as a technical-to-GRC bridge credential — no rush on this now

  

**Resources:**

- ISACA CRISC exam outline (isaca.org) — read the domains even if not testing soon

- CYVITRIX / similar "GRC beginner to advanced" course on Udemy (mentioned as a 2026-updated option) if you want a structured paid course after this week

  

**Deliverable:** Rewrite one of your own past technical findings (from a CTF box, VAPT report, or the DVAIA work) as a formal risk register entry + one-paragraph executive summary. This is the single best artifact from this week — use it in interviews.

  

---

  

## After Day 7

  

- Keep the risk register + audit finding + policy doc from this week — bundle them into a small portfolio (even a GitHub repo or PDF) since GRC roles hire heavily on writing samples

- If you want to go deeper: ISO 27001 Lead Implementer training, or NIST RMF (SP 800-37) for a more US-government-flavored risk framework
