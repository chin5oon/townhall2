"""Interactive Streamlit quiz for Townhall Game — Rounds 4–6."""

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from game_data import GAME_SUBTITLE, GAME_TITLE, INTRODUCTION, QUESTIONS


st.set_page_config(
    page_title="Townhall Game — Rounds 4–6",
    page_icon="🚇",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(180deg, #eff6ff 0, #f8fafc 18rem); }
    .block-container { max-width: 860px; padding-top: 2rem; padding-bottom: 4rem; }
    .hero { padding: 1.5rem 1.6rem; border-radius: 20px; color: white;
            background: linear-gradient(135deg, #1d4ed8, #0f766e); box-shadow: 0 12px 32px #1d4ed825; }
    .hero h1 { margin: 0; font-size: clamp(2rem, 5vw, 3.2rem); line-height: 1.05; }
    .hero p { margin: .55rem 0 0; opacity: .9; font-size: 1.05rem; }
    .question-card { padding: 1.2rem 1.3rem; margin: .8rem 0 1rem; border: 1px solid #dbe5e4;
                     border-radius: 16px; background: #ffffffdd; }
    .eyebrow { color: #1d4ed8; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; font-size: .78rem; }
    .score-note { padding: .8rem 1rem; border-left: 4px solid #f59e0b; border-radius: 8px; background: #fffbeb; }
    [data-testid="stMetric"] { background: white; border: 1px solid #dbe5e4; padding: .75rem; border-radius: 12px; }
    div[data-testid="stRadio"] label { padding: .25rem 0; }
    </style>
    """,
    unsafe_allow_html=True,
)


def score_total(scores):
    return scores["cs"] + scores["pi"] + scores["s"]


def fresh_state():
    for key in [key for key in st.session_state if key.startswith("choice_")]:
        del st.session_state[key]
    st.session_state.question_index = 0
    st.session_state.answers = []
    st.session_state.revealed = False
    st.session_state.started = False


def totals():
    result = {"cs": 0, "pi": 0, "s": 0}
    for answer in st.session_state.answers:
        for key in result:
            result[key] += answer["scores"][key]
    result["total"] = result["cs"] + result["pi"] + result["s"]
    return result


def score_metrics(scores, heading="Choice score"):
    st.caption(heading)
    cols = st.columns(4)
    cols[0].metric("Cost Saving", scores["cs"])
    cols[1].metric("Productivity & Innovation", scores["pi"])
    cols[2].metric("Safety", scores["s"])
    cols[3].metric("Total", score_total(scores))


def sidebar_scoreboard():
    current = totals()
    with st.sidebar:
        st.header("Live score")
        st.metric("Total points", current["total"])
        st.write(f"**Cost Saving:** {current['cs']}")
        st.write(f"**Productivity & Innovation:** {current['pi']}")
        st.write(f"**Safety:** {current['s']}")
        st.divider()
        answered = len(st.session_state.answers)
        st.progress(answered / len(QUESTIONS), text=f"{answered} of {len(QUESTIONS)} decisions confirmed")
        st.caption("Three rounds are included. Round 5 contains two separate decisions.")
        if st.button("Restart game", use_container_width=True):
            fresh_state()
            st.rerun()


if "question_index" not in st.session_state:
    fresh_state()

st.markdown(
    f'<div class="hero"><h1>{GAME_TITLE}</h1><p>{GAME_SUBTITLE}</p></div>',
    unsafe_allow_html=True,
)

sidebar_scoreboard()

if not st.session_state.started:
    st.subheader("Continue the mission")
    st.write(INTRODUCTION)
    st.info(
        "This folder contains Rounds 4–6. Round 5 has two parts, so the app presents four "
        "decision screens in total."
    )
    if st.button("Start Rounds 4–6", type="primary", use_container_width=True):
        st.session_state.started = True
        st.rerun()
    st.stop()

if st.session_state.question_index >= len(QUESTIONS):
    final = totals()
    max_score = sum(max(score_total(option["scores"]) for option in q["options"]) for q in QUESTIONS)
    st.balloons()
    st.header("Rounds 4–6 complete")
    st.write("Your scorecard for these three rounds is ready.")
    score_metrics(final, "Final score")
    st.progress(final["total"] / max_score, text=f"{final['total']} of {max_score} available points")
    if final["total"] == max_score:
        st.success("Outstanding — you selected every recommended option.")
    elif final["total"] >= max_score * 0.6:
        st.success("Good result — review any missed recommendations to strengthen the proposal.")
    else:
        st.warning("There is room to strengthen the proposal. Review the recommendations and try again.")
    with st.expander("Review your decisions", expanded=True):
        for answer in st.session_state.answers:
            icon = "✅" if answer["best"] else "↗️"
            st.markdown(f"{icon} **{answer['round']}:** {answer['label']} — {score_total(answer['scores'])} points")
    if st.button("Play again", type="primary", use_container_width=True):
        fresh_state()
        st.rerun()
    st.stop()

question = QUESTIONS[st.session_state.question_index]
st.progress(
    (st.session_state.question_index + 1) / len(QUESTIONS),
    text=f"Decision {st.session_state.question_index + 1} of {len(QUESTIONS)}",
)
st.markdown(
    f'<div class="question-card"><div class="eyebrow">{question["round"]}</div>'
    f'<h2>{question["title"]}</h2><p>{question["prompt"]}</p></div>',
    unsafe_allow_html=True,
)

labels = [option["label"] for option in question["options"]]
selection = st.radio(
    "Choose one option",
    labels,
    index=None,
    key=f"choice_{question['id']}",
    disabled=st.session_state.revealed,
)

if not st.session_state.revealed:
    if st.button("Confirm choice", type="primary", disabled=selection is None, use_container_width=True):
        selected = next(option for option in question["options"] if option["label"] == selection)
        st.session_state.answers.append({"round": question["round"], **selected})
        st.session_state.revealed = True
        st.rerun()
else:
    selected = st.session_state.answers[-1]
    score_metrics(selected["scores"])
    if selected["best"]:
        st.success("Good job! You chose the recommended option.")
    else:
        st.warning("This is not the recommended option for this scenario.")
    st.write("**Why this choice leads to that outcome**")
    st.write(selected["feedback"])
    if not selected["best"]:
        best = next(option for option in question["options"] if option["best"])
        st.markdown('<div class="score-note"><strong>Best option</strong></div>', unsafe_allow_html=True)
        st.write(f"**{best['label']}**")
        st.write(best["feedback"])
        score_metrics(best["scores"], "Recommended score")
    button_label = "See final score" if st.session_state.question_index == len(QUESTIONS) - 1 else "Next decision"
    if st.button(button_label, type="primary", use_container_width=True):
        st.session_state.question_index += 1
        st.session_state.revealed = False
        st.rerun()
