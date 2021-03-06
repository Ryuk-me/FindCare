#

<h2 align='center'>TODO'S</h2>
<hr>

## TASKS

1. - [X] USER SINGUP
1. - [X] USER LOGIN
1. - [X] USER ME
1. - [X] DOCTOR SIGNUP
1. - [X] DOCTOR LOGIN
1. - [X] DOCTOR ME
1. - [X] CREATE CLINIC
1. - [X] GET CURRENT CLINIC WITH DOCTOR DETAILS
1. - [x] Slots will be automatically calculated in python using calculate_slots function
1. - [x] ADD AGE COLUMN IN DATABASE for both user and doctor (AGE WILL BE calculated in python services before adding it to db)
1. - [x] added post and get appointment route for user
1. - [x] added search for clinics / doctor (public route)
1. - [x] need to implement get all appointments of a clinic
1. - [x] book appointments only if clinic is_open=True
1. - [x] appointment cancellation by user
1. - [x] implement only user can cancel his/her appointment no other user can
1. - [x] appointment cancellation by doctor/clinic
1. - [x] appointment skipped flag by doctor/clinic
1. - [x] appointment completion  flag by doctor / clinic
1. - [x] create a slug for doctor profile ex-> dr-doctor-name-uuid
1. - [x] create admin table and add admin login route
1. - [x] create superadmin route / auth / list all doctors and verify doctors
1. - [x] while sending back all clinic details in `admin/clinics` send back total_no of appointments ,upcoming appointments,cancelled appointments,skipped_appointments,pending_appointments (either cancelled by user or doctor side) with clinic data
1. - [x] categorise `error_handlers/errors.py` based on user/doctor/mixed
1. - [x] IMPLEMENT UPDATE FEATURE FOR USER LIKE (MAIL,PHONE NUMBER,DOB,AGE) (password will be changed on a different route)
1. - [x] host backend with docker
1. - [x] implement ci/cd for backend
1. - [x] host frontend with netlify
1. - [x] IMPLEMENT UPDATE FEATURE FOR DOCTOR LIKE (PASSWORD,MAIL,PHONE NUMBER,DOB,AGE,PROFILE_IMAGE)
1. - [x] verify user/doctor on signup and send a verification email
1. - [x] implement password reset (send a temporary password on email)
1. - [x] change host api url to frontend webiste url and get token as slug and then call on api to verify it [after frontend ez created]
1. - [x] send a welcome email with email verification to user/doctor after creating new accounting (by themselves)
1. - [x] send a reset password mail user/doctor
1. - [x] send a account banned/unbanned
1. - [x] send a welcome email to user/doctor after creation of new account by admin(it will contain temp pass user/dr wont need to verify their email)
1. - [x] send email changed verification mail to user/doctor by admin user/dr will need to verify that mail to continue
1. - [x] when user/doctor change their email they have to verify that email again until their state of will be is_active=False
1. - [ ] clinic on / off flag
1. - [ ] implemnet available_days update and remove ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
1. - [ ] IMPLEMENT UPDATE FEATURE ON DOCTOR CLINIC (WHICH WILL CHANGE OPENS AT,CLOSES AT,SESSION_TIME,AND IS_OPEN AND SLOTS WILL BE CALCULATED ACCORDINGLY)
1. - [ ] set password length minimun to 8 for doctor user and admin (IN LAST)

## HOW SLOT WILL BE CALCULATED

> `int(int(closes_at - opens_at) * 60))` (slots will be calculated using calculate_slots in services.py file)
> `int(total_minutes // session_time)`

## New todo

- [x] doctor reason cancellation new model [required]
- [x] user active  and doctor active(flag) for email verification
- [X] manage user from admin panel [like ban user currently]
- [X] USER WONT BE ABLE TO LOGIN IF ACCOUNT IS BANNED
- [x] manage DOCTOR from admin panel [like ban DOCTOR currently]
- [x] activate/deactivate user/doctor account from admin panel
- [X] get all users for admin panel (name,email phone,number of appointments,is_banned,is_active etc details)
- [x] admin can create user account /doctor and password will be directly sent to the user admin cant see password or set
- [x] admin can change user/doctor email and user have to verify it
- [ ] user can only cancel appointment upto 4 hours before appointment time [will be implemented after slot logic]
- [ ] user can only book future appointments
- [ ] at the time of appointment booking check that appointment date/time and slot is available/free in clinic (bascially it is a precation for external api calls)
