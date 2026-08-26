# Update the weathercard page

<https://documentation.neutrinos.com/articles/#!tutorial-integrate-your-app-with-apis/create-services>

After creating the Modelr flow and the UI service, you call them from the app pages.

### Update the weathercard page

Open the** weathercard** page and double-click the column as highlighted below to open its attributes window.

 ![The column in weathercard page](/resources/Storage/tutorial-integrate-your-app-with-apis/wc_col.png)



 Create a custom property ***ngFor** under custom properties (as** Key & Value **property) and assign it the following value:


 let w of weatherdata?.weather; let i = index


 ![Setting the ngfor property](/resources/Storage/tutorial-integrate-your-app-with-apis/ngfor.png)




 Open the **TS** editor of the **weathercard **page.


 Import the UI service that you created and inject the service in the constructor as **weatherservice**. Now, you can call the flows in the weather service.


 Copy CodeJavaScript//Importing the UI service
import { weatherservice } from '../../sd-services/weatherservice';
...
...
//Injecting the weatherservice in the constructor
constructor(private bdms: NDataModelService,
 public weatherService: weatherservice) {
 super();
 this.mm = new ModelMethods(bdms);
 }




 Define the **getWeatherModelr** function. The flow returns a bh object with output properties. Which in this case, is the local property - currentweather. Set this property to the page's property **weatherdata**.

 Copy CodeJavaScriptasync getWeatherModelr(cityName) {
 try {
 this.weatherdata = (await this.weatherService.getWeatherModelr(cityName)).local.currentWeather;
 this.processWeather(cityName);
 } catch (e) {
 this.res.emit({
 type: 'error',
 message: typeof e.message === 'string' ? e.message : 'Error Occured While Retrieving the Weather Data.'
 });
 }
 }


 **Page Implementation**


 Copy CodeJavaScript/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import { Component, OnInit, Input, OnChanges, Output } from '@angular/core'
import { ModelMethods } from '../../lib/model.methods';
// import { BDataModelService } from '../service/bDataModel.service';
import { NDataModelService } from 'neutrinos-seed-services';
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { weatherservice } from '../../sd-services/weatherservice';
import { EventEmitter } from '@angular/core';
import { logobject } from 'app/models';
/**
 * Service import Example :
 * import { HeroService } from '../../services/hero/hero.service';
 */

/**
*
* Service Designer import Example - Service Name - HeroService
* import { HeroService } from 'app/sd-services/HeroService';
*/


@Component({
 selector: 'bh-weathercard',
 templateUrl: './weathercard.template.html'
})

export class weathercardComponent extends NBaseComponent implements OnInit {
 mm: ModelMethods;
 @Output('log') res: EventEmitter<logobject> = new EventEmitter<logobject>();
 weatherdata: any;
 localStorage = localStorage;
 showCard = false;
 constructor(private bdms: NDataModelService,
 public weatherService: weatherservice) {
 super();
 this.mm = new ModelMethods(bdms);
 }

 ngOnInit() {
 }

 async getWeatherModelr(cityName) {
 try {
 this.weatherdata = (await this.weatherService.getWeatherModelr(cityName)).local.currentWeather;
 this.processWeather(cityName);
 } catch (e) {
 this.res.emit({
 type: 'error',
 message: typeof e.message === 'string' ? e.message : 'Error Occured While Retrieving the Weather Data.'
 });
 }
 }

 async processWeather(cityName) {
 if (typeof this.weatherdata === 'object' && Object.keys(this.weatherdata).length > 0) {
 this.showCard = true;
 localStorage.lastCity = cityName;
 this.res.emit({
 type: 'info',
 message: 'Successfully Retrieved the Weather Data for city: ' + cityName
 });
 } else {
 this.showCard = false;
 this.res.emit({
 type: 'info',
 message: 'Weather Data is Empty for city: ' + cityName
 });
 }
 }

}

### Update the weathersearch page

1. Open the **weathersearch **page.
2. Double-click the **Get weather** button to open its attributes window.
    ![The get weather button](/resources/Storage/tutorial-integrate-your-app-with-apis/get_weather_btn.png)
3. On the click of this button, the app should call the Modelr flow that we created in [Create a Flow in Neutrinos Modelr](/articles/tutorial-integrate-your-app-with-apis/modeler-flow). To do that, add the following value to the (click) property:
    weatherView.getWeatherModelr(searchString).
4. Double-click the **weathercard** view in the **weathersearch **page and update the log (output) property value to updateLog($event)under the advanced properties section.
    ![The get weather button](/resources/Storage/tutorial-integrate-your-app-with-apis/wea_card.png)
5. Double-click the **log** view in the **weathersearch** page and update the  logArray (Input) property value to logArray. If you see the **property not available **error, the error will be solved later when the **logArray** function is defined in the TS editor of the log page. ![weather search page](/resources/Storage/tutorial-integrate-your-app-with-apis/wea_search.png)
6. Click the **TS** tab of the **weathersearch** page and validate the existing code with the following code:

```javascript
/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/import { Component, OnInit, ViewChild, ElementRef } from '@angular/core'import { ModelMethods } from '../../lib/model.methods';// import { BDataModelService } from '../service/bDataModel.service';import { NDataModelService } from 'neutrinos-seed-services';import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';import { HttpClient } from '@angular/common/http';/** * Service import Example : * import { HeroService } from '../../services/hero/hero.service'; *//*** * Service Designer import Example - Service Name - HeroService* import { HeroService } from 'app/sd-services/HeroService';*/@Component({    selector: 'bh-weathersearch',    templateUrl: './weathersearch.template.html'})export class weathersearchComponent extends NBaseComponent {    mm: ModelMethods;    searchString: string;    logArray = [];    constructor(private bdms: NDataModelService,        private http: HttpClient) {        super();        this.mm = new ModelMethods(bdms);    }    updateLog(logObject) {        this.logArray.push(logObject);    }}
```

### Update the log page

1. Open the **log** page.
2. Double-click the **slide-toggle** component to open its attributes window and update the (change) property value to toggleLogVisibility($event).
    ![The slide toggle button](/resources/Storage/tutorial-integrate-your-app-with-apis/slide_tooggle.png)
3. Double-click the **HTML 5- div** component to open its attributes window and add the following custom properties (as** Key & Value **property) and assing the following values:
    **Property**
    **Value**
    *ngFor
    let logObj of logArray; let i = index
    [ngStyle]
    {'color': logObj.type === 'error' ? 'red' : 'green'}
   ![Log attributes](/resources/Storage/tutorial-integrate-your-app-with-apis/log_attributes.png)
4. Double-click the **HTML Editor** of the **HTML5-div** component and add the following code:
    {{'- ' + logObj.message}}
    ![The HTML editor](/resources/Storage/tutorial-integrate-your-app-with-apis/html5-div.png)
