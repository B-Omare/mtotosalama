"""Tests for the GADM boundary loader."""

from pathlib import Path
import pytest
from mtotosalama.ingestion.boundaries import (
    get_target_counties,
    load_kenya_county_boundaries,
)

GADM_PATH = Path("data/raw/gadm41_KEN.gpkg")


def test_get_target_counties_returns_ten_counties():
    counties = get_target_counties()
    assert len(counties) == 10
    assert "Kisumu" in counties
    assert "Homa Bay" in counties


@pytest.mark.skipif(
    not GADM_PATH.exists(),
    reason="GADM file not present locally (gitignored raw data)",
)
def test_load_kenya_county_boundaries_returns_all_ten_counties():
    gdf = load_kenya_county_boundaries(GADM_PATH)
    assert len(gdf) == 10
    assert set(gdf["county_name"]) == set(get_target_counties())


def test_load_kenya_county_boundaries_raises_on_missing_file():
    with pytest.raises(FileNotFoundError):
        load_kenya_county_boundaries(Path("data/raw/nonexistent_file.gpkg"))