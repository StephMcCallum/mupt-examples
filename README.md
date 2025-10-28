# mupt-examples

Environment can be set up from accompanying [requirements file](reqs.yml) along with pip install of the [Multiscale Polymer Toolkit](https://github.com/MuPT-hub/mupt)

## System building examples (high-level):
0. [Simple peptide example](./examples_system/hierarchy_on_peptides.ipynb)
1. [Backmapped chain/melt building](./examples_system/ellipsoidal_chain_placement.ipynb)
2. [Parameterization, export, and MD simulations with OpenFF](./examples_system/mdfiles_with_openff.ipynb)

## MuPT Representation components tutorials (low-level):
0. ["Molecule from scratch" - bare basics](./examples_repr/mol_from_scratch_basic.ipynb)
1. ["Molecule from scratch" - advanced usage](./examples_repr/mol_from_scratch_advanced.ipynb)
2. [Molecule from SMILES/RDKit](./examples_repr/mupt_primitives_rdkit.ipynb)
3. [Rigid body shapes](./examples_repr/mupt_shapes.ipynb)
4. [Inter-body spatial alignment](./examples_repr/connector_alignment.ipynb)

## DPD notebooks:
The DPD notebooks are meant to demonstrate a system initialization workflow of polymer various systems and configuration routines. These configurations are relaxed using a HOOMD simulation with DPD forces. A list of the notebooks and their descriptions:
+ DPD_init.ipynb: initializes a polymer system using a random walk and relaxes the system using DPD forces.
+ DPD_init_ell.ipynb: initializes a random configuration of ellipsoid chains, based on the flowerMD ellipsoid model, and relaxes the system using DPD forces.
+ DPD_init_mbuild.ipynb: initializes a polymer system using an mbuild2.0 random walk and relaxes the system using DPD forces.

Environment for  DPD_init.ipynb can be installed with `dpd_environment.yml` or with:

```
conda create -n mupt-init -c conda-forge matplotlib scipy gsd freud hoomd fresnel jupyter
```

As of Aug 1 2025 DPD_init_ell.ipynb requires a developer install of [flowerMD](https://github.com/cmelab/flowermd)

As of Sep 25 2025 DPD_init_mbuild.ipynb requires a developer install of [mbuild](https://github.com/mosdef-hub/mbuild) `gh pr checkout 1261`

