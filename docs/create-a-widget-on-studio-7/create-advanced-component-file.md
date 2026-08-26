# Create the Advanced Component file

<https://documentation.neutrinos.com/articles/#!create-a-widget-on-studio-7/create-advanced-component-file>

To create an [advanced component](/smart/project-concepts/advanced-component) on Neutrinos Studio, perform the following steps:

1. Design the template
2. Create the advanced component file

**Design the Template **

Before creating an Advanced Component, you should familiarize yourself with the end Angular template that you wish to generate. For example, if you were to create MatTable template from the Angular Material library then you should think about the code generation of Sort, Paginator, and Filter as child-components within it. Follow the [Advanced Component- Design guidelines](/articles/create-a-widget-on-studio-7/create-advanced-component-file)to design the template.

**Component: **

![](/resources/Storage/create-a-widget-on-studio-7/1-5-2-3-create-an-advanced-component-img0001.png)

**Template:**

```html
<mat-form-field>  <input matInput (keyup)="applyFilter($event.target.value)" placeholder="Filter"></mat-form-field><div class="mat-elevation-z8">  <table mat-table [dataSource]="dataSource" matSort>    <!-- ID Column -->    <ng-container matColumnDef="id">      <th mat-header-cell *matHeaderCellDef mat-sort-header> ID </th>      <td mat-cell *matCellDef="let row"> {{row.id}} </td>    </ng-container>        <!-- Progress Column -->    <ng-container matColumnDef="progress">      <th mat-header-cell *matHeaderCellDef mat-sort-header> Progress </th>      <td mat-cell *matCellDef="let row"> {{row.progress}}% </td>    </ng-container>        <!-- Name Column -->    <ng-container matColumnDef="name">      <th mat-header-cell *matHeaderCellDef mat-sort-header> Name </th>      <td mat-cell *matCellDef="let row"> {{row.name}} </td>    </ng-container>        <!-- Color Column -->    <ng-container matColumnDef="color">      <th mat-header-cell *matHeaderCellDef mat-sort-header> Color </th>      <td mat-cell *matCellDef="let row" [style.color]="row.color">        {{row.color}}      </td>    </ng-container>        <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>    <tr mat-row *matRowDef="let row; columns: displayedColumns;"></tr>  </table>    <mat-paginator [pageSizeOptions]="[5, 10, 25, 100]"></mat-paginator></div>
```

Remember, that you want to perform minimal configuration to get the table up and running on the user interface.

### Create the Advanced Component file

| ![Information](/resources/Storage/create-a-widget-on-studio-7/info.png) | Make sure you reread the steps multiple times and verify the contents of the studio package before you test it on Neutrinos Studio. |
| --- | --- |

**Step 1**: Open a code editor and navigate to the studio package that you created.

**Step 2**: Inside the studio package, create a .js file for the component you want to create. For example, if you want to create a** Card **component, you create a **Card.js** file in the editor. Make sure that the file name is unique within the repository.

**Step 3**: Import the advanced component and attributes classes from **@jathworx/bhive-toolkits **repository.

```javascript
// importing AdvancedComponent and Attribute classlet AdvancedComponent = require('@jatahworx/bhive-toolkits').AdvancedComponent;let Attribute = require('@jatahworx/bhive-toolkits').Attribute;
```

Step 4: Create a module with a class name and extend your class from the AdvancedComponent class.

```javascript
// extending the Component class to get all its methodsmodule.exports = class Card extends AdvancedComponent {  constructor() {    ...    }
```

| ![Information](/resources/Storage/create-a-widget-on-studio-7/info.png) | The naming convention should be {compane-name}{package-name}{component-name}. |
| --- | --- |

**Step 5**: Call the **super **constructor to take all the parameters described in the AdvancedComponent class. The parameters include:

1. **name**: Name of the component which should be all in small letters. It should follow the naming convention as {Organisation name}{Name of the package}{name of component}. For example, neutrinos-tablepackage-table.
2. **template**: Is the Angular template which will be added to the page template during the Studio Code generation cycle.
3. **designerTemplate: **Template of the UI that will be displayed when the component is dropped on the Page editor canvas.
4. **paletteTemplate: **Display name for the palette component. This will be displayed on the palette list.
5. **componentLabel: **Label for the component which will be used as a label when the component is dropped on the Page editor canvas.
6. **templateUrl:** Link pointing to the documentation for the component.
7. isAvancedComponent(optional): If true, then this Advanced Component will be considered to be a child to an Advanced component.
8. **visible: **If false, then the component will not be visible in the palette list of the Page Editor

```javascript
super{  {    name: '',     template: '',     designerTemplate: '',    componentLabel: '',     templateUrl: '',    isAdvancedChild: false,     visible: true}  )
```

**Step 6**: Call the addAttribute method of the superclass with the following parameters.

The parameters include:

- **key**: The unique text for the attribute to be replaced inside the template string.
- **value**: The default value of the attribute which gets displayed in the properties window. During template generation, the value field will be replaced according to the attribute type.
- **type**: The type of attribute which determines how the key is replaced during template generation:
  - **a[attribute]**: Searches for the key and replaces it with the default value or the user input in the properties window of a palette component.
  - **kv[key-value]**: Searches for the key and assigns the value to the key key=value.
  - **ma[multiple-attribute]**: Enters multiple attributes if the template of the palette component has multiple key parameters that are supposed to be replaced with the same value.
  - **vk[value-key]**: Provides a unique key for a value in the properties window. For example, #form1=ngForm or #firstName=ngModel. Then, give a unique key as **ngModel** and the user input assigned as value gets added as #value=key.
  - **(optional) dav[dynamic-attribute-value]**: If you want to dynamically generate value for the key, then, there are three events that take a function as a value:
  - The **postSave** event gets fired after a page is saved. For example:
  - Make sure that you return the template at the end of the event.return ("<" + template + ">");
  - The** prerender **event gets fired on the drop of the palette component on the container. For example: Copy CodeJavaScriptsuper.addAttribute(new Attribute({
      key: 'columnId',
      value: '',
      type: 'dav',
      templateUpdater: {
      preRender: () => {
      return new BGuid().generate();
      }
      },
      visible: '',
      isVisibleForParent: ''
      }));
     Make sure that you return the template at the end of the event.return ("<" + template + ">");
  - The **valueChange** event gets fired when an attribute value is changed. For example: Copy CodeJavaScriptsuper.addAttribute(new Attribute({
      key: 'dynamicTab',
      value: 'false',
      type: 'dav',
      templateUpdater: {
      valueChange: (elementValue, attribs) => {
      let componentInstance = this;
      let componentAttribute = componentInstance.getHtmlAttributes(attribs);
      if (elementValue == "dynamic") {
      if (componentAttribute['tabDatasource'] || componentAttribute['tabDatasource']._visibility && componentAttribute['[tabDatasource]']._visibility == false && componentAttribute['tabLabels'] || componentAttribute['tabLabels']._visibility && componentAttribute['tabLabels']._visibility == false) {
      componentAttribute['tabDatasource']._visibility = true;
      componentAttribute['tabLabels']._visibility = true;
      }
      } else if (componentAttribute['tabDatasource'] || componentAttribute['tabDatasource']._visibility && componentAttribute['tabDatasource']._visibility == true && componentAttribute['tabLabels'] || componentAttribute['tabLabels']._visibility && componentAttribute['tabLabels']._visibility == true) {
      componentAttribute['tabDatasource']._visibility = false;
      componentAttribute['tabLabels']._visibility = false;
      }
      return attribs;
      }
      }
      }));
     Make sure that you return the template at the end of the event.return ("<" + template + ">");

- **useAsLabel:** If you want to use the attribute as a label.
- **complexity: **For a component in Neutrinos Studio, attributes can be categorized as **Basic **and **Advanced **properties. By default, all attributes that you provide for a component will appear under **Basic Properties**. If you want to show the attributes under** Advanced Properties**, specify the** complexity **parameter and provide its value as **advanced**.

```javascript
super.addAttribute(  new Attribute({    key, value, type, useAsLabel, complexity  })    );
```

**Step 7 (optional):** By default, the defined attributes of your component will be of type **Input** where you will see a label and an input field in which you give the value for the attribute. For example:

If you want to change the attribute view type to **toggle** or **drop-down** list, perform the following steps:

1. In your studio package, create a folder named **attributeTypes**.
2. In the **attributeTypes** folder, create **<attribute_name>.js** file of each attribute and define the view attribute type. For example, to display the Align attribute of the **Card** component as a drop-down list, add the following code. Here, this.value is the key of the attribute mentioned in your **<component>.js** file.

```javascript
let SchemeInstance = null;module.exports = class scheme {    constructor() {        if (!SchemeInstance) {            SchemeInstance = this;            //set all other default values            this.displayAs = 'Scheme';            this.value = '[scheme]'            this.type = 'DROPDOWN';            this.values = [                { display: "None", value: "", default: true },                { display: "Vivid", value: "'vivid'" },                { display: "Natural ", value: "'natural'"},                { display: "Cool", value: "'cool'" },                { display: "Solar", value: "'solar'" },                { display: "Air", value: "'air'"},                { display: "Aqua", value: "'aqua'"},                { display: "Flame", value: "'flame'"},                { display: "Ocean", value: "'ocean'"},                { display: "Forest", value: "'forest'"},                { display: "Horizon", value: "'horizon'"},                { display: "Neons", value: "'neons'"},                { display: "Picnic", value: "'picnic'"},                { display: "Night", value: "'night'"},                { display: "Night Lights", value: "'nightLights'"}            ];        }        return SchemeInstance;    }}
```

To make the **Show X-Axis Label **attribute appear as a** toggle**, add the following code:

```javascript
let ShowXAxisLabelInstance = null;module.exports = class ShowXAxisLabel {    constructor() {        if (!ShowXAxisLabelInstance) {            ShowXAxisLabelInstance = this;            //set all other default values            this.displayAs = 'Show X-Axis Label';            this.value = '[showXAxisLabel]'            this.type = 'TOGGLE';            this.values = {'true-value':'true', 'false-value': 'false'}        }        return ShowXAxisLabelInstance;    }
```

| ![Information](/resources/Storage/create-a-widget-on-studio-7/info.png) | If you add attribute types for your component, you have to import the same in your** index.js** file. |
| --- | --- |

**Step 8**: Create a get method to accept the template of the advanced component.

**Step 9**: Save the file within the package.

```javascript
const name = "ng-card";    const designerTemplate = `        <ng-card onclick="click(event)" component-label="Card" class="ad-element flex-shrink-0 flex-grow-1">          <ng-card-title n-adv-child></ng-card-title>          <ng-card-subtitle n-adv-child></ng-card-subtitle>          <ng-card-image n-adv-child></ng-card-image>          <ng-card-content n-adv-child></ng-card-content>          <ng-card-action n-adv-child></ng-card-action>          <div  slot="add" class="ad-card-buttons">            <div class="inline-block">              <button id="addcardheader" class="add-child-button flex-column" no-select>Card Header</button>              <button id="addcardtitlegroup" class="add-child-button flex-column" no-select>Card Title Group</button>              <button id="addcardtitle" class="add-child-button flex-column" no-select>Card Title</button>              <button id="addcardsubtitle" class="add-child-button flex-column" no-select>Card Sub-Title</button>            </div>            <div class="inline-block">            <button id="addcardimage" class="add-child-button flex-column" no-select>Card Image</button>            <button id="addcardcontent" class="add-child-button flex-column" no-select>Card Content</button>            <button id="addcardaction" class="add-child-button flex-column" no-select>Card Action</button>            <button id="addcardfooter" class="add-child-button flex-column" no-select>Card Footer</button>            </div>          </div>        </ng-card>`;
```

Refer to these additional topics (at the end of this page) for help on creating the .js file of your advanced component:

- [Define the designerTemplate using slots](/articles/create-a-widget-on-studio-7/create-advanced-component-file/a/h4_148746544)
- [Style the elements inside the slot](/articles/create-a-widget-on-studio-7/create-advanced-component-file/a/h4__981283192)
- [Listen to the HTML events on your element](/articles/create-a-widget-on-studio-7/create-advanced-component-file/a/h4__386328029)
- [Attach children or siblings to the component](/articles/create-a-widget-on-studio-7/create-advanced-component-file/a/h4__1759985169)
- [Share objects between parent and child elements](/articles/create-a-widget-on-studio-7/create-advanced-component-file/a/h4__1727228971)
- [Disable element copy](/articles/create-a-widget-on-studio-7/create-advanced-component-file/a/h4_1043266511)

### Example of an Advanced Component - Card

The parent** Card** component:

```javascript
//This is the parent file"use strict";let AdvancedComponent = require("../../../core/AdvancedComponent");let Attribute = require("../../../core/Attributes");module.exports = class advanceCard extends AdvancedComponent {  constructor() {    const name = "ng-card";    const designerTemplate = `        <ng-card onclick="click(event)" component-label="Card" class="ad-element flex-shrink-0 flex-grow-1">          <ng-card-title n-adv-child></ng-card-title>          <ng-card-subtitle n-adv-child></ng-card-subtitle>          <ng-card-image n-adv-child></ng-card-image>          <ng-card-content n-adv-child></ng-card-content>          <ng-card-action n-adv-child></ng-card-action>          <div  slot="add" class="ad-card-buttons">            <div class="inline-block">              <button id="addcardheader" class="add-child-button flex-column">Card Header</button>              <button id="addcardtitlegroup" class="add-child-button flex-column">Card Title Group</button>              <button id="addcardtitle" class="add-child-button flex-column">Card Title</button>              <button id="addcardsubtitle" class="add-child-button flex-column">Card Sub-Title</button>            </div>            <div class="inline-block">            <button id="addcardimage" class="add-child-button flex-column">Card Image</button>            <button id="addcardcontent" class="add-child-button flex-column">Card Content</button>            <button id="addcardaction" class="add-child-button flex-column">Card Action</button>            <button id="addcardfooter" class="add-child-button flex-column">Card Footer</button>            </div>          </div>        </ng-card>`;    const paletteTemplate = "Card";    const componentLabel = 'Card';    const templateUrl = "https://material.angular.io/components/card/overview";    super({      name,      template: ``,      designerTemplate,      paletteTemplate,      componentLabel,      templateUrl    });    super.setType(AdvancedComponent.COMPONENT_TYPE_TITLES.LAYOUT.val);    super.addAttribute(      new Attribute({        key: 'tabindex',        value: '',        type: 'kv'      })    );    super.composeTemplate({      styles: `      :host {        display: flex;        padding-top: 1em;        padding-bottom: 1em;        min-width: 20em;        flex-direction: column;        align-self: start;      }     .parent_card {       display: flex;       flex-direction: column;    }      `,      slotsTemplate: `         <div class="parent_card">        <slot name="cards"></slot>      </div>      <div class="parent_card">        <slot id="addSlot" name="add"></slot>      </div>      `,      onInit: function () {},      onDestroy: function () {},        customMethods: {        click: function (e) {          if (e.target.id === "addcardheader") {            this.addChild("ng-cardheader");          } else if (e.target.id === "addcardaction") {            this.addChild("ng-card-action");          } else if (e.target.id === "addcardcontent") {            this.addChild("ng-card-content");          } else if (e.target.id === "addcardimage") {            this.addChild("ng-card-image");          } else if (e.target.id === "addcardfooter") {            this.addChild("ng-card-footer");          } else if (e.target.id === "addcardtitle") {            this.addChild("ng-card-title");          } else if (e.target.id === "addcardsubtitle") {            this.addChild("ng-card-subtitle");          } else if (e.target.id === "addcardtitlegroup") {            this.addChild("ng-card-title-group");          }        }      }    });  }  get template() {    const template = `<mat-card %tabindex% %bCustomProps% %style% %class%></mat-card>`;    return template;  }  set template(templateString) {}};
```

**Card sub-components:**

**Copy CodeJavaScript//Card Action

'use strict';
let Attribute = require('../../../core/Attributes');
let AdvancedComponent = require("../../../core/AdvancedComponent");

module.exports = class CardAction extends AdvancedComponent {
 constructor() {
 const name = 'ng-card-action';
 const designerTemplate = ` <ng-card-action slot="cards"
 class=\"drop display-block\" component-label="Card Action" block-copy>
 </ng-card-action>`;
 const paletteTemplate = 'Card Action';
 const componentLabel = 'Card Action';
 const templateUrl = 'https://material.angular.io/components/card/overview';

 super({
 name,
 template: ``,
 designerTemplate,
 paletteTemplate,
 componentLabel,
 isAdvancedChild: true,
 templateUrl
 });

 super.addAttribute(
 new Attribute({
 key: 'align',
 value: '',
 type: 'kv'
 })
 );

 this.template = `
 <mat-card-actions %align% %bCustomProps% %style% %class%></mat-card-actions>
 `;

 super.composeTemplate({
 styles: `:host {
 padding: 1em;
 position: relative;
 min-height: 1em;
 border: 1px solid lightgrey;
 margin: 6px 25px !important;
 border-radius: 5px !important;
 color: black;
 }`
 });
 }
};

// Card Content

'use strict';
let Attribute = require('../../../core/Attributes');
let AdvancedComponent = require("../../../core/AdvancedComponent");

module.exports = class CardContent extends AdvancedComponent {
 constructor() {
 const name = 'ng-card-content';
 const designerTemplate = ` <ng-card-content slot="cards"
 class=\"drop display-block\" component-label="Card Content" block-copy>
 </ng-card-content>`;
 const paletteTemplate = 'Card Content';
 const componentLabel = 'Card Content';
 const templateUrl = 'https://material.angular.io/components/card/overview';

 super({
 name,
 template: ``,
 designerTemplate,
 paletteTemplate,
 componentLabel,
 isAdvancedChild: true,
 templateUrl
 });

 super.addAttribute(
 new Attribute({
 key: 'align',
 value: '',
 type: 'kv'
 })
 );

 this.template = `
 <mat-card-content %align% %style% %class% %bCustomProps%></mat-card-content>
 `;

 super.composeTemplate({
 styles: `:host {
 padding: 1em;
 position: relative;
 min-height: 1em;
 border: 1px solid lightgrey;
 margin: 6px 25px !important;
 border-radius: 5px !important;
 color: black;
 }

 `
 });
 }
};

// Card Footer

'use strict';
let Attribute = require('../../../core/Attributes');
let AdvancedComponent = require("../../../core/AdvancedComponent");

module.exports = class CardFooter extends AdvancedComponent {
 constructor() {
 const name = 'ng-card-footer';
 const designerTemplate = `<ng-card-footer
 class=\"drop display-block\" slot="cards"
 component-label="Card Footer"
 block-copy></ng-card-footer>`;
 const paletteTemplate = 'Card Footer';
 const componentLabel = 'Card Footer';
 const templateUrl =
 'https://material.angular.io/components/card/overview';

 super({
 name,
 template: ``,
 designerTemplate,
 paletteTemplate,
 componentLabel,
 isAdvancedChild: true,
 templateUrl
 });

 super.addAttribute(
 new Attribute({
 key: 'align',
 value: '',
 type: 'kv'
 })
 );

 this.template = `
 <mat-card-footer %align% %bCustomProps% %style%
 %class%></mat-card-footer>
 `;

 super.composeTemplate({
 styles: `:host {
 padding: 1em;
 position: relative;
 min-height: 1em;
 border: 1px solid lightgrey;
 margin: 6px 25px !important;
 border-radius: 5px !important;
 color: black;
 }`
 });
 }
};

// Card Header

'use strict';
let Attribute = require('../../../core/Attributes');
let AdvancedComponent = require("../../../core/AdvancedComponent");

module.exports = class CardHeader extends AdvancedComponent {
 constructor() {
 const name = 'ng-cardheader';
 const designerTemplate = ` <ng-cardheader slot="cards"
 class=\"ad-card-header flex-row display-block\" block-copy>
 <div class=\"ad-card-avatar\"></div>
 <div class="flex-column flex-justify-center padding-1-left">
 <div class=\"ad-card-header-title\">Title</div>
 <div class=\"ad-card-subtitle\">Subtitle</div>
 </div>
 </ng-cardheader>`;
 const paletteTemplate = 'Card Header';
 const componentLabel = 'Card Header';

 const templateUrl =
 'https://material.angular.io/components/card/overview';

 super({
 name,
 template: ``,
 designerTemplate,
 componentLabel,
 paletteTemplate,
 isAdvancedChild: true,
 templateUrl
 });

 this.template = `
 <mat-card-header %bCustomProps% %style% %class%>
 <mat-card-title>%title%</mat-card-title>
 <mat-card-subtitle>%subtitle%</mat-card-subtitle>
 <img mat-card-avatar %imgSecure% %[collectionName]%
 %[imageFilter]% %imgSrc% %[src]% %alt%>
 </mat-card-header>
 `
 super.addAttribute(new Attribute({
 key: 'title',
 value: 'title',
 type: 'a'
 }));
 super.addAttribute(
 new Attribute({
 key: 'subtitle',
 value: 'subtitle',
 type: 'a'
 })
 );
 super.addAttribute(new Attribute({
 key: 'imgSrc',
 value: '',
 type: 'kv'
 }));
 super.addAttribute(new Attribute({
 key: '[src]',
 value: '',
 type: 'kv'
 }));
 super.addAttribute(new Attribute({
 key: 'alt',
 value: '',
 type: 'kv'
 }));
 super.addAttribute(
 new Attribute({
 key: 'imgSecure',
 value: '',
 type: 'a'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[collectionName]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[imageFilter]',
 value: '',
 type: 'kv'
 })
 );
 super.composeTemplate({
 styles: `:host {
 padding: 1em;
 background: white !important;
 position: relative;
 border: 1px solid lightgrey;
 margin: 6px 25px !important;
 border-radius: 5px !important;
 color: #404041;
 }`
 })
 }
};
// Card Image

'use strict';
let Attribute = require('../../../core/Attributes');
let AdvancedComponent = require("../../../core/AdvancedComponent");

module.exports = class CardImage extends AdvancedComponent {
 constructor() {
 const name = 'ng-card-image';
 const designerTemplate = `<ng-card-image slot="cards"
 class=\" display-block ad-card-header flex-row\" block-copy>
 <div class=\"ad-card-avatar\"></div>

 <div class="flex-column flex-justify-center padding-1-left">
 <div class=\"ad-card-header-title ad-card-title-color ad-card-image-text\">Card Image</div>
 </ng-card-image>`;
 const paletteTemplate = 'Card Image';
 const componentLabel = 'Card Image';

 const templateUrl = 'https://material.angular.io/components/card/overview';

 super({
 name,
 template: ``,
 designerTemplate,
 componentLabel,
 paletteTemplate,
 isAdvancedChild: true,
 templateUrl
 });

 super.addAttribute(new Attribute({
 key: 'alt',
 value: '',
 type: 'kv'
 }));
 super.addAttribute(new Attribute({
 key: 'imgSrc',
 value: '',
 type: 'kv'
 }));
 super.addAttribute(new Attribute({
 key: '[src]',
 value: '',
 type: 'kv'
 }));
 super.addAttribute(
 new Attribute({
 key: 'imgSecure',
 value: '',
 type: 'a'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[collectionName]',
 value: '',
 type: 'kv'
 })
 );
 super.addAttribute(
 new Attribute({
 key: '[imageFilter]',
 value: '',
 type: 'kv'
 })
 );

 this.template = `
 <img mat-card-image %imgSecure% %[collectionName]%
 %[imageFilter]% %bCustomProps% %style% %class% %alt% %imgSrc% %[src]%>
 `;

 super.composeTemplate({
 styles: `:host {
 padding: 1em;
 position: relative;
 border: 1px solid lightgrey;
 margin: 6px 25px !important;
 border-radius: 5px !important;
 color: black;
 }

 ::slotted(.card-image-text) {
 position: absolute;
 bottom: 0px;
 text-align: center;
 width: 90%;
 font-size: 14px;
 margin-bottom: 10px;
 color: #404041;
 }
 ::slotted(.ad-card-image) {
 line-height: 40px;
 }
 `
 });
 }
};
// Card Sub-Title
'use strict';
let Attribute = require('../../../core/Attributes');
let AdvancedComponent = require("../../../core/AdvancedComponent");

module.exports = class CardSubTitle extends AdvancedComponent {
 constructor() {
 const name = 'ng-card-subtitle';
 const designerTemplate = `<ng-card-subtitle slot="cards"
 block-copy class="display-block">
 <span class="component-placeholder title-align">Card Sub-Title</span>
 </ng-card-subtitle>`;
 const paletteTemplate = 'Card Sub-title';
 const componentLabel = 'Card Sub-title';

 const templateUrl = 'https://material.angular.io/components/card/overview';

 super({
 name,
 template: ``,
 designerTemplate,
 componentLabel,
 paletteTemplate,
 isAdvancedChild: true,

 templateUrl
 });

 super.addAttribute(
 new Attribute({
 key: 'Sub Title',
 value: 'Card Sub-Title',
 type: 'a',
 useAsLabel: true,
 isVisibleForParent:true
 })
 );
 super.addAttribute(new Attribute({
 key: 'align',
 value: '',
 type: 'kv',
 }));

 this.template = `
 <mat-card-subtitle %align%>%Sub Title%</mat-card-subtitle>
 `;

 super.composeTemplate({
 styles: `:host {
 padding: 1em;
 position: relative;
 border: 1px solid lightgrey;
 margin: 6px 25px !important;
 border-radius: 5px !important;
 }`
 });
 }
};

// Card Title

'use strict';
let Attribute = require('../../../core/Attributes');
let AdvancedComponent = require("../../../core/AdvancedComponent");

module.exports = class CardTitle extends AdvancedComponent {
 constructor() {
 const name = 'ng-card-title';
 const designerTemplate = `<ng-card-title slot="cards"
 block-copy class="display-block">
 <span class="component-placeholder title-align">Card Title</span>
 </ng-card-title>`;
 const paletteTemplate = 'Card Title';
 const componentLabel = 'Card Title';

 const templateUrl = 'https://material.angular.io/components/card/overview';

 super({
 name,
 template: ``,
 designerTemplate,
 componentLabel,
 paletteTemplate,
 isAdvancedChild: true,
 templateUrl
 });

 super.addAttribute(
 new Attribute({
 key: 'Title',
 value: 'Card Title',
 type: 'a',
 useAsLabel: true,
 })
 );
 super.addAttribute(new Attribute({
 key: 'align',
 value: '',
 type: 'kv',
 }));

 this.template = `
 <mat-card-title %align%>%Title%</mat-card-title>
 `;
 super.composeTemplate({
 styles: `:host {
 padding: 1em;
 position: relative;
 min-height: 1em;
 border: 1px solid lightgrey;
 margin: 6px 25px !important;
 border-radius: 5px !important;
 color: black;
 }`
 });
 }
};
// Card Title Group

'use strict';
let Attribute = require('../../../core/Attributes');
let AdvancedComponent = require("../../../core/AdvancedComponent");

module.exports = class CardHeader extends AdvancedComponent {
 constructor() {
 const name = 'ng-card-title-group';
 const designerTemplate = ` <ng-card-title-group slot="cards" class=\"display-block flex-row\" block-copy>
 <div class="flex-column flex-start flex-grow-1 padding-1-left">
 <div class=\"ad-card-header-title\">Title</div>
 <div class=\"ad-card-subtitle\">Subtitle</div>
 </div>
 <div class=\"ad-card-title-group ad-card-avatar flex-end flex-grow-1\"></div>
 </ng-card-title-group>`;
 const paletteTemplate = 'Card Title Group';
 const componentLabel = 'Card Title Group';

 const templateUrl = 'https://material.angular.io/components/card/overview';

 super({
 name,
 template: ``,
 designerTemplate,
 componentLabel,
 paletteTemplate,
 isAdvancedChild: true,
 templateUrl
 });

 this.template = `
 <mat-card-title-group %bCustomProps% %style% %class%>
 <mat-card-title>%title%</mat-card-title>
 <mat-card-subtitle>%subtitle%</mat-card-subtitle>
 %imageType%
 </mat-card-title-group>
 `
 super.addAttribute(new Attribute({
 key: 'title',
 value: 'Title',
 type: 'a'
 }));

 super.addAttribute(
 new Attribute({
 key: 'subtitle',
 value: 'Subtitle',
 type: 'a'
 })
 );

 super.addAttribute(new Attribute({
 key: 'imgSrc',
 value: '',
 type: 'kv'
 }));

 super.addAttribute(new Attribute({
 key: '[src]',
 value: '',
 type: 'kv'
 }));

 super.addAttribute(new Attribute({
 key: 'alt',
 value: '',
 type: 'kv'
 }));

 super.addAttribute(
 new Attribute({
 key: 'imgSecure',
 value: '',
 type: 'a'
 })
 );

 super.addAttribute(
 new Attribute({
 key: '[collectionName]',
 value: '',
 type: 'kv'
 })
 );

 super.addAttribute(
 new Attribute({
 key: '[imageFilter]',
 value: '',
 type: 'kv'
 })
 );

 super.addAttribute(new Attribute({
 key: 'imageType',
 value: 'sm',
 type: 'dav',
 isVisibleForParent: true,
 templateUpdater: {
 postSave: (value, x, componentAttributes) => {
 let template;
 if (value == "sm") {
 template = `img mat-card-sm-image`
 } else if (value == "md") {
 template = `img mat-card-md-image`
 } else if (value == "lg") {
 template = `img mat-card-lg-image`
 }
 if (componentAttributes[4]._value) {
 template = template + " imgSrc" + '=' + '"' + componentAttributes[4]._value + '"';
 }
 if (componentAttributes[5]._value) {
 template = template + " [src]" + '=' + '"' + componentAttributes[5]._value + '"';
 }
 if (componentAttributes[6]._value) {
 template = template + " alt" + '=' + '"' + componentAttributes[6]._value + '"';
 }
 if (componentAttributes[7]._value) {
 template = template + " isSecure" + '=' + '"' + componentAttributes[7]._value + '"';
 }
 if (componentAttributes[8]._value) {
 template = template + " [collectionName]" + '=' + '"' + componentAttributes[8]._value + '"';
 }
 if (componentAttributes[9]._value) {
 template = template + " [imageFilter]" + '=' + '"' + componentAttributes[9]._value + '"';
 }
 return ("<" + template + ">");
 }
 }
 }));

 super.composeTemplate({
 styles: `:host {
 padding: 1em;
 background: white !important;
 position: relative;
 border: 1px solid lightgrey;
 margin: 6px 25px !important;
 border-radius: 5px !important;
 color: #404041;
 }`
 })
 }
};
**

**Help Sections:**

For additional information on creating advanced components, refer to the sections below:

#### Define the designerTemplate using Slots

Slots are visible portions of the designerTemplate that will be viewable once you drop the element on the container. With slots, you can control where your elements will appear on the view. By default, all the elements that are coded to the designerTemplate will be visible to you via the default slot. For example, in this slotsTemplate there are four slots for filter, columns, paginator, and buttons:

```html
<div class="columns_parent">  <slot name="table-filter" id="columns_slot"></slot></div>    <div class="columns_parent">  <slot name="column" id="columns_slot"></slot></div>    <div class="columns_parent">  <slot name="paginator" id="columns_slot"></slot></div>    <div class="columns_parent">  <slot id="addSlot" name="add"></slot></div>
```

By default, any element can get attached in the default slot. To attach your element to the slot, declare it as part of the slot with a slot name. For example:

```html
<!-- This element will always get attached to the "column" slot !--><ng-table-column slot="column" block-copy>  <span class="component-placeholder">Column</span></ng-table-column>
```

#### Style the Elements Inside the Slot

Styles of an advanced component are encapsulated within the element. To style the elements that are inside the slots, you can wrap the slot with the <div> tag and apply your styles. These styles will reflect on the elements inside the slot. You can also query slotted elements using ::slotted() syntax. Or, if you want to style the element itself, you can use the :host.

```css
:host {        background: #fff;        border-radius: 2px;        display: flex;        position: relative;        box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);        border: 1px solid lightgray;        flex-direction: column;      }      #addSlot::slotted(.table-button) {        font-family: "Roboto medium", sans-serif;        font-size: 14px;        display: inline-block;        height: 36px;        min-width: 88px;        padding: 6px 16px;        line-height: 1.42857143;        text-align: center;        white-space: nowrap;        vertical-align: middle;        -ms-touch-action: manipulation;        touch-action: manipulation;        cursor: pointer;        -webkit-user-select: none;        -moz-user-select: none;        -ms-user-select: none;        user-select: none;        border: 0;        border-radius: 2px;        outline: 0;        font-size: 0.7em;        margin: 0.3em !important;     }     #button-list {      padding: 0.3em 0em;     }     .columns_parent {       display: flex;       flex-direction: row;     }
```

#### Listen to the HTML Events on your Element

You can listen to all the HTML events on your element and call your custom methods for the operations that you want to perform. For example, to perform custom operations on listening to the click events on the elements:

#### Attach Children or Siblings to the Component

There are three in-built methods to attach child elements to its parent element:

- The addChild method adds all the elements as children of the parent element. All the child elements will be generated inside the parent template.
- The attachSiblingBefore method adds all the elements that will be generated before the template
- The attachSiblingAfter method adds all the elements that will be generated after the template.

```javascript
/** * addChild method takes the name of the element in lowercase for attaching * it as child to the element. Eg: Attach column inside the table  */this.addChild("ng-table-column");/** * attachSiblingAfter method takes the name of the element * in lowercase for attaching * it as sibling after the element in the generated template. * Eg: Attach paginator after the table  */this.attachSiblingAfter('ng-table-paginator');/** * attachSiblingBefore method takes the name of the element * in lowercase for attaching * it as sibling before the element in the generated template. * Eg: Attach paginator before the table  */this.attachSiblingBefore('ng-table-filter');
```

#### Share Objects Between Parent and Child Elements

Each template has a shared object, which is shared between the parent and child elements during the run time. The shared object can be set to anything, during page save event calls, which can be accessed during the template get method to generate the required template for the page.

```javascript
get template() {    let displayColumns = this.shared      && this.shared.displayColumns ? this.shared.displayColumns : "";    displayColumns = JSON.stringify(displayColumns).replace(new RegExp("\"", 'g'), "'");    return `    <div fxLayout="column">      <table mat-table %[dataSource]%        %bCustomProps% {{CODE_HLITED}}amp;lt;/span>{this.shared.matSort ? this.shared.matSort : ""}        fxFlex="100">        ~%ng-table-header%~        <tr mat-row *matRowDef="let row; columns: ${displayColumns};"></tr>      </table>    </div>    `;  }
```

Apart from the template get and set methods, These are the events that can be utilized to populate the shared object during page save:

- Parent element's toChildren event: to get the current parent instance, and assign any value to the shared object for its children.
- Child element's toParent event: to get the current parent instance, and assign any value to the shared object from its children.
- Child element's fromParent event: to get the current parent instance, and get any value from its parent element.

Parent elements are iterated before child elements, so the parent event will fire first.

```javascript
toParent(parentInstance) {  if (!(parentInstance.shared.displayColumns instanceof Array)) {    parentInstance.shared.displayColumns = [];  }  for (let i = 0; i < this.htmlAttributes.length; i++) {    if (this.htmlAttributes[i]._key === 'Mapping'      && typeof this.htmlAttributes[i]._value === 'string') {      parentInstance.shared.displayColumns.push(this.htmlAttributes[i]._value.replace('table.', ''))    }    if (this.htmlAttributes[i]._key === 'matSortHeaderColumn'      && this.htmlAttributes[i]._value) {      parentInstance.shared.matSort = "matSort";    }  }  return parentInstance;}
```

#### Disable Element Copy

If you do not want an element to be copied, use the block-copy attribute.

```javascript
<!-- Individual columns are not copyable!--><ng-table-column slot="column" block-copy>    <span class="component-placeholder">Column</span></ng-table-column>
```
