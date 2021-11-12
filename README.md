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


```

## Notes

As a proof of concept, all markdown files were created/copied at one point in time. However, ultimately, files and data from external sources (e.g., metadata in the JDC or OEPS documentation) will be programmatically extracted from source.

Also a work in progress: creating metadata documentation extracted from JDC and most up to date JDC Core Baseline Measures document. Goal here is to make all properties/nodes searchable through documentation. 

