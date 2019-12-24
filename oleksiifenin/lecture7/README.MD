Currently the design of the Git index (staging area) only permits files to be listed, and nobody competent enough to make the change to allow empty directories has cared enough about this situation to remedy it.

Directories are added automatically when adding files inside them. That is, directories never have to be added to the repository, and are not tracked on their own.

You can say "git add <dir>" and it will add the files in there.

If you really need a directory to exist in checkouts you should create a file in it. .gitignore works well for this purpose (there is also a tool MarkEmptyDirs using the .NET framework which allows you to automate this task); you can leave it empty or fill in the names of files you do not expect to show up in the directory.

https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F
