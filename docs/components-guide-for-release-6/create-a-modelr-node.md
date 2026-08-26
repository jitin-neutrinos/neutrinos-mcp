# Create and Publish a Modelr Node

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/create-a-modelr-node>

## Create and Publish a Modelr Node

Neutrinos Modelr allows you to create server-side services for your application to link to a variety of backend systems such as Enterprise Service Bus (ESB), Cloud Services, databases, etc. To create server-side services, you drag and drop Modeler nodes and create flows. By default, Neutrinos Modeler provides you with a large set of nodes.

![](/resources/Storage/components-guide-for-release-6/1-5-4-create-and-publish-a-modelr-node-img0001.png)

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | Make sure you reread the steps multiple times and verify the contents of the package before submitting to Neutrinos Support. |
| --- | --- |

To create a Modelr node, perform the steps mentioned in the [Creating Modelr Nodes](/smart/project-b-modelr-documentation/creating-nodes) topic.

### Create the Modelr Node Package

Perform the following steps to package the nodes and submit them to Neutrinos Store.

**Create a parent folder**

Create a parent folder in which you will save the modeler node and the component. For example, **excel-viewer-parent**.

**Create the component folder**

To publish a Modelr node to Neutrinos Store, you should associate it with a palette component. See [Create and Publish a Component](/articles/components-guide-for-release-6/create-your-own-component)to learn more. If you do not have a component to be associated with the package, create a dummy, placeholder component.

**Step 1**: Inside the parent folder, create a component folder. For example, **excel-viewer**.

**Step 2**: Within the component folder, create a folder named **package**.

**Step 3**: Within the package folder, create an **index.js** file.

**Step 4**: If you have a component to be associated with the Modelr node, add the component name within the module.exports statement. If you do not have a component to be associated with the node, add a blank module.exports statement.

```javascript
module.exports = {}
```

**Step 5**: Create a** n-metadata.json** file and include the component metadata information. Note that the **name **attribute should be the same as the component folder name that you created in Step1.

```json
{    "name":"excel-viewer",    "version":"4.0.0",    "displayName":"Excel Viewer",    "type":"Components",    "publisher":"Neutrinos",    "platformSupportVersion":"6.0.3",    "packageType":"studio-package",    "dependencies":[]  }
```

**Step 6**: Create a **package.json **file.

- Open a command prompt
- Navigate to the component folder.
- Invoke the npm utility by issuing the npm init command. Provide required information when prompted. Make sure that the **name** attribute should be the same as the component package folder name.
- After the **package.json **file is created, edit the file and input the import statement to import Angular packages (if any) using the nModules property.

**Template: **

**Copy CodeJSON"nModule": {

"importStatement": "import { <module> } from '<angular-package>';",

"imports": ["<module>"]

}


**

- Enter the Neutrinos Studio version in which you are creating the component, for example, "studioVersion" : "6.0.3".
- Save the file.

Example:

```json
{  "name": "excel-viewer",  "version": "4.0.0",  "description": "Marketplace package to convert excel to html and view on the browser",  "main": "index.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "keywords": [    "excelAsHtml",    "n-sheet",    "Excel",    "Viewer"  ],  "author": "...",  "license": "...",  "nModule": {      "importStatement": "import { NSheetModule } from 'n-sheet';",      "imports": ["NSheetModule"]    },  "studioVersion" : "6.0.3"}
```

At the end of step 6, the folder should contain the following files:

### Create the Modelr Folder

**Step 1**: Create a Modelr folder. For example, **node-red-exceltohtml**.

**Step 2**: Within the Modelr folder, create a folder named **package**.

**Step 3**: Within the package folder, copy all the Modelr node files that you created using the [Creating Nodes](/smart/project-b-modelr-documentation/creating-nodes) topic.

**Step 4:** Update the package.json file with the Neutrinos Studio version number. For example: "studioVersion" : "6.0.3". Make sure that the name attribute in the** package.json **file is the same as the Modelr package folder name.

Example:

```json
{  "name": "node-red-exceltohtml",  "version": "4.0.0",  "description": "",  "main": "exceltohtml.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "author": "Jatahworx <npm.dev@jatahworx.com>",  "license": "ISC",  "dependencies": {    "sheetchart": "~1.20190429.1",    "html-minifier": "4.0.0",    "zlib": "1.0.5"  },  "node-red": {    "nodes": {      "exceltohtml": "exceltohtml.js"    }  },  "studioVersion" : "6.0.3"}
```

At the end of step 4, the folder should contain the following files:

![](/resources/Storage/components-guide-for-release-6/1-5-4-create-and-publish-a-modelr-node-img0004.png)

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | If you want to associate an Angular library with your Modelr node, follow the steps in the Create an Angular package topic to package the Angular library folder with the Modelr node. |
| --- | --- |

**Package the folder**

After you create component and modelr folders, navigate back to the parent folder (in this case, excel-viewer-parent). Create the **n-packages.json** file and add the component and Modelr metadata to this file.

Make sure that the package names are the same as the studio and Modelr packages that you created in the previous steps. Also, make sure that the **packageType** is valid. The **packageType** for studio should be "packageType": "studio-package" and **packageType** for Modelr node should be "packageType": "modelr-node".

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | If you have associated an Angular package with the Modelr node, add the Angular package metadata to this file with "packageType": "angular-package". |
| --- | --- |

Example:

```json
{    "packages": [        {            "name": "excel-viewer",            "version": "4.0.0",            "packageType": "studio-package"        },                {            "name": "node-red-exceltohtml",            "version": "4.0.0",            "packageType": "modelr-node"        }    ]}
```

**Zip the folder**

Create a .zip file by selecting the folders and the **n-packages.json** file.

The .zip file when unzipped should show the Modelr folder, the component folder, the Angular package folder (if any), and the **n-package.json** file.

Submit the .zip file to Neutrinos by raising a support ticket on [support@neutrinos.co](mailto:support@neutrinos.co). The Neutrinos team will test the functionality of the node. If approved, your node is then hosted on Neutrinos MarketPlace.
