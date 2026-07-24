#! /bin/sh

## To be used for curl -fsSL https://install.amlal.nekernel.org | sh

echo "==> PUB: DOWNLOADING REPOSITORY..."

ORG=publications-org
PROFILE=pub-release

SRC=pub
VCS=git
FLAGS=clone --recurse-submodules -j8
DIST=src-${ORG}-${PROFILE}

mkdir ${DIST}

${GIT} ${FLAGS} https://github.com/publications-org/${SRC}.git ${DIST}/${SRC}
