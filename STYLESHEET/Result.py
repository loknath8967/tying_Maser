class STYLESHEET:
    @staticmethod
    def MAIN():
        SHEET = ''' background-color: white; '''
        return SHEET

    @staticmethod
    def ITEM():
        SHEET=''' font-family: "Lucida Handwriting"; font-size:20px;text-align:right;color:green;'''
        return SHEET

    @staticmethod
    def MARKS():
        SHEET ='''font-family: "Ink Free"; padding-left:10px; color:red; font-size:21px;'''
        return SHEET

    @staticmethod
    def PASSED():
        SHEET ='''QLabel{
            font-family: "Comic Sans MS"; 
                    padding:20px; font-size:20px;text-align:right;color:green;}'''
        return SHEET

    @staticmethod
    def FAILED():
        SHEET ='''QLabel{font-family: "Comic Sans MS";
                    padding:20px; font-size:20px;text-align:right;color:red;}'''
        return SHEET

    @staticmethod
    def MARKSHEET():
        SHEET ='''border:2px solid red;'''
        return SHEET

    @staticmethod
    def MARKSHEET_GP():
        SHEET='''

                border-style:hidden; 

                '''
        return SHEET

    @staticmethod
    def MARKSHEET_BTN():
        SHEET ='''

        QGroupBox{
            border-style:hidden;
            background-color: rgb(0, 255, 255);

         }
         QPushButton{
                        border: 1px solid gray;
                        font-style: italic;
                        font-style: oblique;
                        font-weight: bold;
                        border-radius: 15;
                        background-color: blue;
                        color:white;
                        font-size:12px;
                        padding:8px;
                        font-family: "Lucida Handwriting";

        }'''
        return SHEET
    @staticmethod
    def SIGN():
        SHEET='''border-style:hidden;'''
        return SHEET
