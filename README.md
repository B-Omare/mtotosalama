# MtotoSalama

**A quantum-enhanced causal AI system for under-five mortality prediction and prevention in the Lake Victoria Basin**

*Mtoto Salama = "Safe Child" in Swahili*

## Overview

MtotoSalama is an open-science research software project prototyping an early-warning
and intervention-prioritisation system for under-five mortality in Western Kenya
(Siaya, Kisumu, Homa Bay, Migori, Kakamega counties). It combines data engineering,
causal inference, Bayesian survival modelling, and machine learning to explore how
routinely collected health, climate, and satellite data could support community
health worker (CHW) decision-making.

This repository is developed incrementally and transparently: each deliverable is
either **fully implemented** or explicitly marked as **planned**, with no
overstated claims of completeness.

## Data sources

| Source | Status | Notes |
|---|---|---|
| Kenya DHIS2 | Public | Facility-level morbidity, vaccination data |
| KDHS 2022 | Public | National household health survey |
| ERA5 Climate Reanalysis | Public | Rainfall, temperature, humidity |
| Sentinel-2 Satellite | Public | Land use, water proximity, NDVI |
| OpenStreetMap / GADM | Public | Roads, facility locations, boundaries |
| Siaya HDSS (KEMRI/CDC) | Restricted | Requires research agreement — not used; synthetic data substituted where structurally needed |
| CHAMPS Network Kenya | Restricted | Requires data portal access — not used; synthetic data substituted where structurally needed |

## Project status

🚧 **Active development.** See [ROADMAP.md](docs/ROADMAP.md) for what's built vs. planned.

## Repository structure

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Setup

See [docs/SETUP.md](docs/SETUP.md).

## License

See [LICENSE](LICENSE).

## Author

Brian Omare