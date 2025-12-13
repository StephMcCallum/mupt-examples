#!/bin/bash

example_dirs=(
    # 'examples_DPD' # TODO: automate notebook tests for DPD examples
    'examples_repr'
    'examples_system'
)
batch_status="passing"

for dirname in "${example_dirs[@]}"; do
    pushd "./$dirname"
    bash "./notebook_tests.sh" || batch_status="failing"
    popd
done

if [ $batch_status = "failing" ]; then
    exit 1 # bubble up failure to CI if any of batches fail
fi