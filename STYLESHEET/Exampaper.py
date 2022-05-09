class STYLESHEET:
    @staticmethod
    def UNLOCK():
        SHEET='''border: 1px solid green;
                        border-radius: 15;
                        background-color: green;
                        color:white;
                        font-size:12px;
                        padding:8px;
                        margin:10px;
                        font-family: "Lucida Handwriting";'''
        return SHEET

    @staticmethod
    def LOCK():
        SHEET ='''border: 1px solid gray;
                        border-radius: 15;
                        background-color: gray;
                        color:white;
                        font-size:12px;
                        padding:8px;
                        margin:10px;
                        font-family: "Lucida Handwriting";'''
        return SHEET

    @staticmethod
    def Exams():
        SHEET = '''background-color:white;'''
        return SHEET

    @staticmethod
    def Back():
        SHEET ='''QPushButton {
        border: 1px solid gray;
        font-style: italic;font-style: oblique;font-weight: bold;
        border-radius: 15;
        background-color: blue;
        color:white;
        font-size:12px;
        padding:8px;
        font-family: "Lucida Handwriting";
                        }'''
        return SHEET

    @staticmethod
    def Exams_Gp():
        SHEET ='''
        QGroupBox{
height: 20px;
 background-image:url(image/background1.jpg) no-repeat center center ;
 background-repeat: no-repeat;
border: 1px solid red;
border-radius: 15;
border-style:hidden;
 padding:20px;
}
       '''
        return SHEET

