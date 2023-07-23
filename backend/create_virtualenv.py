import subprocess
def create_virtualenv():
    virtualenv_name = "myenv"
    subprocess.run(["pip", "install", "virtualenv"])
    subprocess.run(["python", "-m", "venv", virtualenv_name])

if __name__ == "__main__":
    create_virtualenv()

