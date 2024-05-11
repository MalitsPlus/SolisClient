#!/bin/bash
set -euo pipefail

# init
REPO_NAME="ipr-master-diff"
ARTIFACT_DIR_NAME="masterdata"
VERSION_FILE='!version.txt'
REPO_SSH="git@github.com:Stilamcat/ipr-master-diff.git"
SSH_KEY_PATH=$1
FLAG_FILE="cache/need_update.txt"

# Check repo directory
if [ ! -d ${REPO_NAME} ]; then
  echo ">>> Cloning repo from remote..."
  git clone --depth 1 ${REPO_SSH}
  if [ $? -ne 0 ]; then
    echo ">>> Failed to clone repo."
    exit 1
  fi
fi

# Set git configurations
git -C ${REPO_NAME} config user.name "anonymous"
git -C ${REPO_NAME} config user.email "anonymous@e.mail"
git -C ${REPO_NAME} config core.sshCommand "ssh -o IdentitiesOnly=yes -o StrictHostKeyChecking=no -i $SSH_KEY_PATH -F /dev/null"

# Get master version
pre_ver=`cat ${REPO_NAME}/${VERSION_FILE}`
if [ -f ${VERSION_FILE} ]; then
  cur_ver=`cat ${ARTIFACT_DIR_NAME}/${VERSION_FILE}`
else
  cur_ver='0'
fi

# Exit if no changing
echo ">>> Previous version: ${pre_ver}"
echo ">>> Current version:  ${cur_ver}"
if [ "${pre_ver}" = "${cur_ver}" ]; then
  if [ ! -f ${FLAG_FILE} ]; then
    echo "No need to update. Exiting."
    exit 0
  fi
fi

echo ">>> Pulling from remote..."
git -C ${REPO_NAME} pull --rebase

if [ $? -ne 0 ]; then
  echo ">>> Failed to pull repo."
  exit 1
fi

# Check remote version
rmt_ver=`cat ${REPO_NAME}/${VERSION_FILE}`
echo ">>> Remote version:   ${rmt_ver}"
if [ "${rmt_ver}" = "${cur_ver}" ]; then
  if [ ! -f ${FLAG_FILE} ]; then
    echo "No need to update. Exiting."
    exit 0
  fi
fi

echo ">>> Copy artifacts to repo."
for file in masterdata/*; do
  cp ${file} "${REPO_NAME}/${file##*/}"
done

echo ">>> git adding..."
git -C ${REPO_NAME} add .
echo ">>> git committing..."
git -C ${REPO_NAME} commit -m "${cur_ver}"
echo ">>> Pushing to remote..."
git -C ${REPO_NAME} push

if [ $? -ne 0 ]; then
  echo ">>> Failed to push to remote."
  exit 1
fi

echo ">>> Pushing to remote repository completed."
