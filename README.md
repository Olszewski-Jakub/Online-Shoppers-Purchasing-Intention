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
