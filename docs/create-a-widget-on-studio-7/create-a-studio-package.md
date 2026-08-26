# Create the studio package

<https://documentation.neutrinos.com/articles/#!create-a-widget-on-studio-7/create-a-studio-package>

| ![Information](/resources/Storage/create-a-widget-on-studio-7/info.png) | Make sure you reread the steps multiple times and verify the contents of the studio package. |
| --- | --- |

A Studio package contains various files to make a [component](/articles/concepts-publication/component) for Neutrinos Studio. Perform the following steps:

- [Create the studio package](/articles/create-a-widget-on-studio-7/create-a-studio-package/a/createstudiopackage)
- [Install the bhive-toolkits package](/articles/create-a-widget-on-studio-7/create-a-studio-package/a/installbhive)
- [Create an index.js file](/articles/create-a-widget-on-studio-7/create-a-studio-package/a/createindexjs)

---

### Create the studio package

**Step1**: Navigate to** $HOME\.neutrinos\plugins\marketplace-components\node_modules** in your local machine. This folder automatically gets created when you download a plugin from the marketplace. If these folders do not exist, create them.

By default, the $HOME path is:

- ***C:\Users\<user>*** in a Windows machine.
- **/home/<user>** in a Linux machine.
- ***/Users/<user>* ** in a MAC machine.

**Step 2**: Within the **$HOME\.neutrinos\plugins\marketplace-components\node_modules** folder, create a folder with the name of the format:  {organisation name}{package-name}. Make sure you give a unique name for the package-name. For example, **neutrinos-****component-package**. This will be your studio package which will contain all the components that you are going to create (and their associated files).

---

### Install the bhive-toolkits package

**@jatahworx/bhive-toolkits** npm package is an SDK package that has useful features that will be used throughout when creating the **Studio package**.

**Step 1**: Navigate to the studio package that you created, open a terminal window, run the following command:

```bash (unix shell)
npm init
```

Running this command will initialize the package folder with the package.json file. **package.json** is a plain JSON (JavaScript Object Notation) text file which contains all metadata information about the package.

You should see a similar output as shown in the below screenshot. This utility will help you create the** package.json** file. Enter the required values when prompted:

![](/resources/Storage/create-a-widget-on-studio-7/1-5-2-1-create-a-studio-package-img0002.png)

| ![Warning](/resources/Storage/create-a-widget-on-studio-7/warning.png) | Make sure that you enter the same studio package name that you created at the start of this topic. |
| --- | --- |

**Step 2**: Find the Neutrinos Studio version that you have installed in your machine by launching the Studio and clicking the** About **button on the **Help** menu.

**Step 3**: Install the **@jathworx/bhive-toolkits** package that is compatible with the current studio version. For example, run the following command to install the **7.1.0** version of the **bhive-toolkits** package by giving the version number after the package name. This is because you have installed the Neutrinos Studio version 7.1.0.

```json
npm i @jatahworx/bhive-toolkits@7.1.0
```

![](/resources/Storage/create-a-widget-on-studio-7/1-5-2-1-create-a-studio-package-img0005.png)

---

### Create an index.js file

Create an **index.js** file in your studio package (In this case,** $HOME\.neutrinos\plugins\marketplace-components\node_modules\component-package**) to export all the new [component](/articles/create-a-widget-on-studio-7/create-advanced-component-file) classes that you have created for Neutrinos Studio. If you do not have a component, create the **index.js** file with an empty module. exports statement:

```javascript
module.exports = {    };
```
