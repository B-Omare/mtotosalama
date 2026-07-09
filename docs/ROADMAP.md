# Roadmap

This project is built incrementally and transparently. Each item below is marked
with its actual current status. This file is updated as work progresses, not
written once and forgotten.

## Status legend
- ✅ Built and tested
- 🚧 In progress
- 📋 Planned, not yet started

## Deliverables

| # | Deliverable | Status | Notes |
|---|---|---|---|
| 1 | ETL / multi-source data engineering pipeline | 🚧 | Public sources only: DHIS2, KDHS, ERA5, Sentinel-2, OSM/GADM |
| 2 | Causal inference layer (DiD, RDD, IPW, mediation) | 📋 | |
| 3 | Bayesian hierarchical survival model | 📋 | |
| 4 | Spatial ML and climate integration | 📋 | |
| 5 | Swahili NLP and LLM-based CHW assistant | 📋 | |
| 6 | ML ensemble (XGBoost, survival forest, GNN, anomaly detection) | 📋 | |
| 7 | Quantum-enhanced resource allocation (QAOA) | 📋 | Local simulator scale first, given hardware constraints |
| 8 | Explainability and fairness audit | 📋 | |
| 9 | API layer | 📋 | |
| 10 | Bilingual dashboard | 📋 | |

## Data access notes

- Siaya HDSS and CHAMPS Network data require formal research agreements and are
  **not used** in this repository. Where the original design depends on them,
  synthetic data with matching structure is substituted, and this is documented
  in the relevant module's docstring and any related notebook.
- All ten target counties (former Nyanza + Western provinces) are covered
  wherever the underlying public data source has that geographic coverage.

## Academic outputs

Planned, contingent on results: see original concept note for target journals.
None of these have been drafted yet they will be added here as preprints
become available, not before.