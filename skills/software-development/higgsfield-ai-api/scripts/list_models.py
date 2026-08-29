import json
import sys

def list_models(spec_path):
    """
    Parses a Higgsfield OpenAPI spec and prints all valid model endpoint paths.
    """
    try:
        with open(spec_path, 'r') as f:
            spec = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{spec_path}' was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{spec_path}'.")
        sys.exit(1)

    print("Available Higgsfield AI Model Endpoints:")
    print("---------------------------------------")
    
    count = 0
    if 'paths' in spec:
        for path in spec['paths']:
            if path.startswith('/higgsfield-ai/') and 'post' in spec['paths'][path]:
                print(path)
                count += 1
    
    if count == 0:
        print("No model endpoints found in the specification.")
    else:
        print(f"\nFound {count} models.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python list_models.py <path_to_openapi.json>")
        sys.exit(1)
    
    list_models(sys.argv[1])
