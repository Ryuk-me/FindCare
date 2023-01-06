<h2 align='center'>TODO'S</h2>
<hr>

## TASKS

1. - [X] ~~USER SINGUP~~
2. - ~~ USER LOGIN~~
3. - ~~ USER ME~~
4. - ~~ DOCTOR SIGNUP~~
5. - ~~ DOCTOR LOGIN~~
6. - ~~ DOCTOR ME~~
7. - ~~ CREATE CLINIC~~
8. - ~~ GET CURRENT CLINIC WITH DOCTOR DETAILS~~
9. - ~~ Slots will be automatically calculated in python using calculate_slots function~~
10. - ~~ ADD AGE COLUMN IN DATABASE for both user and doctor (AGE WILL BE calculated in python services before adding it to db)~~
11. - ~~ added post and get appointment route for user~~
12. - ~~ added search for clinics / doctor (public route)~~
13. - ~~ need to implement get all appointments of a clinic~~
14. - ~~ book appointments only if clinic is_open=True~~
15. - ~~ appointment cancellation by user~~
16. - ~~ implement only user can cancel his/her appointment no other user can~~
17. - ~~ appointment cancellation by doctor/clinic~~
18. - ~~ appointment skipped flag by doctor/clinic~~
19. - ~~ appointment completion  flag by doctor / clinic~~
20. - ~~ create a slug for doctor profile ex-> dr-doctor-name-uuid~~
21. - ~~ create admin table and add admin login route~~
22. - ~~ create superadmin route / auth / list all doctors and verify doctors~~
23. - ~~ while sending back all clinic details in `admin/clinics` send back total_no of appointments ,upcoming appointments,cancelled appointments,skipped_appointments,pending_appointments (either cancelled by user or doctor side) with clinic data~~
24. - ~~ categorise `error_handlers/errors.py` based on user/doctor/mixed~~
25. - ~~ IMPLEMENT UPDATE FEATURE FOR USER LIKE (MAIL,PHONE NUMBER,DOB,AGE) (password will be changed on a different route)~~
26. - ~~ host backend with docker~~
27. - ~~ implement ci/cd for backend~~
28. - ~~ host frontend with netlify~~
29. - ~~ IMPLEMENT UPDATE FEATURE FOR DOCTOR LIKE (PASSWORD,MAIL,PHONE NUMBER,DOB,AGE,PROFILE_IMAGE)~~
30. - ~~ verify user/doctor on signup and send a verification email~~
31. - ~~ implement password reset (send a temporary password on email)~~
32. - ~~ change host api url to frontend webiste url and get token as slug and then call on api to verify it [after frontend ez created]~~
33. - ~~ send a welcome email with email verification to user/doctor after creating new accounting (by themselves)~~
34. - ~~ send a reset password mail user/doctor~~
35. - ~~ send a account banned/unbanned~~
36. - ~~ send a welcome email to user/doctor after creation of new account by admin(it will contain temp pass user/dr wont need to verify their email)~~
37. - ~~ send email changed verification mail to user/doctor by admin user/dr will need to verify that mail to continue~~
38. - ~~ when user/doctor change their email they have to verify that email again until their state of will be is_active=False~~
39. - ~~ clinic on / off flag~~
40. - ~~ implemnet available_days update and remove ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]~~
41. - ~~ IMPLEMENT UPDATE FEATURE ON DOCTOR CLINIC (WHICH WILL CHANGE OPENS AT,CLOSES AT,SESSION_TIME,AND IS_OPEN AND SLOTS WILL BE CALCULATED ACCORDINGLY)~~
42. - ~~ set password length minimun to 8 for doctor user and admin (IN LAST)~~

## ~~HOW SLOT WILL BE CALCULATED~~

> ~~`int(int(closes_at - opens_at) * 60))` (slots will be calculated using calculate_slots in services.py file)
> `int(total_minutes // session_time)`~~

## ~~New todo~~

- ~~ doctor reason cancellation new model [required]~~
- ~~ user active  and doctor active(flag) for email verification~~
- ~~ manage user from admin panel [like ban user currently]~~
- ~~ USER WONT BE ABLE TO LOGIN IF ACCOUNT IS BANNED~~
- ~~ manage DOCTOR from admin panel [like ban DOCTOR currently]~~
- ~~ activate/deactivate user/doctor account from admin panel~~
- ~~ get all users for admin panel (name,email phone,number of appointments,is_banned,is_active etc details)~~
- ~~ admin can create user account /doctor and password will be directly sent to the user admin cant see password or set~~
- ~~ admin can change user/doctor email and user have to verify it~~
- ~~ user can only cancel appointment upto 4 hours before appointment time [will be implemented after slot logic]~~
- ~~ user can only book future appointments~~
- ~~ at the time of appointment booking check that appointment date/time and slot is available/free in clinic (bascially it is a precation for external api calls)~~
