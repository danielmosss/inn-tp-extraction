import spacy
from spacy import displacy
from datetime import datetime
import os

models = ["en_core_web_sm", "nl_core_news_sm"]

# Function to list and choose files from the input directory
def get_input_file():
    input_folder = "input"
    files = os.listdir(input_folder)
    
    # Display files to the user
    print("Choose a file to process:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")
    
    # Get the user's choice
    choice = int(input("Enter the file number: ")) - 1
    return os.path.join(input_folder, files[choice])

def choose_model():
    print("Choose a spaCy model:")
    for i, model in enumerate(models):
        print(f"{i+1}. {model}")
    
    choice = int(input("Enter the model number: ")) - 1
    return models[choice]

# Main processing function
def process_file():
    # Get the chosen input file
    input_file = get_input_file()
    input_filename = os.path.basename(input_file)

    # Read the content from the file
    with open(input_file, 'r') as f:
        text = f.read()
    
    # Load the spaCy model and process the text
    model = choose_model()
    nlp = spacy.load(model)
    doc = nlp(text)
    
    # Render the named entities as HTML
    html = displacy.render(doc, style="ent")
    
    # Get the current date and time
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    
    # Output filename format with the original input filename and timestamp
    output_folder = "output"
    output_filename = f"output-{input_filename}-{dt_string}.html"
    output_path = os.path.join(output_folder, output_filename)
    
    # Save the output HTML file in the output directory
    with open(output_path, "w") as f:
        f.write(html)
    
    print(f"Output saved as {output_path}")

# Run the process
process_file()
