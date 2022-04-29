from fastapi import HTTPException, status


# ***********************************************************************************
#                                                                                   #
#                              USER ERRORS                                          #
#                                                                                   #
# ***********************************************************************************


USER_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail=f'user not found')

USER_ALREADY_EXIST = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="user already exist")


# ***********************************************************************************
#                                                                                   #
#                              DOCTOR ERRORS                                        #
#                                                                                   #
# ***********************************************************************************


DOCTOR_ALREADY_EXIST = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="doctor already exist")

DOCTOR_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail=f'doctor not found')

NO_DOCTOR_FOUND_WITH_THIS_ID = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="no doctor found with this id")

DOCTOR_IS_ALREADY_VERIFIED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="doctor is already verified")

DOCTOR_WITH_THIS_REGISTRATION_NUM_ALREADY_EXIST = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="doctor with this registration number already exist")

NOT_POSSIBLE_EXPERINCE_YEAR = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="experince year not acceptable please try lower value")


# ***********************************************************************************
#                                                                                   #
#                              ADMIN ERRORS                                         #
#                                                                                   #
# ***********************************************************************************


# ***********************************************************************************
#                                                                                   #
#                      FORBIDDEN ACTIONS ERRORS                                     #
#                                                                                   #
# ***********************************************************************************


INVALID_CREDENTIALS_ERROR = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")

TOKEN_CREDENTIALS_ERROR = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

FORBIDDEN_ACTION_ERROR = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="not authorised to perform this action")

PLEASE_LOGIN_FIRST = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail=f'please login first')

NOT_A_SUPER_ADMIN = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="you dont have enough permission to perform this action")


# ***********************************************************************************
#                                                                                   #
#                              CLINIC ERRORS                                        #
#                                                                                   #
# ***********************************************************************************


ALREADY_EXIST_CLINIC = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="clinic already exist for this doctor")

CLINIC_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="clinic not found")

CLINIC_IS_NOT_SERVICEABLE = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="clinic is not servicable currently")


# ***********************************************************************************
#                                                                                   #
#                         APPOINTMENT ERRORS                                        #
#                                                                                   #
# ***********************************************************************************


APPOINTNEMT_ALREADY_CANCELLED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="appointment is already cancelled")

APPOINTMENT_ALREADY_SKIPPED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="appointment is already skipped")

APPOINTNEMT_ALREADY_CANCELLED_BY_USER = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="appointment is already cancelled by the user")

APPOINTMENT_ALREADY_CANCELLED_BY_DR = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="appointment is already cancelled by the doctor")

APPOINTMENT_ALREADY_COMPLETED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="appointment is already completed")

APPOINTMENT_SKIPPED_CANCELLATION = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="appointment cancelled due to patient was not on time"
)

NO_APPOINTMENT_FOUND_ERROR = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="no appointment found")


# ***********************************************************************************
#                                                                                   #
#                              UPDATE DATABASE                                      #
#                                                                                   #
# ***********************************************************************************

NOTHING_CHANGED = HTTPException(
    status_code=status.HTTP_304_NOT_MODIFIED, detail="not modified")

# ***********************************************************************************
#                                                                                   #
#                              MISC ERRORS                                          #
#                                                                                   #
# ***********************************************************************************


NOT_FOUND_ERROR = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="not found")


PHONE_NUMBER_ALREADY_EXIST = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="an account with this phone number already exist")

EMAIL_ALREADY_EXIST = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="an account with this email already exist")

PASSWORD_CANNOT_BE_SAME = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="password cannot be same as the old one")


# ***********************************************************************************
#                                                                                   #
#                        EMAIL TOKEN ERRORS                                         #
#                                                                                   #
# ***********************************************************************************


VERIFICATION_LINK_EXPIRED = HTTPException(
    status_code=status.HTTP_410_GONE, detail="verification link has been expired")

EMAIL_ALREADY_VERIFIED = PASSWORD_CANNOT_BE_SAME = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="email already verified")

PLEASE_VERIFY_YOUR_EMAIL = PASSWORD_CANNOT_BE_SAME = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="please verify your email first")
