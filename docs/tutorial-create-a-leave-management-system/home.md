# COLUMN-1

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/home>

This is the main page or the landing page of your application. In LMS, the homepage is a default page that is created because of the template selected while creating the app.

**Layout**

Drag and drop various components from the palette section to create the following layout of the homepage:

![Homepage of LMS](/resources/Storage/tutorial-create-a-leave-management-system/homeLMS.png)

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | If you are using a version higher than 6.2.0, then replace the **paragraph** component with **HTML5** component. |
| --- | --- |

**Properties**

To every component that is dragged and dropped into the page container, the properties should be set.

#### COLUMN-1

![Column 1 of the LMS layout](/resources/Storage/tutorial-create-a-leave-management-system/column1LMS.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | none |
| Perpendicular Direction | none |
| fxshow | true |
| fxhide | false |
| Wrap | Nowrap |

**Custom properties**

Add a custom attribute in the custom property field. Enter `fxFill` in the key field and click **Add**. You will see the `Layout Fill` attribute added (with the `Fill` option selected) to the Attributes window.

![Custom properties for the homepage](/resources/Storage/tutorial-create-a-leave-management-system/customhomeLMS.png)

---

**TOOLBAR-1**

![Toolbar1 of the homepage of LMS](/resources/Storage/tutorial-create-a-leave-management-system/toolbar1LMS.png)

**Custom properties**

Add a new custom attribute using the custom Property field. Enter `fxLayoutAlign` in the key/value field and click **Add**. You will see the `Layout Fill` attribute added to the Attributes window. Enter `space-between` as its value.

---

#### COLUMN-2

![Column 2 of the homepage of the LMS](/resources/Storage/tutorial-create-a-leave-management-system/column_2.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | none |
| Perpendicular Direction | none |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**IMAGE-1**

![Image 1 of the homepage of LMS](/resources/Storage/tutorial-create-a-leave-management-system/image1home.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Style | width:30%;cursor:pointer; |
| imgsrc | Web/logo.png |

**Custom properties**

Add a new custom attribute using the Custom Property field. Select the **Key/Value** option. Enter ` routerLink` in the key field and `/home/userdetail` in the value field. Click **Add**. You will see the attribute added to the Attributes window.

---

**COLUMN-3**

![column3 of the homepage og LMS](/resources/Storage/tutorial-create-a-leave-management-system/column3home.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | center |
| Perpendicular Direction | end |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**ICON-1**

![Icon 1 of the homepage of LMS](/resources/Storage/tutorial-create-a-leave-management-system/icon1home.png)

**Basic properties**

| **Property name** | **Property Value** |
| --- | --- |
| Style | cursor:pointer; |
| IconName | power_settings_new |

**Custom properties**

Add two new custom attributes using the Custom Property field. Select Key/Value. Enter `(click)` in the **key **field and `logoutUser()` in the **value **field. Click **Add**. Enter `title` in the **Key** field, and `Logout` in the value field. Click **Add**. You will see the two attributes added to the Attributes window.

---

**COLUMN-4**

| **Property name** | **Property Value** |
| --- | --- |
| Style | overflow:auto; |
| fxFlex | calc(100%-128px) |
| Layout Direction | none |
| Perpendicular Direction | none |
| fxShow | true |
| fxHide | false |
| wrap | nowrap |

---

**ROUTER OUTLET-1**

![Router Outlet 1 of the homepage of LMS](/resources/Storage/tutorial-create-a-leave-management-system/routerhomeLMS.png)

---

**TOOLBAR-2 **

![Toolbar 2 of the homepage of LMS](/resources/Storage/tutorial-create-a-leave-management-system/toolbar2home.png)

---

**COLUMN-5**

![Column 5 of the homepage of LMS](/resources/Storage/tutorial-create-a-leave-management-system/column5home.png)

| **Property name** | **Property Value** |
| --- | --- |
| fxFlex | 100 |
| Layout Direction | center |
| Perpendicular Direction | center |
| fxShow | true |
| fxHide | false |
| wrap | wrap |

---

**PARAGRAPH-1**

![Paragraph 1 of the homepage of LMS](/resources/Storage/tutorial-create-a-leave-management-system/paragraph1home.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Style | font-size:12px; |

To add a property double click on the Html editor and enter &copy; 2019 Neutrinos.

---

**PAGE IMPLEMENTATION**

The home page navigates the user to a **userdetail** or **user-registration** Page based on whether the metadata of the employee is present or not.

Replace the code in the **Ts **tab of the current page in the studio with the below code.

Copy CodeJSON/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import { Component, OnInit } from '@angular/core'
import { Router } from '@angular/router';
import { ModelMethods } from '../../lib/model.methods';
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { NDataModelService, NLogoutService, NSessionStorageService } from 'neutrinos-seed-services';
import { userService } from '../../services/user/user.service';
@Component({
 selector: 'bh-home',
 templateUrl: './home.template.html'
})
export class homeComponent extends NBaseComponent implements OnInit {
 mm: ModelMethods;
 currentUserData
 constructor(
 private bdms: NDataModelService,
 private logoutService: NLogoutService,
 private router: Router,
 private ss: NSessionStorageService,
 private uService: userService
 ) {
 super();
 this.mm = new ModelMethods(bdms);
 }
 ngOnInit() {
 this.currentUserData = this.ss.getValue('userObj');
 this.get('employee', { "staff.username": this.currentUserData.username }, {}, {}, 1, 1);
 }
 logoutUser() {
 this.logoutService.logout();
 this.router.navigate(['/login']);
 }
 get(dataModelName, filter ?, keys ?, sort ?, pagenumber ?, pagesize ?) {
 this.mm.get(dataModelName, filter, keys, sort, pagenumber, pagesize,
 result => {
 // On Success code here
 if (dataModelName == 'employee' && result.length == 0) {
 // routing the employee form
 this.router.navigate(['home/userregistration']);
 } else {
 // setting the current logged user data in the User service
 this.uService.user = result[0];
 // showing emloyee information here
 this.router.navigate(['/home/userdetail']);
 }
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
