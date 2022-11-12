import os
from git.repo.base import Repo
import shutil

def CreateProject():
    os.system('cls')
    print('Create Project\n')
    name = input('Enter the name of the project: ')
    path = input('Enter the path of the project: ')

    DownloadProject(path, name)

def DownloadProject(path, name):
    print('Downloading engine...\n')    
    Repo.clone_from('https://github.com/almartdev/insiderengine.git', path + '/' + name)
    print('Engine downloaded!')

    SetupProject(path, name)
    SaveProject(path, name)

def SetupProject(path, name):
    os.rename(path + '/' + name + '/insider.insider', path + '/' + name + '/' + name + '.insider')
    with open(path + '/' + name + '/' + name + '.insider', 'w') as f:
        f.write(name)

def SaveProject(path, name):
    #create a file in the projects folder with the name of the project and the path of the project
    #create a variable with the path of the projects folder
    with open(os.path.dirname(os.path.realpath(__file__)) + '/projects/' + name + '.insider', 'w') as f:
        f.write(name + '\n' + path + '/' + name)

    print('Project created on ' + path + '/' + name)

def OpenProject():
    os.system('cls')

    print('Open Project\n')
    print('1.- Project list')
    print('2.- Find project')

    option = input('Select an option: ')

    if option == '1':
        ProjectList()
    elif option == '2':
        FindProject()

def ProjectList():
    print('\n')

    projectsFolder = os.path.dirname(os.path.abspath(__file__)) + '/projects/'
    for file in os.listdir(projectsFolder):
        if file.endswith('.insider'):

            with open(projectsFolder + file, 'r') as f:
                name = f.readline()
                path = f.readline()

            #print the index of the file and the name of the project
            print(str(os.listdir(projectsFolder).index(file)) + '.- ' + file + '    -    ' + path)
    
    option = input('\nSelect a project: ')
    #check if the option is valid
    if option.isdigit() and int(option) < len(os.listdir(projectsFolder)):
        #open the project with the index of the option
        with open(projectsFolder + os.listdir(projectsFolder)[int(option)], 'r') as f:
            name = f.readline()
            path = f.readline()

            #open folder with the path of the project
            print(path)
            os.startfile(path)

def FindProject():
    os.system('cls')
    print('Find Project\n')
    InsiderPath = input('Enter the path of the project (.insider) file: ')
    if InsiderPath.endswith('.insider'):
        with open(InsiderPath, 'r') as f:
            name = f.readline()
        nameLenth = len(name + '.insider')
        path = InsiderPath[:-nameLenth]
        SaveProject(path, name)
    else:
        print('Invalid path!')

def DeleteProject():
    os.system('cls')
    projectsFolder = os.path.dirname(os.path.abspath(__file__)) + '/projects/'
    for file in os.listdir(projectsFolder):
        if file.endswith('.insider'):

            with open(projectsFolder + file, 'r') as f:
                name = f.readline()
                path = f.readline()

            #print the index of the file and the name of the project
            print(str(os.listdir(projectsFolder).index(file)) + '.- ' + file + '    -    ' + path)
    
    option = input('\nSelect a project: ')
    #check if the option is valid
    if option.isdigit() and int(option) < len(os.listdir(projectsFolder)):
        with open(projectsFolder + os.listdir(projectsFolder)[int(option)], 'r') as f:
            name = f.readline()
            path = f.readline()
        shutil.rmtree(path, ignore_errors=True, onerror=None)
        #delete .insider file from projects folder
        os.remove(projectsFolder + os.listdir(projectsFolder)[int(option)])

def Exit():
    os.system('cls')

print('Welcome to the Launcher\n')

print('1. Create a new project')
print('2. Open an existing project')
print('3. Delete project')
print('4. Exit\n')

choice = input('Please enter your choice: ')

if choice == '1':
    CreateProject()
elif choice == '2':
    OpenProject()
elif choice == '3':
    DeleteProject()
elif choice == '4':
    Exit()
else:
    print('Invalid choice')

input('Press enter to exit...')