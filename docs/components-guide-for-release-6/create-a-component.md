# Create a Component

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/create-a-component>

## Create a Component

### Overview

Components are the most basic UI building blocks of an app. In Neutrinos Studio, UI components are called palette components as they exist in the palette section of the page. You use the **component** class to interact with the **.html** file of the component.

By default, the Neutrinos Platform provides you with a large set of components that you can use to develop your apps. See [Default Palette Component](/articles/components-guide-for-release-6/components) to learn about them. Apart from the existing components, Neutrinos also allows you to create your own components and add them to the palette list of Neutrinos Studio. This provides you with an advantage of re-usability, saves time for development and maintenance, and helps create more consistent applications.

### Create the Component File

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | Make sure you reread the steps multiple times and verify the contents of the component file. |
| --- | --- |

**Step 1**: Open a code editor.

**Step 2**: In your studio package, create a .js file for the component that you want to create. For example, if you want to create an Area Chart component, you create an **AreaChart.js** file. Make sure that the file name is unique within your studio package.

**Step 3**: Open the component file in an editor of your choice. In the .js file, import the component and attributes classes from **@jathworx/bhive-toolkits** repository using the require command.

```javascript
// importing Attribute and Component classlet Component = require('@jatahworx/bhive-toolkits').Component;let Attribute = require('@jatahworx/bhive-toolkits').Attribute;
```

**Step 4:** Create a module with a class name and extend the** Component** class. The class name should be the same as the component file name.

```javascript
// extending the Component class to get all its methodsmodule.exports = class AreaChart extends Component {constructor() { ... }
```

**Step 5**: Call the **super** constructor to take all the parameters described in the **Component** class. The parameters include:

- **name**: Name of the component. Accepts string value in lowercase
- **designerTemplate**: HTML to be displayed on the droppable container
- **paletteTemplate**: HTML or text to be displayed on the palette list
- **componentLabel**: Dynamic labels to be assigned for a component
- **templateUrl**: Link to the component documentation
- **template**: HTML template which is generated after each page is saved

```javascript
super(name, template, designerTemplate, paletteTemplate, componentLabel, templateUrl);
```

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | The name of the component should be prefixed with the package name. For example: **const name = 'NG-area-chart';** |
| --- | --- |

**Step 6**: Add attributes to the component. Create a **super** constructor with the addAttribute method which takes all the parameters described from the **Attribute** class. The parameters include:

- **key**: The unique text for the attribute to be replaced inside the template string.
- **value**: The default value of the attribute which gets displayed in the properties window. During template generation, the value field will be replaced according to the Attribute type.
  - **type**: The type of attribute which determines how the key is replaced during template generation:
  - **a[attribute]**: Searches for the key and replaces with the default value or the user input in the properties window of a palette component.
  - **kv[key-value]**: Searches for the key and assigns the value to the key key=value.
  - **ma[multiple-attribute]**: Enters multiple attributes if the template of the palette component has multiple key parameters that are supposed to be replaced with the same value.
  - **vk[value-key]**: Provides a unique key for a value in the properties window. For example, #form1=ngForm or #firstName=ngModel. Then, give unique key as **ngModel** and the user input assigned as value gets added as #value=key.

- **useAsLabel: **If you want to use the attribute as a label.
- **complexity: **For a component in Neutrinos Studio, attributes can be categorized as **Basic **and **Advanced **properties. By default, all attributes that you provide for a component will appear under **Basic Properties**. If you want to show the attributes under** Advanced Properties**, specify the** complexity **parameter and provide its value as **advanced**.

```javascript
super.addAttribute(  new Attribute({    key, value, type, useAsLabel, complexity  })    );
```

![Area Chart properties](/resources/Storage/components-guide-for-release-6/area1.png)

**Step 7 (optional):** By default, the defined attributes of your component will be of type Input where you will see a label and an input field in which you give the value for the attribute. For example:

If you want to change the attribute view type to **toggle** or **drop-down list**, perform the following steps:

1. In your studio package, create a folder named** attributeTypes**.
2. In the **attributeTypes **folder, create** <attribute_name>.js** file of each attribute and define the view attribute type. For example, to display the **Scheme** attribute of the **Area Chart **component as a drop-down list, add the following code. Here, this.value is the **key** of the attribute mentioned in your **<component>.js **file.

```javascript
let SchemeInstance = null;module.exports = class scheme {    constructor() {        if (!SchemeInstance) {            SchemeInstance = this;            //set all other default values            this.displayAs = 'Scheme';            this.value = '[scheme]'            this.type = 'DROPDOWN';            this.values = [                { display: "None", value: "", default: true },                { display: "Vivid", value: "'vivid'" },                { display: "Natural ", value: "'natural'"},                { display: "Cool", value: "'cool'" },                { display: "Solar", value: "'solar'" },                { display: "Air", value: "'air'"},                { display: "Aqua", value: "'aqua'"},                { display: "Flame", value: "'flame'"},                { display: "Ocean", value: "'ocean'"},                { display: "Forest", value: "'forest'"},                { display: "Horizon", value: "'horizon'"},                { display: "Neons", value: "'neons'"},                { display: "Picnic", value: "'picnic'"},                { display: "Night", value: "'night'"},                { display: "Night Lights", value: "'nightLights'"}            ];        }        return SchemeInstance;    }}
```

To make the **Show X-Axis Label** attribute of the **Area Chart **component appear as a **toggle**, add the following code:

```javascript
let ShowXAxisLabelInstance = null;module.exports = class ShowXAxisLabel {    constructor() {        if (!ShowXAxisLabelInstance) {            ShowXAxisLabelInstance = this;            //set all other default values            this.displayAs = 'Show X-Axis Label';            this.value = '[showXAxisLabel]'            this.type = 'TOGGLE';            this.values = {'true-value':'true', 'false-value': 'false'}        }        return ShowXAxisLabelInstance;    }
```

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | If you add attribute types for your component, you have to import the same in your** index.js **file. |
| --- | --- |

**Step 8**: Set the group type of the component. To set the group type of the Component, use the setType method of the **super** class which takes in an argument of type number. Use Component's static variable COMPONENT_TYPE_TITLES to get the correct value of component classification, and to make the code more readable, and maintainable. Accepted COMPONENT_TYPE_TITLES are:

- LAYOUT
- NG_CHARTS
- NGX_CHARTS
- FORM_CONTROLS
- NAVIGATION
- OTHERS

For example:

```javascript
super.setType(Component.COMPONENT_TYPE_TITLES.NGX_CHARTS.val);
```

**Step 9**: Create a get method to accept the template of the component.

**Step 10**: Save the component file. Your studio package should now contain the following files and folders:

**Example of a component:**

**Copy CodeJavaScript'use strict';
let Component = require('@jatahworx/bhive-toolkits').Component;
let Attribute = require('@jatahworx/bhive-toolkits').Attribute;

module.exports = class AreaChart extends Component {
 constructor() {
 const name = 'NG-area-chart';
 const designerTemplate = `<div class=\"ad-charts ad-area-chart\" component-label="Area Chart"></div>`;
 const paletteTemplate = 'Area Chart';
 const componentLabel = 'Area Chart';
 const templateUrl =
 'https://swimlane.gitbooks.io/ngx-charts/content/charts/area-chart.html';

 super(
 name,
 designerTemplate,
 paletteTemplate,
 componentLabel,
 templateUrl
 );


 super.addAttribute(
 new Attribute({
 key: 'componentLabel',
 value: 'Area Chart',
 type: 'kv',
 useAsLabel: true
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[gradient]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[xAxis]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[yAxis]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[legend]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[showXAxisLabel]',
 value: '',
 type: 'kv',
 complexity: 'advanced'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[showYAxisLabel]',
 value: '',
 type: 'kv',
 complexity: 'advanced'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[yAxisLabel]',
 value: '',
 type: 'kv',
 complexity: 'advanced'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[xAxisLabel]',
 value: '',
 type: 'kv',
 complexity: 'advanced'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '(select)',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[scheme]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[results]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: 'fxLayout',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(new Attribute({
 key: 'fxFlex',
 value: '',
 type: 'kv'
 }));
 super.addAttribute(
 new Attribute({
 key: '[schemeType]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[showGridLines]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[legendTitle]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[legendPosition]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(new Attribute({
 key: '[view]',
 value: '',
 type: 'kv'
 }));
 super.addAttribute(
 new Attribute({
 key: '[autoScale]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[xScaleMin]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[xScaleMax]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[yScaleMin]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[yScaleMax]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[animations]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[customColors]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[timeline]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[tooltipDisabled]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[xAxisTicks]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[yAxisTicks]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[xAxisTickFormatting]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[yAxisTickFormatting]',
 value: '',
 type: 'kv'
 })
 );
 super.setType(Component.COMPONENT_TYPE_TITLES.NGX_CHARTS.val);
 }

 get template() {
 return `<div %fxFlex% %fxLayout%>
 <ngx-charts-area-chart %bCustomProps% %[scheme]% %[schemeType]% %[results]% %style% %class% %[gradient]% %[view]% %[xAxis]% %[yAxis]% %[legend]% %[legendTitle]% %[legendPosition]% %[showXAxisLabel]% %[showYAxisLabel]% %[showGridLines]% %[yAxisLabel]% %[xAxisLabel]% %(select)% %[autoScale]% %[xScaleMin]% %[xScaleMax]% %[yScaleMin]% %[yScaleMax]% %[animations]% %[customColors]% %[timeline]% %[tooltipDisabled]% %[xAxisTicks]% %[yAxisTicks]% %[xAxisTickFormatting]% %[yAxisTickFormatting]%></ngx-charts-area-chart>
 </div>`;
 }
 set template(templateString) {}
};
**
