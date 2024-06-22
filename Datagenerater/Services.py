import sqlite3
from  g4f.client import  Client

client = Client()


def initialize_database():
 # Connect to the SQLite database
 conn = sqlite3.connect('questions.db')
 cursor = conn.cursor()

 # Create the table if it doesn't exist
 cursor.execute('''CREATE TABLE IF NOT EXISTS datasets
  (id INTEGER PRIMARY KEY, prompts TEXT , jsonvalue
  TEXT)''')


prompt = '''
You'll receive input resembling a JSON object or similar, which may define database table columns or be in comma-separated values format.
 Validate the input format accordingly; if it doesn't match, inform the user that only key-value pairs or comma-separated values are accepted. 
 Extract column names from JSON keys or split comma-separated values to identify database columns.
  Generate realistic dummy data for each field type specified . Fetch real images from an online source for any fields designated for images.
  Produce a JSON object containing 5 data points that reflect the defined schema, ensuring each data point adheres to its respective field type and name.
  Here is the input:
  name, email,password
    
'''

model_engine = "gpt-3.5-turbo"
explanation_completions = client.chat.completions.create(
 model=model_engine,
 messages=[
  {"role": "user", "content": f"{prompt}"},
 ],
 max_tokens=1024,
 n=1,
 stop=None,
 temperature=0.2,
)

explanation = explanation_completions.choices[0].message.content
print(explanation)