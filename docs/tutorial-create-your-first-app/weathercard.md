# Layout

<https://documentation.neutrinos.com/articles/#!tutorial-create-your-first-app/weathercard>

This page is used to create a weather card that shows the weather information returned from the **Openmapweather** API provider.

### Layout

Drag and drop various components and create the following layout.

![The layout of weather card page](/resources/Storage/tutorial-create-your-first-app/weathercard.png)

### Properties

Use the following tables to configure properties for the **weathercard** page:

![weather card page layout properties 1](/resources/Storage/tutorial-create-your-first-app/weathercard1.png)

**Row-1**

**Basic properties**

- **Style: height:**100%;
- **Layout direction:** Center
- **Perpendicular Direction: **Start

---

**Column 1**

**Basic properties**

- **Perpendicular Direction:** None

---

**Card 1**

**Basic properties**

- **Style: **width:500px;

**Custom properties - Key & Value**

- ***ngIf:** showCard

![](/resources/Storage/tutorial-create-your-first-app/card_ngif.png)

---

**Card Title 1**

**Basic properties**

- **Title:** {{localStorage.lastCity+ ' weather summary' | titlecase}}
- **Align:** Center

![weathercard layout properties 2](/resources/Storage/tutorial-create-your-first-app/weathercard2.png)

**Row 2**

**Basic properties**

- **fxLayoutGap: **5px
- **Layout Direction: **space-evenly

---

**Column 2**

**Basic properties**

- **Class: **weathers
- **Wrap: **NoWrap
- **Perpendicular Direction:** center

**Custom properties**

- ***ngFor: **let w of weatherdata?.weather; let i = index
- **datasource: **weatherdata
- **option: **w

![](/resources/Storage/tutorial-create-your-first-app/col_ngfor.png)

---

**Image 1**

**Basic properties**

- **[src]:** 'http://openweathermap.org/img/w/' + w.icon + '.png'
- **Secure URI:** False

---

**HTML5- 2**

**Basic properties**

- **Element Type: **Paragraph

Double-click the HTML editor and enter {{w.description}} in the editor space.

![](/resources/Storage/tutorial-create-your-first-app/html5_desc.png)

---

![weathercard page layout properties 3](/resources/Storage/tutorial-create-your-first-app/weathercard3.png)

**Card Content 2**

**Basic Properties**

- **Align: **Center

---

**Grid List 1**

**Basic Properties**

- **cols:** 2
- **gutterSize:** 5px
- **rowHeight: **50px

---

**Column 3**

**Custom Properties**

- ***ngFor: **let m of weatherdata?.main | keyvalue

![](/resources/Storage/tutorial-create-your-first-app/col_ngif.png)

---

![weathercard layout properties 4](/resources/Storage/tutorial-create-your-first-app/weathercard4.png)

**Grid Tile 1**

**Basic properties**

- **label: **{{m.key | titlecase}}

---

**Grid Tile 2**

**Basic Properties**

- **label:** {{m.value + (m.key.includes('temp')?'°C': " ")}}

---

### Page Implementation

Open the TS editor of the weathercard page and paste this code.

```javascript
/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/import { Component, OnInit, Input, OnChanges, Output } from '@angular/core'//import { ModelMethods } from '../../lib/model.methods';// import { BDataModelService } from '../service/bDataModel.service';import { NDataModelService } from 'neutrinos-seed-services';import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';import { weatherservice } from '../../sd-services/weatherservice';import { EventEmitter } from '@angular/core';import { logobject } from 'app/models';/** * Service import Example : * import { HeroService } from '../../services/hero/hero.service'; *//*** * Serivice Designer import Example - Service Name - HeroService* import { HeroService } from 'app/sd-services/HeroService';*/@Component({    selector: 'bh-weathercard',    templateUrl: './weathercard.template.html'})export class weathercardComponent extends NBaseComponent implements OnInit {    //mm: ModelMethods;    @Output('log') res: EventEmitter<logobject> = new EventEmitter<logobject>();    weatherdata: any;    localStorage = localStorage;    showCard = false;    constructor(//private bdms: NDataModelService,        public weatherService: weatherservice) {        super();        //this.mm = new ModelMethods(bdms);    }    ngOnInit() {    }    async getWeatherModelr(cityName) {        try {            this.weatherdata = (await this.weatherService.getWeather(cityName)).local.currentWeather;        } catch (e) {            this.weatherdata = {};            this.res.emit({                type: 'error',                message: typeof e.message === 'string' ? e.message : 'Error Occured While Retrieving the Weather Data.'            });        }        this.processWeather(cityName);    }    async processWeather(cityName) {        if (typeof this.weatherdata === 'object' && Object.keys(this.weatherdata).length > 2) {            this.showCard = true;            this.localStorage.lastCity = cityName;            this.res.emit({                type: 'info',                message: 'Successfully Retrieved the Weather Data for city: ' + cityName            });        } else {            this.showCard = false;            this.res.emit({                type: 'error',                message: `Weather Data Not Found${cityName ? ` For the City: ${cityName}` : ''}!`            });        }    }}
```
