"""Streamlit interface for the reserved-book probability tutor."""

import streamlit as st

from tutor import A_BOOKS, A_RATE, B_BOOKS, B_RATE, FEEDBACK, SCOPES, assess


st.set_page_config(
    page_title="Reserved Book Probability Tutor",
    layout="centered",
)

INPUT_KEYS = ("a_count", "b_count", "scope", "probability")


def clear_feedback():
    """Clear the result attached to the previous attempt."""
    st.session_state.pop("result", None)
    st.session_state.pop("expanded", None)


def reset():
    st.session_state["a_count"] = ""
    st.session_state["b_count"] = ""
    st.session_state["scope"] = None
    st.session_state["probability"] = ""
    clear_feedback()


def check_attempt():
    """Check the visible attempt and begin at the first feedback level."""
    values = [st.session_state[key] for key in INPUT_KEYS]
    st.session_state.result = assess(*values)
    st.session_state.expanded = False


def expand_hint():
    """Reveal the detailed hint for the current result."""
    st.session_state.expanded = True


st.title("Reserved Book Probability Tutor")
st.caption(
    "One practice question. Enter counts as whole numbers and probability "
    "as a fraction. You can check an incomplete attempt."
)

with st.container(border=True):
    st.subheader("The library")
    st.write(
        f"The library has {A_BOOKS + B_BOOKS} books. Zone A has {A_BOOKS} books "
        f"and Zone B has {B_BOOKS}. The reserved share is {A_RATE} in Zone A "
        f"and {B_RATE} in Zone B."
    )
    st.write(
        "One book is drawn at random from all the reserved books. "
        "What is the probability that it comes from Zone A?"
    )

st.subheader("1. Count reserved books")
a_column, b_column = st.columns(2)
a_column.text_input(
    "Reserved books in Zone A", key="a_count", max_chars=8,
    on_change=clear_feedback,
)
b_column.text_input(
    "Reserved books in Zone B", key="b_count", max_chars=8,
    on_change=clear_feedback,
)

st.subheader("2. Identify the sampling group")
st.selectbox(
    "Which group did you use as your denominator?",
    SCOPES,
    index=None,
    key="scope",
    placeholder="Choose a group",
    on_change=clear_feedback,
)

st.subheader("3. Enter the probability")
st.text_input(
    "Your probability as a fraction",
    placeholder="For example, 1/3",
    key="probability",
    max_chars=30,
    on_change=clear_feedback,
)

check_column, reset_column = st.columns(2)
check_column.button(
    "Check my attempt", key="check", type="primary", on_click=check_attempt,
)
reset_column.button("Start over", key="reset", on_click=reset)

code = st.session_state.get("result")
if code == "correct":
    st.success(FEEDBACK[code].message)
elif code:
    feedback = FEEDBACK[code]
    with st.container(border=True):
        st.subheader("Feedback")
        st.info(feedback.message)

        if feedback.detail and not st.session_state.expanded:
            st.button(
                "More specific hint", key="more", on_click=expand_hint,
            )

        if feedback.detail and st.session_state.expanded:
            st.markdown("**More specific hint**")
            st.write(feedback.detail)
            if code == "whole_library":
                st.markdown(
                    "| Zone | Reserved | Unreserved |\n"
                    "|---|---|---|\n"
                    "| A | **Include this group** | Outside the draw |\n"
                    "| B | **Include this group** | Outside the draw |"
                )