"""Tests for the stations driver. Must pass out of the box."""

import unittest
from stations import Problem, TestCase


def _brute_force(stations: list, vehicles: list) -> list:
    """O(nq) linear scan — for each vehicle find the station with minimum squared distance."""
    result = []
    for vx, vy in vehicles:
        best_dist, best_idx = float("inf"), 0
        for i, (sx, sy) in enumerate(stations):
            d = (sx - vx) ** 2 + (sy - vy) ** 2
            if d < best_dist or (d == best_dist and i < best_idx):
                best_dist, best_idx = d, i
        result.append(list(stations[best_idx]))
    return result


class TestStationsDriver(unittest.TestCase):
    def test_expected_values_match_brute_force(self) -> None:
        for tc in Problem.get_test_cases():
            bf = _brute_force(tc.stations, tc.vehicles)
            self.assertEqual(
                tc.expected,
                bf,
                msg=(
                    f"stations={tc.stations} vehicles={tc.vehicles}: "
                    f"stored expected={tc.expected}, brute force={bf}"
                ),
            )

    def test_brute_force_tie_breaking(self) -> None:
        """When two stations are equidistant, the one with the smaller index wins."""
        stations = [[0, 0], [1, 0], [0, 1]]
        vehicles = [[2, 2]]
        result = _brute_force(stations, vehicles)
        # dist² to [1,0] = 5, dist² to [0,1] = 5 — tie broken by index 1 < 2
        self.assertEqual(result, [[1, 0]])

    def test_run_returns_correct_structure(self) -> None:
        class BruteForceSolver:
            def nearest_station(self, stations: list, vehicles: list) -> list:
                return _brute_force(stations, vehicles)

        results = Problem.run(BruteForceSolver())
        tcs = Problem.get_test_cases()
        self.assertEqual(len(results), len(tcs))
        for (tc, actual, passed), orig in zip(results, tcs):
            self.assertEqual(tc, orig)
            self.assertTrue(passed)

    def test_run_does_not_mutate_test_cases(self) -> None:
        tc = Problem.get_test_cases()[0]
        original_stations = [list(s) for s in tc.stations]

        class BruteForceSolver:
            def nearest_station(self, stations: list, vehicles: list) -> list:
                for s in stations:
                    s.append(999)
                return _brute_force([[s[0], s[1]] for s in stations], vehicles)

        Problem.run(BruteForceSolver())
        self.assertEqual(tc.stations, original_stations)


if __name__ == "__main__":
    unittest.main()
