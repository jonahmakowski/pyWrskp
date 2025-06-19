from llama_ai import llama_result
import commands
import audio
import helpers
import tkinter as tk


class CommandExecution:
    def __init__(self):
        self.username_write = ""
        self.username_speak = ""
        self.assistant_name = ""
        self.query = ""
        self.setup()

    def setup(self):
        self.username_write = "Jonah"  # This is used by the assistant to refer to you
        self.username_speak = "Jonah"  # This is used by the assistant to refer to you
        self.assistant_name = (
            "Assistant"  # This is used by the speak function in the printout
        )
        with open("details.txt", "w") as file:
            file.write(self.username_write + "\n")
            file.write(self.username_speak + "\n")
            file.write(self.assistant_name + "\n")

        audio.speak("Welcome {{USERNAME}}!")

    def decide(self):
        ai_result = llama_result(self.query)
        commands_from_ai, non_commands_from_ai = self.find_commands(ai_result)
        speak_index = 0
        print(self.assistant_name, end=": ")
        for command in commands_from_ai:
            print(non_commands_from_ai[speak_index], end="")
            audio.speak(non_commands_from_ai[speak_index])
            if "APP" in command:
                commands.open_app(helpers.remove_keyword(command, "APP"))
            elif "FILE" in command:
                commands.open_file(helpers.remove_keyword(command, "FILE"))
            elif "PLAY" in command:
                commands.play()
            elif "PAUSE" in command:
                commands.pause()
            elif "WEBSITE" in command:
                commands.open_webpage(helpers.remove_keyword(command, "WEBSITE"))
            elif "GOOGLE" in command:
                commands.google_search(helpers.remove_keyword(command, "GOOGLE"))
            speak_index += 1
        print()

    @staticmethod
    def find_commands(ai_input):
        command = ai_input.split("$")
        non_command = ai_input.split("$")
        to_delete = 0
        if len(command) != 1:
            while to_delete < len(command):
                del command[to_delete]
                to_delete += 1
            to_delete = 1
            while to_delete < len(non_command):
                del non_command[to_delete]
                to_delete += 1
        return command, non_command

    def change_name(self):
        names = helpers.remove_keyword(self.query, "name")
        names = helpers.remove_keyword(names, "change")
        names = names.split()
        self.username_write = names[0]
        self.username_speak = names[0]
        self.assistant_name = names[1]
        with open("details.txt", "w") as file:
            file.write(self.username_write + "\n")
            file.write(self.username_speak + "\n")
            file.write(self.assistant_name + "\n")

        audio.speak("Welcome {{USERNAME}}!")
        audio.speak("I am now {}".format(self.assistant_name))


class Main:
    def __init__(self):
        self.speakbutton = None
        self.combo_box = None
        self.sendbutton = None
        self.inputtxt = None
        self.frame = None
        self.main_setup()
        self.CommandExecution = CommandExecution()
        self.frame.mainloop()

    def main_setup(self):
        self.frame = tk.Tk()
        self.frame.title("Your Assistant")
        self.frame.geometry("250x110")
        self.frame.resizable(False, False)

        self.frame.attributes("-topmost", True)

        self.inputtxt = tk.Text(self.frame, height=2, width=35, wrap=tk.WORD)
        self.sendbutton = tk.Button(self.frame, text="Send", command=self.get_input)
        self.speakbutton = tk.Button(self.frame, text="Audio", command=self.get_audio)

        self.speakbutton.pack()
        self.inputtxt.pack()
        self.sendbutton.pack()

    def get_audio(self):
        inp = audio.take_command()
        self.CommandExecution.query = inp
        self.CommandExecution.decide()

    def get_input(self):
        inp = self.inputtxt.get(1.0, "end-1c")
        self.inputtxt.delete("1.0", tk.END)
        self.CommandExecution.query = inp
        self.CommandExecution.decide()


if __name__ == "__main__":
    main = Main()
