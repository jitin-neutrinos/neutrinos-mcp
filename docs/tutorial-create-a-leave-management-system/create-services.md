# Create Services

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/create-services>

`On the Neutrinos Platform, services enable information sharing among pages and other services.

**Services for LMS**

For the Leave Management System (LMS) app, you need to create and configure the following services:

1. UI Services

- **login**: sets roles associated with the users.

2. Legacy Services

- **user**: Shares user data across Pages.
- **homeresolver**: Fetches the logged-in user’s data and populates the data in **userservice**. This service also enables you to load data from a remote server before the route is activated and the component is rendered into the app.

---

**Creating a UI Service**

1. To create a UI service, click **S****ervices** on the left and then click **UI ****Services.**

![Create UI services](/resources/Storage/tutorial-create-a-leave-management-system/servicesLMS.png)

2.  Click on the plus ![](/resources/Storage/tutorial-create-a-leave-management-system/add.png) icon in front of the UI services, and enter the name of the service. For example, loginservice. Now, click on **ADD**.

![adding a UI service](/resources/Storage/tutorial-create-a-leave-management-system/uiloginserv.png)

**login service configuration**

1. Drag and drop the **START** node to the service editor. In the start properties window, add the following properties:

- **name**: authenticate
- **function name**: authenticate
- input properties: Enter the following keys. The value for these keys will be associated at runtime.
- **key**: username
- **key**: password
- **key**: remember

![Properties of the start node](/resources/Storage/tutorial-create-a-leave-management-system/startnode.png)

2. Drag and drop a **SCRIPT** node. Double click the node and add the following code to the code editor window.

```javascript
// bh.local.res = await bh.system.loginService.login(bh.input.lkdjfklj, )bh.system.loginService.login(bh.input.username, bh.input.password, bh.input.remember).subscribe((response) =>     {      if (bh.system.loginService.isLoggedIn()) {        bh.system.snackbarService.openSnackBar('User authenticated');        bh.system.router.navigate(['/home']);      }    }, (error) => {      bh.system.httpLoaderService.alertError(error);    });
```

3. Connect the nodes.

![the overall view of the loginservice](/resources/Storage/tutorial-create-a-leave-management-system/UIservice.png)

---

**Creating a Legacy Service**

1. Click on the **ADD ![](/resources/Storage/tutorial-create-a-leave-management-system/add.png)**icon on the menu and select the Legacy Service option.

![Adding legacy service to the app](/resources/Storage/tutorial-create-a-leave-management-system/Legacyservice.png)

2. Enter the name of the service and click on **ADD.**

![Name of the legacy service of the app](/resources/Storage/tutorial-create-a-leave-management-system/addlegacy.png)

**user service implementation**

```json
/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE CLASS NAME*/import { Injectable } from '@angular/core';@Injectable()export class userService {    private __currentUser    set user(user) {        this.__currentUser = user;    }    get user() {        return this.__currentUser;    }    // check whether the logged in user is 'Manager'    isManager( ){        if(this.__currentUser) {            return this.__currentUser.staff.groupList.indexOf('Manager') > -1;        }        return null;    }    getusername(){        return this.__currentUser.staff.username;    }}
```

**homeresolver service implementation**

```json
/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE CLASS NAME*/import { Injectable } from '@angular/core';import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';import { NDataModelService, NSessionStorageService, NLoginService } from 'neutrinos-seed-services';import { Observable } from 'rxjs';import { userService } from '../user/user.service';import { Router } from '@angular/router';@Injectable()export class homeresolverService implements Resolve<any> {    constructor(private dms: NDataModelService,        private ss: NSessionStorageService,        private uService: userService,        private loginService: NLoginService,        private router: Router    ) {        if (this.loginService.isLoggedIn()) {            this.router.navigate(['home']);        }    }    resolve(route: ActivatedRouteSnapshot,state: RouterStateSnapshot): Observable<any> | Promise<any> | any     {        return new Promise((resolve, reject) => {            const username = this.ss.getValue('userObj')['username']            this.dms.get('employee', {                'staff.username': username            }).subscribe(result => {                this.uService.user = result[0];                return resolve();            }, error => {                return reject(error);            })        })    }}
```

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | The Service class name and file name are auto-generated, and to import and use them in a Page a standard path is used. For example, for User Service that path would be import { userService } from '../../services/User/user.service |
| --- | --- |

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | NgService or Service can be used interchangeably. |
| --- | --- |
