# Setup

## Prerequisites

- Python 3.11 (project developed and tested on 3.11; not guaranteed on other versions)
- Git

## Getting started

1. Clone the repository:
```bash
   git clone https://github.com/B-Omare/mtotosalama.git
   cd mtotosalama
```

2. Create and activate a virtual environment (Windows PowerShell shown; adjust for
   macOS/Linux):
```powershell
   py -3.11 -m venv venv
   .\venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. (Optional) Register the Jupyter kernel for notebook work:
```bash
   python -m ipykernel install --user --name=mtotosalama --display-name "Python (mtotosalama)"
```

5. Run the test suite to confirm everything is working:
```bash
   pytest
```

## Data

Raw data is not committed to this repository (see [ARCHITECTURE.md](ARCHITECTURE.md)
for why). To populate `data/`, run the ingestion pipeline once it is available
(tracked in [ROADMAP.md](ROADMAP.md)). Until then, `data/` will remain empty aside
from `.gitkeep` placeholders.

## Environment variables

Some data sources (planned) require API keys. These are never committed. Copy
`.env.example` to `.env` and fill in your own keys once that file exists.