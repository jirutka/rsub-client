Remote Sublime Text (rsub)
==========================
[![version](https://badge.fury.io/py/rsub.svg)](https://pypi.python.org/pypi/rsub)
[![downloads](https://pypip.in/d/rsub/badge.svg)](https://pypi.python.org/pypi/rsub)

With `rsub` you can open and edit files from a remote machine (you’re connected via SSH) in your
local [Sublime Text](http://www.sublimetext.com/)* or [TextMate 2](https://github.com/textmate/textmate).
No need to setup a shared filesystem or anything like that, just a
[SSH tunnel](#setting-up-the-connection)!

This script is a port of the original [rmate](https://github.com/textmate/rmate).

_* To get it work on Sublime Text you need [rsub-plugin](https://github.com/jirutka/rsub-plugin)._


## Installation

The rsub requires Python 2.7+ or 3.× and module [docopt](https://github.com/docopt/docopt) 0.4.0+.

### System-wide

Install from PyPi system-wide:

    sudo pip install rsub

…or manually:

    git clone git@github.com:jirutka/rsub-client.git
    cd rsub-client
    sudo ./setup.py install
    cd .. && rm -Rf rsub-client

### Locally

If you don’t have root access to the system, or just don’t want to install rsub system-wide, then
you can tell `pip` or `setup.py` to install rsub into your home directory (namely `~/.local`):

    pip install --user rsub

…or manually:

    git clone git@github.com:jirutka/rsub-client.git
    cd rsub-client
    ./setup.py --user install
    cd .. && rm -Rf rsub-client

The `rsub` script should be installed in `~/.local/bin`. If you want to make it accessible from
anywhere, add this directory to your `PATH` (choose one according to shell you’re using):

    echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc                   # bash
    echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.zshrc                    # zsh
    echo 'set -x PATH $HOME/.local/bin $PATH' >> ~/.config/fish/config.fish  # fish


## Usage

You can use `rsub --help` to see the usage:

    Usage:
      rsub [options] [-l NUM] [-m NAME] [-t TYPE] -
      rsub [options] [-l NUM...] [-m NAME...] [-t TYPE...] FILE...

      -                     Read from the standard input.
      FILE                  File to open (will be created if does not exist yet).

      -l NUM --line=NUM     Place caret on line [NUM] after loading the file.
      -m NAME --name=NAME   The display name shown in editor.
      -t TYPE --type=TYPE   Treat file as having [TYPE] (e.g. rb, py, md).

    Options:
      -H HOST --host=HOST   Connect to host. Use 'auto' to detect the host from SSH.
      -p PORT --port=PORT   Port number to use for connection.
      -w --wait             Wait for file(s) to be closed by the editor.
      -f --force            Open even if the file is not writable.
      -v --verbose          Verbose logging messages.
      -h --help             Show this message and exit.
      --version             Show version and exit.

Default options can be set in `/etc/rsubrc` and `~/.rsubrc` (or `/etc/rmate.rc` and `~/.rmate.rc`
for compatibility with original rmate):

    host = auto  # prefer host from SSH_CONNECTION over localhost
    port = 52698

You can also set the `RSUB_HOST` and `RSUB_PORT` (or `RMATE_HOST` and `RMATE_PORT`) environment
variables.


## Setting up the connection

To do its job, `rsub` needs a connection back to your computer so that it can talk to Sublime Text
or TextMate. There are multiple ways you can accomplish this, but probably the best way is to use a
reverse SSH tunnel:

    ssh -R 52698:localhost:52698 example.com

The `-R` option sets up a reverse tunnel. The first `52698` names a port on the remote. It will be
connected to `localhost:52698` or the same port on the connecting box. That port number is the
default for Sublime Text, TextMate 2 and rsub. To test things out, launch Sublime Text or
TextMate 2 on your local machine and run a command like this on the remote:

    rsub test.md

After you verify that things are working, feel free to update your SSH setting to automatically
setup the tunnel without you needing to supply the `-R` arguments all the time.

For a single server just add an entry like the following to your `~/.ssh/config`:

    Host example.com
    RemoteForward 52698 localhost:52698

If you want to make those settings the default for all of your servers, use the wildcard host:

    Host *
    RemoteForward 52698 localhost:52698

More information can be found in [this blog post](http://blog.macromates.com/2011/mate-and-rmate/).


## License

This project is licensed under [MIT license](http://opensource.org/licenses/MIT).
