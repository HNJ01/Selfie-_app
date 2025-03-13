from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout

class Selfie_App(App):
    def build(self):
        self.obj_camera = Camera()
        self.obj_camera.resolution = (810, 810)
        obj_button = Button(text='Take Selfie')
        obj_button.size_hint = (0.5, 0.2)
        obj_button.pos_hint = {'center_x': 0.25, 'center_y': 0.25}
        obj_button.bind(on_press=self.selfie_take)
        obj_layout = BoxLayout()
        obj_layout.add_widget(self.obj_camera)
        obj_layout.add_widget(obj_button)
        return obj_layout


    def selfie_take(self, *args):
        try:
            self.obj_camera.export_to_png('selfie.png')
            print('Selfie saved successfully!')
        except Exception as e:
            print('Error saving selfie:', str(e))

if __name__ == '__main__':
    Selfie_App().run()

#The above code will create a simple Kivy app that will take a selfie using the camera of the device. The selfie will be saved as selfie.png in the current directory. The resolution of the selfie will be 810x810 pixels. The app will have a button that will trigger the selfie taking process. The selfie will be saved when the button is pressed.