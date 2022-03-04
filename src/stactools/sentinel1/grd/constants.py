import pystac
from pystac import ProviderRole
from pystac.extensions.eo import Band
from pystac.link import Link
from pystac.utils import str_to_datetime
from pystac.extensions import sar

INSPIRE_METADATA_ASSET_KEY = "inspire-metadata"
SAFE_MANIFEST_ASSET_KEY = "safe-manifest"
PRODUCT_METADATA_ASSET_KEY = "product-metadata"

SENTINEL_LICENSE = Link(
    rel="license",
    target="https://sentinel.esa.int/documents/" + "247904/690755/Sentinel_Data_Legal_Notice",
)

ACQUISITION_MODES = [
    "Stripmap (SM)",
    "Interferometric Wide Swath (IW)",
    "Extra Wide Swath (EW)",
    "Wave (WV)",
]
SENTINEL_CONSTELLATION = "Sentinel-1"

SENTINEL_PROVIDER = pystac.Provider(
    name="ESA",
    roles=[
        ProviderRole.PRODUCER,
        ProviderRole.PROCESSOR,
        ProviderRole.LICENSOR,
    ],
    url="https://earth.esa.int/web/guest/home",
)

SENTINEL_POLARISATIONS = {
    "vh": Band.create(
        name="VH",
        description="VH band: vertical transmit and horizontal receive",
    ),
    "hh": Band.create(
        name="HH",
        description="HH band: horizontal transmit and horizontal receive",
    ),
    "hv": Band.create(
        name="HV",
        description="HV band: horizontal transmit and vertical receive",
    ),
    "vv": Band.create(
        name="VV",
        description="VV band: vertical transmit and vertical receive",
    ),
}

COLLECTION_ID = "sentinel1-grd"

# https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1  # noqa
DESCRIPTION = (
    "Level-1 Ground Range Detected (GRD) products consist of focused SAR data that has"
    " been detected, multi-looked and projected to ground range using the Earth"
    " ellipsoid model WGS84. The ellipsoid projection of the GRD products is corrected"
    " using the terrain height specified in the product general annotation. The terrain"
    " height used varies in azimuth but is constant in range (but can be different for"
    " each IW/EW sub-swath). Ground range coordinates are the slant range coordinates"
    " projected onto the ellipsoid of the Earth. Pixel values represent detected"
    " amplitude. Phase information is lost. The resulting product has approximately"
    " square resolution pixels and square pixel spacing with reduced speckle at a cost"
    " of reduced spatial resolution. For the IW and EW GRD products, multi-looking is"
    " performed on each burst individually. All bursts in all sub-swaths are then"
    " seamlessly merged to form a single, contiguous, ground range, detected image per"
    " polarisation."
)


BOUNDING_BOX = [-180.0, -90.0, 180.0, 90.0]
TEMPORAL_EXTENT = [str_to_datetime("2014-10-03T00:00:00Z"), None]

EXTENT = pystac.Extent(
    pystac.SpatialExtent([BOUNDING_BOX]),
    pystac.TemporalExtent([TEMPORAL_EXTENT]),
)

TITLE = "Sentinel-1 SAR L1 GRD"


SENTINEL_INSTRUMENTS = ["c-sar"]
SENTINEL_CONSTELLATION = "sentinel-1"
SENTINEL_PLATFORMS = ["sentinel-1a", "sentinel-1b"]
SENTINEL_CENTER_FREQUENCY = 5.405
SENTINEL_OBSERVATION_DIRECTION = sar.ObservationDirection.RIGHT
