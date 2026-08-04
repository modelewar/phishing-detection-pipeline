# Phishing Detection Pipeline

This project is an end-to-end machine learning pipeline for detecting phishing URLs. It follows a modular architecture that covers data ingestion, validation, transformation, model training, and prediction through a simple FastAPI-based interface.

The pipeline is designed to help you train a phishing detection model locally, save artifacts, and expose prediction endpoints for testing and deployment.

## Project Overview

The workflow includes:

- ingesting data from MongoDB
- validating the incoming dataset structure
- transforming features for model training
- training a classifier for phishing detection
- serving predictions through a local API

## Project Structure

```text
phishing-detection-pipeline/
├── app.py                   # FastAPI application entry point
├── main.py                  # Training pipeline runner
├── push_data.py             # Seed data into MongoDB
├── requirements.txt         # Python dependencies
├── setup.py                 # Local package installation config
├── config/                  # Configuration files
├── data_schema/             # Dataset schema definitions
├── src/                     # Core source package
│   ├── components/          # Data ingestion, validation, transformation, training
│   ├── config/             # Configuration utilities
│   ├── constant/           # Pipeline constants and artifact names
│   ├── entity/             # Config/artifact entity definitions
│   ├── exception/          # Custom exception handling
│   ├── logging/            # Logging setup
│   ├── pipeline/           # Training orchestration pipeline
│   └── utils/              # Shared helpers and model utilities
├── templates/               # HTML templates for prediction output
└── logs/                    # Runtime and training logs
```

## Prerequisites

Before you begin, make sure you have:

- Python 3.8+ installed
- pip installed
- MongoDB running locally (or a reachable MongoDB instance)
- Git installed

## Local Setup

1. Clone the repository and change into the project directory:

```bash
git clone <repository-url>
cd phishing-detection-pipeline
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install the package in editable mode so imports work correctly:

```bash
pip install -e .
```

5. Configure environment variables.

Create a `.env` file in the project root with your MongoDB connection string:

```env
MONGO_DB_URL=mongodb://localhost:27017
```

If MongoDB is not running yet, start it before running the pipeline.

## Running the Pipeline

### 1. Seed data into MongoDB

If the database collection is empty, run:

```bash
python push_data.py
```

### 2. Run the training pipeline

```bash
python main.py
```

This will execute the full pipeline:

- data ingestion
- validation
- transformation
- model training

### 3. Run the FastAPI app locally

To start the web API:

```bash
python app.py
```

Then open:

```text
http://localhost:8000/docs
```

You can use the `/train` endpoint to trigger training and the `/predict` endpoint to upload a CSV file and get predictions.

## Notes

- Model artifacts and prediction outputs are written to the project folders such as `final_model/` and `prediction_output/`.
- Logs are stored in the `logs/` directory.
- If you modify the schema or data source, update the relevant files under `config/` and `data_schema/` accordingly.

