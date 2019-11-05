#import sys;
#from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel
#                            , QMessageBox, QAction, QHBoxLayout, QVBoxLayout );
#from PyQt5.QtCore import QCoreApplication;

#from PyQt5.QtGui import QPixmap;

#from typing import List;

#class Window(QMainWindow):
    
#    def __init__(self):
#        super().__init__(); # 사위 객체 생성

#        #self.load_tile();
#        self.init_menu();
#        self.init_btn();

#        hbox = QHBoxLayout(slef);
#        self.tiles:QPixmap = QPixmap('assets/Tile/tile (1).png');
#        lbl = QLabel(self);
#        lbl.setPixmap(self.tiles);
#        hbox.addWidget(lbl);
#        self.setLayout(hbox);

#        self.init_window();

#    def init_window(self):
#        self.resize(1024, 1024); # set window size
#        self.setWindowTitle("MapTool"); 

#        self.show();


#    def init_btn(self):
#        #window opt
#        exit_btn = QPushButton('exit', self);
#        exit_btn.resize(exit_btn.sizeHint());
#        exit_btn.setToolTip("현재 프로그램을 종료합니다.");
#        exit_btn.move(250, 250);
#        exit_btn.clicked.connect(QCoreApplication.instance().quit);


#    def closeEvent(self, QCloseEvent):
#        answer = QMessageBox.question(self, "종료 확인","종료 할것인지?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes);

#        if answer == QMessageBox.Yes:
#            QCloseEvent.accept();
#        else:
#            QCloseEvent.ignore();
#        pass;

#    def init_menu(self):
#        menu = self.menuBar();
        
#        menu_file = menu.addMenu('File');
#        menu_edit = menu.addMenu('Edit');

#        # file 메뉴 액션
#        save_file = QAction("save", self);
#        save_file.setShortcut("ctrl+s");

#        new_file = QAction("new", self);
#        new_file.setShortcut("ctrl+n");

#        exit = QAction("exit", self);
#        exit.setShortcut ("ctrl+q");
#        exit.triggered.connect(qApp.quit);

#        open = QAction("open", self);
#        open.setShortcut ("ctrl+o");
#        #exit.triggered.connect(QCoreApplication.instance().quit);

#        menu_file.addAction(save_file);
#        menu_file.addAction(new_file);
#        menu_file.addAction(exit);
#        menu_file.addAction(open);



#    def lqyout_init(self):
#        pass;

#    def load_tile(self):
#        slef.tiles.append(QPixmap('assets/Tile/tile (1).png'));
#        slef.tiles.append(QPixmap('assets/Tile/tile (2).png'));
#        slef.tiles.append(QPixmap('assets/Tile/tile (3).png'));
#        slef.tiles.append(QPixmap('assets/Tile/tile (4).png'));
#        slef.tiles.append(QPixmap('assets/Tile/tile (5).png'));
#        slef.tiles.append(QPixmap('assets/Tile/tile (6).png'));
#        slef.tiles.append(QPixmap('assets/Tile/tile (7).png'));
#        slef.tiles.append(QPixmap('assets/Tile/tile (8).png'));
#        slef.tiles.append(QPixmap('assets/Tile/tile (9).png'));
#        slef.tiles.append(QPixmap('assets/Tile/tile (10).png'));
#        slef.tiles.append(QPixmap('assets/Tile/tile (11).png'));
#        print("end");


#app = QApplication(sys.argv);
#window = Window();
#sys.exit(app.exec_()); #윈도우 이벤트큐
