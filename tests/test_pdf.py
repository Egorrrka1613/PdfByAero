import pytest
from deepdiff import DeepDiff

from src.ticket import Ticket


@pytest.mark.parametrize(
    "compared_file_name,need_deep",
    [
        ("edit_test_task.pdf", False),
        ("edit_test_task2.pdf", True),
        ("edit_test_task3.pdf", True),
    ],
    ids=["test_by_wrong_key", "test_by_wrong_value", "test_move_element"],
)
def test_deep(compared_file_name, need_deep):
    original_data = Ticket("test_task.pdf").parsing_file(need_deep)
    wrong_data = Ticket(compared_file_name).parsing_file(need_deep)
    assert wrong_data == original_data, "\nDifference: \n" + str(
        DeepDiff(original_data, wrong_data)
    )
