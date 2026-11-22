import os

# ============================================================
# Project Configuration
# ============================================================

# ------------------------------------------------------------
# Project Information
# ------------------------------------------------------------

APP_NAME = "AI Investment Research Platform"
VERSION = "0.1.0"

# ------------------------------------------------------------
# Folder Locations
# ------------------------------------------------------------

APP_FOLDER = "app"
DATA_FOLDER = "data"
LOG_FOLDER = "logs"

WATCHLIST_FILE = "data/watchlist.json"
SCORES_FOLDER = "data/scores"
DASHBOARD_FILE = "app/dashboard_data.json"

# ------------------------------------------------------------
# Investment Universe Filters
# ------------------------------------------------------------

EXCLUDED_SECTORS = [
    "financial services"
]

EXCLUDED_INDUSTRIES = [
    "airline",
    "airlines",
    "department store",
    "department stores",
    "regional bank",
    "bank",
    "insurance"
]

# ------------------------------------------------------------
# SEC EDGAR
# ------------------------------------------------------------

# SEC requires every request to carry a real contact email in its User-Agent header
# and may block requests without one. Set your own address in the environment
# variable SEC_CONTACT_EMAIL; it is deliberately not stored in this public repository.
SEC_CONTACT_EMAIL = os.environ.get("SEC_CONTACT_EMAIL", "").strip()
