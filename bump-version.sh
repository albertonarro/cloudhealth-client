#!/bin/bash

VERSION=$1
SEMVER_REGEX="^[vV]?(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)\\.(0|[1-9][0-9]*)(\\-[0-9A-Za-z-]+(\\.[0-9A-Za-z-]+)*)?(\\+[0-9A-Za-z-]+(\\.[0-9A-Za-z-]+)*)?$"

if [ -z "$VERSION" ]
then
    VERSION=$(git flow release list | grep '*' | awk '{print $2}') 
fi

if [[ "$VERSION" =~ $SEMVER_REGEX ]]
then
    sed -i "s/version = .*/version = $VERSION/g" setup.cfg
    echo Files modified successfully, version bumped to $VERSION
else
    echo 'Tag must match the semver scheme X.Y.Z[-PRERELEASE][+BUILD]. See https://semver.org/'
fi
