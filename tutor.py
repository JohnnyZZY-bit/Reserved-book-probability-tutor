"""Assessment rules and authored hints for the reserved-book exercise."""

import re
from dataclasses import dataclass
from fractions import Fraction


A_BOOKS = 30
B_BOOKS = 70
A_RATE = Fraction(2, 5)
B_RATE = Fraction(1, 5)
A_RESERVED = int(A_BOOKS * A_RATE)
B_RESERVED = int(B_BOOKS * B_RATE)
ANSWER = Fraction(A_RESERVED, A_RESERVED + B_RESERVED)

ALL_BOOKS = "All 100 books"
ZONE_A = "All books in Zone A"
ZONE_B = "All books in Zone B"
RESERVED = "Reserved books from both zones"
SCOPES = (ALL_BOOKS, ZONE_A, ZONE_B, RESERVED)


@dataclass(frozen=True)
class Feedback:
    message: str
    detail: str = ""


FEEDBACK = {
    "need_scope": Feedback(
        "Which group of books did you use as the denominator? "
        "Choose your sampling group and check again."
    ),
    "need_a": Feedback("Enter the number of reserved books in Zone A."),
    "need_b": Feedback("Enter the number of reserved books in Zone B."),
    "format_a": Feedback("Enter a whole number from 0 to 30 for Zone A."),
    "format_b": Feedback("Enter a whole number from 0 to 70 for Zone B."),
    "check_a": Feedback(
        "Which group of books does the rate 2/5 describe?",
        "Zone A has 30 books. Work out 30 × 2/5 to find its reserved count.",
    ),
    "check_b": Feedback(
        "Which group of books does the rate 1/5 describe?",
        "Zone B has 70 books. Work out 70 × 1/5 to find its reserved count.",
    ),
    "whole_library": Feedback(
        "Could an unreserved book be drawn in this question?",
        "Find the reserved column. Add the reserved counts from both zones.",
    ),
    "reverse_condition": Feedback(
        "Using all Zone A books as the denominator answers a question about "
        "the reservation rate in Zone A. Which books are eligible for this draw?",
        "In the question, find the group named after 'from'. "
        "Use that whole group for the denominator.",
    ),
    "zone_b_only": Feedback(
        "Does the question restrict the draw to Zone B?",
        "The draw includes reserved books in both zones. "
        "Use both reserved counts to build the denominator.",
    ),
    "need_probability": Feedback("Enter your probability as a fraction."),
    "format_probability": Feedback(
        "Use a fraction with whole numbers, a nonzero denominator "
        "and a value from 0 to 1, for example 1/3."
    ),
    "check_probability": Feedback(
        "Check how the group you selected is represented in your fraction.",
        "Put the Zone A reserved count over the sum of the reserved counts "
        "from Zones A and B.",
    ),
    "correct": Feedback(
        "Your counts, sampling group and fraction agree. "
        "The probability is the share of reserved books that come from Zone A."
    ),
}


def check_count(raw, zone, expected, maximum):
    """Return a feedback code for a missing, invalid or incorrect count."""
    value = raw.strip()
    if not value:
        return f"need_{zone}"
    if not re.fullmatch(r"[0-9]{1,2}", value) or int(value) > maximum:
        return f"format_{zone}"
    if int(value) != expected:
        return f"check_{zone}"
    return None


def read_probability(raw):
    """Read a bounded fraction with optional spaces around the slash."""
    match = re.fullmatch(r"\s*([0-9]{1,6})\s*/\s*([0-9]{1,6})\s*", raw)
    if not match:
        return None

    numerator, denominator = map(int, match.groups())
    if denominator == 0 or numerator > denominator:
        return None
    return Fraction(numerator, denominator)


def assess(a_count, b_count, scope, probability):
    """Select one response using the evidence in this attempt."""
    if probability.strip() and scope not in SCOPES:
        return "need_scope"

    scope_error = {
        ALL_BOOKS: "whole_library",
        ZONE_A: "reverse_condition",
        ZONE_B: "zone_b_only",
    }.get(scope)
    if scope_error:
        return scope_error

    a_issue = check_count(a_count, "a", A_RESERVED, A_BOOKS)
    if a_issue:
        return a_issue

    b_issue = check_count(b_count, "b", B_RESERVED, B_BOOKS)
    if b_issue:
        return b_issue

    if scope != RESERVED:
        return "need_scope"
    if not probability.strip():
        return "need_probability"

    value = read_probability(probability)
    if value is None:
        return "format_probability"
    if value != ANSWER:
        return "check_probability"
    return "correct"