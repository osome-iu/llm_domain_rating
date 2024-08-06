# Introduction

This folder contains the data for our paper.

## LLM ratings

The file `llm_ratings.parquet` contains the responses from the LLMs in parquet format.
It contains the following columns:

| Column Name   | Description                                                    | Data Type    |
|---------------|----------------------------------------------------------------|--------------|
| domain        | The domain being examined                                      | String       |
| rating        | The rating assigned to the website, indicating its credibility | Float, [0, 1]|
| explanation   | A brief explanation for the rating                             | String       |
| model         | The LLM used to generate the rating and explanation            | String       |
| identity      | The political identity assigned to the model                   | String       |

The model column indicates the specific versions of the LLMs used in our experiments:

| Model code name | Model official name with version |
|-----------------|-----------------------------------|
| gpt4omini20240718 | gpt-4o-mini-2024-07-18 |
| gpt4o20240513 | gpt-4o-2024-05-13 |
| gpt4turbo20240409 | gpt-4-turbo-2024-04-09 |
| llama318binstructturbo | meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo |
| llama3170binstructturbo | meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo |
| llama31405binstructturbo | meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo |
| gemini15flash001 | models/gemini-1.5-flash-001 |
| gemini15pro001 | models/gemini-1.5-pro-001 |

The identity column indicates the political identity assigned to the LLM:

| Identity code name | Identity |
|-------------------|----------|
| Default | No political identity assigned |
| Dem | Democrat |
| Ind | Independent |
| Rep | Republican |

The default configuration contains results on 7,523 domains.
The political identity analyses are only performed on 2,683 domains with political bias scores.