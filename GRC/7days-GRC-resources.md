# 7-Day GRC Learning Plan (Governance, Risk & Compliance)

GRC is less about tools and more about **frameworks, judgment, and documentation**. Since you already know CIA triad, RBAC, and PTES from your TCS iON coursework, you can move fast through Day 1–2 and spend more time on the risk assessment and compliance days — that's where GRC actually differs from pure technical security.

Plan on ~3–4 focused hours/day. Each day ends with a small deliverable so you build an actual portfolio piece, not just notes.

---

## Day 1 — Foundations: What GRC Actually Is

**Learn:**
- The three pillars separately: Governance (direction/policy), Risk Management (identify/assess/treat), Compliance (adherence to laws/standards)
- Core vocabulary: asset, threat, vulnerability, likelihood, impact, inherent risk vs residual risk, risk appetite vs risk tolerance, control (preventive/detective/corrective), risk owner
- How GRC differs from — and feeds into — SOC/pentest/red team work

**Resources:**
- TryHackMe room — *Governance & Regulation*: https://tryhackme.com/room/cybergovernanceregulation (covers the GRC framework, GDPR, PCI DSS, ISO 27001, NIST 800-53 hands-on)
- TryHackMe blog — *Is GRC a Good Path Into Cyber Security*: https://tryhackme.com/resources/blog/is-grc-a-good-path-into-cyber-security-a-practical-guide-for-beginners
- NIST Glossary (bookmark for the whole week): https://csrc.nist.gov/glossary

**Deliverable:** A one-page glossary of 15 GRC terms in your own words.

---

## Day 2 — Governance

**Learn:**
- Governance structure: Board → CISO → Security team ("three lines of defense" model)
- Policy hierarchy: Policy → Standard → Procedure → Guideline
- Governance frameworks: **COBIT** (IT governance), **ISO/IEC 27001** (ISMS)

**Resources:**
- ISACA — COBIT Framework overview: https://www.isaca.org/resources/cobit
- ISACA — Credentialing/frameworks hub (also lists free IT Risk/Audit Fundamentals Certificates): https://www.isaca.org/credentialing
- Coursera — *Packt: GRC Fundamentals* (audit free, ~6 hrs, covers governance roles + framework selection): search "Packt GRC Fundamentals Coursera"

**Deliverable:** Draft a one-page mock "Acceptable Use Policy" for a fictional small company.

---

## Day 3 — Risk Management Fundamentals

**Learn:**
- Risk lifecycle: Identify → Assess → Treat → Monitor → Report
- Qualitative (Likelihood × Impact matrix) vs quantitative (**FAIR** — dollar-value loss exposure) risk assessment
- Risk treatment: Accept, Avoid, Transfer, Mitigate

**Resources:**
- NIST SP 800-30 Rev 1 — *Guide for Conducting Risk Assessments* (the best free primer on risk methodology): https://csrc.nist.gov/files/pubs/sp/800/30/r1/final/docs/sp800_30_r1.epub
- FAIR Institute — free FAIR Fundamentals training (student offer): https://www.fairinstitute.org/blog/free-fair-fundamentals-training-for-university-students-and-professors
- Coursera — *Foundations of Cyber Risk Management and FAIR* (free to audit): https://www.coursera.org/learn/foundations-of-cyber-risk-management-with-fair

**Deliverable:** Build a simple 5×5 Likelihood/Impact risk matrix in a spreadsheet.

---

## Day 4 — Compliance & Regulatory Frameworks

**Learn:**
- Global frameworks: **NIST CSF 2.0**, SOC 2, PCI DSS, GDPR, HIPAA
- India-specific: **DPDP Act 2023** + **DPDP Rules 2025** (notified Nov 14, 2025; full enforcement from May 2027; penalties up to ₹250 crore), **CERT-In** incident reporting (6-hour window, 180-day log retention)
- How to map controls across frameworks (e.g. ISO 27001 Annex A → NIST CSF functions)

**Resources:**
- NIST CSF 2.0 official page: https://www.nist.gov/cyberframework
- MeitY — official DPDP Act & Rules page: https://www.meity.gov.in/data-protection
- CERT-In — Directions under Section 70B (official): https://www.cert-in.org.in/Directions70B.jsp

**Deliverable:** Pick one framework (e.g. ISO 27001) and map 5 of its controls to their matching NIST CSF category.

---

## Day 5 — Practical Risk Assessment (Hands-On)

**Learn:**
- Building a **risk register** (asset, threat, vulnerability, likelihood, impact, inherent risk, existing controls, residual risk, treatment, owner, due date)
- Asset classification, Business Impact Analysis (BIA) basics, vendor/third-party risk basics

**Resources:**
- Search "NIST risk register template xlsx" or "ISO 27001 risk register template" for free downloadable templates
- Re-use the TryHackMe *Governance & Regulation* room from Day 1 as a live reference while you build your register: https://tryhackme.com/room/cybergovernanceregulation

**Deliverable:** Build a risk register with 10 realistic entries for a small org (e.g. a startup running AWS + a customer database).

---

## Day 6 — Audit, Controls Testing & GRC Tools

**Learn:**
- Internal vs external audit; control testing: design effectiveness vs operating effectiveness
- KPI vs KRI (Key Risk Indicator) reporting to leadership
- GRC platforms landscape: ServiceNow GRC, Archer, Vanta, Drata, Scrut (India-based, DPDP-focused)

**Resources:**
- ISACA credentialing hub — has a free-to-browse *Cybersecurity Audit Certificate* and *IT Audit Fundamentals Certificate* listing: https://www.isaca.org/credentialing
- Vanta and Drata both publish solid free blog content on control testing and audit prep — search "Vanta control testing guide" / "Drata SOC 2 audit prep"

**Deliverable:** Write a one-paragraph mock audit finding for one control in your Day 5 risk register (gap, evidence, recommendation).

---

## Day 7 — Advanced: Integration + Career Path

**Learn:**
- Bridge technical findings into GRC language — reframe one of your own pentest/CTF findings as a risk register entry with likelihood/impact scoring
- Certification roadmap:
  - **Entry:** ISC2 CGRC (formerly CAP): https://www.isc2.org/certifications/cgrc
  - **Mid:** ISACA CRISC (risk-focused): https://www.isaca.org/credentialing/crisc
  - **Senior:** ISACA CISM, ISO 27001 Lead Implementer/Lead Auditor

Given your OSCP priority, CRISC or ISO 27001 Lead Implementer would pair well later as a technical-to-GRC bridge credential — no rush on this now.

**Resources:**
- ISC2 CGRC overview + free study tools: https://www.isc2.org/certifications/cgrc/cgrc-self-study-resources
- ISACA CRISC page (10 free practice questions available): https://www.isaca.org/credentialing/crisc

**Deliverable:** Rewrite one of your own past technical findings (CTF box, VAPT report, or DVAIA work) as a formal risk register entry + one-paragraph executive summary. This is the strongest artifact from this week — use it in interviews.

---

## After Day 7

- Bundle the risk register + audit finding + policy doc into a small portfolio (GitHub repo or PDF) — GRC roles hire heavily on writing samples
- Next steps if going deeper: ISO 27001 Lead Implementer training, or NIST RMF (SP 800-37) for a more US-government-flavored risk framework
