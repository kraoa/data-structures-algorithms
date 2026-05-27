"""
Runs your BloomFilter. It's useful to see how BloomFilter is called.
You may want to change how BloomFilter is constructed.
"""

from bloom_filter import Problem
from solver import BloomFilter


def banner(legend: str) -> None:
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    banner("BEGIN CODE OUTPUT")
    for i, problem in enumerate(Problem.get_test_cases()):
        print(f"\nProblem {i + 1}: size={problem.size}, num_hashes={problem.num_hashes}")
        results = problem.run(BloomFilter)
        for op, actual, passed in results:
            if op.kind == "add":
                print(f"  add({op.item!r})")
            else:
                status = "PASS" if passed else "FAIL"
                exp_str = str(op.expected) if op.expected is not None else "(false positive ok)"
                print(
                    f"  might_contain({op.item!r}) => {actual} "
                    f"(expected {exp_str}) [{status}]"
                )
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()
