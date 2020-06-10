"""Solution to 8.14 Boolean Evaluation.

Given a boolean expression consisting of the symbols `0` (false), `1`
(true), `&` (AND), `|` (OR), and `^` (XOR), and a desired boolean result
value `result`, implement a function to count the number of ways of
parenthesizing the expression such that it evaluates to `result`. The
expression should be fully parenthesized (e.g., `(0)^(1)`) but not
extraneously (e.g., `(((0))^(1))`).

EXAMPLE
countEval("1^0|0|1", false) -> 2
countEval("0&0&0&1^1|0", true) -> 10
"""

import dataclasses
from typing import List


@dataclasses.dataclass
class _Counts:
    false: int
    true: int


def count_eval(expression: str, result: bool) -> int:
    """Counts ways of parenthesizing a boolean expression.

    Args:
        expression: A non-empty boolean expression consisting of the
            symbols `0` (false), `1` (true), `&` (AND), `|` (OR), and
            `^` (XOR).
        result: Desired boolean result of evaluating expression.

    Returns:
        Number of ways of parenthesizing the expression such that it
        evaluates to desired result.
    """
    num_constants = (len(expression) + 1) // 2
    zeros = _Counts(true=0, false=0)
    # dp[i][j] -> expression[j:i+1]
    dp: List[List[_Counts]] = [[zeros] * (i + 1) for i in range(num_constants)]
    for i in range(num_constants):
        if expression[2 * i] == '0':
            dp[i][i] = _Counts(false=1, true=0)
        else:
            dp[i][i] = _Counts(false=0, true=1)
    for span in range(1, num_constants):
        for hi in range(span, num_constants):
            lo, false, true = hi - span, 0, 0
            for mid in range(lo, hi):
                counts = _permute(dp[mid][lo], dp[hi][mid + 1],
                                  operator=expression[2 * mid + 1])
                false, true = false + counts.false, true + counts.true
            dp[hi][lo] = _Counts(false=false, true=true)
    return dp[-1][0].true if result else dp[-1][0].false


def _permute(counts1: _Counts, counts2: _Counts, operator: str) -> _Counts:
    total = (sum(dataclasses.astuple(counts1)) *
             sum(dataclasses.astuple(counts2)))
    if operator == '&':
        true = counts1.true * counts2.true
        false = total - true
    elif operator == '|':
        false = counts1.false * counts2.false
        true = total - false
    elif operator == '^':
        true = counts1.true * counts2.false + counts1.false * counts2.true
        false = counts1.true * counts2.true + counts1.false * counts2.false
    return _Counts(false=false, true=true)
