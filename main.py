from fastapi import FastAPI, Body
from automation.controller import perform_browser_action

app = FastAPI()

@app.post("/automate")
def automate_browser(command: str = Body(...)):
    result = perform_browser_action(command)
    return {"status": "done", "message": result}
