"""Validate archived OULAD primary results and reproduce panel diagnostics.

This script is intentionally not presented as a raw-data rerun. The current
archive contains a causal-uplift foundation in education_models at commit a49a36f,
but does not yet record the exact article configuration and command. The script
validates registered article output and reruns the panel bootstrap/LOO diagnostic.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
RESULTS = ROOT / "results"


def main() -> None:
    primary = json.loads((RESULTS / "oulad_primary.json").read_text(encoding="utf-8"))
    if primary["provenance"]["raw_pipeline_script"] is not None:
        raise RuntimeError("Update this runner to invoke the registered raw pipeline.")
    subprocess.run([sys.executable, str(ROOT / "panel_bootstrap_loo.py")], check=True)
    panel = json.loads((RESULTS / "panel_bootstrap_loo.json").read_text(encoding="utf-8"))
    assert round(panel["full"]["naive"]["ate"], 4) == round(primary["naive_calibration"]["ate"], 4)
    assert round(panel["full"]["sign_aware"]["ate"], 4) == round(primary["sign_aware_calibration"]["ate"], 4)
    print("Validated archived OULAD primary values and regenerated panel diagnostics.")
    print("Record the exact commit, configuration, and command for the article AIPW/Qini/E-value run before submission.")


if __name__ == "__main__":
    main()
