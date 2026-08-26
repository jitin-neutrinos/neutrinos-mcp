# Layout

<https://documentation.neutrinos.com/articles/#!psd-tutorial-publication/weathersearch-page-ui>

### Layout

Open the UI designer of the **weathersearch** page. Drag and drop various components to the canvas and create the following layout:

![weathersearch layout](/resources/Storage/psd-tutorial-publication/weathersearch.png)

### Properties

![weathersearch 1](/resources/Storage/psd-tutorial-publication/weathersearch1.png)

**Row 1**

**Basic Properties**

- **Style:** height:100%;
- **Layout direction: **Center
- **Perpendicular Direction: **Start

**Column 1**

**Basic properties**

- **Perpendicular Direction: **none

**Form 1**

**Basic Properties**

- **Style:** margin-bottom:0 !important;

**Custom properties**

- **#weatherForm: **ngForm

![](/resources/Storage/psd-tutorial-publication/form_ng.png)

![weatersearch 2](/resources/Storage/psd-tutorial-publication/weathersearch%202.png)

**Row 2**

**Basic Properties**

- **Style:** width:500px;
- **Layout direction: **Space-between
- **Perpendicular Direction:** center

**Input 1**

**Basic Properties**

- **Style:** flex-basis:75%;
- **place holder: **Enter city name
- **Form field appearance:** Standard
- **[(ngModel)]:** page.searchString
- **name: **searchIp

**Custom Properties**

Add the following Key&Value custom properties:

- **autocomplete:** off
- **#searchIp:** ngModel

![](/resources/Storage/psd-tutorial-publication/input_auto.png)

**Raised Button 1**

**Basic Properties**

- **class:** get-weather-button
- **buttonname:** Get weather
- **(click): **Click the **Pick a flow** mat-chip. In the Flow picker editor, select the **get Weather** page flow. Enter **page.searchString** as the value of city name and Click **Ok**.

![get weather flow picker](/resources/Storage/psd-tutorial-publication/gw_flowpicker.png)

- **type:** submit

### weathercard and log views

On the **weathersearch** page, expand the **Views** section of the palette list. Drag and drop the **weathercard** and **log** views to the page.

![](/resources/Storage/psd-tutorial-publication/weather_view.png)

#### Weather card view - Advanced properties

- **[showCard]: **page.showCard
- **[weatherdata]: **page.weatherdata
- **(log): **Select the **Pick a flow** mat-chip. In the Flow picker editor, select the **updateLog** page flow. Enter **$event** as the value of logobject, and click** Ok**.

![Updatelog - flow picker](/resources/Storage/psd-tutorial-publication/updatelog_fp.png)

#### Weather card view - Custom Properties

In the custom properties section, add the following custom attributes:

Select the **Attribute** type, enter #weatherView , and click the **Add** button to add the property to the list.

![](/resources/Storage/psd-tutorial-publication/weather_view_1.png)

---

**Log view**

**Advanced properties**

- **[logArray]** : page.logArray

Save the changes.
