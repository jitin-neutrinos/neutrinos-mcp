# Create an Angular Package

<https://documentation.neutrinos.com/articles/#!create-a-widget-on-studio-7/create-and-publish-an-angular-package>

| ![Information](/resources/Storage/create-a-widget-on-studio-7/info.png) | Make sure you reread the steps multiple times and verify the contents of the package before submitting it to Neutrinos Support. |
| --- | --- |

To create an [Angular package](/smart/project-concepts/angular-package), perform the steps mentioned in the [Creating Angular package](https://angular.io/guide/creating-libraries) topic.

**Create the Angular package folder**

**Step 1**: Create an Angular package folder. For example, **n-sheet**.

**Step 2**: Within the Angular package folder, create a folder named **package**.

**Step 3**: Within the **package** folder, copy all the Angular package files that you created using the [Creating Angular package](https://angular.io/guide/creating-libraries)topic. The files will be located in the **dist **folder of your Angular project after you build your Angular library.

Your package folder should look similar to this:

**Step 4**: Update the **package.json file** with the Neutrinos Studio version number. For example: "studioVersion": "7.1.0". Make sure that the **name **attribute should be the same as the Angular package folder name.

Example:

```json
{  "name": "n-sheet",  "version": "4.0.0",  "description": "",  "main": "exceltohtml.js",  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1"  },  "author": "Jatahworx <npm.dev@jatahworx.com>",  "license": "ISC",  "dependencies": {    "sheetchart": "~1.20190429.1",    "html-minifier": "4.0.0",    "zlib": "1.0.5"  },  "node-red": {    "nodes": {      "exceltohtml": "exceltohtml.js"    }  },  "studioVersion" : "7.1.0"}
```
