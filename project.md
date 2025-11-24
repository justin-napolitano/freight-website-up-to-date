---
slug: github-freight-website-up-to-date
id: github-freight-website-up-to-date
title: freight-website-up-to-date
repo: justin-napolitano/freight-website-up-to-date
githubUrl: https://github.com/justin-napolitano/freight-website-up-to-date
generatedAt: '2025-11-24T21:34:47.849Z'
source: github-auto
summary: >-
  A data-driven documentation website focused on United States freight networks,
  including rail, shipping, intermodal freight, and natural gas infrastructure.
  This project integrates geospatial data, Jupyter Notebook analyses, and
  Sphinx-based documentation to provide a comprehensive overview and analysis of
  freight transportation.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: project
entryLayout: project
showInProjects: true
showInNotes: false
showInWriting: false
showInLogs: false
---

A data-driven documentation website focused on United States freight networks, including rail, shipping, intermodal freight, and natural gas infrastructure. This project integrates geospatial data, Jupyter Notebook analyses, and Sphinx-based documentation to provide a comprehensive overview and analysis of freight transportation.

---

## Features

- Interactive maps and analyses of freight transportation modes including rail, shipping, and intermodal facilities.
- Integration of geospatial data in GeoJSON format.
- Automated build and deployment scripts for generating and publishing HTML documentation.
- Backup functionality for documentation builds using Dropbox API.
- Sphinx-based documentation with support for notebooks (`myst_nb`), blogging (`ablog`), and bibliographic references.

## Tech Stack

- Python 3.5+ (with dependencies managed via `requirements.txt`)
- Jupyter Notebooks for data analysis and visualization
- Sphinx documentation generator with multiple extensions
- Bash scripts for deployment and automation
- Dropbox API for backup
- Geospatial libraries: GeoPandas, Folium, Contextily

## Getting Started

### Prerequisites

- Python 3.5 or higher
- `pip` package manager
- Dropbox account and API token (for backup functionality)
- `make` utility

### Installation

```bash
# Clone the repository
$ git clone https://github.com/justin-napolitano/freight-website-up-to-date.git
$ cd freight-website-up-to-date

# Install Python dependencies
$ pip install -r requirements.txt

# (Optional) For Rocky Linux or similar systems
$ pip install -r requirements_rocky.txt
```

### Build Documentation

```bash
# Clean previous builds
$ make clean

# Build HTML documentation
$ make html
```

### Deployment

```bash
# Deploy the built documentation to GitHub Pages
$ ./deploy.sh
```

### Backup

Edit `backup_html.py` to insert your Dropbox API token, then run:

```bash
$ python backup_html.py
```

## Project Structure

```
freight-website-up-to-date/
├── acp.sh                  # Auxiliary shell script
├── backup_html.py          # Script to backup built HTML to Dropbox
├── chtml.sh                # Auxiliary shell script
├── deploy.sh               # Deployment script to GitHub Pages
├── deployz.sh              # Alternative deployment script
├── doit.sh                 # Automation script
├── install.sh              # Installation script
├── label_list.py           # Script for reading and printing label data from pickle files
├── Makefile                # Build automation
├── pullit.sh               # Git pull helper script
├── pushit.sh               # Git push helper script
├── python_build.py         # Python build pipeline and dependency installer
├── requirements.txt        # Python dependencies
├── requirements_rocky.txt  # Dependencies for Rocky Linux
├── requirments.txt         # Possibly duplicate requirements file (typo)
├── source/                 # Sphinx documentation source files
│   ├── conf.py             # Sphinx configuration
│   ├── index.md            # Main documentation landing page
│   ├── parts/              # Documentation parts (freight, bibliography, etc.)
│   └── ...
├── todo/                   # Notes and TODOs
│   └── todo.md             # TODO list
└── uninstall.sh            # Uninstall script
```

## Future Work / Roadmap

- Consolidate and clean up duplicate or redundant requirement files.
- Enhance backup script to support incremental backups and error logging.
- Expand documentation with more detailed freight network analyses.
- Automate testing of build and deployment pipelines.
- Improve README with usage examples and screenshots.
- Integrate CI/CD for automated deployment on push.

