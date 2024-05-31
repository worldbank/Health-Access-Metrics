#!/bin/bash

# Activate your Python virtual environment if needed
source activate geo_wb_linux_parallel


# Define Python script file path
PYTHON_SCRIPT="/home/jupyter-wb618081/Health-Access-Metrics/notebooks/pak_vector_parallel_rtree_opt.py"

# Execute the Python script
time python "$PYTHON_SCRIPT"


conda deactivate