from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/agent/playground")

# # Edit this to add the chain you want to add
# add_routes(app, NotImplemented)

from app.agent import agent
add_routes(app, agent, path="/agent")

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)