# 4.0.0

<https://documentation.neutrinos.com/articles/#!change-log/release-4-0-0>

## 4.0.0

#### Date: (2018-11-06)

### Features:

MatBadgeModule added to Material imports, closes


 Added CLI and UI Version Information


 Data Model Editor redesigned


 Renaming the different app when unique validation errors come


 Expansion panel added as a palette component.


 Detect old apps and show if migration is required.


 All default seed app services is now a npm module as neutrinos-module (0.0.28) and neutrinos-seed-services (0.0.49)


 Authentication is now required to access studio.


 Thumbnail image can be added for each app on the workspace.


 Edit app details like name, description etc.


 One-click app deploy to Google cloud for Web and Android Platforms.


 Templates can be used while creating an app (Login template available by default).


 Download and install templates from Marketplace.


 Tenant name is prefilled while creating an app.


 The data source is prefilled while creating a data model.


 Dependencies update:


 Angular from version from 5.0.2 to 6.0.3


 Angular material from 5.0.0-rc0 to 6.2.0


 Angular flex-layout from 2.0.0-beta.10-4905443 to 5.0.0-beta.14


 ngx-charts from 7.0.1 to 8.0.2


 chartjs from 2.7.1 to 2.7.2


 d3 from 4.9.1 to 5.4.0


 firebase from 4.6.2 to 5.0.4


 rxjs from 5.5.2 to 6.2.0




 New cordova plugins added as directives


 Bar code scanner


 Media-capture (video)


 Fingerprint for authentication


 Optical character recognition


 Shake detector


 Text to Speech

Migration feature added for apps built on the Studio version of 3.3.1 or later.


 ART 4.0.0-



 The number of Iterations for password hashing is increased, Use neutrinos admin account to reset the password for existing accounts.


 authDatasource removed from login API path.


 default_datasource changed to datasource_uri in tenant document.


 New authentication strategy added - idsLocalAuth




 Bug Fixes

### 

- Fixed the 'exit' command bug in the Neutrinos Studio terminal.
- Fixed the removal of images issue in asset editor,
- Fixed the version field validation while creating and editing app details,
- Fixed alert box's icon and wrong app icon in Mac
- Fixed the incorrect progress bar message while importing, exporting, deleting, and migrating apps.
- Fixed If workspace folder has space in its name, the app icon for the apps in that workspace is not visible
- Fixed the snackbar message while saving the TypeScript file and template file
- Saving an environment will only update the environment object if it already exists.
- Fixed the removal of image issue in asset editor
- Corrupt apps will no longer crash the studio. This PR also changes when the appNmae.json is created, which is now at the end of the app creation process so that the existence of **appName.json **can be used to check whether an app is corrupt or not.
- Migration fails with default route configuration, closes BHIV-658
- Fixed the incorrect progress bar message while importing, exporting, deleting and migrating, closes BHIV-739
- Fixed two snackbar while saving Ts file and template file, closes BHIV-676
- Fixed the issue of removal of app icon when migrated from one version to another, closes BHIV-718
- Electron window focus for magnet link click, closes MAR-135
- Removed console logs from the service files.
- Dynamic message in installation prompt when artifacts are downloaded from Store using magnet link closes MAR-138
- Removed created by from app metadata JSON file, closes BHIV-608
- Fixed the snackbar issue which was breaking after 65th character, closes BHIV-590
- Multiple import of app fails, if import from the same directory, closes BHIV-760
- Progress bar component and slider component were showing the same name, closes BHIV-604
- Migration fails due to Bkeeper referenced HTML not found, closes MAR-145
- Removed file paths from the response messages, closes BHIV-642
- Cannot put complex data model array, closes BHIV-652
- Removed created by from app metadata JSON file, closes BHIV-608
- Updated app name in 'angular.json', closes BHIV-583
- Backup of **.nos** files removed after migration closes BHIV-592
- Remove trailing white spaces in all input fields, closes BHIV-616
- Palette components by default should be collapsed, closes BHIV-593
- Show proper error message while creating a data model, closes BHIV-615
- Image not displayed in app list
- Terminal Resize issue, closes BHIV-586
- Data source undefined error while calling data model API in the constructor
- Data model clone issue closes BHIV-508
