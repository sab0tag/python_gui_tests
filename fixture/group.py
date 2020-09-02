class GroupHelper:
    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        group_lst = []
        self.open_group_editor()
        pass
        self.close_group_editor()
        return group_lst

    def add_new_group(self, name):
        group_lst = []
        self.open_group_editor()
        pass
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()
