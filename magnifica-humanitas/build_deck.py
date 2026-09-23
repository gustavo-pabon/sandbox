"""Build the executive deck for the Magnifica Humanitas talk.

Usage:  python3 build_deck.py
Output: magnifica-humanitas-exec-deck.pptx (16:9)
"""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

OUT = Path(__file__).with_name("magnifica-humanitas-exec-deck.pptx")

INK = RGBColor(0x0F, 0x1C, 0x2E)
DEEP = RGBColor(0x17, 0x2C, 0x4A)
SLATE = RGBColor(0x47, 0x54, 0x67)
MUTED = RGBColor(0x8A, 0x94, 0xA6)
LINE = RGBColor(0xD9, 0xDE, 0xE7)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
SOFT = RGBColor(0xF5, 0xF7, 0xFA)
GOLD = RGBColor(0xB0, 0x8D, 0x42)
BLUE = RGBColor(0x2E, 0x5A, 0xAC)
GREEN = RGBColor(0x2E, 0x7D, 0x5B)
RUST = RGBColor(0xB4, 0x45, 0x1F)

FONT = "Segoe UI"
FONT_LIGHT = "Segoe UI Light"
FONT_SEMI = "Segoe UI Semibold"

SW, SH = Inches(13.333), Inches(7.5)
ML, MR = Inches(0.95), Inches(0.95)
CW = SW - ML - MR


def spacing(run, pts):
    """Apply character spacing (premium look for eyebrow text)."""
    run.font._rPr.set("spc", str(int(pts * 100)))


def rect(slide, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(shape, x, y, w, h)
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(0.75)
    s.shadow.inherit = False
    return s


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    return tf


def para(tf, text, size, color, font=FONT, bold=False, italic=False,
         align=PP_ALIGN.LEFT, space_after=0, space_before=0, line=None,
         first=False, spc=None):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_after = Pt(space_after)
    p.space_before = Pt(space_before)
    if line:
        p.line_spacing = line
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.font.name = font
    r.font.bold = bold
    r.font.italic = italic
    if spc:
        spacing(r, spc)
    return p


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def footer(slide, num, label):
    tf = textbox(slide, ML, SH - Inches(0.62), CW, Inches(0.25))
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = label
    r.font.size = Pt(9)
    r.font.color.rgb = MUTED
    r.font.name = FONT
    spacing(r, 0.6)
    tf2 = textbox(slide, SW - MR - Inches(1.0), SH - Inches(0.62), Inches(1.0), Inches(0.25))
    p2 = tf2.paragraphs[0]
    p2.alignment = PP_ALIGN.RIGHT
    r2 = p2.add_run()
    r2.text = str(num)
    r2.font.size = Pt(9)
    r2.font.color.rgb = MUTED
    r2.font.name = FONT_SEMI


def head(slide, num, eyebrow, title, sub=None):
    """Standard light content slide header. Returns y of content start.

    Title and subtitle heights are estimated from text length so dense slides
    never have their content pushed under a wrapped title.
    """
    rect(slide, Emu(0), Emu(0), SW, Inches(0.09), fill=INK)
    rect(slide, Emu(0), Emu(0), Inches(2.6), Inches(0.09), fill=GOLD)

    tf = textbox(slide, ML, Inches(0.62), CW, Inches(0.24))
    para(tf, eyebrow.upper(), 9.5, GOLD, font=FONT_SEMI, first=True, spc=1.6)

    title_lines = max(1, -(-len(title) // 62))
    title_h = Inches(0.47) * title_lines
    tf = textbox(slide, ML, Inches(0.95), CW - Inches(0.3), title_h)
    para(tf, title, 27, INK, font=FONT_LIGHT, first=True, line=0.98)

    y = Inches(0.95) + title_h + Inches(0.28)
    if sub:
        sub_lines = max(1, -(-len(sub) // 112))
        sub_h = Inches(0.29) * sub_lines
        tf = textbox(slide, ML, y, CW - Inches(1.2), sub_h)
        para(tf, sub, 13, SLATE, first=True, line=1.15)
        y = y + sub_h + Inches(0.34)
    footer(slide, num, "Magnifica Humanitas · Responsible AI")
    return y


def quote_block(slide, x, y, w, text, cite, size=15, accent=GOLD, bg=SOFT):
    cpl = max(20, int(w / Inches(1) * 72 / (size * 0.50)))
    lines = max(1, -(-len(text) // cpl))
    h = Inches(0.30) + Inches(size * 1.20 / 72) * lines + Inches(0.48)
    rect(slide, x, y, w, h, fill=bg)
    rect(slide, x, y, Inches(0.045), h, fill=accent)
    tf = textbox(slide, x + Inches(0.42), y + Inches(0.26), w - Inches(0.75), h - Inches(0.4))
    para(tf, f"\u201c{text}\u201d", size, INK, font=FONT_LIGHT, italic=True, first=True, line=1.18)
    para(tf, cite, 10, MUTED, font=FONT_SEMI, space_before=8, spc=0.8)
    return y + h


def card(slide, x, y, w, h, kicker, title, body, accent=BLUE):
    rect(slide, x, y, w, h, fill=WHITE, line=LINE)
    rect(slide, x, y, w, Inches(0.05), fill=accent)
    tf = textbox(slide, x + Inches(0.32), y + Inches(0.34), w - Inches(0.6), h - Inches(0.5))
    para(tf, kicker.upper(), 9, accent, font=FONT_SEMI, first=True, spc=1.2)
    para(tf, title, 14.5, INK, font=FONT_SEMI, space_before=7, line=1.05)
    if body:
        para(tf, body, 11, SLATE, space_before=7, line=1.2)


def divider(slide, num, kicker, title, items):
    rect(slide, Emu(0), Emu(0), SW, SH, fill=INK)
    rect(slide, Emu(0), Emu(0), Inches(2.6), Inches(0.09), fill=GOLD)
    tf = textbox(slide, ML, Inches(2.05), CW, Inches(0.3))
    para(tf, kicker.upper(), 10, GOLD, font=FONT_SEMI, first=True, spc=1.8)
    tf = textbox(slide, ML, Inches(2.45), Inches(6.4), Inches(1.6))
    para(tf, title, 34, WHITE, font=FONT_LIGHT, first=True, line=1.0)

    x = Inches(7.3)
    y = Inches(2.35)
    for i, (t, g) in enumerate(items, 1):
        tf = textbox(slide, x, y, Inches(0.5), Inches(0.4))
        para(tf, f"{i:02d}", 13, GOLD, font=FONT_SEMI, first=True)
        tf = textbox(slide, x + Inches(0.55), y - Inches(0.02), Inches(4.6), Inches(0.5))
        para(tf, t, 13.5, WHITE, font=FONT, first=True, line=1.05)
        para(tf, g, 9.5, MUTED, font=FONT_SEMI, space_before=3, spc=0.8)
        y = y + Inches(0.72)
    footer(slide, num, "")


def table(slide, x, y, widths, headers, rows, row_h=Inches(0.52), head_h=Inches(0.42)):
    total = sum(widths, Emu(0))
    tf = textbox(slide, x, y + Inches(0.08), total, head_h)
    cx = x
    for w, htxt in zip(widths, headers):
        t = textbox(slide, cx, y + Inches(0.06), w - Inches(0.15), Inches(0.3))
        para(t, htxt.upper(), 9, MUTED, font=FONT_SEMI, first=True, spc=1.1)
        cx = cx + w
    rect(slide, x, y + head_h, total, Inches(0.014), fill=INK)

    ry = y + head_h + Inches(0.1)
    for i, row in enumerate(rows):
        if i % 2 == 1:
            rect(slide, x - Inches(0.14), ry, total + Inches(0.28), row_h, fill=SOFT)
        cx = x
        for j, (w, cell) in enumerate(zip(widths, row)):
            txt, color, font, size = cell
            t = textbox(slide, cx, ry + Inches(0.13), w - Inches(0.15), row_h - Inches(0.2))
            para(t, txt, size, color, font=font, first=True, line=1.06)
            cx = cx + w
        ry = ry + row_h
    return ry


def status(kind):
    return {
        "COVERED": (GREEN, "Covered"),
        "PARTIAL": (GOLD, "Partial"),
        "GAP": (RUST, "Gap"),
    }[kind]


NOTES = [
    # 1 title
    "Disclosure up front, once: this is a papal encyclical. It's a religious document, I'm not "
    "presenting it as one, and nothing I say depends on anyone sharing its premises.\n\n"
    "Then move straight on. Naming it defuses it; dancing around it makes it loud.",
    # 2 BLUF
    "BLUF slide. Three reasons it's worth the time: it's specific enough to disagree with; it "
    "addresses developers directly (§111 — every design choice reflects a vision of humanity); "
    "and our Standard is a set of answers while this is a source of questions.\n\n"
    "Land the bottom band: I want a decision on which proposal to pilot.",
    # 3 context
    "Thirty seconds of context. Encyclical = most authoritative teaching document. First one of "
    "this pope, essentially entirely on AI — a statement of priorities.\n\n"
    "The name is the argument: Leo XIII wrote the 1891 text on industrial capitalism. Same move, "
    "new machinery.\n\nLast biblical reference: Babel (centralised plan, concentrated power) vs "
    "rebuilding a city piece by piece (distributed, shared responsibility).",
    # 4 divider
    "Transition slide. Five ideas, each mapped to a goal in our Standard. Don't read the list — "
    "say 'five ideas, roughly two minutes each' and move.",
    # 5 idea 1
    "'Tools aren't neutral' is not new here. The sharper conclusion is: ethical review cannot be a "
    "question about use. Asking 'is this being used well?' is already too late — the system "
    "arrived carrying commitments.\n\n"
    "Our Impact Assessment is organised around intended uses. That's a good structure; I'm not "
    "proposing we drop it. But nothing in it asks what conception of a person is embedded in the "
    "data and the model.",
    # 6 idea 2
    "Four verbs from §105. Walk the table left to right.\n\n"
    "Justify and monitor are institutional — we do them, and we do them well. Challenge and remedy "
    "belong to the person the decision was made about. A5 is oversight by the operator, not "
    "recourse for the subject.\n\n"
    "§103: exclusion cloaked in a veneer of neutrality is very hard to object to. Structural "
    "property, not a bug.",
    # 7 the line
    "Slow down here. Pause after reading the quote.\n\n"
    "This is a technical observation, not a sentimental one. A model trained on someone's history "
    "is a formal commitment to the proposition that they will remain who they were. Credit models, "
    "risk scores, recidivism tools, reputation systems — all encode it.\n\n"
    "We call it predictive validity. We have never had to defend it as a claim about people.",
    # 8 idea 3
    "A direct shot at how our industry talks about safety. Alignment quietly relocates a political "
    "question into an engineering one.\n\n"
    "'Invisible infrastructure' is the phrase to take away — when a value judgment ships inside a "
    "model, it stops looking like a judgment.\n\n"
    "Give ourselves genuine credit: publishing the Standard made our framework criticisable on "
    "purpose. The thinness is that the reasoning behind trade-offs never leaves the building.",
    # 9 idea 4
    "The part I least expected, and the one real hole rather than a weak spot.\n\n"
    "Read the goals: every one is about what the system does downstream. None is about annotators, "
    "moderators, or extraction upstream.\n\n"
    "Pre-empt the objection: yes, these sit under supplier codes and sustainability reporting. "
    "That is the point — they're not in the responsible-AI review, so they're not in the "
    "responsible-AI conversation. I'm not proposing ORA own supplier audits.",
    # 10 idea 5
    "Closest to what we actually ship.\n\n"
    "The claim is falsifiable: productivity gain and agency loss can happen in the same deployment, "
    "and if you only instrument the first you never see the second.\n\n"
    "Ask the room to sit with it: acceptance rate goes up in both worlds. Dependency and delight "
    "produce nearly identical telemetry.\n\n"
    "§156 is the most operationalisable sentence in the document: verifiable measures, not "
    "intentions.",
    # 11 gap matrix
    "The assessment slide. Don't read every row — point at the three GAP rows.\n\n"
    "Headline: one covered, two partial, three genuine gaps — from a framework built with no "
    "visibility into our process. That convergence is itself evidence our Standard is well-founded.",
    # 12 the ask
    "The slide that makes this a working session. All four are additive to artifacts that already "
    "exist — no new process, no new review body.\n\n"
    "Close on the band: if we cannot name the metric in proposal 04, that is itself the finding.",
    # 13 weakness
    "Credibility move — do not cut this. An audience that sees I'm not selling the document will "
    "engage with the substance.\n\n"
    "The honest gap: it calls for slowing down without saying who bears the cost in a competitive "
    "market, and it doesn't engage the game theory. That gap is where ORA actually operates.",
    # 14 close
    "Read the quote slowly, then land the three short lines.\n\n"
    "Our systems are built out of features. Features are functions. The work is keeping a face "
    "behind every function we ship.\n\n"
    "Then hand over: 'I'd rather spend the next fifteen minutes arguing about the four proposals "
    "than answering questions about the document. Where do you think I'm wrong?'",
    # 15 discussion
    "Open with question 1 or 2 — both are concrete and get engineers talking.\n\n"
    "Prepared answers for likely pushback are in speaker-script.md: why a religious document; isn't "
    "this what we already do; the pace argument is unrealistic; supply chain is someone else's "
    "remit; do you agree with it; what about the transhumanism material.",
    # 16 appendix
    "Backup only. Use if someone challenges a quotation or wants the exact reference.",
]


def build():
    prs = Presentation()
    prs.slide_width, prs.slide_height = SW, SH

    # ---------------------------------------------------------------- 1 title
    s = blank(prs)
    rect(s, Emu(0), Emu(0), SW, SH, fill=INK)
    rect(s, Inches(8.55), Inches(0), Inches(4.78), SH, fill=DEEP)
    rect(s, Emu(0), Emu(0), SW, Inches(0.09), fill=GOLD)
    tf = textbox(s, ML, Inches(2.15), Inches(7.1), Inches(0.3))
    para(tf, "RESPONSIBLE AI  ·  EXTERNAL PERSPECTIVES", 10, GOLD, font=FONT_SEMI, first=True, spc=1.8)
    tf = textbox(s, ML, Inches(2.62), Inches(7.2), Inches(2.2))
    para(tf, "What an outside framework\nsees in our AI governance", 36, WHITE, font=FONT_LIGHT, first=True, line=1.02)
    rect(s, ML, Inches(4.42), Inches(1.5), Inches(0.03), fill=GOLD)
    tf = textbox(s, ML, Inches(4.78), Inches(6.6), Inches(1.1))
    para(tf, "Magnifica Humanitas — Leo XIV, 15 May 2026", 14, WHITE, font=FONT_SEMI, first=True)
    para(tf, "Four gaps it exposes in the Microsoft Responsible AI Standard, and four additive fixes.", 12.5, MUTED, space_before=6, line=1.2)
    tf = textbox(s, ML, Inches(6.35), Inches(6.6), Inches(0.6))
    para(tf, "Gustavo Pabón  ·  30 minutes: 15 present, 15 discuss", 11, MUTED, first=True)

    tf = textbox(s, Inches(9.25), Inches(2.62), Inches(3.4), Inches(3.2))
    para(tf, "AT A GLANCE", 9, GOLD, font=FONT_SEMI, first=True, spc=1.6)
    for k, v in [
        ("The source", "First encyclical of Leo XIV.\nEntirely on AI and digital power."),
        ("The posture", "Normative stakeholder input —\nnot doctrine, not endorsement."),
        ("The value", "Our Standard is a set of answers.\nThis is a source of questions."),
    ]:
        para(tf, k, 11.5, WHITE, font=FONT_SEMI, space_before=16)
        para(tf, v, 10.5, MUTED, space_before=3, line=1.2)

    # ------------------------------------------------------------------ 2 BLUF
    s = blank(prs)
    y = head(s, 2, "Executive summary",
             "Broad convergence — and four specific gaps",
             "An external ethics framework, written without access to our process, independently "
             "arrives at most of our principles. Where it diverges is the useful part.")
    cw_, gap = Inches(3.55), Inches(0.28)
    x = ML
    for kicker, title, body, acc in [
        ("Where we align", "Dignity, fairness, transparency, human oversight",
         "The document's judgment criteria map cleanly onto A1–A5, T1–T3 and F1–F3. External convergence is a signal our framework is well-founded.", GREEN),
        ("Where we diverge", "Recourse · Design intent · Trade-offs · Production chain",
         "Four claims land on parts of the lifecycle our goals do not currently reach — most of them upstream of, or downstream from, the system itself.", GOLD),
        ("What I am asking for", "Four additive changes to artifacts we already produce",
         "No new process, no new review body, no new committee. Four prompts and one metric added to templates that already exist.", BLUE),
    ]:
        card(s, x, y, cw_, Inches(2.5), kicker, title, body, acc)
        x = x + cw_ + gap
    band = y + Inches(2.85)
    rect(s, ML, band, CW, Inches(0.72), fill=INK)
    tf = textbox(s, ML + Inches(0.4), band + Inches(0.2), CW - Inches(0.8), Inches(0.4))
    para(tf, "The decision I would like from this room:  which of the four is worth piloting on the next Sensitive Use review?",
         13, WHITE, font=FONT_SEMI, first=True)

    # --------------------------------------------------------------- 3 context
    s = blank(prs)
    y = head(s, 3, "Context",
             "AI is to 2026 what the factory was to 1891",
             "The author took the name Leo after Leo XIII, whose 1891 text on industrial "
             "capitalism founded this tradition. The analogy is the argument.")
    rect(s, ML, y + Inches(0.705), Inches(8.1), Inches(0.02), fill=LINE)
    for i, (dot_x, year, t, b) in enumerate([
        (ML, "1891", "Rerum Novarum · Leo XIII", "The first industrial revolution.\nFactory labour, wages, the right to organise."),
        (ML + Inches(4.3), "2026", "Magnifica Humanitas · Leo XIV", "AI and digital power.\nWork, truth, freedom, concentration of control."),
    ]):
        rect(s, dot_x, y + Inches(0.63), Inches(0.16), Inches(0.16),
             fill=GOLD if i else MUTED, shape=MSO_SHAPE.OVAL)
        tf = textbox(s, dot_x, y, Inches(3.7), Inches(0.6))
        para(tf, year, 22, INK if i else SLATE, font=FONT_LIGHT, first=True)
        tf = textbox(s, dot_x, y + Inches(0.98), Inches(3.8), Inches(1.4))
        para(tf, t, 13, INK, font=FONT_SEMI, first=True)
        para(tf, b, 11, SLATE, space_before=6, line=1.25)

    bx = Inches(9.5)
    rect(s, bx, y - Inches(0.1), Inches(2.9), Inches(3.0), fill=SOFT)
    tf = textbox(s, bx + Inches(0.32), y + Inches(0.2), Inches(2.3), Inches(2.6))
    para(tf, "HOW TO READ IT", 9, GOLD, font=FONT_SEMI, first=True, spc=1.4)
    para(tf, "The same way we read NIST, the EU AI Act, or a civil-society critique:",
         11.5, INK, space_before=10, line=1.25)
    for b in ["A stakeholder position with real reach",
              "Specific enough to disagree with",
              "It names AI developers directly (§111)"]:
        para(tf, "— " + b, 11, SLATE, space_before=9, line=1.2)

    band = y + Inches(3.15)
    rect(s, ML, band, Inches(11.43), Inches(0.9), fill=INK)
    tf = textbox(s, ML + Inches(0.42), band + Inches(0.22), Inches(10.6), Inches(0.6))
    para(tf, "Same move, new machinery.", 13.5, GOLD, font=FONT_SEMI, first=True)
    para(tf, "In both cases the target is concentrated power over work and over what people are able to know.",
         12.5, WHITE, space_before=5)

    # -------------------------------------------------------------- 4 divider
    s = blank(prs)
    divider(s, 4, "The substance", "Five ideas that\ntouch our Standard", [
        ("Design intent, not just intended use", "§104  ·  A1 · A4 · F3"),
        ("Accountability means recourse", "§103, §105  ·  A5 · T1 · RS3"),
        ("Whose values? The limits of alignment", "§107  ·  T2"),
        ("The production chain we never assess", "§101, §173  ·  no owning goal"),
        ("Worker agency as a measured outcome", "§150, §156  ·  RS3"),
    ])

    # ---------------------------------------------------------------- 5 idea 1
    s = blank(prs)
    y = head(s, 5, "Idea 1 · Design intent",
             "Asking only \u201cis it used well?\u201d arrives too late")
    quote_block(s, ML, y, Inches(7.0),
                "We cannot consider AI to be morally neutral… every technical tool embodies choices "
                "and priorities through what it measures, ignores and optimizes.", "§104")
    tf = textbox(s, ML, y + Inches(2.45), Inches(7.0), Inches(2.0))
    para(tf, "The sharper claim", 11, GOLD, font=FONT_SEMI, first=True, spc=1.0)
    para(tf, "A system that excludes people \u201cwithout the possibility of appeal\u201d is not a neutral "
             "tool being misused. It is already defective — the commitment arrived with the design.",
         13, INK, space_before=8, line=1.2)

    bx = Inches(8.55)
    rect(s, bx, y, Inches(3.83), Inches(3.4), fill=WHITE, line=LINE)
    rect(s, bx, y, Inches(3.83), Inches(0.05), fill=RUST)
    tf = textbox(s, bx + Inches(0.35), y + Inches(0.38), Inches(3.15), Inches(2.9))
    para(tf, "WHAT THIS LANDS ON", 9, RUST, font=FONT_SEMI, first=True, spc=1.2)
    para(tf, "Our Impact Assessment is organised around intended uses.",
         13.5, INK, font=FONT_SEMI, space_before=10, line=1.1)
    para(tf, "A4 governs data. F3 governs stereotyping and demeaning outputs. Both detect defects "
             "against a standard.", 11, SLATE, space_before=10, line=1.25)
    para(tf, "Neither asks the prior question: what conception of a person is embedded in this data "
             "and this model — and what did we decide a person is for?",
         11, INK, space_before=10, line=1.25)
    tf = textbox(s, ML, Inches(6.5), Inches(7.0), Inches(0.3))
    para(tf, "TOUCHES   A1 impact assessment   ·   A4 data governance   ·   F3 stereotyping",
         9.5, MUTED, font=FONT_SEMI, first=True, spc=1.0)

    # ---------------------------------------------------------------- 6 idea 2
    s = blank(prs)
    y = head(s, 6, "Idea 2 · Recourse",
             "Our accountability model covers two of the four verbs",
             "§105 defines accountability as the ability to identify who must account for a decision — "
             "and then to justify, monitor, challenge and remedy it.")
    rows = []
    for verb, who, goal, st in [
        ("Justify", "Held by us", "T1 · System intelligibility for decision making", "COVERED"),
        ("Monitor", "Held by us", "RS3 · Ongoing monitoring, feedback, evaluation", "COVERED"),
        ("Challenge", "Held by the affected person", "No goal in the Standard carries this", "GAP"),
        ("Remedy", "Held by the affected person", "No goal in the Standard carries this", "GAP"),
    ]:
        c, lbl = status(st)
        rows.append([
            (verb, INK, FONT_SEMI, 14),
            (who, SLATE, FONT, 11.5),
            (goal, SLATE, FONT, 11.5),
            (lbl.upper(), c, FONT_SEMI, 10.5),
        ])
    end = table(s, ML, y, [Inches(1.7), Inches(2.6), Inches(5.3), Inches(1.2)],
                ["Verb", "Who holds it", "Where it lives today", "Status"], rows)
    rect(s, ML, end + Inches(0.32), Inches(11.43), Inches(1.15), fill=SOFT)
    rect(s, ML, end + Inches(0.32), Inches(0.045), Inches(1.15), fill=GOLD)
    tf = textbox(s, ML + Inches(0.42), end + Inches(0.52), Inches(10.6), Inches(0.8))
    para(tf, "A5 gives us human oversight and control — but that is oversight by the operator, not recourse for the subject.",
         13, INK, font=FONT_SEMI, first=True)
    para(tf, "§103: once exclusion is \u201ccloaked in a veneer of neutrality and objectivity,\u201d it becomes very hard to object to. That is a structural property, not a bug.",
         11, SLATE, space_before=7, line=1.2)

    # -------------------------------------------------- 7 idea 2b — the line
    s = blank(prs)
    rect(s, Emu(0), Emu(0), SW, SH, fill=INK)
    rect(s, Emu(0), Emu(0), Inches(2.6), Inches(0.09), fill=GOLD)
    tf = textbox(s, ML, Inches(1.5), Inches(11.4), Inches(0.3))
    para(tf, "IDEA 2 · THE LINE WORTH SITTING WITH", 9.5, GOLD, font=FONT_SEMI, first=True, spc=1.6)
    tf = textbox(s, ML, Inches(2.05), Inches(11.4), Inches(1.6))
    para(tf, "Automated decision systems do not know \u201ccompassion, mercy, forgiveness, "
             "and above all, the hope that people are able to change.\u201d",
         24, WHITE, font=FONT_LIGHT, italic=True, first=True, line=1.15)
    tf = textbox(s, ML, Inches(3.22), Inches(3.0), Inches(0.3))
    para(tf, "§102", 10, MUTED, font=FONT_SEMI, first=True, spc=1.0)
    rect(s, ML, Inches(3.95), Inches(1.5), Inches(0.03), fill=GOLD)
    tf = textbox(s, ML, Inches(4.4), Inches(10.6), Inches(1.6))
    para(tf, "This is a technical observation, not a sentimental one.", 15, GOLD, font=FONT_SEMI, first=True)
    para(tf, "A model trained on a person's history is a formal commitment to the proposition that they will remain who they were. "
             "Every credit model, risk score, recidivism tool and trust-and-safety reputation system encodes that claim.",
         14, WHITE, font=FONT_LIGHT, space_before=12, line=1.25)
    para(tf, "We call it predictive validity. We have never had to defend it as a claim about people.",
         13, MUTED, space_before=12, line=1.2)
    footer(s, 7, "")

    # ---------------------------------------------------------------- 8 idea 3
    s = blank(prs)
    y = head(s, 8, "Idea 3 · Trade-off transparency",
             "We publish conclusions, not trade-offs")
    quote_block(s, ML, y, Inches(7.0),
                "A more moral AI is not enough if that morality is determined by a few.", "§107")
    tf = textbox(s, ML, y + Inches(1.85), Inches(7.0), Inches(2.4))
    para(tf, "The argument", 11, GOLD, font=FONT_SEMI, first=True, spc=1.0)
    para(tf, "Alignment is necessary but insufficient on its own, because it quietly relocates a political "
             "question into an engineering one. The requirement is not \u201chave better values\u201d — it is that "
             "the ethical frameworks themselves stay openly discussable, outside the firms that set them.",
         12.5, INK, space_before=8, line=1.25)
    para(tf, "\u201cInvisible infrastructure\u201d is the phrase to take away: when a value judgment ships inside a "
             "model, it stops looking like a judgment and becomes the way the thing works.",
         11.5, SLATE, space_before=10, line=1.25)

    bx = Inches(8.55)
    card(s, bx, y, Inches(3.83), Inches(1.75), "Where we are ahead",
         "We published the Standard",
         "We made our own framework criticisable, on purpose. Transparency Notes do the same at system level.", GREEN)
    card(s, bx, y + Inches(1.95), Inches(3.83), Inches(2.25), "Where we are thin",
         "The reasoning never leaves the building",
         "When safety is traded against utility, or one group's quality of service against another's, we publish the resolution — never the alternatives we rejected or the values we ranked.", GOLD)
    tf = textbox(s, ML, Inches(6.5), Inches(11.4), Inches(0.3))
    para(tf, "§106 adds the institutional half: abstract ethics is not enough — it requires \u201crobust legal frameworks, independent oversight, informed users.\u201d Note \u201cindependent.\u201d",
         10.5, MUTED, first=True)

    # ---------------------------------------------------------------- 9 idea 4
    s = blank(prs)
    y = head(s, 9, "Idea 4 · The production chain",
             "Our goals describe the system, never how it was made")
    half = Inches(5.55)
    rect(s, ML, y, half, Inches(2.95), fill=WHITE, line=LINE)
    rect(s, ML, y, half, Inches(0.05), fill=GREEN)
    tf = textbox(s, ML + Inches(0.35), y + Inches(0.36), half - Inches(0.7), Inches(2.4))
    para(tf, "DOWNSTREAM — FULLY GOVERNED", 9, GREEN, font=FONT_SEMI, first=True, spc=1.2)
    para(tf, "What the system does to users and stakeholders", 14, INK, font=FONT_SEMI, space_before=9)
    para(tf, "A1–A5   accountability\nT1–T3   transparency\nF1–F3   fairness\nRS1–RS3   reliability & safety\nPS1–PS2 · I1   privacy, security, accessibility",
         11.5, SLATE, space_before=12, line=1.45)

    rect(s, ML + half + Inches(0.33), y, half, Inches(2.95), fill=WHITE, line=LINE)
    rect(s, ML + half + Inches(0.33), y, half, Inches(0.05), fill=RUST)
    tf = textbox(s, ML + half + Inches(0.68), y + Inches(0.36), half - Inches(0.7), Inches(2.4))
    para(tf, "UPSTREAM — ABSENT FROM RAI REVIEW", 9, RUST, font=FONT_SEMI, first=True, spc=1.2)
    para(tf, "The conditions under which it was produced", 14, INK, font=FONT_SEMI, space_before=9)
    para(tf, "Data labeling and model training\nContent moderation of disturbing material\nMineral and rare-earth extraction\nEnergy, water and carbon at model scale",
         11.5, SLATE, space_before=12, line=1.45)

    ny = y + Inches(3.25)
    rect(s, ML, ny, Inches(11.43), Inches(1.5), fill=SOFT)
    rect(s, ML, ny, Inches(0.045), Inches(1.5), fill=GOLD)
    tf = textbox(s, ML + Inches(0.42), ny + Inches(0.26), Inches(10.6), Inches(1.1))
    para(tf, "\u201cNothing in the world of AI is immaterial or magical.\u201d  §173",
         14, INK, font=FONT_LIGHT, italic=True, first=True)
    para(tf, "These issues do sit under other governance — supplier codes, sustainability reporting. That is exactly the point: "
             "they are not in the responsible-AI review, so they are not in the responsible-AI conversation. No single artifact "
             "tells the full human-impact story of a system.",
         11.5, SLATE, space_before=9, line=1.25)

    # --------------------------------------------------------------- 10 idea 5
    s = blank(prs)
    y = head(s, 10, "Idea 5 · Worker agency",
             "Dependency and delight produce identical telemetry")
    quote_block(s, ML, y, Inches(11.43),
                "AI frequently forces workers to adapt to the speed and demands of machines, rather than "
                "machines being designed to support those who work.", "§150 — named effects: de-skilling · automated surveillance · eroded agency")
    ny = y + Inches(1.65)
    cw2 = Inches(3.55)
    card(s, ML, ny, cw2, Inches(2.2), "What we measure",
         "Acceptance · completion · time saved · retention · CSAT",
         "Every one of these rises in a world where the tool makes people more capable.", MUTED)
    card(s, ML + cw2 + Inches(0.28), ny, cw2, Inches(2.2), "The blind spot",
         "They also rise where it makes people dependent",
         "A product can make users measurably more productive and measurably less capable. Our instrumentation cannot tell the two apart.", RUST)
    card(s, ML + 2 * (cw2 + Inches(0.28)), ny, cw2, Inches(2.2), "The standard offered",
         "\u201cVerifiable measures\u201d — §156",
         "Every introduction of automation should carry checkable measures for employment, retraining and participation. Intentions do not count.", BLUE)

    # ------------------------------------------------------------ 11 gap matrix
    s = blank(prs)
    y = head(s, 11, "Assessment",
             "Convergence is broad; the gaps are narrow and specific")
    rows = []
    for claim, ref, goal, st in [
        ("Human control of consequential decisions", "§200", "A5 · human oversight and control", "COVERED"),
        ("Design intent — the vision of the person in data and model", "§104", "A1 · A4 · F3", "PARTIAL"),
        ("Values contestable from outside the firm", "§107", "Published Standard · T2", "PARTIAL"),
        ("Contest and remedy by the affected person", "§103 · §105", "A5 covers the operator only", "GAP"),
        ("Labour and environmental conditions of production", "§101 · §173", "No owning goal", "GAP"),
        ("Worker agency as a measured outcome", "§150 · §156", "RS3 measures performance only", "GAP"),
    ]:
        c, lbl = status(st)
        rows.append([
            (claim, INK, FONT, 12),
            (ref, MUTED, FONT_SEMI, 10.5),
            (goal, SLATE, FONT, 11),
            (lbl.upper(), c, FONT_SEMI, 10.5),
        ])
    end = table(s, ML, y, [Inches(4.9), Inches(1.25), Inches(4.1), Inches(1.1)],
                ["Claim in the document", "Ref", "Coverage in the RAI Standard", "Status"],
                rows, row_h=Inches(0.55))
    tf = textbox(s, ML, end + Inches(0.3), Inches(11.4), Inches(0.4))
    para(tf, "One covered, two partial, three genuine gaps — from a framework built with no visibility into our process.",
         12.5, INK, font=FONT_SEMI, first=True)

    # --------------------------------------------------------------- 12 the ask
    s = blank(prs)
    y = head(s, 12, "The ask",
             "Four additive changes to artifacts we already produce",
             "No new process. No new review body. Four prompts and one metric, added to templates that exist today.")
    cw3 = Inches(2.72)
    gap3 = Inches(0.235)
    x = ML
    for n, (title, body, artifact, effort, acc) in enumerate([
        ("Add a design-intent prompt",
         "\u201cWhat does this system treat a person as, and what does it optimise them toward?\u201d Asked once, at the top.",
         "Impact Assessment template", "Low effort", BLUE),
        ("Make recourse first-class",
         "For any consequential decision: who can contest it, through what path, in what time, with what remedy.",
         "Goal A5 · Impact Assessment", "Medium effort", BLUE),
        ("Publish trade-offs, not just outcomes",
         "A short \u201cdecisions and trade-offs\u201d section: what we gave up, what we rejected, how we ranked the values.",
         "Transparency Note", "Low effort", BLUE),
        ("One agency metric per assistive deployment",
         "A single metric that would fall if the tool were making people dependent rather than capable.",
         "RS3 monitoring plan", "Medium effort", BLUE),
    ], 1):
        rect(s, x, y, cw3, Inches(3.15), fill=WHITE, line=LINE)
        rect(s, x, y, cw3, Inches(0.05), fill=acc)
        tf = textbox(s, x + Inches(0.3), y + Inches(0.34), cw3 - Inches(0.6), Inches(2.6))
        para(tf, f"{n:02d}", 19, acc, font=FONT_LIGHT, first=True)
        para(tf, title, 13.5, INK, font=FONT_SEMI, space_before=6, line=1.08)
        para(tf, body, 10.5, SLATE, space_before=8, line=1.25)
        tf2 = textbox(s, x + Inches(0.3), y + Inches(2.5), cw3 - Inches(0.6), Inches(0.6))
        para(tf2, artifact.upper(), 8.5, MUTED, font=FONT_SEMI, first=True, spc=1.0)
        para(tf2, effort.upper(), 8.5, acc, font=FONT_SEMI, space_before=4, spc=1.0)
        x = x + cw3 + gap3
    band = y + Inches(3.45)
    rect(s, ML, band, Inches(11.43), Inches(0.72), fill=INK)
    tf = textbox(s, ML + Inches(0.4), band + Inches(0.2), Inches(10.6), Inches(0.4))
    para(tf, "If we cannot name the metric in proposal 04, that is itself the finding.", 13, WHITE, font=FONT_SEMI, first=True)

    # ------------------------------------------------------------ 13 the weakness
    s = blank(prs)
    y = head(s, 13, "Intellectual honesty",
             "Where the document is weak — and where that leaves us")
    for i, (t, b) in enumerate([
        ("It calls for slowing down without pricing it",
         "§106 argues that prudence and \u201cat times, a slower pace\u201d is not opposition to progress. It never says who bears the cost of slowing in a competitive market."),
        ("It gestures at international frameworks",
         "It does not engage the game theory of what happens when the actors who ignore the advice simply win."),
        ("It is a risk document written in a moment of real benefit",
         "The upside of these systems is acknowledged thinly. A balanced reading has to supply that side itself."),
    ]):
        yy = y + Inches(i * 1.05)
        rect(s, ML, yy + Inches(0.14), Inches(0.045), Inches(0.62), fill=GOLD)
        tf = textbox(s, ML + Inches(0.4), yy + Inches(0.1), Inches(10.6), Inches(0.9))
        para(tf, t, 14.5, INK, font=FONT_SEMI, first=True)
        para(tf, b, 11.5, SLATE, space_before=6, line=1.2)
    band = y + Inches(3.45)
    rect(s, ML, band, Inches(11.43), Inches(0.95), fill=SOFT)
    tf = textbox(s, ML + Inches(0.42), band + Inches(0.26), Inches(10.6), Inches(0.6))
    para(tf, "The gap between a normative document and a working governance regime is precisely where ORA operates.",
         14, INK, font=FONT_SEMI, first=True)
    para(tf, "That gap is not a reason to dismiss the argument. It is the reason the argument needs us.", 11.5, SLATE, space_before=6)

    # ---------------------------------------------------------------- 14 close
    s = blank(prs)
    rect(s, Emu(0), Emu(0), SW, SH, fill=INK)
    rect(s, Emu(0), Emu(0), Inches(2.6), Inches(0.09), fill=GOLD)
    tf = textbox(s, ML, Inches(1.85), Inches(11.0), Inches(2.4))
    para(tf, "\u201cThe quality of a civilization is measured not by the power of its means, "
             "but by the care it is able to offer, by its ability to recognize the other "
             "as a face not merely as a function.\u201d",
         26, WHITE, font=FONT_LIGHT, italic=True, first=True, line=1.2)
    tf = textbox(s, ML, Inches(4.25), Inches(3.0), Inches(0.3))
    para(tf, "§114", 10, MUTED, font=FONT_SEMI, first=True, spc=1.0)
    rect(s, ML, Inches(4.85), Inches(1.5), Inches(0.03), fill=GOLD)
    tf = textbox(s, ML, Inches(5.25), Inches(10.6), Inches(1.2))
    para(tf, "Our systems are built out of features. Features are functions.", 15, GOLD, font=FONT_SEMI, first=True)
    para(tf, "The work is keeping a face behind every function we ship.", 15, WHITE, space_before=8)
    footer(s, 14, "")

    # ------------------------------------------------------------ 15 discussion
    s = blank(prs)
    y = head(s, 15, "Discussion",
             "Fifteen minutes — I would rather argue about the proposals than the document")
    qs = [
        "Which of the four proposals is implementable in our current process, and which is a fantasy?",
        "Can anyone name a metric we track today that would catch a product making users more productive and less capable?",
        "Our Impact Assessments are use-centric. Is there anywhere we ask the design-intent question — or am I looking in the wrong place?",
        "Do we have a recourse story for any consequential automated decision we ship? Any one?",
        "Is there a class of system where \u201ca model of your past is a bet you won't change\u201d should be disqualifying, not a known limitation?",
        "Is there an argument here that is simply wrong, and that we should say so about rather than absorb politely?",
    ]
    for i, q in enumerate(qs):
        col = i // 3
        row = i % 3
        x = ML + col * Inches(5.85)
        yy = y + Inches(row * 1.15)
        tf = textbox(s, x, yy, Inches(0.5), Inches(0.4))
        para(tf, f"{i + 1:02d}", 13, GOLD, font=FONT_SEMI, first=True)
        tf = textbox(s, x + Inches(0.5), yy - Inches(0.02), Inches(4.95), Inches(1.0))
        para(tf, q, 12.5, INK, first=True, line=1.22)

    # ------------------------------------------------------------- 16 appendix
    s = blank(prs)
    y = head(s, 16, "Appendix", "Source citations")
    rows = []
    for ref, txt in [
        ("§100", "Ease of answers \u201ccan encourage excessive reliance… and weaken personal creativity and judgment.\u201d"),
        ("§102", "Automated systems do not know \u201ccompassion, mercy, forgiveness, and above all, the hope that people are able to change.\u201d"),
        ("§103", "Exclusion \u201ccloaked in a veneer of neutrality and objectivity, against which it becomes difficult to raise objections.\u201d"),
        ("§104", "\u201cWe cannot consider AI to be morally neutral… every technical tool embodies choices and priorities.\u201d"),
        ("§105", "Accountability: identify who must account, \u201cjustify them, monitor them, and, when necessary, challenge them and remedy any harm caused.\u201d"),
        ("§106", "Prudence and \u201cat times, a slower pace\u201d is not opposition to progress; requires \u201crobust legal frameworks, independent oversight.\u201d"),
        ("§107", "\u201cA more moral AI is not enough if that morality is determined by a few.\u201d"),
        ("§111", "\u201cEvery design choice reflects a vision of humanity\u201d — direct appeal to developers."),
        ("§150", "AI \u201cfrequently forces workers to adapt to the speed and demands of machines.\u201d"),
        ("§156", "Every introduction of automation needs \u201cverifiable measures\u201d for employment, retraining, participation."),
        ("§173", "\u201cNothing in the world of AI is immaterial or magical\u201d — invisible labour and extraction."),
        ("§200", "Lethal force \u201ccannot be delegated to opaque or automated processes\u201d — effective human control."),
    ]:
        rows.append([(ref, GOLD, FONT_SEMI, 10.5), (txt, SLATE, FONT, 10.5)])
    end = table(s, ML, y, [Inches(1.1), Inches(10.3)],
                ["Ref", "Quotation"], rows, row_h=Inches(0.35))
    tf = textbox(s, ML, end + Inches(0.18), Inches(11.4), Inches(0.3))
    para(tf, "Leo XIV, Magnifica Humanitas, 15 May 2026 · vatican.va   |   Microsoft Responsible AI Standard v2, June 2022",
         9.5, MUTED, first=True)

    for slide, note in zip(prs.slides, NOTES):
        slide.notes_slide.notes_text_frame.text = note

    prs.save(OUT)
    print(f"wrote {OUT}  ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")


if __name__ == "__main__":
    build()
