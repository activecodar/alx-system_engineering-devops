## Shell permissions

|File    | What it does|
|--------|-------------|
|0-iam_betty | switches the current user to the user betty|
|1-who_am_i| prints the effective username of the current user|
|2-groups| prints all the groups the current user is part of|
|3-new_owner| changes the owner of the file hello to the user betty|
|4-empty| creates an empty file called hello|
|5-execute| adds execute permission to the owner of the file hello|
|6-multiple_permissions| adds execute permission to the owner and the group owner, and read permission to other users, to the file hello|
|7-everybody|adds execution permission to the owner, the group owner and the other users, to the file hello|
|8-James_Bond| Add permissions for otherr users other than group and owner|
|9-John_Doe| Add all rwx permission to owner rx to group and wx to others|
|10-mirror_permissions| sets the permission mode of a file using that of another|
|11-directories_permissions| sets execute permissions to all subdirectories in the current folder|
|12-directory_permissions| create a dir and set its mode at the same time|
|13-change_group| changes the group ownership of a provided file|
|100-change_owner_and_group| change ownership of folders and files setting an owner and group together|
|101-symbolic_link_permissions| changes the ownership and group ownership of a symbolic link|
|102-if_only| change ownership of a file only when the current owner is specified|
|103-Star_Wars| prints star wars episode iv on the terminal|
