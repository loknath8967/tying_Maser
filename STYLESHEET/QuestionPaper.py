class STYLESHEET:
    @staticmethod
    def MAIN():
        SHEET='''QWidget{
        background-color:red;
        border-radius:10px;
        color:white;
        border-style:hidden;font-size:21px; 
                font-family: "Comic Sans MS";
        }'''
        return SHEET

    @staticmethod
    def Button():
        SHEET='''QPushButton{
       
        background-color:green;
        border:2px solid green;
        border-radius:10px;
        border-style:hidden;font-size:15px; 
        font-family: "Comic Sans MS";
        
        }'''
        return SHEET


    @staticmethod
    def Display():
        SHEET='''
        QTextEdit{
                border: 9px solid gray;
                border-radius: 15;
                border-style:double;
                border-bottom-style:hidden;
                border-bottom-left-radius:5px;
                border-bottom-right-radius:5px;
                color:rgb(168,168,168);
                font-size:18px;
                padding:8px;
                font-family: "Comic Sans MS";
                scrollbar-width: none;
                user-select: none;
                background-color:rgb(240,240,240);

                                }'''
        return SHEET

    @staticmethod
    def Editor():
        SHEET='''QTextEdit { border: 9px solid gray; border-radius: 15;
                                border-style:double;
                                border-top-style:hidden;
                                border-top-left-radius:5px;
                                border-top-right-radius:5px;
                                color:black;
                                font-size:18px;
                                padding:8px;
                                font-family: "Comic Sans MS";
                                background-color:white;
                                }'''

        return SHEET

    @staticmethod
    def Title():
        SHEET='''QGroupBox{
        border-style:hidden;
        }'''
        return SHEET


    @staticmethod
    def Result():
        SHEET='''
        QGroupBox{
                        border-style:hidden;

                }

        QLabel{

                        border-style:hidden;
                        font-size:19px;
                        color:blue;
                        padding:8px;
                        font-family: "Lucida Handwriting";
                        background-color: red;


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
    def MsgSubmit():
        SHEET='''color:white; background-color:green; text-align:center; width:120px; height:30px;
        font-size:20px;border:2px solid rgb(104,104,104);border-style:hidden;
        border-radius:15px;font-family: Lucida Handwriting ;font-weight: bold;'''


        return SHEET

    @staticmethod
    def MsgCancel():
        SHEET = '''color:white; background-color:red; text-align:center; width:70px; height:30px;
        font-size:20px;border:2px solid rgb(104,104,104);border-style:hidden;
        border-radius:15px;font-family: Lucida Handwriting ;font-weight: bold;'''

        return SHEET

    @staticmethod
    def MsgBox():
        SHEET = '''
        QMessageBox{
        border-style:hidden;
        background-color:white;

        }
        QLabel{
        background-color:white;
        border-style:hidden;
        test-align:center;
        color:black;
        font-size:15px;
        font-family: Lucida Handwriting ;font-weight: bold;
        }

         '''
        return SHEET