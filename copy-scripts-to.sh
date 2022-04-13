#!/bin/bash

my_directory_path="$(dirname "$0")"
#echo "my folder: ${my_directory_path}"

directory_path_in="$1"
to_directory_path=
file_name=
permissions=

echo ""

# do we have a path?
if [[ -n "${directory_path_in}" ]]
then

    # store in directory path
    to_directory_path="${directory_path_in}"

    # does directory already exist?
    if [ -d "$to_directory_path" ]
    then

        # exists - copy files and set permissions.
        echo "Copying git scripts to directory '${to_directory_path}':"

        # ==> git-find-changes.sh
        file_name="git-find-changes.sh"
        permissions="500"
        echo "- Copying ${file_name}, setting permissions to ${permissions}."
        cp "${my_directory_path}/${file_name}" "${to_directory_path}/"
        chmod ${permissions} "${to_directory_path}/${file_name}"

        # ==> git-multi-status.sh
        file_name="git-multi-status.sh"
        permissions="500"
        echo "- Copying ${file_name}, setting permissions to ${permissions}."
        cp "${my_directory_path}/${file_name}" "${to_directory_path}/"
        chmod ${permissions} "${to_directory_path}/${file_name}"

        # ==> show_status.py
        file_name="show_status.py"
        permissions="400"
        echo "- Copying ${file_name}, setting permissions to ${permissions} (to run: python ./${file_name})."
        cp "${my_directory_path}/${file_name}" "${to_directory_path}/"
        chmod ${permissions} "${to_directory_path}/${file_name}"

    else

        # Does not exist - create with default user and group.
        echo "==> Directory '${to_directory_path}' does not exist. Please copy to a folder that already exists."

    fi

else

    # no path - error.
    my_error_message="==> No directory specified to copy into. Please provide the path where you want the scripts to be copied."
    echo "${my_error_message}"

fi #-- END check to see if directory path passed in. --#

echo ""
