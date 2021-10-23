#!/bin/bash

base=$(dirname $(readlink -f $0))

if [[ -d "$base/src/build" ]]
then
    echo "cleaning source directory"
    rm -rf $base/src/build/*
fi

if [[ -d "$base/tests/build" ]]
then
    echo "cleaning tests directory"
    rm -rf $base/tests/build/*
fi

if [[ -d "$base/build" ]]
then
    echo "cleaning project build directory"
    rm -rf $base/build/*
fi

if [[ -n "$(ls -A $base/lib)" ]]
then
    echo "emptying lib directory"
    rm $base/lib/*
fi

if [[ -n "$(ls -A $base/bin)" ]]
then
    echo "emptying bin directory"
    rm $base/bin/*
fi
