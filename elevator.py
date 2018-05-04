def elevator(weights, targets, floors, capacity, limit):
	people = list(zip(weights, targets))
	n = len(people)
	in_elevator = []
	current_weight = 0
	stops = 0

	while people:
		# as long as there are people, try to fill
		for i in range(capacity):
			can_add = (len(in_elevator) < capacity) and (current_weight < limit) and (len(people) > 0)
			if can_add:
				person = people.pop(0)
				in_elevator.append(person)
				#print(in_elevator)
				current_weight += person[0]
			else:
				break
		# take the people up
		unique_floors = list(set([person[1] for person in in_elevator]))
		#print(unique_floors)
		stops += len(unique_floors)
		# clear everybody off the elevator
		in_elevator = []
		current_weight = 0
		# stop one more time at the bottom
		stops += 1
			
	return stops



if __name__ == '__main__':
	print(elevator([60, 80, 40], [2, 3, 5], 5, 2, 200))
	print(elevator([40, 40, 10, 80, 20], [3, 3, 3, 3, 3], 3, 5, 200))