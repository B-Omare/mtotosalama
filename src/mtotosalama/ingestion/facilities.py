"""
Loader for health facility locations from OpenStreetMap.

Queries OSM for amenity=hospital, amenity=clinic, and amenity=doctors
tags within each of the project's ten target counties.
"""

from pathlib import Path
import geopandas as gpd
import osmnx as ox
import yaml

CONFIG_PATH = Path(__file__).resolve().parents[3] / "configs" / "data_sources.yaml"

HEALTH_FACILITY_TAGS = {
    "amenity": ["hospital", "clinic", "doctors", "pharmacy"],
    "healthcare": True,
}


def load_config() -> dict:
    """Load the project data source configuration."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_target_counties() -> list[str]:
    """Return the list of ten target counties from config."""
    config = load_config()
    return config["geographic_scope"]["counties"]


def load_health_facilities_for_county(county_name: str) -> gpd.GeoDataFrame:
    """
    Query OpenStreetMap for health facility locations within a single
    Kenyan county.

    Parameters
    ----------
    county_name : str
        County name, e.g. "Kisumu". Must be one of the project's ten
        target counties.

    Returns
    -------
    gpd.GeoDataFrame
        Health facility points with OSM tags, plus a 'county_name' column.
    """
    place_query = f"{county_name} County, Kenya"
    gdf = ox.features_from_place(place_query, tags=HEALTH_FACILITY_TAGS)
    gdf = gdf.reset_index()
    gdf["county_name"] = county_name
    return gdf


def load_health_facilities_all_counties() -> gpd.GeoDataFrame:
    """
    Query OpenStreetMap for health facility locations across all ten
    target counties and combine into a single GeoDataFrame.

    Returns
    -------
    gpd.GeoDataFrame
        Combined health facility points for all ten counties.
    """
    import pandas as pd

    counties = get_target_counties()
    all_facilities = []

    for county in counties:
        try:
            county_gdf = load_health_facilities_for_county(county)
            all_facilities.append(county_gdf)
        except Exception as e:
            print(f"Warning: failed to load facilities for {county}: {e}")

    combined = pd.concat(all_facilities, ignore_index=True)
    return gpd.GeoDataFrame(combined)