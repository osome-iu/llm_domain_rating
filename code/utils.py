import os
import pandas as pd
import json
from pydantic import BaseModel, Field


class DomainRating(BaseModel):
    rating: float = Field(
        description="Domain credibility rating, ranging from -1 to 1",
        ge=-1,
        le=1,
    )
    url: str = Field(description="The URL.")
    explanation: str = Field(description="Explanation of the rating.")


def load_api_key(api_key_path, provider):
    with open(api_key_path) as f:
        key_obj = json.load(f)
        if provider not in key_obj:
            raise ValueError(
                f"Unknown provider: {provider}, must be one of {key_obj.keys()}"
            )

        api_key = key_obj.get(provider)
        return api_key


def get_domain_to_query(url_list_path, output_root):
    domain_df = pd.read_csv(url_list_path, usecols=["domain"])
    processed_domains = set()
    for file_name in os.listdir(output_root):
        if file_name.endswith(".txt"):
            processed_domains.add(file_name[:-4])

    print(f"{len(processed_domains)} domains have been processed")

    domain_to_query = domain_df[
        ~domain_df.domain.isin(processed_domains)
    ].domain.tolist()
    return domain_to_query
