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

# install pdf creation plugin
There are a few packages available such as mkdocs-with-pdf
On Windows, both give the error:
```
```cannot load library 'gobject-2.0-0': error 0x7e.  Additionally, ctypes.util.find_library() did not manage to locate a library called 'gobject-2.0-0'```


```

## Notes

Now using frictionless so submission procedures will center around using this.


1. Submission procedures
    - overall updated submission procedures
    - data dictionaries from schemas

2. 
    - Diagram of how JDC works
    - link to JDC graph model

Also a work in progress: creating metadata documentation extracted from JDC and most up to date JDC Core Baseline Measures document. Goal here is to make all properties/nodes searchable through documentation. 

