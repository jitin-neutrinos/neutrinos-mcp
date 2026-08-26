# This topic explains how to enable the skipTeamCheck setting for a client.

<https://documentation.neutrinos.com/articles/#!pulse-publication/skip-team-check-faq>

## This topic explains how to enable the skipTeamCheck setting for a client.

**Q**: How to resolve issues caused by team check validation for a client




 **A**: Follow the steps below to verify and update the configuration:

1. Verify Configuration: Ensure that all required configurations related to team validation are correctly set.
2. Check skipTeamCheck in the Database: Connect to the database and verify whether the skipTeamCheck field is set to `false` for the specific client.
3. Update the Value if Needed: If `skipTeamCheck` is `false`, update it to true using the following SQL command:
   Copy CodePL/SQLUPDATE client
   SET "skipTeamCheck" = true
   WHERE client_id = '0ddh_euTKkSA682Yy5HuB';
4. Confirm the Update: Recheck the record to ensure the value has been updated successfully.
