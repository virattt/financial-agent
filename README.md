# Financial Agent

This is a financial agent built on Langchain and FastAPI. It can access current price, historical prices, latest news, and financial data for a ticker via the Polygon API. 

Furthermore, it can compute financial metrics like owner earnings, return on equity, and return on invested capital.

The agent also has the ability to do a simple discounted cash flow valuation.

To use this agent, you will need an OpenAI API key and a Polygon API key.

For a simple example of how this agent works, check out the colab notebook [here](https://colab.research.google.com/gist/virattt/de0423a505f8c7e28f79aef541f6dce0/langchain-financial-agent.ipynb).

**Disclaimer**: The agent is **not** intended as financial advice.  The agent is for informational and entertainment purposes only.  As Warren Buffett says, do your own due diligence.
## Deploy locally with Docker

For easy install and secure containerized deployment, install the appropriate version of [Docker](https://www.docker.com/) for your operating system.

Next, open a terminal and build a Docker image from the remote repository:

```bash
docker build -t virattt-financial-agent https://github.com/virattt/financial-agent.git
```

Then, run the Docker container, replacing `$OPENAI_API_KEY` and `$POLYGON_API_KEY` in the following command with your OpenAI and Polygon API keys:

```bash
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -e POLYGON_API_KEY=$POLYGON_API_KEY -p 8000:8000 --name financial-agent -it virattt-financial-agent
```

Navigate to `http://localhost:8000/agent/playground/` in your browser to interact with the agent.

To stop the container, run:

```bash
docker stop financial-agent
```

## Local deployment without Docker

To deploy the agent locally without Docker, make sure you have an up-to-date version of [Python](https://www.python.org/downloads/) installed on your machine.

Open a terminal, clone the repo to your local machine, and open the folder:

```bash
git clone https://github.com/virattt/financial-agent.git
cd financial-agent
```

We recommend using the poetry package manager to install dependencies for this project. First, install the latest version of [Poetry](https://python-poetry.org/docs/#installation) for your operating system.

Poetry will automatically create a virtual environment for this project. To install the dependencies and activate the virtual environment, run:

```bash
poetry install
poetry shell
```

Copy the `.env.example` file to a new file called `.env`:

```bash
cp .env.example .env
```

Then, open the `.env` file in a text editor and add your OpenAI and Polygon API keys.

Alternatively, you can set these environment variables in your terminal:

```bash
export OPENAI_API_KEY=<your-openai-api-key>
export POLYGON_API_KEY=<your-polygon-api-key>
```

- If you don't have an OpenAI API key, you can get one [here](https://platform.openai.com/).
- If you don't have a Polygon API key, you can get one [here](https://polygon.io/).

Finally, start the LangChain server:

```bash
poetry run langchain serve
```

Then navigate to `http://localhost:8000/agent/playground/` in your browser!

## Questions?

Feel free to reach out to me on X [here](https://twitter.com/virattt).
