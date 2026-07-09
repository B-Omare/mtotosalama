# Architecture

## Repository layout

mtotosalama/
├── data/
│   ├── raw/          # Original downloaded data, untouched (gitignored)
│   ├── interim/       # Cleaned, validated intermediate data (gitignored)
│   ├── processed/     # Model-ready, feature-engineered data (gitignored)
│   └── external/      # Third-party reference data: climate, satellite, boundaries (gitignored)
├── src/mtotosalama/
│   ├── ingestion/      # Data loading, validation, cleaning, harmonisation
│   ├── analysis/       # Causal inference, Bayesian survival modelling
│   ├── models/         # ML ensemble (XGBoost, survival forest, etc.)
│   └── dashboard/       # Streamlit bilingual dashboard (planned)
├── pipeline/           # Snakemake workflow definitions
├── tests/unit/         # pytest test suite
├── notebooks/          # Exploratory analysis notebooks
├── docs/               # This documentation
├── configs/            # YAML configuration (data source URLs, model params)
└── .github/workflows/  # CI: automated testing on push


Data folders are gitignored deliberately, this is a reproducibility pattern, not an
oversight. Anyone cloning this repo re-derives `data/` by running the ingestion
pipeline against the public sources listed in the README, rather than downloading
large files from Git. This keeps the repository lightweight and avoids ever
accidentally distributing restricted-access health data.

## Design principles

1. **Package, not scripts.** All logic lives in the installable `src/mtotosalama`
   package, not loose notebook cells notebooks import from the package, not the
   other way round.
2. **Explicit data provenance.** Every dataset used is either genuinely public (see
   README data sources table) or clearly synthetic, never silently assumed.
3. **Tested before trusted.** Any ingestion, transformation, or modelling function
   that other code depends on has a corresponding test in `tests/unit/`.
4. **Honest scope.** Modules and features are only documented here once they exist.
   See [ROADMAP.md](ROADMAP.md) for what's planned but not yet built.

## Geographic scope

Ten counties spanning the former Nyanza and Western provinces of Kenya:
Kisumu, Homa Bay, Migori, Siaya, Nyamira, Kisii, Kakamega, Vihiga, Busia, Bungoma.