# 4.0.3

<https://documentation.neutrinos.com/articles/#!change-log/release-4-0-3>

## 4.0.3

#### Date: (2019-01-11)

---

### Bug Fixes

Commented out `<plugin name="cordova-plugin-local-notification" spec="~0.9.0-beta.2"/>` from config.xml since it was causing app crash on start [[BHIV-898](https://jatahworx.atlassian.net/browse/BHIV-898)]





 Replaced cordova-plugin-tts with cordova-plugin-neutts in config.xml since it was causing build failures. [BHIV-914](https://jatahworx.atlassian.net/browse/BHIV-914)





 Empty sanckbar message when switched to a workspace with no app. [BHIV-864](https://jatahworx.atlassian.net/browse/BHIV-864)





 Apollo22 project migration fails. [BHIV-858](https://jatahworx.atlassian.net/browse/BHIV-858)





 Firebase configuration not updated in tenant app object during deploy [BHIV-817](https://jatahworx.atlassian.net/browse/BHIV-817)





 'Loading...' screen appears regardless of AutoHideSplashScreen configuration in mobile app [BHIV-805](https://jatahworx.atlassian.net/browse/BHIV-805)





 creating empty app or using template and changing the arturl reflects in both prod env and dev env. [BHIV-782](https://jatahworx.atlassian.net/browse/BHIV-782)





 Remove **messagingSendId** property in environments and add migration logic for removing "messagingSenderId" from environments and firebase related files in the app. [[BHIV-866](https://jatahworx.atlassian.net/browse/BHIV-866)]Bug Fixes in ART 4.0.3 - (2019-01-11)Throwing error message when datasource_uri is not present for the tenant or app, error message modified when API is invalid.
