#!/usr/bin/env python
"""Initialize the project's data space.

Iterates over all defined state points and initializes
the associated job workspace directories.
The result of running this file is the creation of a signac workspace:
    - signac.rc file containing the project name
    - signac_statepoints.json summary for the entire workspace
    - workspace/ directory that contains a sub-directory of every individual statepoint
    - signac_statepoints.json within each individual statepoint sub-directory.

"""

import signac
import flow
import logging
from collections import OrderedDict
from itertools import product


def get_parameters():
    ''''''
    parameters = OrderedDict()
    parameters["num_pol"] = [100,200,500,800,1000]
    parameters["num_mon"] = [100]
    parameters["density"] = [0.85]
    parameters["k"]=[20000,25000]
    parameters["bond_l"]=[1.0]
    parameters["r_cut"]=[1.12,1.15,1.2]
    parameters["kT"]=[1.0]
    parameters["A"]=[1000,5000]
    parameters["gamma"]=[800,1000]
    parameters["dt"]=[0.001]
    parameters["particle_spacing"]=[1.1]

    return list(parameters.keys()), list(product(*parameters.values()))


def main():
    project = signac.init_project()
    param_names, param_combinations = get_parameters()
    # Create workspace of jobs
    for params in param_combinations:
        statepoint = dict(zip(param_names, params))
        job = project.open_job(statepoint)
        job.init()
        job.doc.setdefault("sampled", False)
        job.doc.setdefault("runs", 0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
