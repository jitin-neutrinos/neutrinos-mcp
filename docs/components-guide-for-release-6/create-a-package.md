# Package a Component

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/create-a-package>

## Package a Component

You have already created the studio package and component(s) by following the steps mentioned in the below topics:

- [Create a Studio Package](/articles/components-guide-for-release-6/create-a-studio-package)
- [Create a Component](/articles/components-guide-for-release-6/create-a-component) or [Create an Advanced Component](/articles/components-guide-for-release-6/create-an-advanced-component)

Now, you package the component. The packaging is an essential step if you want to import the component to Neutrinos Studio or publish the component to Neutrinos Marketplace.

### Package a Component

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | Make sure you reread the steps multiple times and verify the contents of the studio package before you test it on Neutrinos Studio. |
| --- | --- |

To package a component, perform the following steps:

1. [Add metadata](/articles/components-guide-for-release-6/create-a-package/a/addmetadata)
2. [Add assets](/articles/components-guide-for-release-6/create-a-package/a/addassets)
3. [Add styles](/articles/components-guide-for-release-6/create-a-package/a/addstyles)
4. [Update the index.js file](/articles/components-guide-for-release-6/create-a-package/a/updateindexjs)

**Step 1: Add Metadata **

Create a file named **n-metadata.json** within the Studio package (In this case, ** $HOME\.neutrinos\plugins\marketplace****-components\nod****e_modules\component-package) **and add all the metadata information about the package. This information will be used when you display your component on Neutrinos Marketplace.

Example:

```json
{  "name":"component-package",  "version":"1.0.0",  "displayName":"AreaChart",  "type":"Components",  "publisher":"Neutrinos",  "platformSupportVersion":"6.0.3",  "packageType":"studio-package",  "dependencies": [  ]}
```

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | In the **n-metadata.json** file, the type attribute can have two values - **Components** or **Templates**. If you have created an advanced component, make sure that you mention the type as **Components**. |
| --- | --- |

**Step 2: Add Assets**

In your studio package, create an **assets** folder. Within the **assets** folder, create an** icons** folder and upload your component's icons. Icons are used to display the component in the palette list. Such as:

Within the **assets** folder, create an **images** folder and add the component's image. The component's image is used to display a preview of the component when dragged and dropped to a page container. Such as:

**Step 3: Add Styles**

If you want to style your component, inside your component's package, create a** styles** folder. Within the **styles** folder, create an **index.css** file and write your CSS script in it. If you are using classes in your CSS script, you should prefix the class names with your package name so that the package's CSS doesn't conflict with the studio CSS.

Example:

```css
.drop-view{background: #d9e8ff!important; }.drop-container {border: 1pxsolid#ccc!important;border-radius: 5px;background: white!important;display: table;min-width: calc(100%-50px);height: 100%;margin: 0px!important;outline: none!important;}
```

**Step 4: Update the index.js file  **

Update the** index.js **file in your studio package with the component name to export the new **c****omponent **class to Neutrinos Studio.

If you have created more than one component, create a **components** property and assign all the **component **classes to that property in a sequence. Neutrinos Studio imports the components based on the** export** statement written in this file.

```javascript
// exporting components from the component folder// this is generally done in index.jslet <componentVariable1> = require('./<components>/<new_component1>');let <componentVariable2> = require('./<components>/<new_component2>');//(optional) import the attribute types defined for your component.let <component_attribute_name>Config = require('./attributeTypes/<attribute_type_filename>');module.exports = {components: {        <componentVariable1>,        <componentVariable2>    },//(optional) To be mentioned if you have defined attribute types for your component.attributeTypes: {        '<attribute_key>': new <component_attribute_name>Config(),    }}
```

Example- **To export the AreaChart component:**

**Copy CodeJavaScriptlet AreaChart = require('./AreaChart');

//Importing attribute Types
let schemeConfig = require('./attributeTypes/scheme');

module.exports = {
 components: {
 AreaChart
 }

 // Specifying attribute types of the component
 attributeTypes: {

 'scheme': new schemeConfig(),

 }
};**

After you perform the above steps, your package should contain the following files:

**Test the Package**

After you package the component, you test the package by creating the **dependency.json** file. Perform the following steps:

1. Create a file named **dependency.json** in the **$HOME\.neutrinos\plugins\marketplace-components **folder.
2. Add the studio package metadata information to this file.

For example:

```javascript
{"packages": [        {"name": "component-package","displayName": "Area Chart","type": "Components","category": "LAYOUTS","version": "1.0.0","description": "To create a component","platformSupportVersion": "6.0.3","publisher": "Neutrinos","packageType": "studio-package"        }      ]}
```

You can now import your component to Neutrinos Studio and test its functionality.
