# Step 1: Create Page and Page flows

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/how-to-invoke-a-legacy-service-on-a-page>

To invoke a legacy service on a page, you use the **[Use Dependency](/smart/project-page-services-designer-guide/use-dependency-node)** node. In this example, you will be creating a legacy resolver service and will be invoking the service on the page. A resolver resolves data via API or other sources before loading a route.

Consider a scenario where you would add user details to a form. With on click of the **Submit** button, the user details are saved to a list. With on click of the **Show Users List **button, the list of the users added is displayed. On click of a particular user, the details of the user are displayed.

To create a similar example, perform the following steps:

### Step 1: Create Page and Page flows

Add the following pages to your application:

- **userlist: **This page displays the list of users added via the form.
- **userDetail:** This page displays the user details.
- **userForm: **This page provides a form to add the user details.

#### Design the flows on the userForm page

You will be designing the following flows:

**Flow 1**

1. Open the flow designer of the **userform **page. You will see a default [On Init flow](/smart/project-page-services-designer-guide/on-init-flow) on the canvas.
2. Add a [Use Dependency](/smart/project-page-services-designer-guide/use-dependency-node) node **On init** a **Script** node of the flow.
3. In the **Use Dependency **node, enter app/services/userservice/userservice.service as the library and import the following modules to the page and assign them to [page variables](/smart/project-page-services-designer-guide/properties-page-designer/a/h3_545829551). Mark as** Injectable** so that these modules are injected into the page component.
  - userservicService - This module is imported to add and get user details.
4. In the script node of the flow, add the following code to bind the declared variable to the UI component that helps in fetching the name, email, and mobile number of the user:
5. Copy CodeJavaScriptthis.page.user = {
    name: '',
    email: '',
    mobile: '',
    }

**Flow 2**

Create a flow to add user details.

1. Drag and drop a **Start** node and name it as add.
2. Drag and drop an HTTP Request node and set the following properties:
  1. **Method**: POST
  2. **url**: http://localhost:8081/api/adduser
  3. **Return Type**: JSON
  4. **Body**: Select page. and enter user
  5. **Result Mapping**: Select bh. and enter response
3. Drag and drop a **Snackbar **node and enter the following:
  1. **Snackbar Message**: Select **String **type and enter** Added Successfully**
  2. **Action Text**: Select **String **type and enter **Okay**
  3. **Snackbar Duration**: 2000

**Flow 3**

Drag and drop another **Start **node. Name the node **Cancel.**Drag and drop a **Script **node and add the following code:

1. Copy CodeJavaScriptthis.page.user = {
    name: '',
    email: '',
    mobile: '',
   }

#### Design the UI of the userForm page

1. Open the [UI designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the **userForm** page.
2. Drag and drop a **Form** component. In the custom attributes section, add a #userform Key&Value attribute.
3. Drag and drop a **Column **component and set the following attributes:
  1. **style**: height:100vh;
4. Drag and drop an **Input** component inside column 2. Enter the following attributes:
  1. **placeholder**: Name
  2. **[(ngModel)]**: page.user.name
5. Drag and drop another **Input**component inside column 2. Enter the following attributes:
  1. **placeholder**: Email Id
  2. **[(ngModel)]**: page.user.email
6. Drag and drop another **Input** component inside column 2. Enter the following attributes:
  1. **placeholder**: Mobile
  2. **[(ngModel)]**: page.user.mobile
7. Drag and drop a **Row **component and set the following attributes:
  1. **style**: height:100vh;
  2. **Layout Direction**:** Center**
  3. **Perpendicular Direction**: **Center**
8. Drag and drop a **Raised Button** into the row and set the following attributes:
  1. **buttonName**: Submit
  2. (**click**): Select the **Flow Picker** icon. Select the **add **flow in the editor and click** Save.**
  3. **Disabled:** userform.invalid ? true : false
9. Drag and drop a **Raised Button** into the row and set the following attributes:
  1. **buttonName: **Show Users List
  2. **routerLink:** /userlist

---

#### Design the flows in the userlist page

![](/resources/Storage/how-to-articles-8/display-a-bottom-sheet-on-a-page-2021-07-22-1.png)

Perform the following steps:

1. Open the flow designer of the **userlist** page. You will see a default [On Init flow](/smart/project-page-services-designer-guide/on-init-flow) on the canvas.
2. Add a [Use Dependency](/smart/project-page-services-designer-guide/use-dependency-node) node in between the **On init** node and the **Script** node of the on init flow.
3. In the **Use Dependency **node, enter @angular/router as the library and import the following modules to the page and assign them to [page variables](/smart/project-page-services-designer-guide/properties-page-designer/a/h3_545829551). Mark as** Injectable** so that these modules are injected into the page component.
  - ActivatedRoute  - Provides access to information about a route associated with a component that is loaded in an outlet.
  - Router - Enables navigation from one view to the next as users perform application tasks.
4. In the script node of the flow, add the following code to get user data from the resolvers before the page is loaded. (See [step 2](/articles/how-to-articles-8/how-to-invoke-a-legacy-service-on-a-page/a/h3__1039056415) for creating resolvers):
5. Copy CodeJavaScriptif (this.page.activatedRoute.snapshot.data && this.page.activatedRoute.snapshot.data.userList) {
    this.page['userlist'] = this.page.activatedRoute.snapshot.data.userList;
    console.log('this.page.userlist====',this.page['userlist']);
   }

#### Flow 2

Create a flow to open the user details.

1. Drag and drop a **Start** node.![](/resources/Storage/how-to-articles-8/display-a-bottom-sheet-on-a-page-2021-07-22-2.png)
  1. Enter the name as **openUserDetail**.
  2. Add an input variable named data of type any and toggle the **Output**.
2. Drag and drop a **Navigation **node and enter the following:

- **Path to navigate**: Select /userdetails/:email from the drop-down
- **Path Parameters**: Select **bh.input** and enter **data.email**

#### Design the UI of the userlist page

1. Open the [UI designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the **userlist** page.
2. Drag and drop a **Form** component. In the custom attributes section, add a #userform Key&Value attribute.
3. Drag and drop a **Column **component and set the following attributes:
  1. style: height:100vh;
  2. Layout Direction:** Center**
  3. Perpendicular Direction: **Center**
4. Drag and drop a **Column **component.
5. Drag and drop a **list** component inside the column.
6. Drag and drop another **List****Item **component inside the list component and set the style as border-bottom: 1px solid black
7. Drag and drop an **HTML 5** Component inside List item 1 and set the Element Type as h3. Double click the HTML editor and enter Users List
8. Drag and drop a **List****Item **component inside the list component below list item 1.
9. Drag and drop a **Row **component and set the **fxFlex** to 100.
10. Drag and drop an **HTML 5** Component inside List item 2 and set the Element Type as h4. Double click the HTML editor and enter Name.
11. Drag and drop another **HTML 5** Component inside List item 2 and set the Element Type as h4. Double click the HTML editor and enter Email
12. Drag and drop another **List****Item **component inside the list component below list item 2.
13. Drag and drop a **Row **component and set the **fxFlex** to 100.
14. Drag and drop an **HTML 5** Component inside List item 2 and set the Element Type as **div**. Double click the HTML editor and enter {{user.name}}
15. Drag and drop another **HTML 5** Component inside List item 2 and set the Element Type as **div**. Double click the HTML editor and enter {{user.email}}

---

#### Design the flows on the userDetails page

You will be designing the following flows:

1. Open the flow designer of the **userDetails** page. You will see a default [On Init flow](/smart/project-page-services-designer-guide/on-init-flow) on the canvas.
2. Add a [Use Dependency](/smart/project-page-services-designer-guide/use-dependency-node) node **On init** a **Script** node of the flow.
3. In the **Use Dependency **node, enter @angular/router as the library and import the following modules to the page and assign them to [page variables](/smart/project-page-services-designer-guide/properties-page-designer/a/h3_545829551). Mark as** Injectable** so that these modules are injected into the page component.
  1. ActivatedRoute: Provides access to information about a route associated with a component that is loaded in an outlet.
4. In the script node of the flow, add the following code to validate the data from the resolver and assign it to a variable:
5. Copy CodeJavaScript
   if (this.page.activatedRoute.snapshot.data && this.page.activatedRoute.snapshot.data.userDetails) {
    this.page['userDetails'] = this.page.activatedRoute.snapshot.data.userDetails.length > 0 ? this.page.activatedRoute.snapshot.data.userDetails[0] : null;
    console.log('this.page.userDetails====',this.page['userDetails']);
   }

this.page.activatedRoute.snapshot.data contains the resolver data and this.page['userDetails'] will hold the user details after the validation of the resolver data.

#### Design the UI of the userDetails page

1. Open the [UI designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the **share** page.
2. Drag and drop a **Form** component. In the custom attributes section, add a #userform Key&Value attribute.
3. Drag and drop a **Column **component and set the following attributes:
  1. style: height:100vh;
  2. Layout Direction:** Center**
  3. Perpendicular Direction: **Center**
4. Drag and drop a **Column **component and set the **fxFlex** to 100.
5. Drag and drop a **list** component inside the column.
6. Drag and drop another **List****Item **component inside the list component and set the style as border-bottom: 1px solid black
7. Drag and drop an **HTML 5** Component inside List item 1 and set the Element Type as h3. Double click the HTML editor and enter Users Detail
8. Drag and drop a **List****Item **component inside the list component below list item 1 and set the style as border-bottom: 1px solid lightgray; cursor: pointer
9. Drag and drop a **Row **component and set the **fxFlex** to 100.
10. Drag and drop an **HTML 5** Component inside List item 2 and set the Element Type as h3. Double click the HTML editor and enter Name.
11. Drag and drop another **HTML 5** Component inside the List item 2 and set the Element Type as h4. Double click the HTML editor and enter {{page.userDetails.name}}
12. Drag and drop another **List****Item **component inside the list component below list item 2 and set the style as border-bottom: 1px solid lightgray; cursor: pointer.
13. Drag and drop a **Row **component and set the **fxFlex** to 100.
14. Drag and drop an **HTML 5** Component inside List item 2 and set the Element Type as div. Double click the HTML editor and enter Email
15. Drag and drop another **HTML 5** Component inside the List item 2 and set the Element Type as div. Double click the HTML editor and enter {{page.userDetails.email}}
16. Drag and drop another **List****Item **component inside the list component below list item 2 and set the style as border-bottom: 1px solid lightgray; cursor: pointer.
17. Drag and drop a **Row **component and set the **fxFlex** to 100.
18. Drag and drop an **HTML 5** Component inside List item 2 and set the Element Type as div. Double click the HTML editor and enter Mobile
19. Drag and drop another **HTML 5** Component inside List item 2 and set the Element Type as div. Double click the HTML editor and enter {{page.userDetails.mobile}}

---

### Step 2: Create Legacy Service

Create the following legacy services in your application:

#### _userlist: To return a list of users

```javascript
/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE CLASS NAME*/import { Injectable } from '@angular/core';import { userService } from 'app/services/user/user.service';import { user } from 'app/sd-services/user'import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';@Injectable()export class _userslistService implements Resolve<any> {constructor( public router: Router,public _userService:userService, public _user: user) {    }    resolve(        route: ActivatedRouteSnapshot,        state: RouterStateSnapshot    ): any {                return this._user.getUsersList().then(res=>{            return res.local.usersList;         })    }}
```

#### user: To get the details of a user using the email id.

```javascript
/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE CLASS NAME*/import { Injectable } from '@angular/core';import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';import { user } from 'app/sd-services/user'@Injectable()export class userService implements Resolve<any> {    constructor( public _user: user) {    }    resolve(        route: ActivatedRouteSnapshot,        state: RouterStateSnapshot    ): any {         const email = route.params['email'];        return this._user.getUserById(email).then(res=>{            console.log(res)            return res.local.userDetails;         })    }}
```

---

### Step 3: Create Client Services

In this section, create a service to add and get user details.

![](/resources/Storage/how-to-articles-8/how-to-invoke-a-legacy-service-on-a-page-2021-08-16.png)

#### Flow 1

1. Open the Client Services designer.
2. Drag and drop a **Start node**. Add userslist variable.
3. Drag and drop an HTTP Request node and set the following properties:
  1. Method: Get
  2. URL: http://localhost:8081/api/getUsersList
  3. Return Type: JSON
  4. Result mapping: select **bh.local** and enter **userslist **

**Flow 2**

1. Drag and drop a **Start node**.
  1. Add email as an **input **variable.
  2. Add userDetails as the **local **variable.
2. Drag and drop a Script node and enter the following code:
3. Copy CodeJavaScriptbh.url = `http://localhost:8081/api/getUsersById?email=${bh.input.email}`
4. Drag and drop an HTTP Request node and set the following properties:
  1. Method: Get
  2. URL: Select bh. and enter **url**
  3. Return Type: JSON
  4. Result mapping: select **bh.local** and enter **userDetails**

---

### Step 4: Create Server Services

In this section, create a service to add and get user details.

#### Flow 1

1. Open the Server Services designer.
2. Drag and drop an **HTTP In node**. Set the following properties:
  1. **Method**: POST
  2. **Path**: adduser
3. Drag and drop a MongoDB node. Set the following properties:
  1. **Config**: Select your database config. See [MongoDB documentation](/smart/project-server-side-service-designer/mongodb-node) to see how to configure your database.
  2. **Operation**: insertOne
  3. **Document**: Select bh.input and enter body
  4. **Result Mapping**: Select bh. and enter result.
4. Drag and drop a Script node and enter the following code:
5. Copy CodeJavaScriptconsole.log('user',bh.result);
6. Drag and drop an HTTP Out node and set the following properties:
  1. **Return Type**: JSON
  2. **Status Code**: 200
  3. **Response Body**: Select bh. and enter result

**Flow 2**

1. Drag and drop an **HTTP In node**. Set the following properties:
  1. **Method**: Get
  2. **Path**: getUsersList
2. Drag and drop a Script node and enter the following code:
3. Copy CodeJavaScriptbh.query={}
4. Drag and drop a MongoDB node. Set the following properties:
  1. **Config**: Select your database config. See [MongoDB documentation](/smart/project-server-side-service-designer/mongodb-node) to see how to configure your database.
  2. **Operation**: find
  3. Query: Select **bh**. and enter query.
  4. **Document**: Select string and enter userdetail
  5. **Result Mapping**: Select bh. and enter response
5. Drag and drop an HTTP Out node and set the following properties:
  1. **Return Type**: JSON
  2. **Status Code**: 200
  3. **Response Body**: Select bh. and enter response

**Flow 3**

1. Drag and drop an **HTTP In node**. Set the following properties:
  1. **Method**: Get
  2. **Path**: getUsersById
2. Drag and drop a Script node and enter the following code:
3. Copy CodeJavaScriptbh.query={email: `${bh.input.query.email}`}
   console.log(bh)
4. Drag and drop a MongoDB node. Set the following properties:
  1. **Config**: Select your database config. See [MongoDB documentation](/smart/project-server-side-service-designer/mongodb-node) to see how to configure your database.
  2. **Operation**: find
  3. **Query**: Select **bh**. and enter query.
  4. **Document**: Select string and enter userdetail
  5. **Result Mapping**: Select bh. and enter response
5. Drag and drop an HTTP Out node and set the following properties:
  1. **Return Type**: JSON
  2. **Status Code**: 200
  3. **Response Body**: Select bh. and enter response

---

### Step 5: Configure Routes

In this section, you are configuring the page routes and resolvers created in the legacy service.

- The [{userList : _userslistService}](/articles/how-to-articles-8/how-to-invoke-a-legacy-service-on-a-page/a/userlistresolver) resolver is used in the userlist route to get the user list before the page is loaded.
- The [{userDetails : userService}](/articles/how-to-articles-8/how-to-invoke-a-legacy-service-on-a-page/a/userserviceresolver) resolver is used in the userdetails route to get the user details depending on the email id before the page is loaded.

Add the following routes in the [Routes editor](/smart/project-sample-how-to-guide/adding-routes).

| **Path** | **Page** | **Resolver** |
| --- | --- | --- |
| userform | userform |  |
| userlist | userlist | {userList : _userslistService} |
| userdetails/:email | userdetails | {userDetails : userService} |

![](/resources/Storage/how-to-articles-8/display-a-bottom-sheet-on-a-page-2021-07-23-1.png)

---

After creating this app, initialize and live preview the app.

The user's list is displayed like this:

The user details are displayed like this:
