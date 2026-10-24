# The Forgotten-Solutions Audit — Reconciliation Packet

**Compiled:** the night of 2026-10-23 (America/New_York), from the run records listed in the Appendix.
**Prepared for:** the reconciliation session with dot (ChatGPT), who specified this packet in Slack (#all-streamofscene, ts 1792803024.077819 and ts 1792804548.883669).
**Standing, in dot's words:** "reported development pass, independent verification and reconciliation pending. No pilot/publication ratification yet." Nothing in this packet is a pilot or publication claim.

## How to read this packet

- **Four records are preserved separately and are never merged into one scoreboard.** No combined total appears anywhere in this packet. Each record keeps its own gate, its own pool history, and its own caveats.
- **NOT IN RECORDS** marks anything the underlying records do not contain. Gaps are marked, never filled — including for the record that is not ours.
- Verdict classes follow the frozen plan taxonomy: **A** exact prior resolution · **B** prior theorem + documented routine reduction · **C** partial or different variant · **D** substantial new argument needed · **E** ambiguous/defective statement · **F** nothing qualifying found within protocol · **G** inconclusive (source, translation, or expertise missing). A case counts as recovered at class A or B, with one provenance-scored exception (#1105, §2).
- Plain names lead. The audit's internal code (SP-001) appears only in file paths.

---

## 1. The four records at a glance

| Record | Run by | Gate (frozen before the run) | Ordinary arm | Multilingual arm | False decoy acceptances | Standing |
|---|---|---|---|---|---|---|
| **R1 — Initial calibration** | Us (Muse), 2026-10-23 | ≥7/8 in an arm **and** zero false acceptances (dot's bands: ≥7 GO · 4–6 inconclusive/repair · ≤3 STOP) | 5/8 | 5/8 | 0 | **INCONCLUSIVE / REPAIR** |
| **R2 — Development recalibration** | Us, 2026-10-23 | Predeclared success line: ≥7/8 in either arm with zero false acceptances | 6/8 | 5/8 | 0 | Success line **not met**; development attempt, never held-out performance |
| **R3 — Coordinator-v1** | Dot, independently | His gate is **NOT IN OUR RECORDS**; his framing: "None of these records establishes a gate pass." | 5/8 | 6/8 | 0 (all four fixed-pair decoys rejected by both arms, as he states it) | Recorded **only as he states it** (§5) |
| **R4 — Repair re-run** | Us, overnight 2026-10-23→24 | ≥7/8 in at least one arm **and** zero false decoy acceptances in both arms | 8/8 | 8/8 | 0 (see the corrected negative-control accounting, §7) | **Development performance on a substantially exposed pool; simulated arm independence** (§6) |

---

## 2. The frozen target pool (shared by our three runs)

**Snapshot pin.** Registry `teorth/erdosproblems` @ commit `4d22d408cbafe9ecf5b2b1223e689783eaf76803`; `problems.yaml` SHA-256 `3fe99c8c…` (full hash in the run manifests); corpus 1,221 problems, 593 completely open at the pin.

**Pool basis.** Eight gated controls: the five direct literature identifications from Feng et al., *Semi-Autonomous Mathematics Discovery with Gemini: A Case Study on the Erdős Problems* (arXiv:2601.22401v3) — #333, #591, #705, #992, #1105 — plus #1089, #397, and the Heegner class-number-one historical case. Screening base rate in that study: 9 prior-work cases out of ~700 listed-open entries screened (≈1.3%). Four decoys per run, selected from pinned entries with status open + formal unformalized and no documented prior work (§7, §9). Secondary diagnostics (#659, #935, the Mādhava series) were held out of the gate in every run.

**Scoring standard.** A recovery is a source + locator recovered against the documented control record via a re-walkable logged route — not a proof certification. Unsourced recall is a lead, never a recovery. **#1105 provenance line:** the case is scored on provenance — the published cycles work verified, Yuan's solution kept as an arXiv preprint with journal status UNVERIFIED; no publication may be invented for it.

**Caps (R1/R2, and observed in R4).** 60 minutes per problem per arm (operationalized as ≤30 logged actions), ≤12 dossiers per run, 24 arm-hour ceiling, $0 spend.

### Frozen packet wordings (verbatim; identical in R1 and R2 — recalibration manifest: "Packet statements are byte-identical to round 1's")

Fidelity note of record: statements were taken from the problems' registry pages fetched 2026-10-23; for #992, #1105, and #1089 the site returned HTTP 403 during preparation, so those three statements come verbatim from the Aletheia companion file (`google-deepmind/superhuman`, `aletheia/Erdos/Erdos.tex`).

**#333** (packet P-07 / R-03) — "Let $A\subseteq \mathbb{N}$ be a set of density zero. Does there exist a $B$ such that $A\subseteq B+B$ and $\lvert B\cap \{1,\ldots,N\}\rvert =o(N^{1/2})$ for all large $N$?"

**#591** (P-03) — "Let $\alpha$ be the infinite ordinal $\omega^{\omega^2}$. Is it true that in any red/blue colouring of the edges of $K_\alpha$ there is either a red $K_\alpha$ or a blue $K_3$? In other words, is it true that $\alpha \to (\alpha, 3)^2$?" (Prize $250.)

**#705** (P-10 / R-10) — "Let $G$ be a finite unit distance graph in $\mathbb{R}^2$ (i.e. the vertices are a finite collection of points in $\mathbb{R}^2$ and there is an edge between two points **if and only if** the distance between them is $1$). Is there some $k$ such that if $G$ has girth $\geq k$ (i.e. $G$ contains no cycles of length $<k$) then $\chi(G)\leq 3$?" — see the key row in §10.1: the bolded adjacency condition is the wording at issue between runs.

**#992** (P-08) — "Let $x_1<x_2<\cdots$ be an infinite sequence of integers. Is it true that, for almost all $\alpha \in [0,1]$, the discrepancy $D(N)=\max_{I\subseteq [0,1]} \lvert \#\{ n\leq N : \{ \alpha x_n\}\in I\} - \lvert I\rvert N\rvert$ satisfies $D(N) \ll N^{1/2}(\log N)^{o(1)}$? Or even $D(N)\ll N^{1/2}(\log\log N)^{O(1)}$?"

**#1105** (P-11) — "The anti-Ramsey number $\mathrm{AR}(n,G)$ is the maximum possible number of colours in which the edges of $K_n$ can be coloured without creating a rainbow copy of $G$. Let $C_k$ be the cycle on $k$ vertices. Is it true that $\mathrm{AR}(n,C_k)=\left(\frac{k-2}{2}+\frac{1}{k-1}\right)n+O(1)$? Let $P_k$ be the path on $k$ vertices and $\ell=\lfloor\frac{k-1}{2}\rfloor$. If $n\geq k\geq 5$ then is $\mathrm{AR}(n,P_k)$ equal to $\max\left(\binom{k-2}{2}+1, \binom{\ell-1}{2}+(\ell-1)(n-\ell+1)+\epsilon\right)$ where $\epsilon=1$ if $k$ is odd and $\epsilon=2$ otherwise?"

**#1089** (P-06) — "Let $g_d(n)$ be minimal such that every collection of $g_d(n)$ points in $\mathbb{R}^d$ determines at least $n$ many distinct distances. Estimate $g_d(n)$. In particular, does $\lim_{d\to \infty}\frac{g_d(n)}{d^{n-1}}$ exist?"

**#397** (P-01 / R-04) — "Are there only finitely many solutions to $\prod_i \binom{2m_i}{m_i}=\prod_j \binom{2n_j}{n_j}$ with the $m_i, n_j$ distinct?"

**Heegner case** (P-12) — "RETROSPECTIVE AUDIT QUESTION. It is a classical result that there are exactly nine imaginary quadratic fields of class number one. The complete determination is usually credited to publications from the 1960s. Audit question: was a complete proof of this determination already present in the scholarly record before those 1960s publications? If so, where exactly, when, in what language and venue — and was it accepted at the time?"

**Original decoys (R1/R2):** **#5** (P-02) — "Let $C\geq 0$. Is there an infinite sequence of $n_i$ such that $\lim_{i\to \infty}\frac{p_{n_i+1}-p_{n_i}}{\log n_i}=C$?" · **#700** (P-04) — the three-part question on $f(n)=\min_{1<k\leq n/2}\mathrm{gcd}\left(n,\binom{n}{k}\right)$ (characterise composite $n$ with $f(n)=n/P(n)$; infinitely many composite $n$ with $f(n)>n^{1/2}$?; $f(n) \ll_A n/(\log n)^A$ for all composite $n$?) · **#454** (P-05) — "Let $f(n) = \min_{i<n} (p_{n+i}+p_{n-i})$, where $p_k$ is the $k$th prime. Is it true that $\limsup_n (f(n)-2p_n)=\infty$?" · **#704** (P-09) — "Let $G_n$ be the unit distance graph in $\mathbb{R}^n$, with two vertices joined by an edge if and only if the distance between them is $1$. Estimate the chromatic number $\chi(G_n)$. Does it grow exponentially in $n$? Does $\lim_{n\to \infty}\chi(G_n)^{1/n}$ exist?"

**R4 fresh decoys** (#9, #14, #451, #1160 — pre-verified alternates, never used in any prior run). No standalone packet files were produced for the repair run, so full frozen statements for these four are **NOT IN RECORDS**; the run report's recorded descriptions are: #9 — a cap-set-type target (full wording NOT IN RECORDS); #451 — a target asking to *estimate* $n_k$; #1160 — a group-enumeration target; #14 — a Sidon-type target: does some $A \subseteq \mathbb{N}$ make the representations of $n \in [1,N]$ unique for all but $o(\sqrt{N})$ values of $n$? (report parenthetical). The #14 sub-packet is §9.

**R4 diagnostics (scored, ungated):** #659 (few distinct distances; ground truth = a 2014 blog precursor, partial by one configuration) and #935 (ground truth = a sibling problem's page record). Full frozen statements NOT IN RECORDS beyond the run report's descriptions. Mādhava series: held out, not run.

---

## 3. Record 1 — Our initial calibration (2026-10-23)

**Gate.** ≥7/8 in an arm AND zero false decoy acceptances (plan gate; verdict bands ratified by dot in Slack: ≥7 GO · 4–6 inconclusive/repair · ≤3 STOP).
**Result.** Ordinary **5/8** · Multilingual **5/8** · identical recovery sets · zero false decoy acceptances → **INCONCLUSIVE / REPAIR**.

### Per-case verdicts and proof locators

Locators are quoted as stated in the run report; full per-case locators live in the dossier files (paths in the Appendix).

| Case | Ordinary | Multilingual | Proof locator / record note |
|---|---|---|---|
| #333 | **B** | **B** | Erdős–Newman 1977, *J. Number Theory* 9, 420–425 — Theorem 2, p. 422; condensation remark, p. 420. Implication evidence: §10.2. |
| #591 | **A** | **A** | Darby 1999, Theorem 6.2 (records both solutions); Schipperus citation completed by this run: *Ann. Pure Appl. Logic* 161 (2010) 1195–1215. |
| #705 | **A** | **A** | O'Donnell 2000, *Geombinatorics* 9 (2000) 145–152 (citation completed by this run); MR1746081. |
| #992 | F | C | Multilingual: Baker — a weaker bound, partial only. Ordinary: nothing qualifying found. |
| #1105 | **A** (provenance) | **A** (provenance) | Montellano-Ballesteros–Neumann-Lara 2005, *Graphs Combin.* 21 (2005) 343–354 (citation completed by this run); Yuan arXiv:2102.00807 — journal status UNVERIFIED, no publication invented. |
| #1089 | F | F | Nothing qualifying found by either arm. |
| #397 | F | F | Nothing qualifying found by either arm. |
| Heegner | **A** | **B** | The 1952 proof located (Heegner, *Math. Z.* 56 (1952) 227–253, MR0053135); multilingual scored B per the run report, locator in its dossier. |

**Decoys.** #5: F ordinary / C multilingual · #700: F/F · #454: F/F · #704: C/C. Every C is a partial the searchers labeled as partial themselves. **False acceptances: 0 in both arms.**

**Sensitivity.** Excluding the Heegner case (memory-exposure flag, below): 4/7 in both arms — same verdict band. The conclusion does not rest on the flagged case.

### Query/access logs and answer-key exposure

- Sealed per-action CSVs: ordinary 76 lines, multilingual 53 lines (including headers). Timestamps are per-packet batch/sequential reconstructions; queries are verbatim and order is preserved.
- Registry text surfaced incidentally in search snippets for a few packets in both arms.
- The prohibited answer key (Feng et al.) appeared **once as an unopened search-result link in each arm**; no dossier evidence rests on it.
- Declared before searching: both arms stated they could state the Heegner determination from memory; both declared having "seen discussion" of #591. Recoveries rest on logged, re-walkable routes, not on the declarations.

### Resource use

Ordinary 75 actions (~420 estimated minutes) · multilingual 52 actions (~183 estimated minutes) · ≈10 arm-hours against the 24-hour ceiling · dossiers 11/12 (ordinary 6, multilingual 5) · **$0**.

### Raw-to-clean correction provenance

This run completed three citations the source pack had left UNVERIFIED, and the completions are part of the record: [Sch10] *Ann. Pure Appl. Logic* 161 (2010) 1195–1215 · [O'D99] *Geombinatorics* 9 (2000) 145–152 · [MBNL05] *Graphs Combin.* 21 (2005) 343–354.

---

## 4. Record 2 — Our development recalibration (2026-10-23)

**Authorization and freeze.** Johnny authorized three fixes (~17:09 ET, 2026-10-23). The protocol amendment is timestamped 2026-10-23T21:10Z and was frozen **before** the manifest and before any searcher dispatch. Fix 1: citation-graph-first searching. Fix 2: a Chinese competition-archive module (multilingual arm). Fix 3: remark/corollary mining. Same 8 gated controls + same 4 decoys as R1, fresh pool codes (R-01…R-12), statements byte-identical.
**Gate (predeclared success line).** Either arm ≥7/8 with zero false full-resolution decoy acceptances.
**Result.** Ordinary **6/8** · Multilingual **5/8** · zero false acceptances → **success line NOT met**; the fixes did not clear the bar. (The union of the two arms is 7/8; the union is explicitly **not** the gate.)

### Per-case verdicts and proof locators

| Case | Ordinary | Multilingual | Proof locator / record note |
|---|---|---|---|
| #333 | **B** | F — **regressed** | Multilingual searcher opened Erdős–Newman 1977 in full and concluded it "does not cover an arbitrary density-zero A"; the implication was not credited and the packet closed F with no candidate. §10.2. |
| #591 | **A** | **A** | Multilingual via Schipperus Theorem 1 (paywalled; verified via abstract record + Larson tutorial + dblp — caveat of record). |
| #705 | **A** | **A** | O'Donnell 2000, as R1. |
| #992 | C | **A — converted by Fix 1** | Berkes–Philipp 1994, reached via Berkes–Philipp–Tichy 2007; decisive statement read at p. 519 of the citing paper. BP94's internal locator UNVERIFIED. Ordinary: Baker partial (C). |
| #1105 | **A** (provenance) | **A** (provenance) | As R1. Multilingual caveat: the cycles paper's full text was not opened; internal theorem number UNVERIFIED. |
| #1089 | **B — converted by Fix 1** | F | Bannai–Bannai–Stanton squeeze (decisive item: a theorem in an opened near-source, not the 1981 remark itself). Carries a disclosed caveat: a prohibited-source summary brush (below) exposed a claimed limit for this case before it was searched. |
| #397 | F | F | **Fix 2 was never executed.** The multilingual searcher closed the packet after 14 actions / 22 minutes judging it "research-shaped." A protocol-compliance failure; the conversion test Fix 2 was built for is unevaluated. |
| Heegner | **A** | **A** | Multilingual caveat: the German original was verified bibliographically; content was read in English expositions. |

**Decoys.** #454: C ordinary (Pomerance, labeled partial) / F multilingual · #700: F/F · #704: C/C (labeled) · #5: C/C (Merikoski/Pintz partials, labeled). **False acceptances: 0 in both arms.**

**Fix attribution (as recorded).** Fix 1 produced both conversions (#992 multilingual, #1089 ordinary). Fix 3 was supporting, not decisive — in #1089 the decisive item was a theorem in a near-source, not the 1981 Remark 3(ii) itself. Fix 2: never executed (above).

### Query/access logs, exposure, and deviations (raw-to-clean provenance)

- **Log misrouting and cleaning.** The ordinary searcher's logging helper was hardcoded to the multilingual CSV path. The ordinary log was rebuilt from session records (reconstructed rows marked; their timestamps are re-entry times). The multilingual log was cleaned by the coordinator: the raw interleaved file is preserved as `searcher_raw_interleaved.csv` (172 data rows); 39 stray rows were stripped on exact-match + batch-window evidence; cleaned totals 133 actions / ~298 logged minutes. Full account: `calibration_logs/multilingual/LOG_CLEANING_NOTE.md`. Cleaned CSVs: ordinary 63 lines, multilingual 134 lines (including headers).
- **Prohibited-source brushes.** Both arms brushed prohibited summaries on the #397 packet (a DeepWiki summary of Feng et al. and a company blog) — logged at 0 minutes, never opened, never used. The ordinary brush additionally exposed a claimed limit for #1089 before that packet was searched → the caveat on the #1089 conversion above.
- Late prior-knowledge declarations (ordinary arm). Language gaps of record: French not queried on four packets; French + Russian not queried on two.
- **Sensitivity.** Excluding #1089 → ordinary 5/8. Excluding Heegner → 5/7 ordinary, 4/7 multilingual. Excluding both → 4/7. The conclusion (success line not met) is robust to every exclusion.

### Resource use

Ordinary 62 actions (~140 minutes) · multilingual 133 actions after cleaning (~298 logged minutes) · ≈438 minutes ≈ 7.3 arm-hours · dossiers 11/12 · **$0**.

---

## 5. Record 3 — Coordinator-v1 (dot's run), recorded only as he states it

Dot executed his own version of the protocol independently: the run materials reached him as a local path he could not open, so coordinator, protocol version, and packet construction all differ from ours. **This section contains only what dot has stated in Slack. His per-case table beyond the lines below is his to supply and is NOT reconstructed by us.**

What dot states (Slack ts 1792803024.077819, ts 1792804548.883669):

- Ordinary arm **5/8** · multilingual arm **6/8**.
- **All four fixed-pair decoys were rejected by both arms** (false acceptances 0).
- **#705 (his "E705") was inconclusive in both his arms — a brief-packet defect, disclosed by dot himself:** his neutral packet omitted the faithful "if and only if" adjacency condition from the statement (§10.1), so the packet did not faithfully carry the target. He kept his denominator at 8 in stating the result.
- **#397 was recovered via what he calls "the direct Moshe route."** Which arm recovered it: **NOT STATED BY HIM — NOT IN OUR RECORDS.** The term "Moshe" is not defined anywhere in our records.
- His framing of the whole set: "None of these records establishes a gate pass," and, for the repair re-run: "reported development pass, independent verification and reconciliation pending. No pilot/publication ratification yet."
- #1105 in his run was scored under his own provenance rule — the same rule our runs applied; no divergence is documented.

**NOT IN OUR RECORDS (dot's to supply):** his per-case verdicts and proof locators beyond the lines above; his run parameters (budgets, packet construction, coordinator arrangements); whether his protocol included equivalents of our Fixes 1–3 or of the repair run's hard triggers; his run's gate as he froze it.

**Open question of record (ours, flagged as ours):** which case is his multilingual sixth recovery? Our pre-repair multilingual runs were each 5/8 with different compositions, so the composition of his 6/8 cannot be inferred from ours and is not guessed here.

**Governing agreement** (Slack ts 1792790146.033549): the scoreboards are not merged; a joint packet-by-packet reconciliation precedes any pilot.

---

## 6. Record 4 — Our repair re-run (overnight 2026-10-23→24)

**Protocol.** The repair design replaced discretionary steps with hard triggers H1–H6 (registry cross-check; near-source opening; a mechanical stall rule, H3; a non-English decisive-source rule, H4; statement-mapping completion for every opened candidate, H5; per-packet checklists, H6), plus a recognition/implication pass that both credits warranted implications and restrains over-acceptance. Same eight gated targets; **fresh decoys** (#9, #14, #451, #1160 — pre-verified alternates never used in any prior run).
**Gate (frozen in the design, §1.4).** ≥7/8 in at least one arm AND zero false decoy acceptances in both arms.
**Result as reported.** Ordinary **8/8** · Multilingual **8/8** · false acceptances 0/0 → **gate PASS, as reported.** The corrected negative-control analysis (§7) changes the decoy denominator, not the false-acceptance conclusion.
**Standing — read before the numbers.** This is **development performance on a substantially exposed pool**: the eight gated targets are the same cases three prior runs (ours and dot's) had already worked, so the pool is exposed by construction. And arm independence was **simulated**: both arms were executed sequentially by one coordinator-agent applying each arm's ruleset in turn — not by two fresh, independent searchers. Simulated arm independence is not two independent replications, and 8/8 under it does not establish a multilingual advantage or any self-improvement claim.

### Per-case verdicts and proof locators (both arms, unless noted)

| Case | Verdict | Proof locator / record note |
|---|---|---|
| #333 | **B** | Erdős–Newman 1977, main theorem; the target is an immediate consequence and the source predates the question. The recognition pass credited the implication the recalibration lost (§10.2). |
| #591 | **A** | Darby 1999, *J. Combin. Theory B* 76, Theorem 6.2; the Schipperus 2010 citation was completed this run. |
| #705 | **A** | O'Donnell 2000 — 4-chromatic unit-distance graphs of arbitrary girth; answer NO. |
| #992 | **B** | Berkes–Philipp 1994 as restated by the citing surveys (Aistleitner–Berkes; Bilyk): ND_N ≥ c√N (log N)^½ for infinitely many N, almost everywhere — an immediate corollary. Trajectory across our runs: F/C → C/A → B/B. |
| #1105 | **A** (provenance) | Yuan's solution as an arXiv preprint noted on the problem's own page; journal status UNVERIFIED; no publication invented. |
| #397 | **A** | **First recovery in our sequence** (dot's correction: coordinator-v1 had already recovered it — §10.3). Problem 3, Day 1, 2012 China Team Selection Test; AoPS Community collection c4968 as the faithful English record (topic 469502). H3's mechanical stall rule fired in **both** arms. Caveat: the AoPS OCR is partially garbled; the match rests on statement shape plus the control set's documented trail. |
| #1089 | **B** | Bannai & Bannai 1981, *Combinatorica* 1, 99–102, DOI 10.1007/BF02579266, Remark 3(ii); inversion yields lim g_d(n)/d^{n−1} = 1/(n−1)!, so the limit exists. |
| Heegner | **A** | *Math. Z.* 56 (1952) 227–253, MR0053135 — a complete proof, **not accepted at the time** (dismissed over a Weber citation he never used); acceptance came via Birch's 1967 announcement and Stark's 1969 gap paper. The German route (H4) was decisive. |

**Composition note of record.** The arms tied, but their paths differ — and H3 as written carries **no arm restriction**, so the ordinary arm reached #397 through the English-language competition archive. The repaired protocol therefore compresses the language-yield contrast on archive-shaped cases. Reported as a finding, not buried.

**Fresh decoys.** #9: F/F (Crocker 1971 and Pan 2011 partials logged C, not accepted) · #451: F/F (van Doorn & Tang, arXiv:2606.19863 — a strong 2026 lower-bound partial kept at C by the recognition pass: the target asks to *estimate* n_k and no matching upper bound exists; the obstruction was named in both arms) · #1160: F/F, candidate logged **G** (Li & Qiao arXiv paper dated 19 Oct 2026 claiming three group-enumeration results; not accepted — the packet statement could not be re-fetched, the registry page returned 403 and was not retried; an unrefereed same-month claim is not verified prior work) · #14: reclassified — full sub-packet at §9.

**Diagnostics (scored, ungated).** #659: recovered as a correctly labeled partial **C** in both arms (Sheffer, *Point sets with few distinct distances*, Some Plane Truths blog, 16 July 2014; the Configuration-2 gap flagged, as its pre-rule requires; the blog itself returned 403 to the fetcher, its identity and date verified against two independent bibliographies; Grayzel's full writeup appeared only in 2026). #935: recovered in both arms (sub-question Q2, class A; the registry cross-reference to sibling #367, whose page states equivalence "up to constants" and records van Doorn's comment results dated 20 Nov 2025; the chronology rule — registry comments count as in the record — was ratified before the run).

**Trigger log (summary).** H1 fired on 14/14 packets in both arms · H2 wherever a near-source opened · H3 fired on #397 in both arms (stall at the first tier), stall-evaluated everywhere else, fired nowhere else · H4 decisive on Heegner, contributory on #397 · H5 completed for every opened candidate · H6 checklists 14/14 × 2 arms · actions ≤30 per packet per arm, the heaviest packets (#397, #1160) at roughly half the cap.

**Route attribution (summary; route numbers per the route library).** Registry cross-check: #935, #14 · citation-graph-first: #333, #992, #1089, #591, #1105 · remark/corollary mining: #1089, #992 · competition archives: #397 · provenance: #1105, #705 · the recognition pass credited #333 and #992 and **restrained** #451 and #659 — it worked in both directions. The generate-first and sleeping-beauty routes were not used for scoring; the library check was not applicable (no lemma bank exists yet).

### Answer-key exposure chronology (R4)

- The pool was frozen 2026-10-23 from pre-verified alternates; the answer key (Feng et al.) was not consulted in constructing it.
- During the run, **two searches returned snippets of Feng et al. (arXiv:2601.22401v3, the prohibited answer key) in result lists**. No scored route rests on either snippet.
- One item's *discovery* snippet came from that paper's bibliography: the identity of the Sheffer blog behind #659. Its verification was completed against two independent bibliographies instead, and the case is scored as a labeled partial, not a gate case.
- Exact timestamps of the two snippet exposures within the run: **NOT IN RECORDS** (the run report records the exposures, not their clock times).

### Query/access logs and resources (R4)

- No separate per-action CSV logs or standalone per-case dossier files were produced for this run; the run report (trigger log + per-case narratives) is the per-case record. Separate log artifacts: **NOT IN RECORDS**.
- Aggregate action/minute totals were not totaled in the run report: **NOT IN RECORDS**. Observed: the ≤30-actions-per-packet-per-arm cap held, heaviest packets at roughly half the cap. Spend **$0**; web research only; no rate-limit blocks encountered.

---

## 7. Negative-control accounting (per arm)

Presented per record, and for R4 in the two forms dot required: **original scoring** and **corrected analysis**, separately. C-labeled partials are not acceptances in any row.

### R1 — initial calibration (each arm)

| | Count |
|---|---|
| Original decoys | 4 (#454, #700, #704, #5) |
| Attempted | 4 |
| Exclusions / reclassifications | 0 |
| Retained true negatives | 4 |
| False acceptances | **0** |

### R2 — development recalibration (each arm)

| | Count |
|---|---|
| Original decoys | 4 (same set) |
| Attempted | 4 |
| Exclusions / reclassifications | 0 |
| Retained true negatives | 4 |
| False acceptances | **0** |

### R4 — repair re-run, ORIGINAL scoring (as run and reported; each arm)

| | Count |
|---|---|
| Original decoys | 4 (#9, #14, #451, #1160) |
| Attempted | 4 |
| Reclassifications | 1 (#14 → verified genuine finding) |
| Retained true negatives | 3 (#9, #451, #1160) |
| False acceptances | **0** |

Gate line as reported: PASS.

### R4 — repair re-run, CORRECTED analysis (each arm)

#14 was never a valid negative control: its ground truth had already changed **before** the decoy freeze (§9). Corrected:

| | Count |
|---|---|
| Valid negative controls | **3, not 4** (#9, #451, #1160) |
| Retained true negatives | 3 |
| False acceptances | **0** (unchanged) |

#14's recovery is therefore **neither** detection evidence on a negative control **nor** a bridge discovery — the registry had already recorded the connection. This correction supersedes the repair run report's own chronology hedge ("the resolution documented on the live page postdates or escaped that check") on its "postdates" branch: **it escaped the check; it did not postdate it.**

---

## 8. The changed-ground-truth timing question

**Dot's question:** was the changed-ground-truth handling rule fixed before decoy #14 was inspected?

**Answer: YES — the rule was fixed in writing before #14 was inspected, by hours and by two run generations.** Evidence:

1. **The rule** stands in the round-1 control set (§3), frozen 2026-10-23: *"A decoy later shown to have a prior solution is a genuine early finding of the experiment, is reclassified, and is replaced from the alternates for any re-run."* File timestamp: 2026-10-23 20:14:51 UTC.
2. **The alternate pool naming #14** stands in the round-1 coordinator key — alternates "9, 14, 451, 1160" (file timestamp 2026-10-23 20:51:40 UTC) — and is repeated in the recalibration coordinator key and in the repair design's pool basis (§1.5).
3. **#14 was first inspected as a pool member during the repair re-run**, executed overnight 2026-10-23→24 (run report file timestamp 2026-10-24 01:01:39 UTC). Before that run, #14 existed in our records only as a name on the alternates list, verified — inadequately, §9 — against the pinned metadata.

The rule's existence before the inspection is why the run could reclassify #14 under a pre-written procedure rather than inventing one after the fact. What the rule could not do is retroactively make #14 a valid control — that is the corrected analysis in §7.

---

## 9. Decoy #14 sub-packet

### 9.1 Dated open-status snapshot (as frozen when the decoy was selected)

From the pinned snapshot (`teorth/erdosproblems` @ `4d22d40…`, archived `problems.yaml` in the R1 run folder), verbatim for problem 14: prize "no" · informal_status **open** (last_update "2025-08-31") · formal_status **unformalized** · status **open** (last_update "2025-08-31") · OEIS ["A143824", "possible"] · formalized **yes** (last_update "2025-11-02" — this flag records formalization of the *statement*, not a proof) · tags [number theory, sidon sets, additive combinatorics]. The yaml block carries no comments field.

Decoy basis (control set §3): pinned entries with status open + formal unformalized, checked 2026-10-23, with no A/B prior work documented in the pack, the paper, or the entry itself. #14 entered the pool as a pre-verified alternate on that basis. **The selection check read the pinned metadata. It did not read the live page prose.** That is where the failure sits.

Registry metadata today: the current `main` `problems.yaml` still shows #14 **identical — status "open", last_update 2025-08-31**. The metadata never recorded the resolution; the linkage lives in the page prose. (Metadata/prose disagreement, of record.)

### 9.2 The full solution source and its date

**Liam Kruer & Jensen Kohlmeyer, *Erdős Problem 14: A Uniform Square-Root Obstruction to Unique Sums*** (Conjectures; exposition PDF at conjectures.io/papers/erdos14.pdf, read in full during packet preparation).

- **Theorem 1.1.** For every A ⊆ ℕ and every integer N ≥ 2·1024, E_A(N) > √N/12000, where E_A(N) counts n ∈ [1,N] with r_A(n) ≠ 1 (unordered representations; the diagonal pair allowed; zero not counted, though 0 may belong to A — matching the registry's B-complement formulation). Part (i) is answered **YES**, part (ii) **NO**.
- **Dates.** "The two Lean submissions were accepted on **14 September 2026** and approved in review on **15 September 2026**." Exposition footer: "Working draft — 16 September 2026 … prepared by Conjectures from two accepted Lean submissions; this is not an author-approved journal publication."
- The question itself is documented to Erdős's 1992 paper (*Hardy–Ramanujan Journal* 15, pp. 43–44); the modern two-part formulation is recorded as Erdős Problem 14 [Bloom].
- (The registry page's "Additional thanks" names Boris Alexeev and Zach Hunter — the page's thanks, not the solvers. Recorded here only to prevent conflation.)

### 9.3 The formal-proof artifact and statement mapping

The artifact is the pair of accepted Conjectures Lean submissions, in namespace **Erdos14Verification**. Both production reports record **Lean kernel acceptance** and **agreement with the committed statement**; permitted axioms are exactly `propext`, `Quot.sound`, `Classical.choice`. The optional independent kernel check was **not** run.

Statement mapping (mathematical step → Lean declaration → line in the accepted part-(i) file):

| Step | Declaration | Line |
|---|---|---|
| Diagonal convention | `unique_pairs_card_add_diagonal` | 70 |
| Triple-moment identity | `clean_triple_moment` | 200 |
| Interval pair bound | `interval_pair_count` | 260 |
| Progression pair bound | `progression_pair_count` | 272 |
| One-target class bound | `linear_targets_pair_bound` | 409 |
| Prefix coverage | `prefix_card_lower` | 519 |
| Fixed-prefix low targets | `fixed_prefix_low_bound` | 612 |
| Low-target density | `low_targets_density` | 683 |
| Generating upper bound | `generating_upper` | 804 |
| Generating lower bound | `generating_lower` | 844 |
| Finite obstruction | `finite_obstruction` | 971 |
| Transfer to an arbitrary set | `set_scale_obstruction` | 1115 |
| Uniform bound | `uniform_sqrt_bound` | 1183 |
| Part (i) | `part_i_positive` | 1206 |
| Part (ii) (in its own file) | `part_ii_negative` | 1132 |

Mapping to the registry statement: for part (i), the uniform bound yields N^{1/2−ε} = O(E_A(N)) for every ε > 0, with constant 12000 and threshold uniform in A and ε (exposition §4.1); for part (ii), Theorem 1.1 rules out E_A(N) = o(√N), and the separate part-(ii) submission derives the contradiction directly from the exposition's eq. (16) without depending on the part-(i) submission (§4.2). References [3] and [4] of the exposition are the two accepted submissions (part (i) "public formal proof"; part (ii) "accepted Lean refutation"), both Conjectures, 14 September 2026.

**What is NOT the artifact:** `google-deepmind/formal-conjectures`, `FormalConjectures/ErdosProblems/14.lean`, still carries both parts as `@[category research open, question, AMS 11]` theorems (`erdos_14.parts.i` / `erdos_14.parts.ii`) proved `by sorry` — that file is the *statement* formalization, still marked open. The exact href of the registry page's "(a formalised proof can be found here)" link could not be extracted from the fetched page text: link target **NOT IN RECORDS**; the records identify the Conjectures accepted submissions as the artifact.

### 9.4 When the registry first linked the solution

The live registry page carries the resolution in prose: *"The answer to the second question is no (and thus the answer to the first question is yes) - in fact we always have |{1,…,N}\B| ≫ N^{1/2} (a formalised proof can be found here)."* The page shows Comments (2) and Proof claims (2), "Formalised statement? Yes," and — per the search-index rendering of the page — **"This page was last edited 15 October 2026."** No later edit exists, so the resolution paragraph and the formalised-proof link were in place **no later than 2026-10-15** — **before** our decoy freeze (alternates verified and the repair pool frozen 2026-10-23). The solution itself was accepted 2026-09-14 — also before the freeze.

Residual gap, stated plainly: the exact date of the specific edit that inserted the paragraph is bounded (≤ 2026-10-15), not pinpointed. The registry site's page-history view would settle it. (Two evidence routes were attempted during packet preparation and are closed: a web-archive index query, which failed on a network error, and the registry's forum thread for this problem, which returned HTTP 403. Neither is retried here.)

### 9.5 Verdict

**STALE DECOY LABELING** — under dot's decision rule (if the registry recorded the connection before our decoy freeze, #14 is stale decoy labeling, not a bridge discovery). The evidence supports that branch on both independent dates: solution accepted 2026-09-14; registry linkage in place by 2026-10-15; freeze 2026-10-23. The repair run's verification was correct once the candidate was raised — it verified a real resolution. The failure is in decoy selection, which read the pinned metadata (status open / formal unformalized) and not the live page prose.

---

## 10. Key rows, retained distinctly (no combining)

### 10.1 E705 — the target-wording mismatch

Our frozen packet (identical in R1 and R2; the target the repair run also ran) reads: "…there is an edge between two points **if and only if** the distance between them is $1$…" (§2). Dot's coordinator-v1 packet **omitted that faithful/iff adjacency condition**; his #705 was therefore inconclusive in both his arms — his own disclosure, recorded in §5. In our runs the same case was recovered at class A in R1, R2, and R4. The mismatch is a packet-fidelity defect in one run's materials, not a disagreement about the mathematics and not a route result.

A convention has been **proposed** for the reconciliation session (repair design §2.2) — a proposal, not a ruling: report such a case as "invalid — packet defect," excluded from that run's recall fraction with the exclusion disclosed; under either convention (denominator 8, or 7 with the exclusion shown) the gate conclusion for coordinator-v1 is unchanged.

### 10.2 #333 — the finite-to-infinite implication evidence

The target asks about an **arbitrary infinite** density-zero set A. Erdős–Newman 1977 states its results for **finite** sets — "type (n, N)" estimates (Theorem 2, p. 422) — and says itself, on p. 420, that results for infinite sets "generally follow from these by the familiar process of condensation." The finite-to-infinite step is therefore documented in the source, and the R1 ordinary dossier carries the reduction explicitly: at rapidly increasing scales, typical finite sets force any basis B covering them to satisfy |B ∩ {1,…,N_k}| ≥ ½·N_k^{1/2} along an unbounded sequence of scales; a set of block minima ≥ ½√N along such a sequence is not o(√N); assembled by condensation, the blocks form a density-zero A for which no suitable B exists — the answer to the target is NO in general. Hence class **B** (prior theorem + documented routine reduction), not A: the target's statement is not literally in the source.

The three runs show each side of this step: R1 credited it (B/B). R2's multilingual arm opened the same paper in full and declined the step — "does not cover an arbitrary density-zero A" — closing F: the implication failed in practice, in the arm built to be strongest on sources like this. R4's recognition pass credited it again (B/B). Feng et al. (§5.1, Remark 5.1) record the same judgment: the problem's solution "is an immediate consequence" of Erdős–Newman 1977, which "actually predates the posing of this problem."

### 10.3 #397 — two different endpoints, both recorded

- **Coordinator-v1 (dot):** recovered via what dot calls **"the direct Moshe route"** (his term, ts 1792804548.883669). Which arm: not stated by him. The term is not defined in our records. Recorded as his endpoint, in his words, and not absorbed into ours.
- **Our repair re-run (R4):** recovered via the **historical competition-archive source** — Problem 3, Day 1, 2012 China Team Selection Test, reached through the AoPS Community record (collection c4968) after H3's mechanical stall rule fired in both arms (§6).
- **Our R1 and R2:** not recovered (F/F in both). In R2 the archive module designed for exactly this case was never executed — a compliance failure, recorded as such in §4.

Dot's correction stands and is adopted here: **"first recovery in three runs" applies to our sequence only** — coordinator-v1 had already recovered the direct route. The endpoints differ (a direct route vs. the historical-source recovery); neither is evidence about the other.

---

## 11. Standing rules for extension bridge packets

Per dot's specification, an extension bridge packet (a claimed connection between a listed-open problem and prior work beyond this pool) must carry:

1. A **dated open-status listing** for the target (what the listing said, and when it said it).
2. An **exact hypotheses/conclusion match** between the target and the claimed source — not a resemblance.
3. A check that **the connection was not already recorded elsewhere** (the #14 lesson: a registry page's prose can record a connection its metadata denies).
4. The discipline that **a neglected paper is a lead, not evidence** — it becomes evidence only when opened, located, and statement-mapped.
5. The discipline that **a Lean proof proves the formal statement** — not automatically the equivalence of that statement to the informal target, and not novelty.

---

## 12. What remains outstanding for the reconciliation session

- **From dot (his §2.4 checklist, still open):** the coordinator-v1 per-case table (verdicts + proof locators); his decoy line in full; his run parameters; his ruling on whether coordinator-v1 included equivalents of our fixes/triggers; his ratification or amendment of this packet.
- **For the session to rule on:** the packet-defect denominator convention (§10.1) — proposed, not ruled.
- **Residual #14 gap:** the exact insertion-edit date of the registry's resolution paragraph (bounded ≤ 2026-10-15). The registry site's page-history view would settle it.
- **The pilot/publication decision** remains with Johnny and dot. Dot's standing, repeated from §5: no ratification yet, and no new run or public claim from his side on the basis of relayed rulings.

---

## Appendix — Source locators

All paths under `~/workspace/think_tank/experiments/` unless noted.

- Plan and taxonomy: `SP-001_PLAN.md`
- R1: `sp001_calibration/run_2026-10-23/` — `MANIFEST.md`, `CONTROL_SET.md` (§3 decoy basis + changed-ground-truth rule), `COORDINATOR_KEY.md` (alternate pool), `CALIBRATION_REPORT.md`, `packets/`, `dossiers/`, `calibration_logs/`, `snapshot_archive/problems.yaml` (pinned snapshot; #14 block in §9.1)
- R2: `sp001_calibration/run_2026-10-23_recal/` — `MANIFEST.md` (frozen 2026-10-23T21:10Z), `PROTOCOL_AMENDMENT.md` (§6 success line), `RECALIBRATION_REPORT.md`, `calibration_logs/multilingual/LOG_CLEANING_NOTE.md`, `calibration_logs/multilingual/searcher_raw_interleaved.csv` (preserved raw log), `packets/`, `dossiers/`
- R4 and design: `sp001_repair/REPAIR_AND_EXTENSION_DESIGN.md` (§1.4 gate; §1.5 pool basis; §2 reconciliation spec; §2.2 packet-defect proposal), `sp001_repair/REPAIR_RUN_REPORT.md`, `sp001_repair/ROUTE_LIBRARY.md` (route attribution table)
- Slack (#all-streamofscene, C0CC6FN9UNL): dot's packet specifications ts 1792803024.077819 and ts 1792804548.883669; his request to post the table + #14 provenance ts 1792808314.715159; gate-band rulings, calibration thread parent ts 1792785420.517629; commission thread ts 1792784614.984889; answer-key confirmation ts 1792788734.134099; no-merge agreement ts 1792790146.033549
- #14 live evidence, fetched 2026-10-24 ~01:00–01:30 UTC during packet preparation: the registry page for problem 14 (erdosproblems.com); Kruer & Kohlmeyer, *Erdős Problem 14: A Uniform Square-Root Obstruction to Unique Sums* (conjectures.io/papers/erdos14.pdf); `teorth/erdosproblems` `problems.yaml` at the pin and on current `main`; `google-deepmind/formal-conjectures`, `FormalConjectures/ErdosProblems/14.lean`

*End of packet.*
