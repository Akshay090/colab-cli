# Welcome to colab-cli 👋
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://choosealicense.com/licenses/mit/)
[![Twitter: aks2899](https://img.shields.io/twitter/follow/aks2899.svg?style=social)](https://twitter.com/aks2899)

> Experience better workflow with google colab, local jupyter notebooks and git

You can now easily manage working with jupyter notebooks 
and google colab from cli. 

# Features 
* 🤠 Upload local jupyter notebook to gdrive from cli
* 😮 Quick access to jupyter notebooks in gdrive from your cli
* 🚀 Keeps jupyter notebooks organized in gdrive by creating local file structure in gdrive
* 🤯 Sync local work on notebooks with gdrive
* 🥂 Git friendly, pull changes from gdrive and commit to git

### ✨ Demo
[![demo](https://asciinema.org/a/314749.svg)](https://asciinema.org/a/314749?autoplay=1)

## Install

```sh
python -m pip install colab-cli
```
OR
```sh
python3.7 -m pip install colab-cli
```
## Set-up

STEP-1: 
 
First we need to get your client_secrets.json file for 
OAuth2.0 authentication for Drive API,

1. Go to [APIs Console](https://console.developers.google.com/iam-admin/projects) 
and make your own project.
2. Search for ‘Google Drive API’, select the entry, and click ‘Enable’.
3. Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.
4. Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. Once finished:
    
    a. Select ‘Application type’ to be Web application.
    
    b. Enter an appropriate name.
    
    c. Input http://localhost:8080 for ‘Authorized JavaScript origins’.
    
    d. Input http://localhost:8080/ for ‘Authorized redirect URIs’.
    
    e. Click ‘Save’.
    
5. Click ‘Download JSON’ on the right side of Client ID to 
download client_secret_\<really long ID>.json.

6. Rename the file to “client_secrets.json” and place it in any directory.

STEP-2: 

 Go to the local directory with client_secrets.json
  ```sh
  colab-cli set-config client_secrets.json
  ```
STEP-3:
 
Now we need to set the google account user id, goto your browser and see how many google logins you have,
 the count start from zero
 
 for eg. I have 3 login and I use the second one for coding work, so my user id is 1
  ```sh
  colab-cli set-auth-user 1
  ```
 
🙌 Now You're all set to go
## Usage

```sh
colab-cli --help
``` 
* List local ipynb
```sh
colab-cli list-nb
``` 
NOTE : Please work with git repo initialized, else below 
commands will not work

* Open local ipynb file in google colab for first time
> Note: It opens the copy of file in gdrive from second time onwards.
```sh
colab-cli open-nb lesson1-pets.ipynb
``` 
* If you need to get modified ipynb from gdrive local directory use 
```sh
colab-cli pull-nb lesson1-pets.ipynb
``` 
* Made some changes to ipynb locally, push it to gdrive
```sh
colab-cli push-nb lesson1-pets.ipynb
``` 

## Author

👤 **Akshay Ashok**

* Twitter: [@aks2899](https://twitter.com/aks2899)
* Github: [@Akshay090](https://github.com/Akshay090)
* LinkedIn: [@akshay-a](https://linkedin.com/in/akshay-a)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check [issues page](https://github.com/Akshay090/colab-cli/issues). You can also take a look at the [contributing guide](https://github.com/Akshay090/colab-cli/blob/master/CONTRIBUTING.md).

## Show your support

Give a 🌟 if this project helped you!

## 📝 License

Copyright © 2020 [Akshay Ashok](https://github.com/Akshay090).

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

***
_This README was generated with ❤ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
