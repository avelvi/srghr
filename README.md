# srghr

Self-replicating GitHub Repository - application which creates a repository in user's GutHub account with app's code.
(written on Python)


### Technical specification:
(Describes what the application does and how)

The application creates a repository in user's GutHub account with app's code.

When user goes to application <b>host:port</b> it redirects to github authorization page.

After that when user enter his github credentials, application forks this repository into user's GutHub account


### Installation documentation

This documentation containing instructions on how to launch the application and get a working URL that replicates the repository.

1 - Clone this repository on your local environment:
```
    git clone git@github.com:avelvi/srghr.git
```
2 - Go into cloned directory:
```
cd srghr
```
3 - Create <b>.env</b> file with name of the profile.
(by default there is a <b>default.json</b> with all properties):
```
echo default > .env
```

If you need another one, create new "*.json" in the "properties/" folder

4.1 - For linux run:
```
./install.sh
```
4.2 - For Windows run:
```
install.bat
```

5 - Run the application:
```
python3 run.py
```

6 - Go to <b>host:port</b> which was specified in the *.json file and this repository will be forked to your GitHub account.