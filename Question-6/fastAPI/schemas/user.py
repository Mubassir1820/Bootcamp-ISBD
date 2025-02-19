from pydantic import BaseModel, Field
from fastapi import HTTPException, status
from email_validator import validate_email, EmailNotValidError


#properties required during user creation
class UserCreate(BaseModel):
    email : str
    password : str = Field(..., min_length=4)

    def __init__(self, **data):
        super().__init__(**data)
    
        if self.email:
            try:
                emailinfo = validate_email(self.email, check_deliverability=False)
                self.email = emailinfo.normalized
            except EmailNotValidError as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Not a valid email!"
                )
            
class UserView(BaseModel):
    id: int
    email : str

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True


class Token(BaseModel):
   access_token: str
   refresh_token: str
   token_type: str = "bearer"