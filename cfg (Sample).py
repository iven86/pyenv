    # Python automation for environment variables.
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


## ENV ##

# ENV file path
env_file = '/home/<your-user>/Desktop/api/.env'

# GitLab Project ID
project_id = 'Add here project id'

# GitLab Private Token
private_token = 'Add here your GitLab private token'

# GitHub GitHub Personal Access Token
GITHUB_TOKEN = 'Add here your GitHub private token'
GITHUB_USER = 'Add here your GutHub User'
REPO_NAME = 'Add here your repo name'

#######  Don't Edit Below Lines  ###############################
url = 'https://gitlab.com/api/v4/projects/' + project_id + '/variables'
content_type = 'application/json'

env_protected = 'true' # true|false
env_masked = 'false' #true|false
env_environment_scope = '*'
