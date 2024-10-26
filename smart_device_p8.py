class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name="Camera"):
        print(f"Installing {app_name}...")
        if app_name not in self.app_list:
            self.app_list.append(app_name)
        return self.app_list

    def delete_app(self, app_name):
        print(f"Deleting {app_name}...")
        if app_name in self.app_list:
            self.app_list.remove(app_name)
            


device_a = SmartDevice(101395, 'Les', 5.7)
device_a.report()

device_a.install_app("Instagram")
print(device_a.app_list)
device_a.install_app("YouTube")
print(device_a.app_list)
device_a.install_app("YouTube")
print(device_a.app_list)
device_a.delete_app("YouTube")
print(device_a.app_list)
device_a.install_app()
