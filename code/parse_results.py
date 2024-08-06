"""
This script processes text files containing API model responses, validates and repairs the JSON content, and compiles the results into a DataFrame, which is then saved as a Parquet file.

Inputs:
    - provider (str): The name of the API provider.
    - model (str): The name of the model used.
    - party (str): The political identity, one of 'dem', 'rep', 'ind', and 'default'.
    - resp_path (str): The directory containing the response text files.
    - output_path (str): The path where the output Parquet file will be saved.

Outputs:
    - A Parquet file containing the compiled DataFrame with domain ratings and associated metadata.

Example:
    python script_name.py openai gpt-4o-mini-2024-07-18 dem /path/to/raw/responses/ /path/to/output/ratings.parquet
"""

import os
import sys
import pandas as pd
from json_repair import repair_json
from utils import DomainRating

if __name__ == "__main__":
    provider = sys.argv[1]
    model = sys.argv[2]
    party = sys.argv[3]
    resp_path = sys.argv[4]
    output_path = sys.argv[-1]

    rating_dict_list = []
    for file_name in os.listdir(resp_path):
        if file_name.endswith(".txt"):
            domain = file_name[:-4]
            with open(os.path.join(resp_path, file_name), "r") as f:
                resp = f.read()
                # Llama models sometimes return invalid JSON objects, need to repair them for parsing
                if "llama" in model:
                    resp = repair_json(resp)
                rating_obj = DomainRating.model_validate_json(resp)
                rating_dict = rating_obj.dict()
                rating_dict["domain"] = domain
                rating_dict_list.append(rating_dict)
    rating_df = pd.DataFrame(rating_dict_list)
    rating_df["provider"] = provider
    rating_df["model"] = model
    rating_df["party"] = party
    rating_df.to_parquet(output_path, index=False)
