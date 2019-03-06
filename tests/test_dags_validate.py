from airflow.models import DagBag  # type: ignore
import pytest  # type: ignore


LOAD_SECOND_THRESHOLD = 2  # seconds


@pytest.fixture
def ietl_dagbag() -> DagBag:
    return DagBag(dag_folder="dags")


def test_dags_validate(ietl_dagbag) -> None:
    assert not len(ietl_dagbag.import_errors), "Errors found in DagBag import."


def test_dags_load_quickly(ietl_dagbag) -> None:
    stats = ietl_dagbag.dagbag_stats
    slow_files = [x for x in stats if x.duration > LOAD_SECOND_THRESHOLD]
    res = ", ".join(map(lambda d: d.file[1:], slow_files))
    assert len(slow_files) == 0, "Slow loads detected: " + res
