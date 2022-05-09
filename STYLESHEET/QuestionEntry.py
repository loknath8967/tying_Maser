class STYLESHEET:
    @staticmethod
    def QUESTION():
        SHEET =''' 
        QTextEdit{
        background-color:white;
        font-size:18px;
        border-radius:1px;
        padding:5px;
        
        }'''
        return SHEET

    @staticmethod
    def TopBar():
        SHEET =''' QGroupBox{
        background-color:rgb(169,169,169);
        border: 1px hidden rgb(169,169,169);
        border-radius:1px;
        }
        '''
        return SHEET


    @staticmethod
    def PLabel():
        SHEET = ''' QLabel{
        color:blue;
        font-size:16px;
        padding:5px;
        
        }
            '''
        return SHEET
    @staticmethod
    def REQUIRE():
        SHEET = ''' QLabel{
                color:red;
                font-size:14px;
                padding:5px;

                }
                    '''
        return SHEET


    @staticmethod
    def NUMBER():
        SHEET ='''
        QLabel{
        color:blue;
        font-size:16px;
        padding-left:3px;
        
        }
        '''
        return SHEET

    @staticmethod
    def PassMark():
        SHEET ="""
                QSpinBox{
                background-color: white;
             border: 1px hidden gray ; border-top-style:solid; border-bottom-style:solid;
             padding-left:10px;
             font-size:15px;

                }
                QSpinBox::down-button{
                    width: 8px ;
                    border: 1px hidden gray ;
                }
                QSpinBox::up-button{
                    width: 8px;
                    border: 1px hidden gray ;
                }
        """
        return SHEET

    @staticmethod
    def BOTTOM():
        SHEET =''' QGroupBox{
        background-color:rgb(169,169,169);
        border-style:hidden;
        border-radius:1px;
        }
        '''
        return SHEET

    @staticmethod
    def ENTRY():
        SHEET ='''QPushButton{
        background-color:blue;
        border:3px double rgb(0, 0, 128);
        border-top-style:hidden;
        border-radius:10px;
        color:white;
        font-size:15px;
        }
        :hover{
        background-color:rgb(100, 149, 237);
        border:3px double rgb(0, 0, 128);
        border-bottom-style:hidden;
        }'''
        return SHEET
    @staticmethod
    def QENTRY():
        SHEET = '''{
                border:1px hidden blue;
                }'''
        return SHEET

    @staticmethod
    def ITEM():
        SHEET = ''' font-family: "Lucida Handwriting"; font-size: 18px;text-align:right;color:green; border:1px hidden; '''
        return SHEET

    @staticmethod
    def VALUE():
        SHEET = ''' font-family: "Lucida Handwriting"; font-size: 18px;text-align:right;color:black; border:1px hidden; '''
        return SHEET

    @staticmethod
    def NewQuestion():
        SHEET = '''border:2px solid red;'''
        return SHEET

    @staticmethod
    def NewQuestion_gp_gp():
        SHEET = '''QLabel{border-style: hidden; }'''
        return SHEET

    @staticmethod
    def HeaderStatus():
        SHEET = '''QLabel{
                        font-family: "Comic Sans MS"; padding:20px; font-size:20px; text-align:right;color:green;
                         border:5px hidden red; border-bottom-style:double;
                          }
                    '''
        return SHEET

    @staticmethod
    def NewQuestion_gp():
        SHEET = '''QGroupBox{ border:5px hidden red; }'''
        return SHEET

    @staticmethod
    def BTN_Gp():
        SHEET = '''QGroupBox{
                        border:2px hidden red;

                     }
                    '''
        return SHEET

    @staticmethod
    def Insert():
        SHEET = ''' QPushButton{
                                    border: 1px solid gray;font-style: italic;font-weight: bold;border-radius: 15;
                                    background-color: blue;color:white;font-size:12px;padding:8px;font-family: "Lucida Handwriting";
                    }
                    ::hover{
                    background-color:green;
                    }
            '''
        return SHEET