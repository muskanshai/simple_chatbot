import json

def load_sample_scenarios():
    # Load the sample scenarios from the JSON file
    with open('data/sample_scenarios.json', 'r') as f:
        return json.load(f)

def demonstrate_chatbot(scenarios):
    # Iterate through each scenario and print the input/expected response
    for scenario in scenarios:
        print(f"Scenario ID: {scenario['scenario_id']}")
        print(f"Input: {scenario['input']}")
        print(f"Expected Response: {scenario['expected_response']}")
        print("-" * 50)

if __name__ == "__main__":
    scenarios = load_sample_scenarios()
    demonstrate_chatbot(scenarios)
