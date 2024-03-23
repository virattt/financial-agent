# Financial Agent
This is a financial agent that can help you with your financial queries. 
It is built using the LangChain framework.

For a simple example of how this agent works, check out the colab notebook [here](https://colab.research.google.com/gist/virattt/de0423a505f8c7e28f79aef541f6dce0/langchain-financial-agent.ipynb).

## Installation
Clone to repo to your local machine
```bash
git clone https://github.com/virattt/financial-agent.git
```

Then, navigate to the `/financial-agent` directory.

Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate
```

Install the LangChain CLI if you haven't yet:

```bash
pip install -U langchain-cli
```

Add your API keys to your environment variables:
```shell
export OPENAI_API_KEY=<your-openai-api-key>
export POLYGON_API_KEY=<your-polygon-api-key>
```

If you don't have an OpenAI API key, you can get one [here](https://platform.openai.com/).

If you don't have a Polygon API key, you can get one [here](https://polygon.io/).

## Launch the app locally

```bash
langchain serve
```

Then navigate to `http://localhost:8000/agent/playground/` in your browser!

## Questions?
Feel free to reach out to me on X [here](https://twitter.com/virattt).
