#!/bin/bash

py.test --nbval-lax --current-env -vv \
    multiscale_chain_placement.ipynb \
    hierarchy_on_peptides.ipynb \
    mdfiles_with_openff.ipynb