# Login

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/login>

The login page enables users to log in to the application. This is a default page that is created because of the template selected while creating the app.

After a user successfully logs in, he or she would be redirected to the home page.

**The view of the Login page on runtime:**

![The Login page](/resources/Storage/tutorial-create-a-leave-management-system/login.png)

**Page Implementation:**

**Copy CodeJSON/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
import { Component, OnInit, OnDestroy } from '@angular/core'
import { Router } from '@angular/router';
import { user } from '../../models/user.model';
import { loaderComponent } from '../loaderComponent/loader.component';
import { ModelMethods } from '../../lib/model.methods';
import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
import { NDataModelService, NLoginService, NSnackbarService, NSystemService , NHTTPLoaderService } from 'neutrinos-seed-services';
import { MatDialog } from '@angular/material';
import { login } from '../../sd-services/login';
@Component({
 selector: 'bh-login',
 templateUrl: './login.template.html'
})
export class loginComponent extends NBaseComponent implements OnInit, OnDestroy {
 httpSubscribe: any;
 mm: ModelMethods;
 user: user;
 isMobile: Boolean;
 systemService = NSystemService.getInstance();
 constructor(private bdms: NDataModelService,
 private loginService: NLoginService,
 private alertService: NSnackbarService,
 private router: Router,
 private dialog: MatDialog,
 private httpLoaderService: NHTTPLoaderService,
 public uiloginService: login
 ) {
 super();
 this.mm = new ModelMethods(bdms);
 this.user = new user();
 }
 openDialog() {
 const dialogRef = this.dialog.open(loaderComponent, {
 data: { message: 'Authenticating' },
 width: '250px',
 disableClose: true
 });
 }
 ngOnInit() {
 this.checkPlatform();
 this.httpSubscribe = this.httpLoaderService._isHTTPRequestInProgress$.subscribe(value => {
 if (value === true) {
 this.openDialog();
 } else {
 this.dialog.closeAll();
 }
 });
 }
 authenticate() {
 // this.loginService.login(this.user.username, this.user.password, this.user.remember).subscribe((response) => {
 // if (this.loginService.isLoggedIn()) {
 // this.alertService.openSnackBar('User authenticated');
 // this.router.navigate(['/home']);
 // }
 // }, (error) => {
 // this.httpLoaderService.alertError(error);
 // });
 this.uiloginService.authenticate(this.user.username, this.user.password, this.user.remember);
 }
 checkPlatform() {
 const platform = this.systemService.deviceType;
 if (platform !== 'browser') {
 this.isMobile = true;
 this.user.remember = true;
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
 delete(dataModelName, filter) {
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
 ngOnDestroy() {
 this.httpSubscribe.unsubscribe();
 }
}
**
