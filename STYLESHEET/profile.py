class STYLESHEET:
    @staticmethod
    def Line():
        SHEET ='''
                QLineEdit{
                font-size:20px;
                margin-right:40px;
                border:2px solid gray;
                background:white;
                color:black;

                }
                '''
        return SHEET

    @staticmethod
    def Address():
        SHEET ='''
        QTextEdit
        {
        font-size:20px;
        margin-right:40px;
        border:2px solid gray;
        background:white;
        color:black;
        padding-top:10px;
        }'''
        return SHEET

    @staticmethod
    def Button():
        SHEET ='''QPushButton{
                background-color:white;
                border:2px solid gray;
                font-size:18px;
                margin-right:40px;
                border-radius:14px;
                border-top-style:hidden;
                color:blue;
                 
                }'''
        return SHEET

    @staticmethod
    def profile():
        SHEET ='''
        QLabel{
        font-size:20px;
        margin-left:40px;

        }
       '''
        return SHEET

