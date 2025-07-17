class SDLC:
    def __init__(self, project_name):
        self.project_name = project_name
        self.requirements = []
        self.design = {}
        self.implementation = ""
        self.testing = {}
        self.deployment = False
        self.maintenance = False

    def requirements_gathering(self):
        print(f"Requirements for {self.project_name}:")
        new_requirements = int(input("Enter the number of requirements: "))
        for i in range(new_requirements):
            requirement = input(f"Enter requirement {i+1}: ")
            self.requirements.append(requirement)
        print("Requirements gathered successfully!")

    def design_phase(self):
        print(f"Design for {self.project_name}:")
        self.design["architecture"] = input("Enter the architecture: ")
        self.design["components"] = input("Enter the components: ")
        print("Design created successfully!")

    def implementation_phase(self):
        print(f"Implementation for {self.project_name}:")
        self.implementation = input("Enter the implementation details: ")
        print("Implementation completed successfully!")

    def testing_phase(self):
        print(f"Testing for {self.project_name}:")
        self.testing["test_cases"] = input("Enter the test cases: ")
        self.testing["test_result"] = input("Enter the results: ")
        print("Testing result successfully!")

    def deployment_phase(self):
        print(f"Deployment for {self.project_name}:")
        self.deployment = True
        print("Deployment completed successfully!")

    def maintenance_phase(self):
        print(f"Maintenance for {self.project_name}:")
        self.maintenance = True
        print("Maintenance completed successfully!")

    def display_sdlc(self):
        print(f"SDLC for {self.project_name}:")
        print("Requirements:")
        for requirement in self.requirements:
            print(requirement)
        print("Design:")
        print(self.design)
        print("Implementation:")
        print(self.implementation)
        print("Testing:")
        print(self.testing)
        print("Deployment:")
        print(self.deployment)
        print("Maintenance:")
        print(self.maintenance)

def main():
    project_name = input("Enter the project name: ")
    sdlc = SDLC(project_name)
    while True:
        print("SDLC Menu:")
        print("1. Requirements")
        print("2. Design")
        print("3. Implementation")
        print("4. Testing")
        print("5. Deployment")
        print("6. Maintenance")
        print("7. Display SDLC")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            sdlc.requirements_gathering()
        elif choice == "2":
            sdlc.design_phase()
        elif choice == "3":
            sdlc.implementation_phase()
        elif choice == "4":
            sdlc.testing_phase()
        elif choice == "5":
            sdlc.deployment_phase()
        elif choice == "6":
            sdlc.maintenance_phase()
        elif choice == "7":
            sdlc.display_sdlc()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
