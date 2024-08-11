from datetime import datetime


extensions = []
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = "Insegel"

exclude_patterns = ["_build"]

html_theme = "insegel"

html_last_updated_fmt = "%d %b %Y"

releases_github_path = "autophagy/insegel"
# Our pre-0.x releases are unstable / mix bugs+features
releases_unstable_prehistory = True

extensions = ["sphinx.ext.autodoc"]

html_theme_options = {"navigation_depth": 2, "local_toc": True}

html_logo = "_static/logo.svg"

html_last_updated_fmt = None
