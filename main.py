import uvicorn

from projectname.main import app

def run():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, headers=[("server", "you-custom-web-name")])

if __name__ == "__main__":
    run()
