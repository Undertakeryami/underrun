

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Setting up UnderRun environment..."


VENV_DIR="$SCRIPT_DIR/venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in ./venv..."
    python3 -m venv "$VENV_DIR"
else
    echo "Using existing virtual environment in ./venv"
fi

echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "Installing dependencies (pygame, wonderwords)..."
pip install pygame wonderwords


echo "Starting thehehehe game..."
python "$SCRIPT_DIR/main.py"

echo "Game finished. To reactivate environment later, run:"
echo "  source venv/bin/activate"