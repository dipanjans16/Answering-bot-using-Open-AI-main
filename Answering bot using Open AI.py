# -*- coding: utf-8 -*-
"""
@author: Dipanjan
"""

from dotenv import load_dotenv
import pandas as pd
from pandasai import PandasAI




load_dotenv()
df = pd.read_csv("2021-2022 NBA Player Stats - Regular.csv", encoding="Windows-1252", delimiter=";")
df = df[df['Tm'] != 'TOT']




# Instantiate a LLM
from pandasai.llm.openai import OpenAI
llm = OpenAI()

pandas_ai = PandasAI(llm, conversational=True)

pandas_ai.run(df, prompt='Who is the tallest player in NBA history?')

pandas_ai.run(df, prompt='Who is the coach with the most NBA championships?')

pandas_ai.run(df,"Which player has won the most NBA Finals MVP awards?")
                  
                  
                  
                  
                  

