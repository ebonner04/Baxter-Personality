# TODO: Some imports

class Personality(Object):
    def __init__(self):
        """
        Gives Baxter a personality
        """
        # TODO: Add all necessary properties
        self._done = False
        self._head = baxter_interface.Head()

        # verify robot is enabled
        print("Getting robot state... ")
        self._rs = baxter_interface.RobotEnable(CHECK_VERSION)
        self._init_state = self._rs.state().enabled
        print("Enabling robot... ")
        self._rs.enable()
        print("Running. Ctrl-c to quit")

        # TODO: Spin up TCP servers for control messages as ros threads

    def clean_shutdown(self):
        """
        Exits example cleanly by moving head to neutral position and
        maintaining start state
        """
        print("\nExiting example...")
        if self._done:
            self.set_neutral()
        if not self._init_state and self._rs.state().enabled:
            print("Disabling robot...")
            self._rs.disable()

    def set_neutral(self):
        """
        Sets the head back into a neutral pose
        """
        self._head.set_pan(0.0)

    def move_head(self):
        # TODO: Move the head (see baxter_examples/scripts/head_wobbler.py)
        return

     def display_image(self):
        # TODO: Display image (see baxter_examples/scripts/xdisplay_image.py)
        return

     def head_tilt_msg_server(self):
        """
        A function to read the desired angle and speed for the head and
        stores to property of the Personality object
        """
        # TODO: Write Function

     def image_msg_server(self):
        """
        A function to read the desired image head and
        stores to property of the Personality object
        """
        # TODO: Write Function

def main():
    # TODO: Write a main function

if __name__ == '__main__':
    main()

