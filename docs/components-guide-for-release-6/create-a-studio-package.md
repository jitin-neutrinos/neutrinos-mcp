# Create a Studio Package

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/create-a-studio-package>

## Create a Studio Package

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | Make sure you reread the steps multiple times and verify the contents of the studio package. |
| --- | --- |

A Studio package contains various classes to make a palette component for Neutrinos Studio. Perform the following steps:

- [Create the studio package](/articles/components-guide-for-release-6/create-a-studio-package/a/createstudiopackage)
- [Install the bhive-toolkits package](/articles/components-guide-for-release-6/create-a-studio-package/a/installbhive)
- [Create the package.json file](/articles/components-guide-for-release-6/create-a-studio-package/a/createpackagejson)
- [Create an index.js file](/articles/components-guide-for-release-6/create-a-studio-package/a/createindexjs)

### Create the studio package

**Step1**: Navigate to** $HOME\.neutrinos\plugins\marketplace-components\node_modules** in your local machine. This folder automatically gets created when you download a plugin from the marketplace. If these folders do not exist, create them.

By default, the $HOME path is:

- ***C:\Users\<user>*** in a Windows machine.
- **/home/<user>** in a Linux machine.
- ***/Users/<user>* ** in a MAC machine.

**Step 2**: Within the **$HOME\.neutrinos\plugins\marketplace-components\node_modules** folder, create a folder with the name of your choice. For example, **component-package**. This will be your studio package which will contain all the components that you are going to create (and their associated files).

### Install the bhive-toolkits package

Find the Neutrinos Studio version that you have installed in your machine by launching the Studio and clicking the** About **button on the **Help** menu.

Open a terminal window, navigate to the studio package that you created, and install the **@jathworx/bhive-toolkits** package. Make sure that you install the same version of the toolkits package as that of your Neutrinos Studio version. For example, using the below command, you install the **6.0.3** version of the **bhive-toolkits** package by giving the version number after the package name. This is because you have installed the Neutrinos Studio version 6.0.3.

```markdown
npm i @jatahworx/bhive-toolkits@6.0.3 --save
```

![](/resources/Storage/components-guide-for-release-6/1-5-2-1-create-a-studio-package-img0005.png)

You will see the **node_modules** folder created inside the Studio package. This package contains all the classes required to make a complete palette component for Neutrinos Studio.

### Create the package.json file

**package.json** is a plain JSON (JavaScript Object Notation) text file which contains all metadata information about the package.

**Step 1**: In the terminal window, run the following command:

```markdown
cd <location of the studio package>npm init
```

**Step 2**: You should see a similar output. This utility will help you create the** package.json** file. Enter the required values when prompted:

| ![Warning](/resources/Storage/components-guide-for-release-6/warning.png) | Make sure that you enter the same studio package name that you created at the start of this topic. |
| --- | --- |

You will see the** package.json** file created within your package.

**Step 3**: Edit the** package.json **file to add the Neutrinos Studio version on which you are building the component.

In this case, it is "studioVersion": "6.0.3".

```json
{  "name": "component-package",  "version": "1.0.0",  "description": "",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "author": "",  "license": "ISC",  "studioVersion": "6.0.3",  "dependencies": {    "@jatahworx/bhive-toolkits": "^6.0.3"  }}
```

**Step 4**: If you have created palette components of an Angular library and if you want to install that library in the app (along with the Studio package plugin), you should configure the **nModule** property and specify the metadata of that Angular library.

- **Add the importStatement property**: This should be a valid semi-colon separated statement with appropriate Modules listed for imports from the library. For example: import { ModuleName1,ModuleName2 } from 'library-name';.
- **Add the imports property**: These are declaration statements of the modules with configurations (if required) for the library. For example: ModuleName.forRoot({ name: environment.properties.name});. You can fill in all the imports by using the following template:

```json
imports: [ "ModuleName.forRoot({name: environment.properties.name})", "ModuleName1"]
```

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | Make sure you follow the import template, else the installation might fail. |
| --- | --- |

**Example:** To import the **Ngx-bootstrap** Angular package with the **component-package** studio package:

```json
{  "name": "component-package",  "version": "1.0.0",  "description": "",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "author": "",  "license": "ISC",  "studioVersion": "6.0.3",  "nModule": {    "name": "ngx-bootstrap",    "version": "5.1.1",    "packageType": "angular-package",    "importStatement": "import { BsDatePicker } from 'ngx-bootstrap';",    "imports": [      "BsDatePicker"    ]  },  "dependencies": {    "@jatahworx/bhive-toolkits": "^6.0.3"  }}
```

### Create an index.js file

Create an **index.js** file in your studio package (In this case,** $HOME\.neutrinos\plugins\marketplace-components\node_modules\component-package**) to export all the new component classes that you have created to Neutrinos Studio. If you do not have a component, create the **index.js** file with an empty module.exports statement:

```javascript
module.exports = {    };
```
