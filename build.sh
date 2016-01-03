#!/bin/bash
NAME="mirall"
VERSION="1.6.2"
cp -rvf  *.spec ~/rpmbuild/SPECS/
if [ -d "$NAME-$VERSION" ]; then
   rm -rf "$NAME-$VERSION"
fi
cp -rf source $NAME-$VERSION
tar -cjf $NAME-$VERSION.tar.bz2 $NAME-$VERSION 
cp -rvf  *.tar.bz2  ~/rpmbuild/SOURCES/
#cp -rvf patches/origin/*  ~/rpmbuild/SOURCES/
#cp -rvf patches/cs2c/*  ~/rpmbuild/SOURCES/
rpmbuild -bs --nodeps owncloud-client.spec

