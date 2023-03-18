import pandas as pd
from flask import Flask, render_template

# file path to sample data source
SAMPLE_EXCEL_FILE_PATH = 'data/fedora-release.xlsx'

# Flask App
app = Flask(__name__)

# load data from Excel file
def load_data_from_excel(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath)
    return df

@app.route('/')
def index():
    df = load_data_from_excel(SAMPLE_EXCEL_FILE_PATH)
    return render_template('base_table.html', title='Fedora Releases',
                           df=df)


if __name__ == '__main__':
    app.run()
