# Welcome to colab-cli 👋
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://choosealicense.com/licenses/mit/)
[![Twitter: aks2899](https://img.shields.io/twitter/follow/aks2899.svg?style=social)](https://twitter.com/aks2899)

> Experience better workflow with google colab, local jupyter notebooks and git

### ✨ Demo
[![demo](https://asciinema.org/a/314749.svg)](https://asciinema.org/a/314749?autoplay=1)

## Install

```sh
python -m pip install colab-cli or python3.7 -m pip install colab-cli
```
## Set-up

STEP-1: 
 
 Get your client_secrets.json, [instructions given here](https://pythonhosted.org/PyDrive/quickstart.html),
only follow till the part where you have client_secrets.json in a local directory

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
* Open local ipynb file in google colab for first time and remote copy for subsequent time
```sh
colab-cli open-nb lesson1-pets.ipynb
``` 
* Now you have made some changes to ipynb in colab, get the modified file locally by
```sh
colab-cli pull-nb lesson1-pets.ipynb
``` 
* Made some changes to ipynb locally, push it to drive
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

Feel free to check [issues page](https://github.com/Akshay090/colab-cli/issues). You can also take a look at the [contributing guide](https://github.com/Akshay090/colab-cli/contributing.md).

## Show your support

Give a 🌟 if this project helped you!

## 📝 License

Copyright © 2020 [Akshay Ashok](https://github.com/Akshay090).

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

***
_This README was generated with ❤ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_