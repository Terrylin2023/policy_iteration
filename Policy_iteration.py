intened_probability = float(input("Enter the intended probability: "))
other_probability = float(input("Enter the other probability: "))
reward = float(input("Enter the reward: "))
discount = float(input("Enter the discount: "))
Value=[0,0,0,0]

def policy_iteration(intened_probability, other_probability, reward, discount):
    up=int(input("Enter the up value: "))
    down=int(input("Enter the down value: "))
    left=int(input("Enter the left value: "))
    right=int(input("Enter the right value: "))
    for i in range(4):
        if i == 0:
            print("Action Up: ")
            Value[i] = intened_probability * (reward + discount * up) + other_probability * (reward + discount * left)+ other_probability * (reward + discount * right)+other_probability * (reward + discount * down)
            print("Value: ", intened_probability * (reward + discount * up) + other_probability * (reward + discount * left)+ other_probability * (reward + discount * right)+other_probability * (reward + discount * down))
        elif i == 1:
            print("Action Down: ")
            Value[i] = intened_probability * (reward + discount * down) + other_probability * (reward + discount * left)+ other_probability * (reward + discount * right)+other_probability * (reward + discount * up)
            print("Value: ", intened_probability * (reward + discount * down) + other_probability * (reward + discount * left)+ other_probability * (reward + discount * right)+other_probability * (reward + discount * up))
        elif i == 2:
            print("Action Left: ")
            Value[i] = intened_probability * (reward + discount * left) + other_probability * (reward + discount * up)+ other_probability * (reward + discount * down)+other_probability * (reward + discount * right)
            print("Value: ", intened_probability * (reward + discount * left) + other_probability * (reward + discount * up)+ other_probability * (reward + discount * down)+other_probability * (reward + discount * right))
        elif i == 3:
            print("Action Right: ")
            Value[i] = intened_probability * (reward + discount * right) + other_probability * (reward + discount * up)+ other_probability * (reward + discount * down)+other_probability * (reward + discount * left)
            print("Value: ", intened_probability * (reward + discount * right) + other_probability * (reward + discount * up)+ other_probability * (reward + discount * down)+other_probability * (reward + discount * left))
    
    # print the biggest value with the direction
    x = Value.index(max(Value))
    if x == 0:
        print("The biggest value is: ", max(Value))
        print("The direction is Up")
    elif x == 1:
        print("The biggest value is: ", max(Value))
        print("The direction is Down")
    elif x == 2:
        print("The biggest value is: ", max(Value))
        print("The direction is Left")
    elif x == 3:
        print("The biggest value is: ", max(Value))
        print("The direction is Right")
    

    

   

policy_iteration(intened_probability, other_probability, reward, discount)
