"""
DAG_NAME = "amb_run"
Executes the tasks needed to import data from the Amobee DSP into a CloudSQL database

Cost Centre:  Data Team
Business Contact: Dan de Sybel
"""
from typing import Any, Dict, List

from airflow import DAG  # type: ignore
from airflow.operators.python_operator import PythonVirtualenvOperator  # type: ignore

from dependencies.config import IETL_VERSION, DEFAULT_ARGS

DAG_REQUIREMENTS: List[str] = [IETL_VERSION]
# TODO: Any overrides required for this DAG.
DAG_OVERRIDES: Dict[str, Any] = {"default": None}
DAG_DEFAULT_ARGS: Dict[str, Any] = {**DAG_OVERRIDES, **DEFAULT_ARGS}

dag = DAG(
    "amb_run",
    schedule_interval="@daily",  # Once at midnight.
    catchup=False,
    default_args=DEFAULT_ARGS,
)


def amb_packages_pull() -> None:
    """TODO: amb_packages_pull annotation.
    """
    from jobs.amobee.dimensions.amb_packages_pull import AmbPackagesPull

    dag_name = "amb_run"
    with AmbPackagesPull("AmbPackagesPull", dag_name=dag_name) as job:
        job.run()


def amb_line_item_creatives_bd_pull() -> None:
    """TODO: amb_line_item_creatives_bd_pull annotation.
    """
    from jobs.amobee.facts.amb_line_item_creatives_bd_pull import (
        AmbLineItemCreativesBdPull,
    )

    dag_name = "amb_run"
    with AmbLineItemCreativesBdPull(
        "AmbLineItemCreativesBdPull", dag_name=dag_name
    ) as job:
        job.run()


def amb_insertion_orders_pull() -> None:
    """TODO: amb_insertion_orders_pull annotation.
    """
    from jobs.amobee.dimensions.amb_insertion_orders_pull import AmbInsertionOrdersPull

    dag_name = "amb_run"
    with AmbInsertionOrdersPull("AmbInsertionOrdersPull", dag_name=dag_name) as job:
        job.run()


def amb_creative_costs_sftp_fetch() -> None:
    """TODO: amb_creative_costs_sftp_fetch annotation.
    """
    from jobs.amobee.facts.amb_creative_costs_sftp_fetch import (
        AmbCreativeCostsSftpFetch,
    )

    dag_name = "amb_run"
    with AmbCreativeCostsSftpFetch(
        "AmbCreativeCostsSftpFetch", dag_name=dag_name
    ) as job:
        job.run()


def amb_creatives_pull() -> None:
    """TODO: amb_creatives_pull annotation.
    """
    from jobs.amobee.dimensions.amb_creatives_pull import AmbCreativesPull

    dag_name = "amb_run"
    with AmbCreativesPull("AmbCreativesPull", dag_name=dag_name) as job:
        job.run()


def amb_creatives_bd_upsert() -> None:
    """TODO: amb_creatives_bd_upsert annotation.
    """
    from jobs.amobee.facts.amb_creatives_bd_upsert import AmbCreativesBdUpsert

    dag_name = "amb_run"
    with AmbCreativesBdUpsert("AmbCreativesBdUpsert", dag_name=dag_name) as job:
        job.run()


def amb_conversions_bh_extract() -> None:
    """TODO: amb_conversions_bh_extract annotation.
    """
    from jobs.amobee.facts.amb_conversions_bh_extract import AmbConversionsBhExtract

    dag_name = "amb_run"
    with AmbConversionsBhExtract("AmbConversionsBhExtract", dag_name=dag_name) as job:
        job.run()


def amb_conversions_sftp_fetch() -> None:
    """TODO: amb_conversions_sftp_fetch annotation.
    """
    from jobs.amobee.facts.amb_conversions_sftp_fetch import AmbConversionsSftpFetch

    dag_name = "amb_run"
    with AmbConversionsSftpFetch("AmbConversionsSftpFetch", dag_name=dag_name) as job:
        job.run()


def amb_adserving_fees_extract() -> None:
    """TODO: amb_adserving_fees_extract annotation.
    """
    from jobs.amobee.facts.amb_adserving_fees_extract import AmbAdservingFeesExtract

    dag_name = "amb_run"
    with AmbAdservingFeesExtract("AmbAdservingFeesExtract", dag_name=dag_name) as job:
        job.run()


def imd_adserving_fees_amb_upsert() -> None:
    """TODO: imd_adserving_fees_amb_upsert annotation.
    """
    from jobs.amobee.facts.imd_adserving_fees_amb_upsert import (
        ImdAdservingFeesAmbUpsert,
    )

    dag_name = "amb_run"
    with ImdAdservingFeesAmbUpsert(
        "ImdAdservingFeesAmbUpsert", dag_name=dag_name
    ) as job:
        job.run()


def amb_advertisers_pull() -> None:
    """TODO: amb_advertisers_pull annotation.
    """
    from jobs.amobee.dimensions.amb_advertisers_pull import AmbAdvertisersPull

    dag_name = "amb_run"
    with AmbAdvertisersPull("AmbAdvertisersPull", dag_name=dag_name) as job:
        job.run()


def amb_creatives_details_pull() -> None:
    """TODO: amb_creatives_details_pull annotation.
    """
    from jobs.amobee.dimensions.amb_creatives_details_pull import (
        AmbCreativesDetailsPull,
    )

    dag_name = "amb_run"
    with AmbCreativesDetailsPull("AmbCreativesDetailsPull", dag_name=dag_name) as job:
        job.run()


def amb_run() -> None:
    """TODO: amb_run annotation.
    """
    from jobs.amobee.amb_run import AmbRun

    dag_name = "amb_run"
    with AmbRun("AmbRun", dag_name=dag_name) as job:
        job.run()


def amb_line_items_pull() -> None:
    """TODO: amb_line_items_pull annotation.
    """
    from jobs.amobee.dimensions.amb_line_items_pull import AmbLineItemsPull

    dag_name = "amb_run"
    with AmbLineItemsPull("AmbLineItemsPull", dag_name=dag_name) as job:
        job.run()


def amb_insertion_orders_deal_id_update() -> None:
    """TODO: amb_insertion_orders_deal_id_update annotation.
    """
    from jobs.amobee.dimensions.amb_insertion_orders_deal_id_update import (
        AmbInsertionOrdersDealIdUpdate,
    )

    dag_name = "amb_run"
    with AmbInsertionOrdersDealIdUpdate(
        "AmbInsertionOrdersDealIdUpdate", dag_name=dag_name
    ) as job:
        job.run()


with dag:
    amb_packages_pull_operator = PythonVirtualenvOperator(
        python_callable=amb_packages_pull,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_packages_pull",
    )

    amb_line_item_creatives_bd_pull_operator = PythonVirtualenvOperator(
        python_callable=amb_line_item_creatives_bd_pull,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_line_item_creatives_bd_pull",
    )

    amb_insertion_orders_pull_operator = PythonVirtualenvOperator(
        python_callable=amb_insertion_orders_pull,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_insertion_orders_pull",
    )

    amb_creative_costs_sftp_fetch_operator = PythonVirtualenvOperator(
        python_callable=amb_creative_costs_sftp_fetch,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_creative_costs_sftp_fetch",
    )

    amb_creatives_pull_operator = PythonVirtualenvOperator(
        python_callable=amb_creatives_pull,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_creatives_pull",
    )

    amb_creatives_bd_upsert_operator = PythonVirtualenvOperator(
        python_callable=amb_creatives_bd_upsert,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_creatives_bd_upsert",
    )

    amb_conversions_bh_extract_operator = PythonVirtualenvOperator(
        python_callable=amb_conversions_bh_extract,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_conversions_bh_extract",
    )

    amb_conversions_sftp_fetch_operator = PythonVirtualenvOperator(
        python_callable=amb_conversions_sftp_fetch,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_conversions_sftp_fetch",
    )

    amb_adserving_fees_extract_operator = PythonVirtualenvOperator(
        python_callable=amb_adserving_fees_extract,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_adserving_fees_extract",
    )

    imd_adserving_fees_amb_upsert_operator = PythonVirtualenvOperator(
        python_callable=imd_adserving_fees_amb_upsert,
        requirements=DAG_REQUIREMENTS,
        task_id="imd_adserving_fees_amb_upsert",
    )

    amb_advertisers_pull_operator = PythonVirtualenvOperator(
        python_callable=amb_advertisers_pull,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_advertisers_pull",
    )

    amb_creatives_details_pull_operator = PythonVirtualenvOperator(
        python_callable=amb_creatives_details_pull,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_creatives_details_pull",
    )

    amb_run_operator = PythonVirtualenvOperator(
        python_callable=amb_run, requirements=DAG_REQUIREMENTS, task_id="amb_run"
    )

    amb_line_items_pull_operator = PythonVirtualenvOperator(
        python_callable=amb_line_items_pull,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_line_items_pull",
    )

    amb_insertion_orders_deal_id_update_operator = PythonVirtualenvOperator(
        python_callable=amb_insertion_orders_deal_id_update,
        requirements=DAG_REQUIREMENTS,
        task_id="amb_insertion_orders_deal_id_update",
    )

    amb_packages_pull_operator.set_downstream(amb_creatives_bd_upsert_operator)
    amb_line_item_creatives_bd_pull_operator.set_downstream(
        amb_creatives_bd_upsert_operator
    )
    amb_insertion_orders_pull_operator.set_downstream(
        amb_insertion_orders_deal_id_update_operator
    )
    amb_creatives_pull_operator.set_downstream(amb_creatives_details_pull_operator)
    amb_conversions_sftp_fetch_operator.set_downstream(
        amb_conversions_bh_extract_operator
    )
    amb_adserving_fees_extract_operator.set_downstream(
        imd_adserving_fees_amb_upsert_operator
    )
    amb_advertisers_pull_operator.set_downstream(amb_creatives_bd_upsert_operator)
    amb_creatives_details_pull_operator.set_downstream(
        amb_adserving_fees_extract_operator
    )
    amb_run_operator.set_downstream(amb_creative_costs_sftp_fetch_operator)
    amb_run_operator.set_downstream(amb_conversions_sftp_fetch_operator)
    amb_run_operator.set_downstream(amb_line_items_pull_operator)
    amb_run_operator.set_downstream(amb_insertion_orders_pull_operator)
    amb_run_operator.set_downstream(amb_advertisers_pull_operator)
    amb_run_operator.set_downstream(amb_packages_pull_operator)
    amb_run_operator.set_downstream(amb_creatives_pull_operator)
    amb_line_items_pull_operator.set_downstream(amb_creatives_bd_upsert_operator)
    amb_line_items_pull_operator.set_downstream(
        amb_line_item_creatives_bd_pull_operator
    )
    amb_insertion_orders_deal_id_update_operator.set_downstream(
        amb_creatives_bd_upsert_operator
    )
