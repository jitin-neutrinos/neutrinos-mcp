# Publish to Neutrinos Store

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/publish-to-marketplace>

## Publish to Neutrinos Store

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | Make sure you reread the steps multiple times and verify the contents of the package before you send it to Neutrinos Support. |
| --- | --- |

To publish components to Neutrinos Store, perform the following steps:

### Create the package folder

1. In your machine, create a folder with the component name. For example,** excel-viewer**.
2. Within the folder, create another folder by name **package**.

1. Copy all your component files to the package folder.

### Create the n-packages file

1. Within the component folder (in this case, within the **areachart** folder), create a file named **n-packages.json** and add the following package dependency information in this file:
  - **name**: The name of the package that you want to publish to the marketplace. This should match the package name specified in the **package.json** file and there must exist a component folder by the same name within the component package.
  - **version:** The version of Neutrinos Studio with which the component was created.
  - **packageType**: The type of package you want to publish to the marketplace. **packageType **can be **studio-package**, **modelr-node**, or **angular-package**. The Angular package is the angular library. The Modeler node is a Neutrinos Modeler node. The Studio package is a Neutrinos Studio component. Note that without a studio package, your component will not get published.

**Example:**

**Copy CodeJSON{
 "packages": [

 {
 "name": "areachart",
 "version": "1.0.0",
 "packageType": "studio-package"
 }
 ]
}**

### Zip the files

Create a .zip file by selecting the bundled package and the **n-packages.json** file.

The .zip file when unzipped should show the bundle package and the **n-package.json** file.

### Submit to Neutrinos

Submit the .zip file to Neutrinos by raising a support ticket on [support@neutrinos.co](mailto:support@neutrinos.co). The Neutrinos team will review the component and upload the component(s) to the MarketPlace.
