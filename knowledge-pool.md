# Resume Knowledge Pool — Shreyash Singh

**Purpose:** Complete inventory of what @resume-writer knows about you, split into **verified** (vault/skills/live GitHub/your chat answers) vs **missing** (you must supply). Fill `- [ ]` items or answer in chat — every answer upgrades the master resume directly. Nothing gets invented.

**Legend:** ✅ verified · ⚠️ partial, confirm · ❌ MISSING · 🗑️ removed at owner request

Last updated: 2026-10-02 *(master resume re-synced to v4)* · **Authoritative resume now
`/Users/shreyashsingh/Developer/Resume/master/resume.pdf` + `resume.tex` (v4, 2026-09-24, one page).**
The copy under `Job/resume/master/` is the stale 2026-08-25 v3 — do not submit it.
Earlier sources: `system/user.md`, `reference/projects/github-portfolio.md` (10 active repos via
`gh repo list`, 3 private), skill `shreyash-portfolio`, `projects/sentinel-fintech/docs/SENTINEL_COMPLETE_GUIDE.md`

---

## 1. Identity & Contact Block ⚠️ *(prints on every resume)*

| Item | Status |
|---|---|
| Full name | ✅ Shreyash Singh |
| Phone | ✅ +91-9302940213 |
| Email | ✅ shreyashsingh755@gmail.com |
| GitHub | ✅ [celestialgeeks](https://github.com/celestialgeeks) — 10 active repos |
| LinkedIn | ✅ https://linkedin.com/in/shreyash-singh755 (Composio search 2026-08-25, 90% confidence) |
| City printed | ⚠️ Indore — confirm what you want shown |
| Portfolio site | ❌ |
| Gender | ✅ Male |
| Date of Birth | ✅ 20 March 2004 |
| Enrollment no. | ✅ 0808cl231133 (SIH roster, college email 0808cl231133.ies@ipsacademy.org) |

## 2. Education ✅ mostly

| Item | Status |
|---|---|
| Degree 1 | ✅ B.Tech CSE (AI & ML), IPS Academy Indore — RGPV University, 2023→2027 |
| Graduation 1 | ✅ **June 2027** → resume line "Expected Jun 2027" |
| CGPA 1 | ✅ **7.0/10** → **CHANGED 2026-09-24: now PRINTED on the master resume.** The old "omit unless ≥7.5" rule no longer holds — confirm before reversing again. |
| Degree 2 | ✅ **BS in Data Science & Applications — Foundation Level, IIT Madras** (new; was absent from the 2026-08-25 pool) |
| Graduation 2 | ✅ **Expected Sep 2026** (Foundation level) |
| CGPA 2 | ✅ **6.2/10** — also printed on the master resume |
| Graduation % (till 6th Sem) | ✅ **66%** (7th sem in progress) |
| Class XII / X | ✅ 10th: 80%, MP Board (Madhya Pradesh Board of Secondary Education) · 12th: 63%, MP Board |
| Relevant coursework | ✅ DBMS · Operating Systems · DSA · Machine Learning · Distributed Systems |

## 3. Experience ⚠️ *(thinned)*

- ✅ **AI Call Agent "Sahaiy"** (Feb 2026, deployed Vercel; repo public) — call-agent platform; Vite 5 multi-page, vanilla JS ES modules, Supabase (Postgres+Realtime+Auth), custom-properties+BEM, Hinglish UX. ❌ client or personal? users/call volume?
- 🗑️ **Aero Technics** — REMOVED at your request (repo deleted 2026-08-25). Note: `system/user.md` still records it as a real Apr 2026 internship project; if you ever want it back as an experience bullet (no repo link needed), say the word and I'll reinstate from the vault record.
- Power BI Viva — academic presentation; coursework line only

## 4. Projects ✅ *(10 live repos)*

> **On master resume v4 (2026-09-24), in this order:** Sahaiy · IP-SAKTI Sahayak · Bharat Maps ·
> Routed-Monitoring. **Sentinel is no longer on the master resume** even though it remains the
> flagship repo — say so if you want it back. Poymarket-Algo and PnL-Calculator also dropped off.
> Verified detail now on the resume for IP-SAKTI Sahayak: seven segregated Qdrant collections,
> 2048-dim NVIDIA Nemotron embeddings, Patents Act Sec. 3(p) prior-art screening, Sarvam AI across
> 22 Indic languages, deterministic citation verifier + multi-factor confidence scorer, SSE
> reasoning-artifact filter, Biological Diversity Act ABS checker. Bharat Maps: 10 Hz dead-reckoning,
> GNSS outage detection ≈0.3 s, re-blend in 1 s, <10% drift target over 60 s, signed-APK OTA updates.

### Flagship: sentinel-fintech 🔒 (private, active — last push 2026-08-20)
Three modules on one event-streaming backbone: **AML/sanctions screening** (LLM entity resolution + vector fuzzy matching) · **real-time fraud detection** (behavioral profiling, graph anomaly detection, agentic alert triage) · **automated merchant approval** (KYB/KYC, RAG document extraction, dynamic risk scoring).
Stack verified: FastAPI+Uvicorn · PostgreSQL+Redis · Milvus · Neo4j (Cypher money-trail, circular-flow & structuring detection) · Kafka · LangChain/LlamaIndex/HF Transformers · Docker→K8s · Prometheus+Grafana · GitHub Actions · pytest(25 passing)+Locust · JWT · 18 API endpoints.
❌ Public link/demo video (repo private) · ⚠️ perf numbers (<500ms, >90% TP, <15% FP) are DESIGN TARGETS until measured

### Quant cluster ✅
- **Poymarket-Algo** 🌐 — Polymarket lags Binance BTC by 10–30s; K-Means regime detector → LightGBM YES/NO classifier; leakage-free time-series validation
- **PnL-Calculator** 🌐 — native macOS SwiftUI "Liquid Glass" P&L calc (zero web views)

### Infra / LLM-infra cluster ✅
- **Freellm-Ollama** 🌐 — key-pooling proxy daemon for Ollama Cloud; proactive rotation at 97% quota / reactive on 429; OpenAI-compatible endpoint → frontier models ~$0 cost
- **Routed-Monitoring** 🌐 — multi-account LLM routing + Token Monitor UI tracking 28+ AI coding tools
- **Contest** 🔒 — Solana token launchpad REST API (Express+TS, Prisma, PostgreSQL, JWT/bcrypt middleware)
- **mini-solana-validator** 🔒 — in-memory Solana JSON-RPC validator in Node.js; binary wire-format txs, base58/multi-sig verification, atomic snapshot rollback; SPL Token + ATA PDAs; web3.js-compatible

### Web / product cluster ✅
AI-Call-Agent (above) · Advisor-profile (Next.js App Router) · Telegram_bot (Pyrogram bulk downloader, resumable, rate-limit aware)

### Resume angles ✅
fintech+compliance ML · latency-arb quant systems · crypto infra · LLM infra at $0 · end-to-end product delivery · agentic engineering (Sentinel verification loop)

## 5. Skills ✅ *(as shipped on master v4, 2026-09-24)*

The v4 resume restricts skills to tech **evidenced in its four listed projects**, so this list is
now narrower and different from the 2026-08-25 pool.

- **Languages:** Python, TypeScript, JavaScript, SQL, HTML5, CSS3, Bash
- **Frontend:** **React**, Next.js, React Native, Expo, Vite, Tailwind CSS, Vanilla JS
- **Backend:** FastAPI, REST APIs, Server-Sent Events (SSE), Pydantic, Supabase, PostgreSQL
- **AI / LLM:** RAG, Vector Search, Qdrant, Semantic Embeddings, NVIDIA NIM, Ollama, Prompt Engineering, Hallucination Mitigation, Multilingual NLP (Sarvam AI)
- **Mobile & Geospatial:** Android, MapLibre GL, OSRM, Dead Reckoning, GNSS/IMU, Offline-First Design
- **DevOps & Testing:** Git, Docker, Docker Compose, Vercel, Render, GitHub Releases, Pytest
- ⚠️ **React reversal (2026-09-24):** the 2026-08-25 note said React was removed at your request and
  would not reappear unless you reversed it. v4 lists it under Frontend, so treat that removal as
  **reversed** — but confirm before citing React as a strength in interview prep.
- ⚠️ **Dropped from v4 vs the old pool:** Java, Spring Boot, Maven, MySQL, Power BI, Arduino, Kafka,
  Neo4j/Cypher, Milvus, LangChain, LlamaIndex, HF Transformers, K8s, Prometheus/Grafana, Prisma,
  Node/Express, Swift/SwiftUI, Solana/crypto stack. Still true of you, just not resume-claimed.
- ❌ Years-of-exposure per language · ⚠️ interview-survival rule applies before any skill is listed

## 6. Certifications / Awards / Extras ⚠️

- ✅ **Introduction to Internet of Things — NPTEL Online Certification, IIT Kharagpur** (Elite; funded
  by MoE, Govt. of India). Roll No `NPTEL26CS37S856401299`, 12-week course Jan–Apr 2026, consolidated
  **66%** (assignments 16.63/25, proctored exam 49.5/75), 4 credits recommended. PDF: Google Drive →
  `Documents/S- Documents/NPTEL Certificate.pdf`. ⚠️ Certificate shows only a month range — forms
  demanding DD-MM-YYYY need a judgement call, so flag it.
- ✅ **Open-source contribution** — multi-account Ollama support contributed upstream to the Token
  Monitor repo (now stated on master v4 via Routed-Monitoring).
- [ ] Claude Certified Architect — done or in progress?
- [ ] DeepLearning.AI short courses completed?
- [ ] Hackathons / competitions / leadership — SIH 2026 filings (PS-168 Bharat Maps, PS-45 IP-SAKTI)
      are on the resume as project tags, not yet listed as competition entries
- [ ] Blogs / publications

## 7. Target Role ✅

FDE / AI Engineer at Palantir, OpenAI, Anthropic-class; India-market roles tracked (`raw-postings/india/`). Long-term independent products; near-term freelance income. Deep company research exists for AIB Technovations (Indore): `reference/research/job-research/aib-technovations/`.

## 8. My capability pool ✅

Workflow skill `resume-workflow` (gather → diff plan → LaTeX → compile → ATS plain-text → notes.md). Templates compile-tested under tectonic 0.17.0: base-jake ✅, base-moderncv ✅, base-cover-letter ✅; base-awesome-cv + base-deedy pending font/macro fixes. ATS research library at `reference/research/resume/ats-research/`. Knowledge layers: vault reference docs + Hermes skills (~160 incl. `shreyash-portfolio`, `hermes-agentic-arsenal`) + agent memory.

---

## 🎯 Remaining blockers (updated)

1. **LinkedIn URL** — ✅ resolved: https://linkedin.com/in/shreyash-singh755 (2026-08-25) · contact block complete
2. Class XII/X details (India portals)
3. Sentinel public link/demo + achieved-vs-target metrics when Phase 6–8 land
4. Sahaiy: client-or-personal + usage numbers
5. Cert statuses (Claude Architect, DLAI)
6. Interview-survival pass + years-per-language

Answer any subset in chat — I fold answers back here immediately.
