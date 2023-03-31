#!/bin/bash
export API_KEY=d3b7c1458amsh18c268d298148c9p1f55ccjsn9a161d57b562
# Check for Python version
if command -v python3 >/dev/null 2>&1; then
    python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
elif command -v python >/dev/null 2>&1; then
    python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
else
    echo "Python not found. Please install Python and try again."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python -m venv stockdata --python=python$python_version

# Activate the virtual environment
echo "Activating virtual environment..."
source myenv/bin/activate

# Install dependencies using pip with the same version of Python
echo "Installing dependencies..."
pip$python_version install -r requirements.txt

# Run the Python script
echo "Running script..."
python$python_version stocks.py

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
# deactivate
