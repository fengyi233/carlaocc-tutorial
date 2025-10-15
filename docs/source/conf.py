# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_context = {
    "display_github": True,               # 告诉RTD显示GitHub按钮
    "github_user": "fengyi233",           # 你的GitHub用户名
    "github_repo": "carlaocc-tutorial",    # 仓库名
    "github_version": "main",             # 分支名（比如 main 或 master）
    "conf_py_path": "/docs/source/",      # conf.py 所在路径（相对于仓库根目录）
    "edit_link": True                     # 可选，用于某些主题兼容
}

html_theme_options = {
    "display_version": True,
    "vcs_pageview_mode": "edit",   # 🟢 将 view 改为 edit！
}