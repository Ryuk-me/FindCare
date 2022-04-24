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
1. - [ ] verify user/doctor on signup and send a verification email [after frontend ez created]
1. - [ ] clinic on / off flag
1. - [ ] categorise `error_handlers/errors.py` based on user/doctor/mixed
1. - [ ] implemnet available_days update and remove ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
1. - [ ] IMPLEMENT UPDATE FEATURE FOR USER LIKE (PASSWORD,MAIL,PHONE NUMBER,DOB,AGE)
1. - [ ] IMPLEMENT UPDATE FEATURE FOR DOCTOR LIKE (PASSWORD,MAIL,PHONE NUMBER,DOB,AGE,PROFILE_IMAGE)
1. - [ ] IMPLEMENT UPDATE FEATURE ON DOCTOR CLINIC (WHICH WILL CHANGE OPENS AT,CLOSES AT,SESSION_TIME,AND IS_OPEN AND SLOTS WILL BE CALCULATED ACCORDINGLY)
1. - [ ] set password length minimun to 8 for doctor user and admin (IN LAST)

## HOW SLOT WILL BE CALCULATED

> `int(int(closes_at - opens_at) * 60))` (slots will be calculated using calculate_slots in services.py file)
> `int(total_minutes // session_time)`
