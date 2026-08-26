# Update index.js file

<https://documentation.neutrinos.com/articles/#!create-a-widget-on-studio-7/update-index-js-file>

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
