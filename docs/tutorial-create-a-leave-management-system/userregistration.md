# userregistration

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/userregistration>

The **userregistration **page enables new users to register.LayoutDrag various components to create the following layout of the **userregistration **page:![The Userregistration page](/resources/Storage/tutorial-create-a-leave-management-system/user_reg.png)PropertiesUse the following table to configure properties for the **userregistration **page:**Row -1****Basic Properties****Property name****Property Value**Layout DirectionCenterPerpendicular DirectionStartfxshowtruefxhidefalseWrapnowrap
**Custom Properties**Add a custom attribute in the custom property field. Enter `fxFill` in the key field and click Add. You will see the `Layout Fill` attribute added (with the `Fill` option selected) to the Attributes window.
**COLUMN-1**![Column 1](/resources/Storage/tutorial-create-a-leave-management-system/2019-07-30_13h19_34.png)**Basic Properties****Property name****Property Value**Layout DirectionCenterPerpendicular DirectionCenterfxshowtruefxhidefalseWrapwrapClassMargin-tb

**Custom Properties**

| **Property name** | **Property Value** | **Property Type** |
| --- | --- | --- |
| fxFlex.gt-md | 40 | TRUE(KV) |
| fxFlex.sm | 70 | TRUE(KV) |
| fxFlex.md | 60 | TRUE(KV) |
| fxFlex.xs | 100 | TRUE(KV) |

---

FORM-1![Form 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/form1.png)Basic Properties**Property name****Property Value**StyleWidth=100%

**Custom Properties**

In the Custom properties field select the Key/Value option. Enter #form in the Key field and ngForm in the Value field.

---

**CARD-1**

---

**CARD TITLE-1**

![Card Title](/resources/Storage/tutorial-create-a-leave-management-system/card%20title.png)

**Basic properties**

| **Property name** | **Property Value** |
| --- | --- |
| Title | Employee Information |

---

**ROW-2**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Center |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |
| fxFlex | 100 |
| fxLayoutGap | 1.25em |

---

**COLUMN-2**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | End |
| Perpendicular Direction | End |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**ICON-1**![Icon1](/resources/Storage/tutorial-create-a-leave-management-system/icon1.png)**Basic Properties****Property name****Property Value**Icon namePerson

---

**COLUMN-3**

![Column3](/resources/Storage/tutorial-create-a-leave-management-system/column3.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Start |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**TEXT-1[[Input](/smart/project-components-documentation-copy/input)]**

** Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | First Name |
| required | required |
| [(ngModel)] | dm.leaverequest.firstname |
| name | firstname |
| disabled | true |

---

**ROW-4**![Row 2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/row4.png)**Basic Properties****Property name****Property Value**Layout DirectionCenterPerpendicular DirectionCenterfxshowtruefxhidefalsefxFlex100fxLayoutGap1.25em

---

**COLUMN-4**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | End |
| Perpendicular Direction | End |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**ICON-2[Icon]**![Icon1](/resources/Storage/tutorial-create-a-leave-management-system/icon2.png)**Basic Properties****Property name****Property Value**Icon namePerson

---

**COLUMN-5**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Start |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**TEXT-2 [Input]**

** Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | Last Name |
| required | required |
| [(ngModel)] | dm.leaverequest.lastname |
| name | lastname |
| disabled | true |

---

**ROW-5**![Row 2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/row5.png)**Basic Properties****Property name****Property Value**Layout DirectionCenterPerpendicular DirectionCenterfxshowtruefxhidefalsefxFlex100fxLayoutGap1.2em

---

**COLUMN-6**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | End |
| Perpendicular Direction | End |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**ICON-3**![Icon1](/resources/Storage/tutorial-create-a-leave-management-system/icon3.png)**Basic Properties****Property name****Property Value**Icon nameEmail

---

**COLUMN-7**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Start |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**TEXT-3 [Input]**

** Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | Email ID |
| required | required |
| [(ngModel)] | dm.leaverequest.username |
| name | username |
| disabled | true |

---

**ROW-6**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Center |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| fxFlex | 100 |
| fxLayoutGap | 1.2em |

---

**COLUMN-8**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | End |
| Perpendicular Direction | End |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**ICON-4**![Icon1](/resources/Storage/tutorial-create-a-leave-management-system/icon4.png)**Basic Properties****Property name****Property Value**Icon namePerson

---

**COLUMN-9**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Start |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**TEXT-4**

** Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | Employee ID |
| required | required |
| [(ngModel)] | dm.leaverequest.employeeID |
| name | employee ID |

---

**ROW-7**![Row 2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/ror7.png)**Basic Properties****Property name****Property Value**Layout DirectionCenterPerpendicular DirectionCenterfxshowtruefxhidefalsefxFlex100fxLayoutGap1.25em

---

**COLUMN-10**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Start |
| Perpendicular Direction | Stretch |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**ICON-5**![Icon1](/resources/Storage/tutorial-create-a-leave-management-system/icon%205.png)**Basic Properties****Property name****Property Value**Icon nameGroup

---

**COLUMN-11**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Start |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**SELECT-1**

** Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | Department |
| required | required |
| [(ngModel)] | dm.employee.staff.department |
| (selectionChange) | showManager() |
| *ngFor | let department of departments |
| [value] | department |
| optiondata | {{department}} |

**Custom Properties**

In the Custom properties field select the Key/Value option. Enter name in the key field and department in the Value field.

---

**ROW-8**![Row 2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/row8.png)**Basic Properties****Property name****Property Value**Layout DirectionCenterPerpendicular DirectionCenterfxshowremovefxhideremovefxFlex100fxLayoutGap1.25em

**Custom Properties**

In the Custom properties field select the Key/Value option. Enter [fxShow] in the key field and !isManager && managers.length > 0 in the Value field.

---

**COLUMN-12**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | End |
| Perpendicular Direction | End |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**ICON-6**![Icon1](/resources/Storage/tutorial-create-a-leave-management-system/icon6.png)**Basic Properties****Property name****Property Value**Icon nameaccount_box

---

**COLUMN-13**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Start |
| Perpendicular Direction | Center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |

---

**SELECT-2**

** Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | Manager |
| [(ngModel)] | dm.employee.staff.ManagerName |
| *ngFor | let manager of managers |
| [value] | manager |
| optiondata | {{manager}} |

**Custom Properties**

| **Property name** | **Property Value** | **Property Type** |
| --- | --- | --- |
| name | managerName | TRUE(KV) |
| [required] | userObj && userObj.groupList.indexOf('Employee') > -1 ? 'required': null | TRUE(KV) |

---

**ROW-9**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Center |
| Perpendicular Direction | Center |
| fxshow | remove |
| fxhide | remove |
| fxFlex | 100 |

---

**RAISED BUTTON-1[Raised Button]**

![radio button 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/RB1.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| buttonname | Save |
| Color | primary |
| (click) | put('employee', dm.employee) |
| disabled | form.valid |

---

Page ImplementationSince this is will be the first page displayed to the new user, we need to map the logged-in users information to the employee information, which can be done in the ngOnInit method of the Page. Copy CodeJavaScriptngOnInit() {
 // mapping the userobject the datamodel
 this.userObj = this.sessionStorage.getValue('userObj');
 this.dm.employee.staff.username = this.userObj.username;
 this.dm.employee.staff.firstName = this.userObj.firstName;
 this.dm.employee.staff.lastName = this.userObj.lastName;
 this.dm.employee.staff.groupList = this.userObj.groupList;
 this.dm.employee.staff.displayName = this.userObj.displayName;
 this.dm.employee.leaves = this.leaves
 this.isManager = (this.userObj.groupList.indexOf('Manager') > -1);
}
On selecting a department we need to get the Manager of the department which can be done using a simple query as below.Copy CodeJavaScriptshowManager() {
 this.get(
 'employee',
 {
 'staff.department': this.dm.employee.staff.department, 'staff.groupList': 'Manager' }
 ,
 {
 'staff.displayName': 1, 'staff.groupList': 1 }
 )
 }
Complete page implementationReplace the code in the **Ts** editor tab of the current page in the studio with the below code.Copy CodeJavaScript/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import { Component, OnInit } from '@angular/core'
import { ModelMethods } from '../../lib/model.methods';
// import { BDataModelService } from '../service/bDataModel.service';
import { NDataModelService, NSessionStorageService } from 'neutrinos-seed-services';
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { Router } from '@angular/router';
import { userService } from '../../services/user/user.service';
/**
 * Service import Example :
 * import { HeroService } from '../../services/hero/hero.service';
 */
@Component({
 selector: 'bh-userregistration',
 templateUrl: './userregistration.template.html'
})
export class userregistrationComponent extends NBaseComponent implements OnInit {
 mm: ModelMethods;
 isManager = true;
 userObj;
 leaves = {
 "annualLeaves": 15,
 "sickLeaves": 15,
 "approvedLeaves": 0
 }
 managers = [
 ];
 departments = [
 'HR',
 'Production'
 ];
 constructor(
 private bdms: NDataModelService,
 private sessionStorage: NSessionStorageService,
 private router: Router,
 private uService: userService
 ) {
 super();
 this.mm = new ModelMethods(bdms);
 }
 ngOnInit() {
 this.userObj = this.sessionStorage.getValue('userObj');
 this.dm.employee.staff.username = this.userObj.username;
 this.dm.employee.staff.firstName = this.userObj.firstName;
 this.dm.employee.staff.lastName = this.userObj.lastName;
 this.dm.employee.staff.groupList = this.userObj.groupList;
 this.dm.employee.staff.displayName = this.userObj.displayName;
 this.dm.employee.leaves = this.leaves
 this.isManager = (this.userObj.groupList.indexOf('Manager') > -1);
 }
 showManager() {
 this.get(
 'employee',
 { 'staff.department': this.dm.employee.staff.department, 'staff.groupList': 'Manager' },
 { 'staff.displayName': 1, 'staff.groupList': 1 })
 }
 get(dataModelName, filter?, keys?, sort?, pagenumber?, pagesize?) {
 this.mm.get(dataModelName, filter, keys, sort, pagenumber, pagesize,
 result => {
 // On Success code here
 if (result && result.length > 0 && result[0].staff.groupList.indexOf("Manager") > -1) {
 this.managers.push(result[0].staff.displayName);
 } else {
 this.managers = [];
 this.dm.employee.staff.managerName = '';
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
 this.uService.user = dataModelObject;
 this.router.navigate(['/home/userdetail']);
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



 ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png)

  Make sure you copy ad paste only the **Complete page implementation** in the TS editor of the page.



**The View of user-registration page on runtime:****![The userregistration page](/resources/Storage/tutorial-create-a-leave-management-system/user_registration1.png)
**
