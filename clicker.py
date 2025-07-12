# for the future me, if you are wondering why is this code commented cause usually I do not comment my code.
# and that's because you have a nut brain, after sleepign you won't remember how your code works, that's why I wanted to help your dunmb ass
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt 

class Windows(QMainWindow):
    def __init__(self):

        super().__init__()
        #creating the window
        # self.setWindowTitle("Clicker")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("icon.png"))
        self.SetUI()   

    def SetUI(self): # All of things related to UI willl be taken care of here
        #creating a label that will be linked to the background image and used as a background
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("Background.jpg"))
        self.background.setScaledContents(True) 
        self.background.setGeometry(0, 0, self.width(), self.height())
        
        '''
        Backgournd was created before the text to avoid Z-layers conflict
        '''

        #creating the welcoming title label
        self.label = QLabel("Click as much as you can!!!!", self)
        self.label.setFont(QFont("Aerial", 40))
        self.label.setGeometry(0, 0, self.width(), 100)
        self.label.setStyleSheet("color: #647E68;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "font-size: 25px;")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        #Create a score ( creation of score before the button itself is executed to avoid layers conflict)
        self.score = QLabel("Click on the button", self)
        self.score.resize(300, 100)
        self.score.setStyleSheet("font-size: 25px; color: red;font-weight: bold;")
        #create a button
        self.click_count = 0 #count how mnay times you clicked the button

        self.button = QPushButton("I want to be clicked!", self)
        self.button.setGeometry(200, 200, 300, 100)
        self.button.setStyleSheet("""
                                  
                                background-color: transparent;
                                color: #A27B5C;
                                font-weight: bold;
                                font-size: 22px;
                                border: 2px solid #A27B5C;
                                border-radius: 12px;
                                padding: 10px 20px;
                                letter-spacing: 1px;
                                text-transform: uppercase;

                                QPushButton:hover {
                                    color: #7A3E0D;
                                    border-color: #7A3E0D;
                                    background-color: rgba(86, 43, 8, 0.05);
                                    }
                                QPushButton:pressed {
                                    background-color: rgba(86, 43, 8, 0.12);
                                    border-color: #3B1A05;
                                    bolor: #3B1A05;
                                    }
                                """)
        self.button.clicked.connect(self.button_clicked)
    #add a function that get triggered when clikcking on a button
    def button_clicked(self):
        self.click_count += 1
        self.score.setText(f"You clicked {self.click_count} times")

        #this is a very important function, this is the reason why when  change windows size nothing break (CSS is shit)
        #If you remarked, I never called this function but it works. And that's because PyQt5 always call a function if you call it exactly "resizeEvent"
    def resizeEvent(self, event):
        self.label.setGeometry(0, 0, self.width(), 100)
        self.background.setGeometry(0, 0, self.width(), self.height())
        btn_x = (self.width() - self.button.width()) // 2
        btn_y = (self.height() - self.button.height()) // 2  
        self.button.move(btn_x, btn_y)
        btn_a = (self.width() - self.score.width()) // 2
        btn_b = btn_y + self.button.height() + 20 
        btn_a += 40
        self.score.move(btn_a, btn_b)

def show_windows():
    app = QApplication(sys.argv)
    windows = Windows()
    windows.show()    
    sys.exit(app.exec_())

show_windows()
