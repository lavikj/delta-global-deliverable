# Goal
Datasets of text come in various and complex forms. This repository contains the logic for processing datasets structured in different ways to uniformly return text embeddings of the data. Explicitly, the user should only need to specify the directory to the dataset and provide an implementation of how to extract chunks of text from files/directories in the dataset. 

# Setup

## 1. Clone the Repository  
```sh
git clone https://github.com/lavikj/delta-global-deliverable.git
cd delta-global-deliverable
```

## 2. Set Up a Virtual Environment (Recommended)
Creating a virtual environment ensures that dependencies don’t conflict with other Python projects on your system.
```sh
python -m venv venv
```

### On macOS/Linux:
```sh
source venv/bin/activate
```

### On Windows:
```sh
venv\Scripts\activate
```

## 3. Install Dependencies
```sh
pip install -r requirements.txt
```
