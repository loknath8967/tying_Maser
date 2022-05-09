class STYLESHEET:
    @staticmethod
    def ITEM():
        SHEET=''' font-family: "Lucida Handwriting"; font-size: 18px;text-align:right;color:green;'''
        return SHEET

    @staticmethod
    def ERROR():
        SHEET ='''QGroupBox{
        border:2px solid red;   
        }
        '''
        return SHEET

    @staticmethod
    def ERROR_GP_GP():
        SHEET ='''QLabel{border-style: hidden; }'''
        return SHEET

    @staticmethod
    def ERROR_RESULT():
        SHEET =''' QLabel{
            font-family: "Comic Sans MS"; padding:20px; font-size:20px; text-align:right; color:red;
            border: 4px hidden red; border-bottom-style:double;

                            }'''
        return SHEET

    @staticmethod
    def ERROR_GP():
        SHEET =''' border-style:hidden; '''
        return SHEET
    @staticmethod
    def ERROR_error():
        SHEET ='''QLabel{
        font-size:18px; color:red; background-color: rgb(250, 204, 204);
        }
        '''
        return SHEET

    @staticmethod
    def ERROR_BTN():
        SHEET ='''
                        QGroupBox{
                            border-style:hidden;
                         }
                         QPushButton{
                         border: 1px solid gray;font-style: italic;font-style: oblique;font-weight: bold;border-radius: 15;
                         background-color: rgb(42, 42, 231);color:white;font-size:12px;padding:8px;font-family: "Lucida Handwriting";
                        }
                        '''
        return SHEET
    @staticmethod
    def RETRY():
        SHEET=''' QPushButton{
                background-color: rgb(235, 47, 47);

            }
        '''
        return SHEET

    @staticmethod
    def Id():
        SHEET =''' font-family: "arial"; font-size: 21px;text-align:right;color:black; background-color:yellow;'''
        return SHEET

    @staticmethod
    def NewAccount():
        SHEET ='''border:2px solid red;'''
        return SHEET

    @staticmethod
    def NewAccount_gp_gp():
        SHEET ='''QLabel{border-style: hidden; }'''
        return SHEET
    @staticmethod
    def HeaderStatus():
        SHEET='''QLabel{
                    font-family: "Comic Sans MS"; padding:20px; font-size:20px; text-align:right;color:green;
                     border:5px hidden red; border-bottom-style:double;
                      }
                '''
        return SHEET

    @staticmethod
    def NewAccount_gp():
        SHEET ='''QGroupBox{ border:5px hidden red; }'''
        return SHEET

    @staticmethod
    def SignGp():
        SHEET ='''border-style:hidden;'''
        return SHEET

    @staticmethod
    def BTN_Gp():
        SHEET ='''QGroupBox{
                    border:2px hidden red;

                 }
                '''
        return SHEET

    @staticmethod
    def NewEntry():
        SHEET =''' QPushButton{
                                border: 1px solid gray;font-style: italic;font-weight: bold;border-radius: 15;
                                background-color: blue;color:white;font-size:12px;padding:8px;font-family: "Lucida Handwriting";
                }
                ::hover{
                background-color:green;
                }
        '''
        return SHEET

