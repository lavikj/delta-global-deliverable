"""
DocumentTypes.py

This file specifies the implementations of the load function for different document types.
It is meant to be the only thing that needs to be specified by the user when adding new 
document types.
"""


from Ingestion.Architecture import Chunk, Document
import pandas as pd
import os
import json


class FootballDocument(Document):

    # Extract content from CSV
    def load_chunks(self) -> None:
        try:
            df = pd.read_csv(self.dir)
            if "content" in df.columns:
                contents = df["content"].dropna().tolist()
                for content in contents:
                    self.chunks.append(Chunk(content)) 
            else:
                raise ValueError("The CSV file does not contain a 'content' column.")
        except Exception as e:
            print(f"Error: {e}")
            return []


class FinanceDocument(Document):

    # Extract content from JSON
    def load_chunks(self) -> None:
        for filename in os.listdir(self.dir):
            if filename.endswith(".json"):  # Ensure it's a JSON file
                filepath = os.path.join(self.dir, filename)
                with open(filepath, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    if "text" in data:  # Check if "text" attribute exists
                        self.chunks.append(Chunk(data["text"]))
