# inn-tp-extraction

## Step 1
- Clone the repository

## Step 2 - Install python 3.11
- https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe

### Step 2.2 - Add Python to PATH
  Add the following path to you PATH environment variable
  ```bash
  C:/Users/{username}/local/programs/python/Python311/Scripts
  ```

## Step 3
- Install the required packages with the following command
  ```bash
  pip install -r requirements.txt
  ```

## Step 3.1 - Error handling
- IF giving error: ImportError: DLL load failed while importing numpy_ops: The specified module could not be found.
then download https://aka.ms/vs/17/release/vc_redist.x64.exe

## Step 4 - Download the spaCy models
- Downloads for the efficiency spaCy models
  ```bash
  python -m spacy download en_core_web_sm
  python -m spacy download nl_core_news_sm
  ```

- Downloads for the accuracy spaCy models
  ```bash
  python -m spacy download en_core_web_trf
  python -m spacy download nl_core_news_lg
  ```

## Step 5
- Create 2 folders in the root directory of the project
  ```bash
  mkdir input output
  ```

## Step 6
- Place the input files in the `input` folder
- This should be an TXT file with text in it. 

## Step 7
- Run the project with the following command
  - `python main.py`
  - Choose depending on you input file text language the right model.
  - The large model will preform significantly better.