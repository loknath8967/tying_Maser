class STYLESHEET:
    @staticmethod
    def MAIN():
        SHEET='''
    QGroupBox{
background-image:url(image/background.jpg) no-repeat center center ;
background-repeat: no-repeat; border: 1px solid red;
border-radius: 15; border-style:hidden; height: 20px;
}
        '''

        return SHEET

    @staticmethod
    def BUTTON():
        SHEET = '''
        QPushButton{
border: 1px solid red; border-radius: 15; background-color: blue;
color:white; font-size:18px; font-family: "Lucida Handwriting"; border-style:hidden;
}
    QGroupBox{
background:transparent; border-style:hidden;
}
        '''

        return SHEET