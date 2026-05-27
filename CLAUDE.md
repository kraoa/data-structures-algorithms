# Problem Generation Guidelines

This repo is a collection of coding problems. Each problem gives the solver a
pre-built environment to interact with and asks them to implement one class or
function. Problems should be LeetCode medium-to-hard difficulty, written in
Python.

---

## Directory layout

```
problem-N/
  .cpad              # CoderPad run targets (see format below)
  README.md          # problem statement (boilerplate intro + problem description)
  requirements.txt   # always: black and ipdb
  src/
    <driver>.py      # pre-built environment — READ THIS FIRST
    solver.py        # stub — the thing to implement
    main.py          # shows how the solver is called; run this to see output
    test_<topic>.py  # tests for the driver (must pass out of the box)
    test_<solver>.py # tests for the solver (assertions commented out)
  data/              # optional: word lists, puzzle configs, etc.
```

`.cpad` defines the CoderPad run targets. Include one entry per test file. The
key pattern is `test_<filename>_py` and `dbg_test_<filename>_py`. Always
include `run_main_py`, `format`, and `dbg_run_main_py`. Example:

```json
{
    "targets": {
        "run_main_py":            {"label": "Main (main.py)",          "command": "python src/main.py"},
        "test_test_board_py":     {"label": "Test (test_board.py)",    "command": "python src/test_board.py"},
        "test_test_solver_py":    {"label": "Test (test_solver.py)",   "command": "python src/test_solver.py"},
        "format":                 {"label": "Format",                  "command": "/home/coderpad/.local/bin/black src/"},
        "dbg_run_main_py":        {"label": "ipdb Main (main.py)",     "command": "/home/coderpad/.local/bin/ipdb3 src/main.py"},
        "dbg_test_test_board_py": {"label": "ipdb Test (test_board.py)","command": "/home/coderpad/.local/bin/ipdb3 src/test_board.py"},
        "dbg_test_test_solver_py":{"label": "ipdb Test (test_solver.py)","command": "/home/coderpad/.local/bin/ipdb3 src/test_solver.py"}
    }
}
```

`README.md` always starts with the CoderPad boilerplate paragraph, followed by
a `# <Problem Title>` section that describes the problem in plain English
(inputs, outputs, rules), and ends with the standard six-step task list.

Number problems sequentially (`problem-1`, `problem-2`, …).

After creating a new problem, append a row to `PROBLEMS.md` in the root of the
repo using this format:

```
| N | [problem-N](problem-N/src/solver.py) | One-sentence description of what the solver implements. |
```

The description should match the summary style used in existing rows: start
with a verb ("Find", "Implement", "Count", …) and mention the key algorithm or
data structure.

---

## The driver module

Name it after the domain, not generically. Examples:
- `puzzle.py` for game-style problems
- `board.py` for grid/board or N-Queens problems
- `graph.py` for graph/scheduling problems
- `tree.py` for binary-tree problems
- `sequences.py` for array/sequence DP problems
- `histogram.py`, `elevation.py`, `window.py`, etc. — match the problem's subject
- `coins.py`, `strings.py`, `patterns.py`, `stream.py`, `decodings.py`, `segmentation.py`, `lists.py`, `operations.py` — all valid when they fit
- `grid.py` for 2D grid problems (islands, BFS-on-grid)

Avoid the name `problem.py`; it is a generic fallback and there is almost always a more specific name.

### Required conventions

**Opening docstring:**
```python
"""Read this first."""
```

**Always provide `get_test_cases()`** as a `@staticmethod` that returns a list
of test inputs. Test cases should cover the LeetCode examples, edge cases
(empty input, single element, impossible cases), and at least one commented-out
placeholder for the user to add their own.

**Always provide `run(solver)`** that calls the solver for each test case and
returns `(test_case, actual, passed)` tuples. This is how `main.py` drives the
solver without knowing its internals.

**Protect mutable inputs.** Pass copies to the solver so stored test cases are
never modified:
```python
solver.my_method(list(tc.nums))          # list copy
solver.my_method(copy.deepcopy(tc.grid)) # deep copy for nested structures
```

### Two problem shapes

**Input → output** (most problems): use a `@dataclass` `TestCase` with input
fields and an `expected` field.

```python
@dataclass
class TestCase:
    nums: List[int]
    expected: int
```

**Operation sequence** (OO-design problems like LRU Cache, Median Finder): use
an `Op` dataclass and make each `Problem` instance a sequence of ops. Return a
list of `Problem` instances from `get_test_cases()`.

```python
@dataclass
class Op:
    kind: str            # e.g. "get" or "put"
    key: int
    value: Optional[int]
    expected: Optional[int]
```

---

## solver.py

**Opening docstring:**
```python
"""You'll implement this."""
```

The class is named after what it does, not always `Solver`:
- `Solver` for most problems
- `LRUCache`, `MedianFinder`, `Serializer` for OO-design problems

Stub methods return trivially wrong values (`0`, `False`, `[]`, `None`, `""`).

Do **not** add a docstring to stub methods. The method name and signature are
the only hint the solver gets.

---

## main.py

**Opening docstring:**
```python
"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""
```

Always wrap output in the banner:
```python
def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)

# called as:
banner("BEGIN CODE OUTPUT")
# ... solver output ...
banner("END CODE OUTPUT")
```

---

## Test files

### Naming

Name test files after what they test, not generically:

| Tests | Good name | Avoid |
|-------|-----------|-------|
| Graph helpers + cycle detection | `test_graph.py` | `test_problem.py` |
| LRU operation replay logic | `test_operations.py` | `test_problem.py` |
| N-Queens board validator | `test_board.py` | `test_problem.py` |
| The Solver / LRUCache / etc. | `test_scheduler.py`, `test_lru_cache.py` | `test_solver.py` |

Two test files per problem is the norm. More is fine when the driver has
clearly separable concerns (e.g. `test_tree.py` + `test_serializer.py`).

### test_\<topic\>.py — driver tests

- All tests must pass against the pre-built driver code.
- Do not test the solver stub here.
- **Preferred pattern:** include a simple brute-force or reference
  implementation and assert that every stored `expected` value agrees with it.
  This proves the test cases are correct and documents the problem's ground
  truth in one shot.

```python
@staticmethod
def _brute_force(nums: list) -> int:
    """O(n²) DP reference."""
    ...

def test_expected_values_match_brute_force(self) -> None:
    for tc in Problem.get_test_cases():
        self.assertEqual(tc.expected, self._brute_force(tc.nums))
```

Good reference implementations by category:

| Problem type | Reference to use |
|--------------|-----------------|
| Numerical DP (LIS, edit distance, coin change, decode ways) | Simpler DP variant |
| Grid BFS (islands, rotting oranges) | BFS flood-fill |
| Histogram, rain water | O(n²) two-loop brute force |
| Streaming / OO design (median finder, LRU) | Sort-based or naive implementation |
| Regex / pattern matching | Python `re.fullmatch` |
| Validation (N-Queens, topological order) | Test the validator method directly |

### test_\<solver\>.py — solver stub tests

- One test that runs the solver without asserting anything (just proves no
  crash on a stub).
- Subsequent tests have their assertions **commented out**. Uncomment them as
  the solver is built.
- Commented tests should cover: a basic case, an edge case, and (where
  applicable) a constraint the naive approach gets wrong.

```python
def test_basic(self) -> None:
    solver = Solver()
    solver.solve(...)
    # Uncomment once Solver is implemented:
    # self.assertEqual(solver.get_result(), expected)

# def test_edge_case(self) -> None:
#     solver = Solver()
#     self.assertEqual(solver.solve([]), 0)

# def test_greedy_counterexample(self) -> None:
#     # Greedy fails here; the correct approach is DP.
#     solver = Solver()
#     self.assertEqual(solver.coin_change([1, 5, 11], 15), 3)
```

---

## Style rules

- **Python only.** Use standard library; no third-party dependencies.
- **Type hints everywhere** in driver and solver files.
- **No comments explaining what code does** — only comments that explain *why*
  (a non-obvious invariant, a subtle edge case in the spec).
- Commented-out test cases in `get_test_cases()` use the format:
  ```python
  # TestCase("???", "??", "??"),  # add your own
  ```
- Method hints in solver stubs describe the *approach*, not just the signature.
- The `run()` method is the only place the driver and solver touch each other;
  `main.py` only calls `run()`.
