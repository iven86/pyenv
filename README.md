<h1 align="center">Welcome to Py-ENV  - Beta</h1>
<p align="center">
    <img src="https://img.shields.io/github/v/release/iven86/pyenv" />
    <a href="https://github.com/iven86/pyenv/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/iven86/pyenv" />
    </a>
    <img src="https://img.shields.io/github/downloads/iven86/pyenv/total" />
    <img src="https://img.shields.io/github/languages/top/iven86/pyenv" />
</p>

<h2>Python automation for environment variables</h2>
> CLI that generates, update and delete environment variables in GitLab CI/CD and GitHub Secrets.
> New Update V2.0 Support multiple platforms (GitHub and GitHub)

![alt text](https://raw.githubusercontent.com/iven86/pyenv/main/img/im01.png)

> GitLab Options:

![alt text](https://raw.githubusercontent.com/iven86/pyenv/main/img/im02.png)

> GitHub Options:

![alt text](https://raw.githubusercontent.com/iven86/pyenv/main/img/im03.png)

## 🚀 Usage

> Make sure to add all environment variables information in .env file
> Than modify cfg.py file after rename it from cfg (Sample).py to cfg.py
> And update bellow varaibles:
> ENV file path.
> GitLab Project ID.
> GitLab Private Token.
> GitHub Token 
> GitHub User
> GitHub REPO Name

Example of `cfg.py`:
```python

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

```

## Author

👤 **Iven Leni Fernandez**

- Twitter: [@iven86](https://twitter.com/iven86)
- Github: [@iven86](https://github.com/iven86)
- Linkedin: [@iven86](https://www.linkedin.com/in/iven86/)

## ✨ Contributing
If you've ever wanted to contribute to open source, and a great cause, now is your chance!

See the [contributing docs](https://github.com/iven86/pyenv/blob/main/docs/contributing.md) for more information

## 📝 License

Copyright © 2020 [Iven Leni Fernandez](https://github.com/iven86).<br />
This project is [AGPL-3.0](https://github.com/iven86/pyenv/blob/main/LICENSE) licensed.