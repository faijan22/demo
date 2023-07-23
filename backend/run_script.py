import subprocess

def install_libraries():
    subprocess.run(["pip", "install", "-r", "req.txt"])

def run_migrations():
    subprocess.run(["python", "manage.py", "makemigrations"])
    subprocess.run(["python", "manage.py", "migrate"])

def add_data():
    subprocess.run(["python", "manage.py", "add-data"])

def run_server():
    subprocess.run(["python", "manage.py", "runserver"])

if __name__ == "__main__":
    install_libraries()
    run_migrations()
    add_data()
    run_server()
