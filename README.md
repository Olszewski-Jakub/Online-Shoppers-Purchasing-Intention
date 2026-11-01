# Online Shopping Purchase Prediction

CT4101 Machine Learning portfolio project.

## Overview

- **Question:** Can browsing behaviour and session information predict whether a shopping session results in a purchase?
- **Target:** `Revenue` - purchase or no purchase.
- **Status:** Milestone 2 - data audit, preprocessing and baseline implemented.


## Baseline results

The majority-class baseline always predicts no purchase. Across five stratified
cross-validation folds on the training data, it achieves **84.37% accuracy** but
**0% purchase-class F1, precision and recall**. The high accuracy comes from the
class imbalance; it misses every purchase. Later models will be compared mainly
using purchase-class F1. The test set remains unused.

These results describe the supplied historical sessions; they do not establish
performance on future customers or explain what causes a purchase.

## Milestone 2 assistance declaration

The following online resources explain the methods used in the three
Milestone 2 notebooks and support the data audit, preprocessing, evaluation
and majority-class baseline methods:

- [NIST/SEMATECH: What are outliers in the data?](https://itl.nist.gov/div898/handbook/prc/section1/prc16.htm) - box plots, quartiles, the interquartile range and potential outliers in session durations.
- [pandas: DataFrame.drop_duplicates](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html) - removing repeated rows while retaining one occurrence.
- [scikit-learn: Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html) - scaling numerical features and one-hot encoding categorical features within a pipeline.
- [scikit-learn: Common pitfalls and recommended practices - data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage) - fitting preprocessing on training data only and using pipelines during cross-validation.
- [scikit-learn: Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) - holding out a test set and using stratified training folds with similar class proportions.
- [scikit-learn: StratifiedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) - constructing folds that keep similar class proportions.
- [scikit-learn: Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html) - accuracy, precision, recall, F1 and scorers, including interpretation of purchase-class performance under class imbalance.
- [scikit-learn: DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html) - the majority-class baseline using `strategy="most_frequent"`.

## Setup

Requires **Python 3.13** and **uv**.

```bash
uv sync
```

The dataset is included at `data/raw/online_shoppers_intention.csv`. See [dataset documentation](data/README.md).

## Package a milestone

Run the packaging script with your milestone number:

```bash
python3 scripts/package_project.py 1
```

This creates `23710521_Milestone1.zip` in the project root. Omit the number to
enter it interactively. Existing archives are never overwritten.

The archive includes `README.md`, `pyproject.toml`, `uv.lock`, root Python files,
and the `data/`, `notebooks/`, `src/`, and `reports/` directories when present.
It excludes packaging scripts, contributor documentation, Git history,
virtual environments, IDE files, caches, local `.env` files, and ZIP archives.
If runtime files are added elsewhere,
update the inclusion lists in `scripts/package_project.py`.

After extracting, run `uv sync` to install dependencies, then
`uv run jupyter lab` to open the notebooks.
