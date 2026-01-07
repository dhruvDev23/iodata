"""Test that the example scripts run without errors."""

import os
import subprocess
import sys
from pathlib import Path

import pytest


def find_example_scripts():
    folder = Path(__file__).parent

    scripts = []
    for file in folder.glob("*.py"):
        if file.name.startswith("test_"):
            continue
        scripts.append(file)

    return scripts


@pytest.mark.parametrize("script_file", find_example_scripts())
def test_example_script_runs(script_file: Path):
    env = os.environ.copy()
    project_root = Path(__file__).resolve().parents[2]
    existing_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{project_root}:{existing_pythonpath}"
    subprocess.run([sys.executable, script_file.name], cwd=script_file.parent, env=env, check=True)
