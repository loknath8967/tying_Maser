class STYLESHEET:
    # @staticmethod
    # def manager():
    #     SHEET=
    #     return SHEET

    @staticmethod
    def manager_btn():
        SHEET ='''
            font-size: 15px;'''
        return SHEET

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
    def Button(color, font):
        SHEET ="QPushButton{" f'''background-color:{color};
                border:2px solid gray;
                font-size:18px;
                margin-right:40px;
                border-radius:14px;
                border-top-style:hidden;
                color:{font};
                ''' "}"

        return SHEET

    @staticmethod
    def details():
        SHEET ='''
        QLabel{
        font-size:20px;
        margin-left:40px;
        }
       '''
        return SHEET

