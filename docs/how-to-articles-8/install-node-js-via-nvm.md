# Step 1: Remove Existing Node.js Installs

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/install-node-js-via-nvm>

If NVM is not set up accurately in your system, you might face issues when trying to install and start Studio. This topic provides step-by-step instructuions on how to install NVM and Node.js via NVM so that you face no issues when starting Studio.

Node.js is a prerequisite of Neutrinos Studio. It is required to install the dependencies (such as default templates and plugins) of Neutrinos Studio. You can install Node.js directly, or via NVM.

NVM stands for Node.js version manager. It allows you to have multiple versions of node on the same machine and switch between them easily. It also allows you to easily upgrade your Node.js versions when required. It works with most Unix-like OSes, including OSX.

Perform the following steps to install NVM and the version of Node.js that Studio supports:

#### Step 1: Remove Existing Node.js Installs

If you have any global Node.js modules installed via NPM, we suggest you delete them. Check if Node.js is already installed on your system by running the command below at the command line:

```markdown
which node which npm
```

If there is no output, you can directly jump to **Step 2**. If there is any output, run the following commands to completely remove each version of node and npm. Be sure to make a note of the output of each command, we will be using these shortly.

![Information](/resources/Storage/how-to-articles-8/info.png)
 The steps below for removing Node.js involve the use of the rm -rf command which can be read as **ReMove -Recursively -Force**. There is no undo for this command and you will not be warned before deletion. Be extremely careful of the directory name you enter. Check each directory name you enter, twice, before hitting return.

There are many ways to remove Node.js from your system, the exact details will depend upon how it was installed. If you have used an operating system package manager, consult the respective documentation for details on how to remove Node.js; most have a simple installer to handle it.

If Node.js has been installed manually from the site, or from the source, you will need to remove it manually. Remove Node.js by using the rm -rf option on each of the directories listed in the which command.

Copy CodeMarkdownsudo rm -rf /directory/of/node/npm

Also, run each of the following commands on each directory to remove any other odds and ends that hang around.

Copy CodeMarkdownsudo rm -f /usr/local/share/man/man1/node.1
sudo rm -f /usr/local/lib/dtrace/node.d
sudo rm -rf ~/.npm
sudo rm -rf ~/.node-gyp

Before going any further, run the which command again. If any directories still appear, go ahead and rm -rf each of those directories too.

#### Step 2: Install NVM

You can install NVM by running the latest script on Github. See the [Install Script](https://github.com/nvm-sh/nvm#install-script) on GitHub. This script works for both Bash and ZSH and will pick the correct profile automatically.

#### Step 3: Install Node.js Via NVM

To install a particular version of Node.js, use the following command:

Make sure to install the version of Node.js that is supported by Neutrinos Platform. See [Prerequisites](/smart/project-sample-how-to-guide/before-you-begin/a/h3_559199291) to view the supported version.

```markdown
nvm install 14.17.6
```

By installing NVM, you can use both node and npm commands without the need for elevated permissions. You can also easily manage different versions of Node.js in your machine.

#### Step 4: Set the Default Version of NVM for all Sessions

To set the version of Node.js (that is supported by Neutrinos Platform) as the default for all sessions, run the following command:Copy CodeMarkdownnvm alias default 14.17.6

This is a very important step for Studio to install and work accurately.

Here are a few more commands that might come in handy when working with NVM:

To list all versions available for install on NVM, including IO.js:Copy CodeMarkdownnvm ls-remoteTo list installed versions:Copy CodeMarkdownnvm ls

To use an installed version for the current console session:Copy CodeMarkdownnvm use 14.17.6

When switching versions of Node.js, it is important to run the npm build command directly after. This rebuilds any native addons for the target version of Node.js amongst other things.
