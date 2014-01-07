#!/bin/bash
# Author: Wonder
# Description:
# Usage: 部署到sae

#专门为部署到sae建的仓库
REPO_FOR_SAE=../ezlog.sae
DEPLOY_TO_SAE_VERSION=1

if [ ! -d "$REPO_FOR_SAE" ]; then
    mkdir -p "$REPO_FOR_SAE"
    git svn clone https://svn.sinaapp.com/ezlog/ "$REPO_FOR_SAE"
fi;

pwd=$PWD

rsync -rlcv --exclude-from="./deploy-exclude.txt" ./ ${REPO_FOR_SAE}/${DEPLOY_TO_SAE_VERSION}/

cd $REPO_FOR_SAE
    git svn rebase
    git add .
    git commit -m "auto commit `date`"
    git svn dcommit
cd $pwd
