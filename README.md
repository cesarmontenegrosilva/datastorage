**B3 D-1 Data Scraping and Storage**

This script automates the process of downloading and processing transaction data from B3 (the Brazilian Stock Exchange) for D-1 (the previous day). The data is downloaded as a ZIP file, extracted, and then saved in Parquet format for optimized storage and processing.

**Features**

- Automated Data Download: Fetches transaction data for D-1 from B3 using dynamically generated URLs.
- Directory Management: Automatically checks if the target directory exists and creates it if necessary.
- ZIP File Handling: Downloads the ZIP file, extracts the contents, and removes the ZIP file afterward to save space.
- Parquet Conversion: Converts the extracted text data into Parquet format for efficient storage and processing (commented out but easily enabled).

**Requirements**

The following Python libraries are required to run the script:
- bs4
- requests
- datetime (part of the Python standard library)
- os (part of the Python standard library)
- zipfile (part of the Python standard library)
- pyarrow (for saving as Parquet)

You can install the required libraries using pip:

pip install -r requirements.txt

How It Works

1. Get the D-1 Date: The script calculates yesterday's date (D-1) using the datetime module and formats it into a string.
   
2. Build the Download URL: A download URL is dynamically constructed using the D-1 date to fetch transaction data from B3.

3. Download and Save the ZIP File: The script sends a GET request to the B3 server. If the response is successful, the ZIP file is saved to the local directory.

4. Extract the ZIP File: The downloaded ZIP file is extracted, and the text files are saved to the target directory.

5. Convert to Parquet: (Optional) The script can convert the extracted text file into Parquet format for more efficient data storage and faster processing.

6. Fallback for D-2: If the D-1 data is not available, the script automatically tries to download the D-2 (two days ago) data as a fallback.

**Usage**

1. Clone the repository or download the script.
2. Open the script in your preferred Python environment.
3. Modify the diretorio_destino variable to point to your desired download location.
4. Run the script:

python dataStorage.py

The script will download the latest D-1 data, extract it, and save it as a Parquet file in the specified directory.

**Customization**

- Directory Path: Update diretorio_destino to the path where you want to save the downloaded and extracted files.
- Enable Parquet Conversion: Uncomment the lines that save the extracted data in Parquet format using pandas.to_parquet().

Example Output

Arquivo ZIP baixado com sucesso: [your_directory]/cotacoes_b3_d1_2024-10-04.zip

Arquivo descompactado com sucesso no diretório: [your_directory]

Arquivo ZIP apagado: [your_directory]/cotacoes_b3_d1_2024-10-04.zip

Arquivo TXT extraído: 04-10-2024_NEGOCIOSAVISTA.txt

Arquivo Parquet salvo com sucesso: [your_directory]/NEGOCIOSAVISTA_2024-10-04.parquet

**License**

This project is licensed under the MIT License - see the LICENSE file for details.
