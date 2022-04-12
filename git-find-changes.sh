#!/bin/bash

function unstaged_changes() {
    worktree=${1%/*};
    git --git-dir="$1" --work-tree="$worktree" diff-files --quiet --ignore-submodules --
}

function uncommited_changes() {
    worktree=${1%/*};
    git --git-dir="$1" --work-tree="$worktree" diff-index --cached --quiet HEAD --ignore-submodules --
}

function git-find-changes() {
    for gitdir in `find . -name .git`;
    do
        worktree=${gitdir%/*};
        if ! unstaged_changes $gitdir
        then
            echo "unstaged     $gitdir"
        fi

        if ! uncommited_changes $gitdir
        then
            echo "uncommitted  $gitdir"
        fi
    done
}

git-find-changes
