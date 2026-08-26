# Layout

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/userdetails>

The **userdetails** page is a tabbed view that displays the **myleaves**, **myprofile,** and **myapprovals** page.

**myapprovals** page will be hidden for the employee and will only be visible to the manager.

### Layout

Drag various components to create the following layout of the **userdetails** page:

![Layout of the userdetails page](/resources/Storage/tutorial-create-a-leave-management-system/layoutUD.png)

### Properties

Use the following table to configure properties for the **userdetails** page:

#### TABGROUP

**![tabgroup of the userdetails page](/resources/Storage/tutorial-create-a-leave-management-system/tabgroupUD.png)**

---

**TAB-1**

**![Tab 1 of the userdetails page](/resources/Storage/tutorial-create-a-leave-management-system/tab1UD.png)**

**Basic Properties**

| **P****roperty name** | **Property Value** |
| --- | --- |
| Label | My Leaves |

---

#### ROW-1

**![Row 1 of the userdetails page](/resources/Storage/tutorial-create-a-leave-management-system/row1UD.png)**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Center |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |
| fxFlex | 100 |

---

**HTML-1**

![HTML 1 of the user details page](/resources/Storage/tutorial-create-a-leave-management-system/html1UD.png)

**Basic Properties**

To add a property double click on the Html editor and enter <bh-myleaves style="width:100%"></bh-myleaves>.

### 

#### TAB-2

![Tab2 of the user details page](/resources/Storage/tutorial-create-a-leave-management-system/tab2ud.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Label | My Profile |

---

### 

#### ROW-2

![Row 2 of the user deatils page](/resources/Storage/tutorial-create-a-leave-management-system/row2ud.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Center |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |
| fxFlex | 100 |

---

### 

#### HTML-2

![Html 2 of the user details page](/resources/Storage/tutorial-create-a-leave-management-system/html_2.png)

**Basic properties**

To add a property, double click on the Html editor and enter <bh-myprofile style="width:100%"></bh-myprofile> in the code

---

### TAB-3

![Tab 3 of the user details page](/resources/Storage/tutorial-create-a-leave-management-system/tab3ud.png)

Basic Properties

| **Property name** | **Property Value** |
| --- | --- |
| Label | My Approvals |

**Custom Properties**

In the Custom Property field, select Key/Value Option. Enter *ngIf in the Key field and enter uService.isManager() in the value field.

---

### ROW-3

![Row 3 of the user details page](/resources/Storage/tutorial-create-a-leave-management-system/row3ud.png)

Basic Properties

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Center |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |
| fxFlex | 100 |

---

### 

#### HTML-3

![Html 3 of the user details page](/resources/Storage/tutorial-create-a-leave-management-system/html3ud.png)

**Basic Properties**

To add a property double click on the Html editor and enter <bh-myapprovals style="width:100%"><bh-myapprovals> .

---

#### If you are using the version 6.2.0 and higher, then follow these steps:

**Step 1**: Replace the **Tab Group** component with the **Tabs** component.

**Step 2**: Add three more tabs using the **New Tab** button inside the **Tabs** component. Refer [Tabs component](/smart/project-components-documentation-copy/tabs) to know more.

![lms layout for 6.2.1](/resources/Storage/tutorial-create-a-leave-management-system/Tabs%20group%20lms.png)

**Properties for the Tabs component:**

![tabs of the layout](/resources/Storage/tutorial-create-a-leave-management-system/T123png.png)

**Tab-1**

| **Property name** | **Property Value** |
| --- | --- |
| label | My leaves |

**Tab-2 **

| **Property name** | **Property Value** |
| --- | --- |
| label | My profile |

**Tab-3**

| **Property name** | **Property Value** |
| --- | --- |
| label | My approvals |

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | The properties for the** Row **and** HTML5** components remain the same as mentioned before. |
| --- | --- |

---

### 

**Page Implementation:**

Copy CodeJavaScript/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import { Component, OnInit } from '@angular/core'
import { ModelMethods } from '../../lib/model.methods';
// import { BDataModelService } from '../service/bDataModel.service';
import { NDataModelService } from 'neutrinos-seed-services';
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { userService } from '../../services/user/user.service';
/**
 * Service import Example :
 * import { HeroService } from '../../services/hero/hero.service';
*/
@Component({
 selector: 'bh-userdetails',
 templateUrl: './userdetails.template.html'
})
export class userdetailsComponent extends NBaseComponent implements OnInit {
 mm: ModelMethods;
 constructor(private bdms: NDataModelService,public uService: userService) {
 super();
 this.mm = new ModelMethods(bdms);
 }
 ngOnInit() {
 }
 get(dataModelName, filter?, keys?, sort?, pagenumber?, pagesize?) {
 this.mm.get(dataModelName, filter, keys, sort, pagenumber, pagesize,
 result => {
 // On Success code here
 },
 error => {
 // Handle errors here
 });
 }
 getById(dataModelName, dataModelId) {
 this.mm.getById(dataModelName, dataModelId,
 result => {
 // On Success code here
 },
 error => {
 // Handle errors here
 })
 }
 put(dataModelName, dataModelObject) {
 this.mm.put(dataModelName, dataModelObject,
 result => {
 // On Success code here
 }, error => {
 // Handle errors here
 })
 }
 validatePut(formObj, dataModelName, dataModelObject) {
 this.mm.validatePut(formObj, dataModelName, dataModelObject,
 result => {
 // On Success code here
 }, error => {
 // Handle errors here
 })
 }
 update(dataModelName, update, filter, options) {
 const updateObject = {
 update: update,
 filter: filter,
 options: options
 };
 this.mm.update(dataModelName, updateObject,
 result => {
 // On Success code here
 }, error => {
 // Handle errors here
 })
 }
 delete (dataModelName, filter) {
 this.mm.delete(dataModelName, filter,
 result => {
 // On Success code here
 }, error => {
 // Handle errors here
 })
 }
 deleteById(dataModelName, dataModelId) {
 this.mm.deleteById(dataModelName, dataModelId,
 result => {
 // On Success code here
 }, error => {
 // Handle errors here
 })
 }
 updateById(dataModelName, dataModelId, dataModelObj) {
 this.mm.updateById(dataModelName, dataModelId, dataModelObj,
 result => {
 // On Success code here
 }, error => {
 // Handle errors here
 })
 }
}
**The view of the userdetails page on runtime:**

![The userdetails page](/resources/Storage/tutorial-create-a-leave-management-system/user_detail.png)
