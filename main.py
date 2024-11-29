class Question:
	def __init__(self, setting: str, question: str, answer_filter: tuple = None):
		self.setting = setting
		self.question = question
		self.answer_filter = answer_filter

	def ask(self) -> str:
		if self.setting:
			print(self.setting)
		while True:
			answer = input(self.question + "\t").lower().strip()
			if not answer:
				print("Response cannot be blank!")
				continue

			if self.answer_filter and answer not in [x.lower() for x in self.answer_filter]:
				print(f"Response must be one of the following: [{', '.join(self.answer_filter)}]")
				continue
			return answer
		return "ERROR"


def main():
	char_name = Question("[Character creation]", "What is your name?").ask().capitalize()
	town = Question("", "What town do you live in?").ask().capitalize()
	favorite_song = Question("", "What id your favorite song?").ask().capitalize()
	favorite_food = Question("", "What is your favorite breakfast?").ask()
	job = Question("", "Where is your profession?").ask()
	print("\n")
	answer_door = Question(
			f"{char_name} is a {job} who lives in the sleepy town of {town}.\nSuddenly an alarm playing {favorite_song} wakes them up in an instant.\n{char_name} goes downstairs to prepare their favorite breakfast: {favorite_food}.\nIn the middle of prepping their meal, {char_name} hears a knock at the door!",
			"Do you answer the door? (y/n)",
			("y", "n")
	).ask()

	if answer_door == "n":
		print("Following your therapist's advice, you ignore the man knocking on the door because he is not real.\nHowever it was actually the IRS. Go to jail, do not collect $200.\n(ENDING 1)")
		return

	help_friend = Question(
			f"It's {char_name} neighbor Jim.\nThey explain that their car won't start.\n {char_name} was always a car guy so this fix surely won't be an issue.",
			"Do you help Jim? (y/n)",
			("y", "n")
	).ask()

	if help_friend == "n":
		print(f"In the middle of your sentence, Jim slams the door in your face.\nIt is possible that he was overcome with emotion because he has nowhere else to go to.\nYou continue with your day and make it to your {job} job on time.\n(ENDING 2)")
		return

	print(f"{char_name} agrees to help Jim with their car.\nIt took longer than expected to fix, but the car now starts!\nBecause of this however, {char_name} was late to work *again* and got a talking-to from their boss.")




if __name__ == '__main__':
	main()
