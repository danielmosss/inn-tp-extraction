import spacy
from spacy import displacy
from datetime import datetime
import os

models = ["en_core_web_sm", "nl_core_news_sm", "nl_core_web_lg", "en_core_web_trf"]

def get_input_file():
    input_folder = "input"
    files = os.listdir(input_folder)

    print("Choose a file to process:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")

    if len(files) == 0:
        IndexError("No files found in the input folder")
        exit()

    choice = int(input("Enter the file number: ")) - 1
    return os.path.join(input_folder, files[choice])

def choose_model():
    print("Choose a spaCy model:")
    for i, model in enumerate(models):
        print(f"{i+1}. {model}")
   
    choice = int(input("Enter the model number: ")) - 1
    return models[choice]

def process_file():
    # Choose file
    input_file = get_input_file()
    input_filename = os.path.basename(input_file)

    # Read contents
    with open(input_file, 'r') as f:
        text = f.read()
    
    # get model
    model = choose_model()
    nlp = spacy.load(model)

    # Process the text
    doc = nlp(text)
    html = displacy.render(doc, style="ent")
    
    # GEt time to put in file
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    
    # create filename
    output_folder = "output"
    output_filename = f"output-{input_filename}-{dt_string}.html"
    output_path = os.path.join(output_folder, output_filename)
    
    # write file to path
    with open(output_path, "w") as f:
        f.write(html)
    
    print(f"Output saved as {output_path}")

# Run the process
process_file()
