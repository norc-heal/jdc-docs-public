# JDC Documentation

This repository makes the documentation for the 
JCOIN data commons using mkdocs and related plugins.

Install python (tested with 3.9) ideally in a virtual environment

## Set up
```python

# To install mkdocs and the 
# mermaid plugin for diagram creation:
pip install mkdocs
pip install mkdocs-mermaid2-plugin

# install packages from documetnation creation
pip install gen3
pip install pandas #or conda install pandas if using conda

# jsonpath expressions for simplifying work with gen3 API
pip install jsonpath_ng
```

## Notes


Here is a list of things to add/edit for v1:

1. Node property tables
    - filter out irrelevant variables other than systemProperties variables
    - if string,integer, or number type -- can be any of that type so add "Any " to the column (eg string --> Any string)
    - create additional description for parent node properties or note at top

2. Overview of JDC data model/nodes/properties
    - Diagram of how JDC works
    - link to JDC graph model

Also a work in progress: creating metadata documentation extracted from JDC and most up to date JDC Core Baseline Measures document. Goal here is to make all properties/nodes searchable through documentation. 

