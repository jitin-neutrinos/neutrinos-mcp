# Migrate to 3.3.1

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migrate-to-3>

Perform the following steps to migrate your app to Neutrinos Studio 3.3.1:

- If you have used any of the following services in components, replace them with the following imports:

**Old Class Name**


 **New Class Name**


 **Import Snippet**


 **Import Form**






 BAuthGaurd


 NAuthGuardService



 import { NDataSourceService }


  from 'neutrinos-seed-services;



 neutrinos-seed-services




 BDataModelsService



 NDataModelService




 `import { NDataModelService } `


 ` from 'neutrinos-seed-services';`



 neutrinos-seed-services




 BDataSourceService


 NDataSourceService






 import { NDataSourceService }


  from 'neutrinos-seed-services';






 neutrinos-seed-services







 BHttp





 NHttpService






 `import { NHttpService } `


 ` from 'neutrinos-seed-services';`



 neutrinos-seed-services








 BLocalStorageService



 NLocalStorageService






 `import { NLocalStorageService } `


 ` from 'neutrinos-seed-services';`



 neutrinos-seed-services







 BLoginService





 NLoginService






 `import { NLoginService } `


 ` from 'neutrinos-seed-services';`



 neutrinos-seed-services







 BLogoutService





 NLogoutService






 `import { NLogoutService } `


 ` from 'neutrinos-seed-services';`



 neutrinos-seed-services







 BSessionStorage





 NSessionStorageService






 import { NSessionStorageService }


  from 'neutrinos-seed-services';






 neutrinos-seed-services







 BTokenService





 NTokenService






 `import { NTokenService } from `


 ` 'neutrinos-seed-services';`



 neutrinos-seed-services








 NotificationService



 NNotificationService






 `import { NNotificationService } from `


 ` 'neutrinos-seed-services';`



 neutrinos-seed-services







 PubSubService





 NPubSubService






 import { NPubSubService }


  from 'neutrinos-seed-services';






 neutrinos-seed-services







 SystemService





 NSystemService






 `import {NSystemService} `


 ` from 'neutrinos-seed-services';`



 neutrinos-seed-services








 BAppService (for snack bar)



 NSnackbarService






 `import { NSnackbarService } `


 ` from 'neutrinos-seed-services';`



 neutrinos-seed-services








 BAppService(for the alert component)



 NAlertService






 `import { NAlertService } `


 ` from 'neutrinos-module';`



 neutrinos-module





 BHFileUploadComponent



 NFileUploadComponent






 `import { NFileUploadComponent } `


 ` from 'neutrinos-module';`




 neutrinos-module





 FileIOService





 NFileIOService






 `import { NFileIOService } `


 ` from 'neutrinos-module';`




 neutrinos-module





 Http





 HttpClient






 `import { HttpClient } from `


 ` ‘@angular/common/http’;`




 angular/common/http





 bHTTPLoader





 NHTTPLoaderService






 `import { NHTTPLoaderService } `


 ` from 'neutrinos-seed-services';`



 neutrinos-seed-services

**Alert** and **SnackBar** usage have changed to the following:

```javascript
constructor( private snackBarService: NSnackbarService, private alertService: NAlertService ) {}this.alertService.alert('Some message to be displayed', 'Title of the alert');this.snackBarService.openSnackBar(‘Some error message’);
```

- For all custom Angular services and Model method imports, go one level down the import path:

**Before**

```javascript
// Service importimport { exampleService } from ‘../services/example.service.ts’//Model method importimport { ModelMethods } from '../lib/model.methods';
```

**After**

```javascript
// Service importimport { exampleService } from ‘../../services/example.service.ts’//Model method importimport { ModelMethods } from '../../lib/model.methods';
```

- Import the **NBaseComponent** component and extend the component. Make a super call in the constructor and change the variable `dm:ModelMethods `to `mm:ModelMethods` throughout the class in all data model methods.

Copy CodeJavaScriptimport { NBaseComponent } from '../../../../baseClasses/nBase.component'

export class yourComponent extends NBaseComponent implements OnInit {
 mm: ModelMethods
 constructor(private bdms: NDataModelService){
 super();
 this.mm = new ModelMethods(bdms);
 }
}

- ** Other Import changes:**
  - Services that have been created with uppercase will be changed to lowercase. Example: `Backend.service.ts` will be changed to `backend.service.ts, ` Change it in all appropriate import places except declaration.ts`.`
  - Any **npm** module downloaded apart from the one provided by default, as to be downloaded and added in `import-module.ts`
  - Any custom assets, styles or themes added in `angular-cli.json` should be created and replaced in `angular.json` in their respective object
  - Any changes, imports in `index.html` should be manually added or imported.
  - Change package name from the default (co.ideas.neutrinos) to app-specific in `config.xml`, `google-services.json` and `GoogleService-Info.plist `for mobile apps
  - If there are any custom models (model classes created without using **Data Model Editor**) add that to new migrated files.
- NSystemService is a singleton service - NSystemService.getInstance();
