"""Tests for the OpenStreetMap health facility loader."""

import pytest
from mtotosalama.ingestion.facilities import (
    get_target_counties,
    load_health_facilities_for_county,
)


def test_get_target_counties_returns_ten_counties():
    counties = get_target_counties()
    assert len(counties) == 10


@pytest.mark.network
def test_load_health_facilities_for_county_returns_data():
    gdf = load_health_facilities_for_county("Kisumu")
    assert len(gdf) > 0
    assert "county_name" in gdf.columns
    assert (gdf["county_name"] == "Kisumu").all()