import PyQt6.QtWidgets as qt

from core.settings import config

class PathsTab:
    def __init__(self, ):
        self.widget = qt.QWidget()
        self.layout = qt.QVBoxLayout()

        tts_binary_path_label = qt.QLabel()
        tts_binary_path_label.setText("TTS Binary Path")
        tts_binary_path_value = qt.QLineEdit()
        tts_binary_choose_button = qt.QPushButton("Choose file...")
        tts_binary_choose_button.clicked.connect(lambda: self.choose_binary())
        tts_mod_path_label = qt.QLabel()
        tts_mod_path_label.setText("TTS Mod Directory")

        self.layout.addWidget(tts_binary_path_label)
        self.layout.addWidget(tts_binary_path_value)
        self.layout.addWidget(tts_binary_choose_button)
        self.layout.addWidget(tts_mod_path_label)

        self.widget.setLayout(self.layout)

    def choose_binary(self):
        binary = qt.QFileDialog.getOpenFileName(self.widget, "Select TTS executable", "/", "*.exe")
        if binary[0]:
            config.set_tts_binary(binary[0])


