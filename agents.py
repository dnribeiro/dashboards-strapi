from crewai import Agent
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

# Cria uma instância do modelo Gemini com todos os parâmetros necessários
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY")) # type: ignore

class CustomAgents:
    def __init__(self):
        self.GoogleGenAI = llm

    def input_reader(self):
        return Agent(
            role="Leitor dos dados e tabelas recebidos por input",
            backstory=dedent(f"""Você é um excelente interpretador do formato .json, e domina estratégias para tornar este formato
                             de dados o mais compreensível possível, sem alterar os dados nele contidos."""),
            goal=dedent(f"""Você deve receber dados json vindo de uma requisição http """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.GoogleGenAI
        )

    def agent_2_name(self):
        return Agent(
            role="Define agent 2 role here",
            backstory=dedent(f"""Define agent 2 backstory here"""),
            goal=dedent(f"""Define agent 2 goal here"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.GoogleGenAI
        )
