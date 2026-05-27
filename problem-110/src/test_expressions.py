"""Tests for the Expressions driver (must pass out of the box)."""

import itertools
import unittest
from typing import List
from expressions import Expressions


def _brute_add_operators(num: str, target: int) -> List[str]:
    """eval-based: try all operator placements using itertools.product."""
    n = len(num)
    results = []
    ops = ['+', '-', '*', '']

    def _valid_expr(num_str: str, op_seq) -> bool:
        """Build expression string; reject leading-zero multi-digit numbers."""
        expr = num_str[0]
        digits = [num_str[0]]
        for i, op in enumerate(op_seq):
            if op == '':
                digits.append(num_str[i + 1])
            else:
                segment = ''.join(digits)
                if len(segment) > 1 and segment[0] == '0':
                    return False
                digits = [num_str[i + 1]]
            expr += op + num_str[i + 1]
        segment = ''.join(digits)
        if len(segment) > 1 and segment[0] == '0':
            return False
        return True

    for op_combo in itertools.product(ops, repeat=n - 1):
        if not _valid_expr(num, op_combo):
            continue
        parts = [num[0]]
        for i, op in enumerate(op_combo):
            parts.append(op)
            parts.append(num[i + 1])
        expr = ''.join(parts)
        try:
            if eval(expr) == target:  # noqa: S307
                results.append(expr)
        except Exception:
            pass
    return sorted(results)


class TestExpressions(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Expressions.get_test_cases():
            if len(tc.num) > 8:
                continue  # skip long strings; brute force is too slow
            brute = _brute_add_operators(tc.num, tc.target)
            self.assertEqual(sorted(tc.expected), brute,
                             f"num={tc.num!r} target={tc.target}")

    def test_expected_is_sorted(self) -> None:
        for tc in Expressions.get_test_cases():
            self.assertEqual(tc.expected, sorted(tc.expected),
                             f"num={tc.num!r}")


if __name__ == "__main__":
    unittest.main()
