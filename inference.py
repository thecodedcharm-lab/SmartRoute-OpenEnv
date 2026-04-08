import random
from delivery_env import DeliveryEnv
from grader import grade_easy, grade_medium, grade_hard

def run_task(packages, grader):

    env = DeliveryEnv(packages=packages)

    print("[START]")

    state = env.reset()
    done = False
    deliveries = 0

    while not done:

        action = random.randint(0,4)

        state, reward, done = env.step(action)

        if reward >= 1:
            deliveries += 1

        print("[STEP]", state, reward)

    score = grader(deliveries)

    print("[END]")
    print("score:", score)

    return score


def main():

    print("Running Easy Task")
    run_task(3, grade_easy)

    print("Running Medium Task")
    run_task(6, grade_medium)

    print("Running Hard Task")
    run_task(10, grade_hard)


if __name__ == "__main__":
    main()
