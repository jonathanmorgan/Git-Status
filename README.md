# Git-Status

A collection of scripts to help manage folders that contain many git repos.

Also check out: https://github.com/fboender/multi-git-status

## copy-scripts-to.sh

This script copies the other scripts in this folder to a directory whose path you specify as the first parameter when you invoke the script, and sets their permissions so the owner can read and run them. By default, they are not allowed to be written, to make it less likely I will accidentally update them outside the repo and lose changes. Feel free to update permissons once they are copied.

This script assumes you are running it in the folder you checked out, alongside the other scripts here.

Example:

    # copy scripts to parent folder
    ./copy-scripts-to.sh ..

## git-find-changes.sh

copy to the folder that holds many git repos, then run the script. It will use `diff-files` and `diff-index` git commands to look for changes not yet staged or committed and output any repos that have changes.

## git-multi-status.sh

copy to the folder that holds many git repos, then run the script. It will use `status` git command to look for repos with the following states:

- `[Untracked]` - status output contains the string 'Untracked'
- `[Modified]` - status output contains the string 'Changes not staged for commit'
- `[Staged]` - status output contains the string 'Changes to be committed'
- `[Unpushed]` - status output contains the string 'Your branch is ahead'
- `[Unmerged]` - status output contains the string 'Your branch is behind'

By default, will scan the current folder. You can also pass one or more file system paths as arguments, separated by spaces, that you want it to scan instead of current folder.

## show_status.py

- originally from: https://github.com/MikePearce/Git-Status

--- Get Status ---
Ever wanted to get the status of repos in multiple sub directories? Yeah, me
too. So I knocked this up.

-- Installation --
Copy the file to /usr/bin (or the folder where you want to run it)

    %> cp show_status.py /usr/bin (or /usr/sbin)

Give it execute permissions

    %> chmod +x /usr/bin/show_status.py

-- Usage --

Usage: python ./show_status.py [options]

Show Status is awesome. If you tell it a directory to look in, it'll scan
through all the sub dirs looking for a .git directory. When it finds one it'll
look to see if there are any changes and let you know. It can also push and
pull to/from a remote location (like github.com) (but only if there are no
changes.) Contact jonathan.morgan.007@gmail.com for any support.

Options:

    -h, --help                  show this help message and exit
    -d DIRNAME, --dir=DIRNAME   The directory to parse sub dirs from
    -v, --verbose               Show the full detail of git status
    -r REMOTE, --remote=REMOTE  Push to the master (remotename:branchname)
    -p PULL, --pull=PULL        Pull from the master (remotename:branchname)

-- Warranties/Guarantees --

None, you're on your own. If you'd like some help, mail me on jonathan.morgan.007@gmail.com
