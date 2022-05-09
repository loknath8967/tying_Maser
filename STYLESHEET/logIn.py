class STYLESHEET:
    @staticmethod
    def MAIN():
        SHEET='''
QWidget {background: #002025;border-radius: 30px;opacity: 100;border: 2px solid #002025;}
QLineEdit{
padding-left: 10px;padding-right: 10px;border-radius : 8;border: 3px solid #002025;
background-color:white ;color:black;font-weight: bold;font-family: serif;font-size: 15px;
}
QPushButton{
padding: 5px;border-radius : 12;border: 3px solid blue;background-color:blue ;
color:white;font-weight: bold;font-family: serif;font-size: 15px; outline: none; 
}
QLabel{
color:red; font-size:14px;
}
'''
        return SHEET

    @staticmethod
    def ErrorDetect():
        SHEET = '''
            QWidget {background: #002025;border-radius: 30px;opacity: 100;border: 2px solid red;}
            QLineEdit{
            padding-left: 10px;padding-right: 10px;border-radius : 8;border: 3px solid red;
            background-color:white ;color:black;font-weight: bold;font-family: serif;font-size: 15px;
            }
            QPushButton{
            padding: 5px;border-radius : 12;border: 3px solid red;background-color:blue ;
            color:white;font-weight: bold;font-family: serif;font-size: 15px; outline: none; 
            }
            QLabel{
            color:red; font-size:14px; border-style:hidden;
            }
            '''
        return SHEET

    @staticmethod
    def Clear():
        SHEET ='''
        QWidget {background: #002025;border-radius: 30px;opacity: 100;border: 2px solid #002025;}
        QLineEdit{
        padding-left: 10px;padding-right: 10px;border-radius : 8;border: 3px solid #002025;
        background-color:white ;color:black;font-weight: bold;font-family: serif;font-size: 15px;
        }
        QPushButton{
        padding: 5px;border-radius : 12;border: 3px solid blue;background-color:blue ;
        color:white;font-weight: bold;font-family: serif;font-size: 15px; outline: none; 
        }
        QLabel{
        color:red; font-size:14px;
        }
        '''
        return SHEET

    @staticmethod
    def LogIn():
        SHEET ='''
    QGroupBox{
background-image:url(image/login.jpg) no-repeat center center; border: 1px solid red;
background-repeat: no-repeat;
border-radius: 15; border-style:hidden; height: 20px;
padding-right:1px; padding-top:1px;
}
        '''
        return SHEET

    @staticmethod
    def Back():
        SHEET = '''
        QPushButton{
    border: 1px hidden red;
    border-radius: 15;
    background-color:#8585ad;
    color:white;
    font-size:19px;
    }
            '''
        return SHEET