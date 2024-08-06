"""
This script processes a list of URLs, queries an API model for each URL, and stores the results.

Inputs:
    - url_list_path (str): Path to the csv file containing the list of URLs, must have a column named 'domain'
    - provider (str): The name of the API provider.
    - model (str): The name of the model to query.
    - party (str): The political party affiliation, one of 'dem', 'rep', 'ind'.
    - output_root (str): The directory where the output text files will be saved.

Example:
    python query_llm.py /path/to/domain_list.csv openai gpt-4o-mini-2024-07-18 dem /path/to/output_dir
"""

import sys
import os
from tqdm import tqdm

import api_factory
import prompt_factory

import utils

party_mapping = {
    "dem": "a Democrat",
    "rep": "a Republican",
    "ind": "an Independent",
    "default": "No political identity assigned",
}

if __name__ == "__main__":
    url_list_path = sys.argv[1]
    provider = sys.argv[2]
    model = sys.argv[3]
    party = sys.argv[4]
    output_root = sys.argv[-1]

    if party not in party_mapping:
        raise ValueError(
            f"{party} does not exist, it must be one of {list(party_mapping.keys())}"
        )

    api_key = utils.load_api_key("api_keys.json", provider)
    api_client = api_factory.create_api_client(provider, api_key)
    domains_to_query = utils.get_domain_to_query(url_list_path, output_root)

    print(f"{len(domains_to_query)} domains to query")

    for domain in tqdm(domains_to_query):
        if party == "default":
            system_prompt = prompt_factory.SYS_BASE
        else:
            party_identity = party_mapping[party]
            system_prompt = f"{prompt_factory.SYS_BASE} {prompt_factory.SYS_IDENTITY.format(party=party_identity)}"
        user_instruction = f"{prompt_factory.USER_INSTRUCTION.format(domain=domain)} {prompt_factory.USER_FORMAT}"

        result = api_client.query_model(model, system_prompt, user_instruction)
        with open(os.path.join(output_root, f"{domain}.txt"), "w") as f:
            f.write(result)
