import os

from ui import gui


class conf_importer:
    ROOT_PATH = None
    conf_lines = ""
    current_tab = None
    current_frame = None

    current_frame_col = 0
    current_button_row = 0

    def __init__(self, conf_file_path, root_path):
        self.ROOT_PATH = root_path
        conf_file = open(root_path + conf_file_path)
        self.conf_lines = conf_file.read().split()

    def create_gui(self, parent):
        top, nb = gui.initialize(parent)
        for line in self.conf_lines:

            s = line.split(':')

            if (s[0].startswith('#')):
                pass

            if (s[0] == 'tab'):
                tab = gui.add_tab(nb, s[1])
                self.current_tab = tab
                self.current_frame_col = 0

            elif (s[0] == 'frame'):
                self.current_frame = gui.add_frame(tab=self.current_tab, frame_name=s[1],
                                                   column=self.current_frame_col)
                self.current_frame_col += 1
                self.current_button_row = 0

            elif (s[0] == 'button'):
                btn = gui.get_button(parent=self.current_frame, text=s[1], col=0, row=self.current_button_row,
                                     command=lambda executable_path=s[2]: self.execute_executable(executable_path))
                self.current_button_row += 1

    def execute_executable(self, ex):
        pass


class conf_importer_win_local(conf_importer):

    def execute_executable(self, executable_path):
        executable_path = self.ROOT_PATH + "\\" + executable_path
        os.system("start " + executable_path)