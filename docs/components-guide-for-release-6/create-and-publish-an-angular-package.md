# Create and Publish an Angular Package

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/create-and-publish-an-angular-package>

## Create and Publish an Angular Package

Many applications need to solve the same general problems, such as presenting a unified user interface, presenting data, and allowing data entry. In such a situation, you can create general solutions that can be adapted for re-use in different apps. Such a solution can be built as Angular libraries and these libraries can be published and shared as npm packages on Neutrinos Store.

By default, Angular provides you with a large set of default libraries. See [Using Published libraries](https://angular.io/guide/using-libraries) to learn how to use them. Apart from using these libraries, if you want to create your own library, perform the following steps:

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | Make sure you reread the steps multiple times and verify the contents of the package before submitting to Neutrinos Support. |
| --- | --- |

### Create an Angular package

To create an Angular package, perform the steps mentioned in the [Creating Angular package](https://angular.io/guide/creating-libraries) topic.

**Publish the Angular package**

To publish an Angular package to Neutrinos Store, you should associate it with a component. If you do not have a component to be associated with the package, create a dummy, placeholder component.

**Perform the following steps:**

** Create a parent folder**

Create a parent folder in which you will save the Angular package and the component. For example, **excel-viewer-parent**.

**Create the component folder**

**Step 1**: Inside the parent folder, create a component folder. For example, **excel-viewer**.

**Step 2**: Within the component folder, create a folder named **package**.

**Step 3**: Within the package folder, create an **index.js** file.

**Step 4**: In the **index.js file**, if you have a component associated with the Angular package, provide the component name in the module.exports statement. If you do not have a component associated with the package, enter a blank module.exports statement.

```javascript
module.exports = {}
```

**Step 5**: Create an **n-metadata.json file** and include the component metadata information. Note that the **name** attribute should be the same as the component folder name that you created in** Step1.**

**Copy CodeJSON{
 "name":"excel-viewer",
 "version":"4.0.0",
 "displayName":"Excel Viewer",
 "type":"Components",
 "publisher":"Neutrinos",
 "platformSupportVersion":"6.0.3",
 "packageType":"studio-package",
 "dependencies":[]
 }**

**Step 6**: Create a **package.json** file.

- Open a command prompt
- Navigate to the **component** folder.
- Invoke the npm utility by issuing the npm init command. Provide required information when prompted. Make sure that the **name** attribute should be the same as the component package folder name.
- After the **package.json **file is created, edit the file and add the** import** statement to import Angular packages using the nModule property.
- Enter the Neutrinos Studio version using the studioVersion property.
- Save the file.

Example:

```json
{  "name": "excel-viewer",  "version": "4.0.0",  "description": "Marketplace package to convert excel to html and view on the browser",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "keywords": [    "excelAsHtml",    "n-sheet",    "Excel",    "Viewer"  ],  "author": "...",  "license": "Proprietary",  "nModule": {      "importStatement": "import { NSheetModule } from 'n-sheet';",      "imports": ["NSheetModule"]    },  "studioVersion" : "6.0.3"}
```

At the end of step 6, the component folder should contain the following files:

### Create the Angular package folder

**Step 1**: In the parent folder(**excel-viewer-parent** folder), create an Angular package folder. For example, **n-sheet**.

**Step 2**: Within the Angular package folder, create a folder named **package**.

**Step 3**: Within the **package** folder, copy all the Angular package files that you created using the [Creating Angular package](https://angular.io/guide/creating-libraries)topic. The files will be located in the **dist **folder of your Angular project after you build your Angular library.

Your package folder should look similar to this:

**Step 4**: Update the **package.json file** with the Neutrinos Studio version number. For example: "studioVersion": "6.0.3". Make sure that the **name **attribute should be the same as the Angular package folder name.

Example:

```json
{  "name": "n-sheet",  "version": "4.0.0",  "description": "",  "main": "exceltohtml.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "author": "Jatahworx <npm.dev@jatahworx.com>",  "license": "ISC",  "dependencies": {    "sheetchart": "~1.20190429.1",    "html-minifier": "4.0.0",    "zlib": "1.0.5"  },  "node-red": {    "nodes": {      "exceltohtml": "exceltohtml.js"    }  },  "studioVersion" : "6.0.3"}
```

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | If you want to associate a Modelr node with your Angular library, follow the steps in the [Create a Modelr node](/articles/project-component-test/1-5-4-create-and-publish-a-modelr-node/a/a_1514164392CreateAModelrNode) topic to package the Angular library folder with the Modelr node. |
| --- | --- |

### Create n-packages.json

After you create the component and Angular package folders, navigate back to the parent folder (in this case,** excel-viewer-parent**). Create the** n-packages.json** file and add the component and Angular package metadata to this file.

Make sure that the **name **attributes indicate the Angular package folder and the component folder names respective. Also, make sure that the packageType parameter is valid.

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | If you have associated a Modelr node with your Angular library, enter the Modelr node metadata information in the n-pckages.json file with "packageType": "modelr-node". |
| --- | --- |

Example:

```json
{    "packages": [        {            "name": "excel-viewer",            "version": "4.0.0",            "packageType": "studio-package"        },        {            "name": "n-sheet",            "version": "4.0.0",            "packageType": "angular-package"        }            ]}
```

### Zip the package

Create a .zip file by selecting the folders and the** n-packages.json** file.

The .zip file when unzipped should show the** Angular package** folder, the **component **folder, the **Modelr node **package(if associated), and the **n-package.json **file.

Submit the .zip file to Neutrinos by raising a support ticket on [support@neutrinos.co](mailto:support@neutrinos.co). The Neutrinos team will test the functionality of the Angular library. If approved, your Angular package is then hosted on Neutrinos MarketPlace.
