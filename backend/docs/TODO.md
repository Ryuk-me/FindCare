#

<h2 align='center'>TODO'S</h2>
<hr>

## TASKS

- [X] USER SINGUP
- [X] USER LOGIN
- [X] USER ME
- [X] DOCTOR SIGNUP
- [X] DOCTOR LOGIN
- [X] DOCTOR ME
- [X] CREATE CLINIC
- [X] GET CURRENT CLINIC WITH DOCTOR DETAILS
- [x] Slots will be automatically calculated in python using calculate_slots function
- [x] ADD AGE COLUMN IN DATABASE for both user and doctor (AGE WILL BE calculated in python services before adding it to db)
- [x] added post and get appointment route for user
- [x] added search for clinics / doctor (public route)
- [x] need to implement get all appointments of a clinic
- [x] book appointments only if clinic is_open=True
- [x] appointment cancellation by user
- [x] implement only user can cancel his/her appointment no other user can
- [x] appointment cancellation by doctor/clinic
- [x] appointment skipped flag by doctor/clinic
- [x] appointment completion  flag by doctor / clinic
- [x] create a slug for doctor profile ex-> dr-doctor-name-uuid
- [x] create admin table and add admin login route
- [x] create superadmin route / auth / list all doctors and verify doctors
- [ ] implemnet available_days update and remove ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
- [ ] clinic on / off flag
- [ ] IMPLEMENT UPDATE FEATURE FOR USER LIKE (PASSWORD,MAIL,PHONE NUMBER,DOB,AGE)
- [ ] IMPLEMENT UPDATE FEATURE FOR DOCTOR LIKE (PASSWORD,MAIL,PHONE NUMBER,DOB,AGE,PROFILE_IMAGE)
- [ ] IMPLEMENT UPDATE FEATURE ON DOCTOR CLINIC (WHICH WILL CHANGE OPENS AT,CLOSES AT,SESSION_TIME,AND IS_OPEN AND SLOTS WILL BE CALCULATED ACCORDINGLY)
- [ ] set password length minimun to 8 for doctor user and admin (IN LAST)

## HOW SLOT WILL BE CALCULATED

> `int(int(closes_at - opens_at) * 60))` (slots will be calculated using calculate_slots in services.py file)
> `int(total_minutes // session_time)`
