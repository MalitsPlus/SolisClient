#!/bin/bash

FLAG_FILE="cache/need_update.txt"
REPO_NAME="VenusSysLib"
REPO_SSH="git@github.com:MalitsPlus/VenusSysLib.git"

if [ ! -f ${FLAG_FILE} ]; then
  echo "No need to update venus. Exiting."
  exit 0
fi

# Check repo directory
if [ ! -d ${REPO_NAME} ]; then
  echo ">>> Cloning venus from remote..."
  git clone ${REPO_SSH}
  if [ $? -ne 0 ]; then
    echo ">>> Failed to clone venus."
    exit 1
  fi
fi

# Set git configurations
git -C ${REPO_NAME} config user.name "SolisClient"
git -C ${REPO_NAME} config user.email "anonymous@e.mail"

echo ">>> Pulling venus from remote..."
git -C ${REPO_NAME} pull --rebase

if [ $? -ne 0 ]; then
  echo ">>> Failed to pull venus."
  exit 1
fi

# Copy files to VenusSysLib and update package version
py_flag=`python update_venus_package.py`

if [ "${py_flag}" = "1" ]; then
  echo ">>> Failed to update venus package."
  exit 1
fi

echo ">>> git adding..."
git -C ${REPO_NAME} add .
echo ">>> git committing..."
git -C ${REPO_NAME} commit -m "feat: update databases"
echo ">>> Pushing to remote..."

ssh-add -D
ssh-add ~/.ssh/id_rsa_1215ff1d8f82d9e36c5ed9d719782b4d
GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/id_rsa_1215ff1d8f82d9e36c5ed9d719782b4d"
git config core.sshCommand "ssh -o IdentitiesOnly=yes -i ~/.ssh/id_rsa_1215ff1d8f82d9e36c5ed9d719782b4d"

git -C ${REPO_NAME} push

if [ $? -ne 0 ]; then
  echo ">>> Failed to push to remote."
  exit 1
fi

# Clean files
rm -f ${FLAG_FILE}
rm -rf "cache/update_master"

echo ">>> Done."
