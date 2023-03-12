#from gptsh.gpt import hello
import subprocess
import os
from rich.console import Console
from rich.prompt import Prompt
import readline
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

def run():
    console = Console()
    while True:
        command =  Prompt.ask(f"[blue](gptsh) {os.getcwd()[-1]} [/blue]")
        if command.strip() == 'exit':
            break
        try:
            if command.startswith('cd '):
                # If the command starts with "cd ", change the current directory
                new_dir = command[3:].strip()
                os.chdir(new_dir)
            else:
                # Otherwise, run the command using subprocess.run with shell=True
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    console.print(result.stdout)
                else:
                    console.print(f"Error: [red]{result.stderr}[/red]")
        except Exception as e:
            console.print(f"Error: [bold red]{e}[/bold red]")
