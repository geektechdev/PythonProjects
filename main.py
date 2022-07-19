import subprocess

print('Welcome to python cmd')
def runCommand():
    while True:
        try:
            command = input('> ')
            if command.lower() == 'exit':
                print('Bye')
                break
            subprocess.run(command)
        except:
            command = input('Enter Command : ')

runCommand()