class STYLESHEET:
    @staticmethod
    def ICON():
        SHEET='''QPushButton{
          font-size:15px;background-color:blue;border-style:hide; font-weight: bold;
          border-radius:10; color:white; font-family: Lucida Handwriting ;
          }
        '''
        return SHEET

    @staticmethod
    def GEOMETRY():
        SHEET ='''QPushButton{ background-color:rgb(168,168,168);
         border:2px solid rgb(104,104,104); 
            border-style:double;
            }
        :hover {
          background-color: rgb(144,144,144);
        }
         '''
        return SHEET

    @staticmethod
    def MAXIMIZATION():
        SHEET ='''QPushButton{background-color:rgb(168,168,168);
         border:3px solid black; 
         border-right-style:double; border-top-style:double;
         border-left-width:1px; border-bottom-width: 1px;
         }
         :hover {
          background-color: rgb(144,144,144);
        }'''
        return SHEET

    @staticmethod
    def MAXIMIZE():
        SHEET ='''QPushButton{
                background-color:blue;border-style:hide;
                }
                 :hover {
          background-color: rgb(144,144,144);
        }'''
        return SHEET

    @staticmethod
    def MINIMIZATION():
        SHEET = '''background-color:rgb(168,168,168);
             border:2px solid rgb(208,208,208); 
             '''
        return SHEET
    @staticmethod
    def MINIMIZE():
        SHEET ='''QPushButton{
        background-color:blue;border-style:hide;
    }
         :hover {
  background-color: rgb(144,144,144);
}'''
        return SHEET

    @staticmethod
    def CLOSE():
        SHEET ='''QPushButton{
  font-size:20px;background-color:blue;border-style:hide; border-radius:3; 
  font-family: Bradley Hand ITC; font-weight: bold; color:rgb(208,208,208);
  }
QPushButton:hover {
  background-color: rgb(255, 26, 26);
}'''
        return SHEET

    @staticmethod
    def TITLE():
        SHEET ='''background-color:gray;'''
        return SHEET
