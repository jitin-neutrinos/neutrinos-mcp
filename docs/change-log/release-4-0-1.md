# 4.0.1

<https://documentation.neutrinos.com/articles/#!change-log/release-4-0-1>

## 4.0.1

#### Date: (2018-11-23)

---

### Features:

- Updated swagger to include latest changes in bhive-art.
- Capture more information about the platform in user_register collection
- Changed Modelr MODELR_HTTP_NODE_ROOT from /mapi to /api to keep it consistent with Studio.
- **ART:** Updated swagger to include latest changes in bhive-art

---

### Bug Fixes

### Changed platFormDetails to platformDetails in bhive-art.

- Fixed the bug for refresh token with respect to the account object which was being created in the first app (replaced into the every app object which gets executed for individual apps).
- Fixed Notification deregisteration not working.
- Changed platFormDetails to platformDetails.
- LocalAuth Change password API access control middleware closes.
- Fixed LocalAuth Default admin creation error
