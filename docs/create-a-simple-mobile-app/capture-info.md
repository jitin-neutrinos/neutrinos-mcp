# Layout

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/capture-info>

This page is used to capture info from the PAN card after it is scanned.

![PAN card scan](/resources/Storage/create-a-simple-mobile-app/Screenshot_blur.jpg)

![Capture info page](/resources/Storage/create-a-simple-mobile-app/PAN.jpg)

### Layout

Open the **Capture info** page. Drag various components and create the following layout.

### Properties

Use the following tables to configure properties for each component in the layout of this page.

**Row-1**

**Basic properties**

- **Class**: red-gradient, red-background
- **Layout Direction:** center
- **Perpendicular direction:** none

**Custom Properties**

- **Layout Fill**: fxFill

---

**Column-1**

**Basic properties**

- **Style**: color:#898a8f;padding: 1em 0px;
- **Class**: hundred-height
- **fxFlex**: 90
- **Layout Direction**: Start
- **Perpendicular Direction**: center

---

**Row 2**

**Basic properties**

- **Style:** width:100%
- **fxFlex**: 10
- **Layout Direction**: Start
- **Perpendicular Direction:** Start

---

**HTML5 1**

**Basic properties**

- **Style**: color:#ffffff;font-size: 2em;padding-bottom:0.5em; font-weight:700;
- **Element type**: Div

Double click the HTML editor and enter **User Details.**

---

**Column- 2**

**Basic properties**

- **fxFlex**: 80
- **wrap**: nowrap
- **Layout Direction**: Start
- **Perpendicular Direction**: Center

---

**Column- 3**

**Basic properties**

- **Class**: rcorners1
- **fxFlex:** 100
- **wrap**: wrap
- **Layout Direction**: Space-evenly
- **Perpendicular Direction:** Center

**Custom Properties**

- ***ngIf**: this.ocrRunner.info
- **LayoutFill**: fxFill

---

**Column 4**

**Basic properties**

- **Style**: margin-top: 20px;
- **Layout Direction**: Start
- **Perpendicular Direction**: Center

**![capture info 3](/resources/Storage/create-a-simple-mobile-app/capinfo3.png)


 **

---

**Input 1**

**Basic properties**

- **Style**: width:20em
- **Place holder**: First Name
- **Form Field appearance**: Outline
- **[(ngModel)]**: this.ocrRunner.info.firstName
- **Label**: First Name

---

**Input 2**

**Basic properties**

- **Style**: width:20em
- **Place holder:** Last Name
- **Form Field appearance:** Outline
- **[(ngModel)]:** this.ocrRunner.info.lastName
- **Label:** Last Name

---

****Input 3**


 **

**Basic properties**

- **Style**: width:20em
- **Place holder**: Date of Birth
- **Form Field appearance:** Outline
- **[(ngModel)]:** this.ocrRunner.info.dob
- **Label:** Date of Birth

---

**Input 4**

**Basic properties**

- **Style**: width:20em
- **Place holder**: PAN Number
- **Form Field appearance**: Outline
- **[(ngModel)]**: this.ocrRunner.info.pan
- **Label:** PAN Number

---

**Raised Button 1**

**Basic properties**

- **Style**: margin-bottom:20px;
- **Button Name**: Submit
- **Color**: warn
- **(click)**: log()

---

### Page Implementation

Open the TS editor of the **captureInfo** page and enter the following code.

```javascript
/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/import { Component, OnInit, AfterViewInit, NgZone } from '@angular/core'import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';import { ocr } from 'app/sd-services/ocr';import { usermanagement } from 'app/sd-services/usermanagement'/*Client Service import Example:import { servicename } from 'app/sd-services/servicename';*//*Legacy Service import Example :import { HeroService } from '../../services/hero/hero.service';*/@Component({    selector: 'bh-captureinfo',    templateUrl: './captureinfo.template.html',    styles: [`        .max-height-initial {            max-height: initial !important;            height: initial !important;        }        .overflows {            overflow-y: auto;            overflow-x: hidden;        }    `]})export class captureinfoComponent extends NBaseComponent implements OnInit {    formData: {}    firstName;    lastName;    pan;    dob;    constructor(public ocrRunner: ocr, private ngZone: NgZone, public mcrud: usermanagement) {        super();    }    ngOnInit() {    }    ngAfterViewInit(): void {      this.ngZone.run(() => {      })    }    async log() {      this.ngZone.run(() => {        // console.log('this.ocrRunner', this.ocrRunner);        this.firstName = this.ocrRunner.info.firstName        this.lastName = this.ocrRunner.info.lastName        this.dob = this.ocrRunner.info.dob        this.pan = this.ocrRunner.info.pan      });      this.formData = {          firstName: this.firstName,          lastName: this.lastName,          dob: this.dob,          pan: this.pan      }    // console.log(this.formData)     await this.mcrud.createUser(this.formData);    }}
```

```

```

---
