# Introduction

This repo contains the code and data for the paper "Accuracy and Political Bias of News Source Credibility Ratings by Large Language Models."

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
@article{yang2024accuracy,
  title={Accuracy and Political Bias of News Source Credibility Ratings by Large Language Models},
  author={Yang, Kai-Cheng and Menczer, Filippo},
  journal={Preprint arXiv:2304.00228},
  year={2024}
}
```