class Event:
    """
    A class representing an event with a name, date, and participant count.
    """
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count to 0

    def add_participant(self):
        """
        Increases the participant count by 1.
        """
        self.participant_count += 1

    def get_participant_count(self):
        """
        Returns the current number of participants.
        """
        return self.participant_count

# Example usage
event1 = Event("Concert", "2024-05-10")

# Add some participants
event1.add_participant()
event1.add_participant()
event1.add_participant()

# Get the participant count
num_participants = event1.get_participant_count()

print(f"Event: {event1.name} - Participants: {num_participants}")