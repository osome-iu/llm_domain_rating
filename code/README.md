# Introduction

This directory contains the code for our paper.
Content of different files:

- [`api_keys.json`](api_keys.json): API keys for OpenAI, Together.ai, and Google
- [`utils.py`](utils.py): Utility functions
- [`api_factory.py`](api_factory.py): Code to create API objects
- [`prompt_factory.py`](prompt_factory.py): Prompts for the experiments
- [`query_llm.py`](query_llm.py): Script to query the LLM
- [`parse_results.py`](parse_results.py): Script to parse the results

To run the code, you need to set up API keys from OpenAI, Together.ai, and Google and put them in `api_keys.json`.

You can then run the code with the following command:

```bash
python query_llm.py /path/to/domain_list.csv openai "gpt-4o-mini-2024-07-18" dem /path/to/output_dir
```

This will query the `gpt-4o-mini-2024-07-18` model identified as a Democrat on the domains in `domain_list.csv` and save the results in `output_dir`.

## Dependencies

- `together`
- `openai`
- `google-generativeai`
- `tqdm`
- `pandas`
- `pydantic`
- `json_repair`

The code has been tested on Python 3.10.