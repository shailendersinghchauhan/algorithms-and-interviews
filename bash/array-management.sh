#!/usr/bin/env bash

array_example()
{
allThreads=(1 2 4 8 16 32 64 128)
allRuntimes=()
for t in ${allThreads[@]}; do
  runtime=$t
  allRuntimes+=( $runtime )
done

echo allruntimes

}

### Call Array example function
array_example