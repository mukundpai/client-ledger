import json
import os

def get_manifest():
    manifest_path = os.path.join('static', 'asset-manifest.json')
    with open(manifest_path) as f:
        return json.load(f)