import importlib, os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.dirname(os.path.dirname(__file__))
DIST = os.path.join(ROOT, "dist")
PAGES = {"inventory": "p_inventory", "supply-chain": "p_supply", "business": "p_business", "business-ai": "p_business_ai", "cold-chain": "p_cold", "": "p_hub"}
shutil.rmtree(DIST, ignore_errors=True)
shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(DIST, "assets"))
for slug, mod in PAGES.items():
    try:
        m = importlib.import_module(mod)
    except ModuleNotFoundError:
        continue
    d = os.path.join(DIST, slug); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(m.build())
    print("built /" + slug)
