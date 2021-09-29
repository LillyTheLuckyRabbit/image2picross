#!/bin/sh

wget http://web.eecs.utk.edu/~jplank/plank/jgraph/2017-11-28-Jgraph.tar
tar -xvf 2017-11-28-Jgraph.tar
rm 2017-11-28-Jgraph.tar
mv jgraph jgraph-src
cd jgraph-src
make
mv jgraph ..
cd ..
rm -rf jgraph-src