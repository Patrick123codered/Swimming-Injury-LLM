import os
from pathlib import Path
import pickle
#from pypdf import PdfReader
from langchain.docstore.document import Document
from langchain_community.document_loaders import TextLoader
#from langchain_community.document_loaders.csv_loader import CSVLoader




def list_txt_files(data_dir="./data"):
    try:
        seen = pickle.load(os.path.join(data_dir, "seen.pkl"))
    except:
        seen = []
    paths = Path(data_dir).glob('**/*.txt')
    for path in paths:
        if path in seen:
            pass
        else:
            seen.append(path)
            yield str(path)
    with open ("seen.pkl", 'wb') as picklefile:
        pickle.dump(seen, picklefile)
    




def load_txt_files(data_dir="./data"):
    docs = []
    paths = list_txt_files(data_dir)
    for path in paths:
        #print(f"Loading {path}")
        loader = TextLoader(path)
        #if loader:
         #   print("Load was not empty")
        #print(loader.load())
        docs.extend(loader.load())
    print(docs)
    return docs






