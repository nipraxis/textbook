# Glossary

:::{glossary}
PATH

: The list of directories in which your system will look for programs to
  execute.  See [PATH].  When you type a command such as `ls` at the
  terminal prompt, this will cause your {term}`shell` to look for an
  {term}`executable` file called `ls` in a list of directories.  The
  list of directories is called the system PATH.  Specifically these
  directories are listed in the value of an {term}`environment variable`
  called `PATH`. Assuming you are using the default Unix `bash`
  shell, you can see these directories by typing:

  ```bash
  echo $PATH
  ```

  at the terminal prompt, followed by the return key. This might give
  you output like this:

  ```bash
  /usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin
  ```

  The shell will search this list of directories in order for an
  executable file called `ls`: first `/usr/bin`, then `/bin`, and
  so on.  We can ask to see the full path of the program that the system
  finds with the `which` command:

  ```bash
  $ which ls
  /bin/ls
  ```

  This tells us that the system did not find a `ls` executable file in
  `/usr/bin`, but did find one in `/bin`, for a full path of
  `/bin/ls`.

shell

: A shell is a program that gives access to the computer operating
  system.  It is usually a "command line interface" program that runs in
  a terminal, accepting strings that the user types at the keyboard.
  The shell program interprets the string and executes commands.  The
  most common default shell program is `bash` {{ -- }} for Bourne-Again
  SHell, so-called because it is an expanded variant of an older shell
  program, called the Bourne shell.  For example, when you open a
  default terminal application, such as `Terminal.app` in OSX or
  `gnome-terminal` in Linux, you will usually see a prompt at which
  you can type.  When you type, the program displaying the characters
  and interpreting them is the *shell*.  When you press return at the
  end of a line, the shell takes the completed line, and tries to
  interpret it as a command.  See also {term}`PATH`.

environment variable

: An environment variable is a key, value pair that is stored in
  computer memory and available to other programs running in the same
  environment.  For example the `PATH` environment variable, is a key,
  value pair where the key is `PATH` and the value is a list of
  directories, such as `/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin`.
  In particular, the shell uses the value of the `PATH` environment
  variable as a list of directories to search for executable programs.

executable

: A file is *executable* if the file is correctly set up to execute as a
  program.  On Unix systems, an executable file has to have special
  {term}`file permissions` that label the file as being suitable for
  execution.

file permissions

: Computer file-systems can store extra information about files,
  including file permissions.  For example, the file permissions tell
  the file-system whether a particular user should be able to read the
  file, or write the file or execute the file as a program.

voxel

: Voxels are volumetric pixels - that is, they are values in a regular
  grid in three dimensional space - see the [Wikipedia voxel](https://en.Wikipedia.org/wiki/Voxel) entry.
:::
