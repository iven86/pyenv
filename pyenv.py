    # Python automation for environment variables V2.0.
    #
    # Copyright (C) 2020  Iven Leni Fernandez
    #
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU Affero General Public License as
    # published by the Free Software Foundation, either version 3 of the
    # License, or (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU Affero General Public License for more details.
    #
    # You should have received a copy of the GNU Affero General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.


import gitlab as gl
import github as gh

import inquirer
# pip install pyfiglet
import pyfiglet

###########################
#    Choose a platform    #
###########################
def platform():
    platform_questions = [inquirer.List(
    'ENV_Tool_Platform',
    message="Choose a Platform:",
    choices=['GitLab', 'GitHub', 'Exit'])]
    platform_answers = inquirer.prompt(platform_questions)  # returns a dict
    return platform_answers['ENV_Tool_Platform']

###########################
#     ENV GitLab Menu     #
###########################
def gitlab_menu():
    gitlab_questions = [inquirer.List(
    'ENV_gitlab_Menu',
    message="What are you interested in?",
    choices=['List Available variables', 'Build ENV variables', 'Update variable', 'Delete all variables', 'Back to main menu'],)]
    gitlab_answers = inquirer.prompt(gitlab_questions)  # returns a dict
    gitlab_menu_answers(gitlab_answers['ENV_gitlab_Menu'])
    return gitlab_answers['ENV_gitlab_Menu']
    

###########################
#     ENV GitHub Menu     #
###########################
def github_menu():
    github_questions = [inquirer.List(
    'ENV_github_Menu',
    message="What are you interested in?",
    choices=['List Available Secrets', 'Build ENV Secrets', 'Update Secrets', 'Delete all Secrets', 'Back to main menu'],)]
    github_answers = inquirer.prompt(github_questions)  # returns a dict
    github_menu_answers(github_answers['ENV_github_Menu'])
    return github_answers['ENV_github_Menu']

###########################
#   GITLAB MENU ANSWERS   #
###########################
def gitlab_menu_answers(gitlab_answers):

    print('You chosed: ', gitlab_answers)

    while gitlab_answers != "" :
        if gitlab_answers == "List Available variables" :
            print('List Available variables')
            print(gl.list_variables()['key'])
            gitlab_menu()

        elif gitlab_answers == "Build ENV variables" :
            print('Build ENV variables')
            payload = gl.build_env_payload()
            gl.create_variables(payload)
            gitlab_menu()

        elif gitlab_answers == "Update variable" :
            gl.update_variables()
            gitlab_menu()

        elif gitlab_answers == "Delete all variables" :
            gl.delete_variables(gl.list_variables()['key'])
            gitlab_menu()

        elif gitlab_answers == "Back to main menu" :
            platform()
            break

        else :
            gitlab_menu()
            break

###########################
#   GITHUB MENU ANSWERS   #
###########################
def github_menu_answers(github_answers):

    print('You chosed: ', github_answers)

    while github_answers != "" :
        if github_answers == "List Available Secrets" :
            print('List Available Secrets')
            for item in gh.list_Secrets():
                print(item)
            # print(gh.list_Secrets())
            github_menu()

        elif github_answers == "Build ENV Secrets" :
            print('Build ENV Secrets')
            payload = gh.payload
            gh.create_Secrets(payload)
            github_menu()

        elif github_answers == "Update Secrets" :
            payload = gh.payload
            gh.update_Secrets(payload)
            github_menu()

        elif github_answers == "Delete all Secrets" :
            gh.delete_Secrets(gh.list_Secrets())
            github_menu()

        elif github_answers == "Back to main menu" :
            platform()
            break

        else :
            github_menu()
            break

######################################################

ascii_banner = pyfiglet.figlet_format("Py-ENV Tool!!")
print(ascii_banner)

main_menu_answers = platform()

while main_menu_answers != "" :
    if main_menu_answers == "GitLab" :
        gitlab_menu()
        

    elif main_menu_answers == "GitHub" :
        github_menu()

    elif main_menu_answers == "Exit" :
        exit()

    else:
        platform()
        print(main_menu_answers)
        


