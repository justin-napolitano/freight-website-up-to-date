---
slug: github-freight-website-up-to-date-note-technical-overview
id: github-freight-website-up-to-date-note-technical-overview
title: freight-website-up-to-date
repo: justin-napolitano/freight-website-up-to-date
githubUrl: https://github.com/justin-napolitano/freight-website-up-to-date
generatedAt: '2025-11-24T18:36:22.376Z'
source: github-auto
summary: >-
  This repo provides a data-driven documentation site for U.S. freight networks,
  covering rail, shipping, intermodal, and natural gas infrastructures. It
  combines geospatial data with Jupyter analyses and Sphinx documentation.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repo provides a data-driven documentation site for U.S. freight networks, covering rail, shipping, intermodal, and natural gas infrastructures. It combines geospatial data with Jupyter analyses and Sphinx documentation.

## Key Components

- Uses Python 3.5+, Jupyter Notebooks, and Sphinx for documentation.
- Interactive maps using GeoJSON.
- Automated deployment scripts and backup functionality via Dropbox API.

## Getting Started

1. **Clone the repo:**

    ```bash
    git clone https://github.com/justin-napolitano/freight-website-up-to-date.git
    cd freight-website-up-to-date
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Build and deploy documentation:**

    ```bash
    make clean
    make html
    ./deploy.sh
    ```

## Gotchas

- Make sure you have a Dropbox API token for backups.
- Check for typos in requirements files (e.g., `requirments.txt`).
