# bolop CANBus

A Python-based GUI application designed primarily for cleaning and filtering event data from SavvyCAN logs by comparing them with noise data using CSV files. The application removes matching rows from the event data based on specific columns. While it is tailored for SavvyCAN data, it can also be used with other similar CSV files if they follow the same structure and standards.

## Features

- **Noise Removal**: Compare two CSV files (noise and event data) and remove matching rows from the event data.
- **CSV File Selection**: Easily select CSV files using the GUI.
- **Results Display**: Shows both the original and cleaned data in a terminal-style window within the application.
- **Export Cleaned Data**: Export the cleaned event data to a new CSV file.
- **Reset Functionality**: Reset the application for new inputs.
- **Responsive Layout**: The interface automatically adjusts to window resizing.

## Designed for SavvyCAN Data

This tool was initially built to work with SavvyCAN data, which logs CAN bus data in CSV format. If your CSV files follow a similar structure with columns such as `ID`, `D1` to `D8`, you can use this tool to clean and filter other types of CAN bus or related data.

### Requirements for Other CSV Files

- The CSV files should have columns `ID`, `D1`, `D2`, `D3`, `D4`, `D5`, `D6`, `D7`, and `D8`.
- Data types should match (i.e., strings in the `ID` and data columns).

As long as these standards are maintained, the application can be used with other CSV files beyond SavvyCAN.

## Installation

### Prerequisites

- Python 3.x
- `pandas` library
- `tkinter` (included in Python standard library)

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/bolop-canbus.git
cd bolop-canbus
```

### Step 2: Install the required dependencies

Ensure you have `pandas` installed. You can install it via `pip`:

```bash
pip install pandas
```

### Step 3: Run the application

Run the program with Python:

```bash
python ui.py
```

## How to Use

1. **Select the Noise File**: Click on the "Select the noise file" button to choose a CSV file containing noise data.
2. **Select the Check File**: Click on the "Select the check file" button to choose the event data CSV file.
3. **Check and Clean**: Click the "Let's check" button to compare the event file with the noise file and remove any matching rows.
4. **View Results**: The cleaned data will be displayed in the result window inside the app.
5. **Export Data**: Click on "Export CSV" to save the cleaned event data as a CSV file.
6. **Reset**: Click the "Reset" button to clear the results and start with new files.

## File Structure

```bash
.
├── ui.py            # Main Python file containing the application code
├── README.md        # This README file
└── requirements.txt # Optional: List of Python dependencies
```

## Screenshots

![Screenshot 2024-09-06 203043](https://github.com/user-attachments/assets/18022681-db0f-46dd-91c9-084da5c27513)

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.

