import importlib.util
import os
import sys

def load_generate_sitemap():
    script_path = os.path.join(
        os.path.dirname(__file__), "..", "scripts", "generate-sitemap.py"
    )
    spec = importlib.util.spec_from_file_location("generate_sitemap", script_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
