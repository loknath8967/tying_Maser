class STYLESHEET:
    @staticmethod
    def Table():
        SHEET = """QHeaderView::section{
        Background-color:rgb(190,1,1);
        font-size:19px;
        text-align:center;
        color:white;
        }
        QTableWidget{
        margin-top:10px;
        }
        """
        return SHEET

    @staticmethod
    def Empty():
        SHEET ='''QLabel{
                        font-size:20px;
                        color:red;
                        }        
                        '''
        return SHEET

    @staticmethod
    def MarkSheet():
        SHEET ='''
                QLabel{
                font-size:20px;
                color:blue;
                border:5px hidden green;
                border-bottom-style:double;
                
                }        
                '''
        return SHEET

