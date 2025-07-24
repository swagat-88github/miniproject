import mlflow
import dagshub

# Set the MLflow tracking URI
mlflow.set_tracking_uri('https://dagshub.com/swagat-88github/miniproject.mlflow')

# Initialize DagsHub integration with correct username
dagshub.init(repo_owner='swagat-88github', repo_name='miniproject', mlflow=True)

# Start an MLflow run
with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)

