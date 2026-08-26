# The view of the applyleaves page on runtime:

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/applyleaves>

The **applyleave** page enables users to apply for leaves.**Layout**Drag various components to create the following layout of the **applyleave **page:![LAyout of the apply leave page](/resources/Storage/tutorial-create-a-leave-management-system/ALlayout.png)**Properties**Use the following table to configure properties for the **applyleave** page:**Row-1**![Row 1 of the apply leaves page](/resources/Storage/tutorial-create-a-leave-management-system/row1al.png)**Basic Properties****Property name****Property Value**Layout DirectionCenterPerpendicular DirectionCenterfxshowtruefxhidefalseWrapwrap**Custom Properties**Add a custom attribute in the custom property field. Enter `fxFill` in the key field and click Add. You will see the `Layout Fill` attribute added (with the `Fill` option selected) to the Attributes window.  **COLUMN-1**![Column 1 of the apply leave page](/resources/Storage/tutorial-create-a-leave-management-system/column1AL.png)**Basic Properties****Property name****Property Value**Layout DirectionCenterPerpendicular DirectionCenterfxshowtruefxhidefalseWrapwrapClassMargin-tb

**Custom Properties**

| **Property name** | **Property Value** | **Property Type** |
| --- | --- | --- |
| fxFlex.gt-md | 40 | TRUE(KV) |
| fxFlex.sm | 70 | TRUE(KV) |
| fxFlex.md | 60 | TRUE(KV) |
| fxFlex.xs | 100 | TRUE(KV) |

---

**CARD-1**

![Card 1 of the apply leaves page](/resources/Storage/tutorial-create-a-leave-management-system/card1AL.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Class | Card |

---

FORM-1

![Form 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/2019-07-29_15h07_02.png)

**Custom Properties**

In the Custom Properties select the Key/Value option. Enter #form in the Key field and ngForm in the Value field.

---

**COLUMN-2 **

![Column2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/column2AL.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | Start |
| Perpendicular Direction | Stretch |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |
| fxFlex | 100 |
| fxLayoutGap | 1em |

---

**SELECT-1**

![Select 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/SelectAL.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | Leave Type |
| [(ngModel)] | dm.leaverequest.leaveType |
| required | required |
| *ngFor | let leave of leaves |
| [value] | leave.leave |
| optiondata | {{leave.value}} |

**Custom Properties**

In the **Custom** property Select the Key/Value option. Enter name in the key field and leaveType in the value field.

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | If you don't find any property in the **Basic Properties**, add that property in the **Custom Properties** section. |
| --- | --- |

---

**DATE-1[Date Picker]**

![Date Picker 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/Datepicker1AL.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | From date |
| [(ngModel)] | dm.leaverequest.fromDate |
| [min] | minDate |
| touchUi | true |
| name | fromDate |
| picker | picker1 |
| required | true |

**Custom Properties**

Add these attributes in the Custom Properties field. **Note that in versions 6.2.x, ****readonly property id included in the basic properties.**

| **Property name** | **Property Value** | **Property Type** |
| --- | --- | --- |
| readonly | readonly | TRUE(KV) |

---

**DATE-2**

![Date Picker 2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/datepicker2.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | To date |
| [(ngModel)] | dm.leaverequest.toDate |
| [min] | minDate |
| touchUi | true |
| name | toDate |
| picker | picker2 |
| required | true |
| disabled | !dm.leaverequest.fromDate?'disabled':null |

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | If you don't find any property in the **Basic Properties**, add that property in the** Custom Properties **section. |
| --- | --- |

---

**TEXT-1**![Text 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/text1.png)**Basic Properties****Property name****Property Value**Place HolderLeave reason[(ngModel)]dm.leaverequest.leaveReason name
reasontypetext

**Custom Properties**In the Custom Properties Select the Key/Value option. Enter minlength in the Key field and **5** in the Value field.**RAISED BUTTON-1**![Raised button 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/Rbutton1png.png)**Basic Properties****Property name****Property Value**buttonnameapplycolorprimary(click)
applyLeave(form)disabled!form.valid

**RAISED BUTTON-2**![Raised button 2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/Rbutton2.png)**Basic Properties****Property name****Property Value**buttonnameCancelcolorprimaryrouterlink/home/userdetail

Page ImplementationWhen the employee clicks on the **APPLY LEAVE **button the **applyLeave** method gets called which takes a form object as input for Data Model form validation. Replace the code in **Ts** tab of the current page in the studio with the below code.Copy CodeJavaScript/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import { Component, OnInit } from '@angular/core'
import { ModelMethods } from '../../lib/model.methods';
// import { BDataModelService } from '../service/bDataModel.service';
import { NDataModelService , NSnackbarService } from 'neutrinos-seed-services';
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { userService } from '../../services/user/user.service';
import { Router } from '@angular/router';
/**
 * Service import Example :
 * import { HeroService } from '../../services/hero/hero.service';
 */
@Component({
 selector: 'bh-applyleave',
 templateUrl: './applyleave.template.html'
})
export class applyleaveComponent extends NBaseComponent implements OnInit {
 mm: ModelMethods;
 leaveRequest;
 minDate = new Date();
 leaves = [
 { leave: "annualLeaves", value: "Annual Leave" },
 { leave: "sickLeaves", value: "Sick Leave" }
 ]
 constructor(
 private bdms: NDataModelService,
 private router: Router,
 private snackbar: NSnackbarService,
 private uService: userService
 ) {
 super();
 this.mm = new ModelMethods(bdms);
 }
 ngOnInit() {
 this.dm.leaverequest.fullName = this.uService.user.staff.displayName;
 this.dm.leaverequest.username = this.uService.user.staff.username;
 this.dm.leaverequest.managerName = this.uService.user.staff.managerName;
 this.dm.leaverequest.leaveStatus = "pending";
 }
 getsTime() {
 this.dm.leaverequest.duration = (((this.dm.leaverequest.toDate.getTime() - this.dm.leaverequest.fromDate.getTime()) / (24 * 60 * 60 * 1000)) + 1)
 }
 /**
 * apply leave with validations
 */
 applyLeave(form) {
 // check if invalid duration
 if (this.dm.leaverequest.duration < 1) {
 this.snackbar.openSnackBar('Invalid duration');
 } else {
 if (this.dm.leaverequest.leaveType == "annualLeaves") {
 // check if duration exceeds the available annualLeaves
 if (this.uService.user.leaves.annualLeaves >= this.dm.leaverequest.duration) {
 this.leaveRequest = this.dm.leaverequest
 this.validatePut(form, 'leaverequest', this.dm.leaverequest);
 } else {
 this.snackbar.openSnackBar('Requested number of leaves exceeds available leaves');
 }
 } else {
 // check if duration exceeds the available sickLeaves
 if (this.uService.user.leaves.sickLeaves >= this.dm.leaverequest.duration) {
 this.leaveRequest = this.dm.leaverequest
 this.validatePut(form, 'leaverequest', this.dm.leaverequest);
 } else {
 this.snackbar.openSnackBar('Requested number of leaves exceeds available leaves');
 }
 }
 }
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
 this.router.navigate(['home/userdetail']);
 }, error => {
 // Handle errors here
 console.log(error);
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

### The view of the applyleaves page on runtime:

![The applyleaves page](/resources/Storage/tutorial-create-a-leave-management-system/apply_leaves.png)
