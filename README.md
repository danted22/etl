### ETL Example Python Code for Interfacing with Airflow on GCP using Cloud Composer

This repository contains example code for Airflow/Composer ETL that runs in GCP.  This is just the DAG definitions and testing required to validate these.  All business logic should be hosted in a separate repository (this example references the IETL private repository which was used to test this example worked).

Special thanks to [@Poogles](https://github.com/Poogles) for vetting the code and providing the initial concept.

#### Notes

This example assumes you have a GCP account and can set up Cloud Composer.  Ideally teraform would be used so that Cloud Composer could be set up with code and destroyed after each use, rather than wasting your free GCP credits whilst you get this to work.

Similarly the example assumes you are using Drone as your CI tool.  In the case of a new Cloud Composer instance you will need to update the CI.  This involves changing the GCS bucket location and updating the service account key in the Drone UI.

#### Getting started

Clone the repository locally and setup a virtual environment.  This needs to be the same Python version that Cloud Composer uses, currently this is 3.6.6.  As the version updates please keep this up to date (and IETL/Drone running the same version).

```sh
# Install the normal and development requirements.
python setup.py develop
# Check the tests run and pass before starting.
pytest --mypy -vv
```

Airflow is installed as part of the requirements, however is not configured straight out of the box.  Airflow installs a directory in your home with its configuration and defaults in.  The `dags_folder` value needs to be updated to point to the dags folder in this repository.  Once that's done you can run the following to get airflow installed.

```sh
# Initialise a local sqlite db stored in ~/airflow
airflow initdb
# Check all your dags are present.   This will include a number of default
# example dags that can be used for testing, and IETL-specific dags.
airflow list_dags
# Run one of the example dags to make sure Airflow is running.
airflow run example_bash_operator also_run_this 2019-02-15
# Check to see if it ran correctly.
airflow task_state example_bash_operator also_run_this 2019-02-15
```

If everything returns success you're set for running locally and have everything required.

#### Deploying

<Steps to get code running in production would be entered here>

#### Testing

Some rudimentary testing is included that checks to see everything is importable and loads in time.

Thing to add would be to verify that each dag file includes at least one valid dag. [here](https://github.com/danielvdende/data-testing-with-airflow/blob/master/integrity_tests/test_dag_integrity.py) is an example of that.
