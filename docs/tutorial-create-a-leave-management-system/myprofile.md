# myprofile

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/myprofile>

The **myprofile** page displays details such as name and employee ID of the logged-in user.


 Layout


 Drag various components to create the following layout of the myprofile page:


 ![The layout of this page](/resources/Storage/tutorial-create-a-leave-management-system/whole%20layout.png)






 Properties



 Use the following table to configure properties for the **myprofile **page:


 **COLUMN-1**


 ![column1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set1.png)


 **Basic Properties**

 **Property name****Property Value**




 Layout DirectionCenter


 Perpendicular Direction
 Center


 fxshow
  true


  fxhide
  false


  fxFlex
  100



 Wrap wrap


 Class
 Margin-tb



  fxLayoutGap
  1em

---

**CARD-1**


 ![Card 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set1.png)


 Basic Properties




 **Property name**

 **Property Value**




 Class

 card

ROW-2
 ![Row 2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2.png)

 **Basic properties**





  **Property name**
  **Property Value**




  Layout Direction
  Center


 Perpendicular Direction
  start


  fxshow
  true


 fxhide
  false


 fxFlex

 100


  Wrap
 wrap


 Class
 Margin-tb

**COLUMN-2**


 ![column2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2.png)


 **Basic Properties**

  **Property name****Property Value**



 Layout DirectionCenterPerpendicular Direction Center

  fxshow true
 fxhidefalse
  fxFlex 45
 fxFlex.xs100
 Wrap wrap
 Class Margin-tb

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | If you don't find any property in the Basic Properties, add that property in the Custom Properties section. |
| --- | --- |

**TEXT-1 **


 ![Text 1 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2.png)


 **Basic Properties**



 **Property name****Property Value**


 PlaceholderFirst Name
 Value{{uService.user.staff.firstName}}
 disabledtrue

**COLUMN-3**


 ![column 3 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2.png)


 **Basic and Custom Properties**





 **Property name**
  **Property Value**
 **Custom**




 Layout Direction
  Center



 Perpendicular Direction
 Center




 fxshow
 true




  fxhide
 false



 fxFlex
 45




  fxFlex.xs
 100
 TRUE(KV)


 Wrap
 wrap




 Class
  Margin-tb

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | If you don't find any property in the Basic Properties, add that property in the Custom Properties section. |
| --- | --- |

**TEXT-2 **


 ![Text 2 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set2.png)


 **Basic Properties**




 **Property name****Property Value**


 placeholder Last Name
 value{{uService.user.staff.lastName}}
  disabled true

**ROW-3**
 ![Row 3 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set3.png)


 **Basic Properties**




 **Property name**  **Property Value**


 Layout DirectionCenter
 Perpendicular Direction start
  fxhidefalse
  fxFlex100
  Wrap wrap

**COLUMN-4**


 ![Column4 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set3.png)


 **Basic and Custom Properties**




 **Property name**  **Property Value** **Custom**


  Layout Direction Center

 Perpendicular DirectionCenter

 fxshowtrue

 fxhide false
 fxFlex 45

 fxFlex.xs 100
TRUE(KV)
 Wrap wrap

**TEXT-3**


 ![Text 3 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set3.png)


 **Basic Properties**



  **Property name** **Property Value**


  placeholder Email ID
 value{{uService.user.staff.userName}}
  disabled true

**COLUMN-5**


 ![Column 5 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set3.png)


 Basic and Custom Properties





  **Property name****Property Value** **Custom**




 Layout Direction
  Center



 Perpendicular Direction
 Center


  fxshow
  true



 fxhide
  false



  fxFlex
  45



  fxFlex.xs
  100
 TRUE(KV)


 Wrap
  wrap

**TEXT-4 [[Input](https://docs.neutrinos.co/component-documentation/1.0.0/components/form-controls/input)]**


 ![Text 4 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set3.png)


 **Basic Properties**



  **Property name****Property Value**


  placeholder Employee ID
  value{{uService.user.staff.employeeID}}
 disabledtrue

**ROW-4**


 ![Row 4 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set4.png)


 **Basic Properties**




  **Property name**
  **Property Value**




 Layout Direction
 Center


 Perpendicular Direction
  start


  fxshow
 true


  fxhide
 false


  fxFlex
 100


  wrap
 wrap

**COLUMN-6 **


 ![column 6 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set4.png)


 **Basic and Custom Properties**





 **Property name**
 **Property Value**
 **Custom**




  Layout Direction
  Center



 Perpendicular Direction
  Center



  fxshow
  true



  fxhide false



  fxFlex
  45



  fxFlex.xs
  100 TRUE(KV)


  Wrap wrap

**TEXT-5**


 ![text 5 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set4.png)


 **Basic Properties**

 **Property name** **Property Value**


 placeholder Department
 value{{uService.user.staff.department}}
 disabledtrue

**COLUMN-7 **


 ![Column 7 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set4.png)


 **Basic and Custom Properties**





 **Property name**
 **Property Value**
  **Custom**




  Layout Direction
  Center



 Perpendicular Direction
  Center



  fxshow
  !uService.isManager()



  fxFlex
  45



  fxFlex.xs
  100
 TRUE(KV)


  Wrap
  wrap

**TEXT-6**


 ![text 6 of this page](/resources/Storage/tutorial-create-a-leave-management-system/set4.png)


 **Basic Properties**



  **Property name****Property Value**


 placeholderManager
  value{{uService.user.staff.managerName}}
 disabledtrue

Page Implementation



 Just import **userService ** service and inject the service in the Page as shown


 Copy CodeJavaScriptconstructor(private bdms: NDataModelService, public uService: userService) {
 super();
 this.mm = new ModelMethods(bdms);
}





 ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png)


 Note that injected service has instance variable **uService** made **public **to make it accessible via the HTML template






 Complete Implementation


 Copy CodeJavaScript/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import {
 Component, OnInit }
from '@angular/core'
 import { ModelMethods } from '../../lib/model.methods';
// import { BDataModelService } from '../service/bDataModel.service';
import { NDataModelService } from 'neutrinos-seed-services';
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { userService } from '../../services/user/user.service';

 /**
* Service import Example :
* import { HeroService } from '../services/hero/hero.service';
*/

 @Component({
 selector: 'bh-myprofile',
 templateUrl: './myprofile.template.html'
 }
 )

 export class myprofileComponent extends NBaseComponent implements OnInit {
 mm: ModelMethods;

 constructor(private bdms: NDataModelService, public uService: userService) {
 super();
 this.mm = new ModelMethods(bdms);
 }

 ngOnInit() {
 // console.log(this.uService.staff.firstName)
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
 }
 )
 }


 }










 ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png)


 Make sure you copy ad paste only the **Complete page implementation** in the TS editor of the page.

---

**The view of myprofile page on runtime:**
