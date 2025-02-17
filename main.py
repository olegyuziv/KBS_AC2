
import json


def load_input_data(file_path):
    """Loads input data from a JSON file."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        print("[INFO] Input data loaded successfully from", file_path)
        return data
    except FileNotFoundError:
        print("[ERROR] JSON file not found. Please check the file path.")
        return None
    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON format. Please check the file contents.")
        return None


def main():
    """Main function to initialize the expert system."""


    input_file = "info.json"
    input_data = load_input_data(input_file)

    if input_data is None:
        print("[ERROR] Exiting due to input file error.")
        return


    print("[INFO] Expert System is Ready!")
    print("[INFO] Data successfully loaded, now processing...")

    # TO DO: Implement rule processing functions here


if __name__ == "__main__":
    main()
