#!/bin/bash

example_dirs=(
    # 'examples_DPD' # TODO: automate notebook tests for DPD examples
    'examples_repr'
    'examples_system'
)
for dirname in "${example_dirs[@]}"; do
    pushd "./$dirname"
    # echo "$PWD"
    bash "./notebook_tests.sh"
    popd
done