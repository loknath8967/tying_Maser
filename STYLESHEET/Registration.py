class STYLESHEET:
    @staticmethod
    def Registration():
        SHEET ='''color:red; font-size:8 px; padding-top: 1px; margin-top:1px;'''
        return SHEET

    @staticmethod
    def field():
        SHEET ='''QLineEdit{
        font-size:15px; padding-left:10px; text-align:center; border: 1px solid black;
         border-radius: 5px; background-color:white;
        }'''
        return SHEET

    @staticmethod
    def phone_code():
        SHEET ='''QComboBox {border: 1px solid black; background-color:white ;
                        color:black;font-weight: bold;font-family: serif;font-size: 15px; border-top-left-radius: 5;
                        border-bottom-left-radius:5; padding-left:1px; 
                        }
                        ::drop-down{
                                        width: 2; border: 1px hidden gray ;
                                    }
                        '''
        return SHEET

    @staticmethod
    def phone_number():
        SHEET ='''QLineEdit{
                             font-size:15px; padding-left:40px; text-align:center; border: 1px solid black;
                              border-radius: 5px; background-color:white;
                             }'''
        return SHEET

    @staticmethod
    def phone_valid():
        SHEET ='''QLineEdit{
                             font-size:15px; padding-left:40px; text-align:center; border: 1px solid green; 
                             border-radius: 5px; background-color:white;
                             }'''
        return SHEET

    @staticmethod
    def state():
        SHEET ='''QLineEdit{
                     font-size:15px; padding-left:10px; text-align:center; border: 1px solid black;
                      border-radius: 5px; background-color:white;
                     }'''
        return SHEET

    @ staticmethod
    def Label():
        SHEET ='''font-size:18px; '''
        return SHEET

    @staticmethod
    def DOB():
        SHEET ='''QDateEdit{
        font-size:15px; padding-left:10px; text-align:center; border: 1px solid black; 
        border-radius: 5px; background-color:white;             
                }'''
        return SHEET

    @staticmethod
    def PASSWORD():
        SHEET ='''QLineEdit{
        font-size:15px; padding-left:10px; text-align:center; border: 1px solid black;
         border-radius: 5px; background-color:white';
        }'''
        return SHEET

    @staticmethod
    def gmail():
        SHEET ='''QLineEdit{
        font-size:15px; padding-left:10px; text-align:center; border: 1px solid black; 
        border-radius: 5px; background-color:white;

        }'''
        return SHEET

    @staticmethod
    def AccountCreate_Title():
        SHEET ='''QLabel{
        font-size:21px;
        color:blue; 
        background-color:yellow;   
        }
        '''
        return SHEET

    @staticmethod
    def PERMISSION_GP():
        SHEET ='''QGroupBox::Title{
        font-size:15px;
        }'''
        return SHEET

    @staticmethod
    def AC_TYPE():
        SHEET ='''QComboBox{
        background-color:white;
        font-size:15px;
        }'''
        return SHEET

    @staticmethod
    def CreateAC():
        SHEET ='''
                QPushButton{
                border:2px solid gray;
                font-size:18px;
                margin-right:40px;
                border-radius:14px;
                border-top-style:hidden;
                }
                '''
        return SHEET

    @staticmethod
    def PERMISSION():
        SHEET ='''font-size:11px; text-align:left; '''
        return SHEET