# myleaves

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/myleaves>

The **myleaves** page displays leave details for the logged-in users.


 Layout


 Drag various components to create the following layout of the **myleaves** page:

 ![Layout of the myleaves page](/resources/Storage/tutorial-create-a-leave-management-system/2019-07-31_09h56_18.png)



 Properties


 Use the following table to configure properties for the **myleaves** page:




 COLUMN-1

 ![Column 1](/resources/Storage/tutorial-create-a-leave-management-system/col1.png)

**Basic Properties**

**Property Name**




 **Property Value**






 class




 margin-tb






 fxFlex




 100






 fxLayoutGap




 1.8em






 Layout Direction




 none






 Perpendicular Direction




 none






 fxShow




 TRUE






 fxHide




 FALSE




 COLUMN-2


 ![Column 2](/resources/Storage/tutorial-create-a-leave-management-system/col2.png)


 **Basic properties:**








 **Property Name**




 **Property Value**






 fxLayoutGap




 1.5em






 fxFLex




 100






 wrap




 wrap






 Perpendicular Direction




 center






 Layout Direction




 center






 fxShow




 TRUE






 fxHide




 FALSE







 **Custom Properties- Key/Value pairs**









 **Property Name**




 **Property Value**






 fxFlex.gt-md




 40






 fxFlex.md




 50






 fxFlex.sm




 60






 fxFlex.xs




 80




 **CARD-1**



 ![Card 1](/resources/Storage/tutorial-create-a-leave-management-system/card%201.png)







 **Property Name**




 **Property Value**






 class




 card




 COLUMN-3

 ![Column 3](/resources/Storage/tutorial-create-a-leave-management-system/col3.png)

**Basic Properties**

**Property Name**




 **Property Value**






 wrap




 wrap






 Layout Direction




 start






 Perpedicular Direction




 stretch






 fxShow




 TRUE






 fxHide




 FALSE




 **ROW-1**

 ![Row 1](/resources/Storage/tutorial-create-a-leave-management-system/row_1.png)Basic Properties







 **Property Name**




 **Property Value**






 wrap




 wrap






 Layout Direction




 center






 Perpendicular Direction




 center






 fxShow




 TRUE






 fxHide




 FALSE




 **HTML 5**

 ![HTMl 5](/resources/Storage/tutorial-create-a-leave-management-system/html_5.png)Basic Properties







 **Property Name**




 **Property Value**






 Element Type




 H4







 Double-click the** H4** HTML editor and add **Leave Information **in it.



 **ROW-2**

 ![Row 2](/resources/Storage/tutorial-create-a-leave-management-system/row_2.png)Basic Properties







 **Property Name**




 **Property Value**






 fxFlex




 100






 wrap




 wrap






 Perpendicular Direction




 none






 Layout Direction




 none






 fxShow




 TRUE






 fxHide




 FALSE








 **COLUMN-4**

 ![Columns 4,5 and 6](/resources/Storage/tutorial-create-a-leave-management-system/col%20and%20textbox.png)Basic Properties





 **Property Name**



 **Property Value**




 fxFlex



 30




 Layout Direction



 center




 Perpedicular Direction



 center




 fxShow



 TRUE




 fxHide



 FALSE




 wrap


 nowrap



 **Custom Properties****Property Name****Property Value** fxFlex.xs100
TEXT AREA 1



 ![Columns 4,5 and 6](/resources/Storage/tutorial-create-a-leave-management-system/col%20and%20textbox.png)Basic Properties







 **Property Name**




 **Property Value**






 placeholder




 Annual Leaves






 value




 {{uService.user.leaves.annualLeaves}}






 disabled



 True





 class




 fullinfix




 COLUMN-5



 ![Columns 4,5 and 6](/resources/Storage/tutorial-create-a-leave-management-system/col%20and%20textbox.png)Basic Properties






 **Property Name**




 **Property Value**






 fxFlex




 30






 Layout Direction




 center






 Perpendicular Direction




 center






 fxShow




 TRUE






 fxHide




 FALSE






 wrap



 nowrap





 fxFlex.xs




 100




 **Custom Property****Property Name****Property Value** fxFlex.xs100
TEXT AREA-2


 ![Columns 4,5 and 6](/resources/Storage/tutorial-create-a-leave-management-system/col%20and%20textbox.png)Basic Properties







 **Property Name**




 **Property Value**






 placeholder




 Sick Leaves






 value




 {{uService.user.leaves.sickLeaves}}






 disabled


 true




 class




 fullinfix




 COLUMN-6


 ![Columns 4,5 and 6](/resources/Storage/tutorial-create-a-leave-management-system/col%20and%20textbox.png)Basic Properties





 **Property Name**



 **Property Value**




 fxFlex



 30




 Layout Direction



 center




 Perpendicular Direction



 center




 fxShow



 TRUE




 fxHide



 FALSE




 wrap


 nowrap




 disabled


 True


 **Custom Properties****Property Name****Property Value** fxFlex.xs100

 TEXT AREA-3



 ![Columns 4,5 and 6](/resources/Storage/tutorial-create-a-leave-management-system/col%20and%20textbox.png)Basic Properties







 **Property Name**




 **Property Value**






 placeholder




 Approved Leaves






 value




 {{uService.user.leaves.approvedLeaves}}






 disabled



 True





 class




 fullinfix




 CARD-2

 ![Card 2](/resources/Storage/tutorial-create-a-leave-management-system/card%202.png)

**Basic Properties**

**Property Name**




 **Property Value**






 *ngIf




 leaveDetails.length == 0






 class




 card








 ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png)

  If you don't find any property in the **Basic Properties**, add that property in the **Custom Properties** section.


HTML 5 - 2


 ![Card 2](/resources/Storage/tutorial-create-a-leave-management-system/card%202.png)


 In the HTML 5 attributes window, select the Element type as **Paragraph**. Double-click the HTML editor and add this sentence: **You have not applied for any leaves**.CARD-3

 ![Card 3](/resources/Storage/tutorial-create-a-leave-management-system/card%203.png)

**Basic and Custom Properties**

**Property Name**




 **Property Value**




 **Custom**






 class




 card











 *ngFor




 let leave of leaveDetails




 TRUE(KV)




 COLUMN-7



 ![Card 3](/resources/Storage/tutorial-create-a-leave-management-system/card%203.png)Basic Properties







 **Property Name**




 **Property Value**






 wrap




 wrap






 Layout Direction




 start






 Perpendicular Direction




 stretch






 fxShow




 TRUE






 fxHide




 FALSE




 ROW-3




 ![Card 3](/resources/Storage/tutorial-create-a-leave-management-system/card%203.png)Basic Properties







 **Property Name**




 **Property Value**






 fxLayoutGap




 1em






 wrap




 wrap






 Layout Direction




 center






 Perpendicular Direction




 center






 fxShow




 true






 fxHide




 false






 fxLayout.xs




 column








 ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png)

  If you don't find any property in the **Basic Properties**, add that property in the **Custom Properties** section.



**COLUMN-8[Flex Layout column]**![Column 5 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set1mylv.png)Basic Properties**Property Name****Property Value** wrapwrapfxflex80Layout DirectioncenterPerpendicular Direction centerfxShowtruefxHidefalse

**ROW-4 [[Flex Layout Row](https://docs.neutrinos.co/component-documentation/1.0.0/components/layouts/flex-layout-row)]**![Row 4 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set1mylv.png)Basic Properties**Property Name****Property Value** fxFlex100Layout DirectioncenterPerpendicular Direction centerfxShowtruefxHidefalsefxLayout.xscolumn (Custom)

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | If you don't find any property in the **Basic Properties**, add that property in the **Custom Properties** section. |
| --- | --- |

**TEXT-4 [[Input](https://docs.neutrinos.co/component-documentation/1.0.0/components/form-controls/input)]**![Text 4 of this page of my Leaves page](/resources/Storage/tutorial-create-a-leave-management-system/set1mylv.png)Basic Properties**Property Name** **Property Value**placeholderFrom Date value{{leave.fromDate | date: 'dd/MMM/yyyy'}} disabledTrue

**TEXT-5 [[Input](https://docs.neutrinos.co/component-documentation/1.0.0/components/form-controls/input)]**![text 5 of my levaes page](/resources/Storage/tutorial-create-a-leave-management-system/set1mylv.png)Basic Properties**Property Name** **Property Value**placeholderTo Date value{{leave.toDate | date: 'dd/MMM/yyyy'}} ssabledTrue

---

**ROW-5 [[Flex Layout Row](https://docs.neutrinos.co/component-documentation/1.0.0/components/layouts/flex-layout-row)]**![Row 5 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set1mylv.png)Basic Properties**Property Name** **Property Value****Custom**fxFlex100Layout Directioncenter  Perpendicular DirectioncenterfxShowTrue
fxHideFalse
fxLayout.xscolumnTRUE(KV)

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | If you don't find any property in the Basic Properties, add that property in the Custom Properties section. |
| --- | --- |

**TEXT-6 [[Input](https://docs.neutrinos.co/component-documentation/1.0.0/components/form-controls/input)]**![text 6 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set1mylv.png)Basic Properties**Property Name** **Property Value**placeholderLeave Typevalue{{leave.leaveType == 'annualLeaves' ? 'Annual' : 'Sick'}} Leave disabledTrue

**TEXT-7 [[Input](https://docs.neutrinos.co/component-documentation/1.0.0/components/form-controls/input)]**![Text 7 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set1mylv.png)Basic Properties**Property Name** **Property Value**placeholderLeave Reasonvalue{{leave.leaveReason}}disabledTrue

**COLUMN-9 [[Flex Layout Column](https://docs.neutrinos.co/component-documentation/1.0.0/components/layouts/flex-layout-column)]**![column 9 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2mylv.png)Basic Properties**Property Name** **Property Value**fxFlex15Layout Directioncenter Perpendicular DirectionstartfxShowTruewrapwrapfxHidefalse

**COLUMN-10 [[Flex Layout Column](https://docs.neutrinos.co/component-documentation/1.0.0/components/layouts/flex-layout-column)]**![Column 10 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2mylv.png)Basic Properties**Property Name** **Property Value**Layout Directioncenter Perpendicular DirectioncenterfxShowTruefxHideFalsewrapwrap

**H4-2 [[H4](https://docs.neutrinos.co/component-documentation/1.0.0/components/form-controls/h4)]**![H5-2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2mylv.png)Basic Properties**Property Name** **Property Value**H4 TextStatus

If you are using version 6.2.x, then the properties are:

| **Property Name** | **Property Value** |
| --- | --- |
| Element Type | Header 4 |

**COLUMN-11 [[Flex Layout Column](https://docs.neutrinos.co/component-documentation/1.0.0/components/layouts/flex-layout-column)]**![Column 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2mylv.png)Basic Properties**Property Name** **Property Value**wrapwrapLayout Directioncenter Perpendicular DirectioncenterfxShowTruefxHideFalse

**ICON-1 [[Icon](https://docs.neutrinos.co/component-documentation/1.0.0/components/form-controls/icon)]**![Icon 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2mylv.png)Basic and Custom Properties**Property Name** **Property Value****Custom**classacceptIconIconNamecheck_circle  *ngIfleave.leaveStatus=='accept' TRUE(KV)titleAcceptedTRUE(KV)



 ICON-2 [[Icon](https://docs.neutrinos.co/component-documentation/1.0.0/components/form-controls/icon)]![Icon 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2mylv.png)Basic and Custom Properties**Property Name** **Property Value****Custom**classacceptIconIconNamecheck_circle  *ngIfleave.leaveStatus=='reject' TRUE(KV)titleRejectedTRUE(KV)
**ICON-3 [[Icon](https://docs.neutrinos.co/component-documentation/1.0.0/components/form-controls/icon)]**![Icon 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2mylv.png)Basic and Custom Properties**Property Name** **Property Value****Custom**classacceptIconIconNamecheck_circle  *ngIfleave.leaveStatus=='pending' TRUE(KV)titlePendingTRUE(KV)

**ROW-6 [[Flex Layout Row](https://docs.neutrinos.co/component-documentation/1.0.0/components/layouts/flex-layout-row)]**![Row 6 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set3mylv.png)Basic Properties**Property Name** **Property Value**wrapwrapLayout Directionend Perpendicular DirectionendClass applyleavebtnfxShowTruefxHideFalse

**FAB BUTTON [[Fab Button](https://docs.neutrinos.co/component-documentation/1.0.0/components/form-controls/fab-button)]**![Fab button of this page](/resources/Storage/tutorial-create-a-leave-management-system/set3mylv.png)Basic and Custom Properties**Property Name** **Property Value****Custom**fabicon<mat-icon>work_off<mat-icontitleApply Leave  TRUE(KV)routerLink/home/applyleave colorprimary

Page Implementation



 On Page load, get the list of all the leaves applied.Copy CodeJavaScriptthis.get('leaverequest', {
 "username": this.uService.user.staff.username}
 , {
 }, {
 _id: -1}
 )





 Complete implementation



 Replace the code in **Ts** tab of the current page in studio with the below code.Copy CodeJavaScript/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
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
 selector: 'bh-myleaves',
 templateUrl: './myleaves.template.html'
})
export class myleavesComponent extends NBaseComponent implements OnInit {
 mm: ModelMethods;
 leaveDetails = [];
 constructor(private bdms: NDataModelService, public uService: userService) {
 super();
 this.mm = new ModelMethods(bdms);
 }
 ngOnInit() {
 this.get('leaverequest', { "username": this.uService.user.staff.username}, {}, {_id: -1})
 }
 get(dataModelName, filter?, keys?, sort?, pagenumber?, pagesize?) {
 this.mm.get(dataModelName, filter, keys, sort, pagenumber, pagesize,
 result => {
 // On Success code here
 this.leaveDetails = result;
 console.log(this.leaveDetails);
 },
 error => {
 // Handle errors here
 console.log(error);
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



 ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png)

  Make sure you copy ad paste only the **Complete page implementation** in the TS editor of the page.



**The view of the myleaves page on runtime:**
![The myleaves page](/resources/Storage/tutorial-create-a-leave-management-system/my_leaves.png)
