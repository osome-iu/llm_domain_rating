# Introduction

This repo contains the code and data for the paper "[Accuracy and Political Bias of News Source Credibility Ratings by Large Language Models](https://doi.org/10.1145/3717867.3717903)."

Also, check out our [dashboard](https://yang3kc.github.io/llm_domain_classification/) with updated results for more recent LLMs.

# Data

We use the following data in our study:

| Data | Location | Note |
|------|----------|------|
| Aggregate domain rating list from Lin et al. | https://github.com/hauselin/domain-quality-ratings | Please download the data in their repo. |
| Tranco list | https://tranco-list.eu | Please download the data from their website. |
| Domain political bias rating | https://doi.org/10.7910/DVN/QAN5VX | Please download the data from the data repository. |
| LLM ratings | [/data/llm_ratings.parquet](/data/llm_ratings.parquet) | We share the responses from the LLMs here. |

# Code

We share the code that we used to query the LLMs in [/code](/code).

# Citation

You can cite our work as follows:

```bib
@inproceedings{yang2025accuracy,
    author = {Yang, Kai-Cheng and Menczer, Filippo},
    title = {Accuracy and Political Bias of News Source Credibility Ratings by Large Language Models},
    year = {2025},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3717867.3717903},
    doi = {10.1145/3717867.3717903},
    booktitle = {Proceedings of the 17th ACM Web Science Conference 2025},
    pages = {127–137},
    numpages = {11},
    series = {Websci '25}
}
```
