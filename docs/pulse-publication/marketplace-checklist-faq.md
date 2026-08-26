# On-Prem Marketplace Development Environment Configuration Guide

<https://documentation.neutrinos.com/articles/#!pulse-publication/marketplace-checklist-faq>

## On-Prem Marketplace Development Environment Configuration Guide

This section describes the required configuration for deploying the marketplace in the Development (Dev) environment.

### Values Configuration

1. “features” Values Configuration:
    Ensure the following configuration is set in your values.yaml file for the Development environment:
    Parameter
    Configuration Values
    features.devMode
    true
    features.marketPlace.enable
    true
    features.marketPlace.clientId
    YOUR_ALPHA_CLIENT_ID
    features.marketPlace.clientSecret
    YOUR_ALPHA_CLIENT_SECRET
    features.marketPlace.ids
    https://YOUR_ALPHA_IDS_URL
    features.marketPlace.url
    https://YOUR_ALPHA_DOMAIN/MARKETPLACE_HEADLESS_PATH/api
  - **Status**: This enables Development mode.
  - **Warning**: This must be set to true only in the Dev environment.
  - **Note**: Replace YOUR_ALPHA_DOMAIN with your actual domain
  - Note: Ensure the IDS URL matches your Dev environment.
  - Note: Ensure that the base path is the same in both `services.backends.marketplace-headless.path and features.marketplace.url`
2. "services.backends.marketplace-headless" Values Configuration:
    Since the Development environment directly consumes components from the Central Marketplace, the following configurations must be applied in the marketplace-headless service:
   **Environment Variable **
   **Configuration Value**
   envs.APP_NAME
   marketplace-headless
   envs.CENTRAL_MARKET_PLACE_URL
   https://marketplace.neutrinos-apps.com/marketplace-headless
   envs.CLIENT_ID
   YOUR_ALPHA_CLIENT_IDenvs.CLIENT_SECRET
   YOUR_ALPHA_CLIENT_SECRET
   envs.CM_CLIENT_ID
   *****envs.CM_CLIENT_SECRET
   *****envs.CM_IDS_ISSUER_URL
   https://marketplace.neutrinos-apps.comenvs.DB_DATABASE
   YOUR_ALPHA_DATABASE_NAME
   envs.DB_PORT
   5432envs.DB_SCHEMA
   YOUR_MARKETPLACE_SCHEMA (this must be same as the schema configured in the migration config when deploying in trinity)
   envs.DEPLOYED_ON_PREM
   trueenvs.DISABLE_S3
   trueenvs.NODE_ENV
   productionenvs.OIDC_ISSUER
   https://YOUR_ALPHA_IDS_URL
   envs.ON_PREM_ENV
   developmentversion
   25.11.0.0.0-49d5909-current
