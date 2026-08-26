# Layout

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/users-list>

The **usersList **page displays the list of the users that are added to the database.

### Layout

Drag various components to create the following layout of the **usersList** page:

![userslist layout](/resources/Storage/create-a-simple-mobile-app/userlist.png)

### Properties

Use the following table to configure properties for the **U****sersList** page:

![userlist properties](/resources/Storage/create-a-simple-mobile-app/userlist1.png)

**Row-1**

**Basic Properties**

- **Class**: red-gradient, red-background
- **Layout Direction**: Center
- **Perpendicular Direction**: Start

**Custom Properties**

- **Layout Fill**: fxFill

---

#### Column-1

**Basic Properties**

- **Style padding**: 1em 0px;
- **Class:** hundred-height
- **Layout Direction**: Start
- **Perpendicular Direction:** Center
- **fxshow:** true
- **fxhide:** false
- **Wrap**: wrap
- **fxFlex**: 90

---

**Row 2**

**Basic Properties**

- **Style width**:100%;
- **fxFlex:** 10
- **Layout Direction**: Start
- **Perpendicular Direction:** Start
- **Wrap:** Wrap

---

#### HTML 5- 1

**Basic Properties**

- **Style**: color:#ffffff;font-size: 2em;padding-bottom:0.5em; font-weight:700;
- **Element type**: Div

Double click the HTML editor and enter Users List

---

### 

#### 

#### Column-2

**Basic Properties**

- **Layout Direction**: Start
- **Perpendicular Direction**: Center
- **fxshow**: true
- **fxhide**: false
- **Wrap**: wrap
- **fxFlex**: 80

**Column 3**

**Basic properties**

- **Class**: card-shadow, rcorners1
- **Layout Direction**: Start
- **Perpendicular Direction**: Stretch

**Table -1**

### 

Basic Properties

- **Style**: padding: 1em;
- **[dataSource]**: usersList

### 

### Table Column 1

Basic Properties

- **Header Label**: First Name
- **Sort**: false
- **Mapping**: {{table.firstName}}

### 

---

#### Table Column 2

**Basic Properties**

- **Class**: col-padding
- **Header Label**: Last Name
- **Sort**: false
- **Mapping**: {{table.lastName}}

---

#### Table Column 3

**Basic Properties**

- **Class**: col-padding
- **Header Label**: PAN
- **Sort**: false
- **Mapping**: {{table.pan}}

**Table Column 4**

**Basic Properties**

- **Class**: col-padding
- **Header Label**: DOB
- **Sort**: false
- **Mapping**: {{table.dob}}

---

### 

**Page Implementation:**

Open the TS editor of the page and enter the following code.

Copy CodeJavaScript/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import { Component, OnInit } from '@angular/core'
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { usermanagement } from 'app/sd-services/usermanagement';

/*
Client Service import Example:
import { servicename } from 'app/sd-services/servicename';
*/

/*
Legacy Service import Example :
import { HeroService } from '../../services/hero/hero.service';
*/

@Component({
 selector: 'bh-userslist',
 templateUrl: './userslist.template.html',
 styles: [
 `
 .overflows {
 overflow-y: auto;
 overflow-x: hidden;
 }
 `
 ]
})

export class userslistComponent extends NBaseComponent implements OnInit {
 usersList;
 constructor(private m: usermanagement) {
 super();
 }

 async ngOnInit() {
 this.usersList = (await this.m.getUsers()).local.usersList;
 // console.log(this.usersList);
 }
}
