import PyQt6.QtWidgets as qt

from core.settings import config

class PathsTab(qt.QWidget):
    def __init__(self, parent=None):
        super(PathsTab,self).__init__()
        layout = qt.QVBoxLayout()

        tts_binary_path_label = qt.QLabel()
        tts_binary_path_label.setText("TTS Binary Path")
        self.tts_binary_path_value = qt.QLineEdit(config.TTSBinaryPath)
        tts_binary_choose_button = qt.QPushButton("Choose file...")
        tts_binary_choose_button.clicked.connect(lambda: self.choose_binary())
        tts_mod_path_label = qt.QLabel()
        tts_mod_path_label.setText("TTS Mod Directory")
        save_button = qt.QPushButton("Save Settings")
        save_button.clicked.connect(self.save_settings)

        layout.addWidget(tts_binary_path_label)
        layout.addWidget(self.tts_binary_path_value)
        layout.addWidget(tts_binary_choose_button)
        layout.addWidget(tts_mod_path_label)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def choose_binary(self):
        binary = qt.QFileDialog.getOpenFileName(self.widget, "Select TTS executable", "/", "*.exe")
        if binary[0]:
            self.tts_binary_path_value.setText(binary[0])
            self.tts_binary_path_value.update()


    def save_settings(self):
        config.set_tts_binary(self.tts_binary_path_value.text())
        config.save()


