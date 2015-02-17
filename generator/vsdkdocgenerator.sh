#!/bin/sh

version=$1
rm -rf ./codegen/$version/doc
cp -Rf ./src/doc ./codegen/$version/
sphinx-apidoc -o codegen/$version/doc codegen/$version
cd codegen/$version/doc
make html
