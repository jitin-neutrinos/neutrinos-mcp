# Create the package folder

<https://documentation.neutrinos.com/articles/#!create-a-widget-on-studio-8/package-a-component>

| ![Information](/resources/Storage/create-a-widget-on-studio-8/info.png) | Make sure you reread the steps multiple times and verify the contents of the package before you send it to Neutrinos Support. |
| --- | --- |

To package components, perform the following steps:

1. [Create the package folder](/articles/create-a-widget-on-studio-8/package-a-component/a/h3_272305453)
2. [Create the n-packages.json file](/articles/create-a-widget-on-studio-8/package-a-component/a/h3_1955604441)
3. [Zip the files](/articles/create-a-widget-on-studio-8/package-a-component/a/h3_1338611247)

### Create the package folder

1. In your machine, create a folder with the component name. For example,** excel-viewer**.
2. Within the folder, create another folder by name **package**.

1. Copy all your component files to the package folder.

### Create the n-packages.json file

Within the component folder (in this case, within the **areachart** folder), create the **n-packages.json** file. This file is used to:

- Install the dependencies of the component while launching the app and updates the  /app/src/app/config/import-module.ts  and adds the required third-party modules to the app.
- Provides the metadata information required to display the component on [Neutrinos Store](/articles/concepts-publication/neutrinos-store).

Enter the following details:

- **name**: The name of the package that you want to publish to the marketplace. This should match the package name specified in the **package.json** file and there must exist a component folder by the same name within the component package.
- **version:** The version of Neutrinos Studio with which the component was created.
- **packageType**: The type of package you want to publish to the marketplace. **packageType **can be **studio-package**, or **angular-package**. The Angular package is the angular library and the Studio package is a Neutrinos Studio component. Note that without a studio package, your component will not get published.
- **displayName**: The display name of the component.
- **nModule**: The Angular module on which the component depends (if any). These details are updated to the import-modules.ts file of the app in which you will download the component.
  - **name:** The name of the third-party component.
  - **version:** The version of the third-party component.
  - **packageType:** The type of package.
  - **importStatements:** The import statements to be added to the import-modules.ts file.
  - **Imports:** The modules to be imported to the import-modules.ts file.
- **Metadata**: The details required to display the app on Neutrinos Store.
  - **name**: The name of the studio package that you have created for the component.
  - **displayName**: The display name of the component on Neutrinos Sore.
  - **version**: The version of the component that you are uploading.
  - **username**: The email ID of the developer who created/updated the component.
  - **publisher**: The organization publishing the component. By default, the publisher is Neutrinos.
  - **platformSupportVersion**: The minimum version of Neutrinos Studio on which the component can be downloaded and used.
  - **type**: The type of package. Defaults to **components**.
  - **description**: A simple description of the component and its purpose.
  - **pluginImage**: The icon to be uploaded along with the component.

**Example:**

**Copy CodeJSON{
 "packages": [

 {
 "name": "areachart",
 "version": "1.0.0",
 "packageType": "studio-package",
 "displayName": "Area Chart",
 "nModule": {
 "name": "@swimlane/ngx-charts",
 "version": "x.x.x",
 "packageType": "angular-package",
 "importStatement": "import { NgxChartsModule } from '@swimlane/ngx-charts';",
 "imports": [
 "NgxChartsModule"
 ]
 }

 }
 ],
 "metadata": {
 "name": "neutrinos-area-chart",
 "displayName": "Area Chart",
 "version": "1.0.0",
 "username": "dayashankar@neutrinos.co",
 "publisher": "Neutrinos",
 "platformSupportVersion": {
 "min": "4.0.1"
 },
 "type": "Components",
 "description": "An area chart is a chart which plots the data value using a area perimeter.",
 "pluginImage": "ng-area-chart.png"

 }
}**

### 

This is how the metadata given in the n-packages.json file is used to display the component card on Neutrinos Store:

![Area chart on Neutrinos Store](/resources/Storage/create-a-widget-on-studio-8/area_chart_card.png)

To attach a node along with a component, create a [node SDK](/smart/project-create-a-client-or-server-node/get-started), update the n-packages.json file, and place the nodes package within this package.

### 

### Zip the files

Create a .zip file by selecting the bundled package and the **n-packages.json** file.

The .zip file when unzipped should show the bundle package and the **n-package.json** file.
