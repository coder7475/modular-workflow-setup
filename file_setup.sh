#!/bin/bash

list_of_files=(
    "src/__init__.py"
    "src/components/__init__.py"
    "src/components/data_ingestion.py"
    "src/components/data_transformation.py"
    "src/components/model_trainer.py"
    "src/components/model_monitoring.py"
    "src/pipelines/__init__.py"
    "src/pipelines/training_pipeline.py"
    "src/pipelines/prediction_pipeline.py"
    "src/exception.py"
    "src/logger.py"
    "src/utils.py"
    "main.py"
)

for filepath in "${list_of_files[@]}"; do
    filedir=$(dirname "$filepath")
    filename=$(basename "$filepath")

    if [ ! -d "$filedir" ] && [ "$filedir" != "." ]; then
        mkdir -p "$filedir"
        echo "Creating directory: $filedir for the file $filename"
    fi

    if [ ! -e "$filepath" ] || [ ! -s "$filepath" ]; then
        touch "$filepath"
        echo "Creating empty file: $filepath"
    else
        echo "$filename already exists"
    fi
done