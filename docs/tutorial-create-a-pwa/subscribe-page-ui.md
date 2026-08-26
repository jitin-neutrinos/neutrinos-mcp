# Properties

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/subscribe-page-ui>

To design the page, drag and drop various [components](/smart/project-concepts/component) from the palette list to create the following layout of the **Subscribe **page:

### Properties

For every component that is dragged and dropped into the page container, properties should be set using the attributes window. Double-click the component to open its attributes window.

#### COLUMN-1

**Basic Properties**

- **fxLayoutGap**: 1rem

---

**Row-1**

**Basic Properties**

- **fxLayoutGap**: 1rem

---

**Row-2**

**Basic Properties**

- **fxLayoutGap: **1rem
- **Wrap: **nowrap

---

**Image-1**

**Basic Properties**

- **Style**: width: 3rem; height:3rem
- **Assets src**: /Web/Icons/favicon.png

---

**Column-2**

**Basic Properties**

- **fxLayoutGap: **.5rem

---

**HTML5-1**

**Basic Properties**

- **style: **font-weight: bold; font-size: 1rem
- **Element Type: **span

Double click the HTML editor inside the HTML 5 component and enter Get instant notifications as they happen.

---

**HTML5-2**

**Basic Properties**

- **style: color: **light-gray; font-size: 1rem
- **Element Type: **span

Double click the HTML editor inside the HTML 5 component and enter

Enter the City name to get the latest updates.

**![Subscribe page components](/resources/Storage/tutorial-create-a-pwa/subscribe_components.png)
**

**Row-4**

**Basic Properties**

- **fxLayoutGap: **1rem
- **Layout Direction: **Center
- **Perpendicular Direction: **Center

---

**Input-1**

##### Basic Properties

- **Place Holder: **City Name
- **[(ngModel)]**: page.cityName

---

**Raised Button-1**

**Basic Properties**

- **Style: **width:50%
- **Class: **get-weather-button
- **Button name: **Subscribe

**Custom Properties**

- **[mat-dialog-close]: **page.cityName
