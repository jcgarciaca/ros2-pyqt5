#! /usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from utils.ui_qt import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication

import threading

class MainWindow(QMainWindow):
    def __init__(self, args=None, parent=None):
        super(MainWindow, self).__init__(parent)
        self.topic_name = 'talker_tp'
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton.clicked.connect(self.publish_btn_cb)
        self.init_ros(args)
        self.counter = 0
        self.state = False

    def init_ros(self, args):
        rclpy.init(args=args)
        self.node = Node('Qt_GUI')
        self.subscription = self.node.create_subscription(
            String,
            self.topic_name,
            self.listener_callback,
            10
        )
        self.publisher_ = self.node.create_publisher(String, '/gui_talker_tp', 10)
        thread = threading.Thread(target=self.spin_loop)
        thread.daemon = True
        thread.start()
    
    def spin_loop(self):
        rclpy.spin(self.node)
        self.node.destroy_node()
        rclpy.shutdown()

    def listener_callback(self, msg):
        self.ui.label.setText(msg.data)
        self.counter += 1
        '''
        if self.counter % 10 == 0:
            if self.state:
                self.show()
            else:
                self.hide()
            self.state = not self.state
        '''
    
    def publish_btn_cb(self):
        msg = String()
        msg.data = self.ui.lineEdit.text()
        self.publisher_.publish(msg)

def main(args=None):
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()