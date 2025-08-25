def main():
    print("=== Career Guidance App ===")
    try:
        marks = float(input("Enter your 12th Marks (%): "))
    except ValueError:
        print("Please enter a valid number for marks.")
        return

    stream = input("Enter Stream (Science/Commerce/Arts): ").strip()
    print("Select your interests (comma separated): Tech, Business, Arts")
    interests_input = input("Enter interests: ")
    interests = [i.strip().capitalize() for i in interests_input.split(',')]

    if stream.capitalize() == "Science" and marks >= 85 and "Tech" in interests:
        recommendation = "Recommended: Computer Engineering or Data Science.\nTop colleges: IITs.\nAvg starting salary: ₹8-12 LPA."
    elif stream.capitalize() == "Commerce" and marks >= 70 and "Business" in interests:
        recommendation = "Recommended: BBA or Accounting.\nTop colleges: Delhi University.\nAvg starting salary: ₹5-8 LPA."
    elif stream.capitalize() == "Arts" and marks >= 60 and "Arts" in interests:
        recommendation = "Recommended: Graphic Design or Journalism.\nAvg starting salary: ₹4-6 LPA."
    else:
        recommendation = "Consider vocational training, diplomas, or short courses to improve your options."

    print("\n" + recommendation)

if __name__ == "__main__":
    main()
