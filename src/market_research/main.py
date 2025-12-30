import warnings
from market_research.crew import MarketResearch
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():

    inputs = {
        'product_idea': 'Handy size robots via LLM Integration. A robot which will only inlcude the voice feature. It will listen, and speak according to it. It will be poersonalized, so it will needs memory as well.'   
        }

    try:
        MarketResearch().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
