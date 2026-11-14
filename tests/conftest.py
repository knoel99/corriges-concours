"""Rend les modules de scripts/exporter importables par les tests (`import pur`)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "exporter"))
