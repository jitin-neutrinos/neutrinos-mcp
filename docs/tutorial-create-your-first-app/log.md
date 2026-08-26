# Layout

<https://documentation.neutrinos.com/articles/#!tutorial-create-your-first-app/log>

This page is used to log the success and failure of the API call while fetching the weather data.

### Layout

Open the **log** page. Drag various components and create the following layout.

### Properties

Use the following tables to configure properties for each component in the layout of this page.

**Row-1**

**Basic properties**

- **Style: **padding:10px;
- **Layout Direction: **space-between
- **Perpendicular direction:** center

---

**Html5-1**

**Basic properties**

- **Style:** font-size:1em;font-weight:bold;
- **Element Type**: Div

Double click the **HTML editor** and enter **Log**.

---

**Slide Toggle-1**

**Basic properties**

- **Slide toggle label: **toggle log visibility
- **text: **toggle log visibility
- **Label Position: **before
- **(change): **toggleLogVisibility($event)
- **checked:** true
- **Disabled: **False
- **Disable Drag Value: **False
- **Disable Ripple:** False
- **Disable Toggle Value:** False

---

![log 2 of the layout](/resources/Storage/tutorial-create-your-first-app/log2.png)

**Column-2**

**Basic properties**

- **Style: **width:500px;
- **fxLayoutGap: **5px
- **Perpendicular Direction: **Start

**Custom properties**

In the custom properties section, select the **Key&Value** button and enter the values from the table respectively and click the **Add **button.

***ngIf:** showLog

---

**Html5- 2**

**Basic properties**

- **Style: **font-size:0.8em; margin-top:10px

**Custom Properties**

IIn the custom properties section, select the Key&Value button and enter the values from the table respectively.

- ***ngFor:** let logObj of logArray; let i = index
- **[ngStyle]:** {'color': logObj.type === 'error' ? 'red' : 'green'}

Double click the HTML editor and enter {{'- ' + logObj.message}}.

---

### Page Implementation

Open the TS editor of the **log** page and enter the following code.

```javascript
/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/import { Component, OnInit , Input } from '@angular/core'//import { ModelMethods } from '../../lib/model.methods';// import { BDataModelService } from '../service/bDataModel.service';import { NDataModelService } from 'neutrinos-seed-services';import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';/** * Service import Example : * import { HeroService } from '../../services/hero/hero.service'; */ /** *  * Serivice Designer import Example - Service Name - HeroService * import { HeroService } from 'app/sd-services/HeroService'; */@Component({    selector: 'bh-log',    templateUrl: './log.template.html'})export class logComponent extends NBaseComponent implements OnInit {    @Input()logArray = [];    showLog = true;    constructor() {        super();    //this.mm = new ModelMethods(bdms);    }    ngOnInit() {    }         toggleLogVisibility(event) {                this.showLog = event.checked;             }}
```
