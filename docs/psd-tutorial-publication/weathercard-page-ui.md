# Layout

<https://documentation.neutrinos.com/articles/#!psd-tutorial-publication/weathercard-page-ui>

### Layout

Drag and drop various components and create the following layout.

### Properties

Use the following details to configure the properties of components on the **weathercard** page:

![weather card page layout properties 1](/resources/Storage/psd-tutorial-publication/weathercard1.png)

**Row 1**

**Basic properties**

- **Style: height:**100%;
- **Layout direction:** Center
- **Perpendicular Direction: **Start

**Column 1**

**Basic properties**

- **Perpendicular Direction:** None

**Card 1**

**Basic properties**

- **Style: **width:500px;

**Custom properties - Key & Value**

- ***ngIf:** showCard

![](/resources/Storage/psd-tutorial-publication/title-2021-12-03.png)

**Card Title 1**

**Basic properties**

- **Title:** {{page.localStorage.lastCity+ ' weather summary' | titlecase}}
- **Align:** Center

![weathercard layout properties 2](/resources/Storage/psd-tutorial-publication/weathercard2.png)

**Row 2**

**Basic properties**

- **fxLayoutGap: **5px
- **Layout Direction: **space-evenly

**Column 2**

**Basic properties**

- **Class: **weathers
- **Wrap: **NoWrap
- **Perpendicular Direction:** center

**Custom properties**

- ***ngFor: **let w of weatherdata?.weather; let i = index;

**Image 1**

**Basic properties**

- **[src]:** 'http://openweathermap.org/img/w/' + w.icon + '.png'
- **Secure URI:** False

**HTML5- 2**

**Basic properties**

- **Element Type: **Paragraph

Double-click the HTML editor and enter {{w.description}} in the editor space.

![](/resources/Storage/psd-tutorial-publication/html5_desc.png)

![weathercard page layout properties 3](/resources/Storage/psd-tutorial-publication/weathercard3.png)

**Card Content 2**

**Basic Properties**

- **Align: **Center

**Grid List 1**

**Basic Properties**

- **cols:** 2
- **gutterSize:** 5px
- **rowHeight: **50px

**Column 3**

**Custom Properties**

- ***ngFor: **let m of weatherdata?.main | keyvalue

![](/resources/Storage/psd-tutorial-publication/title-2021-12-03-1.png)

![weathercard layout properties 4](/resources/Storage/psd-tutorial-publication/weathercard4.png)

**Grid Tile 1**

**Basic properties**

- **label:**<b>{{m.key | titlecase }}</b>

**Grid Tile 2**

**Basic Properties**

- **label:** {{m.value + (m.key.includes('temp')?'°C': " ")}}

Save the changes.
