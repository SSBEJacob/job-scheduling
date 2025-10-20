# Optimal Scheduling Experiment

This repository contains all code, analysis scripts, and results for an **optimal scheduling experiment** built using [oTree](https://www.otree.org/). The experiment investigates how participants make scheduling decisions under resource constraints and deadline pressures, comparing human performance to algorithmic or model-based benchmarks.

---

## 🧠 Overview

Participants are tasked with **allocating limited resources (workers)** to a series of **jobs with varying deadlines, rewards, and penalties**.
Each period, they must decide:

* Which jobs to accept or reject,
* When to work on accepted jobs,
* And how to manage their 10-unit resource constraint per period.

Performance is evaluated based on the **total payoff achieved** relative to the **optimal scheduling policy** derived from computational models.

The experiment was implemented in **oTree**, allowing real-time decision making, logging of participant choices, and structured data export for analysis.

---

## ⚙️ Running the Experiment

### Prerequisites

* Python 3.10+
* [oTree](https://otree.readthedocs.io/en/latest/) ≥ 5.0
* Recommended: virtual environment (conda or venv)

---

## 📊 Analysis

All scripts for data cleaning, aggregation, and visualization are included in the `analysis-code` folder.

Analyses include:

* Average earnings by treatment
* Completion rates and lateness distributions
* Comparison between **human participants** and **optimal scheduling benchmarks**

---

## 📈 Results

All figures showing comparative performance between subjects and the optimal policy are stored in the `results/` folder.
These include:

* **Performance summary plots**
* **Learning curves across periods**
* **Resource utilization heatmaps**
* **Deviation from optimal policy metrics**

---

## 🧩 Citation

If you use this code or data in academic work, please cite:

> Cohn, J. (2025). *Performance of Reinforcement Learning Relative to Human Participants in Job Scheduling Environments*. Chapman University.

---

## 🪪 License

This repository is distributed under the MIT License.
See `LICENSE` for more details.

---
