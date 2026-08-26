# TEXT-1

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/myapprovals>

The **myapprovals** page displays the leave requests applied by the employees of a department to the logged-in manager needs to take action on. In addition, it displays the leaves the logged-in manager has approved.

**Layout**

Drag and drop various components from the palette section to create the following layout of the myapprovals page:

**Properties**

To every component that is dragged and dropped into the page container, the properties should be set if required.

**COLUMN-1**

![Column 1 of the myapprovals page of the LMS app](/resources/Storage/tutorial-create-a-leave-management-system/column1myap.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | none |
| Perpendicular Direction | none |
| fxshow | true |
| fxhide | false |
| Wrap | Nowrap |
| Class | margin-tb |

**Custom Properties**

Add a new custom attribute using the Custom Property field. Enter `fxFill` in the key field and click **Add**. You will see the `Layout Fill`attribute added (with the `**Fill**` option selected) to the Attributes window.

---

**CARD-1**

![Card 1 of the myapproval page of the LMS](/resources/Storage/tutorial-create-a-leave-management-system/card1myap.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Class | card |

**Custom Properties**

In the Custom Property field, select Key/Value option. Enter `fxFlexAlign` in the key field and `center` in the value field. Click **Add**.

Add another key/value field. Enter `*ngIf` in the key field and `leaveRequests.length == 0` in the value field. Click **Add**.

**CARD TITLE**

**Basic properties**

| **Property name** | **Property Value** |
| --- | --- |
| Title | No active leaves for approval |

---

**COLUMN-2**

![Column 2 of the myapproval page of the lms](/resources/Storage/tutorial-create-a-leave-management-system/column2myap.png)

**Basic Properties**

**Property name****Property Value**Layout DirectionnonePerpendicular DirectionnonefxshowtruefxhidefalseWrapwrap**CARD-2**![Card 2 of the myapproval page of the LMS](/resources/Storage/tutorial-create-a-leave-management-system/card2myap.png)**Basic Properties****Property name****Property Value**Class card

**Custom Properties**
In the Custom Property field, select Key/Value option. Enter  `*ngFor`  in the key field and let leaves of leaveRequests in the value field. Click **Add**.ROW-1




![Row1 of the myapproval page](/resources/Storage/tutorial-create-a-leave-management-system/row1myap.png)**Basic Properties****Property name****Property Value**Layout DirectioncenterPerpendicular DirectioncenterfxshowtruefxhidefalseWrapwrapfxFlex100fxLayoutGap1.5em**COLUMN-3**![Column 3 of the myapproval page of the lms](/resources/Storage/tutorial-create-a-leave-management-system/column3myap.png)**Basic Properties****Property name****Property Value**Layout DirectioncenterPerpendicular DirectioncenterfxshowtruefxhidefalseWrapwrapfxFlex100fxLayoutGap0.8em**COLUMN-4**![Column4 of the myapproval page of the lms](/resources/Storage/tutorial-create-a-leave-management-system/column4myap.png)**Basic Properties****Property name****Property Value**Layout DirectionStartPerpendicular DirectionStretchfxshowtruefxhidefalseWrapwrap

**COLUMN-5**![Column 5 of the my approval page of lms](/resources/Storage/tutorial-create-a-leave-management-system/Column5%2Cmyap.png)**Basic Properties****Property name****Property Value**Layout DirectioncenterPerpendicular DirectioncenterfxshowtruefxhidefalseWrapwrapfxFlex28

**Custom Properties**

In the Custom Property field, select Key/Value option. Enter `fxFlex.xs` in the key field and `100` in the value field. Click **Add**.

#### TEXT-1

![Text 1 of the myapproval page of the LMS](/resources/Storage/tutorial-create-a-leave-management-system/text1myap.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | Employee Name |
| Value | {{leaves.fullName}} |
| disabled | true |

---

#### TEXT-2

![text 2 of the myapprovals page of lms](/resources/Storage/tutorial-create-a-leave-management-system/text2myap.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | From Date |
| Value | {{leaves.fromDate\|date:'DD/MM/YYYY'}} |
| disabled | true |

---

#### TEXT-3

![Text 3 of the myapproval page of lms](/resources/Storage/tutorial-create-a-leave-management-system/text3myap.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | To Date |
| Value | {{leaves.fromDate\|date:'DD/MM/YYYY'}} |
| disabled | true |

---

**TEXT-4**![Text 4 of the myapproval page of lms](/resources/Storage/tutorial-create-a-leave-management-system/text4myap.png)**Basic Properties****Property name****Property Value**Place HolderleaveTypeValue{{leaves.leaveType == 'annualLeaves'? 'Annual': 'Sick'}} Leave disabledtrue

---

#### TEXT-5

**![Text 5 of the myapprovals page of the lms](/resources/Storage/tutorial-create-a-leave-management-system/text5myap.png)**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | Duration |
| Value | {{leaves.duration}} Days |
| disabled | true |

---

#### TEXT-6

![text 6 of the myapproval page of the lms](/resources/Storage/tutorial-create-a-leave-management-system/text6myap.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Place Holder | Leave Reason |
| Value | {{leaves.leaveReason}} |
| disabled | true |

---

#### PARAGRAPH-1

![Paragraph 1 of the myapproval page of the lms](/resources/Storage/tutorial-create-a-leave-management-system/para1myap.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Text | Status |
| Class | h4 |

If you are using version **6.2.x,** the following are the properties for this component:

| **Property name** | **Property Value** |
| --- | --- |
| Element type | Header 4 |

---

#### ROW-2

![Row 2 of myapproval page of lms](/resources/Storage/tutorial-create-a-leave-management-system/row2myap.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | none |
| Perpendicular Direction | none |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |
| fxLayoutGap | 1em |

---

**COLUMN-6**

**![Column6 of myapproval page](/resources/Storage/tutorial-create-a-leave-management-system/column6myap.png)**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | center |
| Perpendicular Direction | center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |
| fxFlex | 28 |

**Custom Properties**

In the Custom Property field, enter `fxFlex.xs` in the key field and `100` in the value field. Click **Add**.

---

#### COLUMN-7

**![Column7 of the myapprovals page of lms](/resources/Storage/tutorial-create-a-leave-management-system/Column7myap.png)**

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| Layout Direction | center |
| Perpendicular Direction | center |
| fxshow | true |
| fxhide | false |
| Wrap | wrap |
| fxFlex | 28 |

**Custom Properties**

In the Custom Property field, enter `fxFlex.xs` in the key field and `100` in the value field. Click **Add**.

---

**MINI FAB BUTTON-1**

![Mini fabbutton 1 of myapproval page](/resources/Storage/tutorial-create-a-leave-management-system/minifab1myap.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| fabicon | <mat-icon>check_circle</mat-icon> |
| (click) | accept(leaves) |
| Color | none |
| Class | acceptIcon |
| disabled | leaves.leaveStatus=='accept' |

**Custom Properties**

Add two Key/Value properties in the custom properties, enter the title in the key field and  Accept in the value field.

---

**MINI FAB BUTTON-2**

![Mini fab button 2 of the myapproval page of lms](/resources/Storage/tutorial-create-a-leave-management-system/minifab2myap.png)

**Basic Properties**

| **Property name** | **Property Value** |
| --- | --- |
| fabicon | <mat-icon>cancel</mat-icon> |
| (click) | reject(leaves) |
| Color | default |
| Class | rejectIcon |
| disabled | leaves.leaveStatus=='reject' |

**Custom Properties**

Add a Key/Value properties in the custom properties, enter the title in the key field and  Reject in the value field.

---

### Page Implementation

On page load we will query our database to get all the leaves applied for the **displayName**, this can be done by writing the following the query in **ngOnInit()** method

Copy CodeJavaScript// get DM API to query the leaverequest collection by manager's displayName
this.get('leaverequest',
 { "managerName": this.uService.user.staff.displayName },
 {},
 { _id: -1 }
 );

If the manager accepts the leave request, you have to update **leaverequest** by the new status, and also update the **employee** leave information. We will implement this logic by using the following method:

Copy CodeJavaScriptaccept(leave) {
 leave.leaveStatus = 'accept';

 // updating leave requests
 this.updateById('leaverequest', leave._id, leave);

 // update query for employee
 let leaveKey = 'leaves.' + leave.leaveType;
 let update = {'$inc': {}}
 update['$inc'][leaveKey] = -leave.duration;
 update['$inc']['leaves.approvedLeaves'] = leave.duration;

 // update DM API
 this.update('employee', update, {
 'staff.username': leave.username }
 , {
 });
}

If the manager rejects the leave request, we will only update the **leaverequest **collection.

Copy CodeJavaScriptreject(leave) {
 leave.leaveStatus = 'reject';
 this.updateById('leaverequest', leave._id, leave);
}

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | The** leaveRequests **method variable is used to store all the leaves. |
| --- | --- |

---

### Complete implementation

Replace the code in the **Ts** tab of the current page in the studio with the below code.

Copy CodeJavaScript/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import { Component, OnInit } from '@angular/core'
import { ModelMethods } from '../../lib/model.methods';
// import { BDataModelService } from '../service/bDataModel.service';
import { NDataModelService, NSnackbarService } from 'neutrinos-seed-services';
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { userService } from '../../services/user/user.service';
/**
 * Service import Example :
 * import { HeroService } from '../../services/hero/hero.service';
 */
@Component({
 selector: 'bh-myapprovals',
 templateUrl: './myapprovals.template.html'
})
export class myapprovalsComponent extends NBaseComponent implements OnInit {
 mm: ModelMethods;
 leaveRequests = [];
 constructor(
 private bdms: NDataModelService,
 private uService: userService,
 private alertService: NSnackbarService,
 ) {
 super();
 this.mm = new ModelMethods(bdms);
 }
 ngOnInit() {
 this.get('leaverequest', { "managerName": this.uService.user.staff.displayName }, {}, { _id: -1 });
 }
 reject(leave) {
 leave.leaveStatus = 'reject';
 this.updateById('leaverequest', leave._id, leave);
 }
 accept(leave) {
 leave.leaveStatus = 'accept';
 // updating leave requests
 this.updateById('leaverequest', leave._id, leave);
 // update for employee
 let leaveKey = 'leaves.' + leave.leaveType;
 let update = {
 '$inc': {}
 }
 update['$inc'][leaveKey] = -leave.duration;
 update['$inc']['leaves.approvedLeaves'] = leave.duration;
 this.update('employee', update, { 'staff.username': leave.username }, {});
 }
 get(dataModelName, filter?, keys?, sort?, pagenumber?, pagesize?) {
 this.mm.get(dataModelName, filter, keys, sort, pagenumber, pagesize,
 result => {
 // On Success code here
 this.leaveRequests = result;
 console.log()
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
 this.alertService.openSnackBar('Leave status updated');
 }, error => {
 // Handle errors here
 this.alertService.openSnackBar(error);
 })
 }
}

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | Make sure you copy ad paste only the **Complete page implementation** in the TS editor of the page. |
| --- | --- |

---

### The view of the myapprovals page on runtime:

![The myapprovals page](/resources/Storage/tutorial-create-a-leave-management-system/my_approvals.png)
