# inn-tp-extraction

## Step 1
- Clone the repository
- Install the required packages with the following command
  - `pip install -r requirements.txt`

- Install spaCy with the following command
  - `pip install -U pip setuptools wheel`
    - `pip install -U spacy`

- Download the spaCy model with the following command
    - `python -m spacy download en_core_web_sm`
    - `python -m spacy download nl_core_web_sm`

## Step 2
- Create 2 folders in the root directory of the project
  - `input`
  - `output`

## Step 3
- Place the input files in the `input` folder

## Step 4
- Run the project with the following command
  - `python main.py`