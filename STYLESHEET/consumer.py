class STYLESHEET:
    @staticmethod
    def TabView():
        SHEET='''QTabBar::tab{
            width: 0; height: 0; margin: 0; padding: 0; border: none;
            } '''
        return SHEET

    @staticmethod
    def Button():
        SHEET ='''QPushButton{
        font-size:15px; color:white; background-color:gray; text-align:center;
        padding-top:10px; padding-bottom:10px; margin:20px; border:2px solid gray;
        }'''
        return SHEET

    @staticmethod
    def Management():
        SHEET ='''QWidget{ background-color: rgb(224,224,224) ; }'''
        return SHEET

    @staticmethod
    def LogOut():
        SHEET ='''QPushButton{
        font-size:15px; color:white; background-color: #ff1a1a; text-align:center;
        padding-top:10px; padding-bottom:10px; margin:20px; border:2px solid #ff1a1a;
        }'''
        return SHEET

