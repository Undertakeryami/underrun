
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi


source venv/bin/activate


pip install pygame wonderwords


python main.py
