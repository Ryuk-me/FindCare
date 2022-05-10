from fastapi import HTTPException, status


# ***********************************************************************************
#                                                                                   #
#                              USER ERRORS                                          #
#                                                                                   #
# ***********************************************************************************


USER_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail=f'User not found')

USER_ALREADY_EXIST = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="User already exist")

USER_ALREADY_BANNED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="User is already banned")

USER_ALREADY_UNBANNED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="User is not banned")

USER_IS_BANNED = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Your account has been blocked. Please contact support for further details")

NO_USER_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail=f'No user found')

# ***********************************************************************************
#                                                                                   #
#                              DOCTOR ERRORS                                        #
#                                                                                   #
# ***********************************************************************************


DOCTOR_ALREADY_EXIST = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Doctor already exist")

DOCTOR_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail=f'Doctor not found')

NO_DOCTOR_FOUND_WITH_THIS_ID = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="No doctor found with this id")

DOCTOR_IS_ALREADY_VERIFIED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Doctor is already verified")

DOCTOR_WITH_THIS_REGISTRATION_NUM_ALREADY_EXIST = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Doctor with this registration number already exist")

NOT_POSSIBLE_EXPERINCE_YEAR = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Experince year not acceptable please try lower value")

DOCTOR_IS_NOT_VERIFIED = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Doctor is not verified")

DOCTOR_IS_BANNED = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Doctor is banned")

DOCTOR_IS_ALREADY_BANNED = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Doctor is already banned")

DOCTOR_IS_ALREADY_UNBANNED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Doctor is not banned")

# ***********************************************************************************
#                                                                                   #
#                              ADMIN ERRORS                                         #
#                                                                                   #
# ***********************************************************************************


YOU_CANNOT_SET_PASSWORD_FOR_USER = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="You cannot set password for user")

YOU_CANNOT_SET_PASSWORD_FOR_DOCTOR = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="You cannot set password for doctor")

PLEASE_CONTACT_ADMIN = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Please contact Admin for support")


# ***********************************************************************************
#                                                                                   #
#                      FORBIDDEN ACTIONS ERRORS                                     #
#                                                                                   #
# ***********************************************************************************


INVALID_CREDENTIALS_ERROR = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect Email or Password.")


TOKEN_CREDENTIALS_ERROR = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

FORBIDDEN_ACTION_ERROR = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="Not authorised to perform this action")

PLEASE_LOGIN_FIRST = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail=f'Please login first')

NOT_A_SUPER_ADMIN = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="You dont have enough permission to perform this action")


# ***********************************************************************************
#                                                                                   #
#                              CLINIC ERRORS                                        #
#                                                                                   #
# ***********************************************************************************


ALREADY_EXIST_CLINIC = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Clinic already exist for this doctor")

CLINIC_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Clinic not found")

CLINIC_IS_NOT_SERVICEABLE = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Clinic is not servicable currently")


# ***********************************************************************************
#                                                                                   #
#                         APPOINTMENT ERRORS                                        #
#                                                                                   #
# ***********************************************************************************


APPOINTNEMT_ALREADY_CANCELLED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Appointment is already cancelled")

APPOINTMENT_ALREADY_SKIPPED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Appointment is already skipped")

APPOINTNEMT_ALREADY_CANCELLED_BY_USER = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Appointment is already cancelled by the user")

APPOINTMENT_ALREADY_CANCELLED_BY_DR = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Appointment is already cancelled by the doctor")

APPOINTMENT_ALREADY_COMPLETED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Appointment is already completed")

APPOINTMENT_SKIPPED_CANCELLATION = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Appointment cancelled due to patient was not on time"
)

NO_APPOINTMENT_FOUND_ERROR = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="No appointment found")

NO_CANCELLATION_REASON = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Please enter a cancellation reason")


# ***********************************************************************************
#                                                                                   #
#                              UPDATE DATABASE                                      #
#                                                                                   #
# ***********************************************************************************

NOTHING_CHANGED = HTTPException(
    status_code=status.HTTP_304_NOT_MODIFIED, detail="Not modified")

# ***********************************************************************************
#                                                                                   #
#                              MISC ERRORS                                          #
#                                                                                   #
# ***********************************************************************************


NOT_FOUND_ERROR = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Not found")


PHONE_NUMBER_ALREADY_EXIST = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="An account with this phone number already exist")

EMAIL_ALREADY_EXIST = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="An account with this email already exist")

PASSWORD_CANNOT_BE_SAME = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Password cannot be same as the old one")

ACCOUNT_NOT_FOUND_WITH_THIS_EMAIL = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="No account found with this email")


# ***********************************************************************************
#                                                                                   #
#                        EMAIL TOKEN ERRORS                                         #
#                                                                                   #
# ***********************************************************************************


VERIFICATION_LINK_EXPIRED = HTTPException(
    status_code=status.HTTP_410_GONE, detail="Verification link has been expired")

PASSWORD_RESET_LINK_EXPIRED = HTTPException(
    status_code=status.HTTP_410_GONE, detail="Password reset link has been expired")

EMAIL_ALREADY_VERIFIED = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Email already verified")

PLEASE_VERIFY_YOUR_EMAIL = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="Please verify your Email first")
