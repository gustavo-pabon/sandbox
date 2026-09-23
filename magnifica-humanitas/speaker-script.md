# Magnifica Humanitas → Microsoft RAI Standard & ORA practice
**Format:** 15 min talk + 15 min discussion
**Deck:** [magnifica-humanitas-exec-deck.pptx](./magnifica-humanitas-exec-deck.pptx) (rebuild with `python3 build_deck.py`)
**Source:** Leo XIV, *Magnifica Humanitas*, 15 May 2026 — [vatican.va](https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html). Paragraph numbers (§) cited below are the encyclical's own numbering.

---

## Timing map

| # | Segment | Slides | Time | Cumulative |
|---|---------|--------|------|------------|
| 0 | Framing: why this document, in this room | 1–2 | 1:30 | 1:30 |
| 1 | What it is, in 90 seconds | 3 | 1:30 | 3:00 |
| 2 | Idea 1 — "AI is not morally neutral" | 4–5 | 2:00 | 5:00 |
| 3 | Idea 2 — Accountability means recourse | 6–7 | 2:00 | 7:00 |
| 4 | Idea 3 — Whose values? The critique of "alignment" | 8 | 2:00 | 9:00 |
| 5 | Idea 4 — The supply chain nobody assesses | 9 | 2:00 | 11:00 |
| 6 | Idea 5 — Work, agency, de-skilling | 10 | 2:00 | 13:00 |
| 7 | Four concrete proposals + close | 11–14 | 2:00 | 15:00 |
| — | Discussion | 15 (16 = appendix) | 15:00 | 30:00 |

**If you're running long, cut Idea 4 (supply chain) to 45 seconds** — it's the most self-contained. Never cut segment 7; the proposals are what make this a working session instead of a book report.

**Note on slide 2 (executive summary):** it is the BLUF slide and carries the ask. If the room is senior and short on patience, present slide 2 first and treat slides 5–10 as evidence you can skip through on demand.

---

## Tone guidance (read once, then forget)

- Say the religious framing out loud **once**, at the start, and then drop it. Naming it defuses it; dancing around it makes it loud.
- Treat the text the way you'd treat a well-argued NGO or standards-body submission: **normative stakeholder input from a constituency of ~1.4 billion people**, which happens to name AI developers directly (§111). That's the posture. Not "the Pope says," but "here is an argument; is it right?"
- No scripture, no theology, no "we should." The Babel / Nehemiah imagery is worth **one sentence** as a structural metaphor and nothing more.
- Your credibility move: **criticize the document at least once.** Suggested line in segment 7. An audience that sees you're not selling it will engage with the substance.
- If someone challenges the premise ("why are we discussing a religious document?"), the answer is in the prepared Q&A below. Answer it in 20 seconds and move on.

---

## THE SCRIPT

### 0 — Framing (1:30)

> Quick disclosure before I start: what I'm presenting is a papal encyclical. It's a religious document, I'm not going to present it as one, and nothing I say today depends on anyone in this room sharing its premises.
>
> Here's why I think it's worth fifteen minutes anyway.
>
> It's an unusually specific piece of writing. It is not "AI should serve humanity" — it makes claims about impact assessment, about accountability, about the labor supply chain, that are concrete enough to disagree with. That's rare in this genre. It also addresses us directly: §111 is an explicit appeal to the people who build these systems, arguing that every design choice encodes a view of the human person, and that this creates a professional obligation, not just a personal one.
>
> And the practical reason: our Standard is a set of answers. Documents like this are a source of *questions* — and questions from outside our own frame are the ones most likely to find what our process is structurally blind to. I found four. That's what I want to walk through.

*(Beat. Move on quickly — don't oversell the framing.)*

---

### 1 — What it is, in 90 seconds (1:30)

> Thirty seconds of context so the references make sense.
>
> An encyclical is the most authoritative teaching document the Catholic Church produces. This one came out in May, it's the current pope's first, and it's essentially entirely about AI and digital power — which is a statement of priorities by itself.
>
> The name matters too. He chose "Leo" after Leo XIII, who wrote the 1891 document on industrial capitalism — factory labor, wages, unions — the founding text of this whole tradition. So the framing is deliberate: **AI is to us what the factory was to 1891.** A transformation in what work is, who holds power, and what happens to the people on the wrong end of it.
>
> The document is built around two images: building the Tower of Babel, versus rebuilding a ruined city piece by piece. One is a centralized plan executed by concentrated power; the other is slow, distributed, shared responsibility. That's the argument in one metaphor, and that's the last biblical reference I'll make.
>
> Chapter three is AI and technological power. Chapter four is truth, work, and freedom. Everything I'm about to cover lives there.

---

### 2 — Idea 1: "AI is not morally neutral" (2:00)

> First idea. §104, and I'll read the line:
>
> > "we cannot consider AI to be morally neutral… every technical tool embodies choices and priorities through what it measures, ignores and optimizes, and how it classifies people and situations."
>
> Now, "tools aren't neutral" is not new to anyone here. But the conclusion he draws from it is sharper than the usual version. The claim is that ethical review **cannot be a question about use**. Asking "is this system being used well?" is already too late, because the system arrived carrying commitments — in what it measures, in what it declines to measure, in how it sorts people. And §104 says explicitly: a system that excludes people "without the possibility of appeal" isn't a neutral tool being misused. It's already defective.
>
> Here's why I think that lands on us specifically. Our Impact Assessment is organized around **intended uses**. Stakeholders, harms, benefits, per intended use. That's a good structure and I'm not proposing we abandon it. But it's a use-centric frame, and §104 is asking a design-centric question that our template doesn't currently ask anywhere: *what conception of a person is embedded in this data and this model?*
>
> Goal A4 covers data governance. Goal F3 covers stereotyping and demeaning outputs. But both are about detecting defects against a standard. Neither one asks the prior question — what is this system's implicit theory of what a person is, and what did we decide, by choosing these labels and these metrics, that a person is *for*?
>
> That's a question you can actually put in a template. I'll come back to it.

---

### 3 — Idea 2: Accountability means recourse (2:00)

> Second idea, and for me this is the most useful thing in the document.
>
> §105 defines accountability as the ability to identify who must account for a decision, "justify them, monitor them, and, when necessary, challenge them and remedy any harm caused."
>
> Four verbs. **Justify, monitor, challenge, remedy.** Look at where our Standard is strong and where it isn't.
>
> Justify — Goal T1, system intelligibility for decision-making. Strong. Monitor — RS3, ongoing monitoring and feedback. Strong. Those first two are institutional: *we* justify, *we* monitor.
>
> Challenge and remedy are different. Those are held by the person the decision was made *about*. And they are, at best, thin in our framework. A5 gives us human oversight and control — but that's oversight by the operator, not recourse for the subject. There is no goal in the Standard that says: a person affected by a consequential automated decision must have a path to contest it and obtain a remedy.
>
> §103 sharpens this. It says the real danger is an algorithm deciding "who is worthy or not, without anyone bearing responsibility for that judgment" — and then the exclusion gets "cloaked in a veneer of neutrality," which makes it very hard to object to. Not a bug. A structural property of how these deployments feel from the outside.
>
> And there's one line in §102 I keep coming back to. It says automated decision systems don't know "compassion, mercy, forgiveness, and above all, the hope that people are able to change."
>
> Sit with that last one for a second, because it's a technical observation, not a sentimental one. **A model trained on someone's history is a formal commitment to the proposition that they will remain who they were.** Every credit model, every risk score, every recidivism tool, every trust-and-safety reputation system encodes that. We call it predictive validity. He's pointing out that it's also a claim about human beings, and that we've never had to defend it.

---

### 4 — Idea 3: Whose values? (2:00)

> Third idea, and this one is a direct shot at how our industry talks about safety. §107:
>
> > "A more moral AI is not enough if that morality is determined by a few."
>
> The argument: the alignment project — encoding human values into systems — is necessary but radically insufficient on its own, because it quietly relocates a political question into an engineering one. If the values get set inside a handful of firms, then "those who control AI will impose their own moral vision, which will become the invisible infrastructure of these systems."
>
> *Invisible infrastructure* is the phrase I'd take away. When a value judgment ships inside a model, it stops looking like a judgment. It becomes the way the thing works.
>
> His requirement is not "have better values." It's that **the ethical frameworks themselves have to be openly discussable and subject to shared standards** — outside the firms that set them.
>
> Where we're genuinely good here: we published the Standard. That's not nothing — we made our framework criticizable, on purpose. Transparency Notes do the same at the system level.
>
> Where I think we're weak: **we publish our conclusions, not our trade-offs.** When a deployment decision involves a real conflict — safety against utility, one group's quality of service against another's, a disclosure that would also help an adversary — we resolve it internally and publish the resolution. The reasoning, the alternatives we rejected, and the values we ranked don't leave the building.
>
> §106 adds the institutional version of the same point: ethics talk in the abstract isn't enough, you need "robust legal frameworks, independent oversight, informed users." Note "independent." We can't be the only ones grading this.

---

### 5 — Idea 4: The supply chain nobody assesses (2:00)

> Fourth. This is the part I least expected, and where I think we have an actual hole rather than a weak spot.
>
> §173 opens: "Nothing in the world of AI is immaterial or magical." Then it inventories what's behind a model response — data labeling, model training, content moderation "often involving disturbing material," done largely by young workers, "predominantly women, working under demanding conditions for minimal wages." Then mineral extraction, including children working in dangerous conditions on rare earths. §101 adds energy, water, and carbon, all scaling with model size.
>
> Then the challenge to us: it is not enough to celebrate the benefits of innovation "if they are built on a chain of exploitation that remains deliberately hidden."
>
> Here's the structural observation. **Our RAI Standard is almost entirely about the behavior of the system. It is almost silent about the conditions of its production.** Read the goals: A1 through A5, T1 through T3, F1 through F3, RS1 through RS3, PS, I1. Every one is about what the system does to users and stakeholders downstream. None is about annotators, moderators, or extraction upstream.
>
> That's not an oversight by any individual — those things live in supplier codes of conduct and sustainability reporting, in other orgs, under other governance. But that's exactly the point: **they're not in the responsible-AI review, so they're not in the responsible-AI conversation.** If a reviewer asked about annotator working conditions today, there's no goal to hang it on.
>
> I don't think ORA can or should absorb supplier standards. But an Impact Assessment that never once looks upstream is telling a partial story about a system's human impact.

---

### 6 — Idea 5: Work, agency, de-skilling (2:00)

> Last idea, and it's the one closest to what we actually ship.
>
> §150, quoting an earlier Vatican document on AI:
>
> > AI "frequently forces workers to adapt to the speed and demands of machines, rather than machines being designed to support those who work."
>
> The three named consequences: **de-skilling, automated surveillance, and relegation to rigid and repetitive tasks.** And then a fourth that I find the most interesting — keeping pace with the technology can "erode workers' sense of agency and stifle the innovative abilities they are expected to bring to their work."
>
> That's a specific, falsifiable, measurable claim. It says the productivity gain and the agency loss can occur *simultaneously*, in the same deployment, and that if you only instrument for the first you will never see the second.
>
> Ask yourself what we measure for our own assistive products. Acceptance rate. Task completion. Time saved. Retention. Satisfaction.
>
> Now ask which of those would move if a tool made people measurably more productive and measurably less capable. **Acceptance rate goes up in both worlds.** Dependency and delight produce nearly identical telemetry. §100 makes the same point about individual use — that the ease of getting an answer "can also encourage excessive reliance and the search for ready-made answers, and weaken personal creativity and judgment."
>
> §156 offers a concrete standard, and this is the most operationalizable sentence in the whole document: every introduction of automation should come with **verifiable measures** for the employment, retraining, and participation of the affected workers. Verifiable. Not intentions — measures you can check.

---

### 7 — Four proposals, and the close (2:00)

> So — four things I'd actually put on the table. All of them are additive to what we already do.
>
> **One. Add a design-intent question to the Impact Assessment.** One prompt, at the top: *what does this system treat a person as, and what does it optimize them toward?* Adjacent to A1 and A4. It's the §104 question, and the reason to ask it explicitly is that it's the kind of thing every reviewer assumes someone else already asked.
>
> **Two. Make recourse a first-class requirement, not a byproduct of oversight.** For any consequential decision: who can contest it, through what path, in what time, with what remedy. That's the *challenge and remedy* half of §105, and A5 currently doesn't carry it.
>
> **Three. Publish trade-offs, not just outcomes.** Transparency Notes say what a system does and doesn't do well. They rarely say what we gave up and why. Even a short "decisions and trade-offs" section would make our value choices criticizable from outside — which is the §107 test.
>
> **Four. One agency metric per assistive deployment.** Not a program. One metric that would go *down* if the tool were making people dependent rather than capable. If we can't name one, that's the finding.
>
> And let me say where I think the document is weak, because I don't want to hand you a sales pitch. It calls for slowing down — §106 says prudence and "at times, a slower pace" is not opposition to progress — but it says almost nothing about who bears the cost of slowing down in a competitive market, or what happens when the actors who ignore the advice simply win. It gestures at international frameworks. It doesn't engage the game theory. That's the gap between a document like this and a working governance regime, and it's the gap *we* live in.
>
> I'll close with the line I found hardest to shake, §114:
>
> > "The quality of a civilization is measured not by the power of its means, but by the care it is able to offer, by its ability to recognize the other as a face not merely as a function."
>
> That is the entire argument for why responsible AI is a discipline and not a compliance exercise. Our systems are built out of features. Features are functions. The job — the actual job — is keeping a face behind every function we ship.
>
> That's fifteen minutes. I'd rather spend the next fifteen arguing about the four proposals than answering questions about the document, so: where do you think I'm wrong?

---

## Prepared Q&A

**"Why are we discussing a religious document at Microsoft?"**
> Because it's a stakeholder position with real reach and it makes specific, checkable claims about our work. We read EU regulatory text, NIST frameworks, and civil-society critiques without endorsing their worldviews. Same posture here. If the arguments are bad, they're bad on the merits — and none of the four proposals I made require agreeing with anything religious.

**"Isn't this just restating what our Standard already says?"**
> On fairness, transparency, and oversight — largely yes, and that's worth noting as external convergence. The three places it doesn't overlap are recourse for affected people, upstream labor and environmental conditions, and worker agency as a measured outcome. Those are the three I'd focus on.

**"The pace argument is unrealistic — we can't unilaterally slow down."**
> Agreed, and I said so. But the useful version isn't "go slower." It's that our gates should be capability-based rather than calendar-based, and that ORA needs standing institutional authority to hold a gate without that being an escalation event. That's compatible with shipping fast.

**"Aren't the supply chain issues someone else's remit?"**
> Operationally, yes. But the effect of that split is that no single artifact describes the full human cost of a system. I'm not proposing ORA own supplier audits — I'm proposing the Impact Assessment cite them, so reviewers see one picture instead of two halves.

**"Do you agree with the document?"**
> With about three quarters of it. The claims about accountability, invisible labor, and worker agency I think are straightforwardly correct and underweighted in our practice. The pace and governance sections are where it substitutes an appeal for a mechanism. And it's notably light on the upside — it's a document about risk written at a moment when the benefits are also real.

**"What about the transhumanism material?"**
> It's chapter three's second half, and I deliberately skipped it. It's the most philosophically loaded part and the least connected to anything we'd change on Monday. Happy to go there in discussion if people want.

---

## Discussion starters (in descending order of usefulness)

1. Which of the four proposals is actually implementable in our current process, and which is a fantasy?
2. Can anyone name a metric we currently track that would catch a product making users more productive and less capable?
3. Our Impact Assessments are use-centric. Is there anywhere in our process that asks the design-intent question — and if not, is that a real gap or am I looking in the wrong place?
4. Do we have a recourse story for any consequential automated decision we ship? Any one?
5. §102's point — that a model trained on your past is a bet that you won't change. Is there a category of system where we should treat that as disqualifying rather than as a known limitation?
6. "A more moral AI is not enough if that morality is determined by a few." What would it look like for us to make a value trade-off contestable from outside the company, concretely?
7. Is there any argument in the document that's simply wrong, that we should say so about rather than absorb politely?

---

## Quote sheet (exact, with citations)

| § | Quote | Use |
|---|-------|-----|
| 100 | ease of answers "can also encourage excessive reliance and the search for ready-made answers, and weaken personal creativity and judgment" | de-skilling |
| 102 | automated systems do not know "compassion, mercy, forgiveness, and above all, the hope that people are able to change" | the strongest line in the talk |
| 103 | exclusion "cloaked in a veneer of neutrality and objectivity, against which it becomes difficult to raise objections" | contestability |
| 104 | "we cannot consider AI to be morally neutral… every technical tool embodies choices and priorities through what it measures, ignores and optimizes" | design vs. use |
| 105 | accountability = identify who must account, "justify them, monitor them, and, when necessary, challenge them and remedy any harm caused" | the four verbs |
| 106 | prudence and "at times, a slower pace" is not opposition to progress; needs "robust legal frameworks, independent oversight, informed users" | pace + institutions |
| 107 | "A more moral AI is not enough if that morality is determined by a few." | alignment critique |
| 110 | to "disarm" AI: free it from monopolistic control, make it "human-friendly" | optional close |
| 111 | "every design choice reflects a vision of humanity" — direct appeal to developers | opening hook |
| 114 | "The quality of a civilization is measured not by the power of its means, but by the care it is able to offer, by its ability to recognize the other as a face not merely as a function." | close |
| 150 | AI "frequently forces workers to adapt to the speed and demands of machines" → de-skilling, surveillance, eroded agency | work |
| 156 | every introduction of automation needs "verifiable measures" for employment, retraining, participation | most operational line |
| 173 | "Nothing in the world of AI is immaterial or magical" + invisible labor, extraction | supply chain |
| 200 | lethal force "cannot be delegated to opaque or automated processes" — must stay under "effective, self-aware and responsible human control" | hold in reserve |

**RAI Standard v2 goals referenced:** A1 impact assessment · A2 oversight of significant adverse impacts · A3 fit for purpose · A4 data governance and management · A5 human oversight and control · T1 system intelligibility for decision making · T2 communication to stakeholders · T3 disclosure of AI interaction · F1 quality of service · F2 allocation of resources and opportunities · F3 minimization of stereotyping, demeaning, and erasing outputs · RS1 reliability and safety guidance · RS2 failures and remediations · RS3 ongoing monitoring, feedback, and evaluation · PS1/PS2 privacy and security · I1 accessibility.
