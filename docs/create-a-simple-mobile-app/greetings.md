# greetings

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/greetings>

The **greetings **page is used to display the weather of a city based on your mobile's GPS location. It is part of the **Home** page and looks the same.![Greetings page](/resources/Storage/create-a-simple-mobile-app/Screenshot_2020_0504_143838.jpg)
 Layout

 Drag various components to create the following layout of the **greetings **page:
 ![greetings layout](/resources/Storage/create-a-simple-mobile-app/greetings.png)**Properties**
 Use the following tables to configure properties for the **Greetings** page:
 ![greetings 1](/resources/Storage/create-a-simple-mobile-app/greetngs1.png)**Column -1****Basic Properties****Class**: hundred-height**Layout Direction**: Start**Perpendicular Direction:** Stretch**fxshow**: true**fxhide**: false**Wrap**: NoWrap**Custom Properties****Layout Fill**: fxFill**COLUMN-2****Basic Properties****Layout Direction**: Start**Perpendicular Direction:** Stretch**fxshow:** true**fxhide**: false**wrap:** wrap**fxFlex:** 75

Card-1Basic Properties**Class**: card-font, red-background

**Custom Properties**

- **fxFlex: ****100**

---

**CARD Image-1**

**Basic properties**

- **Assets Src: ** /Web/Icons/clouds2.jpeg

**CARD Title-1**

**Basic properties**

- **Title:** Greeting!

![greetings 2](/resources/Storage/create-a-simple-mobile-app/greetings%202.png)

**Card content 1**

**Basic Properties**

- **A****lign**: Left

---

**Row 1**

**Basic Properties**

- **Layout Direction:** Start
- **Perpendicular Direction**: End
- **fxShow:** true
- **fxhide:** false
- **fxFlex:** 100

**Custom Properties**

- ***ngIf:** currentWeather

**Column 3****Basic Properties****Style**: font-weight: normal;**fxFlex:** 60**Layout Direction**: End**Perpendicular Direction**: Start

---

**Html5-1**

**Basic Properties**

- **Style**: font-size: 3.125em;font-weight: normal
- **Element type**: Caption

Double click the HTML editor and enter {{currentWeather.main.temp + '&degc'}}

**Html5-2**

**Basic Properties**

- **Style**: font-size: 1em;font-weight: normal
- **Element Type**: Header 2

Double click the HTML editor and enter {{currentWeather.weather[0].description | uppercase}}

**Html5-3**

**Basic Properties**

- **Styl****e**: font-size: 1.5em; font-weight: normal
- **Element type**: Caption

Double click the HTML editor and enter {{currentWeather.name}}

---

**Grid List-1**

** Basic Properties**

- **Cols**: 2
- **rowheight**: 2em
- **gutterSize**: 1em

**Custom properties**

- **fxFlex**: 40

**Column 4****Basic Properties****Layout Direction**: Start**Perpendicular Direction**: End

**Custom properties**

- ***ngFor**: let m of currentWeatherDisplay;

---

**Grid Title 1**

**Basic Properties**

- **Style**: font-weight: normal;padding-right:1em;
- **label:** {{m.displayName}}

---

**Grid Title 2**

**Basic Properties**

- **Style**: font-weight: normal;padding-left:1em;
- **label**: {{m.value}}

![greetings 3](/resources/Storage/create-a-simple-mobile-app/greetings%203.png)**Column 5****Basic Properties****fxFlex:** 25**Layout Direction**: Center**Perpendicular Direction:** Stretch

---

**Row 2**

**Basic Properties**

- **Layout Direction**: Center
- **Perpendicular Direction**: Center
- **fxshow**: true
- **fxhide**: false
- **Wrap**: wrap

---

**Column 6**

**Basic Properties**

- **Style**: padding-top:1em;
- **Layout Direction**: center
- **Perpendicular Direction**: center

**Fab button 1****Basic Properties****fabicon**: camera**Color**: Warn**(click)**: scanDoc()**Disabled:** false**HTML5- 4******Basic Properties******Style**: font-weight:normal;**Element Type**: Header 4

Double click the HTML editor and enter Scan

---

Page implementation
 Replace the code in the **TS** editor tab of the current page in the studio with the below code.Copy CodeJavaScript/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import { Component, OnInit, NgZone } from '@angular/core'
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { location } from 'app/sd-services/location';
import { weather } from 'app/sd-services/weather';
import { NPubSubService } from 'neutrinos-seed-services';
import { ocr } from 'app/sd-services/ocr';

/*
Client Service import Example:
import { servicename } from 'app/sd-services/servicename';
*/

/*
Legacy Service import Example :
import { HeroService } from '../../services/hero/hero.service';
*/

@Component({
 selector: 'bh-greetings',
 templateUrl: './greetings.template.html'
})

export class greetingsComponent extends NBaseComponent implements OnInit {

 coordinates;
 currentWeather;
 currentWeatherDisplay = [];

 constructor(private ocrRunner: ocr,
 private loc: location,
 private w: weather,
 private pubsub: NPubSubService,
 private ngZone: NgZone
 ) {
 super();
 }

 async ngOnInit() {
 this.pubsub.$sub('getloc-complete', async () => {
 this.ngZone.run(async () => {
 this.coordinates = this.loc.loc;
 this.currentWeather = (await this.w.getWeather(this.coordinates.coords.latitude, this.coordinates.coords.longitude)).local.currentWeather;
 this.mapCurrentWeather();
 console.log(this.currentWeather)
 })
 })
 await this.loc.getCurrentLocation();
 }

 mapCurrentWeather() {
 let main = this.currentWeather.main;
 if (main) {
 this.currentWeatherDisplay[0] = {
 displayName: 'Feels Like',
 value: main.feels_like + ' ℃'
 }

 this.currentWeatherDisplay[1] = {
 displayName: 'Humidity',
 value: main.humidity + '%'
 }

 this.currentWeatherDisplay[2] = {
 displayName: 'Pressure',
 value: main.pressure + ' bar'
 }

 this.currentWeatherDisplay[3] = {
 displayName: 'Temperature',
 value: main.temp + ' ℃'
 }

 this.currentWeatherDisplay[4] = {
 displayName: 'Temp. Max.',
 value: main.temp_max + ' ℃'
 }

 this.currentWeatherDisplay[5] = {
 displayName: 'Temp. Min.',
 value: main.temp_min + '℃'
 }
 }
 }

 async scanDoc() {
 await this.ocrRunner.scanPanCard();
 }
}
![Information](/resources/Storage/create-a-simple-mobile-app/info.png)
 Make sure you copy and paste the Complete** page implementation** in the TS editor of the page.
