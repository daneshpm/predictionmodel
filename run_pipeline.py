import click
from pipelines.training_pipeline import ml_pipeline
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri


@click.command()
def main():
    """
    Run the ML pipeline and start the MLflow UI for experiment tracking.
    """
    # Run the pipeline
    run = ml_pipeline()

    # Inspect run output
    if isinstance(run, dict) and "model_building_step" in run:
        trained_model = run["model_building_step"]
        print(f"Trained Model Type: {type(trained_model)}")
    else:
        print("Warning: Unable to retrieve trained model. Check pipeline output format.")

    print(
        "Now run \n "
        f"    mlflow ui --backend-store-uri '{get_tracking_uri()}'\n"
        "To inspect your experiment runs within the mlflow UI.\n"
        "You can find your runs tracked within the experiment."
      )


if __name__ == "__main__":
    main()
