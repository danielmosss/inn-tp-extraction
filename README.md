# inn-tp-extraction

## Step 1
- Clone the repository

- Install python 3.11 from the windows store

- Install the required packages with the following command
  - `pip install -r requirements.txt`

- Install spaCy with the following command
  - `pip install -U pip setuptools wheel`
  - `pip install -U spacy`

- Downloads for the efficiency spaCy models
  - `python -m spacy download en_core_web_sm`
  - `python -m spacy download nl_core_news_sm`

- Downloads for the accuracy spaCy models
  - `python -m spacy download en_core_web_trf`
  - `python -m spacy download nl_core_news_lg`

## Step 2
- Create 2 folders in the root directory of the project
  ```bash
  mkdir input
  mkdir output
  ```

## Step 3
- Place the input files in the `input` folder

## Step 4
- Run the project with the following command
  - `python main.py`