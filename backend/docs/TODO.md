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
- [ ] IMPLEMENT UPDATE FEATURE FOR USER LIKE (PASSWORD,MAIL,PHONE NUMBER,DOB,AGE)
- [ ] IMPLEMENT UPDATE FEATURE FOR DOCTOR LIKE (PASSWORD,MAIL,PHONE NUMBER,DOB,AGE,PROFILE_IMAGE)
- [x] ADD AGE COLUMN IN DATABASE for both user and doctor (AGE WILL BE calculated in python services before adding it to db)
- [ ] IMPLEMENT UPDATE FEATURE ON DOCTOR CLINIC (WHICH WILL CHANGE OPENS AT,CLOSES AT,SESSION_TIME,AND IS_OPEN AND SLOTS WILL BE CALCULATED ACCORDINGLY)

## HOW SLOT WILL BE CALCULATED

> `int(int(closes_at - opens_at) * 60))` (slots will be calculated in frontend and it will passed to api call to save in db default is 0)
> `int(total_minutes // session_time)`
