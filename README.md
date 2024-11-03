# arachneAI
## Setup
Setup python virtual environment and install requirements
```bash
python -m venv venv
source venv/bin/activate
pip install -r requimrents.txt
```
***
## Usage
Get your gemini API from [aistudio.google.com](https://aistudio.google.com)
> Change your model in `src/gemini.py` if you want to

Store your API key using
```bash
export GOOGLE_API_KEY=<api_key_here>
```

Then just run the app using
```bash
python app.py
```
And the server will be started at `localhost:5000` 
