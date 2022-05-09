class STYLESHEET:
    @staticmethod
    def TopBAR():
        SHEET='''QPushButton{
        font-size:18px;
        }
        QLabel{
        font-size:18px;
        color:red;
        }
               
        '''
        return SHEET

    @staticmethod
    def Layout():
        SHEET ='''QTabBar::tab{
                    width: 0;height: 0; margin: 0; padding: 0; border: none;  
                    }'''
        return SHEET