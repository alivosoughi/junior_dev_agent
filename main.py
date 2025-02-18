"""
Main entry point for the Automated Developer Agent.
"""

import sys
from auto_dev_agent.agent import AutomatedDeveloperAgent

def main():
    """
    Main function to run the Automated Developer Agent in a loop.
    """
    print("========== Automated Developer Agent ==========")
    print("Enter a high-level task (e.g. 'Implement prime factor function'):")
    user_task = sys.stdin.readline().strip()
    
    # Instantiate our agent
    agent = AutomatedDeveloperAgent()
    
    # Kick off the main workflow
    agent.run(user_task)

    print("All done! Check the output or logs for details.")

if __name__ == "__main__":
    main()
