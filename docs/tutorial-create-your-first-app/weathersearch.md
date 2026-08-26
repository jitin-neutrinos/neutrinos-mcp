# Layout

<https://documentation.neutrinos.com/articles/#!tutorial-create-your-first-app/weathersearch>

This page is used to create a weather card that shows the weather information returned from the server for every API endpoint.

The** wearthercard** and **log pages** are added as [views](/articles/project-concepts/page-elements) to this page.

### Layout

Drag and drop various components and create the following layout

![weathersearch layout](/resources/Storage/tutorial-create-your-first-app/weathersearch.png)

### Properties

![weathersearch 1](/resources/Storage/tutorial-create-your-first-app/weathersearch1.png)

**Row 1**

**Basic Properties**

- **Style:** height:100%;
- **Layout direction: **Center
- **Perpendicular Direction: **Start

---

**Column 1**

**Basic properties**

- **Perpendicular Direction: **none

---

**Form 1**

**Basic Properties**

- **Style:** margin-bottom:0 !important;

**Custom properties**

- **#weatherForm: **ngForm

![](/resources/Storage/tutorial-create-your-first-app/form_ng.png)

---

![weatersearch 2](/resources/Storage/tutorial-create-your-first-app/weathersearch%202.png)

**Row 2**

**Basic Properties**

- **Style:** width:500px;
- **Layout direction: **Space-between
- **Perpendicular Direction:** center

---

**Input 1**

**Basic Properties**

- **Style:** flex-basis:75%;
- **place holder: **Enter city name
- **Form field appearance:** outline
- **[(ngModel)]:** searchString
- **name: **searchIp

**Custom Properties**

- **autocomplete:** off
- **#searchIp:** ngModel

![](/resources/Storage/tutorial-create-your-first-app/input_auto.png)

---

**Raised Button 1**

**Basic Properties**

- **class:** get-weather-button
- **buttonname:** Get weather
- **(click): **weatherView.getWeatherModelr(searchString)
- **Disabled:** searchlp?.invalid
- **type:** submit

---

### weathercard and log views

In the **weathersearch** page, expand the **Views** section of the palette list. Drag and drop the **weathercard** and **log** views to the page.

![](/resources/Storage/tutorial-create-your-first-app/weather_view.png)

---

#### Weather card view - Advanced properties

- **log(Output):** updateLog($event)

#### Weather card view - Custom Properties

In the custom properties section, select the **Attribute** button and enter #weatherView .

![](/resources/Storage/tutorial-create-your-first-app/weather_view_1.png)

---

**Log view**

**Advanced properties**

- **logArray****(****Input) **: logArray

---

### Page Implementation

```javascript
/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/import { Component, OnInit ,ViewChild, ElementRef} from '@angular/core'//import { ModelMethods } from '../../lib/model.methods';// import { BDataModelService } from '../service/bDataModel.service';import { NDataModelService } from 'neutrinos-seed-services';import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';import { HttpClient } from '@angular/common/http';/** * Service import Example : * import { HeroService } from '../../services/hero/hero.service'; */ /** *  * Serivice Designer import Example - Service Name - HeroService * import { HeroService } from 'app/sd-services/HeroService'; */@Component({    selector: 'bh-weathersearch',    templateUrl: './weathersearch.template.html'})export class weathersearchComponent extends NBaseComponent implements OnInit {    searchString: string;    logArray = [];    constructor(private http: HttpClient) {        super();    }    ngOnInit() {    }    updateLog(logObject) {        this.logArray.push(logObject);    }   }
```
