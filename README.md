# MtotoSalama

![Tests](https://github.com/B-Omare/mtotosalama/actions/workflows/tests.yml/badge.svg)

**A quantum-enhanced causal AI system for under-five mortality prediction and prevention in the Lake Victoria Basin**

*Mtoto Salama = "Safe Child" in Swahili*

## Overview

MtotoSalama is an open-science research software project prototyping an early-warning
and intervention-prioritisation system for under-five mortality across the ten counties
of the former Nyanza and Western provinces of Kenya — Kisumu, Homa Bay, Migori, Siaya,
Nyamira, Kisii, Kakamega, Vihiga, Busia, and Bungoma — a coherent regional bloc spanning
the Lake Victoria basin and western highlands. It combines data engineering,
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

## Geographic scope

Ten counties, former Nyanza and Western provinces:

| Sub-region | Counties |
|---|---|
| Former Nyanza | Kisumu, Homa Bay, Migori, Siaya, Nyamira, Kisii |
| Former Western | Kakamega, Vihiga, Busia, Bungoma |

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
