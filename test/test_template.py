
import pytest

from problems.template import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case(solution):
    # Arrange: define the input
    nums = [1, 2, 3]

    # Act: call your implementation
    # actual = solution.solve(nums)

    # Assert: compare with the expected output
    # assert actual == expected

    pytest.skip("Replace with a real test case")


def test_edge_case(solution):
    # TODO: Test an edge case
    pytest.skip("Add an edge case")


def test_another_case(solution):
    # TODO: Add another representative test
    pytest.skip("Add another test case")
