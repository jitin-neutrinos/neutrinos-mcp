# Layout

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/home>

This is the main page or the landing page of your application.

### Layout

Drag and drop various [components](/smart/project-concepts/component) from the palette list to create the following layout of the **Home **page:

![home layout](/resources/Storage/create-a-simple-mobile-app/home.png)

### Properties

To every component that is dragged and dropped into the page container, the properties should be set. Double-click the component to open its attributes window.

---

#### COLUMN-1

**Basic Properties**

- **Style**: bottom: 0;
- **Class**: hundred-height
- **fxFlex**: 100

---

**TOOLBAR-1**

**Basic Properties**

- Class: red-background

---

#### Row 1

**Basic Properties**

- Layout Direction: space-between
- fxFlex: 100
- Perpendicular Direction: center

---

**Row 2**

**Basic Properties**

- **fxFlex: **5

---

**Icon 1**

**Basic Properties**

- **Style color**: #ffffff
- **IconName**: menu

**Custom Properties**

- **(click):** snav.toggle()

---

![home 2](/resources/Storage/create-a-simple-mobile-app/home%202.png)

**Column 2**

**Basic properties**

- **Class: **layout-column

---

**Sidenav Container-1**

- **Class**: hundred-height
- **Auto size**: False

---

**Sidenav**

**Basic properties**

- **Class: **sidenav-style
- **Sidenav Mode**: Over
- **Opened**: False

#### Custom Properties

In the Attributes field, enter #snav and click add

---

**Column 3**

- **Class**: listitem-padding
- **fxFlex:** 100
- **Perpendicular Direction**: Start

**Image 1**

**Basic Properties**

- **style width**: 100%;
- **Assets src:** Web/Icons/neutrinos.jpg

---

![home 3](/resources/Storage/create-a-simple-mobile-app/home%203.png)

**Row 3**

**Basic Properties**

- **Row label**: Home
- **Layout Direction**: Space-between
- **wrap**: wrap
- **Perpendicular Direction**: center

**Custom Properties**

- **(click): **snav.close(); goHome()

---

**Icon 2**

**Basic Properties**

- **style color**:#f22129;
- **Icon Name**: home

---

**Html 5-1**

**Basic Properties**

- **Style:** padding-left: 1em;color:#898a8f;
- **Element Type**: Header 4

Double click the HTML editor inside the HTML 5 component and enter Home.

---

**Row 4**

**Basic Properties**

- **Row Label**: UsersList
- **Wrap**: wrap
- **Layout Direction**: space-between
- **Perpendicular Direction**: Center

**Custom Properties**

- **(click): **snav.close(); goUList()

---

**Icon 3**

**Basic Properties**

- **style**: color:#f22129;
- **Icon name**: list

---

**HTML5 2**

**Basic Properties**

- **style**: padding-left: 1em;color:#898a8f;
- **Element type**: Header 4

Double click the HTML editor inside the HTML 5 component and enter Users list.

![home 4](/resources/Storage/create-a-simple-mobile-app/home%204.png)

---

**Column 5**

**Basic Properties**

- **Class**: hundred-height
- **wrap**: wrap

---

**Column 6**

**Basic Properties**

- **fxFlex**: 30

---

**PAGE IMPLEMENTATION**

Replace the code in the **Ts **tab of the current page in the studio with the below code. To navigate to the TypeScript editor, click the TS icon below the Menu list.

![TS icon](/resources/Storage/create-a-simple-mobile-app/ts_icon.png)

Copy CodeJavaScript/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import { Component, OnInit, NgZone } from '@angular/core'
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { ocr } from 'app/sd-services/ocr';

import { Router } from '@angular/router';
import { NPubSubService } from 'neutrinos-seed-services';
/*
Client Service import Example:
import { servicename } from 'app/sd-services/servicename';
*/

/*
Legacy Service import Example :
import { HeroService } from '../../services/hero/hero.service';
*/

@Component({
 selector: 'bh-home',
 templateUrl: './home.template.html'
})

export class homeComponent extends NBaseComponent implements OnInit {

 constructor(private ocrRunner: ocr,
 private router: Router,
 private pubsub: NPubSubService,
 private ngZone: NgZone
 ) {
 super();
 }

 ngOnInit() {
 this.pubsub.$sub('scan-complete', () => {
 this.ngZone.run(() => {
 this.router.navigate(['/home/captureinfo']);
 })
 })
 this.router.navigate(['/home/greeting']);
 }

 goHome() {
 this.router.navigate(['/home/greeting']);
 }
 goInfo() {
 this.router.navigate(['/home/captureinfo']);
 }
 goUList() {
 this.router.navigate(['/home/usersList']);
 }
}

Save the changes.
