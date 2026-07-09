"""
Loader for Kenya administrative boundary data (GADM).

Downloads county-level administrative boundaries and filters to the
project's ten-county geographic scope (former Nyanza and Western provinces).
"""

from pathlib import Path
import geopandas as gpd
import yaml

CONFIG_PATH = Path(__file__).resolve().parents[3] / "configs" / "data_sources.yaml"
RAW_DATA_DIR = Path(__file__).resolve().parents[3] / "data" / "raw"


def load_config() -> dict:
    """Load the project data source configuration."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_target_counties() -> list[str]:
    """Return the list of ten target counties from config."""
    config = load_config()
    return config["geographic_scope"]["counties"]


def load_kenya_county_boundaries(gadm_gpkg_path: Path) -> gpd.GeoDataFrame:
    """
    Load Kenya county boundaries from a local GADM GeoPackage file and
    filter to the project's ten target counties.

    Parameters
    ----------
    gadm_gpkg_path : Path
        Path to a locally downloaded GADM Kenya GeoPackage
        (gadm41_KEN.gpkg), layer ADM_ADM_1.

    Returns
    -------
    gpd.GeoDataFrame
        Filtered to the ten target counties, with county name column
        standardised to 'county_name'.
    """
    if not gadm_gpkg_path.exists():
        raise FileNotFoundError(
            f"GADM file not found at {gadm_gpkg_path}. "
            "Download it manually from the URL in configs/data_sources.yaml "
            "and place it in data/raw/."
        )

    gdf = gpd.read_file(gadm_gpkg_path, layer="ADM_ADM_1")
    gdf = gdf.rename(columns={"NAME_1": "county_name"})

    target_counties = get_target_counties()
    filtered = gdf[gdf["county_name"].isin(target_counties)].copy()

    return filtered.reset_index(drop=True)